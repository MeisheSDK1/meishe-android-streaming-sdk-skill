# Demo API To Simple Code Map

Use this map to route SDK API questions to reusable simple code. It complements `demo-api-list.md`, which remains the exhaustive API/token inventory. Source labels and snippet ids are self-contained provenance; do not read the external Demo at skill use time.

For exact API/member generation, use `demo-api-simple-code-map.json` as the
authoritative per-member map. This Markdown table is a compact family router.
The JSON distinguishes `direct_unit`, `composed_recipe`, and `evidence_only`
instead of treating every retained evidence fragment as reusable code.

## API Family Map

| API family / class | Simple code refs | Requires | Provides | Modules |
| --- | --- | --- | --- | --- |
| `NvsStreamingContext.init`, `getInstance`, SDK settings | `demo-simple-snippets-core-lifecycle.md`, `effects-transforms-001` | `R0`, Android `Application`/context, license path | SDK singleton | `app-runtime` |
| `NvsEffectSdkContext.init`, human detection setup | `demo-simple-snippets-ar-makeup-segmentation.md`, `official-effects-ar-template.md` | `app-runtime`, Effect SDK libs, model files when enabled | Effect SDK context and model capability | `beauty-camera`, `makeup-editor`, `segmentation-keying` |
| `NvsStreamingContext.getAVInfoFromFile`, `NvsAVFileInfo` | `audio-media-078`, `demo-simple-snippets-audio-media.md` | SDK singleton, media path/URI | duration, size, rotation, live-photo metadata | `media-import`, `url-media-import`, `quick-splicing` |
| `NvsVideoResolution`, `NvsAudioResolution`, `NvsRational` | `demo-simple-snippets-timeline-editing.md`, `audio-media-078` | media metadata or requested ratio | timeline resolution/fps/audio setup | `timeline-state-store`, `editor-shell`, `photo-album` |
| `NvsStreamingContext.createTimeline` | `demo-simple-snippets-timeline-editing.md`, `demo-api-dependency-graph.md` | SDK singleton, video/audio/fps resolutions | `NvsTimeline` | `timeline-state-store`, `editor-shell`, `template-engine` |
| `NvsTimeline.appendVideoTrack`, `appendAudioTrack` | `demo-simple-snippets-timeline-editing.md`, `demo-simple-snippets-audio-media.md` | `NvsTimeline` | video/audio tracks | `clip-editor`, `music-editor`, `voiceover-editor` |
| `NvsVideoTrack.appendClip`, clip insert/remove/split | `demo-simple-snippets-timeline-editing.md` | timeline track, media path, valid time range | `NvsVideoClip` and timeline structure | `clip-editor`, `short-video-editor` |
| `NvsVideoClip` trim, volume, pan/scan, image motion | `demo-simple-snippets-timeline-editing.md`, `demo-simple-snippets-effects-transforms.md` | selected clip and stopped playback | clip edit mutation | `clip-editor`, `photo-album` |
| `NvsStreamingContext.connectTimelineWithLiveWindow` | `demo-simple-snippets-preview-export.md`, `demo-validated-editor-architecture.md` | timeline and `NvsLiveWindow` | synchronized preview | `editor-shell`, `timeline-preview` |
| `NvsStreamingContext.playbackTimeline`, `seekTimeline`, callbacks | `demo-simple-snippets-preview-export.md` | connected timeline/live window | playback and UI refresh | `timeline-preview`, `editor-shell` |
| `NvsLiveWindow.mapViewToCanonical`, `mapCanonicalToView`, `mapViewToNormalized` | `demo-simple-snippets-preview-export.md`, `demo-validated-editor-architecture.md` | live window with timeline bound | overlay coordinate mapping | `caption-editor`, `sticker-editor`, `mask-editor`, `watermark-editor` |
| `NvsStreamingContext.compileTimeline` and compile callbacks | `demo-simple-snippets-preview-export.md` | stopped playback/capture, timeline, output path | exported video or failure callback | `export-compile`, `short-video-editor`, `template-editor` |
| `NvsAssetPackageManager.installAssetPackage`, status/query/version | `demo-simple-snippets-assets-packages.md`, `asset-center-workflow.md` | SDK singleton, package path, package type, optional license | installed package id/status | `asset-package-service`, `asset-center-service` |
| `NvsVideoClip.appendBuiltinFx`, `appendPackagedFx` | `demo-simple-snippets-effects-transforms.md` | selected clip, package id if packaged | `NvsVideoFx` | `filter-editor`, `animation-editor`, `background-editor`, `mask-editor` |
| `NvsTimeline.addBuiltinTimelineVideoFx`, packaged timeline FX | `demo-simple-snippets-effects-transforms.md`, `demo-simple-snippets-rare-structural.md` | timeline, in/out time, package id if packaged | `NvsTimelineVideoFx` | `watermark-editor`, `flip-caption`, `cover-maker` |
| `NvsFx.setFloatVal`, `setStringVal`, `setBooleanVal`, `setIntVal`, `setColorVal` | `demo-simple-snippets-effects-transforms.md`, `demo-sdk-constants-map.md` | FX object and typed parameter key | configured FX | all FX/effect modules |
| `NvsTimeline.addCaption`, `addModularCaption` | `demo-simple-snippets-captions-stickers.md` | timeline, inPoint/duration, text/style | `NvsTimelineCaption` | `caption-editor`, `music-lyrics` |
| `NvsTimeline.addCompoundCaption` | `demo-simple-snippets-captions-stickers.md` | timeline, package id, time range | `NvsTimelineCompoundCaption` | `compound-caption-editor`, `template-editor` |
| `NvsTimeline.addAnimatedSticker`, custom sticker APIs | `demo-simple-snippets-captions-stickers.md` | timeline, package id or custom assets, time range | `NvsTimelineAnimatedSticker` | `sticker-editor` |
| Caption/sticker transform, style, span, keyframe APIs | `demo-simple-snippets-captions-stickers.md`, `demo-simple-snippets-rare-structural.md` | selected caption/sticker | styled and positioned overlay | `caption-editor`, `sticker-editor`, `flip-caption` |
| `NvsAudioTrack.addClip`, `NvsAudioClip`, `NvsAudioFx` | `demo-simple-snippets-audio-media.md` | timeline audio track, audio media, time range | music/voice/audio FX | `music-editor`, `voiceover-editor`, `audio-equalizer` |
| `NvsMediaFileConvertor`, `NvsPassthroughConvertor` | `demo-simple-snippets-audio-media.md` | source media, output path, callbacks | converted/spliced media | `quick-splicing`, `url-media-import` |
| `NvsStreamingContext.connectCapturePreviewWithLiveWindow` | `demo-simple-snippets-capture-recording.md` | SDK singleton, camera permission, live window | camera preview | `capture-camera`, `beauty-camera` |
| `startCapturePreview`, `startRecording`, `stopRecording` | `demo-simple-snippets-capture-recording.md` | capture preview, permissions, output path | captured/recorded media | `capture-camera`, `camera-plus-editor` |
| `NvsCaptureVideoFx`, capture FX parameters | `demo-simple-snippets-capture-recording.md`, `demo-simple-snippets-ar-makeup-segmentation.md` | capture preview, built-in FX or installed package | capture filter/beauty/AR effect | `capture-filter`, `beauty-camera`, `ar-scene` |
| `NvsARSceneManipulate`, makeup/face mesh/warp APIs | `demo-simple-snippets-ar-makeup-segmentation.md` | Effect SDK/capture FX, model gates, packages | AR/makeup/face parameter mutation | `beauty-camera`, `makeup-editor`, `makeup-service` |
| Segmentation/keying/mask generator APIs | `demo-simple-snippets-ar-makeup-segmentation.md`, `official-effects-ar-template.md` | Effect SDK, model files, input media/capture | mask/keyed output | `segmentation-keying` |
| Template footage/caption descriptor APIs | `demo-simple-snippets-template-mimo-cutsame.md` | template package, footage metadata, user media | replacement descriptors | `cutsame-template`, `mimo-template` |
| Template/Mimo timeline creation and compile | `demo-simple-snippets-template-mimo-cutsame.md`, `demo-simple-snippets-preview-export.md` | installed template, validated footage | generated timeline/export | `template-editor`, `full-sdk-demo` |

