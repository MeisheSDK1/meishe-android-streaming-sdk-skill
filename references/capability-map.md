# Capability Map

Use this map to decide which self-contained references and snippets to load for a user request.

For first-time users, vague product goals, "what can the SDK do", or "what can this skill do" questions, read `capability-catalog.md` first. This file is the implementation router after a capability has been selected.

Before applying a capability section, route through `official-docs-index.md` and read the matching `official-*.md` reference for API behavior, parameter constraints, and SDK limitations. Then use `demo-simple-snippets-index.md` and `rg` over `demo-simple-snippets-*.md` for method-level examples. For coverage-sensitive checks, use `demo-coverage-audit.md`, `demo-api-touchpoints.md`, and `demo-simple-snippets-exhaustive-statements.md`. This map is for implementation targeting and curated snippet selection.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [sdk-initialization](#sdk-initialization)
- [timeline-editing](#timeline-editing)
- [preview-playback](#preview-playback)
- [camera-capture-recording](#camera-capture-recording)
- [filters-effects](#filters-effects)
- [beauty-makeup-ar](#beauty-makeup-ar)
- [captions-stickers](#captions-stickers)
- [asset-packages](#asset-packages)
- [audio-music](#audio-music)
- [export-compile](#export-compile)
- [templates-cut-same](#templates-cut-same)
<!-- END GENERATED CONTENTS -->

## sdk-initialization

App-level SDK initialization, license URI setup, Effect SDK init, AR module checks, and human-detection model loading.

Primary SDK classes: `NvsStreamingContext`, `NvsEffectSdkContext`

Snippet ids: `streaming-context-init`, `human-detection-models`, `human-detection-data`

High-signal provenance labels:
- `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java` (27)
- `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java` (2)
- `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java` (2)
- `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java` (2)
- `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java` (1)
- `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java` (1)
- `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java` (1)
- `libEngine/src/main/java/com/meishe/engine/EditorEngine.java` (1)

## timeline-editing

Timeline creation, video/audio tracks, clip import, trim/split, transforms, clip effects, and edit-state to timeline binding.

Primary SDK classes: `NvsTimeline`, `NvsVideoTrack`, `NvsAudioTrack`, `NvsVideoClip`, `NvsAudioClip`

Snippet ids: `timeline-create-main`, `single-clip-timeline`, `append-clip-and-adjust`

High-signal provenance labels:
- `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java` (115)
- `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java` (103)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java` (89)
- `libEngine/src/main/java/com/meishe/engine/EditorEngine.java` (80)
- `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java` (59)
- `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java` (48)
- `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java` (48)
- `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java` (46)
- `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java` (44)
- `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java` (41)
- `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java` (41)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java` (38)

## preview-playback

LiveWindow connection, playback/seek callbacks, engine state checks, and preview sizing.

Primary SDK classes: `NvsLiveWindow`, `NvsStreamingContext`, `NvsTimeline`

Snippet ids: `timeline-create-main`

High-signal provenance labels:
- `libEngine/src/main/java/com/meishe/engine/EditorEngine.java` (45)
- `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java` (34)
- `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java` (25)
- `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java` (25)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java` (22)
- `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java` (22)
- `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java` (22)
- `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java` (19)
- `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java` (17)
- `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java` (17)
- `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java` (16)
- `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java` (15)

## camera-capture-recording

Camera device selection, capture preview, recording, take-picture support, and capture callbacks.

Primary SDK classes: `NvsStreamingContext`, `NvsCaptureVideoFx`, `NvsCaptureAnimatedSticker`, `NvsCaptureCompoundCaption`

Snippet ids: `capture-preview`, `capture-recording-toggle`

High-signal provenance labels:
- `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java` (26)
- `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java` (20)
- `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java` (19)
- `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java` (16)
- `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java` (16)
- `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java` (15)
- `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java` (15)
- `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java` (11)
- `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java` (9)
- `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java` (8)
- `app/src/main/java/com/meishe/sdkdemo/superzoom/processor/MediaMuxerWrapper.java` (6)
- `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java` (4)

## filters-effects

Built-in/package clip effects, timeline effects, capture effects, keyframe/value parameters, and effect intensity.

Primary SDK classes: `NvsVideoFx`, `NvsTimelineVideoFx`, `NvsCaptureVideoFx`

Snippet ids: `append-clip-and-adjust`, `capture-filters`

High-signal provenance labels:
- `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java` (66)
- `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java` (31)
- `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java` (25)
- `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java` (19)
- `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java` (18)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java` (18)
- `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java` (14)
- `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java` (12)
- `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java` (12)
- `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java` (12)
- `libEngine/src/main/java/com/meishe/engine/EditorEngine.java` (10)
- `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java` (9)

## beauty-makeup-ar

Beauty, makeup, face shape, AR scene props, segmentation, avatar, hand/eye/face models, and low-device model choice.

Primary SDK classes: `NvsCaptureVideoFx`, `NvsARSceneManipulate`, `NvsEffectSdkContext`, `NvsStreamingContext`

Snippet ids: `human-detection-models`, `human-detection-data`, `ar-scene-prop`

High-signal provenance labels:
- `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java` (94)
- `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java` (50)
- `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java` (46)
- `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCaptureFragment.java` (40)
- `libBase/src/main/java/com/meishe/http/AssetType.java` (27)
- `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java` (18)
- `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java` (18)
- `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java` (17)
- `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java` (17)
- `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java` (16)
- `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java` (14)
- `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java` (11)

## captions-stickers

Timeline captions, modular captions, compound captions, animated stickers, custom stickers, transforms, animation, and layer metadata.

Primary SDK classes: `NvsTimelineCaption`, `NvsTimelineCompoundCaption`, `NvsTimelineAnimatedSticker`, `NvsAnimatedSticker`

Snippet ids: `timeline-stickers`, `timeline-captions`

High-signal provenance labels:
- `libEngine/src/main/java/com/meishe/engine/EditorEngine.java` (50)
- `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java` (29)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java` (28)
- `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java` (27)
- `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java` (26)
- `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java` (24)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java` (24)
- `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java` (24)
- `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java` (18)
- `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java` (16)
- `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java` (16)
- `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java` (14)

## asset-packages

Package path/license resolution, install/upgrade logic, package ids, and asset package manager callbacks.

Primary SDK classes: `NvsAssetPackageManager`, `NvsStreamingContext`

Snippet ids: `asset-package-install`

High-signal provenance labels:
- `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java` (51)
- `libBase/src/main/java/com/meishe/utils/NvAsset.java` (49)
- `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java` (42)
- `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java` (28)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java` (25)
- `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java` (18)
- `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java` (17)
- `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java` (16)
- `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java` (14)
- `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java` (13)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java` (13)
- `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java` (12)

## audio-music

Audio tracks/clips, music insertion, recording tracks, volume, audio equalizer, and capture noise suppression.

Primary SDK classes: `NvsAudioTrack`, `NvsAudioClip`, `NvsCaptureAudioFx`, `NvsVolume`

Snippet ids: `timeline-create-main`, `capture-recording-toggle`

High-signal provenance labels:
- `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java` (22)
- `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java` (22)
- `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java` (20)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java` (20)
- `libEngine/src/main/java/com/meishe/engine/EditorEngine.java` (18)
- `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java` (15)
- `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java` (12)
- `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java` (11)
- `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java` (10)
- `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java` (8)
- `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java` (8)
- `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java` (6)

## export-compile

Compile/export path generation, compile settings, HEVC/HDR/bitrate flags, callbacks, progress, and media scanning.

Primary SDK classes: `NvsStreamingContext`, `NvsTimeline`, `NvsVideoResolution`

Snippet ids: `compile-video`, `compile-callbacks`

High-signal provenance labels:
- `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java` (22)
- `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java` (20)
- `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java` (14)
- `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java` (13)
- `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java` (11)
- `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java` (8)
- `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java` (6)
- `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java` (5)
- `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java` (5)
- `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java` (4)
- `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java` (4)
- `app/src/main/java/com/meishe/sdkdemo/quicksplicing/QuickSplicingActivity.kt` (2)

## templates-cut-same

Cut-same/template workflows and Mimo-style template edit flows.

Primary SDK classes: `NvsTimeline`, `NvsVideoClip`, `NvsTimelineCaption`, `NvsTimelineAnimatedSticker`

Snippet ids: `timeline-create-main`, `timeline-captions`, `timeline-stickers`

High-signal provenance labels:
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoActivity.java` (63)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java` (45)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/SelectMediaActivity.java` (39)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java` (30)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java` (30)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/template/utils/MiMoFileUtils.java` (18)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java` (17)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/base/BaseEditActivity.java` (15)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/fragment/MediaFragment.java` (14)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/view/SelectBottomMenu.java` (14)
- `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java` (13)
- `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java` (12)
