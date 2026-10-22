# Demo API Priority Map

This reference ranks demo-covered API surfaces by frequency, coverage, role criticality, and failure impact. Use it before loading large snippets when a user request is broad or when choosing which API path to implement first.

Priority semantics:
- `P0`: baseline/core. Missing it usually prevents SDK startup, timeline creation, preview, export, or state management.
- `P1`: common/high-value. Missing it breaks common capture/edit/preview/asset workflows.
- `P2`: feature-critical. Required for a specific requested feature family.
- `P3`: low-frequency or optional. Load only when directly requested or found by exact search.

Scoring inputs: demo file coverage, call-site frequency, method/expanded snippet coverage, official-doc visibility, known core roles, guard/callback complexity, and constant kind.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Summary](#summary)
- [P0/P1 API Class Shortlist](#p0p1-api-class-shortlist)
- [API Class Priority Map](#api-class-priority-map)
- [Observed Method Priority Map](#observed-method-priority-map)
- [Direct Member/Static Token Priority Map](#direct-memberstatic-token-priority-map)
- [Constant/Type Priority Map](#constanttype-priority-map)
<!-- END GENERATED CONTENTS -->

## Summary

| Priority | Count | Use first when |
| --- | ---: | --- |
| `P0` | 8 | Creating any runnable SDK app or diagnosing skeleton failures. |
| `P1` | 32 | Building common editing/capture/preview/export workflows. |
| `P2` | 245 | Implementing a selected feature family. |
| `P3` | 777 | Handling exact edge API/member/constant requests. |

## P0/P1 API Class Shortlist

| API class | Priority | Score | Files | Category | Missing impact |
| --- | --- | ---: | ---: | --- | --- |
| `NvsStreamingContext` | `P0` | 100 | 138 | `core-lifecycle` | project/core flow fails |
| `NvsTimeline` | `P0` | 100 | 103 | `timeline-editing` | project/core flow fails |
| `NvsVideoResolution` | `P0` | 96 | 45 | `core-lifecycle` | timeline/preview/edit flow incomplete |
| `NvsAudioResolution` | `P0` | 90 | 10 | `core-lifecycle` | timeline/preview/edit flow incomplete |
| `NvsRational` | `P0` | 90 | 23 | `core-lifecycle` | timeline/preview/edit flow incomplete |
| `NvsVideoClip` | `P1` | 86 | 71 | `timeline-editing` | timeline/preview/edit flow incomplete |
| `NvsVideoTrack` | `P1` | 85 | 64 | `timeline-editing` | timeline/preview/edit flow incomplete |
| `NvsAVFileInfo` | `P1` | 79 | 38 | `audio-media` | feature-specific or optional |
| `NvsAssetPackageManager` | `P1` | 79 | 40 | `assets-packages` | requested feature may fail or degrade |
| `NvsLiveWindow` | `P1` | 75 | 27 | `preview-export` | timeline/preview/edit flow incomplete |
| `NvsColor` | `P1` | 74 | 25 | `effects-transforms` | requested feature may fail or degrade |
| `NvsLiveWindowExt` | `P1` | 70 | 7 | `preview-export` | timeline/preview/edit flow incomplete |
| `NvsMultiThumbnailSequenceView` | `P1` | 70 | 33 | `preview-export` | feature-specific or optional |
| `NvsSize` | `P1` | 70 | 20 | `core-lifecycle` | feature-specific or optional |

## API Class Priority Map

| API class | Package | Priority | Score | Files | Category | Coverage | Missing impact |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| `NvsStreamingContext` | `com.meicam.sdk` | `P0` | 100 | 138 | `core-lifecycle` | method, expanded, official | project/core flow fails |
| `NvsTimeline` | `com.meicam.sdk` | `P0` | 100 | 103 | `timeline-editing` | method, expanded, official | project/core flow fails |
| `NvsVideoResolution` | `com.meicam.sdk` | `P0` | 96 | 45 | `core-lifecycle` | method, expanded, official | timeline/preview/edit flow incomplete |
| `NvsAudioResolution` | `com.meicam.sdk` | `P0` | 90 | 10 | `core-lifecycle` | method, expanded, official | timeline/preview/edit flow incomplete |
| `NvsRational` | `com.meicam.sdk` | `P0` | 90 | 23 | `core-lifecycle` | method, expanded, official | timeline/preview/edit flow incomplete |
| `NvsVideoClip` | `com.meicam.sdk` | `P1` | 86 | 71 | `timeline-editing` | method, expanded, official | timeline/preview/edit flow incomplete |
| `NvsVideoTrack` | `com.meicam.sdk` | `P1` | 85 | 64 | `timeline-editing` | method, expanded, official | timeline/preview/edit flow incomplete |
| `NvsAVFileInfo` | `com.meicam.sdk` | `P1` | 79 | 38 | `audio-media` | method, expanded, official | feature-specific or optional |
| `NvsAssetPackageManager` | `com.meicam.sdk` | `P1` | 79 | 40 | `assets-packages` | method, expanded, official | requested feature may fail or degrade |
| `NvsLiveWindow` | `com.meicam.sdk` | `P1` | 75 | 27 | `preview-export` | method, expanded, official | timeline/preview/edit flow incomplete |
| `NvsColor` | `com.meicam.sdk` | `P1` | 74 | 25 | `effects-transforms` | method, expanded, official | requested feature may fail or degrade |
| `NvsLiveWindowExt` | `com.meicam.sdk` | `P1` | 70 | 7 | `preview-export` | method, expanded | timeline/preview/edit flow incomplete |
| `NvsMultiThumbnailSequenceView` | `com.meicam.sdk` | `P1` | 70 | 33 | `preview-export` | method, expanded | feature-specific or optional |
| `NvsSize` | `com.meicam.sdk` | `P1` | 70 | 20 | `core-lifecycle` | method, expanded | feature-specific or optional |
| `NvsVideoFx` | `com.meicam.sdk` | `P2` | 62 | 25 | `effects-transforms` | method, expanded, official | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker` | `com.meicam.sdk` | `P2` | 58 | 16 | `captions-stickers` | method, expanded, official | requested feature may fail or degrade |
| `NvsTimelineCaption` | `com.meicam.sdk` | `P2` | 58 | 17 | `captions-stickers` | method, expanded, official | requested feature may fail or degrade |
| `NvsTimelineVideoFx` | `com.meicam.sdk` | `P2` | 58 | 17 | `effects-transforms` | method, expanded, official | requested feature may fail or degrade |
| `NvsAudioTrack` | `com.meicam.sdk` | `P2` | 57 | 15 | `audio-media` | method, expanded, official | feature-specific or optional |
| `NvsAudioClip` | `com.meicam.sdk` | `P2` | 53 | 10 | `audio-media` | method, expanded, official | feature-specific or optional |
| `NvsCaptureVideoFx` | `com.meicam.sdk` | `P2` | 53 | 10 | `audio-media` | method, expanded, official | requested feature may fail or degrade |
| `NvsFx` | `com.meicam.sdk` | `P2` | 53 | 10 | `effects-transforms` | method, expanded, official | requested feature may fail or degrade |
| `NvsTimelineCompoundCaption` | `com.meicam.sdk` | `P2` | 50 | 17 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsAudioFx` | `com.meicam.sdk` | `P2` | 49 | 7 | `audio-media` | method, expanded, official | requested feature may fail or degrade |
| `NvsEffectSdkContext` | `com.meicam.effect.sdk` | `P2` | 48 | 6 | `ar-makeup-segmentation` | method, expanded, official | requested feature may fail or degrade |
| `NvsMaskRegionInfo` | `com.meicam.sdk` | `P2` | 48 | 6 | `effects-transforms` | method, expanded, official | requested feature may fail or degrade |
| `NvsARSceneManipulate` | `com.meicam.sdk` | `P2` | 46 | 5 | `ar-makeup-segmentation` | method, expanded, official | requested feature may fail or degrade |
| `NvsMediaFileConvertor` | `com.meicam.sdk` | `P2` | 46 | 5 | `template-mimo-cutsame` | method, expanded, official | feature-specific or optional |
| `NvsCaption` | `com.meicam.sdk` | `P2` | 45 | 10 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsVideoTransition` | `com.meicam.sdk` | `P3` | 44 | 9 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsVideoStreamInfo` | `com.meicam.sdk` | `P3` | 42 | 8 | `audio-media` | method, expanded | feature-specific or optional |
| `NvsVideoFrameRetriever` | `com.meicam.sdk` | `P3` | 41 | 3 | `captions-stickers` | method, expanded, official | requested feature may fail or degrade |
| `NvsClipCaption` | `com.meicam.sdk` | `P3` | 40 | 6 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsCaptureSceneInfo` | `com.meicam.sdk` | `P3` | 38 | 2 | `ar-makeup-segmentation` | method, expanded, official | requested feature may fail or degrade |
| `NvsControlPointPair` | `com.meicam.sdk` | `P3` | 38 | 5 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsExpressionParam` | `com.meicam.sdk` | `P3` | 38 | 5 | `assets-packages` | method, expanded | requested feature may fail or degrade |
| `NvsPosition2D` | `com.meicam.sdk` | `P3` | 38 | 2 | `audio-media` | method, expanded, official | feature-specific or optional |
| `NvsAnimatedSticker` | `com.meicam.sdk` | `P3` | 36 | 4 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsClipAnimatedSticker` | `com.meicam.sdk` | `P3` | 36 | 4 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsEffect` | `com.meicam.effect.sdk` | `P3` | 34 | 1 | `effects-transforms` | method, expanded, official | requested feature may fail or degrade |
| `NvsEffectRenderCore` | `com.meicam.effect.sdk` | `P3` | 34 | 1 | `ar-makeup-segmentation` | method, expanded, official | requested feature may fail or degrade |
| `NvsObject` | `com.meicam.sdk` | `P3` | 34 | 1 | `template-mimo-cutsame` | method, expanded, official | feature-specific or optional |
| `NvsUtils` | `com.meicam.sdk` | `P3` | 34 | 1 | `audio-media` | method, expanded, official | feature-specific or optional |
| `NvsVideoEffect` | `com.meicam.effect.sdk` | `P3` | 34 | 1 | `effects-transforms` | method, expanded, official | requested feature may fail or degrade |
| `NvsAssetPackageParticleDescParser` | `com.meicam.sdk` | `P3` | 33 | 3 | `audio-media` | method, expanded | requested feature may fail or degrade |
| `NvsPointD` | `com.meicam.sdk` | `P3` | 33 | 3 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsCaptionSpan` | `com.meicam.sdk` | `P3` | 30 | 2 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsCaptureCompoundCaption` | `com.meicam.sdk` | `P3` | 30 | 2 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsFxDescription` | `com.meicam.sdk` | `P3` | 30 | 2 | `audio-media` | method, expanded | requested feature may fail or degrade |
| `NvsIconGenerator` | `com.meicam.sdk` | `P3` | 30 | 2 | `audio-media` | method, expanded | feature-specific or optional |
| `NvsAIContext` | `com.meicam.ai.sdk` | `P3` | 26 | 1 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsArbitraryData` | `com.meicam.sdk` | `P3` | 26 | 1 | `effects-transforms` | method, expanded | requested feature may fail or degrade |
| `NvsBodyOpacitySpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsCaptureAnimatedSticker` | `com.meicam.sdk` | `P3` | 26 | 1 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsCaptureAudioFx` | `com.meicam.sdk` | `P3` | 26 | 1 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsClipCompoundCaption` | `com.meicam.sdk` | `P3` | 26 | 1 | `template-mimo-cutsame` | method, expanded | requested feature may fail or degrade |
| `NvsColorSpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsCompoundCaption` | `com.meicam.sdk` | `P3` | 26 | 1 | `template-mimo-cutsame` | method, expanded | requested feature may fail or degrade |
| `NvsFaceDetector` | `com.meicam.ai.sdk` | `P3` | 26 | 1 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsFontFamilySpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsFontSizeRatioSpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsItalicSpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsMakeupEffectInfo` | `com.meicam.sdk` | `P3` | 26 | 1 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsNormalTextSpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsOpacitySpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsOutlineColorSpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsOutlineOpacitySpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsOutlineWidthSpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsPanAndScan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsParticleSystemContext` | `com.meicam.sdk` | `P3` | 26 | 1 | `audio-media` | method, expanded | requested feature may fail or degrade |
| `NvsPassthroughConvertor` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsRendererIdSpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsShadowOpacitySpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsTrackCaption` | `com.meicam.sdk` | `P3` | 26 | 1 | `template-mimo-cutsame` | method, expanded | requested feature may fail or degrade |
| `NvsUnderlineSpan` | `com.meicam.sdk` | `P3` | 26 | 1 | `captions-stickers` | method, expanded | requested feature may fail or degrade |
| `NvsVideoEffectAnimatedSticker` | `com.meicam.effect.sdk` | `P3` | 26 | 1 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsVideoEffectCompoundCaption` | `com.meicam.effect.sdk` | `P3` | 26 | 1 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsVideoFrameInfo` | `com.meicam.sdk` | `P3` | 26 | 1 | `ar-makeup-segmentation` | method, expanded | requested feature may fail or degrade |
| `NvsVolume` | `com.meicam.sdk` | `P3` | 26 | 1 | `audio-media` | method, expanded | feature-specific or optional |
| `Logger` | `com.meicam.nvconvertorlib` | `P3` | 23 | 3 | `audio-media` | touchpoint-only | feature-specific or optional |

## Observed Method Priority Map

This table ranks the high-signal observed instance/static method rows available in `demo-api-constraint-map.md`.

| API method | Priority | Score | Calls | Area | Guards | Missing impact |
| --- | --- | ---: | ---: | --- | --- | --- |
| `NvsStreamingContext.getTimelineCurrentPosition` | `P0` | 91 | 284 | `timeline-editing` | `conditional`(223), `null-check`(125), `time-range`(99), `engine-state-guard`(33), `empty-string-check`(14), `callback`(9) | feature-specific or optional |
| `NvsTimeline.getDuration` | `P0` | 90 | 253 | `timeline-editing` | `time-range`(253), `conditional`(163), `null-check`(86), `engine-state-guard`(13), `callback`(11), `empty-string-check`(9) | feature-specific or optional |
| `NvsStreamingContext.getInstance` | `P1` | 85 | 139 | `core-lifecycle` | `conditional`(75), `null-check`(57), `time-range`(24), `empty-string-check`(13), `callback`(9), `asset-package-result`(2) | project/core flow fails |
| `NvsStreamingContext.stop` | `P1` | 80 | 70 | `general` | `conditional`(48), `null-check`(32), `engine-state-guard`(14), `time-range`(5), `callback`(3), `permission-gate`(1) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.getStreamingEngineState` | `P1` | 76 | 45 | `general` | `engine-state-guard`(45), `conditional`(36), `null-check`(16), `time-range`(6), `empty-string-check`(1) | project/core flow fails |
| `NvsTimeline.getVideoTrackByIndex` | `P1` | 75 | 140 | `timeline-editing` | `conditional`(131), `null-check`(126), `time-range`(27), `empty-string-check`(6) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.getAssetPackageManager` | `P1` | 73 | 30 | `asset-packages` | `conditional`(22), `null-check`(20), `asset-package-result`(11), `empty-string-check`(9), `time-range`(3), `callback`(3) | requested feature may fail or degrade |
| `NvsStreamingContext.seekTimeline` | `P1` | 72 | 25 | `timeline-editing` | `conditional`(11), `null-check`(7), `time-range`(4), `engine-state-guard`(3) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.connectTimelineWithLiveWindow` | `P1` | 71 | 22 | `timeline-editing` | `conditional`(12), `time-range`(12), `null-check`(8), `engine-state-guard`(3), `callback`(1) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.playbackTimeline` | `P1` | 71 | 23 | `timeline-editing` | `conditional`(11), `null-check`(4), `time-range`(4), `engine-state-guard`(3) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.setPlaybackCallback` | `P2` | 69 | 17 | `preview-playback` | `callback`(17), `conditional`(6), `null-check`(5) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.setStreamingEngineCallback` | `P2` | 69 | 17 | `general` | `callback`(17), `conditional`(10), `engine-state-guard`(8), `time-range`(2), `null-check`(2), `model-or-module-gate`(1) | state/error handling becomes fragile |
| `NvsStreamingContext.removeAllCaptureVideoFx` | `P2` | 68 | 15 | `capture-recording` | `conditional`(11), `null-check`(7), `time-range`(3), `callback`(2), `permission-gate`(2), `model-or-module-gate`(1) | requested feature may fail or degrade |
| `NvsStreamingContext.setPlaybackCallback2` | `P2` | 68 | 15 | `preview-playback` | `callback`(15), `conditional`(6), `null-check`(5), `time-range`(1) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.setCompileConfigurations` | `P2` | 66 | 12 | `compile-export` | `conditional`(10), `null-check`(4), `callback`(4), `time-range`(1), `asset-package-result`(1) | feature-specific or optional |
| `NvsTimeline.getFirstTimelineVideoFx` | `P2` | 66 | 12 | `timeline-editing` | `null-check`(11), `conditional`(8), `engine-state-guard`(1), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimeline.getVideoRes` | `P2` | 66 | 45 | `timeline-editing` | `conditional`(21), `null-check`(15), `time-range`(2) | feature-specific or optional |
| `NvsStreamingContext.setCompileCallback` | `P2` | 65 | 10 | `compile-export` | `callback`(10), `conditional`(3), `null-check`(1), `time-range`(1) | state/error handling becomes fragile |
| `NvsStreamingContext.removeTimeline` | `P2` | 64 | 9 | `timeline-editing` | `conditional`(8), `null-check`(8), `time-range`(1), `callback`(1) | feature-specific or optional |
| `NvsStreamingContext.startRecording` | `P2` | 64 | 9 | `capture-recording` | `conditional`(8), `engine-state-guard`(1), `null-check`(1), `time-range`(1) | requested feature may fail or degrade |
| `NvsStreamingContext.getAVFileInfo` | `P2` | 63 | 30 | `general` | `conditional`(27), `null-check`(23), `time-range`(7) | feature-specific or optional |
| `NvsStreamingContext.removeCurrentCaptureScene` | `P2` | 63 | 7 | `capture-recording` | `conditional`(6), `null-check`(4), `callback`(1) | requested feature may fail or degrade |
| `NvsStreamingContext.stopRecording` | `P2` | 63 | 8 | `capture-recording` | `conditional`(7), `engine-state-guard`(2), `null-check`(2) | requested feature may fail or degrade |
| `NvsVideoTrack.getClipByIndex` | `P2` | 63 | 134 | `timeline-editing` | `conditional`(122), `null-check`(115), `time-range`(64), `empty-string-check`(1) | timeline/preview/edit flow incomplete |
| `NvsTimeline.appendVideoTrack` | `P2` | 62 | 25 | `timeline-editing` | `conditional`(23), `null-check`(23), `empty-string-check`(2), `time-range`(2) | timeline/preview/edit flow incomplete |
| `NvsTimeline.getNextCaption` | `P2` | 62 | 24 | `timeline-editing` | `conditional`(16), `null-check`(9), `time-range`(2) | requested feature may fail or degrade |
| `NvsVideoFx.setFloatVal` | `P2` | 62 | 121 | `effects-transforms` | `conditional`(45), `null-check`(28), `time-range`(4), `engine-state-guard`(4), `empty-string-check`(3) | requested feature may fail or degrade |
| `NvsStreamingContext.setCaptureDeviceCallback` | `P2` | 61 | 6 | `capture-recording` | `time-range`(6), `callback`(6), `conditional`(4), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimeline.getFirstCaption` | `P2` | 60 | 19 | `timeline-editing` | `null-check`(19), `conditional`(15), `time-range`(3) | requested feature may fail or degrade |
| `NvsVideoTrack.getClipCount` | `P2` | 60 | 92 | `timeline-editing` | `conditional`(82), `null-check`(65), `time-range`(16), `empty-string-check`(2) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.getCaptureDeviceCount` | `P2` | 59 | 10 | `capture-recording` | `conditional`(10), `callback`(7), `time-range`(5), `empty-string-check`(1), `permission-gate`(1) | requested feature may fail or degrade |
| `NvsTimeline.addBuiltinTimelineVideoFx` | `P2` | 59 | 16 | `timeline-editing` | `time-range`(16), `conditional`(14), `null-check`(6), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimeline.getAudioTrackByIndex` | `P2` | 59 | 18 | `timeline-editing` | `conditional`(16), `null-check`(16), `time-range`(2), `empty-string-check`(2) | feature-specific or optional |
| `NvsStreamingContext.createTimeline` | `P2` | 58 | 15 | `timeline-editing` | `conditional`(13), `null-check`(13) | project/core flow fails |
| `NvsTimeline.addPackagedTimelineVideoFx` | `P2` | 58 | 14 | `timeline-editing` | `time-range`(14), `conditional`(12), `null-check`(7), `empty-string-check`(4) | requested feature may fail or degrade |
| `NvsTimeline.removeCaption` | `P2` | 58 | 15 | `timeline-editing` | `conditional`(10), `null-check`(7), `time-range`(7), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsStreamingContext.appendBuiltinCaptureVideoFx` | `P2` | 57 | 13 | `capture-recording` | `conditional`(13), `null-check`(9), `empty-string-check`(3), `model-or-module-gate`(1) | requested feature may fail or degrade |
| `NvsStreamingContext.getCaptureVideoFxByIndex` | `P2` | 57 | 13 | `capture-recording` | `conditional`(13), `null-check`(9) | requested feature may fail or degrade |
| `NvsStreamingContext.setCaptureRecordingDurationCallback` | `P2` | 57 | 7 | `capture-recording` | `time-range`(7), `callback`(7), `conditional`(5), `model-or-module-gate`(1) | requested feature may fail or degrade |
| `NvsStreamingContext.setCompileCallback2` | `P2` | 57 | 7 | `compile-export` | `callback`(7), `conditional`(5), `time-range`(1) | state/error handling becomes fragile |
| `NvsTimeline.removeTimelineVideoFx` | `P2` | 57 | 13 | `timeline-editing` | `conditional`(11), `null-check`(10), `time-range`(3) | requested feature may fail or degrade |
| `NvsTimeline.setThemeMusicVolumeGain` | `P2` | 57 | 13 | `timeline-editing` | `conditional`(9), `null-check`(9), `empty-string-check`(8), `time-range`(2) | feature-specific or optional |
| `NvsTimelineCaption.getInPoint` | `P2` | 57 | 62 | `timeline-editing` | `time-range`(62), `conditional`(51), `null-check`(30), `empty-string-check`(5), `engine-state-guard`(1) | requested feature may fail or degrade |
| `NvsVideoClip.getInPoint` | `P2` | 57 | 64 | `timeline-editing` | `time-range`(64), `conditional`(39), `null-check`(27) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.getCaptureVideoFxCount` | `P2` | 56 | 12 | `capture-recording` | `conditional`(11), `null-check`(8), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsStreamingContext.removeCaptureVideoFx` | `P2` | 56 | 11 | `capture-recording` | `conditional`(11), `null-check`(6), `empty-string-check`(3) | requested feature may fail or degrade |
| `NvsTimeline.removeAnimatedSticker` | `P2` | 56 | 12 | `timeline-editing` | `null-check`(10), `conditional`(7), `time-range`(5) | requested feature may fail or degrade |
| `NvsVideoClip.getOutPoint` | `P2` | 56 | 53 | `timeline-editing` | `time-range`(53), `conditional`(24), `null-check`(15) | timeline/preview/edit flow incomplete |
| `NvsClipCaption.getInPoint` | `P2` | 55 | 49 | `timeline-editing` | `time-range`(49), `conditional`(40), `null-check`(18), `empty-string-check`(4), `engine-state-guard`(1) | requested feature may fail or degrade |
| `NvsStreamingContext.compileTimeline` | `P2` | 55 | 6 | `compile-export` | `time-range`(4), `conditional`(4), `callback`(1) | project/core flow fails |
| `NvsStreamingContext.setCaptureRecordingStartedCallback` | `P2` | 55 | 6 | `capture-recording` | `time-range`(6), `callback`(6), `conditional`(4), `model-or-module-gate`(1) | requested feature may fail or degrade |
| `NvsTimeline.getFirstAnimatedSticker` | `P2` | 55 | 10 | `timeline-editing` | `null-check`(10), `conditional`(8), `time-range`(3) | requested feature may fail or degrade |
| `NvsVideoClip.getTrimIn` | `P2` | 55 | 50 | `timeline-editing` | `time-range`(50), `conditional`(24), `null-check`(13) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.getAVInfoFromFile` | `P2` | 54 | 9 | `general` | `conditional`(9), `null-check`(8), `empty-string-check`(2), `time-range`(1) | feature-specific or optional |
| `NvsTimeline.addCaption` | `P2` | 54 | 9 | `timeline-editing` | `conditional`(8), `time-range`(5), `null-check`(3) | requested feature may fail or degrade |
| `NvsTimeline.addCompoundCaption` | `P2` | 54 | 9 | `timeline-editing` | `time-range`(9), `conditional`(8), `empty-string-check`(5), `null-check`(4) | requested feature may fail or degrade |
| `NvsTimeline.appendAudioTrack` | `P2` | 54 | 9 | `timeline-editing` | `conditional`(6), `null-check`(6), `time-range`(1), `empty-string-check`(1) | feature-specific or optional |
| `NvsTimeline.getFirstCompoundCaption` | `P2` | 54 | 9 | `timeline-editing` | `null-check`(8), `conditional`(3), `time-range`(2) | requested feature may fail or degrade |
| `NvsVideoClip.getTrimOut` | `P2` | 54 | 40 | `timeline-editing` | `time-range`(40), `conditional`(15), `null-check`(7) | timeline/preview/edit flow incomplete |
| `NvsVideoClip.setImageMotionMode` | `P2` | 54 | 11 | `timeline-editing` | `conditional`(9), `null-check`(4), `time-range`(3), `callback`(1) | timeline/preview/edit flow incomplete |
| `NvsAVFileInfo.getVideoStreamDimension` | `P2` | 53 | 35 | `general` | `conditional`(30), `null-check`(13), `time-range`(3) | feature-specific or optional |
| `NvsLiveWindow.setOnTouchListener` | `P2` | 53 | 10 | `preview-playback` | `conditional`(7), `null-check`(2), `engine-state-guard`(1) | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.appendPackagedCaptureVideoFx` | `P2` | 53 | 7 | `capture-recording` | `conditional`(7), `empty-string-check`(5), `null-check`(4) | requested feature may fail or degrade |
| `NvsStreamingContext.getCaptureDeviceCapability` | `P2` | 53 | 7 | `capture-recording` | `conditional`(6), `null-check`(6), `exception-handled`(1) | requested feature may fail or degrade |
| `NvsStreamingContext.hasARModule` | `P2` | 53 | 8 | `ar-makeup-segmentation` | `model-or-module-gate`(8), `conditional`(7), `null-check`(6), `time-range`(2) | requested feature may fail or degrade |
| `NvsTimeline.addAnimatedSticker` | `P2` | 53 | 7 | `timeline-editing` | `time-range`(7), `conditional`(6), `null-check`(6) | requested feature may fail or degrade |
| `NvsTimeline.addCustomAnimatedSticker` | `P2` | 53 | 7 | `timeline-editing` | `time-range`(7), `conditional`(6), `null-check`(6), `asset-package-result`(2) | requested feature may fail or degrade |
| `NvsVideoClip.appendBuiltinFx` | `P2` | 53 | 35 | `timeline-editing` | `conditional`(28), `null-check`(25), `time-range`(2) | requested feature may fail or degrade |
| `NvsVideoClip.getFilePath` | `P2` | 53 | 37 | `timeline-editing` | `time-range`(28), `conditional`(19), `null-check`(12), `empty-string-check`(1) | timeline/preview/edit flow incomplete |
| `NvsVideoClip.setImageMotionAnimationEnabled` | `P2` | 52 | 9 | `timeline-editing` | `conditional`(7), `null-check`(4), `time-range`(3), `callback`(1), `empty-string-check`(1) | timeline/preview/edit flow incomplete |
| `NvsLiveWindow.setFillMode` | `P2` | 51 | 8 | `preview-playback` | `time-range`(3), `callback`(1), `conditional`(1), `null-check`(1) | timeline/preview/edit flow incomplete |
| `NvsLiveWindow.setOnClickListener` | `P2` | 51 | 8 | `preview-playback` | `conditional`(4), `callback`(2), `null-check`(2) | timeline/preview/edit flow incomplete |
| `NvsTimeline.getAnimatedStickersByTimelinePosition` | `P2` | 51 | 6 | `timeline-editing` | `conditional`(6), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimeline.getNextAnimatedSticker` | `P2` | 51 | 6 | `timeline-editing` | `conditional`(5), `null-check`(2), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimeline.removeCompoundCaption` | `P2` | 51 | 6 | `timeline-editing` | `null-check`(5), `conditional`(4), `time-range`(4), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getInPoint` | `P2` | 51 | 28 | `timeline-editing` | `time-range`(28), `conditional`(18), `null-check`(13), `empty-string-check`(4), `callback`(1) | requested feature may fail or degrade |
| `NvsVideoClip.setPanAndScan` | `P2` | 51 | 7 | `timeline-editing` | `conditional`(7), `null-check`(3), `time-range`(1), `engine-state-guard`(1) | timeline/preview/edit flow incomplete |
| `NvsVideoTrack.appendClip` | `P2` | 51 | 28 | `timeline-editing` | `conditional`(26), `null-check`(26), `time-range`(11), `empty-string-check`(8) | timeline/preview/edit flow incomplete |
| `NvsVideoTrack.setVolumeGain` | `P2` | 51 | 27 | `timeline-editing` | `conditional`(20), `null-check`(10), `time-range`(7), `empty-string-check`(2) | timeline/preview/edit flow incomplete |
| `NvsClipAnimatedSticker.getInPoint` | `P2` | 50 | 24 | `timeline-editing` | `time-range`(24), `conditional`(15), `null-check`(10), `empty-string-check`(4), `callback`(1) | requested feature may fail or degrade |
| `NvsAVFileInfo.getVideoStreamRotation` | `P2` | 49 | 23 | `general` | `conditional`(22), `null-check`(8) | feature-specific or optional |
| `NvsTimelineCompoundCaption.getInPoint` | `P2` | 49 | 22 | `timeline-editing` | `time-range`(22), `conditional`(13), `null-check`(10), `engine-state-guard`(1) | requested feature may fail or degrade |
| `NvsVideoClip.getFxByIndex` | `P2` | 49 | 22 | `timeline-editing` | `conditional`(21), `null-check`(15), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsVideoClip.getFxCount` | `P2` | 49 | 23 | `timeline-editing` | `conditional`(20), `null-check`(15) | requested feature may fail or degrade |
| `NvsLiveWindow.getHeight` | `P2` | 48 | 19 | `preview-playback` | `conditional`(11), `null-check`(4), `time-range`(1) | timeline/preview/edit flow incomplete |
| `NvsTimelineCompoundCaption.getOutPoint` | `P2` | 48 | 20 | `timeline-editing` | `time-range`(20), `conditional`(11), `null-check`(8), `engine-state-guard`(1) | requested feature may fail or degrade |
| `NvsLiveWindow.getWidth` | `P2` | 47 | 18 | `preview-playback` | `conditional`(11), `null-check`(3), `time-range`(1) | timeline/preview/edit flow incomplete |
| `NvsLiveWindowExt.getHeight` | `P2` | 47 | 16 | `preview-playback` | `conditional`(10), `null-check`(4) | timeline/preview/edit flow incomplete |
| `NvsLiveWindowExt.getWidth` | `P2` | 47 | 16 | `preview-playback` | `conditional`(10), `null-check`(4) | timeline/preview/edit flow incomplete |
| `NvsVideoClip.changeTrimOutPoint` | `P2` | 47 | 17 | `timeline-editing` | `time-range`(17), `conditional`(15), `null-check`(5) | timeline/preview/edit flow incomplete |
| `NvsVideoClip.getRawFxByIndex` | `P2` | 47 | 16 | `timeline-editing` | `conditional`(16), `null-check`(16) | requested feature may fail or degrade |
| `NvsVideoClip.getVideoType` | `P2` | 46 | 15 | `timeline-editing` | `conditional`(15), `time-range`(13), `null-check`(4) | timeline/preview/edit flow incomplete |
| `NvsVideoClip.setVolumeGain` | `P2` | 46 | 15 | `timeline-editing` | `conditional`(12), `empty-string-check`(9), `time-range`(7), `null-check`(3) | timeline/preview/edit flow incomplete |
| `NvsVideoTrack.getTransitionBySourceClipIndex` | `P2` | 46 | 14 | `timeline-editing` | `conditional`(14), `null-check`(14), `time-range`(9) | timeline/preview/edit flow incomplete |
| `NvsVideoTrack.setBuiltinTransition` | `P2` | 46 | 14 | `timeline-editing` | `conditional`(12), `null-check`(8), `time-range`(4), `empty-string-check`(1) | timeline/preview/edit flow incomplete |
| `NvsVideoClip.appendRawBuiltinFx` | `P2` | 45 | 13 | `timeline-editing` | `conditional`(13), `null-check`(12) | requested feature may fail or degrade |
| `NvsVideoClip.changeTrimInPoint` | `P2` | 45 | 13 | `timeline-editing` | `time-range`(13), `conditional`(12), `null-check`(5) | timeline/preview/edit flow incomplete |
| `NvsAVFileInfo.getDuration` | `P3` | 44 | 12 | `general` | `time-range`(12), `conditional`(8), `null-check`(5) | feature-specific or optional |
| `NvsSize.set` | `P3` | 44 | 26 | `general` | `conditional`(25) | feature-specific or optional |
| `NvsVideoClip.getIndex` | `P3` | 44 | 12 | `timeline-editing` | `conditional`(10), `null-check`(7), `time-range`(6) | timeline/preview/edit flow incomplete |
| `NvsVideoClip.getNextCaption` | `P3` | 44 | 11 | `timeline-editing` | `conditional`(6), `null-check`(4), `time-range`(2) | requested feature may fail or degrade |
| `NvsVideoClip.getRawFxCount` | `P3` | 44 | 12 | `timeline-editing` | `conditional`(11), `null-check`(11) | requested feature may fail or degrade |
| `NvsVideoClip.getSpeed` | `P3` | 44 | 11 | `timeline-editing` | `time-range`(6), `conditional`(4), `null-check`(2) | timeline/preview/edit flow incomplete |
| `NvsVideoTrack.setPackagedTransition` | `P3` | 44 | 12 | `timeline-editing` | `conditional`(12), `null-check`(5), `time-range`(5), `empty-string-check`(3) | requested feature may fail or degrade |
| `NvsTimelineCaption.getZValue` | `P3` | 43 | 38 | `timeline-editing` | `conditional`(36), `null-check`(28), `time-range`(8), `empty-string-check`(5) | requested feature may fail or degrade |
| `NvsVideoFx.setBooleanVal` | `P3` | 43 | 36 | `effects-transforms` | `conditional`(30), `null-check`(23), `model-or-module-gate`(6), `time-range`(2), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsVideoFx.setFilterIntensity` | `P3` | 43 | 10 | `effects-transforms` | `conditional`(9), `null-check`(7), `engine-state-guard`(1) | requested feature may fail or degrade |
| `NvsAudioClip.getInPoint` | `P3` | 42 | 32 | `timeline-editing` | `time-range`(32), `conditional`(27), `null-check`(18), `empty-string-check`(1) | feature-specific or optional |
| `NvsVideoClip.getObject` | `P3` | 42 | 9 | `timeline-editing` | `conditional`(8), `null-check`(8), `time-range`(8) | timeline/preview/edit flow incomplete |
| `NvsVideoClip.getPropertyVideoFx` | `P3` | 42 | 9 | `timeline-editing` | `conditional`(9), `null-check`(7), `time-range`(2) | requested feature may fail or degrade |
| `NvsVideoClip.setExtraVideoRotation` | `P3` | 42 | 9 | `timeline-editing` | `conditional`(4), `null-check`(1) | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.getAssetPackageVersion` | `P3` | 41 | 7 | `asset-packages` | `conditional`(7), `asset-package-result`(6), `null-check`(4), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsClipCaption.getZValue` | `P3` | 41 | 28 | `timeline-editing` | `conditional`(26), `null-check`(18), `time-range`(5), `empty-string-check`(4) | requested feature may fail or degrade |
| `NvsLiveWindow.setLayoutParams` | `P3` | 41 | 7 | `preview-playback` | `conditional`(2), `time-range`(1), `null-check`(1) | requested feature may fail or degrade |
| `NvsServerClient.get` | `P3` | 41 | 22 | `general` | `callback`(13), `conditional`(4), `null-check`(2) | feature-specific or optional |
| `NvsVideoClip.appendPackagedFx` | `P3` | 41 | 7 | `timeline-editing` | `conditional`(7), `null-check`(7), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsVideoClip.getFirstCaption` | `P3` | 41 | 7 | `timeline-editing` | `conditional`(7), `null-check`(7), `time-range`(2) | requested feature may fail or degrade |
| `NvsVideoFx.setAttachment` | `P3` | 41 | 27 | `effects-transforms` | `conditional`(18), `null-check`(16) | requested feature may fail or degrade |
| `NvsVideoTrack.getDuration` | `P3` | 41 | 8 | `timeline-editing` | `time-range`(8), `conditional`(7), `null-check`(5) | timeline/preview/edit flow incomplete |
| `NvsVideoTrack.removeClip` | `P3` | 41 | 7 | `timeline-editing` | `conditional`(4), `null-check`(4), `time-range`(2) | timeline/preview/edit flow incomplete |
| `NvsClipCaption.removeKeyframeAtTime` | `P3` | 40 | 26 | `timeline-editing` | `time-range`(21), `conditional`(4), `null-check`(4) | requested feature may fail or degrade |
| `NvsTimelineVideoFx.setFloatVal` | `P3` | 40 | 24 | `timeline-editing` | `conditional`(9), `time-range`(7), `null-check`(7) | requested feature may fail or degrade |
| `NvsAVFileInfo.getAVFileType` | `P3` | 39 | 6 | `general` | `conditional`(6), `null-check`(5), `time-range`(1) | feature-specific or optional |
| `NvsAssetPackageManager.getAssetPackageSupportedAspectRatio` | `P3` | 39 | 6 | `asset-packages` | `conditional`(6), `null-check`(4), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsAudioTrack.getClipCount` | `P3` | 39 | 22 | `timeline-editing` | `conditional`(22), `null-check`(21), `time-range`(17), `empty-string-check`(1) | feature-specific or optional |
| `NvsCaptureVideoFx.setBooleanVal` | `P3` | 39 | 21 | `capture-recording` | `conditional`(20), `null-check`(11), `empty-string-check`(2), `model-or-module-gate`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getCaptionTranslation` | `P3` | 39 | 22 | `timeline-editing` | `conditional`(19), `null-check`(12), `time-range`(1), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.removeKeyframeAtTime` | `P3` | 39 | 21 | `timeline-editing` | `time-range`(15), `conditional`(4), `null-check`(4) | requested feature may fail or degrade |
| `NvsVideoFx.getBuiltinVideoFxName` | `P3` | 39 | 22 | `effects-transforms` | `conditional`(20), `null-check`(15), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsAudioTrack.getClipByIndex` | `P3` | 38 | 19 | `timeline-editing` | `conditional`(19), `time-range`(18), `null-check`(18), `empty-string-check`(1) | feature-specific or optional |
| `NvsTimelineCompoundCaption.getCaptionCount` | `P3` | 38 | 19 | `timeline-editing` | `conditional`(14), `time-range`(4), `null-check`(4) | requested feature may fail or degrade |
| `NvsAudioTrack.addClip` | `P3` | 37 | 16 | `timeline-editing` | `conditional`(16), `time-range`(16), `null-check`(14) | feature-specific or optional |
| `NvsClipCaption.getCaptionTranslation` | `P3` | 37 | 17 | `timeline-editing` | `conditional`(13), `null-check`(9), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getZValue` | `P3` | 37 | 17 | `timeline-editing` | `conditional`(15), `null-check`(8), `time-range`(4), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.getBoundingRectangleVertices` | `P3` | 37 | 16 | `timeline-editing` | `conditional`(16), `null-check`(15) | requested feature may fail or degrade |
| `NvsTimelineCaption.getOutPoint` | `P3` | 37 | 17 | `timeline-editing` | `time-range`(17), `conditional`(14), `null-check`(8), `empty-string-check`(3) | requested feature may fail or degrade |
| `NvsTimelineCompoundCaption.getZValue` | `P3` | 37 | 17 | `timeline-editing` | `conditional`(12), `null-check`(8), `time-range`(7) | requested feature may fail or degrade |
| `NvsVideoFx.getAttachment` | `P3` | 37 | 16 | `effects-transforms` | `conditional`(16), `null-check`(16) | requested feature may fail or degrade |
| `NvsVideoFx.setStringVal` | `P3` | 37 | 17 | `effects-transforms` | `conditional`(13), `null-check`(5), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsAudioClip.setFadeOutDuration` | `P3` | 36 | 15 | `timeline-editing` | `time-range`(15), `conditional`(13), `null-check`(9), `empty-string-check`(1) | feature-specific or optional |
| `NvsCaptureVideoFx.setFloatVal` | `P3` | 36 | 14 | `capture-recording` | `conditional`(12), `null-check`(6), `empty-string-check`(2), `permission-gate`(2) | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.getZValue` | `P3` | 36 | 14 | `timeline-editing` | `conditional`(13), `null-check`(7), `time-range`(3), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsClipCaption.setCurrentKeyFrameTime` | `P3` | 36 | 15 | `timeline-editing` | `time-range`(14), `conditional`(8), `null-check`(6) | requested feature may fail or degrade |
| `NvsLiveWindow.getLayoutParams` | `P3` | 36 | 9 | `preview-playback` | `conditional`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getModularCaptionOutAnimationPackageId` | `P3` | 36 | 15 | `timeline-editing` | `conditional`(12), `empty-string-check`(12), `time-range`(7), `null-check`(1) | requested feature may fail or degrade |
| `NvsTimelineVideoFx.setFilterIntensity` | `P3` | 36 | 14 | `timeline-editing` | `conditional`(11), `time-range`(5), `null-check`(5), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsMultiThumbnailSequenceView.setPixelPerMicrosecond` | `P3` | 35 | 7 | `preview-playback` | `time-range`(3), `conditional`(1) | timeline/preview/edit flow incomplete |
| `NvsMultiThumbnailSequenceView.setThumbnailSequenceDescArray` | `P3` | 35 | 7 | `preview-playback` | `time-range`(3), `conditional`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getOutPoint` | `P3` | 35 | 13 | `timeline-editing` | `time-range`(13), `conditional`(9), `null-check`(8), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getTextSpanList` | `P3` | 35 | 13 | `timeline-editing` | `conditional`(10), `null-check`(1), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setCurrentKeyFrameTime` | `P3` | 35 | 13 | `timeline-editing` | `time-range`(12), `conditional`(7), `null-check`(5) | requested feature may fail or degrade |
| `NvsAudioClip.setAttachment` | `P3` | 34 | 12 | `timeline-editing` | `conditional`(12), `time-range`(12), `null-check`(12) | feature-specific or optional |
| `NvsCaptureVideoFx.getFloatVal` | `P3` | 34 | 12 | `capture-recording` | `conditional`(7), `empty-string-check`(3), `null-check`(2) | requested feature may fail or degrade |
| `NvsCaptureVideoFx.setFilterIntensity` | `P3` | 34 | 12 | `capture-recording` | `conditional`(11), `null-check`(10), `time-range`(1), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsClipCaption.getModularCaptionInAnimationPackageId` | `P3` | 34 | 11 | `timeline-editing` | `conditional`(8), `empty-string-check`(8), `time-range`(5), `null-check`(1) | requested feature may fail or degrade |
| `NvsClipCaption.getOutPoint` | `P3` | 34 | 11 | `timeline-editing` | `time-range`(11), `conditional`(10), `null-check`(5), `empty-string-check`(4) | requested feature may fail or degrade |
| `NvsFx.setFloatVal` | `P3` | 34 | 12 | `effects-transforms` | `conditional`(10), `null-check`(6), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.getModularCaptionAnimationPackageId` | `P3` | 34 | 11 | `timeline-editing` | `conditional`(8), `empty-string-check`(8), `time-range`(6), `null-check`(3) | requested feature may fail or degrade |
| `NvsTimelineCaption.getModularCaptionInAnimationPackageId` | `P3` | 34 | 12 | `timeline-editing` | `conditional`(9), `empty-string-check`(9), `time-range`(6), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getRotationZ` | `P3` | 34 | 12 | `timeline-editing` | `conditional`(5), `null-check`(4), `time-range`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getScaleX` | `P3` | 34 | 12 | `timeline-editing` | `conditional`(9), `null-check`(7), `time-range`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getScaleY` | `P3` | 34 | 12 | `timeline-editing` | `conditional`(8), `null-check`(7), `time-range`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getTextAlignment` | `P3` | 34 | 12 | `timeline-editing` | `conditional`(9), `null-check`(9), `time-range`(3), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setDrawOutline` | `P3` | 34 | 11 | `timeline-editing` | `conditional`(10), `null-check`(7) | requested feature may fail or degrade |
| `NvsTimelineCaption.setTextColor` | `P3` | 34 | 11 | `timeline-editing` | `conditional`(10), `null-check`(8), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineVideoFx.setRegion` | `P3` | 34 | 12 | `timeline-editing` | `conditional`(7), `null-check`(5), `time-range`(3) | requested feature may fail or degrade |
| `NvsAudioClip.getFilePath` | `P3` | 33 | 10 | `timeline-editing` | `conditional`(9), `time-range`(8), `null-check`(5), `empty-string-check`(1) | feature-specific or optional |
| `NvsClipAnimatedSticker.getOutPoint` | `P3` | 33 | 10 | `timeline-editing` | `time-range`(10), `conditional`(7), `null-check`(6), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsClipCaption.getControlPoint` | `P3` | 33 | 10 | `timeline-editing` | `conditional`(10), `time-range`(10), `null-check`(10) | requested feature may fail or degrade |
| `NvsClipCaption.setControlPoint` | `P3` | 33 | 10 | `timeline-editing` | `time-range`(7), `conditional`(3), `null-check`(3) | requested feature may fail or degrade |
| `NvsTimelineCaption.setDrawShadow` | `P3` | 33 | 10 | `timeline-editing` | `conditional`(6), `null-check`(2), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsAudioTrack.removeAllClips` | `P3` | 32 | 9 | `timeline-editing` | `conditional`(9), `null-check`(9), `time-range`(4), `empty-string-check`(3) | feature-specific or optional |
| `NvsClipCaption.getModularCaptionAnimationPackageId` | `P3` | 32 | 9 | `timeline-editing` | `conditional`(6), `empty-string-check`(6), `time-range`(4), `null-check`(1) | requested feature may fail or degrade |
| `NvsFx.setBooleanVal` | `P3` | 32 | 9 | `effects-transforms` | `conditional`(8), `null-check`(5) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.setScale` | `P3` | 32 | 9 | `timeline-editing` | `conditional`(4), `time-range`(3), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getRoleInTheme` | `P3` | 32 | 9 | `timeline-editing` | `conditional`(9), `null-check`(4), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setBold` | `P3` | 32 | 9 | `timeline-editing` | `conditional`(8), `null-check`(5), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setCaptionTranslation` | `P3` | 32 | 9 | `timeline-editing` | `conditional`(5), `null-check`(5), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setLetterSpacing` | `P3` | 32 | 9 | `timeline-editing` | `conditional`(7), `null-check`(6) | requested feature may fail or degrade |
| `NvsTimelineCaption.setZValue` | `P3` | 32 | 9 | `timeline-editing` | `conditional`(7), `null-check`(6), `time-range`(1) | requested feature may fail or degrade |
| `NvsVideoFx.setMenuVal` | `P3` | 32 | 9 | `effects-transforms` | `conditional`(9), `null-check`(5), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsAudioClip.appendFx` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(7), `null-check`(4), `time-range`(1) | requested feature may fail or degrade |
| `NvsAudioClip.getOutPoint` | `P3` | 31 | 7 | `timeline-editing` | `time-range`(7), `conditional`(5), `null-check`(1) | feature-specific or optional |
| `NvsAudioClip.setFadeInDuration` | `P3` | 31 | 7 | `timeline-editing` | `time-range`(7), `conditional`(6), `null-check`(6) | feature-specific or optional |
| `NvsAudioClip.setVolumeGain` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `time-range`(7), `null-check`(7) | feature-specific or optional |
| `NvsAudioFx.getBuiltinAudioFxName` | `P3` | 31 | 7 | `effects-transforms` | `conditional`(7), `null-check`(5), `empty-string-check`(2), `time-range`(1) | requested feature may fail or degrade |
| `NvsAudioTrack.setVolumeGain` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(6), `null-check`(6), `empty-string-check`(1), `time-range`(1) | feature-specific or optional |
| `NvsCaptureAnimatedSticker.getHorizontalFlip` | `P3` | 31 | 7 | `capture-recording` | `conditional`(7), `null-check`(6), `time-range`(1) | requested feature may fail or degrade |
| `NvsCaptureVideoFx.getBuiltinCaptureVideoFxName` | `P3` | 31 | 8 | `capture-recording` | `conditional`(8), `null-check`(4), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsCaptureVideoFx.getCaptureVideoFxPackageId` | `P3` | 31 | 7 | `capture-recording` | `conditional`(7), `null-check`(4), `empty-string-check`(3), `asset-package-result`(1) | requested feature may fail or degrade |
| `NvsCaptureVideoFx.getIndex` | `P3` | 31 | 8 | `capture-recording` | `conditional`(8), `null-check`(8), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.getAnimatedStickerOutAnimationPackageId` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(7), `empty-string-check`(6), `time-range`(5), `null-check`(3) | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.removeAllKeyframe` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `null-check`(4) | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.removeKeyframeAtTime` | `P3` | 31 | 8 | `timeline-editing` | `time-range`(8), `conditional`(3), `null-check`(1) | requested feature may fail or degrade |
| `NvsClipCaption.getBoundingRectangleVertices` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(7), `null-check`(7) | requested feature may fail or degrade |
| `NvsClipCaption.getRotationZ` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(4), `null-check`(3), `time-range`(2) | requested feature may fail or degrade |
| `NvsClipCaption.getScaleX` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(7), `null-check`(4), `time-range`(2) | requested feature may fail or degrade |
| `NvsClipCaption.getScaleY` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(6), `null-check`(5), `time-range`(2) | requested feature may fail or degrade |
| `NvsClipCaption.getTextAlignment` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(5), `null-check`(5), `time-range`(3), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsFx.getFloatVal` | `P3` | 31 | 8 | `effects-transforms` | `conditional`(7), `empty-string-check`(3), `null-check`(2) | requested feature may fail or degrade |
| `NvsMaskRegionInfo.addRegionInfo` | `P3` | 31 | 7 | `effects-transforms` | `conditional`(1), `null-check`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getAnimatedStickerOutAnimationPackageId` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(7), `empty-string-check`(6), `time-range`(5), `null-check`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getHorizontalFlip` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(5), `null-check`(4), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getScale` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(4), `null-check`(2), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getTranslation` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(4), `time-range`(3), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.removeAllKeyframe` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `null-check`(4) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.removeKeyframeAtTime` | `P3` | 31 | 8 | `timeline-editing` | `time-range`(8), `conditional`(3), `null-check`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.setVolumeGain` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(5), `null-check`(5) | requested feature may fail or degrade |
| `NvsTimelineCaption.getControlPoint` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `time-range`(8), `null-check`(8) | requested feature may fail or degrade |
| `NvsTimelineCaption.getModularCaptionOutAnimationDuration` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(7), `time-range`(7), `empty-string-check`(4), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.getOpacity` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(6), `null-check`(5), `time-range`(3) | requested feature may fail or degrade |
| `NvsTimelineCaption.getText` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(6), `null-check`(5), `time-range`(4), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.getTextColor` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(7), `null-check`(6), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setBackgroundColor` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `null-check`(5), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setControlPoint` | `P3` | 31 | 8 | `timeline-editing` | `time-range`(6), `conditional`(3), `null-check`(3) | requested feature may fail or degrade |
| `NvsTimelineCaption.setFontFamily` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(6), `empty-string-check`(4), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.setItalic` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(5), `null-check`(4) | requested feature may fail or degrade |
| `NvsTimelineCaption.setLineSpacing` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `null-check`(6), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setModularCaptionAnimationPeroid` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `time-range`(8), `empty-string-check`(5), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.setModularCaptionInAnimationDuration` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `time-range`(8), `empty-string-check`(4), `null-check`(3) | requested feature may fail or degrade |
| `NvsTimelineCaption.setModularCaptionOutAnimationDuration` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(8), `time-range`(8), `null-check`(2), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.setOutlineColor` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(7), `null-check`(4) | requested feature may fail or degrade |
| `NvsTimelineCaption.setOutlineWidth` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(7), `null-check`(5), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setScaleX` | `P3` | 31 | 7 | `timeline-editing` | `time-range`(1), `conditional`(1), `null-check`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setScaleY` | `P3` | 31 | 7 | `timeline-editing` | `conditional`(2), `null-check`(2), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimelineCaption.setShadowColor` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(3), `null-check`(1) | requested feature may fail or degrade |
| `NvsTimelineVideoFx.setBooleanVal` | `P3` | 31 | 8 | `timeline-editing` | `conditional`(6), `null-check`(6), `time-range`(5) | requested feature may fail or degrade |
| `NvsVideoEffect.setFloatVal` | `P3` | 31 | 7 | `effects-transforms` | `conditional`(6), `null-check`(6) | requested feature may fail or degrade |
| `NvsVideoFx.getSubType` | `P3` | 31 | 8 | `effects-transforms` | `conditional`(7), `null-check`(4) | requested feature may fail or degrade |
| `NvsVideoFx.setArbDataVal` | `P3` | 31 | 7 | `effects-transforms` | `conditional`(5), `null-check`(3) | requested feature may fail or degrade |
| `NvsVideoTransition.getVideoTransitionDuration` | `P3` | 31 | 8 | `timeline-editing` | `time-range`(8), `conditional`(6), `null-check`(6) | feature-specific or optional |
| `NvsVideoTransition.setVideoTransitionDuration` | `P3` | 31 | 7 | `timeline-editing` | `time-range`(7), `conditional`(6), `null-check`(3) | feature-specific or optional |
| `NvsClipCaption.getModularCaptionOutAnimationPackageId` | `P3` | 30 | 14 | `timeline-editing` | `conditional`(11), `empty-string-check`(11), `time-range`(6) | requested feature may fail or degrade |
| `NvsCaptureAnimatedSticker.getAttachment` | `P3` | 29 | 6 | `capture-recording` | `conditional`(6), `null-check`(6), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsCaptureAnimatedSticker.getBoundingRectangleVertices` | `P3` | 29 | 6 | `capture-recording` | `conditional`(6), `null-check`(5), `time-range`(1) | requested feature may fail or degrade |
| `NvsCaptureCompoundCaption.getAttachment` | `P3` | 29 | 6 | `capture-recording` | `conditional`(4), `null-check`(4), `empty-string-check`(3) | requested feature may fail or degrade |
| `NvsCaptureVideoFx.setStringVal` | `P3` | 29 | 6 | `capture-recording` | `conditional`(5), `null-check`(4) | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.getAnimatedStickerInAnimationPackageId` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(6), `empty-string-check`(5), `null-check`(4), `time-range`(3) | requested feature may fail or degrade |
| `NvsClipCaption.getTemplateAttachment` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(6), `time-range`(6), `null-check`(4), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsClipCaption.setModularCaptionInAnimationDuration` | `P3` | 29 | 6 | `timeline-editing` | `time-range`(6), `conditional`(5), `empty-string-check`(3), `null-check`(3) | requested feature may fail or degrade |
| `NvsClipCaption.setModularCaptionOutAnimationDuration` | `P3` | 29 | 6 | `timeline-editing` | `time-range`(6), `conditional`(5), `null-check`(2), `empty-string-check`(1) | requested feature may fail or degrade |
| `NvsFx.getStringVal` | `P3` | 29 | 6 | `effects-transforms` | `conditional`(5), `null-check`(3), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsFx.setIntVal` | `P3` | 29 | 6 | `effects-transforms` | `conditional`(6), `null-check`(1) | requested feature may fail or degrade |
| `NvsFx.setStringVal` | `P3` | 29 | 6 | `effects-transforms` | `conditional`(5), `null-check`(2), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getAnimatedStickerInAnimationPackageId` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(6), `empty-string-check`(5), `time-range`(3), `null-check`(3) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getRotationZ` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(3), `null-check`(2), `time-range`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.getVolumeGain` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(5), `null-check`(4) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.setCurrentKeyFrameTime` | `P3` | 29 | 6 | `timeline-editing` | `time-range`(4), `conditional`(2), `empty-string-check`(1), `null-check`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.setHorizontalFlip` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(3), `null-check`(3) | requested feature may fail or degrade |
| `NvsTimelineCaption.getCategory` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(6), `null-check`(4) | requested feature may fail or degrade |
| `NvsTimelineCaption.getModularCaptionInAnimationDuration` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(6), `time-range`(6), `empty-string-check`(4), `null-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.removeAllKeyframe` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(3), `null-check`(3) | requested feature may fail or degrade |
| `NvsTimelineCaption.setFontByFilePath` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(5), `null-check`(3), `empty-string-check`(2) | requested feature may fail or degrade |
| `NvsTimelineCaption.setFontSize` | `P3` | 29 | 6 | `timeline-editing` | `conditional`(4), `null-check`(4) | requested feature may fail or degrade |
| `NvsCaptionSpan.getEnd` | `P3` | 25 | 8 | `captions-stickers` | `conditional`(8) | requested feature may fail or degrade |
| `NvsCaptionSpan.setEnd` | `P3` | 25 | 7 | `captions-stickers` | `conditional`(6) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.setRotationZ` | `P3` | 25 | 7 | `timeline-editing` | `time-range`(3), `conditional`(1) | requested feature may fail or degrade |
| `NvsTimelineAnimatedSticker.setTranslation` | `P3` | 25 | 7 | `timeline-editing` | `time-range`(2) | requested feature may fail or degrade |

## Direct Member/Static Token Priority Map

| Token | Priority | Score | Occurrences | Method snippet | Expanded | Missing impact |
| --- | --- | ---: | ---: | --- | --- | --- |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK` | `P0` | 94 | 84 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING` | `P1` | 80 | 15 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.getInstance` | `P1` | 80 | 139 | yes | yes | project/core flow fails |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW` | `P1` | 76 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER` | `P1` | 75 | 7 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720` | `P1` | 74 | 6 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM` | `P1` | 74 | 6 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER` | `P1` | 74 | 65 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH` | `P1` | 73 | 5 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE` | `P1` | 73 | 5 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME` | `P1` | 71 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME` | `P1` | 71 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE` | `P1` | 71 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE` | `P1` | 71 | 43 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080` | `P2` | 69 | 3 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING` | `P2` | 69 | 3 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED` | `P2` | 69 | 3 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.COMPILE_USE_OPERATING_RATE` | `P2` | 67 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME` | `P2` | 67 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER` | `P2` | 67 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360` | `P2` | 67 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480` | `P2` | 67 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO` | `P2` | 67 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER` | `P2` | 67 | 26 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.COMPILE_BITRATE` | `P2` | 64 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_2160` | `P2` | 64 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_SOFTWARE_VIDEO_INTRA_FRAME_ONLY_FAST_STOP` | `P2` | 64 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc` | `P2` | 63 | 66 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.PlaybackCallback` | `P2` | 63 | 16 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING` | `P2` | 63 | 16 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.StreamingEngineCallback` | `P2` | 63 | 16 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.PlaybackCallback2` | `P2` | 62 | 14 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContextUtil.getInstance` | `P2` | 62 | 15 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.CompileCallback` | `P2` | 60 | 11 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME` | `P2` | 59 | 9 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.getAVInfoFromFile` | `P2` | 59 | 9 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.CompileCallback2` | `P2` | 58 | 8 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.ImageGrabberCallback` | `P2` | 58 | 8 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.hasARModule` | `P2` | 58 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.CaptureDeviceCapability` | `P2` | 57 | 7 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME` | `P2` | 57 | 7 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX` | `P2` | 56 | 28 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE` | `P2` | 56 | 6 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | `P2` | 56 | 6 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | `P2` | 55 | 5 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | `P2` | 55 | 5 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.initHumanDetectionExt` | `P2` | 55 | 5 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.templateFootageInfo` | `P2` | 55 | 5 | yes | yes | feature-specific or optional |
| `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT` | `P2` | 55 | 5 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.COMPILE_BITRATE_GRADE_MEDIUM` | `P2` | 54 | 1 | no | yes | feature-specific or optional |
| `NvsStreamingContext.COMPILE_FPS` | `P2` | 54 | 1 | no | yes | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_ENABLE_TAKE_PICTURE` | `P2` | 54 | 1 | no | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_IGNORE_VIDEO_ROTATION` | `P2` | 54 | 1 | no | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME` | `P2` | 53 | 4 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.SdkVersion` | `P2` | 53 | 4 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH` | `P2` | 53 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER` | `P2` | 51 | 14 | yes | yes | requested feature may fail or degrade |
| `NvsEffectSdkContext.getInstance` | `P2` | 51 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_SPEED_COMP_MODE` | `P2` | 51 | 3 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.SeekingCallback` | `P2` | 51 | 3 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE` | `P2` | 51 | 3 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.class` | `P2` | 51 | 3 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.setupHumanDetectionData` | `P2` | 51 | 3 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH` | `P2` | 49 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE` | `P2` | 49 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION` | `P2` | 49 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK` | `P2` | 49 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION` | `P2` | 49 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK` | `P2` | 49 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE` | `P2` | 49 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND` | `P2` | 49 | 2 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT` | `P2` | 49 | 2 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE` | `P2` | 49 | 2 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_LOW_PIPELINE_SIZE` | `P2` | 49 | 2 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_EXTREMELY_HIGH` | `P2` | 49 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH` | `P2` | 49 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.init` | `P2` | 49 | 2 | yes | yes | project/core flow fails |
| `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT` | `P2` | 48 | 9 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.VIDEO_CLIP_TYPE_AV` | `P2` | 48 | 10 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED` | `P2` | 47 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR` | `P2` | 47 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE` | `P2` | 47 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE` | `P2` | 47 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION` | `P2` | 47 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateCaptionDesc` | `P2` | 47 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo` | `P2` | 47 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateFootageDesc` | `P2` | 47 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.CaptureRecordingDurationCallback` | `P2` | 47 | 7 | no | yes | requested feature may fail or degrade |
| `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE` | `P2` | 47 | 8 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsAIContext.getInstance` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsAIContext.init` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.CaptureDeviceCallback` | `P2` | 46 | 6 | no | yes | requested feature may fail or degrade |
| `NvsStreamingContext.CaptureRecordingStartedCallback` | `P2` | 46 | 6 | no | yes | requested feature may fail or degrade |
| `NvsStreamingContext.DEVICE_POWER_LEVEL_LOW` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.HardwareErrorCallback` | `P2` | 46 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.RECORD_GOP_SIZE` | `P2` | 46 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED` | `P2` | 46 | 1 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_CONTEXT_FLAG_INTERRUPT_STOP_FOR_INTERNAL_STOP` | `P2` | 46 | 1 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.STREAMING_CONTEXT_FLAG_NEED_GIF_MOTION` | `P2` | 46 | 1 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_ALIGN_VIDEO_SIZE` | `P2` | 46 | 1 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_HARDWARE_ENCODER` | `P2` | 46 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsStreamingContext.WebCallback` | `P2` | 46 | 1 | yes | yes | state/error handling becomes fragile |
| `NvsStreamingContext.closeHumanDetection` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.initHumanDetection` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.setIconSize` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.setMaxReaderCount` | `P2` | 46 | 1 | yes | yes | feature-specific or optional |
| `NvsTimeline.NvsTimelineWatermarkPosition_TopLeft` | `P2` | 46 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsTimeline.NvsTimelineWatermarkPosition_TopRight` | `P2` | 46 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAVFileInfo.AV_FILE_TYPE_IMAGE` | `P2` | 45 | 6 | yes | yes | feature-specific or optional |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME` | `P2` | 45 | 6 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.AssetPackageManagerCallback` | `P2` | 45 | 6 | yes | yes | requested feature may fail or degrade |
| `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN` | `P2` | 45 | 6 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH` | `P3` | 44 | 5 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP` | `P3` | 44 | 5 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP` | `P3` | 44 | 5 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.AspectRatio` | `P3` | 44 | 35 | yes | yes | feature-specific or optional |
| `NvsLiveWindow.HDR_DISPLAY_MODE_SDR` | `P3` | 44 | 5 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE` | `P3` | 42 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION` | `P3` | 42 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc` | `P3` | 42 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsMultiThumbnailSequenceView.OnScrollChangeListener` | `P3` | 42 | 4 | yes | yes | feature-specific or optional |
| `NvsServerClient.get` | `P3` | 41 | 23 | yes | yes | feature-specific or optional |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0` | `P3` | 40 | 3 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.IMAGE_CLIP_MOTIONMMODE_ROI` | `P3` | 40 | 3 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST` | `P3` | 39 | 18 | yes | yes | feature-specific or optional |
| `NvsStreamingContext.AV_FILEINFO_EXTRA_INFO` | `P3` | 39 | 2 | no | yes | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_AVATAR_EXPRESSION` | `P3` | 39 | 2 | no | yes | requested feature may fail or degrade |
| `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_16_BIT_FLOAT` | `P3` | 39 | 2 | no | yes | timeline/preview/edit flow incomplete |
| `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_AUTO` | `P3` | 39 | 2 | no | yes | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_ANIMATION` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_CONTEXT` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_IN_ANIMATION` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_OUT_ANIMATION` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_AUDIO` | `P3` | 38 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsFxDescription.ParamInfoObject` | `P3` | 38 | 17 | yes | yes | requested feature may fail or degrade |
| `NvsUtils.checkFunctionInMainThread` | `P3` | 38 | 16 | yes | yes | feature-specific or optional |
| `NvsVideoClip.ClIP_BACKGROUNDMODE_BLUR` | `P3` | 38 | 2 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180` | `P3` | 38 | 2 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270` | `P3` | 38 | 2 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90` | `P3` | 38 | 2 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ROLE_IN_THEME_TITLE` | `P3` | 38 | 2 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ROLE_IN_THEME_TRAILER` | `P3` | 38 | 2 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsMaskRegionInfo.RegionInfo` | `P3` | 37 | 15 | yes | yes | feature-specific or optional |
| `NvsEffectSdkContext.init` | `P3` | 36 | 1 | no | yes | requested feature may fail or degrade |
| `NvsStreamingContext.CapturedPictureCallback` | `P3` | 36 | 1 | no | yes | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK` | `P3` | 36 | 1 | no | yes | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_SKY` | `P3` | 36 | 1 | no | yes | feature-specific or optional |
| `NvsStreamingContext.close` | `P3` | 36 | 1 | no | yes | feature-specific or optional |
| `NvsAVFileInfo.AV_FILE_TYPE_AUDIOVIDEO` | `P3` | 35 | 1 | yes | yes | feature-specific or optional |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_16v9` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_18v9` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_1v1` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_3v4` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_4v3` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_9v16` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_9v18` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_FREEZE_FRAME` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_IMAGE` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_VIDEO` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_VIDEO_IMAGE` | `P3` | 35 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE` | `P3` | 35 | 11 | yes | yes | requested feature may fail or degrade |
| `NvsLiveWindow.FILLMODE_PRESERVEASPECTCROP` | `P3` | 35 | 1 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE` | `P3` | 35 | 1 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID` | `P3` | 35 | 1 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME` | `P3` | 35 | 1 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE` | `P3` | 35 | 1 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_REPLACE_ID` | `P3` | 35 | 1 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsConstants.ADJUST_TINT` | `P3` | 34 | 9 | yes | yes | feature-specific or optional |
| `NvsConstants.POST_PACKAGE_ID` | `P3` | 34 | 9 | yes | yes | requested feature may fail or degrade |
| `NvsTimelineCaption.THEME_CATEGORY` | `P3` | 34 | 9 | yes | yes | requested feature may fail or degrade |
| `NvsTimelineEditor.OnScrollChangeListener` | `P3` | 34 | 10 | yes | yes | feature-specific or optional |
| `NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D` | `P3` | 33 | 8 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_VIDEO_MODE` | `P3` | 33 | 8 | yes | yes | feature-specific or optional |
| `NvsTimelineCaption.ROLE_IN_THEME_GENERAL` | `P3` | 33 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME` | `P3` | 33 | 8 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.KEY_MASK_GENERATOR` | `P3` | 32 | 7 | yes | yes | feature-specific or optional |
| `NvsTimelineTimeSpan.OnTrimInChangeListener` | `P3` | 32 | 7 | yes | yes | feature-specific or optional |
| `NvsTimelineTimeSpan.OnTrimOutChangeListener` | `P3` | 32 | 7 | yes | yes | feature-specific or optional |
| `NvsVideoStreamInfo.VIDEO_ROTATION_270` | `P3` | 32 | 7 | yes | yes | feature-specific or optional |
| `NvsVideoStreamInfo.VIDEO_ROTATION_90` | `P3` | 32 | 7 | yes | yes | feature-specific or optional |
| `NvsCaptureSceneInfo.ClipData` | `P3` | 31 | 6 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN` | `P3` | 31 | 6 | yes | yes | feature-specific or optional |
| `NvsConstants.IS_POST_STORY_BOARD_3D` | `P3` | 31 | 6 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.KEY_MASK_GENERATOR_TYPE` | `P3` | 31 | 6 | yes | yes | feature-specific or optional |
| `NvsConstants.PACKAGE_EFFECT_IN` | `P3` | 31 | 6 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.PACKAGE_EFFECT_OUT` | `P3` | 31 | 6 | yes | yes | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.getInPoint` | `P3` | 30 | 5 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.Crop` | `P3` | 30 | 5 | yes | yes | feature-specific or optional |
| `NvsMultiThumbnailSequenceView.THUMBNAIL_IMAGE_FILLMODE_ASPECTCROP` | `P3` | 30 | 3 | no | yes | feature-specific or optional |
| `NvsVideoFx.VIDEOFX_TYPE_BUILTIN` | `P3` | 30 | 5 | yes | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_NORMAL_TEXT` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_OUTLINE_WIDTH` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_RENDER_ID` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.removeKeyframeAtTime` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_MODE` | `P3` | 28 | 4 | yes | yes | feature-specific or optional |
| `NvsEffectSdkContext.initHumanDetectionExt` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsExpressionParam.TYPE_COLOR` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsLiveWindow.HDR_DISPLAY_MODE_DEPEND_DEVICE` | `P3` | 28 | 2 | no | yes | timeline/preview/edit flow incomplete |
| `NvsLiveWindow.HDR_DISPLAY_MODE_TONE_MAP_SDR` | `P3` | 28 | 2 | no | yes | timeline/preview/edit flow incomplete |
| `NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON` | `P3` | 28 | 4 | yes | yes | feature-specific or optional |
| `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR` | `P3` | 28 | 4 | yes | yes | state/error handling becomes fragile |
| `NvsMediaFileConvertor.MeidaFileConvertorCallback` | `P3` | 28 | 4 | yes | yes | state/error handling becomes fragile |
| `NvsObject.TEMPLATE_KEY_BEST_SEEK_TIME` | `P3` | 28 | 4 | yes | yes | timeline/preview/edit flow incomplete |
| `NvsTimelineCaption.TEXT_ALIGNMENT_CENTER` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsTimelineCaption.TEXT_ALIGNMENT_LEFT` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT` | `P3` | 28 | 4 | yes | yes | requested feature may fail or degrade |
| `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE` | `P3` | 28 | 4 | yes | yes | feature-specific or optional |
| `NvsCaptionSpan.SPAN_TYPE_COLOR` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsClipCaption.ROLE_IN_THEME_GENERAL` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsClipCaption.THEME_CATEGORY` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.ADJUST_AMOUNT` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ADJUST_BLACKPOINT` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ADJUST_BRIGHTNESS` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ADJUST_CONTRAST` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ADJUST_DEGREE` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ADJUST_HIGHTLIGHT` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ADJUST_SATURATION` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ADJUST_SHADOW` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ADJUST_TEMPERATURE` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.ANIMATION_POST_PACKAGE_ID` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_RIGHT_GAIN` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.CUT_FX_TYPE_FOR_TRANSFORM` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.FX_SHARPEN` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.FX_VIGNETTE` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.KEY_CROPPER_SCALE_X` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_SCALE_Y` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsEffectSdkContext.setupHumanDetectionData` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsExpressionParam.FloatParam` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsExpressionParam.IntParam` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsExpressionParam.TYPE_BOOLEAN` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsExpressionParam.TYPE_FLOAT` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsExpressionParam.TYPE_INT` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsObject.TEMPLATE_KEY_FX_GROUP` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsObject.TEMPLATE_KEY_REPLACE_ID` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsPassthroughConvertor.NvsPassthroughFileInfo` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsTimelineCaption.ROLE_IN_THEME_TITLE` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsTimelineTimeSpanExt.OnMarginChangeListener` | `P3` | 26 | 3 | yes | yes | requested feature may fail or degrade |
| `NvsVideoStreamInfo.VIDEO_ROTATION_180` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH` | `P3` | 26 | 3 | yes | yes | feature-specific or optional |
| `NvsAVFileInfo.AV_FILE_INFO_FLAGS_HAS_VIDEO_PART_IN_IMAGE` | `P3` | 25 | 1 | no | yes | requested feature may fail or degrade |
| `NvsAVFileInfo.ExtendsDataInfo` | `P3` | 25 | 1 | no | yes | feature-specific or optional |
| `NvsAssetPackageManager.ARSceneCameraPreset` | `P3` | 25 | 1 | no | yes | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_WORKING_INPROGRESS` | `P3` | 25 | 1 | no | yes | requested feature may fail or degrade |
| `NvsARSceneManipulate.CheckedFunctionType_Matte` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsARSceneManipulate.NvsFaceFeatureInfo` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsCaption.BOUNDING_TYPE_TEXT` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_ITALIC` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_OPACITY` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_UNDERLINE` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsCaptureSceneInfo.CAPTURESCENE_INFO_IMAGE_FILLMODE_CROP` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.ANIMATION_PACKAGE_ID` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.CUT_KEY_IS_NORMALIZED_COORD` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.CUT_KEY_MASK_GENERATOR` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_ROTATION` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_TRANS_X` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_TRANS_Y` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_CROP_FULL_TRANSFORM` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_MASK_GENERATOR_SIGN_MASK` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_MASK_STORYBOARD_DESC` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.PROPERTY_FX` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_COLOR` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_IMAGE` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_VALUE_BACKGROUND_COLOR_SOLID` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.SIZE_4K_HEIGHT` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.SIZE_4K_WIDTH` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.VALUE_CROP_FULL_TRANSFORM` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsFaceDetector.NvsFaceData` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsMaskRegionInfo.Transform2D` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsTimelineTimeSpan.OnMarginChangeListener` | `P3` | 24 | 2 | yes | yes | requested feature may fail or degrade |
| `NvsTimelineTimeSpanExt.OnTrimInChangeListener` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsTimelineTimeSpanExt.OnTrimOutChangeListener` | `P3` | 24 | 2 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_BACKGROUND_MODE` | `P3` | 22 | 7 | no | yes | feature-specific or optional |
| `NvsARSceneManipulate.NvsARSceneManipulateCallback` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsARSceneManipulate.NvsFaceBoundingRectInfo` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsARSceneManipulate.NvsHandFeatureInfo` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_ID` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NAME` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TAGS` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TYPE` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsCaption.BOUNDING_TYPE_FRAME` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.getZValue` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsClipAnimatedSticker.setCurrentKeyFrameTime` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.ANIMATION_ENABLE_MUTLISAMPLE` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.ANIMATION_IS_POST_STORYBOARD_3D` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.ANIMATION_PACKAGE_EFFECT_IN` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.ANIMATION_PACKAGE_EFFECT_OUT` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsConstants.KEY_BACKGROUND_COLOR` | `P3` | 21 | 6 | no | yes | feature-specific or optional |
| `NvsConstants.KEY_MASK_FEATHER_WIDTH` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_MASK_GENERATOR_SIGN_CROP` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_MASK_INVERSE_REGION` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_MASK_KEEP_RGB` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_MASK_REGION_INFO` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_BLUR_RADIUS` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_ROTATION` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_SCALE_X` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_SCALE_Y` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_TRANS_X` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_TRANS_Y` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR_NEW_MODE_ENABLE` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_VALUE_BACKGROUND_IMAGE_FILE` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsEffectSdkContext.initHumanDetection` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsFaceDetector.AI_SDK_DETECTION_BUFFER_FORMAT_RGBA` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_VIDEO_MODE` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsFaceDetector.createNvsFaceDetector` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsMaskRegionInfo.Ellipse2D` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsMaskRegionInfo.MASK_REGION_TYPE_ELLIPSE2D` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsMediaFileConvertor.CONVERTOR_ENABLE_HDR` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsTimelineCaption.ROLE_IN_THEME_TRAILER` | `P3` | 21 | 1 | yes | yes | requested feature may fail or degrade |
| `NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsVideoFrameRetriever.VIDEO_FRAME_HEIGHT_GRADE_720` | `P3` | 21 | 1 | yes | yes | feature-specific or optional |
| `NvsConstants.KEY_BACKGROUND_BLUR_RADIUS` | `P3` | 20 | 5 | no | yes | feature-specific or optional |
| `NvsConstants.VALUE_COLOR_BACKGROUND_MODE` | `P3` | 20 | 5 | no | yes | feature-specific or optional |
| `NvsCaptionSpan.SPAN_TYPE_FONT_FAMILY` | `P3` | 18 | 4 | no | yes | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_ROTATION` | `P3` | 18 | 4 | no | yes | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_SCALE_X` | `P3` | 18 | 4 | no | yes | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_SCALE_Y` | `P3` | 18 | 4 | no | yes | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_TRANS_X` | `P3` | 18 | 4 | no | yes | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_TRANS_Y` | `P3` | 18 | 4 | no | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_OUTLINE_COLOR` | `P3` | 16 | 3 | no | yes | requested feature may fail or degrade |
| `NvsConstants.KEY_BACKGROUND_IMAGE_PATH` | `P3` | 16 | 3 | no | yes | feature-specific or optional |
| `NvsConstants.KEY_BACKGROUND_ROTATION` | `P3` | 16 | 3 | no | yes | feature-specific or optional |
| `NvsConstants.POST_PACKAGE_ID_OLD` | `P3` | 16 | 3 | no | yes | requested feature may fail or degrade |
| `NvsVideoFx.VIDEOFX_TYPE_PACKAGE` | `P3` | 16 | 3 | no | yes | requested feature may fail or degrade |
| `NvsVideoStreamInfo.VIDEO_ROTATION_0` | `P3` | 16 | 3 | no | yes | feature-specific or optional |
| `NvsConstants.FX_TRANSFORM_2D` | `P3` | 14 | 2 | no | yes | requested feature may fail or degrade |
| `NvsConstants.KEY_CROPPER_ASSET_ASPECT_RATIO` | `P3` | 14 | 2 | no | yes | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_RATIO` | `P3` | 14 | 2 | no | yes | feature-specific or optional |
| `NvsConstants.PROPERTY_OPACITY` | `P3` | 14 | 2 | no | yes | feature-specific or optional |
| `NvsConstants.VALUE_CROPPER_FREE` | `P3` | 14 | 2 | no | yes | feature-specific or optional |
| `NvsConstants.VALUE_IMAGE_BACKGROUND_MODE` | `P3` | 14 | 2 | no | yes | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_180` | `P3` | 14 | 2 | no | yes | feature-specific or optional |
| `NvsIconGenerator.IconCallback` | `P3` | 14 | 2 | no | yes | state/error handling becomes fragile |
| `NvsVideoTransition.VIDEO_TRANSITION_TYPE_BUILTIN` | `P3` | 14 | 2 | no | yes | feature-specific or optional |
| `NvsVideoTransition.VIDEO_TRANSITION_TYPE_PACKAGE` | `P3` | 14 | 2 | no | yes | requested feature may fail or degrade |
| `NvsAssetPackageParticleDescParser.PARTICLE_TYPE_NORMAL` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsAssetPackageParticleDescParser.PARTICLE_TYPE_TOUCH` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_BODY_OPACITY` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_FONT_SIZE_RATIO` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_OUTLINE_OPACITY` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsConstants.KEY_BACKGROUND_MUTLISAMPLE` | `P3` | 11 | 1 | no | yes | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_KEEP_RGB` | `P3` | 11 | 1 | no | yes | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_REGION_INFO` | `P3` | 11 | 1 | no | yes | feature-specific or optional |
| `NvsConstants.VALUE_BLUR_BACKGROUND_MODE` | `P3` | 11 | 1 | no | yes | feature-specific or optional |
| `NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsEffectSdkContext.class` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsEffectSdkContext.close` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_0` | `P3` | 11 | 1 | no | yes | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_270` | `P3` | 11 | 1 | no | yes | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_90` | `P3` | 11 | 1 | no | yes | feature-specific or optional |
| `NvsPassthroughConvertor.PassthroughConvertorCallback` | `P3` | 11 | 1 | no | yes | state/error handling becomes fragile |
| `NvsTimelineVideoFx.TIMELINE_VIDEOFX_TYPE_BUILTIN` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsTimelineVideoFx.TIMELINE_VIDEOFX_TYPE_PACKAGE` | `P3` | 11 | 1 | no | yes | requested feature may fail or degrade |
| `NvsVideoFrameRetriever.VIDEO_FRAME_HEIGHT_GRADE_480` | `P3` | 11 | 1 | no | yes | feature-specific or optional |

## Constant/Type Priority Map

| Token | Priority | Score | Kind | Occurrences | Missing impact |
| --- | --- | ---: | --- | ---: | --- |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK` | `P1` | 83 | `engine-state` | 85 | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING` | `P1` | 70 | `engine-state` | 15 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW` | `P2` | 65 | `engine-state` | 8 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER` | `P2` | 64 | `capture-flag` | 7 | requested feature may fail or degrade |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720` | `P2` | 63 | `compile-option` | 6 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM` | `P2` | 63 | `compile-option` | 6 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH` | `P2` | 62 | `compile-option` | 5 | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE` | `P2` | 62 | `engine-state` | 5 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME` | `P2` | 61 | `capture-flag` | 4 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO` | `P2` | 61 | `capture-flag` | 4 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME` | `P2` | 61 | `capture-flag` | 4 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE` | `P2` | 61 | `capture-flag` | 4 | requested feature may fail or degrade |
| `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc` | `P2` | 59 | `nested-type/callback` | 66 | state/error handling becomes fragile |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080` | `P2` | 59 | `compile-option` | 3 | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING` | `P2` | 59 | `engine-state` | 3 | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED` | `P2` | 59 | `engine-state` | 3 | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.PlaybackCallback` | `P2` | 58 | `nested-type/callback` | 16 | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.StreamingEngineCallback` | `P2` | 58 | `nested-type/callback` | 16 | state/error handling becomes fragile |
| `NvsStreamingContext.COMPILE_USE_OPERATING_RATE` | `P2` | 57 | `compile-option` | 2 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME` | `P2` | 57 | `compile-option` | 2 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER` | `P2` | 57 | `compile-option` | 2 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360` | `P2` | 57 | `compile-option` | 2 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480` | `P2` | 57 | `compile-option` | 2 | feature-specific or optional |
| `NvsStreamingContext.PlaybackCallback2` | `P2` | 57 | `nested-type/callback` | 14 | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.CompileCallback` | `P2` | 56 | `nested-type/callback` | 11 | state/error handling becomes fragile |
| `NvsStreamingContext.COMPILE_BITRATE` | `P2` | 53 | `compile-option` | 1 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_BITRATE_GRADE_MEDIUM` | `P2` | 53 | `compile-option` | 1 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_FPS` | `P2` | 53 | `compile-option` | 1 | feature-specific or optional |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_2160` | `P2` | 53 | `compile-option` | 1 | feature-specific or optional |
| `NvsStreamingContext.CompileCallback2` | `P2` | 53 | `nested-type/callback` | 8 | state/error handling becomes fragile |
| `NvsStreamingContext.ImageGrabberCallback` | `P2` | 53 | `nested-type/callback` | 8 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_ENABLE_TAKE_PICTURE` | `P2` | 53 | `capture-flag` | 1 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_IGNORE_VIDEO_ROTATION` | `P2` | 53 | `recording-flag` | 1 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_SOFTWARE_VIDEO_INTRA_FRAME_ONLY_FAST_STOP` | `P2` | 53 | `recording-flag` | 1 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX` | `P2` | 52 | `asset-package-type` | 28 | requested feature may fail or degrade |
| `NvsStreamingContext.CaptureDeviceCapability` | `P2` | 52 | `nested-type/callback` | 7 | requested feature may fail or degrade |
| `NvsStreamingContext.CaptureRecordingDurationCallback` | `P2` | 52 | `nested-type/callback` | 7 | requested feature may fail or degrade |
| `NvsStreamingContext.CaptureDeviceCallback` | `P2` | 51 | `nested-type/callback` | 6 | requested feature may fail or degrade |
| `NvsStreamingContext.CaptureRecordingStartedCallback` | `P2` | 51 | `nested-type/callback` | 6 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER` | `P2` | 51 | `constant` | 65 | requested feature may fail or degrade |
| `NvsStreamingContext.SdkVersion` | `P2` | 49 | `nested-type/callback` | 4 | state/error handling becomes fragile |
| `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE` | `P2` | 48 | `constant` | 43 | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER` | `P2` | 47 | `asset-package-type` | 14 | requested feature may fail or degrade |
| `NvsStreamingContext.SeekingCallback` | `P2` | 47 | `nested-type/callback` | 3 | timeline/preview/edit flow incomplete |
| `NvsConstants.AspectRatio` | `P2` | 46 | `nested-type/callback` | 35 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER` | `P3` | 44 | `constant` | 26 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED` | `P3` | 43 | `asset-package-error` | 8 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR` | `P3` | 43 | `asset-package-error` | 8 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE` | `P3` | 43 | `asset-package-type` | 8 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE` | `P3` | 43 | `asset-package-type` | 8 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION` | `P3` | 43 | `asset-package-type` | 8 | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateCaptionDesc` | `P3` | 43 | `nested-type/callback` | 8 | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo` | `P3` | 43 | `nested-type/callback` | 8 | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateFootageDesc` | `P3` | 43 | `nested-type/callback` | 8 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME` | `P3` | 41 | `asset-package-type` | 6 | requested feature may fail or degrade |
| `NvsAssetPackageManager.AssetPackageManagerCallback` | `P3` | 41 | `nested-type/callback` | 6 | requested feature may fail or degrade |
| `NvsFxDescription.ParamInfoObject` | `P3` | 41 | `nested-type/callback` | 17 | requested feature may fail or degrade |
| `NvsStreamingContext.CapturedPictureCallback` | `P3` | 41 | `nested-type/callback` | 1 | requested feature may fail or degrade |
| `NvsStreamingContext.HardwareErrorCallback` | `P3` | 41 | `nested-type/callback` | 1 | requested feature may fail or degrade |
| `NvsStreamingContext.WebCallback` | `P3` | 41 | `nested-type/callback` | 1 | state/error handling becomes fragile |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE` | `P3` | 40 | `asset-package-type` | 5 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH` | `P3` | 40 | `asset-package-type` | 5 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP` | `P3` | 40 | `asset-package-type` | 5 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP` | `P3` | 40 | `asset-package-type` | 5 | requested feature may fail or degrade |
| `NvsMaskRegionInfo.RegionInfo` | `P3` | 40 | `nested-type/callback` | 15 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING` | `P3` | 40 | `constant` | 16 | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION` | `P3` | 39 | `asset-package-type` | 4 | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc` | `P3` | 39 | `nested-type/callback` | 4 | requested feature may fail or degrade |
| `NvsMultiThumbnailSequenceView.OnScrollChangeListener` | `P3` | 39 | `nested-type/callback` | 4 | state/error handling becomes fragile |
| `NvsTimelineEditor.OnScrollChangeListener` | `P3` | 37 | `nested-type/callback` | 10 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME` | `P3` | 36 | `constant` | 9 | timeline/preview/edit flow incomplete |
| `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED` | `P3` | 35 | `asset-package-status` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION` | `P3` | 35 | `asset-package-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION` | `P3` | 35 | `asset-package-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION` | `P3` | 35 | `asset-package-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_ANIMATION` | `P3` | 35 | `asset-package-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_CONTEXT` | `P3` | 35 | `asset-package-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_IN_ANIMATION` | `P3` | 35 | `asset-package-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_OUT_ANIMATION` | `P3` | 35 | `asset-package-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER` | `P3` | 35 | `asset-package-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc` | `P3` | 35 | `nested-type/callback` | 2 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME` | `P3` | 34 | `constant` | 7 | timeline/preview/edit flow incomplete |
| `NvsTimelineTimeSpan.OnTrimInChangeListener` | `P3` | 34 | `nested-type/callback` | 7 | state/error handling becomes fragile |
| `NvsTimelineTimeSpan.OnTrimOutChangeListener` | `P3` | 34 | `nested-type/callback` | 7 | state/error handling becomes fragile |
| `NvsCaptureSceneInfo.ClipData` | `P3` | 33 | `nested-type/callback` | 6 | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE` | `P3` | 33 | `human-detection` | 6 | feature-specific or optional |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | `P3` | 33 | `constant` | 6 | timeline/preview/edit flow incomplete |
| `NvsConstants.Crop` | `P3` | 32 | `nested-type/callback` | 5 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | `P3` | 32 | `constant` | 5 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | `P3` | 32 | `constant` | 5 | timeline/preview/edit flow incomplete |
| `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT` | `P3` | 32 | `constant` | 5 | timeline/preview/edit flow incomplete |
| `NvsAVFileInfo.ExtendsDataInfo` | `P3` | 31 | `nested-type/callback` | 1 | state/error handling becomes fragile |
| `NvsAssetPackageManager.ARSceneCameraPreset` | `P3` | 31 | `nested-type/callback` | 1 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_WORKING_INPROGRESS` | `P3` | 31 | `asset-package-error` | 1 | requested feature may fail or degrade |
| `NvsMediaFileConvertor.MeidaFileConvertorCallback` | `P3` | 31 | `nested-type/callback` | 4 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME` | `P3` | 31 | `constant` | 4 | state/error handling becomes fragile |
| `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH` | `P3` | 31 | `constant` | 4 | requested feature may fail or degrade |
| `NvsExpressionParam.FloatParam` | `P3` | 29 | `nested-type/callback` | 3 | requested feature may fail or degrade |
| `NvsExpressionParam.IntParam` | `P3` | 29 | `nested-type/callback` | 3 | requested feature may fail or degrade |
| `NvsPassthroughConvertor.NvsPassthroughFileInfo` | `P3` | 29 | `nested-type/callback` | 3 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_SPEED_COMP_MODE` | `P3` | 29 | `constant` | 3 | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE` | `P3` | 29 | `constant` | 3 | feature-specific or optional |
| `NvsTimelineTimeSpanExt.OnMarginChangeListener` | `P3` | 29 | `nested-type/callback` | 3 | requested feature may fail or degrade |
| `NvsARSceneManipulate.NvsFaceFeatureInfo` | `P3` | 27 | `nested-type/callback` | 2 | requested feature may fail or degrade |
| `NvsFaceDetector.NvsFaceData` | `P3` | 27 | `nested-type/callback` | 2 | state/error handling becomes fragile |
| `NvsIconGenerator.IconCallback` | `P3` | 27 | `nested-type/callback` | 2 | state/error handling becomes fragile |
| `NvsMaskRegionInfo.Transform2D` | `P3` | 27 | `nested-type/callback` | 2 | state/error handling becomes fragile |
| `NvsStreamingContext.AV_FILEINFO_EXTRA_INFO` | `P3` | 27 | `constant` | 2 | feature-specific or optional |
| `NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH` | `P3` | 27 | `constant` | 2 | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE` | `P3` | 27 | `human-detection` | 2 | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_AVATAR_EXPRESSION` | `P3` | 27 | `human-detection` | 2 | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION` | `P3` | 27 | `human-detection` | 2 | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK` | `P3` | 27 | `human-detection` | 2 | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION` | `P3` | 27 | `human-detection` | 2 | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK` | `P3` | 27 | `human-detection` | 2 | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE` | `P3` | 27 | `human-detection` | 2 | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND` | `P3` | 27 | `human-detection` | 2 | feature-specific or optional |
| `NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT` | `P3` | 27 | `constant` | 2 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE` | `P3` | 27 | `constant` | 2 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_LOW_PIPELINE_SIZE` | `P3` | 27 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_EXTREMELY_HIGH` | `P3` | 27 | `constant` | 2 | requested feature may fail or degrade |
| `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH` | `P3` | 27 | `constant` | 2 | requested feature may fail or degrade |
| `NvsTimelineTimeSpan.OnMarginChangeListener` | `P3` | 27 | `nested-type/callback` | 2 | requested feature may fail or degrade |
| `NvsTimelineTimeSpanExt.OnTrimInChangeListener` | `P3` | 27 | `nested-type/callback` | 2 | state/error handling becomes fragile |
| `NvsTimelineTimeSpanExt.OnTrimOutChangeListener` | `P3` | 27 | `nested-type/callback` | 2 | state/error handling becomes fragile |
| `NvsVideoClip.VIDEO_CLIP_TYPE_AV` | `P3` | 27 | `constant` | 10 | timeline/preview/edit flow incomplete |
| `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_16_BIT_FLOAT` | `P3` | 27 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_AUTO` | `P3` | 27 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT` | `P3` | 26 | `constant` | 9 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE` | `P3` | 25 | `constant` | 8 | timeline/preview/edit flow incomplete |
| `NvsAVFileInfo.AV_FILE_TYPE_IMAGE` | `P3` | 24 | `constant` | 7 | feature-specific or optional |
| `NvsARSceneManipulate.NvsARSceneManipulateCallback` | `P3` | 23 | `nested-type/callback` | 1 | requested feature may fail or degrade |
| `NvsARSceneManipulate.NvsFaceBoundingRectInfo` | `P3` | 23 | `nested-type/callback` | 1 | requested feature may fail or degrade |
| `NvsARSceneManipulate.NvsHandFeatureInfo` | `P3` | 23 | `nested-type/callback` | 1 | requested feature may fail or degrade |
| `NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST` | `P3` | 23 | `constant` | 18 | feature-specific or optional |
| `NvsMaskRegionInfo.Ellipse2D` | `P3` | 23 | `nested-type/callback` | 1 | state/error handling becomes fragile |
| `NvsPassthroughConvertor.PassthroughConvertorCallback` | `P3` | 23 | `nested-type/callback` | 1 | state/error handling becomes fragile |
| `NvsStreamingContext.DEVICE_POWER_LEVEL_LOW` | `P3` | 23 | `constant` | 1 | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY` | `P3` | 23 | `human-detection` | 1 | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON` | `P3` | 23 | `human-detection` | 1 | feature-specific or optional |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK` | `P3` | 23 | `human-detection` | 1 | requested feature may fail or degrade |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_SKY` | `P3` | 23 | `human-detection` | 1 | feature-specific or optional |
| `NvsStreamingContext.RECORD_GOP_SIZE` | `P3` | 23 | `constant` | 1 | requested feature may fail or degrade |
| `NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED` | `P3` | 23 | `constant` | 1 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_CONTEXT_FLAG_INTERRUPT_STOP_FOR_INTERNAL_STOP` | `P3` | 23 | `constant` | 1 | timeline/preview/edit flow incomplete |
| `NvsStreamingContext.STREAMING_CONTEXT_FLAG_NEED_GIF_MOTION` | `P3` | 23 | `constant` | 1 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_ALIGN_VIDEO_SIZE` | `P3` | 23 | `constant` | 1 | state/error handling becomes fragile |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_HARDWARE_ENCODER` | `P3` | 23 | `constant` | 1 | requested feature may fail or degrade |
| `NvsTimeline.NvsTimelineWatermarkPosition_TopLeft` | `P3` | 23 | `constant` | 1 | requested feature may fail or degrade |
| `NvsTimeline.NvsTimelineWatermarkPosition_TopRight` | `P3` | 23 | `constant` | 1 | requested feature may fail or degrade |
| `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN` | `P3` | 23 | `constant` | 6 | timeline/preview/edit flow incomplete |
| `NvsLiveWindow.HDR_DISPLAY_MODE_SDR` | `P3` | 22 | `constant` | 5 | timeline/preview/edit flow incomplete |
| `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE` | `P3` | 20 | `constant` | 11 | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_AUDIO` | `P3` | 19 | `template-footage-type` | 3 | requested feature may fail or degrade |
| `NvsMultiThumbnailSequenceView.THUMBNAIL_IMAGE_FILLMODE_ASPECTCROP` | `P3` | 19 | `constant` | 3 | feature-specific or optional |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0` | `P3` | 19 | `constant` | 3 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.IMAGE_CLIP_MOTIONMMODE_ROI` | `P3` | 19 | `constant` | 3 | timeline/preview/edit flow incomplete |
| `NvsConstants.ADJUST_TINT` | `P3` | 18 | `constant` | 9 | feature-specific or optional |
| `NvsConstants.POST_PACKAGE_ID` | `P3` | 18 | `constant` | 9 | requested feature may fail or degrade |
| `NvsTimelineCaption.THEME_CATEGORY` | `P3` | 18 | `constant` | 9 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_16v9` | `P3` | 17 | `template-aspect-ratio` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_18v9` | `P3` | 17 | `template-aspect-ratio` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_1v1` | `P3` | 17 | `template-aspect-ratio` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_3v4` | `P3` | 17 | `template-aspect-ratio` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_4v3` | `P3` | 17 | `template-aspect-ratio` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_9v16` | `P3` | 17 | `template-aspect-ratio` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_9v18` | `P3` | 17 | `template-aspect-ratio` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_FREEZE_FRAME` | `P3` | 17 | `template-footage-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_IMAGE` | `P3` | 17 | `template-footage-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_VIDEO` | `P3` | 17 | `template-footage-type` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_VIDEO_IMAGE` | `P3` | 17 | `template-footage-type` | 2 | requested feature may fail or degrade |
| `NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D` | `P3` | 17 | `constant` | 8 | feature-specific or optional |
| `NvsConstants.KEY_VIDEO_MODE` | `P3` | 17 | `constant` | 8 | feature-specific or optional |
| `NvsLiveWindow.HDR_DISPLAY_MODE_DEPEND_DEVICE` | `P3` | 17 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsLiveWindow.HDR_DISPLAY_MODE_TONE_MAP_SDR` | `P3` | 17 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsTimelineCaption.ROLE_IN_THEME_GENERAL` | `P3` | 17 | `constant` | 8 | requested feature may fail or degrade |
| `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME` | `P3` | 17 | `constant` | 8 | requested feature may fail or degrade |
| `NvsVideoClip.ClIP_BACKGROUNDMODE_BLUR` | `P3` | 17 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180` | `P3` | 17 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270` | `P3` | 17 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90` | `P3` | 17 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ROLE_IN_THEME_TITLE` | `P3` | 17 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.ROLE_IN_THEME_TRAILER` | `P3` | 17 | `constant` | 2 | timeline/preview/edit flow incomplete |
| `NvsConstants.KEY_BACKGROUND_MODE` | `P3` | 16 | `constant` | 7 | feature-specific or optional |
| `NvsConstants.KEY_MASK_GENERATOR` | `P3` | 16 | `constant` | 7 | feature-specific or optional |
| `NvsVideoStreamInfo.VIDEO_ROTATION_270` | `P3` | 16 | `constant` | 7 | feature-specific or optional |
| `NvsVideoStreamInfo.VIDEO_ROTATION_90` | `P3` | 16 | `constant` | 7 | feature-specific or optional |
| `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN` | `P3` | 15 | `constant` | 6 | feature-specific or optional |
| `NvsConstants.IS_POST_STORY_BOARD_3D` | `P3` | 15 | `constant` | 6 | requested feature may fail or degrade |
| `NvsConstants.KEY_BACKGROUND_COLOR` | `P3` | 15 | `constant` | 6 | feature-specific or optional |
| `NvsConstants.KEY_MASK_GENERATOR_TYPE` | `P3` | 15 | `constant` | 6 | feature-specific or optional |
| `NvsConstants.PACKAGE_EFFECT_IN` | `P3` | 15 | `constant` | 6 | requested feature may fail or degrade |
| `NvsConstants.PACKAGE_EFFECT_OUT` | `P3` | 15 | `constant` | 6 | requested feature may fail or degrade |
| `NvsConstants.KEY_BACKGROUND_BLUR_RADIUS` | `P3` | 14 | `constant` | 5 | feature-specific or optional |
| `NvsConstants.VALUE_COLOR_BACKGROUND_MODE` | `P3` | 14 | `constant` | 5 | feature-specific or optional |
| `NvsVideoFx.VIDEOFX_TYPE_BUILTIN` | `P3` | 14 | `constant` | 5 | requested feature may fail or degrade |
| `NvsAVFileInfo.AV_FILE_INFO_FLAGS_HAS_VIDEO_PART_IN_IMAGE` | `P3` | 13 | `constant` | 1 | requested feature may fail or degrade |
| `NvsAVFileInfo.AV_FILE_TYPE_AUDIOVIDEO` | `P3` | 13 | `constant` | 1 | feature-specific or optional |
| `NvsCaptionSpan.SPAN_TYPE_FONT_FAMILY` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_NORMAL_TEXT` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_OUTLINE_WIDTH` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_RENDER_ID` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_ROTATION` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_SCALE_X` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_SCALE_Y` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_TRANS_X` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsConstants.FX_TRANSFORM_2D_TRANS_Y` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_MODE` | `P3` | 13 | `constant` | 4 | feature-specific or optional |
| `NvsExpressionParam.TYPE_COLOR` | `P3` | 13 | `fx-param-type` | 4 | requested feature may fail or degrade |
| `NvsLiveWindow.FILLMODE_PRESERVEASPECTCROP` | `P3` | 13 | `constant` | 1 | timeline/preview/edit flow incomplete |
| `NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON` | `P3` | 13 | `constant` | 4 | feature-specific or optional |
| `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR` | `P3` | 13 | `constant` | 4 | state/error handling becomes fragile |
| `NvsObject.TEMPLATE_KEY_BEST_SEEK_TIME` | `P3` | 13 | `constant` | 4 | timeline/preview/edit flow incomplete |
| `NvsTimelineCaption.TEXT_ALIGNMENT_CENTER` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsTimelineCaption.TEXT_ALIGNMENT_LEFT` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT` | `P3` | 13 | `constant` | 4 | requested feature may fail or degrade |
| `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE` | `P3` | 13 | `constant` | 1 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID` | `P3` | 13 | `constant` | 1 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME` | `P3` | 13 | `constant` | 1 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE` | `P3` | 13 | `constant` | 1 | timeline/preview/edit flow incomplete |
| `NvsVideoClip.TEMPLATE_KEY_REPLACE_ID` | `P3` | 13 | `constant` | 1 | timeline/preview/edit flow incomplete |
| `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE` | `P3` | 13 | `constant` | 4 | feature-specific or optional |
| `NvsCaption.BOUNDING_TYPE_TEXT` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_COLOR` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_OUTLINE_COLOR` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsClipCaption.ROLE_IN_THEME_GENERAL` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsClipCaption.THEME_CATEGORY` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsConstants.ADJUST_AMOUNT` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ADJUST_BLACKPOINT` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ADJUST_BRIGHTNESS` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ADJUST_CONTRAST` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ADJUST_DEGREE` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ADJUST_HIGHTLIGHT` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ADJUST_SATURATION` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ADJUST_SHADOW` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ADJUST_TEMPERATURE` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.ANIMATION_POST_PACKAGE_ID` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_RIGHT_GAIN` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.CUT_FX_TYPE_FOR_TRANSFORM` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsConstants.FX_SHARPEN` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsConstants.FX_VIGNETTE` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsConstants.KEY_BACKGROUND_IMAGE_PATH` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.KEY_BACKGROUND_ROTATION` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_SCALE_X` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_SCALE_Y` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsConstants.POST_PACKAGE_ID_OLD` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsExpressionParam.TYPE_BOOLEAN` | `P3` | 11 | `fx-param-type` | 3 | requested feature may fail or degrade |
| `NvsExpressionParam.TYPE_FLOAT` | `P3` | 11 | `fx-param-type` | 3 | requested feature may fail or degrade |
| `NvsExpressionParam.TYPE_INT` | `P3` | 11 | `fx-param-type` | 3 | requested feature may fail or degrade |
| `NvsObject.TEMPLATE_KEY_FX_GROUP` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsObject.TEMPLATE_KEY_REPLACE_ID` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsTimelineCaption.ROLE_IN_THEME_TITLE` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsVideoFx.VIDEOFX_TYPE_PACKAGE` | `P3` | 11 | `constant` | 3 | requested feature may fail or degrade |
| `NvsVideoStreamInfo.VIDEO_ROTATION_0` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsVideoStreamInfo.VIDEO_ROTATION_180` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH` | `P3` | 11 | `constant` | 3 | feature-specific or optional |
| `NvsARSceneManipulate.CheckedFunctionType_Matte` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsCaptionSpan.SPAN_TYPE_ITALIC` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_OPACITY` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_UNDERLINE` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsCaptureSceneInfo.CAPTURESCENE_INFO_IMAGE_FILLMODE_CROP` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsConstants.ANIMATION_PACKAGE_ID` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsConstants.CUT_KEY_IS_NORMALIZED_COORD` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.CUT_KEY_MASK_GENERATOR` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.FX_TRANSFORM_2D` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsConstants.KEY_CROPPER_ASSET_ASPECT_RATIO` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_RATIO` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_ROTATION` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_TRANS_X` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_TRANS_Y` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.KEY_CROP_FULL_TRANSFORM` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.KEY_MASK_GENERATOR_SIGN_MASK` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.KEY_MASK_STORYBOARD_DESC` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsConstants.PROPERTY_FX` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_COLOR` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_IMAGE` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.PROPERTY_OPACITY` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.PROPERTY_VALUE_BACKGROUND_COLOR_SOLID` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.SIZE_4K_HEIGHT` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.SIZE_4K_WIDTH` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.VALUE_CROPPER_FREE` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.VALUE_CROP_FULL_TRANSFORM` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsConstants.VALUE_IMAGE_BACKGROUND_MODE` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_180` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsVideoTransition.VIDEO_TRANSITION_TYPE_BUILTIN` | `P3` | 9 | `constant` | 2 | feature-specific or optional |
| `NvsVideoTransition.VIDEO_TRANSITION_TYPE_PACKAGE` | `P3` | 9 | `constant` | 2 | requested feature may fail or degrade |
| `NvsAssetPackageParticleDescParser.PARTICLE_TYPE_NORMAL` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsAssetPackageParticleDescParser.PARTICLE_TYPE_TOUCH` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_ID` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NAME` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TAGS` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TYPE` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsCaption.BOUNDING_TYPE_FRAME` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_BODY_OPACITY` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_FONT_SIZE_RATIO` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsCaptionSpan.SPAN_TYPE_OUTLINE_OPACITY` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsConstants.ANIMATION_ENABLE_MUTLISAMPLE` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.ANIMATION_IS_POST_STORYBOARD_3D` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsConstants.ANIMATION_PACKAGE_EFFECT_IN` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsConstants.ANIMATION_PACKAGE_EFFECT_OUT` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsConstants.KEY_BACKGROUND_MUTLISAMPLE` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_KEEP_RGB` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.KEY_CROPPER_REGION_INFO` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.KEY_MASK_FEATHER_WIDTH` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.KEY_MASK_GENERATOR_SIGN_CROP` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.KEY_MASK_INVERSE_REGION` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.KEY_MASK_KEEP_RGB` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.KEY_MASK_REGION_INFO` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_BLUR_RADIUS` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_ROTATION` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_SCALE_X` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_SCALE_Y` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_TRANS_X` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_KEY_TRANS_Y` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR_NEW_MODE_ENABLE` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.PROPERTY_VALUE_BACKGROUND_IMAGE_FILE` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsConstants.VALUE_BLUR_BACKGROUND_MODE` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsFaceDetector.AI_SDK_DETECTION_BUFFER_FORMAT_RGBA` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_0` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_270` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_90` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsFaceDetector.AI_SDK_DETECTION_FRAME_VIDEO_MODE` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsMaskRegionInfo.MASK_REGION_TYPE_ELLIPSE2D` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsMediaFileConvertor.CONVERTOR_ENABLE_HDR` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsTimelineCaption.ROLE_IN_THEME_TRAILER` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsTimelineVideoFx.TIMELINE_VIDEOFX_TYPE_BUILTIN` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsTimelineVideoFx.TIMELINE_VIDEOFX_TYPE_PACKAGE` | `P3` | 5 | `constant` | 1 | requested feature may fail or degrade |
| `NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsVideoFrameRetriever.VIDEO_FRAME_HEIGHT_GRADE_480` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
| `NvsVideoFrameRetriever.VIDEO_FRAME_HEIGHT_GRADE_720` | `P3` | 5 | `constant` | 1 | feature-specific or optional |
