#!/usr/bin/env python3
"""Build standalone Meishe SDK knowledge artifacts from an external Demo."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

from coverage_summary import write_coverage_artifacts
from extract_sdk_signatures import extract_signatures

import sys
for _stream in (sys.stdout, sys.stderr):
    if _stream is not None and hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

DIRECT_MEMBER_ROW_RE = re.compile(r"^\| `([^`]+)` \| ([^|]+) \| (\d+) \|")
API_CLASS_ROW_RE = re.compile(
    r"^\| `([^`]+)` \| `([^`]+)` \| (\d+) \| `([^`]+)` \|"
)
TOKEN_ROW_RE = re.compile(r"^\| `([^`]+)` \| (\d+) \|")
PRIORITY_CLASS_ROW_RE = re.compile(
    r"^\| `([^`]+)` \| `([^`]+)` \| `?(P[0-3])`? \|"
)
FEATURE_PRIORITY_ROW_RE = re.compile(
    r"^\| `([^`]+)` [^|]*\| `?(P(?:0/P1|[0-3]))`? \|"
)
MEMBER_PRIORITY_ROW_RE = re.compile(r"^\| `([^`]+)` \| `?(P[0-3])`? \|")

SCHEMA_VERSION = 2
IMPLEMENTATION_STATES = {
    "evidence_only",
    "contract_only",
    "compiled_unit",
    "generated_module",
    "runtime_verified",
}
LIFECYCLE_HOOKS = {
    "sdk_init",
    "activity_create",
    "timeline_created",
    "live_window_bound",
    "asset_installed",
    "before_structural_mutation",
    "after_mutation_refresh",
    "destroy",
}

API_DOMAIN_CONTRACTS = {
    "core-runtime": {
        "title": "SDK runtime and process lifecycle",
        "module_ids": ["app-runtime"],
    },
    "media-inspection": {
        "title": "Media metadata, frames, and icons",
        "module_ids": ["media-import", "cover-maker", "still-image-export"],
    },
    "timeline-editing": {
        "title": "Timeline, track, and clip structure",
        "module_ids": ["timeline-state-store", "clip-editor"],
    },
    "preview-playback": {
        "title": "LiveWindow preview, playback, seek, and coordinates",
        "module_ids": ["timeline-preview", "timeline-ui"],
    },
    "capture-recording": {
        "title": "Camera capture, device controls, and recording",
        "module_ids": ["capture-camera"],
    },
    "effect-parameters": {
        "title": "Effects, masks, parameters, and keyframes",
        "module_ids": ["filter-editor", "animation-editor", "mask-editor", "background-editor"],
    },
    "caption-editing": {
        "title": "Caption typography, spans, transforms, and timing",
        "module_ids": ["caption-editor", "compound-caption-editor", "flip-caption"],
    },
    "sticker-editing": {
        "title": "Animated sticker transforms, timing, and animation",
        "module_ids": ["sticker-editor"],
    },
    "asset-packages": {
        "title": "Asset package constants, metadata, status, and install support",
        "module_ids": ["asset-package-service"],
    },
    "audio-editing": {
        "title": "Audio clips, transitions, effects, and volume",
        "module_ids": ["music-editor", "audio-equalizer"],
    },
    "template-workflows": {
        "title": "Template, CutSame, Mimo, and theme authoring",
        "module_ids": ["template-engine", "template-editor", "cutsame-template", "mimo-template", "theme-editor"],
    },
    "ar-beauty-segmentation": {
        "title": "AR scene, beauty, makeup, models, and segmentation",
        "module_ids": ["ar-scene", "beauty-camera", "makeup-service", "segmentation-keying"],
    },
    "render-core": {
        "title": "Effect render core and OpenGL texture processing",
        "module_ids": ["filter-editor", "superzoom-ai"],
    },
    "timeline-ui": {
        "title": "Thumbnail sequence and timeline interaction UI",
        "module_ids": ["timeline-ui"],
    },
    "media-conversion": {
        "title": "Media conversion, passthrough, and reverse generation",
        "module_ids": ["quick-splicing", "template-engine"],
    },
    "particle-effects": {
        "title": "Particle descriptors, emitters, and coordinate mapping",
        "module_ids": ["particle-effects"],
    },
    "transition-editing": {
        "title": "Video and audio transition configuration",
        "module_ids": ["transition-editor"],
    },
    "export-compile": {
        "title": "Compile configuration, callbacks, and output",
        "module_ids": ["export-compile"],
    },
}

API_OWNER_DOMAINS = {
    "NvsARSceneManipulate": ["ar-beauty-segmentation"],
    "NvsAVFileInfo": ["media-inspection"],
    "NvsAnimatedSticker": ["sticker-editing"],
    "NvsAssetPackageManager": ["asset-packages"],
    "NvsAssetPackageParticleDescParser": ["asset-packages", "particle-effects"],
    "NvsAudioClip": ["audio-editing"],
    "NvsAudioFx": ["audio-editing"],
    "NvsAudioTrack": ["audio-editing", "transition-editing"],
    "NvsCaptureAudioFx": ["capture-recording", "audio-editing"],
    "NvsCaptureSceneInfo": ["capture-recording", "ar-beauty-segmentation"],
    "NvsCaptureVideoFx": ["capture-recording", "effect-parameters"],
    "NvsEffectRenderCore": ["render-core"],
    "NvsEffectSdkContext": ["ar-beauty-segmentation"],
    "NvsExpressionParam": ["effect-parameters"],
    "NvsFx": ["effect-parameters"],
    "NvsFxDescription": ["effect-parameters"],
    "NvsIconGenerator": ["media-inspection", "timeline-ui"],
    "NvsLiveWindow": ["preview-playback"],
    "NvsLiveWindowExt": ["preview-playback"],
    "NvsMakeupEffectInfo": ["ar-beauty-segmentation"],
    "NvsMaskRegionInfo": ["effect-parameters"],
    "NvsMediaFileConvertor": ["media-conversion"],
    "NvsMultiThumbnailSequenceView": ["timeline-ui"],
    "NvsObject": ["template-workflows"],
    "NvsParticleSystemContext": ["particle-effects"],
    "NvsPassthroughConvertor": ["media-conversion"],
    "NvsStreamingContext": ["core-runtime"],
    "NvsTimeline": ["timeline-editing"],
    "NvsTimelineVideoFx": ["effect-parameters"],
    "NvsVideoClip": ["timeline-editing"],
    "NvsVideoFrameInfo": ["media-inspection", "render-core"],
    "NvsVideoFrameRetriever": ["media-inspection"],
    "NvsVideoFx": ["effect-parameters"],
    "NvsVideoResolution": ["timeline-editing", "export-compile"],
    "NvsVideoStreamInfo": ["media-inspection"],
    "NvsVideoTrack": ["timeline-editing"],
    "NvsVideoTransition": ["transition-editing"],
}

CAPTION_OBJECT_OWNERS = {
    "NvsBodyOpacitySpan",
    "NvsCaption",
    "NvsCaptionSpan",
    "NvsClipCaption",
    "NvsClipCompoundCaption",
    "NvsColorSpan",
    "NvsFontFamilySpan",
    "NvsFontSizeRatioSpan",
    "NvsItalicSpan",
    "NvsNormalTextSpan",
    "NvsOpacitySpan",
    "NvsOutlineColorSpan",
    "NvsOutlineOpacitySpan",
    "NvsOutlineWidthSpan",
    "NvsRendererIdSpan",
    "NvsShadowOpacitySpan",
    "NvsTimelineCaption",
    "NvsTimelineCompoundCaption",
    "NvsTrackCaption",
    "NvsUnderlineSpan",
    "NvsVideoEffectCompoundCaption",
}

STICKER_OBJECT_OWNERS = {
    "NvsClipAnimatedSticker",
    "NvsTimelineAnimatedSticker",
    "NvsVideoEffectAnimatedSticker",
}

BLUEPRINT_APP_TEMPLATES = {
    "camera-plus-editor": "camera-plus-editor",
    "template-mimo-cutsame-app": "template-mimo-cutsame-app",
    "pip-editor": "pip-editor",
    "quick-splicing-app": "quick-splicing-app",
    "full-sdk-demo": "full-sdk-demo",
    "incremental-integration": "incremental-integration",
}

MODULE_TEMPLATE_FEATURE_ADDITIONS = {
    "template-engine": ["template-workflows"],
    "template-editor": ["template-workflows", "preview-playback"],
    "cutsame-template": ["template-workflows", "preview-playback"],
    "mimo-template": ["template-workflows", "preview-playback"],
    "theme-editor": ["template-workflows"],
    "url-media-import": ["media-workflows"],
    "photo-album": ["media-workflows"],
    "theme-shoot": ["media-workflows"],
    "dou-video-workflow": ["media-workflows"],
    "boomrang-capture": ["media-workflows"],
    "cover-maker": ["media-workflows"],
    "sequence-nesting": ["media-workflows"],
    "livephoto-editor": ["media-workflows"],
    "still-image-export": ["media-workflows"],
    "quick-splicing": ["media-workflows"],
}

MODULE_REQUIRED_ADDITIONS = {
    "template-engine": ["media-import"],
    "livephoto-editor": ["export-compile"],
}

MODULE_RENDER_UNIT_EXCLUSIONS = {
    "template-engine": {
        "java.timeline.create-template",
        "java.timeline.create-template-configured",
        "java.timeline.create-template-with-flags",
    },
}

TEMPLATE_RECIPE_ADDITIONS = [
    {
        "id": "template-prepare-footage",
        "title": "Template Prepare Footage",
        "priority": "P1",
        "requires": ["asset-package-service", "media-import"],
        "provides": ["validated template descriptors", "template footage mapping"],
        "simple_code_refs": ["demo-simple-snippets-template-mimo-cutsame.md"],
        "guards": [
            "template package installed",
            "replacement file count matches replaceable footage ids",
            "reverse media generated only for descriptors with needReverse",
        ],
        "resources": ["R0", "R1", "R4", "R10"],
        "lifecycle": [
            "install template package",
            "query descriptors",
            "map replacement media",
            "generate required reverse media",
            "validate and build templateFootageInfo",
        ],
    },
    {
        "id": "cutsame-replace-export",
        "title": "CutSame Replace Export",
        "priority": "P1",
        "requires": ["template-engine"],
        "provides": ["CutSame replacement timeline", "CutSame preview and export"],
        "simple_code_refs": [
            "demo-simple-snippets-template-mimo-cutsame.md",
            "demo-simple-snippets-preview-export.md",
        ],
        "guards": [
            "select the CutSame timeline creation branch only",
            "template footage mapping validates before timeline creation",
            "stop the engine before reconnecting preview or export",
        ],
        "resources": ["R0", "R1", "R4", "R10"],
        "lifecycle": [
            "prepare footage",
            "create CutSame timeline",
            "replace template captions",
            "connect preview",
            "export",
            "release reverse convertor",
        ],
    },
    {
        "id": "mimo-replace-export",
        "title": "Mimo Replace Export",
        "priority": "P1",
        "requires": ["app-runtime", "asset-package-service", "media-import"],
        "provides": ["Mimo JSON-driven timeline", "Mimo preview and export"],
        "simple_code_refs": [
            "demo-simple-snippets-template-mimo-cutsame.md",
            "demo-simple-snippets-preview-export.md",
        ],
        "guards": [
            "Mimo packages use info.json and are not SDK .template packages",
            "install every referenced Mimo child package before timeline construction",
            "selected media satisfies every shot duration and reverse/speed requirement",
            "video FPS and audio resolution are valid",
            "stop the engine before reconnecting preview or export",
        ],
        "resources": ["R0", "R1", "R4", "R10"],
        "lifecycle": [
            "download and extract Mimo archive",
            "parse info.json",
            "install child packages",
            "map shot media",
            "build Mimo tracks, effects, transitions, captions, and music",
            "connect preview",
            "export",
        ],
    },
]

EDITOR_RECIPE_ADDITIONS = [
    {
        "id": "editor-session-orchestration",
        "title": "Editor Session Orchestration",
        "priority": "P1",
        "requires": [
            "media-import",
            "timeline-state-store",
            "timeline-preview",
            "export-compile",
        ],
        "provides": [
            "thin Activity lifecycle",
            "owned editor Timeline session",
            "delegated edit command routing",
        ],
        "simple_code_refs": ["demo-validated-editor-architecture.md"],
        "guards": [
            "Activity delegates SDK ownership to MeisheEditorSessionController",
            "structural mutation stops playback and refreshes the connected LiveWindow",
            "callbacks are cleared before an editor-owned Timeline is removed",
        ],
        "resources": ["R0", "R1", "R3"],
        "lifecycle": [
            "initialize editor coordinator",
            "open Timeline session",
            "bind playback and compile callbacks",
            "delegate commands and child modules",
            "persist project state",
            "release the session on destroy",
        ],
    },
    {
        "id": "editor-project-v3-ownership",
        "title": "Editor Project V3 And Timeline Ownership",
        "priority": "P1",
        "requires": ["app-repository", "timeline-state-store"],
        "provides": [
            "atomic version-3 editor project",
            "stable object identifiers",
            "namespaced project extensions",
            "explicit editor-owned or host-owned Timeline policy",
        ],
        "simple_code_refs": ["demo-validated-editor-architecture.md"],
        "guards": [
            "persist project JSON under filesDir/meishe-projects/<projectId>/project.json",
            "migrate legacy SharedPreferences projects before Timeline restoration",
            "host-owned Timelines are never removed by the generated editor",
            "host-safe mode blocks structural mutation and editor-feature rebuild unless the host opts in",
            "process restoration rebuilds SDK objects and does not persist undo history",
        ],
        "resources": ["R0", "R1", "R3"],
        "lifecycle": [
            "load or migrate version-3 project",
            "acquire editor-owned or host-owned Timeline",
            "restore structure and editor-owned descriptors",
            "persist atomic project snapshots after mutation",
            "release only editor-owned Timeline objects",
        ],
    },
]

RECIPE_ADDITIONS = [*TEMPLATE_RECIPE_ADDITIONS, *EDITOR_RECIPE_ADDITIONS]

RECIPE_CONTRACT_UPDATES = {
    "effect-sdk-init": {
        "guards": [
            "load only models required by the selected effect capability",
            "resolve model files from samples/android/SdkDemo/app/src/main/assets/facemode in the official Android LTS face package",
            "preserve facemode/ms and facemode/common relative structure",
        ],
        "resources": ["R0", "R8", "R9"],
        "demo_evidence": [
            "official-sdk-download-resources.md",
            "demo-simple-snippets-ar-makeup-segmentation.md",
        ],
    },
    "template-replace-export": {
        "requires": ["template-engine"],
        "provides": ["template replacement timeline", "template preview and export"],
        "guards": [
            "select the standard template timeline creation branch only",
            "template footage mapping validates before timeline creation",
            "stop the engine before reconnecting preview or export",
        ],
        "lifecycle": [
            "prepare footage",
            "create standard template timeline",
            "replace template captions",
            "connect preview",
            "export",
            "release reverse convertor",
        ],
    },
    "bundled-material-install": {
        "title": "External Local Material Install",
        "category": "assets-packages",
        "aliases": [
            "external local material install",
            "offline material catalog",
            "本地素材安装",
            "内置素材目录",
            "官网SDK素材目录",
            "下载SDK人脸版本",
        ],
        "requires": ["asset-package-service"],
        "resources": ["R0", "R4"],
        "demo_evidence": [
            "asset-center-workflow.md",
            "default-sample-assets.md",
            "official-sdk-download-resources.md",
        ],
        "provides": [
            "copied external local material catalog",
            "installed local package id",
            "registered external font family",
        ],
        "guards": [
            "do not embed a material endpoint, request client, authentication, or download implementation",
            "install only package paths listed by the copied external local catalog",
            "register fonts from an app-private copied file",
            "direct service-interface and license-acquisition questions to Meishe business",
        ],
        "lifecycle": [
            "open bundled catalog",
            "select a local material family",
            "install package or register font on the SDK thread",
            "return package id, font family, or local path to the owning feature",
        ],
    },
}
for _recipe_addition in RECIPE_ADDITIONS:
    RECIPE_CONTRACT_UPDATES[_recipe_addition["id"]] = _recipe_addition

MODULE_CONTRACT_UPDATES = {
    "segmentation-keying": {
        "guards": [
            "required segmentation models are selected from the official Android LTS face package",
            "keep segmentation controls disabled until the selected model initializes successfully",
        ],
        "demo_evidence": [
            "official-sdk-download-resources.md",
            "demo-simple-snippets-ar-makeup-segmentation.md",
        ],
    },
    "superzoom-ai": {
        "guards": [
            "required face models are selected from samples/android/SdkDemo/app/src/main/assets/facemode/ms",
            "keep SuperZoom controls disabled until model initialization succeeds",
        ],
        "demo_evidence": [
            "official-sdk-download-resources.md",
            "demo-simple-snippets-ar-makeup-segmentation.md",
        ],
    },
    "asset-center-service": {
        "title": "External local material catalog",
        "category": "assets-packages",
        "aliases": [
            "asset center",
            "material center",
            "external material catalog",
            "offline material samples",
            "素材中心",
            "本地素材",
            "内置素材示例",
            "官网SDK素材目录",
            "下载SDK人脸版本",
        ],
        "integration_modes": ["new-app", "incremental", "api-only"],
        "permissions": [],
        "resources": ["R0", "R4"],
        "api_recipes": ["bundled-material-install"],
        "demo_evidence": [
            "asset-center-workflow.md",
            "default-sample-assets.md",
            "official-sdk-download-resources.md",
        ],
        "provides": [
            "copied external local material catalog",
            "offline package install and upgrade",
            "external font copy and registration",
            "package id result contract for editor and capture modules",
        ],
        "guards": [
            "no material service URL, request client, authentication contract, or download code is generated",
            "SDK package installation runs on the Android main thread",
            "font bytes are copied to app-private storage before registration",
            "large models are selected from samples/android/SdkDemo/app/src/main/assets/facemode in the official Android LTS face package",
            "copy only requested Demo material families from the official package",
            "service-interface and license-acquisition questions are referred to Meishe business",
        ],
        "conflicts": [
            "do not add Demo service addresses or service request implementations",
            "do not apply package ids before install or upgrade succeeds",
            "do not claim a missing standard template, Mimo, or CutSame package is bundled",
        ],
        "lifecycle": [
            "open bundled catalog",
            "filter local entries by material family",
            "install or upgrade selected package or register selected font",
            "return and apply package id or font family",
        ],
    },
    "permission-gates": {
        "integration_modes": ["new-app", "incremental", "api-only"],
    },
    "media-import": {
        "integration_modes": ["new-app", "incremental", "api-only"],
    },
    "app-repository": {
        "integration_modes": ["new-app", "incremental", "api-only"],
        "provides": [
            "shared app state",
            "latest project lookup",
            "atomic version-3 project persistence",
            "stable object identifiers",
            "namespaced module extension state",
            "legacy SharedPreferences project migration",
        ],
        "guards": [
            "persist only app-owned readable media paths",
            "write project state atomically under filesDir/meishe-projects/<projectId>/project.json",
            "preserve unknown extension namespaces during migration and save",
            "do not serialize NvsTimeline, track, clip, or LiveWindow object references",
        ],
        "lifecycle": [
            "load or migrate before Timeline population",
            "assign stable ids before descriptor association",
            "save a full project snapshot after successful mutation",
            "save before Activity teardown",
        ],
    },
    "timeline-state-store": {
        "api_recipes": ["timeline-build"],
        "provides": [
            "NvsTimeline",
            "tracks",
            "clips",
            "stable clip identity",
            "project state remapping after split, move, or delete",
        ],
        "guards": [
            "timeline factory may return null",
            "stop playback or export before structural rebuild",
            "persist app-owned paths, source trim ranges, speed, and image-motion state",
            "preserve stable ids when clips move and explicitly remap ids after split or delete",
            "do not clear or remove host-owned Timeline objects by default",
        ],
        "lifecycle": [
            "acquire Timeline ownership",
            "create or accept Timeline",
            "append ordered image and video clips",
            "restore structural state and stable ids",
            "remap project descriptors after structural mutation",
        ],
    },
    "timeline-preview": {
        "api_recipes": ["connect-livewindow", "editor-session-orchestration"],
        "guards": [
            "timeline/live window not null",
            "seek after mutation",
            "callbacks update UI",
            "MeisheEditorSessionController owns playback and compile callback cleanup",
        ],
        "lifecycle": [
            "open editor session",
            "connect timeline",
            "register callbacks",
            "seek/play and refresh",
            "clear callbacks on teardown",
        ],
    },
    "editor-shell": {
        "integration_modes": ["new-app", "incremental", "api-only"],
        "api_recipes": [
            "apply-refresh-editor-child",
            "editor-session-orchestration",
            "editor-project-v3-ownership",
        ],
        "provides": [
            "editor screen",
            "module toolbar",
            "child result apply and refresh",
            "version-3 project restore and undo/redo",
            "editor-owned and host-owned integration modes",
        ],
        "guards": [
            "do not enter without media seed unless explicit empty project",
            "Activity does not directly own or mutate SDK Timeline objects",
            "refresh live window after child mutation",
            "clear only editor-owned SDK objects before descriptor restore",
            "associate descriptors by stable object id rather than mutable clip index",
            "host-owned Timeline mutation and feature rebuild require explicit host permission",
            "removeTimeline is valid only for EDITOR_OWNED sessions",
        ],
        "lifecycle": [
            "enter from media import",
            "create MeisheEditorCoordinator",
            "load or migrate version-3 project",
            "open MeisheEditorSessionController with explicit Timeline ownership",
            "route UI commands to focused controllers",
            "persist atomic project snapshots on pause and state save",
            "release only editor-owned Timeline objects on destroy",
        ],
    },
    "template-engine": {
        "api_recipes": ["template-prepare-footage"],
        "provides": [
            "template descriptors",
            "validated template footage mapping",
            "required reverse footage",
        ],
        "guards": [
            "template package installed",
            "replacement paths are readable",
            "reverse media is generated only when needReverse is true",
        ],
        "lifecycle": [
            "install template",
            "query and flatten descriptors",
            "map footage by replace id",
            "generate required reverse footage",
            "validate templateFootageInfo",
        ],
    },
    "capture-camera": {
        "integration_modes": ["new-app", "incremental", "api-only"],
    },
    "template-editor": {
        "requires": ["template-engine"],
        "api_recipes": ["template-replace-export"],
        "integration_modes": ["new-app", "incremental", "api-only"],
        "resources": ["R0", "R1", "R3", "R4", "R10"],
        "provides": ["standard template replacement UI, preview, and export"],
        "guards": [
            "standard template branch is selected",
            "all footage replacements validate before timeline creation",
            "LiveWindow is created only after SDK initialization",
        ],
        "lifecycle": [
            "prepare footage",
            "create standard template timeline",
            "replace captions",
            "connect LiveWindow",
            "preview and export",
        ],
    },
    "cutsame-template": {
        "requires": ["template-engine"],
        "api_recipes": ["cutsame-replace-export"],
        "integration_modes": ["new-app", "incremental", "api-only"],
        "resources": ["R0", "R1", "R3", "R4", "R10"],
        "provides": ["CutSame replacement UI, preview, and export"],
        "guards": [
            "CutSame branch is selected",
            "all footage replacements validate before timeline creation",
            "required reverse footage exists before createTimeline",
        ],
        "lifecycle": [
            "prepare footage",
            "create CutSame timeline",
            "replace captions",
            "connect LiveWindow",
            "preview and export",
        ],
    },
    "mimo-template": {
        "requires": [
            "app-runtime",
            "asset-package-service",
            "media-import",
            "timeline-preview",
        ],
        "api_recipes": ["mimo-replace-export"],
        "integration_modes": ["new-app", "incremental", "api-only"],
        "resources": ["R0", "R1", "R3", "R4", "R10"],
        "provides": ["Mimo JSON-driven editing, preview, and export"],
        "guards": [
            "Mimo archive is extracted and info.json is parsed",
            "Mimo is not passed to the SDK .template installation path",
            "all referenced child packages install before timeline construction",
            "shot media and optional reverse media satisfy the Mimo recipe",
            "video FPS and audio resolution are valid",
        ],
        "lifecycle": [
            "parse Mimo metadata",
            "install Mimo child packages",
            "build shot tracks and packaged effects",
            "append Mimo captions and music",
            "connect LiveWindow",
            "preview and export",
        ],
    },
}

BLUEPRINT_CONTRACT_UPDATES = {
    "asset-center-demo": {
        "title": "External local material demo app",
        "resources": ["R0", "R4"],
        "notes": (
            "Browse authorized external offline examples copied into the app, install or upgrade a selected package, "
            "register the copied font, and return the selected local material result. The standalone product shell "
            "owns a real sample Timeline and aspect-matched LiveWindow, applies an installed filter to its sample "
            "clip, and exposes filter intensity and removal. Picker mode keeps a typed setResult contract for any "
            "owning editor or camera. "
            "No material endpoint, request client, authentication, or download code is generated."
        ),
        "lifecycle": [
            "initialize SDK",
            "create sample Timeline and aspect-matched LiveWindow preview",
            "open bundled local catalog",
            "install selected package or register selected font",
            "return typed local material result to the owning host",
            "apply installed filter to the sample clip and expose intensity/removal",
        ],
        "demo_evidence": [
            "asset-center-workflow.md",
            "default-sample-assets.md",
            "official-sdk-download-resources.md",
        ],
    },
    "beauty-camera": {
        "modules": [
            "feature-hub",
            "capture-camera",
            "capture-filter",
            "capture-scene",
            "beauty-camera",
            "makeup-service",
            "ar-scene",
            "segmentation-keying",
            "asset-center-service",
        ],
        "requires": [
            "feature-hub",
            "capture-camera",
            "capture-filter",
            "capture-scene",
            "beauty-camera",
            "makeup-service",
            "ar-scene",
            "segmentation-keying",
            "asset-center-service",
        ],
        "template_features": ["beauty-ar", "asset-center", "effects"],
        "resources": ["R0", "R1", "R2", "R4", "R5", "R8", "R9"],
        "notes": (
            "Full camera preview and recording shell with typed local-material picker results for VIDEOFX, "
            "CAPTURESCENE, ARSCENE, FACE_MESH, and MAKEUP; package-kind-specific dispatch; beauty, makeup, "
            "face mesh, AR scene, capture scene, filter, and segmentation controls; capability-gated focus, "
            "flash, zoom, and exposure; and callback-driven recording pause/resume. Proprietary material "
            "packages are not bundled; contact Meishe business to obtain authorized resources."
        ),
        "lifecycle": [
            "initialize Streaming SDK, Effect SDK, permissions, license, and required human detection models",
            "register capture device, recording started, duration, and first-frame callbacks before preview",
            "connect the LiveWindow, start preview, and track the active capture device and its capabilities",
            "install or register authorized local material before applying it through the typed camera route",
            "apply filters, capture scenes, AR scenes, face mesh, makeup, and segmentation on the main thread",
            "gate focus, flash, zoom, and exposure by the active device capability",
            "start, pause, resume, and stop recording while finalizing UI state from SDK callbacks",
            "clear callbacks and capture effects and release model/effect resources during teardown",
        ],
    },
    "template-mimo-cutsame-app": {
        "modules": [
            "feature-hub",
            "template-editor",
            "cutsame-template",
            "mimo-template",
            "asset-center-service",
        ],
        "resources": ["R0", "R1", "R3", "R4", "R10"],
        "notes": (
            "Runnable standard-template and CutSame branches use SDK .template descriptor mapping. "
            "The independent Mimo branch parses info.json and builds normal tracks from child "
            "packages. All branches support LiveWindow preview, export, and an external local-material entry."
        ),
    },
}

RECIPE_API_MEMBERS = {
    "sdk-init": [
        "NvsStreamingContext.init",
        "NvsStreamingContext.getInstance",
        "NvsStreamingContext.getSdkVersion",
        "NvsStreamingContext.getAssetPackageManager",
    ],
    "effect-sdk-init": [
        "NvsEffectSdkContext.init",
        "NvsEffectSdkContext.getInstance",
        "NvsEffectSdkContext.initHumanDetectionExt",
        "NvsEffectSdkContext.setupHumanDetectionData",
    ],
    "media-probe-and-ratio": [
        "NvsStreamingContext.getAVFileInfo",
        "NvsStreamingContext.getAVInfoFromFile",
        "NvsAVFileInfo.getDuration",
        "NvsAVFileInfo.getVideoStreamDimension",
        "NvsAVFileInfo.getVideoStreamRotation",
    ],
    "timeline-build": [
        "NvsStreamingContext.createTimeline",
        "NvsTimeline.appendVideoTrack",
        "NvsTimeline.appendAudioTrack",
        "NvsTimeline.getVideoTrackByIndex",
        "NvsVideoTrack.appendClip",
        "NvsVideoTrack.insertClip",
        "NvsTrack.splitClip",
        "NvsClip.changeTrimInPoint",
        "NvsClip.changeTrimOutPoint",
    ],
    "connect-livewindow": [
        "NvsStreamingContext.connectTimelineWithLiveWindow",
        "NvsStreamingContext.connectTimelineWithLiveWindowExt",
        "NvsStreamingContext.playbackTimeline",
        "NvsStreamingContext.seekTimeline",
        "NvsStreamingContext.getTimelineCurrentPosition",
        "NvsStreamingContext.stop",
        "NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK",
    ],
    "apply-refresh-editor-child": [
        "NvsStreamingContext.stop",
        "NvsStreamingContext.seekTimeline",
        "NvsStreamingContext.getStreamingEngineState",
    ],
    "install-asset-package": [
        "NvsAssetPackageManager.getAssetPackageStatus",
        "NvsAssetPackageManager.installAssetPackage",
        "NvsAssetPackageManager.upgradeAssetPackage",
        "NvsAssetPackageManager.getAssetPackageVersion",
        "NvsAssetPackageManager.getAssetPackageVersionFromAssetPackageFilePath",
    ],
    "bundled-material-install": [
        "NvsAssetPackageManager.installAssetPackage",
        "NvsAssetPackageManager.upgradeAssetPackage",
    ],
    "caption-sticker-edit": [
        "NvsTimeline.addCaption",
        "NvsTimeline.addModularCaption",
        "NvsTimeline.addCompoundCaption",
        "NvsTimeline.addAnimatedSticker",
        "NvsTimeline.removeCaption",
        "NvsTimeline.removeAnimatedSticker",
        "NvsCaption.setText",
        "NvsCompoundCaption.setText",
    ],
    "filter-effect-edit": [
        "NvsVideoClip.appendBuiltinFx",
        "NvsVideoClip.appendPackagedFx",
        "NvsTimeline.addBuiltinTimelineVideoFx",
        "NvsTimeline.addPackagedTimelineVideoFx",
        "NvsFx.setFloatVal",
        "NvsFx.setStringVal",
        "NvsFx.setBooleanVal",
        "NvsFx.setIntVal",
        "NvsFx.setColorVal",
    ],
    "audio-edit": [
        "NvsTimeline.appendAudioTrack",
        "NvsTimeline.getAudioTrackByIndex",
        "NvsAudioTrack.addClip",
        "NvsAudioTrack.appendClip",
        "NvsTrack.setVolumeGain",
        "NvsClip.setVolumeGain",
        "NvsAudioClip.appendFx",
    ],
    "capture-preview-record": [
        "NvsStreamingContext.connectCapturePreviewWithLiveWindow",
        "NvsStreamingContext.getCaptureDeviceCount",
        "NvsStreamingContext.startCapturePreview",
        "NvsStreamingContext.startRecording",
        "NvsStreamingContext.isRecordingPaused",
        "NvsStreamingContext.pauseRecording",
        "NvsStreamingContext.resumeRecording",
        "NvsStreamingContext.stopRecording",
        "NvsStreamingContext.getStreamingEngineState",
        "NvsStreamingContext.setCaptureDeviceCallback",
        "NvsStreamingContext.setCaptureRecordingStartedCallback",
        "NvsStreamingContext.setCaptureRecordingDurationCallback",
        "NvsStreamingContext.setCaptureRecordingFrameReachedCallback",
    ],
    "compile-export": [
        "NvsStreamingContext.compileTimeline",
        "NvsStreamingContext.setCompileCallback",
        "NvsStreamingContext.setCompileCallback2",
        "NvsStreamingContext.setCompileCallback3",
    ],
    "template-replace-export": [
        "NvsStreamingContext.createTimeline",
        "NvsStreamingContext.connectTimelineWithLiveWindow",
        "NvsStreamingContext.seekTimeline",
        "NvsStreamingContext.playbackTimeline",
        "NvsStreamingContext.getTimelineCurrentPosition",
        "NvsStreamingContext.compileTimeline",
        "NvsStreamingContext.setCompileCallback",
        "NvsStreamingContext.setCompileCallback2",
        "NvsAssetPackageManager.installAssetPackage",
        "NvsAssetPackageManager.getTemplateFootages",
        "NvsAssetPackageManager.getTemplateCaptions",
        "NvsAssetPackageManager.getTemplateCompoundCaptions",
        "NvsMediaFileConvertor.setMeidaFileConvertorCallback",
        "NvsMediaFileConvertor.convertMeidaFile",
        "NvsCaption.setText",
        "NvsCompoundCaption.setText",
    ],
}

RECIPE_API_MEMBERS["template-prepare-footage"] = [
    "NvsAssetPackageManager.installAssetPackage",
    "NvsAssetPackageManager.getTemplateFootages",
    "NvsAssetPackageManager.getTemplateCaptions",
    "NvsAssetPackageManager.getTemplateCompoundCaptions",
    "NvsMediaFileConvertor.setMeidaFileConvertorCallback",
    "NvsMediaFileConvertor.convertMeidaFile",
]
RECIPE_API_MEMBERS["cutsame-replace-export"] = list(
    RECIPE_API_MEMBERS["template-replace-export"]
)
RECIPE_API_MEMBERS["mimo-replace-export"] = list(
    dict.fromkeys(
        [
            "NvsAssetPackageManager.installAssetPackage",
            "NvsStreamingContext.createTimeline",
            "NvsTimeline.appendVideoTrack",
            "NvsVideoTrack.appendClip",
            "NvsVideoClip.appendPackagedFx",
            "NvsVideoTrack.setPackagedTransition",
            "NvsTimeline.addCompoundCaption",
            "NvsTimeline.addPackagedTimelineVideoFx",
            "NvsTimeline.appendAudioTrack",
            "NvsAudioTrack.appendClip",
            "NvsStreamingContext.connectTimelineWithLiveWindow",
            "NvsStreamingContext.seekTimeline",
            "NvsStreamingContext.compileTimeline",
        ]
    )
)

JAVA_UNIT_SPECS = [
    (
        "java.sdk.initialize",
        "Initialize NvsStreamingContext once",
        "app-runtime",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheSdkManager.java",
        "initialize",
        [
            "NvsStreamingContext.getInstance",
            "NvsStreamingContext.init",
            "NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT",
            "NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED",
        ],
        ["Android Context", "assets:/meishesdk.lic", "SDK runtime artifacts"],
        ["NvsStreamingContext"],
    ),
    (
        "java.media.probe",
        "Probe media duration, dimension, and rotation",
        "media-import",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaProbeController.java",
        "probe",
        [
            "NvsStreamingContext.getAVFileInfo",
            "NvsStreamingContext.getAVInfoFromFile",
            "NvsAVFileInfo.getDuration",
            "NvsAVFileInfo.getVideoStreamDimension",
            "NvsAVFileInfo.getVideoStreamRotation",
        ],
        ["NvsStreamingContext", "readable media file path"],
        ["media probe", "timeline ratio seed"],
    ),
    (
        "java.timeline.create",
        "Create an editable timeline",
        "timeline-state-store",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
        "createTimeline",
        [
            "NvsStreamingContext.createTimeline",
            "NvsTimeline.appendVideoTrack",
            "NvsTimeline.appendAudioTrack",
        ],
        ["NvsStreamingContext", "output width", "output height"],
        ["NvsTimeline", "video track 0", "audio track 0"],
    ),
    (
        "java.timeline.append-clip",
        "Append media to the primary video track",
        "timeline-state-store",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
        "appendClip",
        [
            "NvsTimeline.getVideoTrackByIndex",
            "NvsTimeline.appendVideoTrack",
            "NvsVideoTrack.appendClip",
        ],
        ["NvsTimeline", "readable media file path"],
        ["NvsVideoClip"],
    ),
    (
        "java.preview.connect",
        "Bind timeline state to LiveWindow",
        "timeline-preview",
        "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
        "connectTimeline",
        ["NvsStreamingContext.connectTimelineWithLiveWindow"],
        ["NvsStreamingContext", "NvsTimeline", "NvsLiveWindow"],
        ["synchronized timeline preview"],
    ),
    (
        "java.preview.play",
        "Play the current timeline range",
        "timeline-preview",
        "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
        "play",
        [
            "NvsTimeline.getDuration",
            "NvsStreamingContext.playbackTimeline",
            "NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE",
        ],
        ["NvsTimeline", "startUs", "endUs", "playback flags"],
        ["active timeline playback"],
    ),
    (
        "java.preview.seek",
        "Seek and refresh LiveWindow",
        "timeline-preview",
        "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
        "seek",
        [
            "NvsTimeline.getDuration",
            "NvsStreamingContext.seekTimeline",
            "NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE",
        ],
        ["NvsTimeline", "timestampUs", "seek flags"],
        ["updated LiveWindow frame"],
    ),
    (
        "java.asset.install-or-upgrade",
        "Install or upgrade an asset package",
        "asset-package-service",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAssetInstaller.java",
        "installOrUpgrade",
        RECIPE_API_MEMBERS["install-asset-package"],
        ["package path", "optional license path", "asset package type"],
        ["installed package id"],
    ),
    (
        "java.effect.append-builtin",
        "Append a built-in clip effect",
        "filter-editor",
        "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
        "appendBuiltinClipFx",
        ["NvsVideoClip.appendBuiltinFx"],
        ["NvsVideoClip", "built-in FX name"],
        ["NvsVideoFx"],
    ),
    (
        "java.effect.add-timeline-builtin",
        "Add a built-in timeline effect",
        "filter-editor",
        "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
        "addBuiltinTimelineFx",
        ["NvsTimeline.addBuiltinTimelineVideoFx"],
        ["NvsTimeline", "inPointUs", "durationUs", "built-in FX name"],
        ["NvsTimelineVideoFx"],
    ),
    (
        "java.effect.append-packaged",
        "Append a packaged clip effect",
        "filter-editor",
        "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
        "appendPackagedClipFx",
        ["NvsVideoClip.appendPackagedFx"],
        ["NvsVideoClip", "installed FX package id"],
        ["NvsVideoFx"],
    ),
    (
        "java.effect.set-float",
        "Set a numeric FX parameter",
        "filter-editor",
        "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
        "setFloat",
        ["NvsFx.setFloatVal"],
        ["NvsFx", "parameter key", "double value"],
        ["updated FX parameter"],
    ),
    (
        "java.caption.add",
        "Add a timeline caption",
        "caption-editor",
        "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
        "addCaption",
        ["NvsTimeline.addCaption"],
        ["NvsTimeline", "text", "inPointUs", "durationUs", "optional style package id"],
        ["NvsTimelineCaption"],
    ),
    (
        "java.caption.add-compound",
        "Add a compound caption",
        "compound-caption-editor",
        "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
        "addCompoundCaption",
        ["NvsTimeline.addCompoundCaption"],
        ["NvsTimeline", "inPointUs", "durationUs", "installed compound caption package id"],
        ["NvsTimelineCompoundCaption"],
    ),
    (
        "java.caption.set-text",
        "Set timeline caption text",
        "caption-editor",
        "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
        "setCaptionText",
        ["NvsCaption.setText"],
        ["NvsTimelineCaption", "text"],
        ["updated caption text"],
    ),
    (
        "java.sticker.add",
        "Add a packaged animated sticker",
        "sticker-editor",
        "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
        "addAnimatedSticker",
        ["NvsTimeline.addAnimatedSticker"],
        ["NvsTimeline", "inPointUs", "durationUs", "installed sticker package id"],
        ["NvsTimelineAnimatedSticker"],
    ),
    (
        "java.sticker.remove",
        "Remove a timeline animated sticker",
        "sticker-editor",
        "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
        "removeAnimatedSticker",
        ["NvsTimeline.removeAnimatedSticker"],
        ["NvsTimeline", "NvsTimelineAnimatedSticker"],
        ["removed animated sticker"],
    ),
    (
        "java.audio.ensure-track",
        "Create or retrieve an audio track",
        "music-editor",
        "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
        "ensureAudioTrack",
        [
            "NvsTimeline.audioTrackCount",
            "NvsTimeline.getAudioTrackByIndex",
            "NvsTimeline.appendAudioTrack",
        ],
        ["NvsTimeline", "audio track index"],
        ["NvsAudioTrack"],
    ),
    (
        "java.audio.add-clip",
        "Add music or voice audio at a timeline position",
        "music-editor",
        "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
        "addClip",
        ["NvsAudioTrack.addClip"],
        ["NvsAudioTrack", "audio file path", "inPointUs", "trimInUs", "trimOutUs"],
        ["NvsAudioClip"],
    ),
    (
        "java.audio.set-clip-volume",
        "Set audio clip volume",
        "music-editor",
        "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
        "setClipVolume",
        ["NvsClip.setVolumeGain"],
        ["NvsAudioClip", "volume"],
        ["updated audio volume"],
    ),
    (
        "java.capture.start-preview",
        "Start camera capture preview",
        "capture-camera",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
        "startPreview",
        [
            "NvsStreamingContext.getCaptureDeviceCount",
            "NvsStreamingContext.connectCapturePreviewWithLiveWindow",
            "NvsStreamingContext.startCapturePreview",
        ],
        ["NvsStreamingContext", "NvsLiveWindow", "camera permission", "device index"],
        ["active capture preview"],
    ),
    (
        "java.capture.start-recording",
        "Start capture recording",
        "capture-camera",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
        "startRecording",
        [
            "NvsStreamingContext.getStreamingEngineState",
            "NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING",
            "NvsStreamingContext.startRecording",
        ],
        ["active capture preview", "writable output path"],
        ["recording session"],
    ),
    (
        "java.capture.pause-recording",
        "Pause an active capture recording in the same output file",
        "capture-camera",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
        "pauseRecording",
        [
            "NvsStreamingContext.getStreamingEngineState",
            "NvsStreamingContext.isRecordingPaused",
            "NvsStreamingContext.pauseRecording",
        ],
        [
            "active capture recording",
            "capture preview started with STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER",
        ],
        ["paused recording session that retains the current output file"],
    ),
    (
        "java.capture.resume-recording",
        "Resume a paused capture recording in the same output file",
        "capture-camera",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
        "resumeRecording",
        [
            "NvsStreamingContext.getStreamingEngineState",
            "NvsStreamingContext.isRecordingPaused",
            "NvsStreamingContext.resumeRecording",
        ],
        ["paused capture recording"],
        ["resumed recording session that retains the current output file"],
    ),
    (
        "java.capture.stop-recording",
        "Stop capture recording",
        "capture-camera",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
        "stopRecording",
        [
            "NvsStreamingContext.getStreamingEngineState",
            "NvsStreamingContext.stopRecording",
        ],
        ["active recording session"],
        ["stopped recording"],
    ),
    (
        "java.beauty.effect-sdk-init",
        "Initialize Effect SDK context",
        "beauty-camera",
        "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
        "initializeEffectSdkIfNeeded",
        [
            "NvsEffectSdkContext.getInstance",
            "NvsEffectSdkContext.init",
        ],
        ["Android Context", "Effect SDK jar", "license"],
        ["NvsEffectSdkContext"],
    ),
    (
        "java.beauty.append-ar-scene",
        "Append AR scene capture effect",
        "ar-scene",
        "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
        "appendArSceneCaptureFx",
        [
            "NvsStreamingContext.hasARModule",
            "NvsStreamingContext.appendBuiltinCaptureVideoFx",
            "NvsStreamingContext.isAndroidCameraPreferDualBufferAR",
            "NvsFx.setBooleanVal",
        ],
        ["NvsStreamingContext", "AR module", "human detection models"],
        ["NvsCaptureVideoFx"],
    ),
    (
        "java.beauty.apply-ar-scene-package",
        "Bind an installed AR Scene package through Scene Id",
        "ar-scene",
        "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
        "applyArScenePackage",
        [
            "NvsFx.setStringVal",
            "NvsFx.getStringVal",
        ],
        ["AR Scene capture FX", "installed AR Scene package id"],
        ["verified Scene Id package binding"],
    ),
    (
        "java.beauty.apply-face-mesh-package",
        "Bind an eyebrow-angle Face Mesh package through AR Scene keys",
        "ar-scene",
        "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
        "applyEyebrowAngleFaceMeshPackage",
        [
            "NvsFx.setBooleanVal",
            "NvsFx.setStringVal",
            "NvsFx.setFloatVal",
            "NvsFx.getStringVal",
        ],
        [
            "AR Scene capture FX",
            "installed Face Mesh package id",
            "Eyebrow Angle degree",
        ],
        [
            "Beauty Shape and Face Mesh Internal Enabled state",
            "verified Eyebrow Angle Custom Package Id binding",
        ],
    ),
    (
        "java.beauty.enable-ai-face-occlusion",
        "Enable AI face occlusion on high-power devices",
        "ar-scene",
        "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
        "enableAIFaceOcclusionIfHighPower",
        [
            "NvsStreamingContext.getDeviceCpuLevel",
            "NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH",
            "NvsFx.setBooleanVal",
        ],
        ["NvsStreamingContext", "AR Scene capture effect"],
        ["device-gated AI face occlusion state"],
    ),
    (
        "java.export.compile",
        "Compile timeline to a video file",
        "export-compile",
        "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheExportController.java",
        "export",
        ["NvsTimeline.getDuration", "NvsStreamingContext.compileTimeline"],
        ["NvsStreamingContext", "NvsTimeline", "writable output path"],
        ["compile start result", "export callbacks"],
    ),
]

JAVA_UNIT_SPECS.extend(
    [
        (
            "java.app.apply-system-bar-insets",
            "Keep generated Activity content outside system bars",
            "editor-ui-shell",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "applySystemBarInsets",
            [],
            ["Activity with an inflated content view"],
            ["system-bar-safe content layout"],
        ),
        (
            "java.app.request-permissions",
            "Request only the runtime permissions required by selected modules",
            "permission-gates",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "requestPermissions",
            [],
            ["Activity", "permission names", "request code"],
            ["permission request or already-granted result"],
        ),
        (
            "java.app.route-feature",
            "Open a selected feature entry",
            "feature-hub",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "openFeature",
            [],
            ["Android Context", "feature Activity class"],
            ["feature navigation result"],
        ),
        (
            "java.app.show-editor-message",
            "Show an editor-owned message dialog",
            "editor-ui-shell",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "showEditorMessage",
            [],
            ["Android Context", "title", "message"],
            ["AlertDialog"],
        ),
        (
            "java.app.save-project-state",
            "Persist serialized editor project state",
            "app-repository",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "saveProjectState",
            [],
            ["Android Context", "project id", "serialized project state"],
            ["persistence result"],
        ),
        (
            "java.app.create-stable-object-id",
            "Create a stable project object identifier",
            "app-repository",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "createStableObjectId",
            [],
            ["semantic object prefix"],
            ["stable project object identifier"],
        ),
        (
            "java.app.save-atomic-project-state",
            "Atomically persist a versioned editor project",
            "app-repository",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "saveAtomicProjectState",
            [],
            ["Android Context", "project id", "serialized version-3 project"],
            ["atomic persistence result"],
        ),
        (
            "java.app.load-atomic-project-state",
            "Load an atomically persisted editor project",
            "app-repository",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "loadAtomicProjectState",
            [],
            ["Android Context", "project id"],
            ["serialized version-3 project or empty string"],
        ),
        (
            "java.app.save-timeline-structure",
            "Persist a multi-clip Timeline structure for later restoration",
            "app-repository",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "saveTimelineStructure",
            [
                "NvsTimeline.getVideoTrackByIndex",
                "NvsTrack.getClipCount",
                "NvsVideoTrack.getClipByIndex",
                "NvsClip.getFilePath",
                "NvsClip.getTrimIn",
                "NvsClip.getTrimOut",
                "NvsClip.getSpeed",
                "NvsClip.isKeepAudioPitch",
                "NvsVideoClip.getVideoType",
                "NvsVideoClip.getImageMotionAnimationEnabled",
            ],
            ["Android Context", "project id", "NvsTimeline", "project width and height"],
            ["persisted structural project state"],
        ),
        (
            "java.app.load-project-state",
            "Load serialized editor project state",
            "app-repository",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "loadProjectState",
            [],
            ["Android Context", "project id"],
            ["serialized project state or empty string"],
        ),
        (
            "java.app.latest-project-id",
            "Resolve the latest persisted editor project",
            "app-repository",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "latestProjectId",
            [],
            ["Android Context"],
            ["latest project id or empty string"],
        ),
        (
            "java.app.read-project-dimension",
            "Read a persisted project Timeline dimension",
            "app-repository",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "readProjectDimension",
            [],
            ["serialized project state", "width or height key", "fallback"],
            ["validated project dimension"],
        ),
        (
            "java.app.restore-timeline-structure",
            "Restore mixed image and video clips into a Timeline",
            "timeline-state-store",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "restoreTimelineStructure",
            [
                "NvsTimeline.getVideoTrackByIndex",
                "NvsTimeline.appendVideoTrack",
                "NvsTrack.removeAllClips",
                "NvsVideoTrack.appendClip",
                "NvsClip.changeSpeed",
                "NvsVideoClip.getVideoType",
                "NvsVideoClip.setImageMotionAnimationEnabled",
            ],
            ["NvsTimeline", "serialized project state"],
            ["restored clip count"],
        ),
        (
            "java.effect.build-parameter",
            "Build typed effect parameter metadata",
            "effect-parameter-models",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "buildEffectParameter",
            [],
            ["parameter key", "parameter type", "parameter value"],
            ["immutable effect parameter map"],
        ),
        (
            "java.app.create-feedback",
            "Create a host-controlled feedback intent",
            "support-feedback",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAppSupport.java",
            "createFeedbackIntent",
            [],
            ["support email", "subject", "body"],
            ["feedback Intent"],
        ),
        (
            "java.thread.require-main",
            "Guard SDK calls on the Android main thread",
            "app-runtime",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheThreading.java",
            "requireMainThread",
            ["NvsUtils.checkFunctionInMainThread"],
            ["operation name"],
            ["validated main-thread execution"],
        ),
        (
            "java.sdk.configure-runtime",
            "Configure global reader and icon limits",
            "app-runtime",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheSdkManager.java",
            "configureRuntime",
            ["NvsStreamingContext.setMaxReaderCount", "NvsStreamingContext.setIconSize"],
            ["max reader count", "icon size"],
            ["updated SDK runtime limits"],
        ),
        (
            "java.engine.stop",
            "Stop the streaming engine before conflicting work",
            "app-runtime",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheSdkManager.java",
            "stopEngine",
            ["NvsStreamingContext.stop"],
            ["initialized NvsStreamingContext"],
            ["stopped streaming engine"],
        ),
        (
            "java.timeline.get-video-clip",
            "Retrieve a video clip by track index",
            "clip-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "getVideoClip",
            ["NvsVideoTrack.getClipByIndex"],
            ["NvsTimeline", "clip index"],
            ["NvsVideoClip"],
        ),
        (
            "java.timeline.get-video-resolution",
            "Read timeline video resolution",
            "timeline-state-store",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "getVideoResolution",
            ["NvsTimeline.getVideoRes"],
            ["NvsTimeline"],
            ["NvsVideoResolution"],
        ),
        (
            "java.timeline.set-theme-music-volume",
            "Set theme music volume gain",
            "music-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "setThemeMusicVolume",
            ["NvsTimeline.setThemeMusicVolumeGain"],
            ["NvsTimeline", "volume"],
            ["updated theme music volume"],
        ),
        (
            "java.timeline.remove",
            "Stop the engine and remove a timeline",
            "timeline-state-store",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "removeTimeline",
            ["NvsStreamingContext.stop", "NvsStreamingContext.removeTimeline"],
            ["NvsStreamingContext", "NvsTimeline"],
            ["timeline removal result"],
        ),
        (
            "java.preview.configure-live-window",
            "Configure LiveWindow fill mode",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "configureLiveWindow",
            ["NvsLiveWindow.setFillMode"],
            ["NvsLiveWindow", "fill mode"],
            ["configured preview surface"],
        ),
        (
            "java.preview.register-callbacks",
            "Register playback and streaming engine callbacks",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "registerCallbacks",
            [
                "NvsStreamingContext.setPlaybackCallback",
                "NvsStreamingContext.setPlaybackCallback2",
                "NvsStreamingContext.setStreamingEngineCallback",
            ],
            ["playback callbacks", "streaming engine callback"],
            ["registered preview callbacks"],
        ),
        (
            "java.preview.build-seek-flags",
            "Build caption, sticker, and fast-scrub seek flags",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "buildSeekFlags",
            [
                "NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER",
                "NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER",
                "NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING",
            ],
            ["poster visibility and scrubbing choices"],
            ["seek flags"],
        ),
        (
            "java.preview.set-seek-scale",
            "Set timeline scale used for seek",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "setSeekTimelineScale",
            ["NvsStreamingContext.setTimelineScaleForSeek"],
            ["NvsTimeline", "positive seek scale"],
            ["updated seek scale"],
        ),
        (
            "java.preview.map-thumbnail-position",
            "Map thumbnail view X coordinate to timeline time",
            "timeline-ui",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "mapThumbnailXToTimelinePosition",
            ["NvsMultiThumbnailSequenceView.mapTimelinePosFromX"],
            ["NvsMultiThumbnailSequenceView", "view X coordinate"],
            ["timeline position in microseconds"],
        ),
        (
            "java.preview.read-engine-state",
            "Read and classify streaming engine state",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "streamingEngineStateName",
            [
                "NvsStreamingContext.getStreamingEngineState",
                "NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED",
                "NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW",
                "NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING",
                "NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE",
            ],
            ["NvsStreamingContext"],
            ["normalized engine state name"],
        ),
        (
            "java.effect.append-raw-builtin",
            "Append a raw built-in clip effect",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "appendRawBuiltinClipFx",
            ["NvsVideoClip.appendRawBuiltinFx"],
            ["NvsVideoClip", "built-in FX name"],
            ["NvsVideoFx"],
        ),
        (
            "java.effect.list-clip-fx",
            "Inspect normal and raw clip effects",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "listBuiltinClipFxNames",
            [
                "NvsVideoClip.getFxByIndex",
                "NvsVideoClip.getRawFxCount",
                "NvsVideoClip.getRawFxByIndex",
                "NvsVideoFx.getBuiltinVideoFxName",
            ],
            ["NvsVideoClip"],
            ["built-in clip FX names"],
        ),
        (
            "java.effect.get-first-timeline-fx",
            "Retrieve the first timeline effect",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "getFirstTimelineFx",
            ["NvsTimeline.getFirstTimelineVideoFx"],
            ["NvsTimeline"],
            ["NvsTimelineVideoFx"],
        ),
        (
            "java.effect.remove-timeline-fx",
            "Remove a timeline video effect",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "removeTimelineFx",
            ["NvsTimeline.removeTimelineVideoFx"],
            ["NvsTimeline", "NvsTimelineVideoFx"],
            ["removed timeline effect"],
        ),
        (
            "java.transition.set-builtin",
            "Set a built-in transition",
            "transition-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "setBuiltinTransition",
            ["NvsVideoTrack.setBuiltinTransition"],
            ["NvsVideoTrack", "source clip index", "transition name"],
            ["NvsVideoTransition"],
        ),
        (
            "java.transition.set-packaged",
            "Set an installed packaged transition",
            "transition-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "setPackagedTransition",
            ["NvsVideoTrack.setPackagedTransition"],
            ["NvsVideoTrack", "source clip index", "transition package id"],
            ["NvsVideoTransition"],
        ),
        (
            "java.transition.get",
            "Retrieve a transition by source clip index",
            "transition-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "getTransition",
            ["NvsVideoTrack.getTransitionBySourceClipIndex"],
            ["NvsVideoTrack", "source clip index"],
            ["NvsVideoTransition"],
        ),
        (
            "java.clip.configure-image-motion",
            "Configure image motion, pan, and scan",
            "animation-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "configureImageMotion",
            [
                "NvsVideoClip.setImageMotionMode",
                "NvsVideoClip.setPanAndScan",
                "NvsVideoClip.setImageMotionAnimationEnabled",
            ],
            ["NvsVideoClip", "motion mode", "pan", "scan", "animation flag"],
            ["updated image motion"],
        ),
        (
            "java.clip.is-audio-video",
            "Identify audio-video clip type",
            "clip-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "isAudioVideoClip",
            ["NvsVideoClip.getVideoType", "NvsVideoClip.VIDEO_CLIP_TYPE_AV"],
            ["NvsVideoClip"],
            ["audio-video clip predicate"],
        ),
        (
            "java.caption.list-timeline",
            "Iterate timeline captions",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "listTimelineCaptions",
            ["NvsTimeline.getFirstCaption", "NvsTimeline.getNextCaption"],
            ["NvsTimeline"],
            ["timeline captions"],
        ),
        (
            "java.caption.list-compound",
            "Iterate timeline compound captions",
            "compound-caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "listCompoundCaptions",
            ["NvsTimeline.getFirstCompoundCaption", "NvsTimeline.getNextCaption"],
            ["NvsTimeline"],
            ["timeline compound captions"],
        ),
        (
            "java.sticker.list-timeline",
            "Iterate timeline animated stickers",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "listAnimatedStickers",
            ["NvsTimeline.getFirstAnimatedSticker", "NvsTimeline.getNextAnimatedSticker"],
            ["NvsTimeline"],
            ["timeline animated stickers"],
        ),
        (
            "java.sticker.list-at-position",
            "Read animated stickers at a timeline position",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "animatedStickersAt",
            ["NvsTimeline.getAnimatedStickersByTimelinePosition"],
            ["NvsTimeline", "timeline position"],
            ["animated stickers at position"],
        ),
        (
            "java.sticker.add-custom",
            "Add a custom animated sticker",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "addCustomAnimatedSticker",
            ["NvsTimeline.addCustomAnimatedSticker"],
            ["NvsTimeline", "time range", "package id", "image path"],
            ["NvsTimelineAnimatedSticker"],
        ),
        (
            "java.caption.timeline-range",
            "Read timeline caption time range",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "timelineCaptionRange",
            ["NvsTimelineCaption.getInPoint", "NvsTimelineCaption.getOutPoint"],
            ["NvsTimelineCaption"],
            ["caption time range"],
        ),
        (
            "java.caption.compound-range",
            "Read compound caption time range",
            "compound-caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "compoundCaptionRange",
            ["NvsTimelineCompoundCaption.getInPoint", "NvsTimelineCompoundCaption.getOutPoint"],
            ["NvsTimelineCompoundCaption"],
            ["compound caption time range"],
        ),
        (
            "java.sticker.timeline-range",
            "Read timeline sticker time range",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "animatedStickerRange",
            ["NvsTimelineAnimatedSticker.getInPoint", "NvsTimelineAnimatedSticker.getOutPoint"],
            ["NvsTimelineAnimatedSticker"],
            ["sticker time range"],
        ),
        (
            "java.caption.clip-range",
            "Read clip caption time range",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "clipCaptionRange",
            ["NvsClipCaption.getInPoint", "NvsClipCaption.getOutPoint"],
            ["NvsClipCaption"],
            ["clip caption time range"],
        ),
        (
            "java.sticker.clip-range",
            "Read clip sticker time range",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "clipAnimatedStickerRange",
            ["NvsClipAnimatedSticker.getInPoint", "NvsClipAnimatedSticker.getOutPoint"],
            ["NvsClipAnimatedSticker"],
            ["clip sticker time range"],
        ),
        (
            "java.caption.list-clip",
            "Iterate clip captions",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "listClipCaptions",
            ["NvsVideoClip.getFirstCaption", "NvsVideoClip.getNextCaption"],
            ["NvsVideoClip"],
            ["clip captions"],
        ),
        (
            "java.caption.list-clip-compound",
            "Iterate clip compound captions",
            "compound-caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "listClipCompoundCaptions",
            ["NvsVideoClip.getFirstCompoundCaption", "NvsVideoClip.getNextCaption"],
            ["NvsVideoClip"],
            ["clip compound captions"],
        ),
        (
            "java.caption.register-font",
            "Register a font file with the streaming context",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "registerFont",
            ["NvsStreamingContext.registerFontByFilePath"],
            ["NvsStreamingContext", "font file path"],
            ["font family name"],
        ),
        (
            "java.caption.apply-readable-style",
            "Apply a readable default caption style",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "applyReadableDefaultStyle",
            [
                "NvsCaption.TEXT_ALIGNMENT_CENTER",
                "NvsCaption.setTextAlignment",
                "NvsCaption.setTextColor",
                "NvsCaption.setFontSize",
                "NvsCaption.setDrawOutline",
                "NvsCaption.setOutlineColor",
                "NvsCaption.setOutlineWidth",
                "NvsColor",
            ],
            ["NvsTimelineCaption"],
            ["readable default caption appearance"],
        ),
        (
            "java.caption.set-letter-spacing",
            "Set absolute caption letter spacing",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "setAbsoluteLetterSpacing",
            [
                "NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE",
                "NvsCaption.setLetterSpacingType",
                "NvsCaption.setLetterSpacing",
            ],
            ["NvsCaption", "letter spacing"],
            ["updated caption letter spacing"],
        ),
        (
            "java.caption.remove-compound",
            "Remove a compound timeline caption",
            "compound-caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "removeCompoundCaption",
            ["NvsTimeline.removeCompoundCaption"],
            ["NvsTimeline", "NvsTimelineCompoundCaption"],
            ["removed compound caption"],
        ),
        (
            "java.audio.get-clip",
            "Retrieve an audio clip by index",
            "music-editor",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "getClip",
            ["NvsAudioTrack.getClipByIndex"],
            ["NvsAudioTrack", "clip index"],
            ["NvsAudioClip"],
        ),
        (
            "java.audio.set-fades",
            "Set audio clip fade-in and fade-out durations",
            "music-editor",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "setFadeDurations",
            ["NvsAudioClip.setFadeInDuration", "NvsAudioClip.setFadeOutDuration"],
            ["NvsAudioClip", "fade durations"],
            ["updated audio fades"],
        ),
        (
            "java.capture.build-preview-flags",
            "Build capture preview flags",
            "capture-camera",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "buildCapturePreviewFlags",
            [
                "NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME",
                "NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO",
                "NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER",
                "NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_ENABLE_TAKE_PICTURE",
                "NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME",
                "NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE",
            ],
            ["capture behavior choices"],
            ["capture preview flags"],
        ),
        (
            "java.capture.start-recording-with-flags",
            "Start recording with rotation and fast-stop flags",
            "capture-camera",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "startRecordingWithFlags",
            [
                "NvsStreamingContext.startRecording",
                "NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_IGNORE_VIDEO_ROTATION",
                "NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_SOFTWARE_VIDEO_INTRA_FRAME_ONLY_FAST_STOP",
            ],
            ["output path", "recording behavior choices"],
            ["recording start result"],
        ),
        (
            "java.capture.get-device-capability",
            "Read capture device capability",
            "capture-camera",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "getDeviceCapability",
            ["NvsStreamingContext.getCaptureDeviceCapability"],
            ["device index"],
            ["CaptureDeviceCapability"],
        ),
        (
            "java.capture.register-callbacks",
            "Register capture device and recording callbacks",
            "capture-camera",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "registerCallbacks",
            [
                "NvsStreamingContext.setCaptureDeviceCallback",
                "NvsStreamingContext.setCaptureRecordingStartedCallback",
                "NvsStreamingContext.setCaptureRecordingDurationCallback",
                "NvsStreamingContext.setCaptureRecordingFrameReachedCallback",
            ],
            ["capture callbacks"],
            ["registered capture callbacks"],
        ),
        (
            "java.capture.list-effects",
            "Inspect capture video effects",
            "capture-filter",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "listCaptureEffects",
            [
                "NvsStreamingContext.getCaptureVideoFxCount",
                "NvsStreamingContext.getCaptureVideoFxByIndex",
            ],
            ["NvsStreamingContext"],
            ["capture video effects"],
        ),
        (
            "java.capture.remove-effect",
            "Remove one capture video effect",
            "capture-filter",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "removeCaptureEffect",
            [
                "NvsStreamingContext.getCaptureVideoFxCount",
                "NvsStreamingContext.removeCaptureVideoFx",
            ],
            ["capture effect index"],
            ["capture effect removal result"],
        ),
        (
            "java.capture.clear-effects",
            "Remove capture video effects and current capture scene",
            "capture-filter",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "clearCaptureEffects",
            [
                "NvsStreamingContext.removeAllCaptureVideoFx",
                "NvsStreamingContext.removeCurrentCaptureScene",
            ],
            ["NvsStreamingContext"],
            ["cleared capture effect state"],
        ),
        (
            "java.beauty.initialize-human-detection",
            "Initialize main and optional human detection data",
            "ar-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "initializeHumanDetection",
            [
                "NvsStreamingContext.initHumanDetection",
                "NvsStreamingContext.initHumanDetectionExt",
                "NvsStreamingContext.setupHumanDetectionData",
            ],
            ["Android Context", "model paths", "feature flags", "data type"],
            ["human detection initialization result"],
        ),
        (
            "java.beauty.release-human-detection",
            "Release human detection resources",
            "ar-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "releaseHumanDetection",
            ["NvsStreamingContext.closeHumanDetection"],
            ["initialized human detection"],
            ["released human detection resources"],
        ),
        (
            "java.beauty.configure-ar-scene",
            "Enable and configure AR Scene beauty parameters",
            "ar-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "configureArBeauty",
            [
                "NvsFx.setBooleanVal",
                "NvsFx.setFloatVal",
            ],
            ["NvsCaptureVideoFx AR Scene", "beauty strength", "whitening strength"],
            ["configured AR Scene beauty"],
        ),
        (
            "java.segmentation.append-background-capture",
            "Append and configure capture background segmentation",
            "segmentation-keying",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "appendSegmentationBackgroundFx",
            [
                "NvsStreamingContext.hasARModule",
                "NvsStreamingContext.appendBuiltinCaptureVideoFx",
                "NvsFx.setMenuVal",
                "NvsFx.setIntVal",
                "NvsFx.setColorVal",
            ],
            ["NvsStreamingContext", "background segmentation model", "background color"],
            ["NvsCaptureVideoFx background segmentation"],
        ),
        (
            "java.capture.append-packaged-fx",
            "Append an installed capture video effect",
            "capture-filter",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "appendCapturePackagedFx",
            ["NvsStreamingContext.appendPackagedCaptureVideoFx"],
            ["NvsStreamingContext", "capture FX package id"],
            ["NvsCaptureVideoFx"],
        ),
        (
            "java.export.configure",
            "Configure bitrate, FPS, operating rate, encoder, and HDR transfer",
            "export-compile",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheExportController.java",
            "configureCompile",
            [
                "NvsStreamingContext.COMPILE_BITRATE",
                "NvsStreamingContext.COMPILE_FPS",
                "NvsStreamingContext.COMPILE_USE_OPERATING_RATE",
                "NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME",
                "NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER",
                "NvsStreamingContext.setCompileConfigurations",
            ],
            ["compile configuration choices"],
            ["applied compile configurations"],
        ),
        (
            "java.export.resolution-grade",
            "Choose compile resolution grade from output height",
            "export-compile",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheExportController.java",
            "resolutionGradeForHeight",
            [
                "NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360",
                "NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480",
                "NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720",
                "NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080",
                "NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_2160",
                "NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM",
            ],
            ["output height"],
            ["compile resolution grade"],
        ),
        (
            "java.export.bitrate-grade",
            "Choose compile bitrate grade",
            "export-compile",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheExportController.java",
            "bitrateGrade",
            [
                "NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH",
                "NvsStreamingContext.COMPILE_BITRATE_GRADE_MEDIUM",
            ],
            ["quality preference"],
            ["compile bitrate grade"],
        ),
        (
            "java.asset.package-type",
            "Map lightweight sample package extensions to SDK package types",
            "asset-package-service",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAssetInstaller.java",
            "packageTypeForPath",
            [
                "NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX",
                "NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER",
                "NvsAssetPackageManager.ASSET_PACKAGE_TYPE_TEMPLATE",
            ],
            ["asset package path"],
            ["asset package type or unsupported result"],
        ),
    ]
)

JAVA_UNIT_SPECS.extend(
    [
        (
            "java.sdk.initialize-activity-default",
            "Initialize NvsStreamingContext with the Activity overload that uses default flags",
            "app-runtime",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheSdkManager.java",
            "initializeForActivityDefault",
            ["NvsStreamingContext.getInstance", "NvsStreamingContext.init"],
            ["Activity", "assets:/meishesdk.lic"],
            ["NvsStreamingContext initialization result"],
        ),
        (
            "java.timeline.create-with-flags",
            "Create an editable timeline with SDK timeline flags",
            "timeline-state-store",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "createTimelineWithFlags",
            ["NvsStreamingContext.createTimeline"],
            ["NvsStreamingContext", "output width", "output height", "timeline flags"],
            ["NvsTimeline"],
        ),
        (
            "java.timeline.create-template-configured",
            "Create a template timeline with flags and explicit audio/video settings",
            "template-engine",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "createTemplateTimelineConfigured",
            ["NvsStreamingContext.createTimeline"],
            ["template id", "template footage", "flags", "video FPS", "audio resolution"],
            ["template NvsTimeline"],
        ),
        (
            "java.export.compile-configured",
            "Compile a timeline with per-call configuration options",
            "export-compile",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheExportController.java",
            "exportWithConfigurations",
            ["NvsTimeline.getDuration", "NvsStreamingContext.stop", "NvsStreamingContext.compileTimeline"],
            ["timeline", "time range", "output path", "resolution grade", "bitrate grade", "compile configurations", "flags"],
            ["compile start result"],
        ),
        (
            "java.beauty.initialize-human-detection-configured",
            "Initialize the main human detection model with SDK options",
            "ar-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "initializeStreamingHumanDetectionWithOptions",
            ["NvsStreamingContext.initHumanDetection"],
            ["Context", "model path", "license path", "features", "options"],
            ["human detection initialization result"],
        ),
        (
            "java.beauty.initialize-human-detection-ext-configured",
            "Initialize an extended human detection model with SDK options",
            "ar-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "initializeStreamingHumanDetectionExtWithOptions",
            ["NvsStreamingContext.initHumanDetectionExt"],
            ["Context", "extension model path", "license path", "features", "options"],
            ["extended human detection initialization result"],
        ),
        (
            "java.capture.stop-recording-synchronous",
            "Stop capture recording with explicit synchronous behavior",
            "capture-camera",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "stopRecordingSynchronously",
            ["NvsStreamingContext.getStreamingEngineState", "NvsStreamingContext.stopRecording"],
            ["active recording session", "synchronous flag"],
            ["recording stop request result"],
        ),
        (
            "java.effect.append-builtin-range",
            "Append a built-in clip effect over an explicit clip range",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "appendBuiltinClipFxInRange",
            ["NvsVideoClip.appendBuiltinFx"],
            ["NvsVideoClip", "built-in FX name", "clip in point", "duration"],
            ["NvsVideoFx"],
        ),
        (
            "java.effect.append-raw-builtin-range",
            "Append a raw-input built-in clip effect over an explicit clip range",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "appendRawBuiltinClipFxInRange",
            ["NvsVideoClip.appendRawBuiltinFx"],
            ["NvsVideoClip", "built-in FX name", "clip in point", "duration"],
            ["NvsVideoFx"],
        ),
        (
            "java.audio.append-clip-default",
            "Append a complete audio file with SDK default placement",
            "music-editor",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "appendClipDefault",
            ["NvsAudioTrack.appendClip"],
            ["NvsAudioTrack", "readable audio path"],
            ["NvsAudioClip"],
        ),
        (
            "java.clip.change-speed",
            "Change clip speed with the default audio-pitch behavior",
            "clip-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "changeClipSpeed",
            ["NvsClip.changeSpeed"],
            ["NvsClip", "positive finite speed"],
            ["clip speed mutation result"],
        ),
        (
            "java.clip.change-trim-in",
            "Change clip trim-in and return the SDK-adjusted value",
            "clip-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "changeClipTrimIn",
            ["NvsClip.changeTrimInPoint"],
            ["NvsClip", "source trim-in point", "affect sibling flag"],
            ["SDK-adjusted trim-in result"],
        ),
        (
            "java.caption.set-compound-text",
            "Set one text slot on a compound caption",
            "compound-caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "setCompoundCaptionTextAt",
            ["NvsCompoundCaption.setText"],
            ["NvsCompoundCaption", "caption index", "text"],
            ["updated compound caption text"],
        ),
        (
            "java.beauty.effect-sdk-init-activity-default",
            "Initialize Effect SDK with the Activity overload that uses default flags",
            "beauty-camera",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "initializeEffectSdkForActivityWithFlags",
            ["NvsEffectSdkContext.getInstance", "NvsEffectSdkContext.init"],
            ["Activity", "assets:/meishesdk.lic"],
            ["NvsEffectSdkContext initialization result"],
        ),
        (
            "java.beauty.effect-human-detection-ext-configured",
            "Initialize an Effect SDK extended human detection model with options",
            "ar-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "initializeEffectHumanDetectionExtWithOptions",
            ["NvsEffectSdkContext.getInstance", "NvsEffectSdkContext.initHumanDetectionExt"],
            ["Context", "extension model path", "license path", "features", "options"],
            ["Effect SDK extended human detection result"],
        ),
        (
            "java.export.register-callback3",
            "Register the compile secondary-progress callback",
            "export-compile",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheExportController.java",
            "registerCompileCallback3",
            ["NvsStreamingContext.setCompileCallback3"],
            ["NvsStreamingContext.CompileCallback3"],
            ["registered compile callback 3"],
        ),
        (
            "java.clip.move-to-timeline-position",
            "Move a clip to a timeline position with insertion and spacing controls",
            "clip-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "moveClipToTimelinePosition",
            ["NvsTrack.getClipCount", "NvsTrack.moveClip"],
            ["NvsTrack", "clip index", "target timeline position", "insert target", "keep space"],
            ["clip move result"],
        ),
        (
            "java.audio.set-track-stereo-volume",
            "Set independent left and right track volume gains",
            "music-editor",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "setTrackStereoVolume",
            ["NvsTrack.setVolumeGain"],
            ["NvsTrack", "left gain", "right gain"],
            ["updated track volume"],
        ),
        (
            "java.effect.append-packaged-range",
            "Append a packaged clip effect over an explicit clip range",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "appendPackagedClipFxInRange",
            ["NvsVideoClip.appendPackagedFx"],
            ["NvsVideoClip", "installed FX package id", "clip in point", "duration"],
            ["NvsVideoFx"],
        ),
    ]
)

JAVA_UNIT_SPECS.extend(
    [
        (
            "java.sdk.initialize-activity",
            "Initialize NvsStreamingContext with an Activity",
            "app-runtime",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheSdkManager.java",
            "initializeForActivity",
            ["NvsStreamingContext.init"],
            ["Activity", "streaming context flags"],
            ["NvsStreamingContext initialization result"],
        ),
        (
            "java.sdk.get-asset-package-manager",
            "Get the SDK asset package manager",
            "asset-package-service",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheSdkManager.java",
            "getAssetPackageManager",
            ["NvsStreamingContext.getAssetPackageManager"],
            ["initialized NvsStreamingContext"],
            ["NvsAssetPackageManager"],
        ),
        (
            "java.engine.stop-with-flags",
            "Stop the streaming engine with SDK stop flags",
            "app-runtime",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheSdkManager.java",
            "stopEngineWithFlags",
            ["NvsStreamingContext.stop"],
            ["initialized NvsStreamingContext", "stop flags"],
            ["stopped streaming engine"],
        ),
        (
            "java.media.probe-with-flags",
            "Probe media with SDK AV-file flags",
            "media-import",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaProbeController.java",
            "probeWithFlags",
            ["NvsStreamingContext.getAVFileInfo"],
            ["media path", "AV-file flags"],
            ["NvsAVFileInfo"],
        ),
        (
            "java.timeline.create-template",
            "Create a timeline from template footage",
            "template-engine",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "createTemplateTimeline",
            ["NvsStreamingContext.createTimeline"],
            ["template id", "template footage list"],
            ["template NvsTimeline"],
        ),
        (
            "java.timeline.create-template-with-flags",
            "Create a template timeline with SDK flags",
            "template-engine",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "createTemplateTimelineWithFlags",
            ["NvsStreamingContext.createTimeline"],
            ["template id", "template footage list", "timeline flags"],
            ["template NvsTimeline"],
        ),
        (
            "java.timeline.append-trimmed-clip",
            "Append a trimmed video clip",
            "clip-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "appendTrimmedClip",
            ["NvsVideoTrack.appendClip"],
            ["media path", "trim in", "trim out"],
            ["NvsVideoClip"],
        ),
        (
            "java.preview.current-position",
            "Read current timeline playback position",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "currentPosition",
            ["NvsStreamingContext.getTimelineCurrentPosition"],
            ["NvsTimeline"],
            ["current timeline position"],
        ),
        (
            "java.preview.play-with-fps",
            "Play a timeline with explicit preview FPS",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "playWithPreviewFps",
            ["NvsStreamingContext.playbackTimeline"],
            ["NvsTimeline", "time range", "preview FPS", "playback flags"],
            ["active timeline playback"],
        ),
        (
            "java.preview.seek-with-fps",
            "Seek a timeline with explicit preview FPS",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "seekWithPreviewFps",
            ["NvsStreamingContext.seekTimeline"],
            ["NvsTimeline", "timestamp", "preview FPS", "seek flags"],
            ["updated preview frame"],
        ),
        (
            "java.effect.add-packaged-timeline",
            "Add an installed packaged timeline effect",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "addPackagedTimelineFx",
            ["NvsTimeline.addPackagedTimelineVideoFx"],
            ["NvsTimeline", "time range", "FX package id"],
            ["NvsTimelineVideoFx"],
        ),
        (
            "java.caption.remove",
            "Remove a timeline caption",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "removeCaption",
            ["NvsTimeline.removeCaption"],
            ["NvsTimeline", "NvsTimelineCaption"],
            ["removed timeline caption"],
        ),
        (
            "java.capture.start-recording-configured",
            "Start recording with flags and configuration table",
            "capture-camera",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "startRecordingWithConfigurations",
            ["NvsStreamingContext.startRecording"],
            ["output path", "recording flags", "recording configurations"],
            ["recording start result"],
        ),
        (
            "java.export.register-callbacks",
            "Register compile completion and progress callbacks",
            "export-compile",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheExportController.java",
            "registerCompileCallbacks",
            [
                "NvsStreamingContext.setCompileCallback",
                "NvsStreamingContext.setCompileCallback2",
            ],
            ["compile callbacks"],
            ["registered compile callbacks"],
        ),
        (
            "java.audio.add-clip-at",
            "Add an audio clip at a timeline position",
            "music-editor",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "addClipAt",
            ["NvsAudioTrack.addClip"],
            ["NvsAudioTrack", "audio path", "timeline position"],
            ["NvsAudioClip"],
        ),
        (
            "java.app.copy-content-uri-to-cache",
            "Copy a selected Android content URI into app-owned cache storage",
            "media-import",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaFiles.java",
            "copyContentUriToCache",
            [],
            ["Android Context", "content URI"],
            ["readable app-owned media file path"],
        ),
        (
            "java.app.copy-bundled-media-to-project",
            "Copy bundled APK media into persistent app storage before SDK media probing",
            "media-import",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaFiles.java",
            "copyAssetToProject",
            [],
            ["Android Context", "relative APK asset path", "safe output name"],
            ["persistent SDK-readable bundled media file path"],
        ),
        (
            "java.app.copy-content-uri-to-project",
            "Copy selected Android content into persistent project media storage",
            "media-import",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaImporter.java",
            "copyToProjectFile",
            [],
            ["Android Context", "content URI"],
            ["persistent app-owned project media file"],
        ),
        (
            "java.timeline.build-picture-in-picture",
            "Build a two-track picture-in-picture timeline",
            "pip-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCompositionController.java",
            "buildPictureInPicture",
            [
                "NvsTimeline.getVideoTrackByIndex",
                "NvsTimeline.appendVideoTrack",
                "NvsVideoTrack.appendClip",
                "NvsVideoClip.setImageMotionAnimationEnabled",
                "NvsVideoClip.appendBuiltinFx",
                "NvsFx.setFloatVal",
            ],
            ["NvsTimeline", "base media path", "overlay media path"],
            ["two-track PIP composition with Transform 2D overlay"],
        ),
        (
            "java.timeline.build-quick-splice",
            "Build a multi-clip timeline with transitions",
            "quick-splicing",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCompositionController.java",
            "buildQuickSplice",
            [
                "NvsTimeline.getVideoTrackByIndex",
                "NvsVideoTrack.appendClip",
                "NvsVideoClip.setImageMotionAnimationEnabled",
                "NvsVideoTrack.setPackagedTransition",
                "NvsVideoTrack.setBuiltinTransition",
            ],
            ["NvsTimeline", "at least two media paths", "optional installed transition package id"],
            ["appended clip count and connected transitions"],
        ),
        (
            "java.timeline.append-media-list",
            "Append mixed image and video media to the primary track",
            "timeline-state-store",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "appendMediaList",
            [
                "NvsTimeline.getVideoTrackByIndex",
                "NvsTimeline.appendVideoTrack",
                "NvsVideoTrack.appendClip",
                "NvsVideoClip.getVideoType",
                "NvsVideoClip.setImageMotionAnimationEnabled",
            ],
            ["created NvsTimeline", "ordered app-owned media paths"],
            ["appended mixed-media clip count"],
        ),
        (
            "java.clip.trim-out-at-playhead",
            "Trim a selected clip using Timeline playhead coordinates",
            "clip-editor",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheClipEditController.java",
            "trimOutAtTimelinePosition",
            [
                "NvsClip.getInPoint",
                "NvsClip.getOutPoint",
                "NvsClip.getSpeed",
                "NvsClip.getTrimIn",
                "NvsClip.getTrimOut",
                "NvsClip.changeTrimOutPoint",
            ],
            ["NvsVideoClip", "Timeline playhead position in microseconds"],
            ["trim mutation result"],
        ),
        (
            "java.clip.remove-at",
            "Remove a selected clip by track index",
            "clip-editor",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheClipEditController.java",
            "removeAt",
            ["NvsTrack.getClipCount", "NvsTrack.removeClip"],
            ["NvsVideoTrack", "clip index"],
            ["remove mutation result"],
        ),
        (
            "java.clip.move",
            "Move a selected clip to a bounded track index",
            "clip-editor",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheClipEditController.java",
            "moveAt",
            ["NvsTrack.getClipCount", "NvsTrack.moveClip"],
            ["NvsVideoTrack", "source index", "target index"],
            ["move mutation result"],
        ),
        (
            "java.clip.split-at-playhead",
            "Split a selected clip using Timeline playhead coordinates",
            "clip-editor",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheClipEditController.java",
            "splitAt",
            [
                "NvsTrack.getClipCount",
                "NvsVideoTrack.getClipByIndex",
                "NvsClip.getInPoint",
                "NvsClip.getOutPoint",
                "NvsTrack.splitClip",
            ],
            ["NvsVideoTrack", "clip index", "Timeline playhead position in microseconds"],
            ["split mutation result"],
        ),
        (
            "java.app.extract-editor-state",
            "Extract versioned editor descriptors from persisted project state",
            "app-repository",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheEditorProjectStore.java",
            "extractEditorState",
            [],
            ["serialized project state"],
            ["versioned editor state JSON"],
        ),
        (
            "java.app.save-editor-state",
            "Merge versioned editor descriptors into persisted project state",
            "app-repository",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheEditorProjectStore.java",
            "saveEditorState",
            [],
            ["Android Context", "project id", "serialized editor state"],
            ["editor state persistence result"],
        ),
        (
            "java.editor.clear-supported-features",
            "Clear editor-owned effects, overlays, transitions, and audio before deterministic restore",
            "editor-shell",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheEditorProjectStore.java",
            "clearEditorFeatures",
            [
                "NvsTimeline.getVideoTrackByIndex",
                "NvsTrack.getClipCount",
                "NvsVideoTrack.getClipByIndex",
                "NvsClip.getFxCount",
                "NvsVideoClip.removeAllFx",
                "NvsVideoTrack.getTransitionBySourceClipIndex",
                "NvsVideoTrack.setBuiltinTransition",
                "NvsTimeline.getFirstCaption",
                "NvsTimeline.getNextCaption",
                "NvsTimeline.removeCaption",
                "NvsTimeline.getFirstAnimatedSticker",
                "NvsTimeline.getNextAnimatedSticker",
                "NvsTimeline.removeAnimatedSticker",
                "NvsTimeline.audioTrackCount",
                "NvsTimeline.getAudioTrackByIndex",
                "NvsTrack.removeAllClips",
            ],
            ["editor-owned NvsTimeline"],
            ["cleared editor item count"],
        ),
        (
            "java.editor.restore-supported-features",
            "Restore packaged filters, captions, stickers, transitions, and audio descriptors",
            "editor-shell",
            "assets/android-blueprint-templates/short-video-editor/app/src/main/java/{{PACKAGE_PATH}}/MeisheEditorProjectStore.java",
            "restoreEditorFeaturesByClipIds",
            [
                "NvsTimeline.getVideoTrackByIndex",
                "NvsTrack.getClipCount",
                "NvsVideoTrack.getClipByIndex",
                "NvsVideoClip.appendPackagedFx",
                "NvsTimeline.addCaption",
                "NvsCaption.setTextAlignment",
                "NvsCaption.setTextColor",
                "NvsCaption.setFontSize",
                "NvsCaption.setDrawOutline",
                "NvsCaption.setOutlineColor",
                "NvsCaption.setOutlineWidth",
                "NvsTimeline.addAnimatedSticker",
                "NvsVideoTrack.setPackagedTransition",
                "NvsTimeline.audioTrackCount",
                "NvsTimeline.appendAudioTrack",
                "NvsTimeline.getAudioTrackByIndex",
                "NvsAudioTrack.addClip",
                "NvsClip.setVolumeGain",
                "NvsAudioClip.setFadeInDuration",
                "NvsAudioClip.setFadeOutDuration",
            ],
            ["rebuilt NvsTimeline", "versioned editor state JSON", "installed asset packages"],
            ["restored editor item count"],
        ),
    ]
)

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo-root", type=Path, required=True, help="External SdkDemo root.")
    parser.add_argument("--sdk-jar", type=Path, help="Optional SDK jar used to extract public signatures.")
    parser.add_argument(
        "--sdk-signatures",
        type=Path,
        help="Optional previously extracted v2 signature map used for iterative rebuilds.",
    )
    parser.add_argument("--jdk-home", type=Path, help="Optional JDK home used to locate javap.")
    parser.add_argument("--output", type=Path, help="Optional full build-time extraction JSON.")
    parser.add_argument(
        "--write-references",
        action="store_true",
        help="Refresh standalone JSON artifacts and generated coverage Markdown.",
    )
    parser.add_argument("--max-methods", type=int, default=0, help="Optional AST result limit.")
    return parser.parse_args()

def skill_dir():
    return Path(__file__).resolve().parents[1]

def load_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True

def run_ast_extractor(demo_root):
    java_source = skill_dir() / "scripts" / "java" / "DemoAstExtractor.java"
    javac = shutil.which("javac")
    java = shutil.which("java")
    if not javac or not java:
        raise SystemExit("JDK 17+ is required to extract Demo Java AST data")
    with tempfile.TemporaryDirectory(prefix="meishe-demo-ast-") as build_dir:
        compile_result = subprocess.run(
            [javac, "-encoding", "UTF-8", "-d", build_dir, str(java_source)],
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            check=False,
        )
        if compile_result.returncode:
            raise SystemExit("Failed to compile DemoAstExtractor:\n" + compile_result.stderr)
        run_result = subprocess.run(
            [java, "-cp", build_dir, "DemoAstExtractor", str(demo_root)],
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            check=False,
        )
        if run_result.returncode:
            raise SystemExit("Demo AST extraction failed:\n" + run_result.stderr)
    return [
        json.loads(line)
        for line in run_result.stdout.splitlines()
        if line.strip()
    ]

def parse_markdown_api_inventory(references_dir):
    api_classes = []
    class_names = set()
    direct_members = {}
    section = ""
    for line in (references_dir / "demo-api-list.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## SDK Class/API Imports"):
            section = "classes"
            continue
        if line.startswith("## Direct API/Member Tokens"):
            section = "members"
            continue
        if line.startswith("## SDK-Adjacent Token Map"):
            section = "tokens"
            continue
        if line.startswith("## ") and section:
            section = ""
        if section == "classes":
            match = API_CLASS_ROW_RE.match(line)
            if match:
                api_class, package_name, files, category = match.groups()
                api_classes.append(
                    {
                        "class": api_class,
                        "package": package_name,
                        "file_count": int(files),
                        "category": category,
                    }
                )
                class_names.add(api_class)
        elif section == "members":
            match = DIRECT_MEMBER_ROW_RE.match(line)
            if match:
                member, kind, occurrences = match.groups()
                direct_members[member] = {
                    "member": member,
                    "kind": kind.strip(),
                    "occurrences": int(occurrences),
                    "source_labels": [],
                    "arities": [],
                }
        elif section == "tokens":
            match = TOKEN_ROW_RE.match(line)
            if match:
                token, occurrences = match.groups()
                if token not in class_names:
                    api_classes.append(
                        {
                            "class": token,
                            "package": "demo-observed",
                            "file_count": 0,
                            "token_occurrences": int(occurrences),
                            "category": "sdk-adjacent",
                        }
                    )
                    class_names.add(token)
    return api_classes, direct_members

def parse_priorities(path, section_header, row_pattern):
    priorities = {}
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(section_header):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if not in_table:
            continue
        match = row_pattern.match(line)
        if match:
            values = match.groups()
            priority = "P1" if values[-1] == "P0/P1" else values[-1]
            priorities[values[0]] = priority
    return priorities

def normalize_registry(registry):
    for recipe in registry.get("api_recipes", []):
        if recipe.get("id") == "material-center-download-install":
            recipe["id"] = "bundled-material-install"
    for collection_name in ("modules", "blueprints"):
        for item in registry.get(collection_name, []):
            item["api_recipes"] = [
                "bundled-material-install"
                if recipe_id == "material-center-download-install"
                else recipe_id
                for recipe_id in item.get("api_recipes", [])
            ]
    category_by_brick = {
        "streaming-context": "core-lifecycle",
        "effect-context": "ar-makeup-segmentation",
        "media-info": "audio-media",
        "timeline": "timeline-editing",
        "track-clip": "timeline-editing",
        "live-window": "preview-export",
        "asset-package-manager": "assets-packages",
        "timeline-fx": "effects-transforms",
        "caption-sticker-objects": "captions-stickers",
        "audio-objects": "audio-media",
        "capture-objects": "capture-recording",
        "template-objects": "template-mimo-cutsame",
    }
    recipe_category = {
        "sdk-init": "core-lifecycle",
        "effect-sdk-init": "ar-makeup-segmentation",
        "media-probe-and-ratio": "audio-media",
        "timeline-build": "timeline-editing",
        "connect-livewindow": "preview-export",
        "apply-refresh-editor-child": "timeline-editing",
        "editor-session-orchestration": "timeline-editing",
        "install-asset-package": "assets-packages",
        "bundled-material-install": "assets-packages",
        "caption-sticker-edit": "captions-stickers",
        "filter-effect-edit": "effects-transforms",
        "audio-edit": "audio-media",
        "capture-preview-record": "capture-recording",
        "compile-export": "preview-export",
        "template-replace-export": "template-mimo-cutsame",
        "template-prepare-footage": "template-mimo-cutsame",
        "cutsame-replace-export": "template-mimo-cutsame",
        "mimo-replace-export": "template-mimo-cutsame",
    }
    existing_recipe_ids = {
        recipe["id"] for recipe in registry.get("api_recipes", [])
    }
    for addition in RECIPE_ADDITIONS:
        if addition["id"] not in existing_recipe_ids:
            registry.setdefault("api_recipes", []).append(dict(addition))
            existing_recipe_ids.add(addition["id"])
    for brick in registry.get("api_bricks", []):
        brick.setdefault("level", "api_brick")
        brick.setdefault("category", category_by_brick.get(brick["id"], "general"))
        brick.setdefault("aliases", [brick["id"], brick.get("title", "")])
        brick.setdefault("requires", [])
        brick.setdefault("api_recipes", [])
        brick.setdefault("permissions", [])
        brick.setdefault("template_features", [])
        brick.setdefault("guards", ["required SDK object must be non-null before use"])
        brick.setdefault("conflicts", [])
        brick.setdefault("lifecycle", ["create or obtain before dependent recipes"])
        brick.setdefault("integration_modes", ["new-app", "incremental", "api-only"])
        brick.setdefault("demo_evidence", brick.get("simple_code_refs", []))
    for recipe in registry.get("api_recipes", []):
        for field, value in RECIPE_CONTRACT_UPDATES.get(recipe["id"], {}).items():
            recipe[field] = list(value) if isinstance(value, list) else value
        recipe.setdefault("title", recipe["id"].replace("-", " ").title())
        recipe.setdefault("level", "api_recipe")
        recipe.setdefault(
            "priority",
            "P0" if recipe["id"] in {"sdk-init", "timeline-build", "compile-export"} else "P1",
        )
        recipe.setdefault("category", recipe_category.get(recipe["id"], "general"))
        recipe.setdefault("aliases", [recipe["id"], recipe["title"]])
        recipe.setdefault("api_recipes", [])
        recipe.setdefault("permissions", [])
        recipe.setdefault("template_features", [])
        recipe.setdefault("conflicts", [])
        recipe.setdefault("lifecycle", list(recipe.get("provides", [])) or ["execute ordered SDK calls"])
        recipe.setdefault("integration_modes", ["new-app", "incremental", "api-only"])
        recipe.setdefault("demo_evidence", recipe.get("simple_code_refs", []))
    for module in registry.get("modules", []):
        for field, value in MODULE_CONTRACT_UPDATES.get(module["id"], {}).items():
            module[field] = list(value) if isinstance(value, list) else value
        module["template_features"] = sorted(
            set(module.get("template_features", []))
            | set(MODULE_TEMPLATE_FEATURE_ADDITIONS.get(module["id"], []))
        )
        module["requires"] = list(
            dict.fromkeys(
                [
                    *module.get("requires", []),
                    *MODULE_REQUIRED_ADDITIONS.get(module["id"], []),
                ]
            )
        )
    for feature in registry.get("demo_feature_coverage", []):
        if feature.get("module_id") == "asset-center-service":
            feature["coverage"] = "policy-replaced-local"
            feature["simple_code_refs"] = [
                "asset-center-workflow.md",
                "default-sample-assets.md",
            ]
            feature["resources"] = ["R0", "R4"]
            feature["source_labels"] = ["asset-center-workflow.md"]
    for blueprint in registry.get("blueprints", []):
        for field, value in BLUEPRINT_CONTRACT_UPDATES.get(blueprint["id"], {}).items():
            blueprint[field] = list(value) if isinstance(value, list) else value
        blueprint["resources"] = [
            resource for resource in blueprint.get("resources", []) if resource != "R13"
        ]
    registry["version"] = max(SCHEMA_VERSION, int(registry.get("version", 1)))
    return registry

def extract_method(source_text, symbol):
    pattern = re.compile(
        r"(?m)^[ \t]*(?:public|protected|private)\b[^{;]*\b"
        + re.escape(symbol)
        + r"\s*\("
    )
    match = pattern.search(source_text)
    if not match:
        raise ValueError(f"Method not found: {symbol}")
    brace_start = source_text.find("{", match.start())
    depth = 0
    in_string = False
    quote = ""
    escaped = False
    for index in range(brace_start, len(source_text)):
        character = source_text[index]
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote:
                in_string = False
            continue
        if character in {'"', "'"}:
            in_string = True
            quote = character
        elif character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return source_text[match.start(): index + 1].strip()
    raise ValueError(f"Unbalanced method body: {symbol}")

def module_blueprints(registry, module_id):
    return [
        blueprint["id"]
        for blueprint in registry.get("blueprints", [])
        if module_id in blueprint.get("modules", [])
    ]

def unit_contract(
    unit_id,
    kind,
    priority,
    feature,
    source_label,
    api_members,
    requires,
    inputs,
    provides,
    resources,
    guards,
    compose_into,
    evidence_refs,
    code="",
    template_source="",
    source_symbol="",
    steps=None,
    api_signatures=None,
    implementation_state=None,
    requires_modules=None,
    requires_capabilities=None,
    compose_after_units=None,
    lifecycle_hook="activity_create",
):
    if implementation_state is None:
        implementation_state = "compiled_unit" if kind == "java_unit" else "generated_module"
    if implementation_state not in IMPLEMENTATION_STATES:
        raise ValueError(f"Invalid implementation state: {implementation_state}")
    if lifecycle_hook not in LIFECYCLE_HOOKS:
        raise ValueError(f"Invalid lifecycle hook: {lifecycle_hook}")
    return {
        "schema_version": SCHEMA_VERSION,
        "id": unit_id,
        "kind": kind,
        "implementation_state": implementation_state,
        "priority": priority,
        "feature": feature,
        "source_label": source_label,
        "scenario": f"Demo-derived reusable operation for {feature}",
        "api_classes": sorted({member.split(".", 1)[0] for member in api_members}),
        "api_members": sorted(set(api_members)),
        "api_signatures": sorted(set(api_signatures or [])),
        "requires": list(requires),
        "inputs": list(inputs),
        "provides": list(provides),
        "resources": list(resources),
        "threading": "SDK calls run on the Android main thread; substantial file I/O runs in background.",
        "guards": list(guards),
        "failure": "Stop on false/null/error, report the SDK stage, and do not advance application state.",
        "compose_after": list(requires),
        "compose_after_units": list(compose_after_units or []),
        "compose_into": sorted(set(compose_into)),
        "requires_modules": list(requires_modules or []),
        "requires_capabilities": list(requires_capabilities or []),
        "lifecycle_hook": lifecycle_hook,
        "evidence_refs": list(evidence_refs),
        "code": code,
        "template_source": template_source,
        "source_symbol": source_symbol,
        "steps": list(steps or []),
    }

UNIT_COMPOSE_AFTER = {
    "java.sdk.initialize": [],
    "java.app.create-stable-object-id": [],
    "java.app.load-atomic-project-state": [],
    "java.app.save-atomic-project-state": ["java.app.create-stable-object-id"],
    "java.media.probe": ["java.sdk.initialize"],
    "java.timeline.create": ["java.sdk.initialize", "java.media.probe"],
    "java.timeline.append-clip": ["java.timeline.create"],
    "java.preview.connect": ["java.timeline.create"],
    "java.preview.play": ["java.preview.connect"],
    "java.preview.seek": ["java.preview.connect"],
    "java.asset.install-or-upgrade": ["java.sdk.initialize"],
    "java.asset-center.list-bundled-materials": [],
    "java.asset-center.install-bundled-package": [
        "java.sdk.initialize",
        "java.asset-center.list-bundled-materials",
    ],
    "java.asset-center.register-bundled-font": [
        "java.sdk.initialize",
        "java.asset-center.list-bundled-materials",
    ],
    "java.effect.append-builtin": ["java.timeline.append-clip"],
    "java.effect.add-timeline-builtin": ["java.timeline.create"],
    "java.effect.append-packaged": ["java.asset.install-or-upgrade", "java.timeline.append-clip"],
    "java.effect.set-float": ["java.effect.append-builtin"],
    "java.caption.add": ["java.timeline.create"],
    "java.caption.add-compound": ["java.asset.install-or-upgrade", "java.timeline.create"],
    "java.caption.set-text": ["java.caption.add"],
    "java.sticker.add": ["java.asset.install-or-upgrade", "java.timeline.create"],
    "java.sticker.remove": ["java.sticker.add"],
    "java.audio.ensure-track": ["java.timeline.create"],
    "java.audio.add-clip": ["java.audio.ensure-track"],
    "java.audio.set-clip-volume": ["java.audio.add-clip"],
    "java.capture.start-preview": ["java.sdk.initialize"],
    "java.capture.start-recording": ["java.capture.start-preview"],
    "java.capture.pause-recording": ["java.capture.start-recording"],
    "java.capture.resume-recording": ["java.capture.pause-recording"],
    "java.capture.stop-recording": ["java.capture.start-recording"],
    "java.beauty.effect-sdk-init": ["java.sdk.initialize"],
    "java.beauty.append-ar-scene": ["java.beauty.effect-sdk-init", "java.capture.start-preview"],
    "java.beauty.apply-ar-scene-package": [
        "java.asset.install-or-upgrade",
        "java.beauty.append-ar-scene",
    ],
    "java.beauty.apply-face-mesh-package": [
        "java.asset.install-or-upgrade",
        "java.beauty.append-ar-scene",
    ],
    "java.export.compile": ["java.timeline.create"],
}

UNIT_LIFECYCLE_HOOKS = {
    "java.sdk.initialize": "sdk_init",
    "java.app.create-stable-object-id": "timeline_created",
    "java.app.load-atomic-project-state": "activity_create",
    "java.app.save-atomic-project-state": "after_mutation_refresh",
    "java.media.probe": "activity_create",
    "java.timeline.create": "timeline_created",
    "java.timeline.append-clip": "before_structural_mutation",
    "java.preview.connect": "live_window_bound",
    "java.preview.play": "live_window_bound",
    "java.preview.seek": "after_mutation_refresh",
    "java.asset.install-or-upgrade": "asset_installed",
    "java.asset-center.list-bundled-materials": "activity_create",
    "java.asset-center.install-bundled-package": "asset_installed",
    "java.asset-center.register-bundled-font": "asset_installed",
    "java.effect.append-builtin": "before_structural_mutation",
    "java.effect.add-timeline-builtin": "before_structural_mutation",
    "java.effect.append-packaged": "asset_installed",
    "java.effect.set-float": "after_mutation_refresh",
    "java.caption.add": "before_structural_mutation",
    "java.caption.add-compound": "asset_installed",
    "java.caption.set-text": "after_mutation_refresh",
    "java.sticker.add": "asset_installed",
    "java.sticker.remove": "before_structural_mutation",
    "java.audio.ensure-track": "before_structural_mutation",
    "java.audio.add-clip": "before_structural_mutation",
    "java.audio.set-clip-volume": "after_mutation_refresh",
    "java.capture.start-preview": "activity_create",
    "java.capture.start-recording": "activity_create",
    "java.capture.pause-recording": "activity_create",
    "java.capture.resume-recording": "activity_create",
    "java.capture.stop-recording": "destroy",
    "java.beauty.effect-sdk-init": "sdk_init",
    "java.beauty.append-ar-scene": "activity_create",
    "java.beauty.apply-ar-scene-package": "asset_installed",
    "java.beauty.apply-face-mesh-package": "asset_installed",
    "java.export.compile": "before_structural_mutation",
}

STRUCTURAL_MUTATION_UNIT_IDS = {
    "java.audio.add-clip",
    "java.audio.add-clip-at",
    "java.audio.ensure-track",
    "java.caption.add",
    "java.caption.add-compound",
    "java.caption.remove",
    "java.caption.remove-compound",
    "java.clip.configure-image-motion",
    "java.effect.add-packaged-timeline",
    "java.effect.add-timeline-builtin",
    "java.effect.append-builtin",
    "java.effect.append-packaged",
    "java.effect.append-raw-builtin",
    "java.effect.remove-timeline-fx",
    "java.export.compile",
    "java.export.configure",
    "java.sticker.add",
    "java.sticker.add-custom",
    "java.sticker.remove",
    "java.timeline.append-clip",
    "java.timeline.append-trimmed-clip",
    "java.timeline.build-picture-in-picture",
    "java.timeline.build-quick-splice",
    "java.timeline.append-media-list",
    "java.app.restore-timeline-structure",
    "java.editor.clear-supported-features",
    "java.editor.restore-supported-features",
    "java.clip.trim-out-at-playhead",
    "java.clip.remove-at",
    "java.clip.move",
    "java.clip.split-at-playhead",
    "java.timeline.remove",
    "java.transition.set-builtin",
    "java.transition.set-packaged",
    "java.export.compile-configured",
    "java.effect.append-builtin-range",
    "java.effect.append-raw-builtin-range",
    "java.audio.append-clip-default",
    "java.clip.change-speed",
    "java.clip.change-trim-in",
    "java.clip.move-to-timeline-position",
    "java.effect.append-packaged-range",
}

UNIT_API_SIGNATURES = {
    "java.sdk.initialize": [
        "NvsStreamingContext#init(Landroid/content/Context;Ljava/lang/String;I)Lcom/meicam/sdk/NvsStreamingContext;",
    ],
    "java.asset-center.register-bundled-font": [
        "NvsStreamingContext#registerFontByFilePath(Ljava/lang/String;)Ljava/lang/String;",
    ],
    "java.timeline.create": [
        "NvsStreamingContext#createTimeline(Lcom/meicam/sdk/NvsVideoResolution;Lcom/meicam/sdk/NvsRational;Lcom/meicam/sdk/NvsAudioResolution;)Lcom/meicam/sdk/NvsTimeline;",
    ],
    "java.preview.play": [
        "NvsStreamingContext#playbackTimeline(Lcom/meicam/sdk/NvsTimeline;JJIZI)Z",
    ],
    "java.preview.seek": [
        "NvsStreamingContext#seekTimeline(Lcom/meicam/sdk/NvsTimeline;JII)Z",
    ],
    "java.beauty.effect-sdk-init": [
        "NvsEffectSdkContext#init(Landroid/content/Context;Ljava/lang/String;I)Lcom/meicam/effect/sdk/NvsEffectSdkContext;",
    ],
    "java.caption.list-timeline": [
        "NvsTimeline#getNextCaption(Lcom/meicam/sdk/NvsTimelineCaption;)Lcom/meicam/sdk/NvsTimelineCaption;",
    ],
    "java.caption.list-compound": [
        "NvsTimeline#getNextCaption(Lcom/meicam/sdk/NvsTimelineCompoundCaption;)Lcom/meicam/sdk/NvsTimelineCompoundCaption;",
    ],
    "java.caption.list-clip": [
        "NvsVideoClip#getNextCaption(Lcom/meicam/sdk/NvsClipCaption;)Lcom/meicam/sdk/NvsClipCaption;",
    ],
    "java.caption.list-clip-compound": [
        "NvsVideoClip#getNextCaption(Lcom/meicam/sdk/NvsClipCompoundCaption;)Lcom/meicam/sdk/NvsClipCompoundCaption;",
    ],
    "java.sdk.initialize-activity": [
        "NvsStreamingContext#init(Landroid/app/Activity;Ljava/lang/String;I)Lcom/meicam/sdk/NvsStreamingContext;",
    ],
    "java.timeline.create-template-with-flags": [
        "NvsStreamingContext#createTimeline(Ljava/lang/String;Ljava/util/List;I)Lcom/meicam/sdk/NvsTimeline;",
    ],
    "java.preview.play-with-fps": [
        "NvsStreamingContext#playbackTimeline(Lcom/meicam/sdk/NvsTimeline;JJLcom/meicam/sdk/NvsRational;ZI)Z",
    ],
    "java.preview.seek-with-fps": [
        "NvsStreamingContext#seekTimeline(Lcom/meicam/sdk/NvsTimeline;JLcom/meicam/sdk/NvsRational;I)Z",
    ],
    "java.capture.start-recording-configured": [
        "NvsStreamingContext#startRecording(Ljava/lang/String;ILjava/util/Hashtable;)Z",
    ],
    "java.sdk.initialize-activity-default": [
        "NvsStreamingContext#init(Landroid/app/Activity;Ljava/lang/String;)Lcom/meicam/sdk/NvsStreamingContext;",
    ],
    "java.timeline.create-with-flags": [
        "NvsStreamingContext#createTimeline(Lcom/meicam/sdk/NvsVideoResolution;Lcom/meicam/sdk/NvsRational;Lcom/meicam/sdk/NvsAudioResolution;I)Lcom/meicam/sdk/NvsTimeline;",
    ],
    "java.timeline.create-template-configured": [
        "NvsStreamingContext#createTimeline(Ljava/lang/String;Ljava/util/List;ILcom/meicam/sdk/NvsRational;Lcom/meicam/sdk/NvsAudioResolution;)Lcom/meicam/sdk/NvsTimeline;",
    ],
    "java.export.compile-configured": [
        "NvsStreamingContext#compileTimeline(Lcom/meicam/sdk/NvsTimeline;JJLjava/lang/String;IILjava/util/Hashtable;I)Z",
    ],
    "java.beauty.initialize-human-detection-configured": [
        "NvsStreamingContext#initHumanDetection(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ILjava/util/Hashtable;)Z",
    ],
    "java.beauty.initialize-human-detection-ext-configured": [
        "NvsStreamingContext#initHumanDetectionExt(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ILjava/util/Hashtable;)Z",
    ],
    "java.capture.stop-recording-synchronous": [
        "NvsStreamingContext#stopRecording(Z)V",
    ],
    "java.effect.append-builtin-range": [
        "NvsVideoClip#appendBuiltinFx(Ljava/lang/String;JJ)Lcom/meicam/sdk/NvsVideoFx;",
    ],
    "java.effect.append-raw-builtin-range": [
        "NvsVideoClip#appendRawBuiltinFx(Ljava/lang/String;JJ)Lcom/meicam/sdk/NvsVideoFx;",
    ],
    "java.audio.append-clip-default": [
        "NvsAudioTrack#appendClip(Ljava/lang/String;)Lcom/meicam/sdk/NvsAudioClip;",
    ],
    "java.clip.change-speed": [
        "NvsClip#changeSpeed(D)V",
    ],
    "java.clip.change-trim-in": [
        "NvsClip#changeTrimInPoint(JZ)J",
    ],
    "java.caption.set-compound-text": [
        "NvsCompoundCaption#setText(ILjava/lang/String;)V",
    ],
    "java.beauty.effect-sdk-init-activity-default": [
        "NvsEffectSdkContext#init(Landroid/app/Activity;Ljava/lang/String;)Lcom/meicam/effect/sdk/NvsEffectSdkContext;",
    ],
    "java.beauty.effect-human-detection-ext-configured": [
        "NvsEffectSdkContext#initHumanDetectionExt(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ILjava/util/Hashtable;)Z",
    ],
    "java.export.register-callback3": [
        "NvsStreamingContext#setCompileCallback3(Lcom/meicam/sdk/NvsStreamingContext$CompileCallback3;)V",
    ],
    "java.clip.move-to-timeline-position": [
        "NvsTrack#moveClip(IJZZ)Z",
    ],
    "java.audio.set-track-stereo-volume": [
        "NvsTrack#setVolumeGain(FF)V",
    ],
    "java.effect.append-packaged-range": [
        "NvsVideoClip#appendPackagedFx(Ljava/lang/String;JJ)Lcom/meicam/sdk/NvsVideoFx;",
    ],
}

JAVA_UNIT_SPECS.extend(
    [
        (
            "java.asset-center.list-bundled-materials",
            "List bundled materials by local family",
            "asset-center-service",
            "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheLocalMaterialOperations.java",
            "matchingIndexes",
            [],
            ["local material family"],
            ["bundled material entries"],
        ),
        (
            "java.asset-center.install-bundled-package",
            "Install a selected bundled material package",
            "asset-center-service",
            "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheLocalMaterialOperations.java",
            "installBundledPackage",
            ["NvsAssetPackageManager.installAssetPackage", "NvsAssetPackageManager.upgradeAssetPackage"],
            ["selected bundled material", "initialized SDK"],
            ["installed package id and package type"],
        ),
        (
            "java.asset-center.register-bundled-font",
            "Copy and register a bundled caption font",
            "asset-center-service",
            "assets/android-feature-templates/asset-center/app/src/main/java/{{PACKAGE_PATH}}/MeisheLocalMaterialOperations.java",
            "registerBundledFont",
            ["NvsStreamingContext.registerFontByFilePath"],
            ["bundled font entry", "app-private file directory"],
            ["registered font family and local path"],
        ),
        (
            "java.audio.add-voiceover",
            "Place a recorded voiceover on an audio track",
            "voiceover-editor",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "addVoiceoverClip",
            ["NvsAudioTrack.addClip"],
            ["audio track", "recorded audio path", "timeline and trim range"],
            ["NvsAudioClip voiceover"],
        ),
        (
            "java.audio.apply-equalizer",
            "Create or update a video clip Audio EQ band",
            "audio-equalizer",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "applyVideoClipEqualizer",
            [
                "NvsVideoClip.getAudioFxCount",
                "NvsVideoClip.getAudioFxByIndex",
                "NvsVideoClip.appendAudioFx",
                "NvsFx.setFloatVal",
            ],
            ["video clip", "Audio EQ band key", "gain"],
            ["configured NvsAudioFx"],
        ),
        (
            "java.effect.apply-mask-region",
            "Apply reusable Mask Generator region data to a clip",
            "mask-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "applyMaskRegion",
            [
                "NvsVideoClip.appendRawBuiltinFx",
                "NvsFx.setArbDataVal",
                "NvsFx.setFloatVal",
                "NvsFx.setBooleanVal",
            ],
            ["video clip", "NvsMaskRegionInfo", "feather width", "inverse flag"],
            ["Mask Generator NvsVideoFx"],
        ),
        (
            "java.effect.apply-solid-background",
            "Configure the clip property FX with a solid background",
            "background-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "applySolidBackground",
            [
                "NvsVideoClip.enablePropertyVideoFx",
                "NvsVideoClip.getPropertyVideoFx",
                "NvsFx.setMenuVal",
                "NvsFx.setColorVal",
            ],
            ["video clip", "background color", "transform values"],
            ["configured property NvsVideoFx"],
        ),
        (
            "java.effect.add-watermark",
            "Replace the current timeline watermark",
            "watermark-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "addTimelineWatermark",
            ["NvsTimeline.deleteWatermark", "NvsTimeline.addWatermark"],
            ["timeline", "watermark image", "size", "position", "margins"],
            ["watermark application result"],
        ),
        (
            "java.effect.add-particle",
            "Add a packaged particle timeline effect",
            "particle-effects",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "addParticleFx",
            ["NvsTimeline.addPackagedTimelineVideoFx", "NvsFx.setFloatVal"],
            ["timeline range", "installed particle package id", "tail duration"],
            ["particle NvsTimelineVideoFx"],
        ),
        (
            "java.capture.append-glitter",
            "Append and configure the built-in Glitter capture effect",
            "glitter-effects",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "appendGlitterCaptureFx",
            ["NvsStreamingContext.appendBuiltinCaptureVideoFx", "NvsFx.setStringVal", "NvsFx.setFloatVal"],
            ["streaming context", "glitter source path", "quantity"],
            ["configured NvsCaptureVideoFx"],
        ),
        (
            "java.caption.add-timed-lyrics",
            "Add parsed lyric lines as timed captions",
            "music-lyrics",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "addTimedLyrics",
            ["NvsTimeline.addCaption"],
            ["timeline", "lyric lines", "in/out points", "caption style package id"],
            ["lyric caption list"],
        ),
        (
            "java.caption.add-flip-storyboard",
            "Render flip-caption XML through a Storyboard timeline effect",
            "flip-caption",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "addFlipCaptionStoryboard",
            ["NvsTimeline.addBuiltinTimelineVideoFx", "NvsFx.setStringVal", "NvsFx.setBooleanVal"],
            ["timeline", "flip-caption storyboard description"],
            ["Storyboard NvsTimelineVideoFx"],
        ),
        (
            "java.makeup.apply-compound",
            "Apply a compound makeup package to a clip AR Scene effect",
            "makeup-editor",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "applyCompoundMakeup",
            ["NvsVideoClip.getFxByIndex", "NvsVideoClip.appendBuiltinFx", "NvsFx.setStringVal"],
            ["video clip", "installed compound makeup package id"],
            ["clip AR Scene NvsVideoFx"],
        ),
        (
            "java.makeup.configure-part",
            "Enable custom makeup and configure package and intensity keys for one makeup type",
            "makeup-service",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "configureMakeupPart",
            [
                "NvsFx.setBooleanVal",
                "NvsFx.setIntVal",
                "NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL",
                "NvsFx.setStringVal",
                "NvsFx.setFloatVal",
            ],
            ["AR Scene FX", "makeup type", "package id", "intensity"],
            ["enabled custom makeup state with package and intensity"],
        ),
        (
            "java.capture.append-scene-keyer",
            "Append the Demo-proven Master Keyer capture scene",
            "capture-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "appendCaptureSceneKeyer",
            ["NvsStreamingContext.appendBuiltinCaptureVideoFx", "NvsFx.setBooleanVal", "NvsFx.setFloatVal"],
            ["streaming context with capture preview"],
            ["configured Master Keyer capture FX"],
        ),
        (
            "java.superzoom.create-output-timeline",
            "Create a preview timeline from NvSuperZoom rendered output",
            "superzoom-ai",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "createSuperZoomPreviewTimeline",
            ["NvsStreamingContext.createTimeline", "NvsTimeline.appendVideoTrack", "NvsVideoTrack.appendClip"],
            ["NvSuperZoom rendered video", "video/audio resolution", "video FPS"],
            ["SuperZoom output NvsTimeline"],
        ),
        (
            "java.template.query-footages",
            "Read nested footage descriptors from an installed template package",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "getTemplateFootages",
            [
                "NvsStreamingContext.getAssetPackageManager",
                "NvsAssetPackageManager.getTemplateFootages",
            ],
            ["streaming context", "installed template id"],
            ["template footage descriptors"],
        ),
        (
            "java.template.query-captions",
            "Read replaceable normal caption descriptors from a template package",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "getTemplateCaptions",
            [
                "NvsStreamingContext.getAssetPackageManager",
                "NvsAssetPackageManager.getTemplateCaptions",
            ],
            ["streaming context", "installed template id"],
            ["template normal caption descriptors"],
        ),
        (
            "java.template.query-compound-captions",
            "Read replaceable compound caption descriptors from a template package",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "getTemplateCompoundCaptions",
            [
                "NvsStreamingContext.getAssetPackageManager",
                "NvsAssetPackageManager.getTemplateCompoundCaptions",
            ],
            ["streaming context", "installed template id"],
            ["template compound caption descriptors"],
        ),
        (
            "java.template.list-replaceable-footage",
            "Flatten nested template descriptors into stable replacement slot ids",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "listReplaceableFootageIds",
            [],
            ["template footage descriptors"],
            ["ordered unique replacement slot ids"],
        ),
        (
            "java.template.list-reverse-footage",
            "Detect replacement slots that require generated reverse media",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "listReverseFootageIds",
            [],
            ["template footage descriptors"],
            ["ordered reverse-media slot ids"],
        ),
        (
            "java.template.validate-footage",
            "Validate every replaceable template slot and required reverse file",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "validateFootageSelections",
            [],
            ["template descriptors", "media map", "reverse-media map"],
            ["deterministic footage validation failures"],
        ),
        (
            "java.template.build-footage",
            "Build SDK templateFootageInfo values from validated descriptor mappings",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "buildTemplateFootage",
            [],
            ["template descriptors", "media map", "reverse-media map"],
            ["SDK template footage list"],
        ),
        (
            "java.template.create-editor-timeline",
            "Create an editable template timeline from replacement footage",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "createTemplateEditorTimeline",
            ["NvsStreamingContext.createTimeline"],
            ["installed template id", "template footage list"],
            ["template editor NvsTimeline"],
        ),
        (
            "java.template.create-cutsame-timeline",
            "Create a CutSame timeline with explicit SDK flags",
            "cutsame-template",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "createCutSameTimeline",
            ["NvsStreamingContext.createTimeline"],
            ["installed CutSame template id", "replacement footage", "timeline flags"],
            ["CutSame NvsTimeline"],
        ),
        (
            "java.template.create-mimo-timeline",
            "Create an SDK template timeline with explicit audio and video settings",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "createConfiguredTemplateTimeline",
            ["NvsStreamingContext.createTimeline"],
            ["installed SDK template id", "replacement footage", "timeline flags", "video FPS", "audio resolution"],
            ["configured template NvsTimeline"],
        ),
        (
            "java.template.replace-captions",
            "Replace normal template captions across nested timelines by replace id",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "replaceTemplateCaptionTexts",
            [
                "NvsObject.getTemplateAttachment",
                "NvsCaption.setText",
                "NvsClip.getInternalTimeline",
            ],
            ["template timeline", "normal caption text map"],
            ["normal caption replacement count"],
        ),
        (
            "java.template.replace-compound-captions",
            "Replace compound template caption items across nested timelines",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "replaceTemplateCompoundCaptionTexts",
            [
                "NvsObject.getTemplateAttachment",
                "NvsCompoundCaption.setText",
                "NvsClip.getInternalTimeline",
            ],
            ["template timeline", "compound caption item text map"],
            ["compound caption item replacement count"],
        ),
        (
            "java.template.reconnect-preview",
            "Stop, reconnect, and seek the LiveWindow after template mutation",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "reconnectTemplatePreview",
            [
                "NvsStreamingContext.stop",
                "NvsStreamingContext.connectTimelineWithLiveWindow",
                "NvsStreamingContext.seekTimeline",
            ],
            ["streaming context", "template timeline", "LiveWindow", "seek position"],
            ["preview refresh result"],
        ),
        (
            "java.template.play",
            "Play the selected template timeline without a standard editor timeline dependency",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "playTemplate",
            ["NvsStreamingContext.playbackTimeline", "NvsTimeline.getDuration"],
            ["streaming context", "selected template timeline", "playback range", "playback flags"],
            ["template playback start result"],
        ),
        (
            "java.template.current-position",
            "Read the current position from the selected template timeline",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "currentTemplatePosition",
            ["NvsStreamingContext.getTimelineCurrentPosition", "NvsTimeline.getDuration"],
            ["streaming context", "selected template timeline"],
            ["clamped template timeline position"],
        ),
        (
            "java.template.register-compile-callbacks",
            "Register compile progress and completion callbacks for template export",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "registerTemplateCompileCallbacks",
            [
                "NvsStreamingContext.setCompileCallback",
                "NvsStreamingContext.setCompileCallback2",
            ],
            ["streaming context", "compile progress callback", "compile completion callback"],
            ["template compile callback registration result"],
        ),
        (
            "java.template.export",
            "Compile the selected template timeline without creating a standard editor timeline",
            "template-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "exportTemplate",
            ["NvsStreamingContext.stop", "NvsStreamingContext.compileTimeline"],
            [
                "streaming context",
                "selected template timeline",
                "compile range",
                "output path",
                "resolution and bitrate grades",
                "compile configurations and flags",
            ],
            ["template compile start result"],
        ),
        (
            "java.template.reverse-register-callback",
            "Register reverse-media conversion callbacks on an explicit Handler",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateReverseController.java",
            "registerCallback",
            [
                "NvsMediaFileConvertor.isReleased",
                "NvsMediaFileConvertor.setMeidaFileConvertorCallback",
            ],
            ["convertor callback", "callback Handler"],
            ["reverse conversion callback registration"],
        ),
        (
            "java.template.reverse-generate",
            "Generate a reverse media file for a template footage slot",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateReverseController.java",
            "generateReverseMedia",
            [
                "NvsMediaFileConvertor.isReleased",
                "NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT",
                "NvsMediaFileConvertor.convertMeidaFile",
            ],
            ["source media", "output file", "trim range", "optional output height"],
            ["reverse conversion task id"],
        ),
        (
            "java.template.reverse-cancel",
            "Cancel an active template reverse-media conversion",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateReverseController.java",
            "cancel",
            ["NvsMediaFileConvertor.isReleased", "NvsMediaFileConvertor.cancelTask"],
            ["reverse conversion task id"],
            ["cancel request"],
        ),
        (
            "java.template.reverse-release",
            "Release the template reverse-media convertor",
            "template-engine",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateReverseController.java",
            "release",
            ["NvsMediaFileConvertor.isReleased", "NvsMediaFileConvertor.release"],
            ["template reverse controller"],
            ["released media convertor"],
        ),
        (
            "java.theme.apply",
            "Replace and configure the current timeline theme",
            "theme-editor",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheTemplateWorkflowController.java",
            "applyTheme",
            [
                "NvsTimeline.removeCurrentTheme",
                "NvsTimeline.applyTheme",
                "NvsTimeline.setThemeTitleCaptionText",
                "NvsTimeline.setThemeTrailerCaptionText",
                "NvsTimeline.setThemeMusicVolumeGain",
            ],
            ["timeline", "installed theme package id", "title", "trailer", "music volume"],
            ["theme application result"],
        ),
        (
            "java.media.probe-url",
            "Probe SDK-readable URL or local media metadata",
            "url-media-import",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "probeUrlMedia",
            ["NvsStreamingContext.getAVInfoFromFile"],
            ["SDK-readable media URL or path", "probe flags"],
            ["NvsAVFileInfo"],
        ),
        (
            "java.workflow.append-photo-album",
            "Append still images as a motion-disabled album track",
            "photo-album",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "appendPhotoAlbum",
            ["NvsTimeline.getVideoTrackByIndex", "NvsVideoTrack.appendClip", "NvsVideoClip.setImageMotionAnimationEnabled"],
            ["timeline", "readable image paths"],
            ["appended image clip count"],
        ),
        (
            "java.workflow.append-theme-shots",
            "Append trimmed and speed-adjusted theme-shoot clips",
            "theme-shoot",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "appendThemeShots",
            ["NvsVideoTrack.appendClip", "NvsClip.changeSpeed"],
            ["timeline", "shot paths", "trim ranges", "speeds"],
            ["appended theme shot count"],
        ),
        (
            "java.workflow.append-recorded-clips",
            "Move recorded clips into an editable timeline",
            "dou-video-workflow",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "appendRecordedClips",
            ["NvsTimeline.getVideoTrackByIndex", "NvsVideoTrack.appendClip"],
            ["timeline", "recorded media paths"],
            ["appended recorded clip count"],
        ),
        (
            "java.workflow.append-boomerang",
            "Build boomerang playback from forward and pre-generated reverse media",
            "boomrang-capture",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "appendBoomerangClips",
            ["NvsTimeline.getVideoTrackByIndex", "NvsVideoTrack.appendClip"],
            ["timeline", "forward media path", "reverse media path"],
            ["boomerang clip pair application result"],
        ),
        (
            "java.media.grab-cover-frame",
            "Grab a timeline bitmap for cover selection",
            "cover-maker",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "grabCoverFrame",
            ["NvsStreamingContext.grabImageFromTimeline", "NvsTimeline.getDuration"],
            ["streaming context", "timeline", "cover position"],
            ["cover Bitmap"],
        ),
        (
            "java.timeline.append-nested",
            "Append or insert a child timeline as a nested clip",
            "sequence-nesting",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "appendNestedTimeline",
            ["NvsVideoTrack.appendTimelineClip", "NvsVideoTrack.insertTimelineClip"],
            ["parent timeline", "child timeline", "head/tail placement"],
            ["nested NvsVideoClip"],
        ),
        (
            "java.media.make-live-photo",
            "Create a live-photo file from compiled video",
            "livephoto-editor",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "makeLivePhoto",
            ["NvsStreamingContext.makeLivePhotoFromVideoFile"],
            ["compiled video", "cover position", "writable live-photo output path"],
            ["live-photo creation result"],
        ),
        (
            "java.media.export-still-frame",
            "Grab and persist one timeline frame as JPEG",
            "still-image-export",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "exportTimelineFrame",
            ["NvsStreamingContext.grabImageFromTimeline", "NvsTimeline.getDuration"],
            ["streaming context", "timeline", "frame position", "output file", "JPEG quality"],
            ["still image output result"],
        ),
    ]
)

JAVA_UNIT_SPECS.extend(
    [
        (
            "java.asset.install-async",
            "Install callback-driven packages such as SDK templates asynchronously",
            "asset-package-service",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAssetInstaller.java",
            "installAsynchronously",
            [
                "NvsAssetPackageManager.setCallbackInterface",
                "NvsAssetPackageManager.installAssetPackage",
                "NvsAssetPackageManager.AssetPackageManagerCallback.onFinishAssetPackageInstallation",
                "NvsAssetPackageManager.AssetPackageManagerCallback.onFinishAssetPackageUpgrading",
            ],
            ["package path", "optional license path", "asset package type", "completion callback"],
            ["accepted start code", "exact asynchronous installation result"],
        ),
        (
            "java.capture.apply-scene",
            "Apply an installed capture scene package during physical preview",
            "capture-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "applyCaptureScene",
            ["NvsStreamingContext.applyCaptureScene"],
            ["streaming context in capture preview", "installed capture scene id"],
            ["capture scene application result"],
        ),
        (
            "java.mimo.parse-package",
            "Parse legacy Mimo info.json without treating it as an SDK template",
            "mimo-template",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMimoWorkflowController.java",
            "parse",
            [],
            ["Mimo info.json input stream"],
            ["validated Mimo shot, effect, caption, and music specification"],
        ),
        (
            "java.mimo.extract-archive",
            "Safely extract a Mimo ZIP and locate its info.json",
            "mimo-template",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMimoWorkflowController.java",
            "extractArchive",
            [],
            ["Mimo ZIP input stream", "private extraction directory"],
            ["extracted Mimo root and info.json"],
        ),
        (
            "java.mimo.install-child-packages",
            "Install effect packages extracted from a Mimo archive",
            "mimo-template",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMimoWorkflowController.java",
            "installChildPackages",
            ["NvsAssetPackageManager.installAssetPackage"],
            ["Android context", "streaming context", "extracted Mimo asset root"],
            ["per-package installation counts and failures"],
        ),
        (
            "java.mimo.install-extracted-child-packages",
            "Install Mimo child packages from an extracted private directory",
            "mimo-template",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMimoWorkflowController.java",
            "installExtractedChildPackages",
            ["NvsAssetPackageManager.installAssetPackage"],
            ["streaming context", "extracted Mimo asset root"],
            ["per-package installation counts and failures"],
        ),
        (
            "java.mimo.build-timeline",
            "Build a normal SDK timeline from Mimo shots and installed child packages",
            "mimo-template",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMimoWorkflowController.java",
            "buildTimeline",
            [
                "NvsStreamingContext.createTimeline",
                "NvsTimeline.appendVideoTrack",
                "NvsVideoTrack.appendClip",
                "NvsVideoClip.appendPackagedFx",
                "NvsVideoTrack.setPackagedTransition",
                "NvsTimeline.addCompoundCaption",
                "NvsTimeline.addPackagedTimelineVideoFx",
                "NvsTimeline.appendAudioTrack",
                "NvsAudioTrack.appendClip",
            ],
            ["Mimo specification", "shot media", "music path", "video/audio resolution"],
            ["Mimo NvsTimeline", "applied element counts", "exact failures"],
        ),
        (
            "java.mimo.reconnect-preview",
            "Stop, connect, and seek a Mimo timeline in LiveWindow",
            "mimo-template",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMimoWorkflowController.java",
            "reconnectPreview",
            [
                "NvsStreamingContext.stop",
                "NvsStreamingContext.connectTimelineWithLiveWindow",
                "NvsStreamingContext.seekTimeline",
            ],
            ["streaming context", "Mimo timeline", "LiveWindow", "position", "seek flags"],
            ["synchronized Mimo preview"],
        ),
        (
            "java.mimo.export",
            "Compile a Mimo timeline with explicit output settings",
            "mimo-template",
            "assets/android-feature-templates/template-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMimoWorkflowController.java",
            "export",
            ["NvsStreamingContext.stop", "NvsStreamingContext.compileTimeline"],
            ["Mimo timeline", "output path", "resolution/bitrate", "compile configuration"],
            ["Mimo compile start result"],
        ),
    ]
)

UNIT_API_SIGNATURES.update(
    {
        "java.capture.register-callbacks": [
            "NvsStreamingContext#setCaptureDeviceCallback(Lcom/meicam/sdk/NvsStreamingContext$CaptureDeviceCallback;)V",
            "NvsStreamingContext#setCaptureRecordingStartedCallback(Lcom/meicam/sdk/NvsStreamingContext$CaptureRecordingStartedCallback;)V",
            "NvsStreamingContext#setCaptureRecordingDurationCallback(Lcom/meicam/sdk/NvsStreamingContext$CaptureRecordingDurationCallback;)V",
            "NvsStreamingContext#setCaptureRecordingFrameReachedCallback(Lcom/meicam/sdk/NvsStreamingContext$CaptureRecordingFrameReachedCallback;)V",
        ],
        "java.capture.pause-recording": [
            "NvsStreamingContext#getStreamingEngineState()I",
            "NvsStreamingContext#isRecordingPaused()Z",
            "NvsStreamingContext#pauseRecording()Z",
        ],
        "java.capture.resume-recording": [
            "NvsStreamingContext#getStreamingEngineState()I",
            "NvsStreamingContext#isRecordingPaused()Z",
            "NvsStreamingContext#resumeRecording()Z",
        ],
        "java.capture.configure-device-controls": [
            "NvsStreamingContext#getCaptureDeviceCapability(I)Lcom/meicam/sdk/NvsStreamingContext$CaptureDeviceCapability;",
            "NvsStreamingContext#getCaptureDeviceCount()I",
            "NvsStreamingContext#getExposureCompensation()I",
            "NvsStreamingContext#getZoom()I",
            "NvsStreamingContext#isCaptureDeviceBackFacing(I)Z",
            "NvsStreamingContext#isFlashOn()Z",
            "NvsStreamingContext#setAutoExposureRect(Landroid/graphics/RectF;)V",
            "NvsStreamingContext#setExposureCompensation(I)V",
            "NvsStreamingContext#setZoom(I)V",
            "NvsStreamingContext#startAutoFocus(Landroid/graphics/RectF;)V",
            "NvsStreamingContext#toggleFlash(Z)V",
        ],
        "java.caption.configure-typography": [
            "NvsCaption#getText()Ljava/lang/String;",
            "NvsCaption#setBackgroundColor(Lcom/meicam/sdk/NvsColor;)V",
            "NvsCaption#setBackgroundRadius(F)V",
            "NvsCaption#setBold(Z)V",
            "NvsCaption#setDrawShadow(Z)V",
            "NvsCaption#setFontByFilePath(Ljava/lang/String;)V",
            "NvsCaption#setItalic(Z)V",
            "NvsCaption#setLineSpacing(F)V",
            "NvsCaption#setOpacity(F)V",
            "NvsCaption#setShadowColor(Lcom/meicam/sdk/NvsColor;)V",
            "NvsCaption#setShadowOffset(Landroid/graphics/PointF;)V",
            "NvsCaption#setUnderline(Z)V",
        ],
        "java.caption.configure-transform": [
            "NvsCaption#setCaptionTranslation(Landroid/graphics/PointF;)V",
            "NvsCaption#setCurrentKeyFrameTime(J)V",
            "NvsCaption#setRecordingUserOperation(Z)V",
            "NvsCaption#setRotationZ(F)V",
            "NvsCaption#setScaleX(F)V",
            "NvsCaption#setScaleY(F)V",
            "NvsCaption#setZValue(F)V",
        ],
        "java.caption.apply-modular-assets": [
            "NvsCaption#applyCaptionStyle(Ljava/lang/String;)Z",
            "NvsCaption#applyModularCaptionAnimation(Ljava/lang/String;)Z",
            "NvsCaption#applyModularCaptionContext(Ljava/lang/String;)Z",
            "NvsCaption#applyModularCaptionInAnimation(Ljava/lang/String;)Z",
            "NvsCaption#applyModularCaptionOutAnimation(Ljava/lang/String;)Z",
            "NvsCaption#applyModularCaptionRenderer(Ljava/lang/String;)Z",
            "NvsCaption#setModularCaptionAnimationPeroid(I)V",
            "NvsCaption#setModularCaptionInAnimationDuration(I)V",
            "NvsCaption#setModularCaptionOutAnimationDuration(I)V",
        ],
        "java.sticker.configure-animation-transform": [
            "NvsAnimatedSticker#applyAnimatedStickerInAnimation(Ljava/lang/String;)Z",
            "NvsAnimatedSticker#applyAnimatedStickerOutAnimation(Ljava/lang/String;)Z",
            "NvsAnimatedSticker#applyAnimatedStickerPeriodAnimation(Ljava/lang/String;)Z",
            "NvsAnimatedSticker#getHorizontalFlip()Z",
            "NvsAnimatedSticker#rotateAnimatedSticker(F)V",
            "NvsAnimatedSticker#scaleAnimatedSticker(FLandroid/graphics/PointF;)V",
            "NvsAnimatedSticker#setAnimatedStickerAnimationPeriod(I)V",
            "NvsAnimatedSticker#setAnimatedStickerInAnimationDuration(I)V",
            "NvsAnimatedSticker#setAnimatedStickerOutAnimationDuration(I)V",
            "NvsAnimatedSticker#setHorizontalFlip(Z)V",
            "NvsAnimatedSticker#setVolumeGain(FF)V",
            "NvsAnimatedSticker#setZValue(F)V",
            "NvsAnimatedSticker#translateAnimatedSticker(Landroid/graphics/PointF;)V",
        ],
        "java.clip.add-caption": [
            "NvsVideoClip#addCaption(Ljava/lang/String;JJLjava/lang/String;)Lcom/meicam/sdk/NvsClipCaption;",
        ],
        "java.clip.add-modular-caption": [
            "NvsVideoClip#addModularCaption(Ljava/lang/String;JJ)Lcom/meicam/sdk/NvsClipCaption;",
        ],
        "java.clip.add-animated-sticker": [
            "NvsVideoClip#addAnimatedSticker(JJLjava/lang/String;)Lcom/meicam/sdk/NvsClipAnimatedSticker;",
            "NvsVideoClip#addCustomAnimatedSticker(JJLjava/lang/String;Ljava/lang/String;)Lcom/meicam/sdk/NvsClipAnimatedSticker;",
        ],
        "java.clip.list-animated-stickers": [
            "NvsVideoClip#getFirstAnimatedSticker()Lcom/meicam/sdk/NvsClipAnimatedSticker;",
            "NvsVideoClip#getNextAnimatedSticker(Lcom/meicam/sdk/NvsClipAnimatedSticker;)Lcom/meicam/sdk/NvsClipAnimatedSticker;",
        ],
        "java.clip.remove-caption": [
            "NvsVideoClip#removeCaption(Lcom/meicam/sdk/NvsClipCaption;)Lcom/meicam/sdk/NvsClipCaption;",
        ],
        "java.clip.remove-animated-sticker": [
            "NvsVideoClip#removeAnimatedSticker(Lcom/meicam/sdk/NvsClipAnimatedSticker;)Lcom/meicam/sdk/NvsClipAnimatedSticker;",
        ],
    }
)

UNIT_API_SIGNATURES.update(
    {
        "java.clip.configure-advanced-playback": [
            "NvsVideoClip#changeVariableSpeed(DDZ)V",
            "NvsVideoClip#disableAmbiguousCrop(Z)V",
            "NvsVideoClip#enableRawSourceMode(Z)V",
            "NvsVideoClip#getClipWrapMode()I",
            "NvsVideoClip#getExtraVideoRotation()I",
            "NvsVideoClip#getPlayInReverse()Z",
            "NvsVideoClip#getSourceBackgroundMode()I",
            "NvsVideoClip#isAmbiguousCropDisabled()Z",
            "NvsVideoClip#setClipWrapMode(I)V",
            "NvsVideoClip#setExtraVideoRotation(I)V",
            "NvsVideoClip#setPlayInReverse(Z)V",
            "NvsVideoClip#setSoftWareDecoding(Z)V",
            "NvsVideoClip#setSourceBackgroundMode(I)V",
        ],
        "java.clip.configure-image-regions": [
            "NvsVideoClip#getEndROI()Landroid/graphics/RectF;",
            "NvsVideoClip#getImageMaskROI()Landroid/graphics/RectF;",
            "NvsVideoClip#getStartROI()Landroid/graphics/RectF;",
            "NvsVideoClip#setImageMaskROI(Landroid/graphics/RectF;)V",
            "NvsVideoClip#setImageMotionROI(Landroid/graphics/RectF;Landroid/graphics/RectF;)V",
        ],
        "java.effect.set-float-keyframe": [
            "NvsFx#getFloatValAtTime(Ljava/lang/String;J)D",
            "NvsFx#hasKeyframeList(Ljava/lang/String;)Z",
            "NvsFx#setFloatValAtTime(Ljava/lang/String;DJ)V",
        ],
        "java.effect.remove-nearest-keyframe": [
            "NvsFx#findKeyframeTime(Ljava/lang/String;JI)J",
            "NvsFx#removeKeyframeAtTime(Ljava/lang/String;J)Z",
        ],
        "java.effect.set-position-parameters": [
            "NvsFx#getPosition2DVal(Ljava/lang/String;)Lcom/meicam/sdk/NvsPosition2D;",
            "NvsFx#getPosition3DVal(Ljava/lang/String;)Lcom/meicam/sdk/NvsPosition3D;",
            "NvsFx#setPosition2DVal(Ljava/lang/String;Lcom/meicam/sdk/NvsPosition2D;)V",
            "NvsFx#setPosition3DVal(Ljava/lang/String;Lcom/meicam/sdk/NvsPosition3D;)V",
        ],
        "java.transition.configure-timing": [
            "NvsVideoTransition#enableTimelineTransition(Z)V",
            "NvsVideoTransition#getVideoTransitionDuration()J",
            "NvsVideoTransition#getVideoTransitionDurationMatchMode()I",
            "NvsVideoTransition#setVideoTransitionDuration(JI)V",
            "NvsVideoTransition#setVideoTransitionDurationScaleFactor(F)V",
        ],
        "java.particle.configure-emitter": [
            "NvsParticleSystemContext#appendPositionToEmitterPositionCurve(Ljava/lang/String;FFF)V",
            "NvsParticleSystemContext#setEmitterParticleSizeGain(Ljava/lang/String;F)V",
            "NvsParticleSystemContext#setEmitterRateGain(Ljava/lang/String;F)V",
        ],
        "java.preview.grab-image-async": [
            "NvsStreamingContext#grabImageFromTimelineAsync(Lcom/meicam/sdk/NvsTimeline;JLcom/meicam/sdk/NvsRational;I)Z",
            "NvsStreamingContext#setImageGrabberCallback(Lcom/meicam/sdk/NvsStreamingContext$ImageGrabberCallback;)V",
        ],
        "java.preview.map-live-window-point": [
            "NvsLiveWindow#mapCanonicalToView(Landroid/graphics/PointF;)Landroid/graphics/PointF;",
            "NvsLiveWindow#mapNormalizedToView(Landroid/graphics/PointF;)Landroid/graphics/PointF;",
            "NvsLiveWindow#mapViewToCanonical(Landroid/graphics/PointF;)Landroid/graphics/PointF;",
            "NvsLiveWindow#mapViewToNormalized(Landroid/graphics/PointF;)Landroid/graphics/PointF;",
        ],
        "java.preview.configure-thumbnail-sequence": [
            "NvsMultiThumbnailSequenceView#getPixelPerMicrosecond()D",
            "NvsMultiThumbnailSequenceView#scaleWithAnchor(DI)V",
            "NvsMultiThumbnailSequenceView#setEndPadding(I)V",
            "NvsMultiThumbnailSequenceView#setOnScrollChangeListenser(Lcom/meicam/sdk/NvsMultiThumbnailSequenceView$OnScrollChangeListener;)V",
            "NvsMultiThumbnailSequenceView#setPixelPerMicrosecond(D)V",
            "NvsMultiThumbnailSequenceView#setStartPadding(I)V",
            "NvsMultiThumbnailSequenceView#setThumbnailSequenceDescArray(Ljava/util/ArrayList;)V",
        ],
        "java.timeline.add-clip-at-position": [
            "NvsVideoTrack#addClip(Ljava/lang/String;JJJ)Lcom/meicam/sdk/NvsVideoClip;",
            "NvsVideoTrack#getClipByTimelinePosition(J)Lcom/meicam/sdk/NvsVideoClip;",
        ],
        "java.timeline.insert-clip-at-index": [
            "NvsVideoTrack#insertClip(Ljava/lang/String;JJI)Lcom/meicam/sdk/NvsVideoClip;",
        ],
        "java.timeline.configure-structure": [
            "NvsStreamingContext#stop()V",
            "NvsTimeline#audioTrackCount()I",
            "NvsTimeline#changeVideoSize(II)Z",
            "NvsTimeline#getAudioFadeOutDuration()J",
            "NvsTimeline#removeAudioTrack(I)Z",
            "NvsTimeline#removeVideoTrack(I)Z",
            "NvsTimeline#setAudioFadeOutDuration(J)V",
            "NvsTimeline#videoTrackCount()I",
        ],
    }
)

UNIT_API_SIGNATURES.update(
    {
        "java.asset.inspect-package": [
            "NvsAssetPackageManager#ASSET_PACKAGE_TYPE_ARSCENE:I",
            "NvsAssetPackageManager#getARSceneAssetPackageCameraPreset(Ljava/lang/String;)Lcom/meicam/sdk/NvsAssetPackageManager$ARSceneCameraPreset;",
            "NvsAssetPackageManager#getARSceneAssetPackagePrompt(Ljava/lang/String;)Ljava/lang/String;",
            "NvsAssetPackageManager#getAssetPackageStatus(Ljava/lang/String;I)I",
            "NvsAssetPackageManager#getAssetPackageSupportedAspectRatio(Ljava/lang/String;I)I",
            "NvsAssetPackageManager#getVideoFxAssetPackageDescription(Ljava/lang/String;)Ljava/lang/String;",
            "NvsAssetPackageManager#isARSceneAssetPackageContainFaceMesh(Ljava/lang/String;)Z",
            "NvsAssetPackageManager#isARSceneAssetPackageContainWarp(Ljava/lang/String;)Z",
        ],
        "java.media.create-frame-retriever": [
            "NvsStreamingContext#createVideoFrameRetriever(Ljava/lang/String;)Lcom/meicam/sdk/NvsVideoFrameRetriever;",
        ],
        "java.media.retrieve-frame": [
            "NvsVideoFrameRetriever#getFrameAtTime(JI)Landroid/graphics/Bitmap;",
            "NvsVideoFrameRetriever#getFrameAtTimeWithCustomVideoFrameHeight(JI)Landroid/graphics/Bitmap;",
        ],
        "java.media.release-frame-retriever": [
            "NvsVideoFrameRetriever#release()V",
        ],
        "java.beauty.append-capture-fx": [
            "NvsStreamingContext#appendBeautyCaptureVideoFx()Lcom/meicam/sdk/NvsCaptureVideoFx;",
        ],
        "java.beauty.effect-sdk-init-activity-flags": [
            "NvsEffectSdkContext#init(Landroid/app/Activity;Ljava/lang/String;I)Lcom/meicam/effect/sdk/NvsEffectSdkContext;",
        ],
        "java.beauty.configure-ar-manipulation": [
            "NvsARSceneManipulate#CheckedFunctionType_Matte:I",
            "NvsARSceneManipulate#isFunctionAvailable(I)Z",
            "NvsARSceneManipulate#setARSceneCallback(Lcom/meicam/sdk/NvsARSceneManipulate$NvsARSceneManipulateCallback;)V",
            "NvsARSceneManipulate#setDetectionAutoProbe(Z)V",
            "NvsARSceneManipulate#setDetectionMode(I)V",
            "NvsFx#getARSceneManipulate()Lcom/meicam/sdk/NvsARSceneManipulate;",
        ],
        "java.media.convert-passthrough": [
            "NvsPassthroughConvertor#convertMediaFile(Ljava/util/List;Ljava/lang/String;Ljava/util/Hashtable;I)J",
            "NvsPassthroughConvertor#setPassthroughConvertorCallback(Lcom/meicam/sdk/NvsPassthroughConvertor$PassthroughConvertorCallback;Landroid/os/Handler;)V",
        ],
        "java.audio.append-clip-fx": [
            "NvsAudioClip#appendFx(Ljava/lang/String;)Lcom/meicam/sdk/NvsAudioFx;",
            "NvsAudioFx#getBuiltinAudioFxName()Ljava/lang/String;",
        ],
        "java.audio.replace-clip-fx": [
            "NvsAudioClip#getFxByIndex(I)Lcom/meicam/sdk/NvsAudioFx;",
            "NvsAudioClip#insertFx(Ljava/lang/String;I)Lcom/meicam/sdk/NvsAudioFx;",
            "NvsAudioClip#removeFx(I)Z",
        ],
        "java.audio.configure-transition": [
            "NvsAudioTrack#getTransitionWithSourceClipIndex(I)Lcom/meicam/sdk/NvsAudioTransition;",
            "NvsAudioTrack#setBuiltinTransition(ILjava/lang/String;)Lcom/meicam/sdk/NvsAudioTransition;",
        ],
        "java.beauty.initialize-human-detection": [
            "NvsEffectSdkContext#initHumanDetection(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;I)Z",
            "NvsEffectSdkContext#initHumanDetectionExt(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;I)Z",
            "NvsEffectSdkContext#setupHumanDetectionData(ILjava/lang/String;)Z",
        ],
    }
)

UNIT_COMPOSE_AFTER.update(
    {
        "java.asset-center.list-bundled-materials": [],
        "java.asset-center.install-bundled-package": [
            "java.sdk.initialize",
            "java.asset-center.list-bundled-materials",
        ],
        "java.asset-center.register-bundled-font": [
            "java.sdk.initialize",
            "java.asset-center.list-bundled-materials",
        ],
        "java.asset.install-async": ["java.sdk.initialize"],
        "java.audio.add-voiceover": ["java.audio.ensure-track", "java.engine.stop"],
        "java.audio.apply-equalizer": ["java.timeline.append-clip", "java.engine.stop"],
        "java.effect.apply-mask-region": ["java.timeline.append-clip", "java.engine.stop"],
        "java.effect.apply-solid-background": ["java.timeline.append-clip", "java.engine.stop"],
        "java.effect.add-watermark": ["java.timeline.create", "java.engine.stop"],
        "java.effect.add-particle": ["java.asset.install-or-upgrade", "java.timeline.create", "java.engine.stop"],
        "java.capture.append-glitter": ["java.capture.start-preview"],
        "java.caption.add-timed-lyrics": ["java.timeline.create", "java.engine.stop"],
        "java.caption.add-flip-storyboard": ["java.timeline.create", "java.engine.stop"],
        "java.makeup.apply-compound": ["java.asset.install-or-upgrade", "java.timeline.append-clip", "java.engine.stop"],
        "java.makeup.configure-part": [
            "java.asset.install-or-upgrade",
            "java.beauty.append-ar-scene",
        ],
        "java.capture.apply-scene": [
            "java.asset.install-or-upgrade",
            "java.capture.start-preview",
        ],
        "java.capture.append-scene-keyer": ["java.capture.apply-scene"],
        "java.superzoom.create-output-timeline": ["java.sdk.initialize", "java.media.probe"],
        "java.template.query-footages": ["java.asset.install-async"],
        "java.template.query-captions": ["java.asset.install-async"],
        "java.template.query-compound-captions": ["java.asset.install-async"],
        "java.template.list-replaceable-footage": ["java.template.query-footages"],
        "java.template.list-reverse-footage": ["java.template.query-footages"],
        "java.template.reverse-register-callback": ["java.sdk.initialize"],
        "java.template.reverse-generate": [
            "java.media.probe",
            "java.template.list-reverse-footage",
            "java.template.reverse-register-callback",
        ],
        "java.template.validate-footage": [
            "java.template.list-replaceable-footage",
            "java.template.list-reverse-footage",
        ],
        "java.template.build-footage": ["java.template.validate-footage"],
        "java.template.create-editor-timeline": ["java.template.build-footage"],
        "java.template.create-cutsame-timeline": ["java.template.build-footage"],
        "java.template.create-mimo-timeline": ["java.template.build-footage"],
        "java.template.replace-captions": [
            "java.template.query-captions",
            "java.template.build-footage",
            "java.engine.stop",
        ],
        "java.template.replace-compound-captions": [
            "java.template.query-compound-captions",
            "java.template.build-footage",
            "java.engine.stop",
        ],
        "java.template.reconnect-preview": [
            "java.template.replace-captions",
            "java.template.replace-compound-captions",
        ],
        "java.template.play": ["java.template.reconnect-preview"],
        "java.template.current-position": ["java.template.reconnect-preview"],
        "java.template.register-compile-callbacks": ["java.sdk.initialize"],
        "java.template.export": [
            "java.template.reconnect-preview",
            "java.template.register-compile-callbacks",
        ],
        "java.template.reverse-cancel": ["java.template.reverse-generate"],
        "java.template.reverse-release": ["java.template.reverse-register-callback"],
        "java.mimo.extract-archive": ["java.sdk.initialize"],
        "java.mimo.parse-package": ["java.sdk.initialize"],
        "java.mimo.install-child-packages": ["java.mimo.parse-package"],
        "java.mimo.install-extracted-child-packages": [
            "java.mimo.extract-archive",
            "java.mimo.parse-package",
        ],
        "java.mimo.build-timeline": [
            "java.mimo.install-extracted-child-packages",
            "java.engine.stop",
        ],
        "java.mimo.reconnect-preview": ["java.mimo.build-timeline"],
        "java.mimo.export": ["java.mimo.reconnect-preview"],
        "java.theme.apply": ["java.asset.install-or-upgrade", "java.timeline.create", "java.engine.stop"],
        "java.media.probe-url": ["java.sdk.initialize"],
        "java.workflow.append-photo-album": ["java.timeline.create", "java.engine.stop"],
        "java.workflow.append-theme-shots": ["java.timeline.create", "java.engine.stop"],
        "java.workflow.append-recorded-clips": ["java.timeline.create", "java.engine.stop"],
        "java.workflow.append-boomerang": ["java.timeline.create", "java.engine.stop"],
        "java.media.grab-cover-frame": ["java.timeline.create"],
        "java.timeline.append-nested": ["java.timeline.create", "java.engine.stop"],
        "java.media.make-live-photo": ["java.export.compile"],
        "java.media.export-still-frame": ["java.timeline.create"],
    }
)

UNIT_LIFECYCLE_HOOKS.update(
    {
        "java.asset-center.list-bundled-materials": "activity_create",
        "java.asset-center.install-bundled-package": "asset_installed",
        "java.asset-center.register-bundled-font": "asset_installed",
        "java.asset.install-async": "activity_create",
        "java.audio.add-voiceover": "before_structural_mutation",
        "java.audio.apply-equalizer": "before_structural_mutation",
        "java.effect.apply-mask-region": "before_structural_mutation",
        "java.effect.apply-solid-background": "before_structural_mutation",
        "java.effect.add-watermark": "before_structural_mutation",
        "java.effect.add-particle": "asset_installed",
        "java.capture.append-glitter": "activity_create",
        "java.capture.apply-scene": "asset_installed",
        "java.caption.add-timed-lyrics": "before_structural_mutation",
        "java.caption.add-flip-storyboard": "before_structural_mutation",
        "java.makeup.apply-compound": "asset_installed",
        "java.makeup.configure-part": "asset_installed",
        "java.capture.append-scene-keyer": "activity_create",
        "java.superzoom.create-output-timeline": "timeline_created",
        "java.template.query-footages": "asset_installed",
        "java.template.query-captions": "asset_installed",
        "java.template.query-compound-captions": "asset_installed",
        "java.template.list-replaceable-footage": "asset_installed",
        "java.template.list-reverse-footage": "asset_installed",
        "java.template.validate-footage": "asset_installed",
        "java.template.build-footage": "asset_installed",
        "java.template.create-editor-timeline": "timeline_created",
        "java.template.create-cutsame-timeline": "timeline_created",
        "java.template.create-mimo-timeline": "timeline_created",
        "java.template.replace-captions": "before_structural_mutation",
        "java.template.replace-compound-captions": "before_structural_mutation",
        "java.template.reconnect-preview": "after_mutation_refresh",
        "java.template.play": "live_window_bound",
        "java.template.current-position": "live_window_bound",
        "java.template.register-compile-callbacks": "activity_create",
        "java.template.export": "before_structural_mutation",
        "java.template.reverse-register-callback": "activity_create",
        "java.template.reverse-generate": "activity_create",
        "java.template.reverse-cancel": "destroy",
        "java.template.reverse-release": "destroy",
        "java.mimo.extract-archive": "activity_create",
        "java.mimo.parse-package": "activity_create",
        "java.mimo.install-child-packages": "asset_installed",
        "java.mimo.install-extracted-child-packages": "asset_installed",
        "java.mimo.build-timeline": "timeline_created",
        "java.mimo.reconnect-preview": "after_mutation_refresh",
        "java.mimo.export": "before_structural_mutation",
        "java.theme.apply": "asset_installed",
        "java.media.probe-url": "activity_create",
        "java.workflow.append-photo-album": "before_structural_mutation",
        "java.workflow.append-theme-shots": "before_structural_mutation",
        "java.workflow.append-recorded-clips": "before_structural_mutation",
        "java.workflow.append-boomerang": "before_structural_mutation",
        "java.media.grab-cover-frame": "after_mutation_refresh",
        "java.timeline.append-nested": "before_structural_mutation",
        "java.media.make-live-photo": "after_mutation_refresh",
        "java.media.export-still-frame": "after_mutation_refresh",
    }
)

STRUCTURAL_MUTATION_UNIT_IDS.update(
    {
        "java.audio.add-voiceover",
        "java.audio.apply-equalizer",
        "java.effect.apply-mask-region",
        "java.effect.apply-solid-background",
        "java.effect.add-watermark",
        "java.effect.add-particle",
        "java.caption.add-timed-lyrics",
        "java.caption.add-flip-storyboard",
        "java.makeup.apply-compound",
        "java.template.replace-captions",
        "java.template.replace-compound-captions",
        "java.theme.apply",
        "java.workflow.append-photo-album",
        "java.workflow.append-theme-shots",
        "java.workflow.append-recorded-clips",
        "java.workflow.append-boomerang",
        "java.timeline.append-nested",
    }
)

UNIT_API_SIGNATURES.update(
    {
        "java.audio.add-voiceover": [
            "NvsAudioTrack#addClip(Ljava/lang/String;JJJ)Lcom/meicam/sdk/NvsAudioClip;",
        ],
        "java.audio.apply-equalizer": [
            "NvsVideoClip#getAudioFxCount()I",
            "NvsVideoClip#getAudioFxByIndex(I)Lcom/meicam/sdk/NvsAudioFx;",
            "NvsVideoClip#appendAudioFx(Ljava/lang/String;)Lcom/meicam/sdk/NvsAudioFx;",
            "NvsFx#setFloatVal(Ljava/lang/String;D)V",
        ],
        "java.effect.apply-mask-region": [
            "NvsVideoClip#appendRawBuiltinFx(Ljava/lang/String;)Lcom/meicam/sdk/NvsVideoFx;",
            "NvsFx#setArbDataVal(Ljava/lang/String;Lcom/meicam/sdk/NvsArbitraryData;)V",
        ],
        "java.effect.apply-solid-background": [
            "NvsVideoClip#enablePropertyVideoFx(Z)V",
            "NvsVideoClip#getPropertyVideoFx()Lcom/meicam/sdk/NvsVideoFx;",
        ],
        "java.effect.add-watermark": [
            "NvsTimeline#deleteWatermark()V",
            "NvsTimeline#addWatermark(Ljava/lang/String;IIFIII)Z",
        ],
        "java.effect.add-particle": [
            "NvsTimeline#addPackagedTimelineVideoFx(JJLjava/lang/String;)Lcom/meicam/sdk/NvsTimelineVideoFx;",
        ],
        "java.capture.append-glitter": [
            "NvsStreamingContext#appendBuiltinCaptureVideoFx(Ljava/lang/String;)Lcom/meicam/sdk/NvsCaptureVideoFx;",
        ],
        "java.caption.add-timed-lyrics": [
            "NvsTimeline#addCaption(Ljava/lang/String;JJLjava/lang/String;)Lcom/meicam/sdk/NvsTimelineCaption;",
        ],
        "java.caption.add-flip-storyboard": [
            "NvsTimeline#addBuiltinTimelineVideoFx(JJLjava/lang/String;)Lcom/meicam/sdk/NvsTimelineVideoFx;",
        ],
        "java.makeup.apply-compound": [
            "NvsVideoClip#appendBuiltinFx(Ljava/lang/String;)Lcom/meicam/sdk/NvsVideoFx;",
            "NvsFx#setStringVal(Ljava/lang/String;Ljava/lang/String;)V",
        ],
        "java.makeup.configure-part": [
            "NvsFx#setBooleanVal(Ljava/lang/String;Z)V",
            "NvsFx#setIntVal(Ljava/lang/String;I)V",
            "NvsMakeupEffectInfo#MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL:I",
            "NvsFx#setStringVal(Ljava/lang/String;Ljava/lang/String;)V",
            "NvsFx#setFloatVal(Ljava/lang/String;D)V",
        ],
        "java.beauty.apply-ar-scene-package": [
            "NvsFx#setStringVal(Ljava/lang/String;Ljava/lang/String;)V",
            "NvsFx#getStringVal(Ljava/lang/String;)Ljava/lang/String;",
        ],
        "java.beauty.apply-face-mesh-package": [
            "NvsFx#setBooleanVal(Ljava/lang/String;Z)V",
            "NvsFx#setStringVal(Ljava/lang/String;Ljava/lang/String;)V",
            "NvsFx#setFloatVal(Ljava/lang/String;D)V",
            "NvsFx#getStringVal(Ljava/lang/String;)Ljava/lang/String;",
        ],
        "java.capture.append-scene-keyer": [
            "NvsStreamingContext#appendBuiltinCaptureVideoFx(Ljava/lang/String;)Lcom/meicam/sdk/NvsCaptureVideoFx;",
        ],
        "java.superzoom.create-output-timeline": [
            "NvsStreamingContext#createTimeline(Lcom/meicam/sdk/NvsVideoResolution;Lcom/meicam/sdk/NvsRational;Lcom/meicam/sdk/NvsAudioResolution;)Lcom/meicam/sdk/NvsTimeline;",
            "NvsTimeline#appendVideoTrack()Lcom/meicam/sdk/NvsVideoTrack;",
            "NvsVideoTrack#appendClip(Ljava/lang/String;)Lcom/meicam/sdk/NvsVideoClip;",
        ],
        "java.template.query-footages": [
            "NvsStreamingContext#getAssetPackageManager()Lcom/meicam/sdk/NvsAssetPackageManager;",
            "NvsAssetPackageManager#getTemplateFootages(Ljava/lang/String;)Ljava/util/List;",
        ],
        "java.template.query-captions": [
            "NvsStreamingContext#getAssetPackageManager()Lcom/meicam/sdk/NvsAssetPackageManager;",
            "NvsAssetPackageManager#getTemplateCaptions(Ljava/lang/String;)Ljava/util/List;",
        ],
        "java.template.query-compound-captions": [
            "NvsStreamingContext#getAssetPackageManager()Lcom/meicam/sdk/NvsAssetPackageManager;",
            "NvsAssetPackageManager#getTemplateCompoundCaptions(Ljava/lang/String;)Ljava/util/List;",
        ],
        "java.template.create-editor-timeline": [
            "NvsStreamingContext#createTimeline(Ljava/lang/String;Ljava/util/List;)Lcom/meicam/sdk/NvsTimeline;",
        ],
        "java.template.create-cutsame-timeline": [
            "NvsStreamingContext#createTimeline(Ljava/lang/String;Ljava/util/List;I)Lcom/meicam/sdk/NvsTimeline;",
        ],
        "java.template.create-mimo-timeline": [
            "NvsStreamingContext#createTimeline(Ljava/lang/String;Ljava/util/List;ILcom/meicam/sdk/NvsRational;Lcom/meicam/sdk/NvsAudioResolution;)Lcom/meicam/sdk/NvsTimeline;",
        ],
        "java.template.replace-captions": [
            "NvsObject#getTemplateAttachment(Ljava/lang/String;)Ljava/lang/String;",
            "NvsCaption#setText(Ljava/lang/String;)V",
            "NvsClip#getInternalTimeline()Lcom/meicam/sdk/NvsTimeline;",
        ],
        "java.template.replace-compound-captions": [
            "NvsObject#getTemplateAttachment(Ljava/lang/String;)Ljava/lang/String;",
            "NvsCompoundCaption#setText(ILjava/lang/String;)V",
            "NvsClip#getInternalTimeline()Lcom/meicam/sdk/NvsTimeline;",
        ],
        "java.template.reconnect-preview": [
            "NvsStreamingContext#stop()V",
            "NvsStreamingContext#connectTimelineWithLiveWindow(Lcom/meicam/sdk/NvsTimeline;Lcom/meicam/sdk/NvsLiveWindow;)Z",
            "NvsStreamingContext#seekTimeline(Lcom/meicam/sdk/NvsTimeline;JII)Z",
        ],
        "java.template.play": [
            "NvsStreamingContext#playbackTimeline(Lcom/meicam/sdk/NvsTimeline;JJIZI)Z",
        ],
        "java.template.current-position": [
            "NvsStreamingContext#getTimelineCurrentPosition(Lcom/meicam/sdk/NvsTimeline;)J",
        ],
        "java.template.register-compile-callbacks": [
            "NvsStreamingContext#setCompileCallback(Lcom/meicam/sdk/NvsStreamingContext$CompileCallback;)V",
            "NvsStreamingContext#setCompileCallback2(Lcom/meicam/sdk/NvsStreamingContext$CompileCallback2;)V",
        ],
        "java.template.export": [
            "NvsStreamingContext#stop()V",
            "NvsStreamingContext#compileTimeline(Lcom/meicam/sdk/NvsTimeline;JJLjava/lang/String;IILjava/util/Hashtable;I)Z",
        ],
        "java.template.reverse-register-callback": [
            "NvsMediaFileConvertor#isReleased()Z",
            "NvsMediaFileConvertor#setMeidaFileConvertorCallback(Lcom/meicam/sdk/NvsMediaFileConvertor$MeidaFileConvertorCallback;Landroid/os/Handler;)V",
        ],
        "java.template.reverse-generate": [
            "NvsMediaFileConvertor#isReleased()Z",
            "NvsMediaFileConvertor#CONVERTOR_CUSTOM_VIDEO_HEIGHT:Ljava/lang/String;",
            "NvsMediaFileConvertor#convertMeidaFile(Ljava/lang/String;Ljava/lang/String;ZJJLjava/util/Hashtable;)J",
        ],
        "java.template.reverse-cancel": [
            "NvsMediaFileConvertor#isReleased()Z",
            "NvsMediaFileConvertor#cancelTask(J)V",
        ],
        "java.template.reverse-release": [
            "NvsMediaFileConvertor#isReleased()Z",
            "NvsMediaFileConvertor#release()V",
        ],
        "java.theme.apply": [
            "NvsTimeline#removeCurrentTheme()V",
            "NvsTimeline#applyTheme(Ljava/lang/String;)Z",
            "NvsTimeline#setThemeMusicVolumeGain(FF)V",
        ],
        "java.media.probe-url": [
            "NvsStreamingContext#getAVInfoFromFile(Ljava/lang/String;I)Lcom/meicam/sdk/NvsAVFileInfo;",
        ],
        "java.workflow.append-photo-album": [
            "NvsVideoTrack#appendClip(Ljava/lang/String;)Lcom/meicam/sdk/NvsVideoClip;",
            "NvsVideoClip#setImageMotionAnimationEnabled(Z)V",
        ],
        "java.workflow.append-theme-shots": [
            "NvsVideoTrack#appendClip(Ljava/lang/String;JJ)Lcom/meicam/sdk/NvsVideoClip;",
            "NvsClip#changeSpeed(D)V",
        ],
        "java.workflow.append-recorded-clips": [
            "NvsVideoTrack#appendClip(Ljava/lang/String;)Lcom/meicam/sdk/NvsVideoClip;",
        ],
        "java.workflow.append-boomerang": [
            "NvsVideoTrack#appendClip(Ljava/lang/String;)Lcom/meicam/sdk/NvsVideoClip;",
        ],
        "java.media.grab-cover-frame": [
            "NvsStreamingContext#grabImageFromTimeline(Lcom/meicam/sdk/NvsTimeline;JLcom/meicam/sdk/NvsRational;)Landroid/graphics/Bitmap;",
        ],
        "java.timeline.append-nested": [
            "NvsVideoTrack#appendTimelineClip(Lcom/meicam/sdk/NvsTimeline;)Lcom/meicam/sdk/NvsVideoClip;",
            "NvsVideoTrack#insertTimelineClip(Lcom/meicam/sdk/NvsTimeline;I)Lcom/meicam/sdk/NvsVideoClip;",
        ],
        "java.media.make-live-photo": [
            "NvsStreamingContext#makeLivePhotoFromVideoFile(Ljava/lang/String;JLjava/lang/String;)Z",
        ],
        "java.media.export-still-frame": [
            "NvsStreamingContext#grabImageFromTimeline(Lcom/meicam/sdk/NvsTimeline;JLcom/meicam/sdk/NvsRational;)Landroid/graphics/Bitmap;",
        ],
    }
)

JAVA_UNIT_SPECS.extend(
    [
        (
            "java.capture.configure-device-controls",
            "Configure exposure, zoom, focus, and flash on the active capture device",
            "capture-camera",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptureController.java",
            "configureDeviceControls",
            [
                "NvsStreamingContext.getCaptureDeviceCapability",
                "NvsStreamingContext.getCaptureDeviceCount",
                "NvsStreamingContext.isCaptureDeviceBackFacing",
                "NvsStreamingContext.setExposureCompensation",
                "NvsStreamingContext.getExposureCompensation",
                "NvsStreamingContext.setZoom",
                "NvsStreamingContext.getZoom",
                "NvsStreamingContext.setAutoExposureRect",
                "NvsStreamingContext.startAutoFocus",
                "NvsStreamingContext.toggleFlash",
                "NvsStreamingContext.isFlashOn",
            ],
            ["active capture preview", "device index", "device control values"],
            ["applied capture device controls"],
        ),
        (
            "java.caption.configure-typography",
            "Configure caption font, emphasis, spacing, opacity, background, and shadow",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "configureCaptionTypography",
            [
                "NvsCaption.setFontByFilePath",
                "NvsCaption.setBold",
                "NvsCaption.setItalic",
                "NvsCaption.setUnderline",
                "NvsCaption.setLineSpacing",
                "NvsCaption.setOpacity",
                "NvsCaption.setBackgroundColor",
                "NvsCaption.setBackgroundRadius",
                "NvsCaption.setDrawShadow",
                "NvsCaption.setShadowColor",
                "NvsCaption.setShadowOffset",
                "NvsCaption.getText",
            ],
            ["NvsCaption", "font and style parameters"],
            ["configured caption typography"],
        ),
        (
            "java.caption.configure-transform",
            "Configure caption translation, scale, rotation, z order, and keyframe time",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "configureCaptionTransform",
            [
                "NvsCaption.setRecordingUserOperation",
                "NvsCaption.setCurrentKeyFrameTime",
                "NvsCaption.setCaptionTranslation",
                "NvsCaption.setScaleX",
                "NvsCaption.setScaleY",
                "NvsCaption.setRotationZ",
                "NvsCaption.setZValue",
            ],
            ["NvsCaption", "transform values", "keyframe time"],
            ["configured caption transform"],
        ),
        (
            "java.caption.apply-modular-assets",
            "Apply modular caption style, renderer, context, and animation packages",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "applyModularCaptionAssets",
            [
                "NvsCaption.applyCaptionStyle",
                "NvsCaption.applyModularCaptionContext",
                "NvsCaption.applyModularCaptionRenderer",
                "NvsCaption.applyModularCaptionAnimation",
                "NvsCaption.setModularCaptionAnimationPeroid",
                "NvsCaption.applyModularCaptionInAnimation",
                "NvsCaption.setModularCaptionInAnimationDuration",
                "NvsCaption.applyModularCaptionOutAnimation",
                "NvsCaption.setModularCaptionOutAnimationDuration",
            ],
            ["NvsCaption", "installed modular caption package ids", "durations"],
            ["modular caption package application result"],
        ),
        (
            "java.sticker.configure-animation-transform",
            "Configure sticker transform, audio, z order, and modular animations",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "configureAnimatedSticker",
            [
                "NvsAnimatedSticker.translateAnimatedSticker",
                "NvsAnimatedSticker.scaleAnimatedSticker",
                "NvsAnimatedSticker.rotateAnimatedSticker",
                "NvsAnimatedSticker.setHorizontalFlip",
                "NvsAnimatedSticker.getHorizontalFlip",
                "NvsAnimatedSticker.setZValue",
                "NvsAnimatedSticker.setVolumeGain",
                "NvsAnimatedSticker.applyAnimatedStickerPeriodAnimation",
                "NvsAnimatedSticker.setAnimatedStickerAnimationPeriod",
                "NvsAnimatedSticker.applyAnimatedStickerInAnimation",
                "NvsAnimatedSticker.setAnimatedStickerInAnimationDuration",
                "NvsAnimatedSticker.applyAnimatedStickerOutAnimation",
                "NvsAnimatedSticker.setAnimatedStickerOutAnimationDuration",
            ],
            ["NvsAnimatedSticker", "transform values", "installed animation package ids"],
            ["configured animated sticker"],
        ),
        (
            "java.clip.add-caption",
            "Add a caption in clip-local time",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "addClipCaption",
            ["NvsVideoClip.addCaption"],
            ["NvsVideoClip", "text", "clip-local range", "optional style package"],
            ["NvsClipCaption"],
        ),
        (
            "java.clip.add-modular-caption",
            "Add a modular caption in clip-local time",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "addClipModularCaption",
            ["NvsVideoClip.addModularCaption"],
            ["NvsVideoClip", "text", "clip-local range"],
            ["NvsClipCaption"],
        ),
        (
            "java.clip.add-animated-sticker",
            "Add a packaged or custom animated sticker in clip-local time",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "addClipAnimatedSticker",
            ["NvsVideoClip.addAnimatedSticker", "NvsVideoClip.addCustomAnimatedSticker"],
            ["NvsVideoClip", "clip-local range", "sticker package", "optional custom image"],
            ["NvsClipAnimatedSticker"],
        ),
        (
            "java.clip.list-animated-stickers",
            "Traverse clip-local animated stickers",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "listClipAnimatedStickers",
            ["NvsVideoClip.getFirstAnimatedSticker", "NvsVideoClip.getNextAnimatedSticker"],
            ["NvsVideoClip"],
            ["ordered clip-local sticker list"],
        ),
        (
            "java.clip.remove-caption",
            "Remove a clip-local caption",
            "caption-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "removeClipCaption",
            ["NvsVideoClip.removeCaption"],
            ["NvsVideoClip", "NvsClipCaption"],
            ["removed clip caption result"],
        ),
        (
            "java.clip.remove-animated-sticker",
            "Remove a clip-local animated sticker",
            "sticker-editor",
            "assets/android-feature-templates/captions-stickers/app/src/main/java/{{PACKAGE_PATH}}/MeisheCaptionStickerController.java",
            "removeClipAnimatedSticker",
            ["NvsVideoClip.removeAnimatedSticker"],
            ["NvsVideoClip", "NvsClipAnimatedSticker"],
            ["removed clip sticker result"],
        ),
        (
            "java.clip.configure-advanced-playback",
            "Configure variable speed, rotation, reverse, decode, crop, wrap, and background",
            "clip-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "configureAdvancedClipPlayback",
            [
                "NvsVideoClip.changeVariableSpeed",
                "NvsVideoClip.setExtraVideoRotation",
                "NvsVideoClip.getExtraVideoRotation",
                "NvsVideoClip.setPlayInReverse",
                "NvsVideoClip.getPlayInReverse",
                "NvsVideoClip.setSoftWareDecoding",
                "NvsVideoClip.disableAmbiguousCrop",
                "NvsVideoClip.isAmbiguousCropDisabled",
                "NvsVideoClip.enableRawSourceMode",
                "NvsVideoClip.setClipWrapMode",
                "NvsVideoClip.getClipWrapMode",
                "NvsVideoClip.setSourceBackgroundMode",
                "NvsVideoClip.getSourceBackgroundMode",
            ],
            ["NvsVideoClip", "speed and decode configuration"],
            ["configured clip playback state"],
        ),
        (
            "java.clip.configure-image-regions",
            "Configure image motion and mask regions",
            "animation-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "configureClipImageRegions",
            [
                "NvsVideoClip.setImageMotionROI",
                "NvsVideoClip.getStartROI",
                "NvsVideoClip.getEndROI",
                "NvsVideoClip.setImageMaskROI",
                "NvsVideoClip.getImageMaskROI",
            ],
            ["NvsVideoClip", "start/end motion ROI", "mask ROI"],
            ["configured image regions"],
        ),
        (
            "java.effect.set-float-keyframe",
            "Set and validate a numeric FX keyframe",
            "animation-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "setFloatKeyframe",
            ["NvsFx.setFloatValAtTime", "NvsFx.hasKeyframeList", "NvsFx.getFloatValAtTime"],
            ["NvsFx", "parameter key", "value", "keyframe time"],
            ["validated numeric FX keyframe"],
        ),
        (
            "java.effect.remove-nearest-keyframe",
            "Find and remove the nearest FX keyframe",
            "animation-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "removeNearestKeyframe",
            ["NvsFx.findKeyframeTime", "NvsFx.removeKeyframeAtTime"],
            ["NvsFx", "parameter key", "input time", "find mode"],
            ["keyframe removal result"],
        ),
        (
            "java.effect.set-position-parameters",
            "Set and read two-dimensional and three-dimensional FX positions",
            "filter-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "setPositionParameters",
            [
                "NvsFx.setPosition2DVal",
                "NvsFx.getPosition2DVal",
                "NvsFx.setPosition3DVal",
                "NvsFx.getPosition3DVal",
            ],
            ["NvsFx", "position keys", "NvsPosition2D", "NvsPosition3D"],
            ["configured FX positions"],
        ),
        (
            "java.transition.configure-timing",
            "Configure transition enablement, duration, match mode, and scale",
            "transition-editor",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "configureTransitionTiming",
            [
                "NvsVideoTransition.enableTimelineTransition",
                "NvsVideoTransition.setVideoTransitionDuration",
                "NvsVideoTransition.setVideoTransitionDurationScaleFactor",
                "NvsVideoTransition.getVideoTransitionDuration",
                "NvsVideoTransition.getVideoTransitionDurationMatchMode",
            ],
            ["NvsVideoTransition", "duration and match configuration"],
            ["configured transition timing"],
        ),
        (
            "java.particle.configure-emitter",
            "Configure particle emitter rate, size, and position curve",
            "particle-effects",
            "assets/android-feature-templates/effects/app/src/main/java/{{PACKAGE_PATH}}/MeisheEffectController.java",
            "configureParticleEmitter",
            [
                "NvsParticleSystemContext.setEmitterRateGain",
                "NvsParticleSystemContext.setEmitterParticleSizeGain",
                "NvsParticleSystemContext.appendPositionToEmitterPositionCurve",
            ],
            ["NvsParticleSystemContext", "emitter name", "rate/size/position values"],
            ["configured particle emitter"],
        ),
        (
            "java.preview.grab-image-async",
            "Register the image callback and request an asynchronous timeline frame",
            "still-image-export",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "grabImageAsynchronously",
            ["NvsStreamingContext.setImageGrabberCallback", "NvsStreamingContext.grabImageFromTimelineAsync"],
            ["NvsTimeline", "timestamp", "aspect ratio", "image callback"],
            ["asynchronous image request result"],
        ),
        (
            "java.preview.map-live-window-point",
            "Map points between LiveWindow view, canonical, and normalized coordinates",
            "timeline-preview",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "mapLiveWindowPoint",
            [
                "NvsLiveWindow.mapViewToCanonical",
                "NvsLiveWindow.mapCanonicalToView",
                "NvsLiveWindow.mapViewToNormalized",
                "NvsLiveWindow.mapNormalizedToView",
            ],
            ["NvsLiveWindow", "PointF", "mapping mode"],
            ["mapped LiveWindow point"],
        ),
        (
            "java.preview.configure-thumbnail-sequence",
            "Configure thumbnail descriptions, scale, padding, and scrolling",
            "timeline-ui",
            "assets/android-feature-templates/preview-playback/app/src/main/java/{{PACKAGE_PATH}}/MeishePlaybackController.java",
            "configureThumbnailSequence",
            [
                "NvsMultiThumbnailSequenceView.setStartPadding",
                "NvsMultiThumbnailSequenceView.setEndPadding",
                "NvsMultiThumbnailSequenceView.setPixelPerMicrosecond",
                "NvsMultiThumbnailSequenceView.getPixelPerMicrosecond",
                "NvsMultiThumbnailSequenceView.setThumbnailSequenceDescArray",
                "NvsMultiThumbnailSequenceView.setOnScrollChangeListenser",
                "NvsMultiThumbnailSequenceView.scaleWithAnchor",
            ],
            ["NvsMultiThumbnailSequenceView", "thumbnail descriptors", "scale and padding"],
            ["configured thumbnail sequence"],
        ),
        (
            "java.timeline.add-clip-at-position",
            "Add a trimmed clip at an explicit timeline position",
            "clip-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "addClipAtTimelinePosition",
            ["NvsVideoTrack.addClip", "NvsVideoTrack.getClipByTimelinePosition"],
            ["NvsVideoTrack", "media path", "timeline and trim range"],
            ["NvsVideoClip at the requested timeline position"],
        ),
        (
            "java.timeline.insert-clip-at-index",
            "Insert a trimmed clip at a track index",
            "clip-editor",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "insertClipAtIndex",
            ["NvsVideoTrack.insertClip"],
            ["NvsVideoTrack", "media path", "trim range", "clip index"],
            ["inserted NvsVideoClip"],
        ),
        (
            "java.timeline.configure-structure",
            "Change timeline size and audio fade, then optionally remove extra tracks",
            "timeline-state-store",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheTimelineController.java",
            "configureTimelineStructure",
            [
                "NvsStreamingContext.stop",
                "NvsTimeline.changeVideoSize",
                "NvsTimeline.setAudioFadeOutDuration",
                "NvsTimeline.getAudioFadeOutDuration",
                "NvsTimeline.videoTrackCount",
                "NvsTimeline.removeVideoTrack",
                "NvsTimeline.audioTrackCount",
                "NvsTimeline.removeAudioTrack",
            ],
            ["NvsTimeline", "video size", "audio fade", "track removal choices"],
            ["reconfigured timeline structure"],
        ),
        (
            "java.asset.inspect-package",
            "Inspect installed package status, aspect support, and AR/video metadata",
            "asset-package-service",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheAssetInstaller.java",
            "inspectInstalledPackage",
            [
                "NvsAssetPackageManager.getAssetPackageStatus",
                "NvsAssetPackageManager.getAssetPackageSupportedAspectRatio",
                "NvsAssetPackageManager.getVideoFxAssetPackageDescription",
                "NvsAssetPackageManager.getARSceneAssetPackagePrompt",
                "NvsAssetPackageManager.getARSceneAssetPackageCameraPreset",
                "NvsAssetPackageManager.isARSceneAssetPackageContainFaceMesh",
                "NvsAssetPackageManager.isARSceneAssetPackageContainWarp",
                "NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE",
            ],
            ["installed package id", "package type"],
            ["typed package metadata map"],
        ),
        (
            "java.media.create-frame-retriever",
            "Create a video frame retriever for an app-owned media path",
            "media-import",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaProbeController.java",
            "createFrameRetriever",
            ["NvsStreamingContext.createVideoFrameRetriever"],
            ["NvsStreamingContext", "readable media path"],
            ["NvsVideoFrameRetriever"],
        ),
        (
            "java.media.retrieve-frame",
            "Retrieve a frame at time with default or custom output height",
            "media-import",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaProbeController.java",
            "retrieveFrame",
            [
                "NvsVideoFrameRetriever.getFrameAtTime",
                "NvsVideoFrameRetriever.getFrameAtTimeWithCustomVideoFrameHeight",
            ],
            ["NvsVideoFrameRetriever", "timestamp", "flags", "optional output height"],
            ["Bitmap frame"],
        ),
        (
            "java.media.release-frame-retriever",
            "Release a caller-owned video frame retriever",
            "media-import",
            "assets/android-template/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaProbeController.java",
            "releaseFrameRetriever",
            ["NvsVideoFrameRetriever.release"],
            ["caller-owned NvsVideoFrameRetriever"],
            ["released frame retriever"],
        ),
        (
            "java.beauty.append-capture-fx",
            "Append the built-in beauty capture effect",
            "beauty-camera",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "appendBeautyCaptureFx",
            ["NvsStreamingContext.appendBeautyCaptureVideoFx"],
            ["active capture preview"],
            ["NvsCaptureVideoFx beauty effect"],
        ),
        (
            "java.beauty.effect-sdk-init-activity-flags",
            "Initialize Effect SDK for an Activity with explicit feature flags",
            "beauty-camera",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "initializeEffectSdkForActivity",
            ["NvsEffectSdkContext.getInstance", "NvsEffectSdkContext.init"],
            ["Activity", "assets:/meishesdk.lic", "Effect SDK feature flags"],
            ["NvsEffectSdkContext initialization result"],
        ),
        (
            "java.beauty.configure-ar-manipulation",
            "Configure AR scene detection mode, probing, callback, and capability gate",
            "ar-scene",
            "assets/android-feature-templates/beauty-ar/app/src/main/java/{{PACKAGE_PATH}}/MeisheBeautyArController.java",
            "configureArSceneManipulation",
            [
                "NvsFx.getARSceneManipulate",
                "NvsARSceneManipulate.setARSceneCallback",
                "NvsARSceneManipulate.setDetectionMode",
                "NvsARSceneManipulate.setDetectionAutoProbe",
                "NvsARSceneManipulate.isFunctionAvailable",
                "NvsARSceneManipulate.CheckedFunctionType_Matte",
            ],
            ["AR Scene NvsFx", "detection configuration", "owned callback"],
            ["AR scene manipulation availability"],
        ),
        (
            "java.media.convert-passthrough",
            "Convert compatible media without re-encoding and register its callback",
            "quick-splicing",
            "assets/android-feature-templates/media-workflows/app/src/main/java/{{PACKAGE_PATH}}/MeisheMediaWorkflowController.java",
            "convertMediaFilesWithoutReencoding",
            [
                "NvsPassthroughConvertor.setPassthroughConvertorCallback",
                "NvsPassthroughConvertor.convertMediaFile",
            ],
            ["NvsPassthroughConvertor", "NvsPassthroughConvertor.NvsPassthroughFileInfo list", "output path", "callback owner"],
            ["passthrough conversion task id"],
        ),
        (
            "java.audio.append-clip-fx",
            "Append and validate an audio clip effect",
            "audio-equalizer",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "appendAudioClipFx",
            ["NvsAudioClip.appendFx", "NvsAudioFx.getBuiltinAudioFxName"],
            ["NvsAudioClip", "built-in audio FX name"],
            ["NvsAudioFx"],
        ),
        (
            "java.audio.replace-clip-fx",
            "Replace an indexed audio clip effect",
            "audio-equalizer",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "replaceAudioClipFx",
            [
                "NvsAudioClip.getFxByIndex",
                "NvsAudioClip.removeFx",
                "NvsAudioClip.insertFx",
            ],
            ["NvsAudioClip", "FX index", "built-in audio FX name"],
            ["replacement NvsAudioFx"],
        ),
        (
            "java.audio.configure-transition",
            "Set and query a built-in audio transition",
            "music-editor",
            "assets/android-feature-templates/audio/app/src/main/java/{{PACKAGE_PATH}}/MeisheAudioController.java",
            "configureAudioTransition",
            ["NvsAudioTrack.setBuiltinTransition", "NvsAudioTrack.getTransitionWithSourceClipIndex"],
            ["NvsAudioTrack", "source clip index", "built-in transition name"],
            ["NvsAudioTransition"],
        ),
    ]
)

UNIT_COMPOSE_AFTER.update(
    {
        "java.capture.configure-device-controls": ["java.capture.start-preview"],
        "java.caption.configure-typography": ["java.caption.add"],
        "java.caption.configure-transform": ["java.caption.add"],
        "java.caption.apply-modular-assets": [
            "java.caption.add",
            "java.asset.install-or-upgrade",
        ],
        "java.sticker.configure-animation-transform": ["java.sticker.add"],
        "java.clip.add-caption": ["java.timeline.append-clip", "java.engine.stop"],
        "java.clip.add-modular-caption": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.clip.add-animated-sticker": [
            "java.timeline.append-clip",
            "java.asset.install-or-upgrade",
            "java.engine.stop",
        ],
        "java.clip.list-animated-stickers": ["java.timeline.append-clip"],
        "java.clip.remove-caption": ["java.clip.add-caption", "java.engine.stop"],
        "java.clip.remove-animated-sticker": [
            "java.clip.add-animated-sticker",
            "java.engine.stop",
        ],
        "java.clip.configure-advanced-playback": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.clip.configure-image-regions": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.effect.set-float-keyframe": ["java.effect.append-builtin"],
        "java.effect.remove-nearest-keyframe": ["java.effect.set-float-keyframe"],
        "java.effect.set-position-parameters": ["java.effect.append-builtin"],
        "java.transition.configure-timing": ["java.transition.set-builtin"],
        "java.particle.configure-emitter": ["java.effect.add-particle"],
        "java.preview.grab-image-async": ["java.preview.connect"],
        "java.preview.map-live-window-point": ["java.preview.connect"],
        "java.preview.configure-thumbnail-sequence": ["java.timeline.create"],
        "java.timeline.add-clip-at-position": ["java.timeline.create", "java.engine.stop"],
        "java.timeline.insert-clip-at-index": ["java.timeline.create", "java.engine.stop"],
        "java.timeline.configure-structure": ["java.timeline.create", "java.engine.stop"],
        "java.asset.inspect-package": ["java.asset.install-or-upgrade"],
        "java.media.create-frame-retriever": ["java.sdk.initialize"],
        "java.media.retrieve-frame": ["java.media.create-frame-retriever"],
        "java.media.release-frame-retriever": ["java.media.create-frame-retriever"],
        "java.beauty.append-capture-fx": ["java.capture.start-preview"],
        "java.beauty.effect-sdk-init-activity-flags": ["java.sdk.initialize"],
        "java.beauty.configure-ar-manipulation": ["java.beauty.append-ar-scene"],
        "java.media.convert-passthrough": ["java.sdk.initialize", "java.media.probe"],
        "java.audio.append-clip-fx": ["java.audio.add-clip", "java.engine.stop"],
        "java.audio.replace-clip-fx": ["java.audio.append-clip-fx", "java.engine.stop"],
        "java.audio.configure-transition": ["java.audio.ensure-track", "java.engine.stop"],
    }
)

UNIT_COMPOSE_AFTER.update(
    {
        "java.app.request-permissions": [],
        "java.app.route-feature": ["java.app.request-permissions"],
        "java.app.show-editor-message": [],
        "java.app.save-project-state": [],
        "java.app.save-timeline-structure": ["java.timeline.create"],
        "java.app.extract-editor-state": ["java.app.load-project-state"],
        "java.app.save-editor-state": ["java.app.save-timeline-structure"],
        "java.app.load-project-state": [],
        "java.app.latest-project-id": [],
        "java.app.read-project-dimension": [],
        "java.app.restore-timeline-structure": ["java.timeline.create", "java.engine.stop"],
        "java.editor.clear-supported-features": [
            "java.app.restore-timeline-structure",
            "java.engine.stop",
        ],
        "java.editor.restore-supported-features": [
            "java.app.extract-editor-state",
            "java.app.restore-timeline-structure",
            "java.editor.clear-supported-features",
            "java.engine.stop",
        ],
        "java.effect.build-parameter": [],
        "java.app.create-feedback": [],
        "java.thread.require-main": [],
        "java.sdk.configure-runtime": ["java.sdk.initialize"],
        "java.engine.stop": ["java.sdk.initialize"],
        "java.timeline.get-video-clip": ["java.timeline.create"],
        "java.timeline.get-video-resolution": ["java.timeline.create"],
        "java.timeline.set-theme-music-volume": ["java.timeline.create"],
        "java.timeline.remove": ["java.timeline.create", "java.engine.stop"],
        "java.preview.configure-live-window": ["java.preview.connect"],
        "java.preview.register-callbacks": ["java.sdk.initialize"],
        "java.preview.build-seek-flags": [],
        "java.preview.set-seek-scale": ["java.preview.connect"],
        "java.preview.map-thumbnail-position": ["java.timeline.create"],
        "java.preview.read-engine-state": ["java.sdk.initialize"],
        "java.effect.append-raw-builtin": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.effect.list-clip-fx": ["java.timeline.append-clip"],
        "java.effect.get-first-timeline-fx": ["java.timeline.create"],
        "java.effect.remove-timeline-fx": [
            "java.timeline.create",
            "java.engine.stop",
        ],
        "java.transition.set-builtin": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.transition.set-packaged": [
            "java.asset.install-or-upgrade",
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.transition.get": ["java.timeline.append-clip"],
        "java.clip.configure-image-motion": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.clip.is-audio-video": ["java.timeline.append-clip"],
        "java.caption.list-timeline": ["java.timeline.create"],
        "java.caption.list-compound": ["java.timeline.create"],
        "java.sticker.list-timeline": ["java.timeline.create"],
        "java.sticker.list-at-position": ["java.timeline.create"],
        "java.sticker.add-custom": [
            "java.asset.install-or-upgrade",
            "java.timeline.create",
            "java.engine.stop",
        ],
        "java.caption.timeline-range": ["java.caption.list-timeline"],
        "java.caption.compound-range": ["java.caption.list-compound"],
        "java.sticker.timeline-range": ["java.sticker.list-timeline"],
        "java.caption.clip-range": ["java.caption.list-clip"],
        "java.sticker.clip-range": ["java.timeline.append-clip"],
        "java.caption.list-clip": ["java.timeline.append-clip"],
        "java.caption.list-clip-compound": ["java.timeline.append-clip"],
        "java.caption.register-font": ["java.sdk.initialize"],
        "java.caption.apply-readable-style": ["java.caption.add"],
        "java.caption.set-letter-spacing": ["java.caption.add"],
        "java.caption.remove-compound": [
            "java.caption.add-compound",
            "java.engine.stop",
        ],
        "java.audio.get-clip": ["java.audio.add-clip"],
        "java.audio.set-fades": ["java.audio.add-clip"],
        "java.capture.build-preview-flags": [],
        "java.capture.start-recording-with-flags": ["java.capture.start-preview"],
        "java.capture.get-device-capability": ["java.sdk.initialize"],
        "java.capture.register-callbacks": ["java.sdk.initialize"],
        "java.capture.list-effects": ["java.capture.start-preview"],
        "java.capture.remove-effect": ["java.capture.start-preview"],
        "java.capture.clear-effects": ["java.capture.start-preview"],
        "java.beauty.initialize-human-detection": ["java.sdk.initialize"],
        "java.beauty.release-human-detection": [
            "java.beauty.initialize-human-detection",
        ],
        "java.beauty.configure-ar-scene": ["java.beauty.append-ar-scene"],
        "java.beauty.enable-ai-face-occlusion": ["java.beauty.append-ar-scene"],
        "java.segmentation.append-background-capture": [
            "java.beauty.initialize-human-detection",
            "java.capture.start-preview",
        ],
        "java.capture.append-packaged-fx": [
            "java.asset.install-or-upgrade",
            "java.capture.start-preview",
        ],
        "java.export.configure": ["java.timeline.create", "java.engine.stop"],
        "java.export.resolution-grade": [],
        "java.export.bitrate-grade": [],
        "java.asset.package-type": [],
        "java.sdk.initialize-activity": [],
        "java.sdk.get-asset-package-manager": ["java.sdk.initialize"],
        "java.engine.stop-with-flags": ["java.sdk.initialize"],
        "java.media.probe-with-flags": ["java.sdk.initialize"],
        "java.timeline.create-template": [
            "java.sdk.initialize",
            "java.asset.install-or-upgrade",
        ],
        "java.timeline.create-template-with-flags": [
            "java.sdk.initialize",
            "java.asset.install-or-upgrade",
        ],
        "java.timeline.append-trimmed-clip": [
            "java.timeline.create",
            "java.engine.stop",
        ],
        "java.preview.current-position": ["java.preview.connect"],
        "java.preview.play-with-fps": ["java.preview.connect"],
        "java.preview.seek-with-fps": ["java.preview.connect"],
        "java.effect.add-packaged-timeline": [
            "java.asset.install-or-upgrade",
            "java.timeline.create",
            "java.engine.stop",
        ],
        "java.caption.remove": ["java.caption.add", "java.engine.stop"],
        "java.capture.start-recording-configured": ["java.capture.start-preview"],
        "java.export.register-callbacks": ["java.sdk.initialize"],
        "java.audio.add-clip-at": ["java.audio.ensure-track"],
        "java.app.copy-content-uri-to-cache": [],
        "java.app.copy-bundled-media-to-project": [],
        "java.app.copy-content-uri-to-project": [],
        "java.timeline.build-picture-in-picture": ["java.timeline.create"],
        "java.timeline.build-quick-splice": ["java.timeline.create"],
        "java.timeline.append-media-list": ["java.timeline.create", "java.engine.stop"],
        "java.clip.trim-out-at-playhead": ["java.timeline.append-media-list", "java.engine.stop"],
        "java.clip.remove-at": ["java.timeline.append-media-list", "java.engine.stop"],
        "java.clip.move": ["java.timeline.append-media-list", "java.engine.stop"],
        "java.clip.split-at-playhead": ["java.timeline.append-media-list", "java.engine.stop"],
        "java.sdk.initialize-activity-default": [],
        "java.timeline.create-with-flags": [
            "java.sdk.initialize",
            "java.media.probe",
        ],
        "java.timeline.create-template-configured": [
            "java.sdk.initialize",
            "java.asset.install-or-upgrade",
        ],
        "java.export.compile-configured": [
            "java.timeline.create",
            "java.engine.stop",
            "java.export.configure",
        ],
        "java.beauty.initialize-human-detection-configured": [
            "java.sdk.initialize",
        ],
        "java.beauty.initialize-human-detection-ext-configured": [
            "java.sdk.initialize",
        ],
        "java.capture.stop-recording-synchronous": [
            "java.capture.start-recording",
        ],
        "java.effect.append-builtin-range": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.effect.append-raw-builtin-range": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.audio.append-clip-default": [
            "java.audio.ensure-track",
            "java.engine.stop",
        ],
        "java.clip.change-speed": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.clip.change-trim-in": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.caption.set-compound-text": ["java.caption.add-compound"],
        "java.beauty.effect-sdk-init-activity-default": ["java.sdk.initialize"],
        "java.beauty.effect-human-detection-ext-configured": [
            "java.beauty.effect-sdk-init",
        ],
        "java.export.register-callback3": ["java.sdk.initialize"],
        "java.clip.move-to-timeline-position": [
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
        "java.audio.set-track-stereo-volume": ["java.audio.ensure-track"],
        "java.effect.append-packaged-range": [
            "java.asset.install-or-upgrade",
            "java.timeline.append-clip",
            "java.engine.stop",
        ],
    }
)
UNIT_COMPOSE_AFTER["java.timeline.append-clip"] = [
    "java.timeline.create",
    "java.engine.stop",
]
UNIT_COMPOSE_AFTER["java.export.compile"] = [
    "java.timeline.create",
    "java.engine.stop",
    "java.export.configure",
]

UNIT_LIFECYCLE_HOOKS.update(
    {
        "java.capture.configure-device-controls": "activity_create",
        "java.caption.configure-typography": "after_mutation_refresh",
        "java.caption.configure-transform": "after_mutation_refresh",
        "java.caption.apply-modular-assets": "asset_installed",
        "java.sticker.configure-animation-transform": "after_mutation_refresh",
        "java.clip.add-caption": "before_structural_mutation",
        "java.clip.add-modular-caption": "before_structural_mutation",
        "java.clip.add-animated-sticker": "before_structural_mutation",
        "java.clip.list-animated-stickers": "timeline_created",
        "java.clip.remove-caption": "before_structural_mutation",
        "java.clip.remove-animated-sticker": "before_structural_mutation",
        "java.clip.configure-advanced-playback": "before_structural_mutation",
        "java.clip.configure-image-regions": "before_structural_mutation",
        "java.effect.set-float-keyframe": "after_mutation_refresh",
        "java.effect.remove-nearest-keyframe": "after_mutation_refresh",
        "java.effect.set-position-parameters": "after_mutation_refresh",
        "java.transition.configure-timing": "after_mutation_refresh",
        "java.particle.configure-emitter": "after_mutation_refresh",
        "java.preview.grab-image-async": "live_window_bound",
        "java.preview.map-live-window-point": "live_window_bound",
        "java.preview.configure-thumbnail-sequence": "live_window_bound",
        "java.timeline.add-clip-at-position": "before_structural_mutation",
        "java.timeline.insert-clip-at-index": "before_structural_mutation",
        "java.timeline.configure-structure": "before_structural_mutation",
        "java.asset.inspect-package": "asset_installed",
        "java.media.create-frame-retriever": "activity_create",
        "java.media.retrieve-frame": "activity_create",
        "java.media.release-frame-retriever": "destroy",
        "java.beauty.append-capture-fx": "activity_create",
        "java.beauty.effect-sdk-init-activity-flags": "sdk_init",
        "java.beauty.configure-ar-manipulation": "activity_create",
        "java.media.convert-passthrough": "activity_create",
        "java.audio.append-clip-fx": "before_structural_mutation",
        "java.audio.replace-clip-fx": "before_structural_mutation",
        "java.audio.configure-transition": "before_structural_mutation",
    }
)

STRUCTURAL_MUTATION_UNIT_IDS.update(
    {
        "java.clip.add-caption",
        "java.clip.add-modular-caption",
        "java.clip.add-animated-sticker",
        "java.clip.remove-caption",
        "java.clip.remove-animated-sticker",
        "java.clip.configure-advanced-playback",
        "java.clip.configure-image-regions",
        "java.timeline.add-clip-at-position",
        "java.timeline.insert-clip-at-index",
        "java.timeline.configure-structure",
        "java.audio.append-clip-fx",
        "java.audio.replace-clip-fx",
        "java.audio.configure-transition",
    }
)

UNIT_LIFECYCLE_HOOKS.update(
    {
        "java.app.request-permissions": "activity_create",
        "java.app.route-feature": "activity_create",
        "java.app.show-editor-message": "activity_create",
        "java.app.save-project-state": "destroy",
        "java.app.save-timeline-structure": "after_mutation_refresh",
        "java.app.extract-editor-state": "activity_create",
        "java.app.save-editor-state": "after_mutation_refresh",
        "java.app.load-project-state": "activity_create",
        "java.app.latest-project-id": "activity_create",
        "java.app.read-project-dimension": "activity_create",
        "java.app.restore-timeline-structure": "before_structural_mutation",
        "java.editor.clear-supported-features": "before_structural_mutation",
        "java.editor.restore-supported-features": "after_mutation_refresh",
        "java.effect.build-parameter": "activity_create",
        "java.app.create-feedback": "activity_create",
        "java.thread.require-main": "activity_create",
        "java.sdk.configure-runtime": "sdk_init",
        "java.engine.stop": "before_structural_mutation",
        "java.timeline.get-video-clip": "timeline_created",
        "java.timeline.get-video-resolution": "timeline_created",
        "java.timeline.set-theme-music-volume": "after_mutation_refresh",
        "java.timeline.remove": "destroy",
        "java.preview.configure-live-window": "live_window_bound",
        "java.preview.register-callbacks": "activity_create",
        "java.preview.build-seek-flags": "activity_create",
        "java.preview.set-seek-scale": "live_window_bound",
        "java.preview.map-thumbnail-position": "live_window_bound",
        "java.preview.read-engine-state": "activity_create",
        "java.effect.append-raw-builtin": "before_structural_mutation",
        "java.effect.list-clip-fx": "after_mutation_refresh",
        "java.effect.get-first-timeline-fx": "timeline_created",
        "java.effect.remove-timeline-fx": "before_structural_mutation",
        "java.transition.set-builtin": "before_structural_mutation",
        "java.transition.set-packaged": "asset_installed",
        "java.transition.get": "after_mutation_refresh",
        "java.clip.configure-image-motion": "before_structural_mutation",
        "java.clip.is-audio-video": "timeline_created",
        "java.caption.list-timeline": "timeline_created",
        "java.caption.list-compound": "timeline_created",
        "java.sticker.list-timeline": "timeline_created",
        "java.sticker.list-at-position": "live_window_bound",
        "java.sticker.add-custom": "asset_installed",
        "java.caption.timeline-range": "after_mutation_refresh",
        "java.caption.compound-range": "after_mutation_refresh",
        "java.sticker.timeline-range": "after_mutation_refresh",
        "java.caption.clip-range": "after_mutation_refresh",
        "java.sticker.clip-range": "after_mutation_refresh",
        "java.caption.list-clip": "timeline_created",
        "java.caption.list-clip-compound": "timeline_created",
        "java.caption.register-font": "asset_installed",
        "java.caption.apply-readable-style": "after_mutation_refresh",
        "java.caption.set-letter-spacing": "after_mutation_refresh",
        "java.caption.remove-compound": "before_structural_mutation",
        "java.audio.get-clip": "timeline_created",
        "java.audio.set-fades": "after_mutation_refresh",
        "java.capture.build-preview-flags": "activity_create",
        "java.capture.start-recording-with-flags": "activity_create",
        "java.capture.get-device-capability": "activity_create",
        "java.capture.register-callbacks": "activity_create",
        "java.capture.list-effects": "activity_create",
        "java.capture.remove-effect": "activity_create",
        "java.capture.clear-effects": "destroy",
        "java.beauty.initialize-human-detection": "sdk_init",
        "java.beauty.release-human-detection": "destroy",
        "java.beauty.configure-ar-scene": "activity_create",
        "java.segmentation.append-background-capture": "activity_create",
        "java.capture.append-packaged-fx": "asset_installed",
        "java.export.configure": "before_structural_mutation",
        "java.export.resolution-grade": "activity_create",
        "java.export.bitrate-grade": "activity_create",
        "java.asset.package-type": "activity_create",
        "java.sdk.initialize-activity": "sdk_init",
        "java.sdk.get-asset-package-manager": "sdk_init",
        "java.engine.stop-with-flags": "before_structural_mutation",
        "java.media.probe-with-flags": "activity_create",
        "java.timeline.create-template": "asset_installed",
        "java.timeline.create-template-with-flags": "asset_installed",
        "java.timeline.append-trimmed-clip": "before_structural_mutation",
        "java.preview.current-position": "live_window_bound",
        "java.preview.play-with-fps": "live_window_bound",
        "java.preview.seek-with-fps": "live_window_bound",
        "java.effect.add-packaged-timeline": "asset_installed",
        "java.caption.remove": "before_structural_mutation",
        "java.capture.start-recording-configured": "activity_create",
        "java.export.register-callbacks": "activity_create",
        "java.audio.add-clip-at": "before_structural_mutation",
        "java.app.copy-content-uri-to-cache": "activity_create",
        "java.app.copy-bundled-media-to-project": "activity_create",
        "java.app.copy-content-uri-to-project": "activity_create",
        "java.timeline.build-picture-in-picture": "before_structural_mutation",
        "java.timeline.build-quick-splice": "before_structural_mutation",
        "java.timeline.append-media-list": "before_structural_mutation",
        "java.clip.trim-out-at-playhead": "before_structural_mutation",
        "java.clip.remove-at": "before_structural_mutation",
        "java.clip.move": "before_structural_mutation",
        "java.clip.split-at-playhead": "before_structural_mutation",
        "java.sdk.initialize-activity-default": "sdk_init",
        "java.timeline.create-with-flags": "timeline_created",
        "java.timeline.create-template-configured": "asset_installed",
        "java.export.compile-configured": "before_structural_mutation",
        "java.beauty.initialize-human-detection-configured": "sdk_init",
        "java.beauty.initialize-human-detection-ext-configured": "sdk_init",
        "java.capture.stop-recording-synchronous": "destroy",
        "java.effect.append-builtin-range": "before_structural_mutation",
        "java.effect.append-raw-builtin-range": "before_structural_mutation",
        "java.audio.append-clip-default": "before_structural_mutation",
        "java.clip.change-speed": "before_structural_mutation",
        "java.clip.change-trim-in": "before_structural_mutation",
        "java.caption.set-compound-text": "after_mutation_refresh",
        "java.beauty.effect-sdk-init-activity-default": "sdk_init",
        "java.beauty.effect-human-detection-ext-configured": "sdk_init",
        "java.export.register-callback3": "activity_create",
        "java.clip.move-to-timeline-position": "before_structural_mutation",
        "java.audio.set-track-stereo-volume": "after_mutation_refresh",
        "java.effect.append-packaged-range": "asset_installed",
    }
)

RECIPE_LIFECYCLE_HOOKS = {
    "sdk-init": "sdk_init",
    "effect-sdk-init": "sdk_init",
    "media-probe-and-ratio": "activity_create",
    "timeline-build": "timeline_created",
    "connect-livewindow": "live_window_bound",
    "apply-refresh-editor-child": "after_mutation_refresh",
    "editor-session-orchestration": "activity_create",
    "editor-project-v3-ownership": "activity_create",
    "install-asset-package": "asset_installed",
    "bundled-material-install": "asset_installed",
    "caption-sticker-edit": "before_structural_mutation",
    "filter-effect-edit": "before_structural_mutation",
    "audio-edit": "before_structural_mutation",
    "capture-preview-record": "activity_create",
    "compile-export": "before_structural_mutation",
    "template-replace-export": "asset_installed",
    "template-prepare-footage": "asset_installed",
    "cutsame-replace-export": "asset_installed",
    "mimo-replace-export": "asset_installed",
}

TEMPLATE_PREPARE_STEP_UNITS = [
    "java.asset.install-async",
    "java.template.query-footages",
    "java.template.query-captions",
    "java.template.query-compound-captions",
    "java.template.list-replaceable-footage",
    "java.template.list-reverse-footage",
    "java.template.reverse-register-callback",
    "java.template.reverse-generate",
    "java.template.validate-footage",
    "java.template.build-footage",
]

TEMPLATE_FINALIZE_STEP_UNITS = [
    "java.template.replace-captions",
    "java.template.replace-compound-captions",
    "java.template.reconnect-preview",
    "java.template.current-position",
    "java.template.play",
    "java.template.register-compile-callbacks",
    "java.template.export",
    "java.template.reverse-cancel",
    "java.template.reverse-release",
]

RECIPE_STEP_UNITS = {
    "sdk-init": [
        "java.thread.require-main",
        "java.sdk.initialize",
        "java.sdk.initialize-activity",
        "java.sdk.initialize-activity-default",
        "java.sdk.configure-runtime",
        "java.sdk.get-asset-package-manager",
    ],
    "effect-sdk-init": [
        "java.beauty.effect-sdk-init",
        "java.beauty.effect-sdk-init-activity-default",
        "java.beauty.initialize-human-detection",
        "java.beauty.initialize-human-detection-configured",
        "java.beauty.initialize-human-detection-ext-configured",
        "java.beauty.effect-human-detection-ext-configured",
        "java.beauty.release-human-detection",
    ],
    "media-probe-and-ratio": [
        "java.app.copy-bundled-media-to-project",
        "java.app.copy-content-uri-to-project",
        "java.media.probe",
        "java.media.probe-with-flags",
    ],
    "timeline-build": [
        "java.app.latest-project-id",
        "java.app.load-project-state",
        "java.app.read-project-dimension",
        "java.app.extract-editor-state",
        "java.timeline.create",
        "java.timeline.create-with-flags",
        "java.timeline.create-template-configured",
        "java.app.restore-timeline-structure",
        "java.editor.clear-supported-features",
        "java.editor.restore-supported-features",
        "java.timeline.append-media-list",
        "java.timeline.append-clip",
        "java.timeline.append-trimmed-clip",
        "java.clip.change-speed",
        "java.clip.change-trim-in",
        "java.clip.move-to-timeline-position",
        "java.timeline.get-video-clip",
        "java.timeline.get-video-resolution",
        "java.timeline.remove",
        "java.app.save-timeline-structure",
        "java.app.save-editor-state",
    ],
    "connect-livewindow": [
        "java.preview.connect",
        "java.preview.configure-live-window",
        "java.preview.register-callbacks",
        "java.preview.build-seek-flags",
        "java.preview.set-seek-scale",
        "java.preview.seek",
        "java.preview.seek-with-fps",
        "java.preview.play",
        "java.preview.play-with-fps",
        "java.preview.current-position",
        "java.preview.read-engine-state",
        "java.preview.map-thumbnail-position",
    ],
    "apply-refresh-editor-child": [
        "java.editor.clear-supported-features",
        "java.editor.restore-supported-features",
        "java.app.save-editor-state",
        "java.preview.seek",
    ],
    "editor-session-orchestration": [
        "java.sdk.initialize",
        "java.app.load-project-state",
        "java.timeline.create",
        "java.app.restore-timeline-structure",
        "java.timeline.append-media-list",
        "java.preview.connect",
        "java.preview.register-callbacks",
        "java.editor.restore-supported-features",
        "java.preview.seek",
        "java.app.save-timeline-structure",
        "java.app.save-editor-state",
        "java.timeline.remove",
    ],
    "editor-project-v3-ownership": [
        "java.app.load-atomic-project-state",
        "java.app.create-stable-object-id",
        "java.timeline.create",
        "java.app.restore-timeline-structure",
        "java.editor.restore-supported-features",
        "java.app.save-atomic-project-state",
        "java.timeline.remove",
    ],
    "install-asset-package": [
        "java.asset.package-type",
        "java.asset.install-or-upgrade",
    ],
    "bundled-material-install": [
        "java.asset-center.list-bundled-materials",
        "java.asset.install-or-upgrade",
        "java.asset-center.install-bundled-package",
        "java.asset-center.register-bundled-font",
    ],
    "caption-sticker-edit": [
        "java.caption.add",
        "java.caption.set-text",
        "java.caption.remove",
        "java.caption.list-timeline",
        "java.caption.timeline-range",
        "java.caption.list-clip",
        "java.caption.clip-range",
        "java.caption.register-font",
        "java.caption.apply-readable-style",
        "java.caption.set-letter-spacing",
        "java.sticker.add",
        "java.sticker.remove",
        "java.sticker.add-custom",
        "java.sticker.list-timeline",
        "java.sticker.list-at-position",
        "java.sticker.timeline-range",
        "java.sticker.clip-range",
        "java.caption.add-compound",
        "java.caption.list-compound",
        "java.caption.compound-range",
        "java.caption.list-clip-compound",
        "java.caption.remove-compound",
        "java.caption.set-compound-text",
    ],
    "filter-effect-edit": [
        "java.effect.append-builtin",
        "java.effect.append-builtin-range",
        "java.effect.add-timeline-builtin",
        "java.effect.add-packaged-timeline",
        "java.effect.append-packaged",
        "java.effect.append-packaged-range",
        "java.effect.append-raw-builtin",
        "java.effect.append-raw-builtin-range",
        "java.effect.list-clip-fx",
        "java.effect.get-first-timeline-fx",
        "java.effect.remove-timeline-fx",
        "java.effect.set-float",
        "java.transition.set-builtin",
        "java.transition.set-packaged",
        "java.transition.get",
        "java.clip.configure-image-motion",
        "java.clip.is-audio-video",
    ],
    "audio-edit": [
        "java.audio.ensure-track",
        "java.audio.add-clip",
        "java.audio.add-clip-at",
        "java.audio.append-clip-default",
        "java.audio.get-clip",
        "java.audio.set-clip-volume",
        "java.audio.set-track-stereo-volume",
        "java.audio.set-fades",
        "java.timeline.set-theme-music-volume",
    ],
    "capture-preview-record": [
        "java.capture.build-preview-flags",
        "java.capture.register-callbacks",
        "java.capture.get-device-capability",
        "java.capture.start-preview",
        "java.capture.start-recording",
        "java.capture.start-recording-with-flags",
        "java.capture.start-recording-configured",
        "java.capture.pause-recording",
        "java.capture.resume-recording",
        "java.capture.list-effects",
        "java.capture.remove-effect",
        "java.capture.clear-effects",
        "java.capture.append-packaged-fx",
        "java.capture.stop-recording",
        "java.capture.stop-recording-synchronous",
    ],
    "compile-export": [
        "java.engine.stop",
        "java.export.configure",
        "java.export.resolution-grade",
        "java.export.bitrate-grade",
        "java.export.register-callbacks",
        "java.export.register-callback3",
        "java.export.compile",
        "java.export.compile-configured",
    ],
    "template-prepare-footage": list(TEMPLATE_PREPARE_STEP_UNITS),
    "template-replace-export": [
        *TEMPLATE_PREPARE_STEP_UNITS,
        "java.template.create-editor-timeline",
        *TEMPLATE_FINALIZE_STEP_UNITS,
    ],
    "cutsame-replace-export": [
        *TEMPLATE_PREPARE_STEP_UNITS,
        "java.template.create-cutsame-timeline",
        *TEMPLATE_FINALIZE_STEP_UNITS,
    ],
    "mimo-replace-export": [
        "java.mimo.extract-archive",
        "java.mimo.parse-package",
        "java.mimo.install-extracted-child-packages",
        "java.mimo.build-timeline",
        "java.mimo.reconnect-preview",
        "java.mimo.export",
    ],
}

def slug(value):
    value = re.sub(r"[^a-zA-Z0-9]+", "-", str(value).strip().casefold()).strip("-")
    return value or "feature"

def required_capabilities(modules, required_module_ids):
    return sorted(
        {
            capability
            for module_id in required_module_ids
            for capability in modules.get(module_id, {}).get("provides", [])
        }
    )

def feature_lifecycle_hook(module, units_by_id, step_unit_ids):
    for unit_id in step_unit_ids:
        unit = units_by_id.get(unit_id)
        if unit and unit.get("lifecycle_hook") in LIFECYCLE_HOOKS:
            return unit["lifecycle_hook"]
    if module["id"] == "app-runtime":
        return "sdk_init"
    if module["id"] == "permission-gates":
        return "activity_create"
    if "asset" in module["id"]:
        return "asset_installed"
    if any(token in module["id"] for token in ("editor", "timeline", "audio", "effect")):
        return "before_structural_mutation"
    return "activity_create"

def build_simple_code_registry(registry):
    modules = {item["id"]: item for item in registry.get("modules", [])}
    units = []
    module_unit_ids = defaultdict(list)
    for (
        unit_id,
        feature,
        module_id,
        source,
        symbol,
        api_members,
        inputs,
        provides,
    ) in JAVA_UNIT_SPECS:
        module = modules[module_id]
        code = extract_method((skill_dir() / source).read_text(encoding="utf-8"), symbol)
        source_labels = module.get("demo_evidence", []) or module.get("simple_code_refs", [])
        compose_after_units = list(UNIT_COMPOSE_AFTER.get(unit_id, []))
        lifecycle_hook = UNIT_LIFECYCLE_HOOKS.get(unit_id, "activity_create")
        if unit_id in STRUCTURAL_MUTATION_UNIT_IDS:
            if "java.engine.stop" not in compose_after_units:
                compose_after_units.append("java.engine.stop")
            if unit_id != "java.timeline.remove":
                lifecycle_hook = "before_structural_mutation"
        unit = unit_contract(
            unit_id,
            "java_unit",
            module.get("priority", "P2"),
            feature,
            source_labels[0] if source_labels else module_id,
            api_members,
            module.get("requires", []),
            inputs,
            provides,
            module.get("resources", []),
            module.get("guards", []),
            [module_id, *module_blueprints(registry, module_id)],
            module.get("simple_code_refs", []),
            code=code,
            template_source=source,
            source_symbol=symbol,
            api_signatures=UNIT_API_SIGNATURES.get(unit_id, []),
            implementation_state="compiled_unit",
            requires_modules=module.get("requires", []),
            requires_capabilities=required_capabilities(
                modules,
                module.get("requires", []),
            ),
            compose_after_units=compose_after_units,
            lifecycle_hook=lifecycle_hook,
        )
        units.append(unit)
        if unit_id not in MODULE_RENDER_UNIT_EXCLUSIONS.get(module_id, set()):
            module_unit_ids[module_id].append(unit_id)

    for recipe in registry.get("api_recipes", []):
        recipe_id = f"recipe.{recipe['id']}"
        owning_modules = [
            module["id"]
            for module in modules.values()
            if recipe["id"] in module.get("api_recipes", [])
        ]
        step_unit_ids = [
            unit_id for unit_id in RECIPE_STEP_UNITS.get(recipe["id"], [])
            if any(unit["id"] == unit_id for unit in units)
        ]
        targets = list(owning_modules)
        for module_id in owning_modules:
            targets.extend(module_blueprints(registry, module_id))
        unit = unit_contract(
            recipe_id,
            "recipe",
            recipe.get("priority", "P2"),
            recipe.get("title", recipe["id"]),
            (recipe.get("demo_evidence") or [recipe["id"]])[0],
            RECIPE_API_MEMBERS.get(recipe["id"], []),
            recipe.get("requires", []),
            recipe.get("resources", []),
            recipe.get("provides", []),
            recipe.get("resources", []),
            recipe.get("guards", []),
            targets,
            recipe.get("simple_code_refs", []),
            steps=step_unit_ids,
            implementation_state="generated_module" if step_unit_ids else "contract_only",
            requires_modules=recipe.get("requires", []),
            requires_capabilities=required_capabilities(
                modules,
                recipe.get("requires", []),
            ),
            compose_after_units=step_unit_ids,
            lifecycle_hook=RECIPE_LIFECYCLE_HOOKS.get(
                recipe["id"],
                "activity_create",
            ),
        )
        units.append(unit)
        for module_id in owning_modules:
            module_unit_ids[module_id].append(recipe_id)

    feature_recipe_ids_by_module = defaultdict(list)
    existing_unit_ids = {unit["id"] for unit in units}
    for feature in registry.get("demo_feature_coverage", []):
        module = modules.get(feature.get("module_id"))
        if not module:
            continue
        feature_slug = slug(feature.get("feature", module["id"]))
        unit_id = f"recipe.feature.{feature_slug}"
        if unit_id in existing_unit_ids:
            unit_id = f"{unit_id}.{slug(module['id'])}"
        step_unit_ids = [
            unit_id
            for unit_id in module_unit_ids.get(module["id"], [])
            if unit_id in existing_unit_ids
        ]
        direct_steps = [
            unit_id
            for unit_id in step_unit_ids
            if next((unit for unit in units if unit["id"] == unit_id), {}).get("implementation_state")
            in {"compiled_unit", "generated_module"}
        ]
        if direct_steps:
            implementation_state = (
                "compiled_unit"
                if any(
                    next((unit for unit in units if unit["id"] == unit_id), {}).get("implementation_state")
                    == "compiled_unit"
                    for unit_id in direct_steps
                )
                else "generated_module"
            )
        else:
            implementation_state = "contract_only"
        units_by_id = {unit["id"]: unit for unit in units}
        unit = unit_contract(
            unit_id,
            "recipe",
            feature.get("priority", module.get("priority", "P3")),
            feature.get("feature", module["title"]),
            (
                module.get("simple_code_refs", ["asset-center-workflow.md"])[0]
                if module["id"] == "asset-center-service"
                else (feature.get("source_labels") or module.get("demo_evidence") or [module["id"]])[0]
            ),
            sorted(
                {
                    api_member
                    for step_id in step_unit_ids
                    for api_member in next(
                        (unit for unit in units if unit["id"] == step_id),
                        {},
                    ).get("api_members", [])
                }
            ),
            module.get("requires", []),
            module.get("resources", []),
            module.get("provides", []),
            module.get("resources", []),
            module.get("guards", []),
            [module["id"], *module_blueprints(registry, module["id"])],
            module.get("simple_code_refs", []),
            steps=step_unit_ids,
            implementation_state=implementation_state,
            requires_modules=module.get("requires", []),
            requires_capabilities=required_capabilities(
                modules,
                module.get("requires", []),
            ),
            compose_after_units=step_unit_ids,
            lifecycle_hook=feature_lifecycle_hook(
                module,
                units_by_id,
                step_unit_ids,
            ),
        )
        units.append(unit)
        existing_unit_ids.add(unit_id)
        feature_recipe_ids_by_module[module["id"]].append(unit_id)

    for module in registry.get("modules", []):
        module["simple_code_ids"] = sorted(
            set(module_unit_ids[module["id"]] + feature_recipe_ids_by_module[module["id"]])
        )
    for recipe in registry.get("api_recipes", []):
        recipe["simple_code_ids"] = [f"recipe.{recipe['id']}"]
    return {
        "version": SCHEMA_VERSION,
        "description": (
            "Schema v2 reusable units distilled from Demo evidence, skill-owned templates, "
            "and SDK jar signatures. Legacy snippets are evidence_fragment sources only."
        ),
        "coverage_states": sorted(IMPLEMENTATION_STATES),
        "legacy_evidence_policy": {
            "kind": "evidence_fragment",
            "id_preservation": True,
            "runtime_external_demo_required": False,
            "files": sorted(
                path.name
                for path in (skill_dir() / "references").glob("demo-simple-snippets-*.md")
            ),
        },
        "units": sorted(units, key=lambda item: item["id"]),
    }

def build_feature_map(registry, simple_registry, feature_priorities):
    unit_index = {unit["id"]: unit for unit in simple_registry["units"]}
    modules = {module["id"]: module for module in registry.get("modules", [])}

    def collect_unit_states(unit_id, active=None):
        active = active or set()
        if unit_id in active or unit_id not in unit_index:
            return set()
        active.add(unit_id)
        unit = unit_index[unit_id]
        states = {unit.get("implementation_state", "contract_only")}
        for child_id in unit.get("steps", []) + unit.get("compose_after_units", []):
            states.update(collect_unit_states(child_id, active))
        active.remove(unit_id)
        return states

    rows = []
    for feature in registry.get("demo_feature_coverage", []):
        module = modules[feature["module_id"]]
        unit_ids = module.get("simple_code_ids", [])
        states = set()
        for unit_id in unit_ids:
            states.update(collect_unit_states(unit_id))
        row = dict(feature)
        row["priority"] = feature_priorities.get(feature["feature"], module.get("priority", "P3"))
        row["simple_code_ids"] = unit_ids
        row["feature_recipe_id"] = next(
            (
                unit_id
                for unit_id in unit_ids
                if unit_id.startswith("recipe.feature.")
            ),
            "",
        )
        if "runtime_verified" in states:
            coverage_status = "runtime_verified"
        elif "compiled_unit" in states:
            coverage_status = "compiled_unit"
        elif "generated_module" in states:
            coverage_status = "generated_module"
        elif states:
            coverage_status = "contract_only"
        else:
            coverage_status = "evidence_only"
        row["coverage_status"] = coverage_status
        row["parent_modules"] = module.get("requires", [])
        row["removable"] = module.get("priority") != "P0"
        rows.append(row)
        feature.update(
            {
                "simple_code_ids": unit_ids,
                "priority": row["priority"],
                "coverage_status": row["coverage_status"],
                "feature_recipe_id": row["feature_recipe_id"],
            }
        )
    return {
        "version": SCHEMA_VERSION,
        "feature_count": len(rows),
        "coverage": dict(Counter(row["coverage_status"] for row in rows)),
        "features": rows,
    }

def compact_ast(methods):
    records = {}
    for method in methods:
        sequence = [
            f"{item['owner']}.{item['method']}"
            for item in method.get("invocations", [])
        ]
        for invocation in method.get("invocations", []):
            member = f"{invocation['owner']}.{invocation['method']}"
            record = records.setdefault(
                member,
                {
                    "member": member,
                    "kind": "method",
                    "occurrences": 0,
                    "source_labels": [],
                    "arities": [],
                    "call_orders": [],
                },
            )
            record["occurrences"] += 1
            source_label = f"{method['source']}:{invocation['line']}"
            if source_label not in record["source_labels"] and len(record["source_labels"]) < 8:
                record["source_labels"].append(source_label)
            if invocation["arity"] not in record["arities"]:
                record["arities"].append(invocation["arity"])
            call_order = {
                "source": f"{method['source']}:{method['start_line']}",
                "method": method["method"],
                "sequence": sequence,
            }
            if call_order not in record["call_orders"] and len(record["call_orders"]) < 3:
                record["call_orders"].append(call_order)
    return records

def infer_api_domains(row):
    owner = row.get("owner", "")
    member_name = row.get("member_name", "")
    normalized_name = member_name.casefold()
    domains = set(API_OWNER_DOMAINS.get(owner, []))

    if owner in CAPTION_OBJECT_OWNERS or "caption" in owner.casefold() or owner.endswith("Span"):
        domains.add("caption-editing")
    if owner in STICKER_OBJECT_OWNERS or "sticker" in owner.casefold():
        domains.add("sticker-editing")
    if owner.startswith("NvsCapture"):
        domains.add("capture-recording")

    if owner == "NvsStreamingContext":
        specialized_domains = set()
        if any(token in normalized_name for token in (
            "capture", "record", "camera", "focus", "flash", "zoom", "exposure"
        )):
            specialized_domains.add("capture-recording")
        if any(token in normalized_name for token in (
            "human", "beauty", "arscene", "face", "hand", "segmentation", "device_power"
        )):
            specialized_domains.add("ar-beauty-segmentation")
        if any(token in normalized_name for token in ("compile", "bitrate", "gop_size")):
            specialized_domains.add("export-compile")
        if any(token in normalized_name for token in (
            "playback", "seek", "livewindow", "streaming_engine_seek", "streaming_engine_playback"
        )):
            specialized_domains.add("preview-playback")
        if "template" in normalized_name:
            specialized_domains.add("template-workflows")
        if any(token in normalized_name for token in (
            "grabimage", "frame", "av_file", "detectvideofile", "videofxdescription"
        )):
            specialized_domains.add("media-inspection")
        if specialized_domains:
            domains.discard("core-runtime")
            domains.update(specialized_domains)

    if owner == "NvsTimeline":
        if "caption" in normalized_name:
            domains.add("caption-editing")
        if "sticker" in normalized_name:
            domains.add("sticker-editing")
        if "audio" in normalized_name or "music" in normalized_name:
            domains.add("audio-editing")
        if "theme" in normalized_name or "template" in normalized_name:
            domains.add("template-workflows")
        if "fx" in normalized_name:
            domains.add("effect-parameters")

    if owner == "NvsVideoClip":
        if "caption" in normalized_name:
            domains.add("caption-editing")
        if "sticker" in normalized_name:
            domains.add("sticker-editing")
        if "fx" in normalized_name or "roi" in normalized_name or "background" in normalized_name:
            domains.add("effect-parameters")

    if owner == "NvsAssetPackageManager":
        if "caption" in normalized_name:
            domains.add("caption-editing")
        if "sticker" in normalized_name:
            domains.add("sticker-editing")
        if "transition" in normalized_name:
            domains.add("transition-editing")
        if any(token in normalized_name for token in ("arscene", "face_mesh", "makeup", "warp")):
            domains.add("ar-beauty-segmentation")
        if "template" in normalized_name or "teimplate" in normalized_name or "theme" in normalized_name:
            domains.add("template-workflows")
        if "capturescene" in normalized_name:
            domains.add("capture-recording")

    if not domains:
        domains.add("core-runtime")
    return sorted(domains)

def evidence_only_disposition(row):
    primary_domain = row["domain_ids"][0]
    domain_title = API_DOMAIN_CONTRACTS[primary_domain]["title"]
    owner = row.get("owner", "SDK object")
    member_name = row.get("member_name", "member")
    normalized_name = member_name.casefold()

    if row.get("kind") == "field":
        return (
            f"{primary_domain}.typed_constant",
            f"Typed {owner} constant used by {domain_title}; keep the SDK symbol rather than copying its raw value or generating a standalone operation.",
        )
    if owner.endswith("Span") or owner in {"NvsCaptionSpan", "NvsExpressionParam"}:
        return (
            f"{primary_domain}.value_object_contract",
            f"{owner}.{member_name} is a value-object accessor/mutator used while assembling a larger {domain_title} operation; its receiver must come from the active SDK object graph.",
        )
    if "callback" in normalized_name:
        return (
            f"{primary_domain}.callback_contract",
            f"{owner}.{member_name} registers an asynchronous callback whose lifetime belongs to the surrounding {domain_title} controller; retain the exact signature and Demo ordering instead of emitting an unowned listener.",
        )
    if owner == "NvsEffectRenderCore" or "render" in normalized_name:
        return (
            "render-core.opengl_operation",
            f"{owner}.{member_name} requires caller-owned OpenGL context, textures, and render-thread teardown; no context-free Java unit can safely represent that pipeline.",
        )
    if normalized_name.startswith(("get", "is", "has", "find")):
        return (
            f"{primary_domain}.read_only_query",
            f"{owner}.{member_name} is a read-only query used to branch a {domain_title} workflow; validate its returned status/object in the related module rather than counting a getter wrapper as implementation.",
        )
    if normalized_name.startswith(("close", "release", "cleanup", "clean", "cancel", "destory")):
        return (
            f"{primary_domain}.owned_lifecycle_operation",
            f"{owner}.{member_name} releases or cancels caller-owned {domain_title} state and must be paired with the exact creator/task owner; it remains evidence until that owner is selected.",
        )
    return (
        f"{primary_domain}.stateful_operation_requires_context",
        f"{owner}.{member_name} mutates specialized {domain_title} state but the Demo receiver, resource, or lifecycle owner cannot be reduced to a safe context-free unit; use the related module contract and retained Demo call order.",
    )

def annotate_api_map(api_map, registry):
    module_index = {module["id"]: module for module in registry.get("modules", [])}
    for row in api_map.get("api_members", []):
        domain_ids = infer_api_domains(row)
        domain_module_ids = {
            module_id
            for domain_id in domain_ids
            for module_id in API_DOMAIN_CONTRACTS[domain_id]["module_ids"]
            if module_id in module_index
        }
        row["domain_ids"] = domain_ids
        row["module_ids"] = sorted(set(row.get("module_ids", [])) | domain_module_ids)
        row["prerequisites"] = sorted(
            set(row.get("prerequisites", []))
            | {
                required
                for module_id in row["module_ids"]
                for required in module_index[module_id].get("requires", [])
            }
        )
        row["resources"] = sorted(
            set(row.get("resources", []))
            | {
                resource
                for module_id in row["module_ids"]
                for resource in module_index[module_id].get("resources", [])
            }
        )
        row["related_recipe_ids"] = sorted(
            {
                recipe_id
                for module_id in row["module_ids"]
                for recipe_id in (
                    list(module_index[module_id].get("api_recipes", []))
                    + [
                        unit_id
                        for unit_id in module_index[module_id].get("simple_code_ids", [])
                        if unit_id.startswith("recipe.")
                    ]
                )
            }
        )
        row["classification_source"] = "member-level owner/name rules"
        row["processing_disposition"] = row.get("coverage_status", "contract_only")
        if row.get("coverage_status") == "evidence_only":
            reason_code, reason = evidence_only_disposition(row)
            row["evidence_only_reason_code"] = reason_code
            row["evidence_only_reason"] = reason
        else:
            row.pop("evidence_only_reason_code", None)
            row.pop("evidence_only_reason", None)

    api_map["domain_contracts"] = [
        {
            "id": domain_id,
            "title": contract["title"],
            "module_ids": list(contract["module_ids"]),
        }
        for domain_id, contract in sorted(API_DOMAIN_CONTRACTS.items())
    ]
    return api_map

def build_p3_processing_report(api_map, frozen_scope):
    row_index = {
        row["stable_id"]: row
        for row in api_map.get("api_members", [])
    }
    target_ids = frozen_scope.get("target_stable_ids", [])
    items = []
    for stable_id in target_ids:
        row = row_index.get(stable_id)
        if row is None:
            items.append({"stable_id": stable_id, "processing_disposition": "missing"})
            continue
        item = {
            "stable_id": stable_id,
            "owner": row.get("owner", ""),
            "member_name": row.get("member_name", ""),
            "kind": row.get("kind", ""),
            "occurrences": row.get("occurrences", 0),
            "domain_ids": row.get("domain_ids", []),
            "module_ids": row.get("module_ids", []),
            "related_recipe_ids": row.get("related_recipe_ids", []),
            "simple_code_ids": row.get("simple_code_ids", []),
            "coverage_status": row.get("coverage_status", ""),
            "processing_disposition": row.get("processing_disposition", ""),
        }
        if row.get("coverage_status") == "evidence_only":
            item["evidence_only_reason_code"] = row.get("evidence_only_reason_code", "")
            item["evidence_only_reason"] = row.get("evidence_only_reason", "")
        items.append(item)

    generic_reason = "Demo-observed API surface has no exact compiled/generated unit."
    return {
        "schema_version": 1,
        "frozen_scope": "p3-api-processing-scope.json",
        "target_count": len(target_ids),
        "processed_count": sum(item.get("processing_disposition") != "missing" for item in items),
        "upgraded_count": sum(
            item.get("coverage_status") in {"compiled_unit", "generated_module", "runtime_verified"}
            for item in items
        ),
        "retained_evidence_count": sum(
            item.get("coverage_status") == "evidence_only" for item in items
        ),
        "coverage_counts": dict(sorted(Counter(item.get("coverage_status", "missing") for item in items).items())),
        "domain_counts": dict(sorted(Counter(domain_id for item in items for domain_id in item.get("domain_ids", [])).items())),
        "reason_code_counts": dict(sorted(Counter(item.get("evidence_only_reason_code") for item in items if item.get("evidence_only_reason_code")).items())),
        "unclassified_count": sum(not item.get("domain_ids") for item in items),
        "missing_module_count": sum(not item.get("module_ids") for item in items),
        "generic_reason_count": sum(item.get("evidence_only_reason") == generic_reason for item in items),
        "items": items,
    }

def infer_guards(member):
    method = member.rsplit(".", 1)[-1].casefold()
    guards = ["receiver/prerequisite objects must be non-null"]
    if any(token in method for token in ("trim", "duration", "point", "seek", "playback", "clip")):
        guards.append("time values use microseconds and stay within media/timeline bounds")
    if any(token in method for token in ("package", "packaged", "asset")):
        guards.append("package type, path/id, license, and install result must be validated")
    if any(token in method for token in ("capture", "record")):
        guards.append("permission and streaming engine state gates are required")
    if any(token in method for token in ("compile", "playback", "record", "stop")):
        guards.append("avoid conflicting playback/capture/compile state")
    return guards

def build_official_doc_index(references_dir, signatures):
    members_by_token = defaultdict(set)
    for signature in signatures.get("members", []):
        member_name = signature.get("member_name", "")
        if not member_name or member_name == "<init>":
            continue
        members_by_token[member_name].add(signature["member"])
    if not members_by_token:
        return {}
    token_pattern = re.compile(
        r"\b(?:"
        + "|".join(
            re.escape(token)
            for token in sorted(members_by_token, key=len, reverse=True)
        )
        + r")\b"
    )
    refs = defaultdict(list)
    for path in sorted(references_dir.glob("official-*.md")):
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(),
            start=1,
        ):
            for token in set(token_pattern.findall(line)):
                source_ref = f"{path.name}:{line_number}"
                for member in members_by_token[token]:
                    if source_ref not in refs[member] and len(refs[member]) < 8:
                        refs[member].append(source_ref)
    return refs

def infer_threading(owner, kind):
    if kind == "field":
        return ["none"]
    if owner in {"NvsEffectRenderCore", "NvsEffectRenderCoreProxy"}:
        return ["opengl_render_thread"]
    return ["android_main_thread"]

def infer_lifecycle(member):
    name = member.rsplit(".", 1)[-1].casefold()
    if name in {"init", "getinstance"} or name.startswith("setuphumandetection"):
        return ["sdk_init"]
    if "connect" in name and "livewindow" in name:
        return ["live_window_bound"]
    if "assetpackage" in name or "package" in name and any(
        token in name for token in ("install", "upgrade", "status")
    ):
        return ["asset_installed"]
    if any(token in name for token in ("remove", "delete", "trim", "split", "transition")):
        return ["before_structural_mutation", "after_mutation_refresh"]
    if any(token in name for token in ("appendclip", "insertclip", "createtimeline")):
        return ["timeline_created"]
    if any(token in name for token in ("close", "destroy", "removetimeline")):
        return ["destroy"]
    if any(token in name for token in ("seek", "playback", "livewindow")):
        return ["live_window_bound"]
    return ["activity_create"]

def infer_state_conflicts(member):
    name = member.rsplit(".", 1)[-1].casefold()
    conflicts = []
    if any(token in name for token in ("remove", "trim", "split", "transition", "compile")):
        conflicts.extend(["playback", "capture_recording", "compile"])
    elif any(token in name for token in ("capture", "record")):
        conflicts.extend(["timeline_playback", "compile"])
    elif "playback" in name or "seek" in name:
        conflicts.extend(["capture_recording", "compile"])
    return conflicts

def infer_return_handling(return_type, kind):
    if kind == "field":
        return "Use as a typed SDK constant; do not treat the raw value as a portable enum."
    if return_type == "void":
        return "No direct return value; observe SDK callbacks or state when the operation is asynchronous."
    if return_type == "boolean":
        return "Check false and stop the dependent workflow before mutating application state."
    if return_type in {"byte", "short", "int", "long"}:
        return "Validate status/error/time values against the documented constants and valid bounds."
    if return_type in {"float", "double"}:
        return "Validate finite numeric output before using it in UI or SDK parameters."
    return "Check for null before using the returned SDK object."

def infer_failure_paths(member, return_type, kind):
    name = member.rsplit(".", 1)[-1].casefold()
    failures = []
    if kind != "field" and return_type != "void":
        failures.append("return value indicates failure or is null")
    if any(token in name for token in ("capture", "record")):
        failures.append("permission, device capability, or streaming engine state is invalid")
    if any(token in name for token in ("install", "upgrade", "package")):
        failures.append("package path, license, package type, or install result is invalid")
    if any(token in name for token in ("compile", "export")):
        failures.append("output path, timeline range, encoder, or engine state is invalid")
    if any(token in name for token in ("trim", "point", "duration", "seek", "playback")):
        failures.append("time value is outside media or timeline bounds")
    return failures or ["required receiver or prerequisite object is unavailable"]

def invocation_arities(code, member_name):
    arities = set()
    pattern = re.compile(rf"\b{re.escape(member_name)}\s*\(")
    for match in pattern.finditer(code):
        index = match.end()
        depth = 1
        commas = 0
        has_argument = False
        quote = ""
        escaped = False
        while index < len(code) and depth:
            character = code[index]
            if quote:
                if escaped:
                    escaped = False
                elif character == "\\":
                    escaped = True
                elif character == quote:
                    quote = ""
            elif character in {'"', "'"}:
                quote = character
                has_argument = True
            elif character == "(":
                depth += 1
                has_argument = True
            elif character == ")":
                depth -= 1
            elif depth == 1 and character == ",":
                commas += 1
            elif depth == 1 and not character.isspace():
                has_argument = True
            index += 1
        if depth == 0:
            arities.add(commas + 1 if has_argument else 0)
    return arities

def build_api_map(
    api_classes,
    direct_members,
    ast_members,
    sdk_signatures,
    simple_registry,
    class_priorities,
    member_priorities,
    valid_module_ids,
    official_doc_index,
):
    merged = {key: dict(value) for key, value in direct_members.items()}
    for member, ast_record in ast_members.items():
        record = merged.setdefault(
            member,
            {
                "member": member,
                "kind": "method",
                "occurrences": 0,
                "source_labels": [],
                "arities": [],
            },
        )
        record.update(
            {
                "kind": "method",
                "occurrences": max(record.get("occurrences", 0), ast_record["occurrences"]),
                "source_labels": ast_record["source_labels"],
                "arities": sorted(ast_record["arities"]),
                "call_orders": ast_record["call_orders"],
            }
        )
    units = simple_registry["units"]
    unit_index = {unit["id"]: unit for unit in units}
    member_units = defaultdict(list)
    explicit_signature_units = defaultdict(list)
    for unit in units:
        for member in unit.get("api_members", []):
            member_units[member].append(unit["id"])
        for stable_id in unit.get("api_signatures", []):
            explicit_signature_units[stable_id].append(unit["id"])
    signatures_by_member = defaultdict(list)
    explicit_ids_by_member = defaultdict(set)
    for signature in sdk_signatures.get("members", []):
        signatures_by_member[signature["member"]].append(signature)
        if signature["stable_id"] in explicit_signature_units:
            explicit_ids_by_member[signature["member"]].add(signature["stable_id"])
    exact_signature_units = defaultdict(list)
    for signature in sdk_signatures.get("members", []):
        stable_id = signature["stable_id"]
        exact_signature_units[stable_id].extend(
            explicit_signature_units.get(stable_id, [])
        )
        for unit_id in member_units.get(signature["member"], []):
            unit = unit_index[unit_id]
            explicit_ids = set(unit.get("api_signatures", []))
            explicit_for_member = {
                candidate_id
                for candidate_id in explicit_ids
                if candidate_id.startswith(
                    f"{signature['owner']}#{signature['member_name']}"
                )
            }
            if explicit_for_member:
                if stable_id in explicit_for_member:
                    exact_signature_units[stable_id].append(unit_id)
                continue
            if signature["kind"] == "field":
                exact_signature_units[stable_id].append(unit_id)
                continue
            arities = invocation_arities(
                unit.get("code", ""),
                signature["member_name"],
            )
            if signature.get("arity") in arities:
                exact_signature_units[stable_id].append(unit_id)

    def coverage_for_units(unit_ids, has_demo_evidence, has_jar_signature):
        states = {
            unit_index[unit_id].get("implementation_state", "contract_only")
            for unit_id in unit_ids
            if unit_id in unit_index
        }
        if "runtime_verified" in states:
            return "runtime_verified"
        if "compiled_unit" in states:
            return "compiled_unit"
        if "generated_module" in states:
            return "generated_module"
        if has_demo_evidence:
            return "evidence_only"
        if unit_ids or has_jar_signature:
            return "contract_only"
        return "contract_only"

    def module_ids_for_units(unit_ids):
        return sorted(
            {
                target
                for unit_id in unit_ids
                for target in unit_index[unit_id].get("compose_into", [])
                if target in valid_module_ids
            }
        )

    def prerequisite_modules_for_units(unit_ids):
        return sorted(
            {
                required
                for unit_id in unit_ids
                for required in unit_index[unit_id].get("requires_modules", [])
            }
        )

    def resources_for_units(unit_ids):
        return sorted(
            {
                resource
                for unit_id in unit_ids
                for resource in unit_index[unit_id].get("resources", [])
            }
        )

    rows = []
    seen_signature_ids = set()
    relevant_members = set(merged) | set(member_units)
    for signature in sorted(sdk_signatures.get("members", []), key=lambda item: item["stable_id"]):
        member = signature["member"]
        if member not in relevant_members:
            continue
        record = merged.get(member, {})
        arities = record.get("arities", [])
        if (
            explicit_ids_by_member.get(member)
            and signature["stable_id"] not in explicit_ids_by_member[member]
            and arities
            and signature.get("arity") not in arities
            and signature["kind"] != "field"
        ):
            continue
        if (
            arities
            and signature.get("arity") not in arities
            and signature["kind"] != "field"
            and member not in member_units
        ):
            continue
        has_matching_demo_shape = bool(record) and (
            not arities
            or signature.get("arity") in arities
            or signature["kind"] == "field"
        )
        owner = signature["owner"]
        unit_ids = sorted(set(exact_signature_units.get(signature["stable_id"], [])))
        direct_ids = [
            unit_id
            for unit_id in unit_ids
            if unit_index[unit_id].get("implementation_state") == "compiled_unit"
        ]
        coverage_status = coverage_for_units(
            unit_ids,
            has_matching_demo_shape,
            True,
        )
        row = {
            "id": signature["stable_id"],
            "stable_id": signature["stable_id"],
            "member": member,
            "owner": owner,
            "full_owner": signature.get("full_owner", ""),
            "member_name": signature.get("member_name", ""),
            "signature": signature["stable_id"],
            "descriptor": signature.get("descriptor", ""),
            "declaration": signature.get("declaration", ""),
            "kind": signature.get("kind", "unknown"),
            "priority": member_priorities.get(member, "P3"),
            "occurrences": record.get("occurrences", 0) if has_matching_demo_shape else 0,
            "source_labels": record.get("source_labels", []) if has_matching_demo_shape else [],
            "arities": [signature.get("arity", 0)] if signature.get("kind") != "field" else [],
            "parameters": signature.get("parameters", []),
            "parameter_types": signature.get("parameter_types", []),
            "parameter_names_inferred": False,
            "returns": signature.get("returns", {"descriptor": "", "java_type": ""}),
            "return_type": signature.get("return_type", ""),
            "modifiers": signature.get("modifiers", []),
            "is_static": signature.get("is_static", False),
            "is_final": signature.get("is_final", False),
            "constant_value": signature.get("constant_value"),
            "overload_ids": signature.get("overload_ids", [signature["stable_id"]]),
            "declared_owner": signature.get("declared_owner", signature.get("full_owner", "")),
            "official_doc_refs": official_doc_index.get(member, []),
            "prerequisites": prerequisite_modules_for_units(unit_ids),
            "guards": infer_guards(member),
            "resources": resources_for_units(unit_ids),
            "threading": infer_threading(owner, signature.get("kind", "unknown")),
            "lifecycle": infer_lifecycle(member),
            "state_conflicts": infer_state_conflicts(member),
            "return_handling": infer_return_handling(
                signature.get("return_type", ""),
                signature.get("kind", "unknown"),
            ),
            "failure_paths": infer_failure_paths(
                member,
                signature.get("return_type", ""),
                signature.get("kind", "unknown"),
            ),
            "simple_code_ids": unit_ids,
            "direct_compiled_unit_ids": direct_ids,
            "module_ids": module_ids_for_units(unit_ids),
            "coverage_status": coverage_status,
            "jar_signature": True,
            "observed_in_demo": has_matching_demo_shape,
            "call_orders": record.get("call_orders", []) if has_matching_demo_shape else [],
            "semantic_source": "SDK jar descriptor; Demo AST evidence when observed; official docs provide usage semantics where referenced.",
        }
        if coverage_status == "evidence_only":
            row["evidence_only_reason"] = (
                "Demo-observed API surface has no exact compiled/generated unit."
            )
        rows.append(row)
        seen_signature_ids.add(signature["stable_id"])

    for member in sorted(merged):
        if member in signatures_by_member:
            continue
        record = merged[member]
        owner = member.split(".", 1)[0]
        unit_ids = sorted(set(member_units.get(member, [])))
        if not unit_ids:
            continue
        direct_ids = [
            unit_id
            for unit_id in unit_ids
            if unit_index[unit_id].get("implementation_state") == "compiled_unit"
        ]
        coverage_status = coverage_for_units(unit_ids, True, False)
        row = {
            "id": f"{owner}#{member.split('.', 1)[-1]}",
            "stable_id": f"{owner}#{member.split('.', 1)[-1]}",
            "member": member,
            "owner": owner,
            "full_owner": "",
            "member_name": member.split(".", 1)[-1] if "." in member else member,
            "signature": member,
            "descriptor": "",
            "declaration": "",
            "kind": record.get("kind", "unknown"),
            "priority": member_priorities.get(member, "P3"),
            "occurrences": record.get("occurrences", 0),
            "source_labels": record.get("source_labels", []),
            "arities": record.get("arities", []),
            "parameters": [],
            "parameter_types": [],
            "parameter_names_inferred": False,
            "returns": {"descriptor": "", "java_type": ""},
            "return_type": "",
            "modifiers": [],
            "is_static": False,
            "is_final": False,
            "constant_value": None,
            "overload_ids": [f"{owner}#{member.split('.', 1)[-1]}"],
            "declared_owner": "",
            "official_doc_refs": official_doc_index.get(member, []),
            "prerequisites": prerequisite_modules_for_units(unit_ids),
            "guards": infer_guards(member),
            "resources": resources_for_units(unit_ids),
            "threading": infer_threading(owner, record.get("kind", "unknown")),
            "lifecycle": infer_lifecycle(member),
            "state_conflicts": infer_state_conflicts(member),
            "return_handling": "No public jar signature is available; use Demo evidence only.",
            "failure_paths": ["public SDK signature could not be verified"],
            "simple_code_ids": unit_ids,
            "direct_compiled_unit_ids": direct_ids,
            "module_ids": module_ids_for_units(unit_ids),
            "coverage_status": coverage_status,
            "jar_signature": False,
            "observed_in_demo": True,
            "call_orders": record.get("call_orders", []),
            "semantic_source": "Demo evidence only; no matching public SDK jar signature was found.",
        }
        if coverage_status == "evidence_only":
            row["evidence_only_reason"] = (
                "Demo/member inventory surface has no matching public jar signature and no exact unit."
            )
        rows.append(row)
    type_rows = []
    signature_classes = {item["class"]: item for item in sdk_signatures.get("classes", [])}
    observed_classes = {item["class"]: item for item in api_classes}
    for owner in sorted(set(signature_classes) | set(observed_classes)):
        api_class = dict(observed_classes.get(owner, {}))
        if owner in signature_classes:
            api_class.update(signature_classes[owner])
        unit_ids = sorted(
            {
                unit["id"]
                for unit in units
                if owner in unit.get("api_classes", [])
            }
        )
        type_row = dict(api_class)
        type_row.setdefault("class", owner)
        type_row["priority"] = class_priorities.get(owner, "P3")
        type_row["simple_code_ids"] = unit_ids
        type_row["coverage_status"] = coverage_for_units(
            unit_ids,
            owner in observed_classes,
            owner in signature_classes,
        )
        type_row["jar_signature"] = owner in signature_classes
        type_rows.append(type_row)
    return {
        "version": SCHEMA_VERSION,
        "description": "Schema v2 per-type and per-member map built from SDK jar signatures plus Demo AST evidence.",
        "coverage_states": sorted(IMPLEMENTATION_STATES),
        "sdk_signature": {
            "class_count": sdk_signatures.get("class_count", 0),
            "member_count": sdk_signatures.get("member_count", 0),
            "error_count": len(sdk_signatures.get("errors", [])),
            "jdk_home": sdk_signatures.get("jdk_home", ""),
        },
        "type_count": len(type_rows),
        "member_count": len(rows),
        "observed_method_count": sum(
            row["kind"] == "method" and row.get("observed_in_demo")
            for row in rows
        ),
        "observed_without_jar_signature_count": sum(
            row.get("observed_in_demo") and not row.get("jar_signature")
            for row in rows
        ),
        "coverage": dict(Counter(row["coverage_status"] for row in rows)),
        "api_types": type_rows,
        "api_members": rows,
    }

def finish_registry_contracts(registry, simple_registry):
    modules = {item["id"]: item for item in registry.get("modules", [])}
    recipes = {item["id"]: item for item in registry.get("api_recipes", [])}
    for module in registry.get("modules", []):
        module["render_units"] = list(module.get("simple_code_ids", []))
        if module["id"] == "asset-center-service":
            # Keep renamed historical Demo features in the evidence graph without
            # rendering their old download/network-oriented recipe identifiers.
            module["render_units"] = [
                unit_id
                for unit_id in module["render_units"]
                if unit_id
                not in {
                    "recipe.feature.base",
                    "recipe.feature.download",
                    "recipe.feature.libnet",
                }
            ]
        module["manifest"] = {
            "permissions": list(module.get("permissions", [])),
            "activities": [],
            "metadata": [],
        }
        module["gradle"] = {
            "dependencies": ["app/libs/NvAndroidStreamingSdk.jar"],
            "min_sdk_required": 19,
            "uses_android_plugin": True,
        }
        module["resource_contract"] = {
            "resource_keys": list(module.get("resources", [])),
            "user_provided": [
                resource
                for resource in module.get("resources", [])
                if resource in {"R0", "R1", "R2", "R4", "R8", "R9", "R10", "R13"}
            ],
        }
        module["navigation"] = {
            "entry_points": list(module.get("provides", [])),
            "host_handles_navigation": module.get("level") in {"small_module", "big_module"},
        }
        module["host_contract"] = {
            "language": "Java",
            "threading": "Invoke NvsStreamingContext and NvsEffectSdkContext APIs on the Android main thread.",
            "integration_modes": list(module.get("integration_modes", [])),
            "does_not_overwrite_host": True,
        }
    for blueprint in registry.get("blueprints", []):
        if not blueprint.get("app_template") and blueprint["id"] in BLUEPRINT_APP_TEMPLATES:
            blueprint["app_template"] = BLUEPRINT_APP_TEMPLATES[blueprint["id"]]
        selected_modules = [
            modules[module_id]
            for module_id in blueprint.get("modules", [])
            if module_id in modules
        ]
        blueprint.setdefault("level", "app_blueprint")
        blueprint.setdefault("priority", "P1")
        blueprint.setdefault("category", "application-blueprint")
        blueprint.setdefault("requires", list(blueprint.get("modules", [])))
        blueprint.setdefault("provides", [f"{blueprint['id']} application workflow"])
        blueprint["api_recipes"] = sorted(
            {
                recipe_id
                for module in selected_modules
                for recipe_id in module.get("api_recipes", [])
                if recipe_id in recipes
            }
        )
        blueprint["simple_code_ids"] = sorted(
            {
                unit_id
                for module in selected_modules
                for unit_id in module.get("simple_code_ids", [])
            }
        )
        blueprint.setdefault(
            "simple_code_refs",
            sorted(
                {
                    ref
                    for module in selected_modules
                    for ref in module.get("simple_code_refs", [])
                }
            ),
        )
        blueprint["permissions"] = sorted(
            {
                permission
                for module in selected_modules
                for permission in module.get("permissions", [])
            }
        )
        blueprint.setdefault("guards", ["resolve module dependency closure before generation"])
        blueprint.setdefault("conflicts", ["apply no more than one product UI shell"])
        blueprint.setdefault("lifecycle", [blueprint.get("notes", "compose selected modules")])
        blueprint.setdefault(
            "demo_evidence",
            sorted(
                {
                    evidence
                    for module in selected_modules
                    for evidence in module.get("demo_evidence", [])
                }
            ),
        )
    registry["simple_code_registry"] = {
        "path": "simple-code-registry.json",
        "unit_count": len(simple_registry["units"]),
        "legacy_snippets_are_evidence_fragments": True,
        "schema_version": SCHEMA_VERSION,
    }
    return registry

def update_lookup_index(references_dir, registry):
    lookup_path = references_dir / "skill-lookup-index.json"
    lookup = load_json(lookup_path)
    modules = {module["id"]: module for module in registry.get("modules", [])}
    blueprints = {item["id"]: item for item in registry.get("blueprints", [])}
    entries = lookup.setdefault("entries", [])
    official_package_entry = {
        "id": "official-sdk-resources",
        "title": "Official Android LTS face package resource paths",
        "category": "android-integration",
        "aliases": [
            "official sdk download",
            "Android LTS SDK",
            "download SDK face version",
            "SDK face package",
            "SDK package resource path",
            "NvAndroidStreamingSdk.jar path",
            "libNvStreamingSdkCore.so path",
            "effectlib.jar path",
            "effectlib.jar 总包路径",
            "facemode model path",
            "NvAndroidStreamingSdk.jar 官网包路径",
            "官网下载SDK",
            "SDK下载及开发文档",
            "Android LTS",
            "下载SDK人脸版本",
            "官网SDK资源",
            "SDK总包",
            "总包资源目录",
            "人脸模型目录",
            "facemode 在哪里",
            "模板包是否在SDK下载包中",
            "Mimo 模板包是否在SDK下载包中",
        ],
        "api_classes": [
            "NvsStreamingContext",
            "NvsEffectSdkContext",
            "NvsAssetPackageManager",
        ],
        "feature_refs": [
            "official-sdk-download-resources.md",
            "resource-requirements-index.md",
            "default-sample-assets.md",
            "asset-center-workflow.md",
        ],
        "api_refs": ["android-integration.md"],
        "snippet_refs": [],
        "official_refs": [
            "official-sdk-download-resources.md",
            "official-core.md",
            "android-integration.md",
        ],
        "resource_keys": ["R0", "R4", "R8", "R9", "R10", "R13"],
        "module_ids": [
            "app-runtime",
            "asset-package-service",
            "beauty-camera",
            "makeup-service",
            "ar-scene",
            "segmentation-keying",
            "superzoom-ai",
            "template-engine",
            "cutsame-template",
            "mimo-template",
        ],
        "blueprint_ids": [
            "beauty-camera",
            "template-mimo-cutsame-app",
            "full-sdk-demo",
        ],
        "simple_code_refs": [
            "official-sdk-download-resources.md",
            "official-sdk-download-resource-map.json",
        ],
        "optional_template_features": ["beauty-ar"],
    }
    existing_official = next(
        (entry for entry in entries if entry.get("id") == "official-sdk-resources"),
        None,
    )
    if existing_official is None:
        entries.append(official_package_entry)
    else:
        existing_official.update(official_package_entry)
    for entry in entries:
        if entry.get("id") == "asset-center":
            entry.update(
                {
                    "title": "External local material catalog and authorized-resource guidance",
                    "category": "assets-packages",
                    "aliases": [
                        "asset center",
                        "material center",
                        "external local material",
                        "offline material",
                        "online material",
                        "material service",
                        "license acquisition",
                        "素材中心",
                        "本地素材",
                        "在线素材",
                        "素材服务",
                        "远程素材下载",
                        "下载素材",
                        "lic 获取",
                        "官网素材目录",
                        "官方SDK包素材路径",
                        "下载SDK人脸版本",
                    ],
                    "api_classes": [
                        "NvsAssetPackageManager",
                        "NvsStreamingContext",
                        "MeisheLocalMaterialCatalog",
                    ],
                    "resource_keys": ["R0", "R4"],
                    "feature_refs": [
                        "asset-center-workflow.md",
                        "default-sample-assets.md",
                        "resource-requirements-index.md",
                        "official-sdk-download-resources.md",
                    ],
                }
            )
        unit_ids = {
            unit_id
            for module_id in entry.get("module_ids", [])
            for unit_id in modules.get(module_id, {}).get("simple_code_ids", [])
        }
        if not entry.get("module_ids"):
            for blueprint_id in entry.get("blueprint_ids", []):
                unit_ids.update(blueprints.get(blueprint_id, {}).get("simple_code_ids", []))
        entry["simple_code_ids"] = sorted(unit_ids)
    write_json(lookup_path, lookup)

def main():
    args = parse_args()
    demo_root = args.demo_root.resolve()
    if not demo_root.is_dir():
        raise SystemExit(f"Missing demo root: {demo_root}")
    methods = run_ast_extractor(demo_root)
    if args.max_methods:
        methods = methods[: args.max_methods]
    references_dir = skill_dir() / "references"
    api_classes, direct_members = parse_markdown_api_inventory(references_dir)
    class_priorities = parse_priorities(
        references_dir / "demo-api-priority-map.md",
        "## API Class Priority Map",
        PRIORITY_CLASS_ROW_RE,
    )
    member_priorities = {}
    for section in (
        "## Observed Method Priority Map",
        "## Direct Member/Static Token Priority Map",
        "## Constant/Type Priority Map",
    ):
        member_priorities.update(
            parse_priorities(
                references_dir / "demo-api-priority-map.md",
                section,
                MEMBER_PRIORITY_ROW_RE,
            )
        )
    feature_priorities = parse_priorities(
        references_dir / "demo-feature-priority-map.md",
        "## Feature Module Priority Map",
        FEATURE_PRIORITY_ROW_RE,
    )
    registry = normalize_registry(load_json(references_dir / "sdk-module-registry.json"))
    simple_registry = build_simple_code_registry(registry)
    feature_map = build_feature_map(registry, simple_registry, feature_priorities)
    if args.sdk_signatures:
        sdk_signatures = load_json(args.sdk_signatures.resolve())
        if int(sdk_signatures.get("version", 0)) < 2:
            raise SystemExit("--sdk-signatures must use extractor schema version 2 or newer")
    elif args.sdk_jar:
        sdk_signatures = extract_signatures(args.sdk_jar, args.jdk_home)
    else:
        sdk_signatures = {
            "classes": [],
            "members": [],
            "class_count": 0,
            "member_count": 0,
            "errors": [],
        }
    official_doc_index = build_official_doc_index(references_dir, sdk_signatures)
    api_map = build_api_map(
        api_classes,
        direct_members,
        compact_ast(methods),
        sdk_signatures,
        simple_registry,
        class_priorities,
        member_priorities,
        {module["id"] for module in registry.get("modules", [])},
        official_doc_index,
    )
    api_map = annotate_api_map(api_map, registry)
    p3_scope_path = references_dir / "p3-api-processing-scope.json"
    if not p3_scope_path.is_file():
        raise SystemExit(
            "Missing frozen Stage 9 scope: references/p3-api-processing-scope.json"
        )
    p3_processing = build_p3_processing_report(
        api_map,
        load_json(p3_scope_path),
    )
    registry = finish_registry_contracts(registry, simple_registry)
    result = {
        "source_kind": "external-demo-build-time-only",
        "java_method_count": len(methods),
        "observed_call_count": sum(len(method.get("invocations", [])) for method in methods),
        "observed_api_method_count": api_map["observed_method_count"],
        "api_type_count": api_map["type_count"],
        "api_member_count": api_map["member_count"],
        "sdk_signature_class_count": sdk_signatures.get("class_count", 0),
        "sdk_signature_member_count": sdk_signatures.get("member_count", 0),
        "simple_code_unit_count": len(simple_registry["units"]),
        "feature_count": feature_map["feature_count"],
        "p3_processing_target_count": p3_processing["target_count"],
        "p3_processing_upgraded_count": p3_processing["upgraded_count"],
        "p3_processing_retained_evidence_count": p3_processing["retained_evidence_count"],
        "sdk_jar_validated": bool(args.sdk_jar and args.sdk_jar.is_file()),
        "methods": methods,
    }
    if args.output:
        write_json(args.output, result)
    if args.write_references:
        write_json(references_dir / "simple-code-registry.json", simple_registry)
        write_json(references_dir / "sdk-signature-map.json", sdk_signatures)
        write_json(references_dir / "demo-api-simple-code-map.json", api_map)
        write_json(references_dir / "p3-api-processing.json", p3_processing)
        write_json(references_dir / "demo-feature-simple-code-map.json", feature_map)
        write_json(references_dir / "sdk-module-registry.json", registry)
        update_lookup_index(references_dir, registry)
        write_coverage_artifacts(references_dir.parent)
    print(json.dumps({key: value for key, value in result.items() if key != "methods"}, indent=2))

if __name__ == "__main__":
    main()
