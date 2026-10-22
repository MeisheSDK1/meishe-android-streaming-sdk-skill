# Demo API Dependency Graph

This reference turns demo-proven call order and constraints into a composable API graph. Use it when a user asks for API call chains, safe custom composition, or the minimum dependency subgraph for a new feature.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Graph Semantics](#graph-semantics)
- [API Node Map](#api-node-map)
- [Dependency Edges](#dependency-edges)
- [Minimal Subgraph Recipes](#minimal-subgraph-recipes)
- [Generation Rules](#generation-rules)
<!-- END GENERATED CONTENTS -->

## Graph Semantics

- `hard requires`: the target should not be called until the source node is satisfied.
- `produces`: the source returns or owns the SDK object consumed by the target.
- `enables`: the target is optional unless the requested feature needs that capability.
- `recommended guard`: not always mandatory, but needed for robust media validation or UI behavior.
- `stop-first conflict`: call `NvsStreamingContext.stop()` or the specific stop API before crossing the edge.
- `callback-gated`: wait for callback/status/boolean result before downstream use.

Do not treat this as a single fixed workflow. A generated app should extract the smallest subgraph that satisfies the user request. Equivalent user-defined controllers may satisfy any node if they produce the same SDK object/state and obey the same guards.

## API Node Map

| Node | Priority | Requires | Produces | Enables | Guards | Conflicts / teardown |
| --- | --- | --- | --- | --- | --- | --- |
| sdk-artifacts | P0 | license/AAR/JAR/native libs in generated Android project | runtime-ready SDK files | `NvsStreamingContext.init` | Project files exist; no demo secrets. | Missing artifacts block build/runtime. |
| streaming-context-init | P0 | `sdk-artifacts`; Android app startup | initialized `NvsStreamingContext` singleton | `getInstance`, timeline, capture, assets, compile | Call once per process; official docs win on init args. | Do not recreate per Activity; release/stop on teardown. |
| streaming-context-instance | P0 | `streaming-context-init` | `NvsStreamingContext` handle | asset manager, AV info, timeline, preview, capture, compile | Null-check if app lifecycle can race. | Invalid before init. |
| effect-sdk-context | P2 | `streaming-context-init`; requested Effect SDK/render/camera effect feature | `NvsEffectSdkContext` handle | Effect SDK render/core, beauty, makeup, AR helper flows | Initialize only when needed. | Do not initialize all human models by default. |
| human-detection-models | P2 | `effect-sdk-context` or AR-capable streaming context; model assets | human/face/segmentation capability enabled | beauty, makeup, segmentation, face mesh, warp | `hasARModule`; model file availability. | Feature should degrade or fail clearly when model missing. |
| asset-package-manager | P1 | `streaming-context-instance` | `NvsAssetPackageManager` | status/install/update; packaged FX/caption/sticker/template use | Null-check manager and constants. | Package ids are not valid until status/install succeeds. |
| asset-package-status-install | P1 | `asset-package-manager`; package path/type | installed package id or status/error result | packaged FX, filters, captions, stickers, templates | Use correct `ASSET_PACKAGE_TYPE_*`; inspect error codes/callbacks. | Do not pass uninstalled ids downstream. |
| media-info-probe | P1 | `streaming-context-instance`; media path/uri | `NvsAVFileInfo`, dimensions, duration, rotation | timeline insertion, template footage validation, resolution choice | Null-check; stream index usually `0`. | Do not assume media metadata exists. |
| media-selection-import | P0/P1 for editor | Android picker/MediaStore or custom import UI; media permission strategy; `media-info-probe` recommended | selected media paths/uris, selected count, validated media metadata | ratio/resolution choice, clip seed state, PIP/template validation | Validate missing/oversized/unsupported media; PIP needs two items. | Do not enter the full editor without media seed state unless creating an explicit empty-project editor. |
| editor-state-store | P0/P1 for editor | `media-selection-import`; ratio choice; video resolution; clip info list | `TimelineData`-style project state | timeline creation/rebuild, child edit result handling, export | Keep state synchronized after child modules mutate clips/effects/audio. | Stale state causes preview/export mismatch. |
| timeline-resolution | P0 | requested canvas size/fps/audio sample settings; optional media info | `NvsVideoResolution`, `NvsAudioResolution`, `NvsRational` | `createTimeline` | Use valid fps and dimensions; decide aspect ratio. | Wrong values break timeline/preview/export quality. |
| timeline-create | P0 | `streaming-context-instance`; `timeline-resolution` or template footage inputs | `NvsTimeline` | track creation, preview, captions/stickers, compile | Null-check returned timeline. | Remove/recreate deliberately; do not leak old timelines. |
| track-create | P1 | `timeline-create` | `NvsVideoTrack`; optional `NvsAudioTrack` | clip insertion, audio graph, volume/track operations | Null-check track returns. | Structural mutation should happen while playback/export is stopped. |
| clip-insert | P1 | `track-create`; media path; trim/time range | `NvsVideoClip`/`NvsAudioClip` | clip FX, trim/split, transform, audio gain | Microsecond ranges; null-check returned clip. | Do not use clip APIs before clip object exists. |
| timeline-connect-preview | P1 | `timeline-create`; `NvsLiveWindow` or `NvsLiveWindowExt` | preview binding | seek/playback/live UI | Use matching connect API for window type. | Reconnect if timeline/window changes. |
| playback-seek | P1 | `timeline-connect-preview`; callbacks recommended | preview state, current position, UI refresh | interactive editing, captions/stickers/effects preview | State/time guards; use callbacks for UI. | Call `stop()` before structural mutation/compile. |
| editor-livewindow-shell | P0/P1 for editor | `editor-state-store`; `timeline-create`; `timeline-connect-preview`; `playback-seek` | interactive editor screen with synchronized preview | editor toolbar modules, overlay coordinate editing, export | `NvsLiveWindow` coordinate mapping for captions/stickers/watermark/masks; callback-driven UI. | Do not treat timeline creation alone as an editor. |
| capture-preview | P1 | `streaming-context-instance`; camera permission; device/capability selection | capture preview state | capture FX, recording, camera UI | Check `getStreamingEngineState`; boolean-return check. | Capture conflicts with compile and some playback flows. |
| capture-recording | P1 | `capture-preview`; output path; recording callback/config | recorded media file | edit/export recorded media | Gate by `STREAMING_ENGINE_STATE_CAPTURERECORDING`. | Do not start if already recording; call `stopRecording`. |
| capture-fx | P2 | `capture-preview`; built-in name or installed package id | `NvsCaptureVideoFx`/capture effect handle | beauty/filter/AR capture preview | Null-check FX; package ids require asset install. | Typed parameters only after FX exists. |
| clip-timeline-fx | P2 | `clip-insert` or `timeline-create`; built-in name or installed package id | `NvsVideoFx`/`NvsTimelineVideoFx`/`NvsFx` | filters, transforms, masks, storyboard, keyframes | Choose built-in vs packaged API; null-check. | Stop preview for destructive timeline mutations when needed. |
| fx-typed-params | P2 | `capture-fx` or `clip-timeline-fx`; parameter key/type | configured effect parameters | beauty/makeup/filter/adjust/mask behavior | Use matching setter: float/string/bool/int/color. | Do not coerce all params to strings. |
| captions-stickers-create | P2 | `timeline-create`; inPoint/duration; optional installed style/package id | `NvsTimelineCaption`, `NvsTimelineCompoundCaption`, `NvsTimelineAnimatedSticker` | caption/sticker style/mutation/keyframes | Microseconds; null-check returned object. | Package style id must be installed first. |
| caption-sticker-mutate | P2 | `captions-stickers-create`; selected caption/sticker object | styled/transformed caption or sticker | text/color/position/scale/rotation/span/keyframe UI | Use typed caption/span APIs; seek preview after mutation. | Do not mutate stale/deleted objects. |
| audio-track-clip | P2 | `track-create`; audio media path/time range | `NvsAudioTrack`, `NvsAudioClip`, `NvsAudioFx` | music, voiceover, lyrics, volume | Microseconds; left/right gain values. | Stop compile/playback when mutating shared timeline. |
| editor-child-apply-refresh | P1 for editor | `editor-livewindow-shell`; selected mutation node such as `clip-timeline-fx`, `captions-stickers-create`, `audio-track-clip`, beauty/makeup/background/mask/transition | synchronized timeline state and preview frame | continued editing and compile/export | Stop playback where needed; rebuild/apply affected `TimelineData` sections; seek/refresh live window. | Do not leave child-module state unapplied after returning to editor. |
| thumbnail-frame-grab | P2 | `timeline-create` or media path; optional preview binding | thumbnail sequence/frame bitmap | timeline UI, cover, frame selection | Use size/range guards. | Avoid heavy work on UI thread in generated apps. |
| media-convertor | P2 | `streaming-context-instance`; input/output paths; callbacks | converted media or passthrough result | quick splicing, format conversion, template prep | Callback/result handling required. | Do not assume synchronous completion. |
| template-descriptor-query | P1 | `asset-package-status-install` with template package id | nested footage, normal caption, and compound caption descriptors | replace-id mapping, reverse requirements, caption replacement | Flatten nested descriptors; preserve stable replace-id order. | Do not infer required slots from UI order alone. |
| template-footage-map | P1 | `template-descriptor-query`; readable replacement media | validated `templateFootageInfo` list | one selected template timeline branch | Match `footageId`; set `reverseFilePath` only when required. | Missing footage or reverse output blocks timeline creation. |
| template-reverse-media | P1 when requested by descriptor | `template-descriptor-query`; `media-convertor`; source duration | reverse media path for each `needReverse` footage id | `template-footage-map` | Register callback before conversion; wait for success and verify output file. | Conditional node; omit it when no descriptor requires reverse media. |
| template-timeline-branch | P1 | `template-footage-map`; template package id | exactly one standard, CutSame, or Mimo `NvsTimeline` | nested caption replacement, preview, export | Pick the overload from the selected module; Mimo also requires FPS/audio resolution. | The three creation overloads are alternatives, not sequential calls. |
| template-caption-replace | P1 | `template-timeline-branch`; caption descriptors | updated normal/compound captions, including internal timelines | preview refresh and export | Match `TEMPLATE_KEY_REPLACE_ID`; stop active playback before mutation. | Skip cleanly when the template has no replaceable captions. |
| compile-export | P0 | `timeline-create`; output path; compile callbacks; stopped playback/capture | exported video or compile error/cancel callback | final render/share/save workflow | Boolean start check plus callbacks; time range in microseconds. | Do not compile while capture/playback/structural mutation is active. |
| teardown | P0 | Activity/Fragment destroy or project close | stopped engine, cleared callbacks, optional removed timeline | safe lifecycle cleanup | Stop playback/capture/compile; remove callbacks if owned. | Do not release shared singleton still used elsewhere. |

## Dependency Edges

| From | To | Relation |
| --- | --- | --- |
| sdk-artifacts | streaming-context-init | hard requires |
| streaming-context-init | streaming-context-instance | produces |
| streaming-context-instance | asset-package-manager | enables |
| streaming-context-instance | media-info-probe | enables |
| media-info-probe | media-selection-import | recommended guard |
| media-selection-import | editor-state-store | produces media seed |
| editor-state-store | timeline-resolution | hard requires for editor |
| editor-state-store | timeline-create | hard requires for editor |
| streaming-context-instance | timeline-create | hard requires |
| timeline-resolution | timeline-create | hard requires |
| timeline-create | track-create | produces parent |
| track-create | clip-insert | produces parent |
| timeline-create | timeline-connect-preview | hard requires |
| timeline-connect-preview | playback-seek | enables |
| playback-seek | editor-livewindow-shell | hard requires for editor |
| editor-livewindow-shell | editor-child-apply-refresh | hard requires for editor modules |
| editor-child-apply-refresh | compile-export | recommended guard |
| playback-seek | clip-insert | stop-first conflict |
| playback-seek | track-create | stop-first conflict |
| playback-seek | compile-export | stop-first conflict |
| timeline-create | captions-stickers-create | hard requires |
| asset-package-status-install | captions-stickers-create | required for packaged styles |
| captions-stickers-create | caption-sticker-mutate | produces object |
| clip-insert | clip-timeline-fx | hard requires for clip FX |
| timeline-create | clip-timeline-fx | hard requires for timeline FX |
| asset-package-status-install | clip-timeline-fx | required for packaged FX |
| clip-timeline-fx | fx-typed-params | produces object |
| capture-preview | capture-fx | hard requires for capture FX |
| asset-package-status-install | capture-fx | required for packaged capture FX |
| capture-fx | fx-typed-params | produces object |
| timeline-create | audio-track-clip | hard requires |
| media-info-probe | clip-insert | recommended guard |
| media-info-probe | timeline-create | recommended/required for template footage validation |
| asset-package-status-install | template-descriptor-query | hard requires |
| template-descriptor-query | template-reverse-media | conditional when `needReverse=true` |
| template-descriptor-query | template-footage-map | hard requires |
| template-reverse-media | template-footage-map | conditional hard requires |
| template-footage-map | template-timeline-branch | hard requires |
| template-timeline-branch | template-caption-replace | enables |
| template-caption-replace | timeline-connect-preview | recommended refresh |
| template-caption-replace | compile-export | required after requested replacements |
| timeline-create | thumbnail-frame-grab | enables |
| streaming-context-instance | media-convertor | hard requires |
| timeline-create | compile-export | hard requires |
| capture-preview | compile-export | stop-first conflict |
| capture-recording | compile-export | stop/wait conflict |
| compile-export | teardown | cancel/stop before release |
| playback-seek | teardown | stop before release |
| capture-preview | teardown | stop before release |
| effect-sdk-context | human-detection-models | enables |
| human-detection-models | capture-fx | required for AR/makeup/segmentation |

## Minimal Subgraph Recipes

| Request shape | Load these nodes first | Then add | Avoid |
| --- | --- | --- | --- |
| basic timeline editor API shell | `sdk-artifacts -> streaming-context-init -> timeline-resolution -> timeline-create -> track-create -> clip-insert -> timeline-connect-preview -> playback-seek` | requested edit nodes such as `clip-timeline-fx`, `captions-stickers-create`, `audio-track-clip`, `compile-export` | capture nodes unless camera input is requested |
| real short-video editor app | `sdk-artifacts -> streaming-context-init -> media-info-probe -> media-selection-import -> editor-state-store -> timeline-resolution -> timeline-create -> track-create -> clip-insert -> timeline-connect-preview -> playback-seek -> editor-livewindow-shell` | requested child modules, `asset-package-status-install` for packaged assets, `editor-child-apply-refresh`, `compile-export` | raw SDK buttons without media import/live preview/editor routing |
| camera preview/recording | `sdk-artifacts -> streaming-context-init -> capture-preview` | `capture-recording`, `capture-fx`, `fx-typed-params` as requested | timeline nodes until recorded media must be edited/exported |
| asset-backed filter/effect | `streaming-context-instance -> asset-package-manager -> asset-package-status-install` | `clip-timeline-fx` or `capture-fx`, then `fx-typed-params` | using package ids before install/status success |
| caption/sticker feature | `timeline-create -> captions-stickers-create -> caption-sticker-mutate` | `asset-package-status-install` for packaged style/sticker ids; `playback-seek` for UI refresh | mutating null/stale caption or sticker objects |
| export workflow | `timeline-create -> compile-export` | compile callbacks and output-path validation | active playback/capture/recording during compile |
| AR/makeup/segmentation | `streaming-context-init -> effect-sdk-context -> human-detection-models` | `capture-preview`, `capture-fx`, `fx-typed-params`, relevant asset packages | enabling model-gated params before module/model checks |

## Generation Rules

1. Start from the requested output, walk backward through hard requirements, then add only recommended guards that affect correctness or UX.
2. Prefer P0/P1 nodes for generated project skeletons; add P2/P3 only when the feature asks for them or an exact API search lands there.
3. Treat every SDK factory/adder return as nullable unless official docs state otherwise.
4. Treat boolean-return APIs and long-running callbacks as gates; expose failure to UI/logs instead of continuing silently.
5. Keep timeline time units in microseconds across trim, inPoint, outPoint, duration, seek, playback, and compile APIs.
6. Use `demo-api-constraint-map.md` for exact parameter shapes and guard tags, `demo-sdk-constants-map.md` for constants, and `demo-api-call-order-map.md` for broader flow sequencing.
