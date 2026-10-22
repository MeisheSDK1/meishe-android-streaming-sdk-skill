# Capability Catalog

Use this reference when the user is new to Meishe Android Streaming SDK, asks what the SDK/skill can do, asks for examples of possible apps/features, or describes a vague product goal before naming exact APIs.

This catalog is a discovery layer, not the implementation source of truth. After selecting capabilities here, route to `capability-map.md`, `demo-feature-priority-map.md`, `demo-api-priority-map.md`, `demo-api-dependency-graph.md`, `demo-feature-dependency-graph.md`, `demo-api-constraint-map.md`, official docs, and simple snippets.
For implementation requests, first use `skill-lookup-index.json` or `scripts/search_skill_index.py` to route the request, then use `resource-requirements-index.md` to list the feature-specific resources the customer must provide.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Relationship Between SDK And Skill](#relationship-between-sdk-and-skill)
- [SDK Capability Catalog](#sdk-capability-catalog)
- [Skill Capability Catalog](#skill-capability-catalog)
- [What Skill Adds Beyond The SDK](#what-skill-adds-beyond-the-sdk)
- [First-Time User Prompt Map](#first-time-user-prompt-map)
- [Capability Discovery Flow](#capability-discovery-flow)
- [Coverage And Boundary Snapshot](#coverage-and-boundary-snapshot)
<!-- END GENERATED CONTENTS -->

## Relationship Between SDK And Skill

| Surface | Meaning | Use this answer |
| --- | --- | --- |
| SDK capability | What Meishe Android Streaming SDK can do at API/runtime level. | "The SDK provides the media engine APIs: capture, timeline editing, effects, assets, preview, and export." |
| Skill capability | What this skill can do on top of the SDK. | "The skill can explain, plan, and generate Android project code that uses those SDK APIs with demo-proven call order, constraints, and snippets." |
| Skill-supervised capability | Things not provided by SDK directly but enabled by the skill. | "The skill can choose dependency subgraphs, generate controllers/managers, map vague feature requests to APIs, and identify required SDK artifacts/assets." |
| Boundary | What neither the SDK docs nor this skill can fully guarantee alone. | "Runtime success still depends on proprietary SDK binaries, license, native libraries, model/assets, device permissions, Gradle compatibility, and device QA." |

## SDK Capability Catalog

| Capability | What users usually mean | Main SDK/API families | Implementation refs |
| --- | --- | --- | --- |
| SDK setup and lifecycle | Initialize SDK, load license, structure Android project, avoid repeated context init. | `NvsStreamingContext`, `NvsEffectSdkContext`, license/assets/native libs | `official-core.md`, `android-integration.md`, `demo-api-dependency-graph.md`, `demo-simple-snippets-core-lifecycle.md` |
| Media inspection | Read video/audio metadata, duration, size, rotation, stream information. | `NvsAVFileInfo`, `NvsVideoStreamInfo`, `NvsSize`, `NvsRational` | `official-core.md`, `demo-simple-snippets-audio-media.md`, `demo-api-constraint-map.md` |
| Timeline creation | Create timelines with video/audio resolution, frame rate, and canvas settings. | `NvsTimeline`, `NvsVideoResolution`, `NvsAudioResolution`, `NvsRational` | `official-editing-export.md`, `demo-api-dependency-graph.md`, `demo-simple-snippets-timeline-editing.md` |
| Complete short-video editor workflow | Pick media, choose ratio, build timeline, bind `NvsLiveWindow`, edit with subtitles/stickers/filters/audio/beauty modules, then export. | `NvsStreamingContext`, `NvsTimeline`, `NvsLiveWindow`, `NvsAssetPackageManager`, captions/stickers/audio/FX APIs | `demo-validated-editor-architecture.md`, `demo-feature-dependency-graph.md`, `demo-api-dependency-graph.md` |
| Tracks and clips | Add video/audio tracks, insert media, trim, split, reorder, adjust clip ranges. | `NvsVideoTrack`, `NvsAudioTrack`, `NvsVideoClip`, `NvsAudioClip` | `demo-simple-snippets-timeline-editing.md`, `demo-api-constraint-map.md` |
| Preview and playback | Connect timeline to preview view, seek, play ranges, update UI from callbacks. | `NvsLiveWindow`, `NvsLiveWindowExt`, `NvsStreamingContext` playback/seek APIs | `official-editing-export.md`, `demo-api-dependency-graph.md`, `demo-simple-snippets-preview-export.md` |
| Camera capture and recording | Start camera preview, switch device, focus/flash, capture effects, record video. | `NvsStreamingContext` capture APIs, `NvsCaptureVideoFx`, capture callbacks | `official-editing-export.md`, `demo-simple-snippets-capture-recording.md`, `demo-api-constraint-map.md` |
| Compile and export | Export timeline to video, handle progress/completion/error/cancel callbacks. | `NvsStreamingContext.compileTimeline`, compile callbacks/constants | `official-editing-export.md`, `demo-api-dependency-graph.md`, `demo-simple-snippets-preview-export.md` |
| Asset packages | Install/query/update filters, transitions, captions, stickers, AR, templates. | `NvsAssetPackageManager`, package type/status/error constants | `official-core.md`, `demo-sdk-constants-map.md`, `demo-simple-snippets-assets-packages.md` |
| Built-in and packaged effects | Add filters, color adjust, clip/timeline/capture FX, intensity, masks, watermarks. | `NvsVideoFx`, `NvsTimelineVideoFx`, `NvsCaptureVideoFx`, `NvsFx` | `official-fx-and-errors.md`, `demo-simple-snippets-effects-transforms.md` |
| Typed effect parameters | Set float/string/bool/int/color parameters and effect-specific keys. | `setFloatVal`, `setStringVal`, `setBooleanVal`, `setIntVal`, `setColorVal`, `NvsExpressionParam` | `demo-sdk-constants-map.md`, `demo-api-constraint-map.md` |
| Animation and keyframes | Animate transforms, effect values, caption/sticker movement, scale, rotation. | keyframe APIs on FX/caption/sticker objects | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-captions-stickers.md` |
| Captions and text | Add/edit timeline captions, compound captions, text styles, spans, translation, scale. | `NvsTimelineCaption`, `NvsTimelineCompoundCaption`, `NvsCaption`, `NvsCaptionSpan` | `official-editing-export.md`, `demo-simple-snippets-captions-stickers.md` |
| Stickers | Add animated/custom stickers, packaged stickers, position/scale/rotate/keyframe. | `NvsTimelineAnimatedSticker`, `NvsAnimatedSticker`, `NvsClipAnimatedSticker` | `demo-simple-snippets-captions-stickers.md`, `demo-simple-snippets-rare-structural.md` |
| Audio and music | Add music, voiceover, audio clips/effects, volume gain, lyric timing. | `NvsAudioTrack`, `NvsAudioClip`, `NvsAudioFx`, media info APIs | `official-editing-export.md`, `demo-simple-snippets-audio-media.md` |
| Beauty, makeup, AR | Apply beauty, face shape, makeup, AR scene props, face/hand/eye model features. | `NvsEffectSdkContext`, `NvsARSceneManipulate`, `NvsCaptureVideoFx`, `NvsFx` | `official-effects-ar-template.md`, `demo-simple-snippets-ar-makeup-segmentation.md` |
| Segmentation/keying/masks | Human/background segmentation, mask generator, master keyer, virtual live features. | Effect SDK context/render/core APIs, mask/segmentation objects | `official-effects-ar-template.md`, `demo-simple-snippets-ar-makeup-segmentation.md` |
| Template, Mimo, CutSame | Standard/CutSame install `.template` packages and use template descriptor/Timeline APIs. Mimo separately extracts `info.json`, installs child packages, and composes a normal Timeline from shots, effects, captions, transitions, and music. | `NvsAssetPackageManager`, template Timeline overloads, normal Timeline/track/clip/effect/audio APIs | `official-effects-ar-template.md`, `demo-simple-snippets-template-mimo-cutsame.md`, `demo-api-call-order-map.md` |
| Media conversion and splicing | Passthrough conversion, quick splicing, format-specific conversion workflows. | `NvsMediaFileConvertor`, `NvsPassthroughConvertor` | `demo-simple-snippets-audio-media.md`, `demo-api-dependency-graph.md` |
| Timeline UI helpers | Thumbnail sequence, custom time spans, cover/frame selection, edit UI previews. | `NvsMultiThumbnailSequenceView`, frame retriever/grab APIs | `demo-simple-snippets-preview-export.md`, `demo-simple-snippets-timeline-editing.md` |
| Error handling and constants | Interpret SDK error codes, engine states, package status, compile/capture flags. | `NvsStreamingContext` constants, `NvsAssetPackageManager` constants, error docs | `official-fx-and-errors.md`, `demo-sdk-constants-map.md` |

## Skill Capability Catalog

| Skill capability | What the skill can do | Inputs it needs | Output it can produce |
| --- | --- | --- | --- |
| Explain SDK scope | Tell a new user what Meishe SDK can build and what artifacts are needed. | Vague product goal or "what can it do?" | Capability overview and next-choice menu. |
| Map natural language to SDK APIs | Convert requests like "add subtitle editor" or "beauty camera" into SDK capability groups. | User feature phrase | Capability section, priority modules, APIs, and snippet refs. |
| Generate Android project skeleton | Create a minimal Java Android app scaffold for SDK integration. | Output path, package name, app name | Gradle/Manifest/template project with SDK artifact slots. |
| Generate real editor architecture | Build or patch a product-level editor flow with feature hub, media import, ratio selection, live preview, requested child tools, external local-material hooks, and export. | Product goal, target path, package/app name, selected modules/resources | New standalone editor app or incremental editor module wired into an existing app. |
| Generate focused controllers/managers | Produce project-local SDK wrappers instead of copying demo Activity code. | Feature requirements and target project style | `MeisheSdkManager`, timeline/capture/asset/effect/export controllers. |
| Choose implementation order | Select P0/P1/P2/P3 modules and APIs before writing code. | Broad app or ambiguous feature scope | Ordered implementation plan and dependency list. |
| Extract minimum dependency subgraph | Determine required predecessors and optional modules for a custom feature. | Requested feature/API combination | API/feature subgraph with required/recommended/optional/conflict nodes. |
| Explain API call chains | Answer "what must be called before this API?" | API/class/method name | `requires`, `produces`, callbacks, state guards, teardown rules. |
| Enforce parameter/return constraints | Use observed guards, return checks, typed setters, constants, callback gates. | Exact API or feature implementation | Safer code and explanation of assumptions. |
| Compose new features | Combine capture/edit/export/effects/captions/assets/audio/templates into custom workflows. | Feature combination request | Minimal controllers and integration sequence. |
| Answer coverage questions | Say whether a feature/API is covered by docs, demo snippets, touchpoints, or needs more SDK artifacts. | Feature/API name | Readiness level and lookup path. |
| Route to simple snippets | Load the right compressed demo-derived example group instead of all snippets. | Selected capability/API | Targeted snippet ids/files for implementation. |
| Route with compact search index | Use a small local lookup index before reading large references. | User request text or API terms | Candidate reference files, snippet groups, resource keys, and optional template overlays. |
| Identify required runtime artifacts | Point out license, AAR/JAR, `.so`, model, package, and permission requirements. | Requested feature or project generation | Artifact checklist and project placement guidance. |
| Generate integration notes | Produce Gradle, Manifest, permission, ABI, asset, and lifecycle guidance. | New app or existing Android project | Patch plan or generated code structure. |
| Explain limitations | Separate SDK limits, skill inference limits, and runtime/device validation limits. | Any broad claim request | Clear boundary statement before implementation. |

## What Skill Adds Beyond The SDK

| Added layer | Why it matters |
| --- | --- |
| Natural-language intent routing | Users do not need to know exact classes like `NvsTimelineCaption` or `NvsAssetPackageManager` before asking. |
| Priority model | The skill can decide what is mandatory, common, feature-specific, or optional before generating code. |
| Dependency graph | The skill can preserve API order without forcing the full demo workflow. |
| Demo-derived simple snippets | The skill has reusable API call fragments distilled from the demo. |
| Constraint map | The skill knows common null checks, boolean result gates, callback gates, state guards, time units, and typed setters. |
| Resource requirements index | The skill can tell users what media, packages, models, fonts, SDK binaries, permissions, and output paths are needed for a requested module. |
| Project template | The skill can create a self-contained Android project skeleton that no SDK API provides by itself. |
| Coverage assessment | The skill can say whether it is using official docs, demo snippets, exhaustive touchpoints, or inference. |

## First-Time User Prompt Map

| User asks | Interpret as | First refs to load | Suggested response shape |
| --- | --- | --- | --- |
| "What can this SDK do?" | SDK capability discovery | `capability-catalog.md`, then `official-docs-index.md` | Summarize SDK groups and ask which product goal to start with. |
| "What can this skill do?" | Skill capability discovery | `capability-catalog.md`, then `standalone-workflow.md` | Explain project generation, API explanation, dependency graph, and boundaries. |
| "I want a short-video editor." | broad editor app | `capability-catalog.md`, `demo-validated-editor-architecture.md`, `demo-feature-priority-map.md`, `demo-api-dependency-graph.md` | Propose feature hub, media selection, ratio setup, livewindow editor, requested child modules, material center, export, and required SDK artifacts. |
| "I want a beauty camera." | capture + AR/beauty/makeup | `skill-lookup-index.json`, `resource-requirements-index.md`, `demo-feature-dependency-graph.md`, `demo-simple-snippets-ar-makeup-segmentation.md` | Explain capture preview, model gates, packages, and recording/export options. |
| "A face is detected, but AR scene or face mesh has no visible effect." | AR/face runtime diagnosis | `skill-lookup-index.json`, `ar-face-runtime-troubleshooting.md`, `runtime-verification.md` | Separate authorization, model, capture-frame, package/readback, callback, and physical-preview evidence before changing resources. |
| "I want subtitle editing." | captions/text workflow | `skill-lookup-index.json`, `resource-requirements-index.md`, `demo-api-dependency-graph.md`, `demo-simple-snippets-captions-stickers.md` | Explain timeline prerequisite, caption creation, style/mutation, preview refresh. |
| "I want filters/effects." | FX/asset package workflow | `skill-lookup-index.json`, `resource-requirements-index.md`, `demo-sdk-constants-map.md`, `demo-simple-snippets-effects-transforms.md` | Distinguish built-in vs packaged effects and typed parameter setters. |
| "I want templates/CutSame/Mimo." | template replacement/export | `skill-lookup-index.json`, `resource-requirements-index.md`, `demo-feature-dependency-graph.md`, `demo-api-call-order-map.md`, `demo-simple-snippets-template-mimo-cutsame.md` | Separate the standard/CutSame `.template` descriptor path from the Mimo ZIP/`info.json` composition path, then explain resources, validation, preview, and export. |
| "Can you make a full Android app?" | project generation | `skill-lookup-index.json`, `capability-catalog.md`, `standalone-workflow.md`, `resource-requirements-index.md`, `android-integration.md` | State generated project scope and external SDK artifacts needed. |
| "Does it support API X?" | API coverage check | `capability-catalog.md`, `demo-api-list.md`, `demo-feature-api-simple-coverage.md` | Answer covered/direct/composed/needs-docs with lookup evidence. |

## Capability Discovery Flow

1. If the user is unsure what to ask, summarize `SDK Capability Catalog` in product terms and offer 3-5 capability starting points.
2. If the user names a product goal, map it to one or more SDK capabilities and load priority maps.
3. If the user wants implementation, load dependency graphs to extract the minimum required API/module subgraph.
4. If exact APIs are named, load `demo-api-list.md`, `demo-api-constraint-map.md`, and official docs before snippets.
5. If the requested capability depends on runtime artifacts, load `resource-requirements-index.md` and state the required license/AAR/JAR/native/model/package/media/font files before promising a runnable build.
6. Keep the user's freedom: offer capability combinations and tradeoffs, not a fixed demo menu.

## Coverage And Boundary Snapshot

<!-- BEGIN GENERATED CAPABILITY COVERAGE -->
| Area | Current skill coverage | Boundary |
| --- | --- | --- |
| Demo features | 62 feature recipes mapped into 57 modules. | A recipe or mapping is not automatically a generated or device-verified implementation. |
| Exact API contracts | 283 SDK types, 751 exact members, and 515 Demo-observed methods. | SDK surfaces absent from both Demo and bundled official references remain out of scope. |
| API implementation | 405 compiled, 0 contract-only, and 346 evidence-only members. | Contract/evidence states must not be reported as generated implementation. |
| Low-frequency P3 APIs | 149 of the frozen 495 members now have exact compiled units; 346 retain explicit member-level reasons. | Constants, callbacks, diagnostic getters, value objects, and owned lifecycle operations are not promoted with meaningless wrapper code. |
| Simple Code | 322 semantic units: 241 compilable Java units and 81 recipes. | Historical evidence fragments prove Demo usage only. |
| Application generation | 9 blueprints with dependency-closed module plans. | Product depth varies by blueprint and resource gate. |
| Physical-device evidence | 22 runs across 8 blueprints; 8 blueprints have passed runs and 0 are partial-only. | Read the runtime matrix before making any runtime claim. |
<!-- END GENERATED CAPABILITY COVERAGE -->