## Bundled API Composition Checks

These are skill-owned integration checks built from the Demo-derived simple code:

| Product shell | API chain composed in generated code |
| --- | --- |
| `short-video-editor` | `getAVInfoFromFile` -> `createTimeline` -> `appendVideoTrack`/`appendClip` -> `connectTimelineWithLiveWindow` -> playback/seek callbacks -> split/filter/caption/sticker/transition/audio mutations -> `compileTimeline`. |
| `beauty-camera` | `connectCapturePreviewWithLiveWindow` -> `startCapturePreview` -> built-in beauty parameters -> `appendPackagedCaptureVideoFx` -> `startRecording`/`stopRecording`. |
| `asset-center-demo` | bundled local catalog -> selected package/font -> `installAssetPackage`/upgrade or font registration -> typed local result. The standalone host applies an installed filter with `appendPackagedFx`, edits intensity, removes it, and refreshes an aspect-matched Timeline/LiveWindow. No request layer is retained. |

## Exact API Lookup Rule

For an exact member such as `NvsTimelineCaption.setTextColor`, first search:

```powershell
rg "NvsTimelineCaption|setTextColor" .codex\skills\meishe-android-streaming-sdk-api\references\demo-simple-snippets-*.md
```

Then use this map to attach the found snippet to the correct module dependency chain. If no method-level snippet exists, search `demo-simple-snippets-exhaustive-statements.md` before treating the API as uncovered.
