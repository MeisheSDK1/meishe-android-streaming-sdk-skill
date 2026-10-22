# Demo Simple Snippets Index

Use this index after official docs and before loading the larger `demo-simple-snippets-*.md` files.
The snippets are generated from the Android demo as compact method-level API sequences. Source paths are provenance labels only; the original demo is not required at skill use time.

Coverage-sensitive references:
- `capability-catalog.md`: user-facing SDK/skill capability catalog; use before snippet routing when the user is new, vague, or asks what can be built.
- `skill-lookup-index.json` and `scripts/search_skill_index.py`: compact retrieval router; use first to map natural-language feature/API requests to snippet files, references, resource keys, and optional template overlays.
- `resource-requirements-index.md`: feature-to-resource map; use before implementation when the feature needs SDK binaries, native libraries, media, packages, models, fonts, or output paths.
- `demo-feature-list.md`: implementation-facing demo feature list; use to map a feature request to source labels, primary SDK classes, and snippet coverage.
- `demo-api-list.md`: capability-facing demo API list; use to map SDK classes/members/constants to demo evidence and simple/expanded coverage.
- `demo-feature-priority-map.md`: feature/module priority and weight map; use to choose P0/P1 implementation foundations for broad or ambiguous app requests.
- `demo-api-priority-map.md`: API class/method/member/constant priority and weight map; use to identify mandatory, common, feature-critical, and optional SDK surfaces before loading snippets.
- `demo-api-dependency-graph.md`: API call/dependency graph; use to derive required predecessors, produced SDK objects, callback gates, conflicts, teardown, and minimal subgraphs before composing snippets.
- `demo-feature-dependency-graph.md`: feature/module dependency graph; use to combine modules by required/recommended/optional/conflict relationships without copying demo Activity flows.
- `demo-api-constraint-map.md`: API constraint map; use for preconditions, guard tags, parameter/return handling, and observed method call shapes.
- `demo-sdk-constants-map.md`: constants/type map; use for built-in constants, nested callback/type names, template constants, and typed FX parameter keys.
- `demo-api-call-order-map.md`: call-order map; use when composing APIs into complete feature flows.
- `demo-feature-api-simple-coverage.md`: combined feasibility assessment for API coverage, feature coverage, composability, and complete project generation boundaries.
- `demo-coverage-audit.md`: explains why the baseline method-level pass was not full and records the expanded zero-missing-token coverage result.
- `demo-simple-snippets-rare-structural.md`: low-frequency, field-level, nested callback, caption span, watermark, `NvsTrackCaption`, `NvsPanAndScan`, and Effect SDK object usages.
- `demo-simple-snippets-exhaustive-statements.md`: every unique sanitized SDK-related Java statement pattern extracted from the demo.
- `demo-api-touchpoints.md`: full import, token, direct member, and SDK-bearing source file map.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Routing](#routing)
- [High-Frequency API Classes In Snippets](#high-frequency-api-classes-in-snippets)
- [Lookup Strategy](#lookup-strategy)
- [Representative Snippets Per Group](#representative-snippets-per-group)
<!-- END GENERATED CONTENTS -->

## Routing

| Reference | Snippets | Read when |
| --- | ---: | --- |
| `demo-simple-snippets-core-lifecycle.md` | 46 | SDK initialization, singleton access, callbacks, permissions, AV file info, thumbnail views, main-thread checks, and lifecycle cleanup. |
| `demo-simple-snippets-timeline-editing.md` | 88 | timeline/video/audio track creation, clip append/insert/remove/split, timeline data binding, clip transforms, timeline mutation, and edit-state reconstruction. |
| `demo-simple-snippets-preview-export.md` | 214 | live window connection, playback, seek, engine state checks, compile/export, image grab, thumbnail generation, and retriever flows. |
| `demo-simple-snippets-capture-recording.md` | 19 | camera capture preview, capture callbacks, capture effects, recording toggles, capture flags, device capability checks, and picture/video capture. |
| `demo-simple-snippets-effects-transforms.md` | 248 | built-in/package video effects, color adjust, transform/crop/background, transitions, masks, watermarks, speed, keyframes, and effect parameter setting. |
| `demo-simple-snippets-captions-stickers.md` | 408 | timeline/clip captions, compound captions, caption spans, animated stickers, sticker/caption packages, text styles, and keyframe editing. |
| `demo-simple-snippets-assets-packages.md` | 21 | NvsAssetPackageManager install/query/update flows, package type constants, theme/transition/caption/sticker/filter package IDs, and package callbacks. |
| `demo-simple-snippets-ar-makeup-segmentation.md` | 150 | AR scene, human detection, beauty, makeup, face mesh, warp, segmentation, mask generator, master keyer, and virtual background style flows. |
| `demo-simple-snippets-template-mimo-cutsame.md` | 175 | template package parsing, template footage replacement, Mimo timeline creation, CutSame editing, and template/cut-same compile flows. |
| `demo-simple-snippets-audio-media.md` | 122 | audio tracks/clips/effects, music/lyrics, recording voiceover, media convertor, passthrough convertor, AV file info, and frame retrieval. |

## High-Frequency API Classes In Snippets

| Class | Snippets |
| --- | ---: |
| `NvsStreamingContext` | 425 |
| `NvsTimeline` | 298 |
| `NvsVideoClip` | 189 |
| `NvsVideoTrack` | 113 |
| `NvsTimelineCaption` | 102 |
| `NvsVideoFx` | 84 |
| `NvsColor` | 63 |
| `NvsAssetPackageManager` | 60 |
| `NvsTimelineTimeSpan` | 50 |
| `NvsVideoResolution` | 50 |
| `NvsAudioClip` | 40 |
| `NvsCaptureVideoFx` | 35 |
| `NvsFx` | 34 |
| `NvsConstants` | 34 |
| `NvsAVFileInfo` | 34 |
| `NvsTimelineCompoundCaption` | 33 |
| `NvsRational` | 28 |
| `NvsMultiThumbnailSequenceView` | 28 |
| `NvsTimelineAnimatedSticker` | 25 |
| `NvsCaption` | 23 |
| `NvsLiveWindow` | 22 |
| `NvsServerClient` | 18 |
| `NvsAudioFx` | 18 |
| `NvsAudioTrack` | 17 |
| `NvsMaskRegionInfo` | 17 |
| `NvsSize` | 16 |
| `NvsTimelineVideoFx` | 16 |
| `NvsClipCaption` | 16 |
| `NvsMediaFileConvertor` | 13 |
| `NvsUtils` | 12 |
| `NvsTimelineEditor` | 11 |
| `NvsCaptionSpan` | 11 |
| `NvsVideoTransition` | 11 |
| `NvsTimelineTimeSpanExt` | 10 |
| `NvsPosition2D` | 10 |
| `NvsControlPointPair` | 9 |
| `NvsClipAnimatedSticker` | 9 |
| `NvsStreamingContextUtil` | 8 |
| `NvsCaptureCompoundCaption` | 8 |
| `NvsCaptureAnimatedSticker` | 8 |
| `NvsARSceneManipulate` | 8 |
| `NvsTemplateFootageCorrespondingClipInfo` | 6 |
| `NvsMakeupEffectInfo` | 6 |
| `NvsVideoStreamInfo` | 6 |
| `NvsLiveWindowExt` | 6 |
| `NvsTemplateFootageDesc` | 6 |
| `NvsPointD` | 5 |
| `NvsTemplateCaptionDesc` | 4 |
| `NvsAudioResolution` | 4 |
| `NvsVideoEffect` | 3 |
| `NvsEffectRenderCore` | 3 |
| `NvsEffect` | 3 |
| `NvsVideoEffectCompoundCaption` | 3 |
| `NvsFxDescription` | 3 |
| `NvsAnimatedSticker` | 3 |
| `NvsExpressionParam` | 3 |
| `NvsTemplateCompoundCaptionItemDesc` | 3 |
| `NvsEffectSdkContext` | 2 |
| `NvsCaptureSceneInfo` | 2 |
| `NvsShadowOpacitySpan` | 2 |
| `NvsPassthroughConvertor` | 2 |
| `NvsPassthroughFileInfo` | 2 |
| `NvsAIContext` | 2 |
| `NvsFaceDetector` | 2 |
| `NvsFaceFeatureInfo` | 2 |
| `NvsArbitraryData` | 2 |
| `NvsCompoundCaption` | 2 |
| `NvsTemplateCompoundCaptionDesc` | 2 |
| `NvsClipCompoundCaption` | 2 |
| `NvsIconGenerator` | 2 |
| `NvsVideoFrameInfo` | 1 |
| `NvsColorSpan` | 1 |
| `NvsOpacitySpan` | 1 |
| `NvsBodyOpacitySpan` | 1 |
| `NvsOutlineColorSpan` | 1 |
| `NvsOutlineWidthSpan` | 1 |
| `NvsNormalTextSpan` | 1 |
| `NvsOutlineOpacitySpan` | 1 |
| `NvsFontSizeRatioSpan` | 1 |
| `NvsFontFamilySpan` | 1 |

## Lookup Strategy

- Read this file for routing only.
- Use `rg "NvsTimelineCaption|setTextColor|caption" references/demo-simple-snippets-*.md` to find exact snippets without loading every group.
- Read `demo-simple-snippets-catalog.md` only when you need a full snippet id/source table across all categories.
- Read `demo-api-dependency-graph.md` and `demo-feature-dependency-graph.md` before combining snippets from multiple feature groups.
- Read `demo-simple-snippets-rare-structural.md` when a class or nested type is missing from normal category snippets.
- Search `demo-simple-snippets-exhaustive-statements.md` before concluding the demo does not use a specific SDK statement or constant.

## Representative Snippets Per Group

| Snippet | Group | Source | API classes |
| --- | --- | --- | --- |
| `core-lifecycle-001` `getSdkVersion` | `demo-simple-snippets-core-lifecycle.md` | `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:57` | `NvsStreamingContext` |
| `core-lifecycle-002` `getSdkVersion` | `demo-simple-snippets-core-lifecycle.md` | `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:59` | `NvsStreamingContext` |
| `core-lifecycle-003` `OnRightTextClick` | `demo-simple-snippets-core-lifecycle.md` | `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:459` | `NvsStreamingContext` |
| `core-lifecycle-004` `checkSupport4K` | `demo-simple-snippets-core-lifecycle.md` | `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:651` | `NvsConstants` |
| `core-lifecycle-005` `support4kAvcEncoding` | `demo-simple-snippets-core-lifecycle.md` | `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:702` | `NvsConstants` |
| `core-lifecycle-006` `support4kAvcEncoding` | `demo-simple-snippets-core-lifecycle.md` | `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:704` | `NvsConstants` |
| `core-lifecycle-007` `getStreamingContext` | `demo-simple-snippets-core-lifecycle.md` | `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:76` | `NvsStreamingContext` |
| `core-lifecycle-008` `getStreamingContext` | `demo-simple-snippets-core-lifecycle.md` | `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:77` | `NvsStreamingContext` |
| `timeline-editing-001` `initTimeline` | `demo-simple-snippets-timeline-editing.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:140` | `NvsVideoTrack` |
| `timeline-editing-002` `onStreamingEngineStateChanged` | `demo-simple-snippets-timeline-editing.md` | `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:144` | `NvsTimeline` |
| `timeline-editing-003` `rebuildTimelineStructure` | `demo-simple-snippets-timeline-editing.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1564` | `NvsVideoClip` |
| `timeline-editing-004` `localVideoTrim` | `demo-simple-snippets-timeline-editing.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1648` | `NvsVideoClip` |
| `timeline-editing-005` `muteVideoTrack` | `demo-simple-snippets-timeline-editing.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1924` | `NvsVideoTrack`, `NvsVideoClip` |
| `timeline-editing-006` `muteVideoTrack` | `demo-simple-snippets-timeline-editing.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1928` | `NvsVideoClip` |
| `timeline-editing-007` `setPanAndScan` | `demo-simple-snippets-timeline-editing.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1941` | `NvsVideoClip` |
| `timeline-editing-008` `getClipRange` | `demo-simple-snippets-timeline-editing.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1953` | `NvsVideoClip` |
| `preview-export-001` `onStop` | `demo-simple-snippets-preview-export.md` | `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:68` | `NvsStreamingContext` |
| `preview-export-002` `onStop` | `demo-simple-snippets-preview-export.md` | `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:69` | `NvsStreamingContext` |
| `preview-export-003` `initListener` | `demo-simple-snippets-preview-export.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:92` | `NvsTimeline`, `NvsStreamingContext` |
| `preview-export-004` `setCompileCallback` | `demo-simple-snippets-preview-export.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:101` | `NvsTimeline` |
| `preview-export-005` `onCompileProgress` | `demo-simple-snippets-preview-export.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:106` | `NvsTimeline` |
| `preview-export-006` `onResume` | `demo-simple-snippets-preview-export.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:213` | `NvsStreamingContext` |
| `preview-export-007` `LiveWindow` | `demo-simple-snippets-preview-export.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:25` | `NvsStreamingContext`, `NvsTimeline` |
| `preview-export-008` `onPlaybackPreloadingCompletion` | `demo-simple-snippets-preview-export.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:43` | `NvsTimeline` |
| `capture-recording-001` `onClick` | `demo-simple-snippets-capture-recording.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java:163` | `NvsStreamingContext` |
| `capture-recording-002` `onClick` | `demo-simple-snippets-capture-recording.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java:166` | `NvsStreamingContext` |
| `capture-recording-003` `changeFlash` | `demo-simple-snippets-capture-recording.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java:193` | `NvsStreamingContext` |
| `capture-recording-004` `setRecordVideoBitrateMultiplier` | `demo-simple-snippets-capture-recording.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:201` | `NvsStreamingContextUtil`, `NvsStreamingContext` |
| `capture-recording-005` `setRecordVideoBitrateMultiplier` | `demo-simple-snippets-capture-recording.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:202` | `NvsStreamingContextUtil`, `NvsStreamingContext` |
| `capture-recording-006` `onPause` | `demo-simple-snippets-capture-recording.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3632` | `NvsStreamingContext` |
| `capture-recording-007` `getDialog` | `demo-simple-snippets-capture-recording.md` | `app/src/main/java/com/meishe/sdkdemo/dialog/TopMoreDialog.java:328` | `NvsStreamingContext` |
| `capture-recording-008` `initRootView` | `demo-simple-snippets-capture-recording.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:302` | `NvsLiveWindow` |
| `effects-transforms-001` `initMeicamSdk` | `demo-simple-snippets-effects-transforms.md` | `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:68` | `NvsStreamingContext` |
| `effects-transforms-002` `onResume` | `demo-simple-snippets-effects-transforms.md` | `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java:318` | `NvsStreamingContext` |
| `effects-transforms-003` `getEffectContext` | `demo-simple-snippets-effects-transforms.md` | `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:93` | `NvsEffectSdkContext` |
| `effects-transforms-004` `setStrength` | `demo-simple-snippets-effects-transforms.md` | `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java:112` | `NvsColor` |
| `effects-transforms-005` `getColor` | `demo-simple-snippets-effects-transforms.md` | `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java:116` | `NvsColor` |
| `effects-transforms-006` `clearShape` | `demo-simple-snippets-effects-transforms.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2648` | `NvsCaptureVideoFx` |
| `effects-transforms-007` `clearShape` | `demo-simple-snippets-effects-transforms.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2649` | `NvsCaptureVideoFx` |
| `effects-transforms-008` `clearShape` | `demo-simple-snippets-effects-transforms.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2650` | `NvsCaptureVideoFx` |
| `captions-stickers-001` `onScaleAndRotate` | `demo-simple-snippets-captions-stickers.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:570` | `NvsTimelineCompoundCaption` |
| `captions-stickers-002` `deleteCaptionOrSticker` | `demo-simple-snippets-captions-stickers.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:819` | `NvsCaptureAnimatedSticker`, `NvsCaptureCompoundCaption` |
| `captions-stickers-003` `deleteCaptionOrSticker` | `demo-simple-snippets-captions-stickers.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:820` | `NvsCaptureAnimatedSticker`, `NvsCaptureCompoundCaption` |
| `captions-stickers-004` `deleteCaptionOrSticker` | `demo-simple-snippets-captions-stickers.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:821` | `NvsCaptureAnimatedSticker` |
| `captions-stickers-005` `deleteCaptionOrSticker` | `demo-simple-snippets-captions-stickers.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:824` | `NvsCaptureAnimatedSticker` |
| `captions-stickers-006` `checkSelectCaption` | `demo-simple-snippets-captions-stickers.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:917` | `NvsCaption` |
| `captions-stickers-007` `getCaptionList` | `demo-simple-snippets-captions-stickers.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1185` | `NvsTimelineCompoundCaption` |
| `captions-stickers-008` `getCaptionList` | `demo-simple-snippets-captions-stickers.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1187` | `NvsTimelineCompoundCaption` |
| `assets-packages-001` `installEffect` | `demo-simple-snippets-assets-packages.md` | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/CaptureEffectTabFragment.java:271` | `NvsAssetPackageManager` |
| `assets-packages-002` `setCaptureFilterByPath` | `demo-simple-snippets-assets-packages.md` | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java:136` | `NvsAssetPackageManager` |
| `assets-packages-003` `initData` | `demo-simple-snippets-assets-packages.md` | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:155` | `NvsAssetPackageManager` |
| `assets-packages-004` `setCaptureFilterByPath` | `demo-simple-snippets-assets-packages.md` | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:343` | `NvsAssetPackageManager` |
| `assets-packages-005` `initData` | `demo-simple-snippets-assets-packages.md` | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:130` | `NvsAssetPackageManager` |
| `assets-packages-006` `setCaptureFilterByPath` | `demo-simple-snippets-assets-packages.md` | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:332` | `NvsAssetPackageManager` |
| `assets-packages-007` `installEffect` | `demo-simple-snippets-assets-packages.md` | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:359` | `NvsAssetPackageManager` |
| `assets-packages-008` `initData` | `demo-simple-snippets-assets-packages.md` | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java:123` | `NvsAssetPackageManager` |
| `ar-makeup-segmentation-001` `getBuffingSkin` | `demo-simple-snippets-ar-makeup-segmentation.md` | `MArScene/src/main/java/com/meishe/arscene/BeautyDataManager.java:176` | `NvsStreamingContext` |
| `ar-makeup-segmentation-002` `checkBuildCaptureBeautyFx` | `demo-simple-snippets-ar-makeup-segmentation.md` | `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:70` | `NvsCaptureVideoFx`, `NvsStreamingContext` |
| `ar-makeup-segmentation-003` `checkBuildCaptureBeautyFx` | `demo-simple-snippets-ar-makeup-segmentation.md` | `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:71` | `NvsStreamingContext` |
| `ar-makeup-segmentation-004` `checkBuildCaptureBeautyFx` | `demo-simple-snippets-ar-makeup-segmentation.md` | `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:72` | `NvsStreamingContext` |
| `ar-makeup-segmentation-005` `getCaptureVideoFx` | `demo-simple-snippets-ar-makeup-segmentation.md` | `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:105` | `NvsCaptureVideoFx` |
| `ar-makeup-segmentation-006` `getCaptureVideoFx` | `demo-simple-snippets-ar-makeup-segmentation.md` | `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:106` | `NvsCaptureVideoFx` |
| `ar-makeup-segmentation-007` `getCaptureBeautyFx` | `demo-simple-snippets-ar-makeup-segmentation.md` | `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:119` | `NvsFx` |
| `ar-makeup-segmentation-008` `getBeautyFx` | `demo-simple-snippets-ar-makeup-segmentation.md` | `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:127` | `NvsVideoFx`, `NvsVideoClip` |
| `template-mimo-cutsame-001` `bindLayout` | `demo-simple-snippets-template-mimo-cutsame.md` | `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:56` | `NvsStreamingContext`, `NvsRational` |
| `template-mimo-cutsame-002` `initData` | `demo-simple-snippets-template-mimo-cutsame.md` | `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:58` | `NvsStreamingContext` |
| `template-mimo-cutsame-003` `initData` | `demo-simple-snippets-template-mimo-cutsame.md` | `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:60` | `NvsStreamingContext` |
| `template-mimo-cutsame-004` `onCompileProgress` | `demo-simple-snippets-template-mimo-cutsame.md` | `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:139` | `NvsTimeline` |
| `template-mimo-cutsame-005` `onCompileFinished` | `demo-simple-snippets-template-mimo-cutsame.md` | `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:144` | `NvsTimeline` |
| `template-mimo-cutsame-006` `onCompileFailed` | `demo-simple-snippets-template-mimo-cutsame.md` | `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:147` | `NvsStreamingContext` |
| `template-mimo-cutsame-007` `onCompileFailed` | `demo-simple-snippets-template-mimo-cutsame.md` | `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:149` | `NvsTimeline` |
| `template-mimo-cutsame-008` `bindLayout` | `demo-simple-snippets-template-mimo-cutsame.md` | `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:98` | `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip` |
| `audio-media-001` `onClick` | `demo-simple-snippets-audio-media.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:160` | `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext` |
| `audio-media-002` `onClick` | `demo-simple-snippets-audio-media.md` | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:162` | `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext` |
| `audio-media-003` `setOnClickListener` | `demo-simple-snippets-audio-media.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2105` | `NvsStreamingContext` |
| `audio-media-004` `setOnClickListener` | `demo-simple-snippets-audio-media.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2107` | `NvsStreamingContext` |
| `audio-media-005` `setOnClickListener` | `demo-simple-snippets-audio-media.md` | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2200` | `NvsVideoStreamInfo`, `NvsAVFileInfo`, `NvsSize` |
| `audio-media-006` `jumpToPreview` | `demo-simple-snippets-audio-media.md` | `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:295` | `NvsVideoStreamInfo`, `NvsAVFileInfo`, `NvsSize` |
| `audio-media-007` `onProgress` | `demo-simple-snippets-audio-media.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:57` | `NvsMediaFileConvertor` |
| `audio-media-008` `cancelConvert` | `demo-simple-snippets-audio-media.md` | `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:252` | `NvsMediaFileConvertor` |
