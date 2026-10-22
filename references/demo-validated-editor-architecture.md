# Demo-Validated Editor Architecture

Use this reference when a user asks for a complete short-video editor, a 0-to-1 SDK demo app, media selection followed by editing, or an editor that should behave like the official Android demo instead of exposing only preview/recording buttons.

This file is distilled from the official demo source and true-device UI traversal. It is a product/workflow correction layer over the lower-level API and feature maps: keep custom flexibility, but do not omit the editor's required front-to-back chain.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Device-Verified Official Flow](#device-verified-official-flow)
- [Required Editor Chain](#required-editor-chain)
- [Big Modules](#big-modules)
- [Editor Child Modules](#editor-child-modules)
- [Local Material Binding Rules](#local-material-binding-rules)
- [Structural Project State](#structural-project-state)
- [Timeline Ownership](#timeline-ownership)
- [Generated Editor Runtime Boundaries](#generated-editor-runtime-boundaries)
- [API Families To Load For A Real Editor](#api-families-to-load-for-a-real-editor)
- [Generation Rules](#generation-rules)
<!-- END GENERATED CONTENTS -->

## Device-Verified Official Flow

The official demo app exposes a feature hub first, then routes editor users through media import before opening the timeline editor.

| Stage | Demo evidence | Required behavior in generated apps |
| --- | --- | --- |
| Startup | `MSApplication.initMeicamSdk()` initializes `NvsStreamingContext`, optional `NvsEffectSdkContext`, `NvAssetManager`, license path, and SDK settings. `MainActivity` copies resources, checks authorization, and initializes AR/model state when needed. | Initialize SDK once at app startup. Copy or verify required SDK/sample resources before the user enters SDK features. Keep model-heavy AR/beauty init optional and guarded. |
| Feature hub | `MainActivity` shows modules such as short video, keying background, particles, templates, flip captions, URL editing, PIP, music lyrics, cover, theme shoot, sequence nesting, audio equalizer, quick splicing; bottom actions include video capture and video edit. | For a broad demo app, show product-level feature entries, not raw SDK test buttons only. |
| Media selection | `MainActivity` video-edit action launches `SelectMediaActivity` with `visitMethod=FROMMAINACTIVITYTOVISIT` and unlimited media count. | A short-video editor needs media selection/import or an equivalent project-media source before timeline creation. |
| Ratio and timeline seed | `SelectMediaActivity.selectCreateRatio(...)` probes media via `NvsStreamingContext.getAVInfoFromFile(...)`, validates resolution, creates `ClipInfo` entries, sets `TimelineData.videoResolution`, `TimelineData.clipInfoData`, and `TimelineData.makeRatio`, then opens `VideoEditActivity`. | Do not create an empty timeline and stop. Build timeline seed state from selected videos/images and chosen aspect ratio. |
| Editor shell | `VideoEditActivity` creates `mTimeline = TimelineUtil.createTimeline()`, initializes `VideoFragment`, `CompileVideoFragment`, asset info, and the bottom edit-module list. | The editor screen owns timeline state and module navigation. It must connect timeline preview to a live window and keep playback/seek callbacks active. |
| Live preview | `VideoFragment.setTimeline(mTimeline)` then `connectTimelineWithLiveWindow(...)`; it maps overlay coordinates with `NvsLiveWindow` methods and uses seek/playback callbacks to refresh UI. | Timeline mutations must be reflected in `NvsLiveWindow` via seek/refresh/reconnect logic. A real editor is timeline + live preview + controls, not timeline creation alone. |
| Edit tools | Toolbar entries include edit, filter, sticker, animation, mask, caption, compound caption, background, watermark, transition, music, voiceover, beauty, and makeup. Child activities return modified `TimelineData`; parent calls `TimelineUtil` apply/rebuild methods and refreshes preview. | Feature modules should be children of the editor shell unless they are camera-only or specialized workflows. |
| Export | `CompileVideoFragment.compileVideo()` calls compile utilities against the same `NvsTimeline` and handles finish/fail/cancel callbacks. | Export is part of the editor chain; stop playback/capture before compile and expose callbacks. |

## Required Editor Chain

For a complete short-video editor, include this chain or an equivalent custom architecture:

```text
app-root
-> sdk-runtime-init
-> first-run-resource-copy-or-check
-> asset-manager-init
-> feature-hub
-> media-selection-or-import
-> ratio-resolution-selection
-> timeline-state-store
-> timeline-create-and-build-tracks
-> livewindow-preview-binding
-> playback-seek-callbacks
-> editor-child-modules
-> apply-or-rebuild-timeline-and-refresh-preview
-> compile-export
```

If a user selects a downstream editor capability, automatically include its predecessors. Examples:

- Subtitles, stickers, filters, masks, background, watermark, music, voiceover, beauty edit, makeup edit, and transitions require the editor shell, timeline state, timeline preview binding, playback/seek refresh, and export path unless the user explicitly asks for an API-only snippet.
- Transition requires at least two timeline clips.
- PIP requires two selected media items or a generated alternate media-source picker.
- Voiceover requires microphone permission and a record-audio timeline track.
- Beauty camera requires capture preview; beauty/makeup edit requires timeline media and model/Effect SDK gates when face features are used.

## Big Modules

| Module | Priority for broad editor | Owns | Required by |
| --- | --- | --- | --- |
| App/runtime bootstrap | P0 | License path, SDK artifacts, native libs, `NvsStreamingContext`, optional `NvsEffectSdkContext`, `NvAssetManager`, permissions. | Every SDK feature. |
| Media source/import | P0 for editor | Media picker, selected count, media metadata, ratio popup, `ClipInfo`, `TimelineData.videoResolution`, `TimelineData.clipInfoData`, `TimelineData.makeRatio`. | Timeline editor, PIP, templates, cover, photo album. |
| Core editor shell | P0/P1 | `VideoEditActivity` equivalent, `NvsTimeline`, toolbar, timeline state ownership, result handling from child modules. | All timeline edit submodules. |
| Live preview/playback | P0/P1 | `VideoFragment` equivalent, `NvsLiveWindow`, playback/seek callbacks, overlay coordinate mapping. | Interactive editor, captions/stickers, masks, watermark, compile preview. |
| Timeline build/apply layer | P0/P1 | `TimelineUtil` equivalent for timeline creation, track/clip rebuild, effects, captions, audio, beauty/makeup, background, mask, transitions. | Every timeline mutation. |
| Compile/export | P0/P1 | Compile callbacks, output path, progress/failure/cancel handling. | Complete editor result. |
| Local material catalog/package install | P1 when packaged examples are requested | Bundled family list, install/upgrade, font registration, package-id result, and explicit missing-resource states. | Packaged filters, caption styles, stickers, transitions, AR, themes, and fonts. |
| Capture/beauty camera | P1 when camera is requested | Capture preview, recording, camera effects, beauty/makeup/AR packages and model gates. | Camera apps and record-then-edit flows. |
| Specialized workflows | P2/P3 | PIP, templates/CutSame/Mimo, quick splicing, URL edit, music lyrics, cover, album, particles, keying, sequence nesting. | Only selected product features. |

## Editor Child Modules

| Child module | Parent | Can stand alone? | Removal effect | Asset/resource binding |
| --- | --- | --- | --- | --- |
| Clip edit | Core editor | No for editor UX; yes as a focused clip tool if a timeline exists. | Removes trim/split/speed/volume/color/crop/photo motion controls. | Media source, preview, timeline rebuild. |
| Filter | Core editor or capture | Only as API demo; normal use is editor/camera child. | No filter UI or packaged video FX. | Built-in FX need core only; packaged filters need asset packages/material center. |
| Sticker | Core editor | Only as API demo. | No overlay stickers. | Sticker packages/licenses, package id, preview coordinate mapping. |
| Caption | Core editor | Only as API demo. | No text/subtitle editor. | Caption style/font packages for styled captions; timeline time ranges. |
| Compound caption | Core editor | Only as API demo. | No packaged compound text templates. | Compound caption packages/licenses. |
| Transition | Core editor | No. | No inter-clip transitions. | Requires at least two clips; transition packages optional. |
| Music | Core editor | Possible as audio-only tool, but editor binding is normal. | No soundtrack. | Audio files, audio track, timeline duration guards. |
| Voiceover | Core editor | Possible as recorder, but editor binding is normal. | No narration recording. | `RECORD_AUDIO`, app-private output, record audio track. |
| Animation | Core editor | Only as effect API demo. | No clip animation presets/keyframes. | Animation metadata/packages if packaged. |
| Mask | Core editor | No for user-facing mask edit. | No region/mask UI. | Preview coordinate mapping, mask parameter keys. |
| Background | Core editor | Depends on selected background mode. | No canvas/background replacement controls. | Background images/videos or color/blur modes. |
| Watermark | Core editor/export | Possible as export-only helper. | No logo/watermark overlay. | Watermark image/storyboard resources if used. |
| Beauty edit | Core editor | No; camera beauty is a separate path. | No post-edit beauty. | Effect SDK/model gates and beauty parameters. |
| Makeup edit | Core editor | No; capture makeup is separate path. | No post-edit makeup. | Makeup packages/licenses, model gates. |
| Material catalog | Local service used by modules | Yes as a bundled browsing/install screen, but should be invoked from modules. | Only bundled or user-provided local resources are available. | No network permission; local package installer and font registration. |

## Local Material Binding Rules

Treat the local material catalog as a package-install service plus module-specific entry points, not as an unrelated homepage button.

| Module request | Asset type/package type to resolve | Apply after install |
| --- | --- | --- |
| Filters/effects | `NvAsset.ASSET_FILTER` -> `ASSET_PACKAGE_TYPE_VIDEOFX` | Add packaged FX to clip/timeline/capture with the returned package id. |
| Transitions | transition asset -> `ASSET_PACKAGE_TYPE_VIDEOTRANSITION` | Apply between clips; guard clip count >= 2. |
| Caption styles | `ASSET_CAPTION_STYLE` -> `ASSET_PACKAGE_TYPE_CAPTIONSTYLE` | Use style package id when creating/updating captions. |
| Caption context/renderer/animation | `ASSET_PACKAGE_TYPE_CAPTION_CONTEXT` / `CAPTION_RENDERER` / `CAPTION_ANIMATION` | Create the caption with `addModularCaption`; apply renderer -> context -> animation with the animation period set first. `addCaption` captions reject modular applies. See `references/editor-runtime-pitfalls.md`. |
| Animated stickers | `ASSET_ANIMATED_STICKER` -> `ASSET_PACKAGE_TYPE_ANIMATEDSTICKER` | Add/update timeline animated stickers. |
| Compound captions | `ASSET_COMPOUND_CAPTION` -> compound-caption package type | Add/update compound captions. |
| Capture scene/AR | capture scene or AR scene assets -> capture/AR package types | Apply to capture preview after package/model checks. |
| Makeup | makeup/face/warp assets -> makeup/face-mesh/warp package types | Apply only after Effect SDK/model gates pass. |
| Templates | theme/Mimo/CutSame packages | Parse template, validate footage, then create/export timeline. |

Large model directories such as `facemode`, AR face data, segmentation models, and other AI packs are not bundled. Resolve selected files from `samples/android/SdkDemo/app/src/main/assets/facemode` in the official Android LTS face package, expose placement hooks such as `--human-models-dir`, and fall back clearly when missing.

## Structural Project State

Generated editors must distinguish persistent project structure from live SDK objects. `NvsTimeline`, tracks, clips, and `NvsLiveWindow` are rebuilt after process death; do not attempt to persist their Java object references.

The minimum structural project record contains:

- Timeline width and height or the selected aspect-ratio preset.
- Ordered app-owned media paths. Provider `content://` URIs must be copied before they become long-lived project inputs.
- Per-clip source `trimIn` and `trimOut`, playback speed, pitch-preservation choice, media type, and image-motion state.
- A version field so descriptor schemas can migrate old projects safely.

Restore order is `load state -> create Timeline -> create/get video track -> append ordered clips -> restore source trim/speed/image state -> connect LiveWindow -> seek/refresh`. Missing app-owned files are skipped and reported; an empty restore is a failure, not a valid editor project.

Timeline positions are not valid source trim positions for every clip. Convert a Timeline playhead to source media time before calling trim APIs:

```text
sourceTrimOut = clip.trimIn + (timelinePosition - clip.inPoint) * clip.speed
```

Reject positions outside `(trimIn, trimOut)`, stop the engine before structural mutation, verify the SDK return/resulting trim value, then refresh the connected LiveWindow.

The generated short-video editor uses a version-3 project root. It stores canvas width/height, video FPS, audio sample rate/channel count, ordered clips with stable `clip-*` identifiers, source trim/speed/image state, editor-owned filters and parameter maps, transitions linked by stable source/target ids, captions, compound captions, stickers, audio tracks, backgrounds, watermarks, and a namespaced `extensions` object. New module state must use `MeisheProjectExtensionCodec`; it must not add unversioned top-level fields or serialize SDK objects.

Projects are written atomically to `filesDir/meishe-projects/<projectId>/project.json`. `MeisheEditorProjectRepository` first reads that file, then migrates a legacy version-2/SharedPreferences project when needed. Migration preserves known descriptor arrays and unknown extension namespaces, assigns stable ids to clips and descriptors, writes the v3 file, and keeps the legacy record only as migration input.

Undo/redo captures the complete serialized v3 project after a successful mutation and keeps at most 50 snapshots in memory. Split creates a new stable clip id and remaps affected descriptors; delete removes references to the deleted id; move retains the same ids while recomputing adjacency-dependent transitions. The latest project is persisted for process restoration, but undo/redo history is deliberately not persisted or reconstructed after process death.

This is not arbitrary SDK object serialization. `NvsTimeline`, tracks, clips, `NvsLiveWindow`, callbacks, and other live SDK objects are rebuilt or supplied by the host. Missing app-owned files/packages are reported and skipped without invalidating the remaining project. Third-party host objects are outside the generated editor's ownership unless the host explicitly grants mutation rights.

## Timeline Ownership

`MeisheEditorHostContract` makes ownership explicit when the editor is embedded in another app:

| Ownership | Timeline source | Structural mutation | Feature descriptor rebuild | Teardown |
| --- | --- | --- | --- | --- |
| `EDITOR_OWNED` | `MeisheEditorSessionController` creates the Timeline. | Allowed through editor command controllers. | Allowed for editor-owned descriptors. | Stop callbacks/engine and call `removeTimeline`. |
| `HOST_OWNED` | Host returns an existing Timeline from `acquireTimeline`. | Denied by default; host must explicitly return `true` from `allowStructuralMutations`. | Denied by default; host must explicitly return `true` from `allowEditorFeatureRebuild`. | Never call `removeTimeline`; notify the host through `onEditorClosed`. |

The safe default for a host-owned Timeline is read/preview/export coordination only. Split/delete/move, clear-and-reapply, undo/redo, filters, captions, stickers, transitions, music, and voiceover all check the matching permission before mutation. This preserves host-created clips, captions, effects, audio, and other non-skill objects when the host does not opt in.

## Generated Editor Runtime Boundaries

The generated `short-video-editor` blueprint uses a thin Activity and explicit collaborators. This is the default standalone architecture; it preserves the existing Intent entry points while preventing Android screen code from becoming the SDK object owner.

| Class | Responsibility | Must not own |
| --- | --- | --- |
| `MeisheEditorActivity` | Android lifecycle, permission and Activity Result forwarding, Intent construction, navigation delegation. | Direct `NvsTimeline`, Track, Clip, Caption, Sticker, Audio, playback, seek, mutation, or compile calls. |
| `MeisheEditorCoordinator` | Create and connect collaborators; route UI commands, material results, permission results, pause/save/destroy events. | Low-level SDK mutation details or persistent object serialization. |
| `MeisheEditorSessionController` | Acquire editor-owned or host-owned `NvsTimeline`, acquire/bind `NvsLiveWindow`, own playback/seek/engine callbacks, preview refresh, export callbacks, ownership guards, and teardown. | View lookup, dialogs, feature-specific descriptor mutation, or removal of host-owned Timelines. |
| `MeisheEditorCommandController` | Select, split, trim, delete, move, undo, redo, persist after successful structural mutations, and refresh preview. | Activity lifecycle or overlay/package installation. |
| `MeisheEditorOverlayController` | Filters, captions, stickers, transitions, music, bundled/downloaded package application, and descriptor updates. | Timeline creation/destruction or Activity Result dispatch. |
| `MeisheVoiceoverController` | Microphone permission trigger, `MediaRecorder` lifecycle, app-private recording output, and voiceover insertion. | General editor navigation or unrelated audio edits. |
| `MeisheEditorProjectController` | Version-3 project state, stable-id synchronization/remapping, editor descriptors, atomic persistence, 50-snapshot history, migration, and restore/reapply coordination. | Live SDK object serialization or bypassing session ownership guards. |
| `MeisheEditorProjectRepository` | Resolve project paths, atomic file persistence, latest-project lookup, and v2/SharedPreferences migration. | Timeline mutation or SDK object lifetime. |
| `MeisheEditorHostContract` | Supply host Timeline/LiveWindow ownership decisions and receive ready/save/close callbacks. | Implicit permission to mutate or release host objects. |
| `MeisheEditorUiBindings` | View lookup, listeners, caption input dialog, button state, seek/status rendering. | SDK objects or persistence. |

The Activity should remain below 300 lines and have no `com.meicam`/`Nvs*` imports. Structural mutations follow `ownership guard -> stop engine -> mutate -> stable-id remap -> persist/capture -> seek or reconnect LiveWindow`; export follows `stop engine -> compile callbacks -> terminal result`. `recipe.editor-session-orchestration` records the Android/SDK session chain, while `recipe.editor-project-v3-ownership` records v3 load/migration, stable identity, atomic save, and ownership-aware teardown.

## API Families To Load For A Real Editor

Load these API/snippet groups before implementing a broad short-video editor:

- Startup: `NvsStreamingContext.init`, `NvsStreamingContext.getInstance`, `NvsStreamingContext.setIconSize`, `NvsStreamingContext.setMaxReaderCount`, optional `NvsEffectSdkContext.init`.
- Media source: `NvsStreamingContext.getAVInfoFromFile`, `NvsAVFileInfo`, `NvsVideoResolution`, `NvsRational`.
- Timeline: `NvsStreamingContext.createTimeline`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsAudioTrack`, `NvsAudioClip`.
- Preview: `NvsStreamingContext.connectTimelineWithLiveWindow`, `playbackTimeline`, `seekTimeline`, playback/engine callbacks, `NvsLiveWindow` coordinate mapping.
- Mutation: `appendBuiltinFx`, `appendPackagedFx`, `NvsFx` typed setters, caption/sticker creation and mutation APIs, transition APIs, timeline audio APIs.
- Packages: `NvsAssetPackageManager.installAssetPackage`, status/version/query constants, install callbacks and already-installed success handling.
- Export: `compileTimeline` or demo compile utility wrappers plus progress/completion/failure/cancel callbacks.

## Generation Rules

1. When a user asks for "短视频编辑器", "video editor", "editor with captions/stickers/filters", or "0-to-1 SDK demo", generate the real editor chain above. Do not answer with only preview/recording buttons.
2. For an existing-project integration, map the user's current navigation to the chain: add missing source/import, timeline state, live preview, child module, or export nodes without forcing the demo UI.
3. For a new standalone project, create a feature hub, media picker/import screen, ratio selector, editor screen with `NvsLiveWindow`, toolbar child modules, material center hooks, and export flow.
4. Keep modules replaceable. A generated `MeisheTimelineController`, `MeisheEditorActivity`, or project-local ViewModel can satisfy demo nodes if it obeys the same SDK object ownership and callback rules.
5. Load `resource-requirements-index.md` and `official-sdk-download-resources.md` before implementation and list required resource rows plus official-package-relative paths. Tell the user that the skill stores no materials, use an authorized external lightweight bundle for first-run effects when available, select required large models from the official face package, and direct material acquisition to Meishe business.
6. Bind the copied external local catalog to each requested packaged feature. Do not add a material endpoint or request layer; unavailable packages remain customer inputs, and acquisition questions go to Meishe business.
7. After every child-module mutation, stop playback if needed, apply or rebuild the affected timeline part, seek/refresh the live window, and keep `TimelineData` or equivalent project state synchronized.
8. For caption context/renderer/animation materials, create the caption with `addModularCaption` and apply renderer -> context -> animation (set the animation period first); `addCaption` is only for plain/style captions. Expose X/Y movement (`setCaptionTranslation` / `translateAnimatedSticker`), persist translationX/Y, and keep applied-material property dialogs scrollable with a pinned bottom action bar. See `references/editor-runtime-pitfalls.md`.
