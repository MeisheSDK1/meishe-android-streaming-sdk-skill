# Demo Feature List

This is the implementation-facing feature list extracted from demo modules, Android manifests, Java packages, and SDK-bearing source files.
Use this list when a user asks for a feature/workflow. It maps feature surfaces to implementation entry points, primary SDK APIs, and simple-snippet coverage.

Coverage levels:
- `method-snippets`: feature has reusable method-level snippets.
- `touchpoints/statements`: feature has SDK source evidence but not enough curated method snippets; search `demo-api-touchpoints.md` and `demo-simple-snippets-exhaustive-statements.md`.
- `manifest-only`: UI/workflow entry exists but direct SDK logic is in supporting files or adjacent flows.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Summary](#summary)
- [Feature Inventory](#feature-inventory)
- [Per-Feature Details](#per-feature-details)
<!-- END GENERATED CONTENTS -->

## Summary

| Category | Features | Method-snippet features | Touchpoint-only features | Manifest-only features |
| --- | ---: | ---: | ---: | ---: |
| `ar-makeup-segmentation` | 12 | 12 | 0 | 0 |
| `assets-packages` | 3 | 2 | 0 | 1 |
| `audio-media` | 9 | 9 | 0 | 0 |
| `captions-stickers` | 20 | 20 | 0 | 0 |
| `core-lifecycle` | 5 | 3 | 0 | 2 |
| `effects-transforms` | 6 | 6 | 0 | 0 |
| `preview-export` | 2 | 2 | 0 | 0 |
| `template-mimo-cutsame` | 5 | 5 | 0 | 0 |

## Feature Inventory

| Feature | Category | Implementation entries | Primary SDK/API classes | Simple coverage | Source examples |
| --- | --- | --- | --- | --- | --- |
| `app-root` App Root | `core-lifecycle` | 2 Class | `NvsEffectSdkContext`, `NvsStreamingContext` | method-snippets; snippets=4; sdk-lines=47 | `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java`, `app/src/main/java/com/meishe/sdkdemo/MSApplication.java` |
| `base-meishe` Base Meishe | `core-lifecycle` | 1 Activity, 13 Class, 2 Util, 1 Fragment | `NvsStreamingContext`, `NvsLiveWindowExt`, `NvsMultiThumbnailSequenceView`, `NvsAssetPackageManager`, `NvsVideoClip`, `NvsTimeline`, `NvsVideoResolution`, `NvsFx` | method-snippets; snippets=26; sdk-lines=107 | `libBase/src/main/java/com/meishe/base/constants/NvsConstants.java`, `libBase/src/main/java/com/meishe/base/model/BaseMvpActivity.java`, `libBase/src/main/java/com/meishe/base/model/BaseMvpFragment.java`, `libBase/src/main/java/com/meishe/base/model/IBaseView.java`, `libBase/src/main/java/com/meishe/base/model/NvsError.java`, `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java` |
| `capture` Capture | `ar-makeup-segmentation` | 1 Activity, 5 Fragment, 1 ViewModel | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsEffectSdkContext`, `NvsEffect`, `NvsEffectRenderCore`, `NvsVideoEffect`, `NvsVideoEffectAnimatedSticker`, `NvsVideoEffectCompoundCaption` | method-snippets; snippets=37; sdk-lines=110 | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseFragment.java`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseHorizontalLoadMoreAndRefreshFragment.java`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/CaptureEffectTabFragment.java`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java` |
| `capture-beauty` Capture Beauty | `ar-makeup-segmentation` | 1 Fragment, 1 Presenter | `NvsFx` | method-snippets; snippets=7; sdk-lines=9 | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCaptureFragment.java`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java` |
| `edit-makeup` Edit Makeup | `ar-makeup-segmentation` | 1 Activity | `NvsColor`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoFx`, `NvsVideoTrack` | method-snippets; snippets=9; sdk-lines=19 | `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java` |
| `edit-view` Edit View | `ar-makeup-segmentation` | 1 View | `NvsColor` | method-snippets; snippets=4; sdk-lines=3 | `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java` |
| `makeup` Makeup module | `ar-makeup-segmentation` | 1 Manager, 1 Helper, 1 Class | `NvsAssetPackageManager`, `NvsStreamingContext`, `NvsCaptureVideoFx`, `NvsColor`, `NvsFx`, `NvsMakeupEffectInfo`, `NvsVideoClip`, `NvsVideoFx` | method-snippets; snippets=40; sdk-lines=54 | `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java`, `MMakeup/src/main/java/com/meishe/makeup/utils/DataConvertUtils.java` |
| `presenter` Presenter | `ar-makeup-segmentation` | 2 Presenter | `NvsARSceneManipulate`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoFx`, `NvsVideoTrack`, `NvsStreamingContext` | method-snippets; snippets=8; sdk-lines=23 | `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java`, `app/src/main/java/com/meishe/sdkdemo/presenter/MainPresenter.java` |
| `superzoom` SuperZoom AI workflow | `ar-makeup-segmentation` | 2 Activity | `NvsAIContext`, `NvsFaceDetector`, `NvsRational`, `NvsVideoResolution`, `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext`, `NvsTimeline` | method-snippets; snippets=8; sdk-lines=28 | `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java` |
| `utils` Utils | `core-lifecycle` | 4 Util, 3 Class | `NvsStreamingContext`, `NvsVideoResolution`, `NvsTimeline`, `NvsTimelineAnimatedSticker`, `NvsTimelineCaption`, `NvsVideoClip`, `NvsAVFileInfo`, `NvsSize` | method-snippets; snippets=61; sdk-lines=439 | `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java`, `app/src/main/java/com/meishe/sdkdemo/utils/ImageConverter.java`, `app/src/main/java/com/meishe/sdkdemo/utils/ParameterSettingValues.java`, `app/src/main/java/com/meishe/sdkdemo/utils/StoryboardUtil.java`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java`, `app/src/main/java/com/meishe/sdkdemo/utils/Util.java` |
| `utils-asset` Utils Asset | `ar-makeup-segmentation` | 1 Class, 1 Manager | `NvsAssetPackageManager`, `NvsStreamingContext` | method-snippets; snippets=4; sdk-lines=32 | `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java`, `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java` |
| `view` View | `ar-makeup-segmentation` | 5 View | `NvsExpressionParam`, `NvsMultiThumbnailSequenceView`, `NvsARSceneManipulate`, `NvsFx`, `NvsAssetPackageManager`, `NvsStreamingContext`, `NvsColor` | method-snippets; snippets=5; sdk-lines=27 | `app/src/main/java/com/meishe/sdkdemo/view/AdjustSpecialEffectsView.java`, `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java`, `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java`, `app/src/main/java/com/meishe/sdkdemo/view/FaceUPropView.java`, `app/src/main/java/com/meishe/sdkdemo/view/MakeUpSingleView.java` |
| `capture-filter` Capture Filter | `assets-packages` | 2 Fragment | `NvsAssetPackageManager`, `NvsStreamingContext` | method-snippets; snippets=4; sdk-lines=7 | `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java` |
| `download` Download | `assets-packages` | 1 Activity | - | manifest-only; snippets=0; sdk-lines=0 | `app/src/main/java/com/meishe/sdkdemo/download/AssetDownloadActivity.java` |
| `edit-filter` Edit Filter | `assets-packages` | 2 Activity, 2 View, 1 Presenter | `NvsTimeline`, `NvsStreamingContext`, `NvsExpressionParam`, `NvsVideoClip`, `NvsVideoTrack`, `NvsAssetPackageManager`, `NvsColor`, `NvsVideoFx` | method-snippets; snippets=29; sdk-lines=100 | `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/KeyFramePointView.java` |
| `boomrang` BoomRang capture/playback workflow | `capture-recording` | 2 Activity, 1 Fragment, 1 Class | `NvsStreamingContext`, `NvsTimeline`, `NvsLiveWindow`, `NvsAVFileInfo`, `NvsSize`, `NvsVideoTrack` | method-snippets; snippets=19; sdk-lines=35 | `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java`, `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java`, `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java`, `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java` |
| `capturescene` Capture scene workflow | `capture-recording` | 2 Activity, 2 Fragment, 2 View, 1 Util | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsCaptureVideoFx`, `NvsLiveWindow`, `NvsTimeline`, `NvsAVFileInfo`, `NvsCaptureSceneInfo`, `NvsColor` | method-snippets; snippets=27; sdk-lines=74 | `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneFragment.java`, `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java`, `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewActivity.java`, `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java`, `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneBottomView.java` |
| `edit-audio` Edit Audio | `audio-media` | 1 Activity | `NvsAudioFx`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` | method-snippets; snippets=10; sdk-lines=20 | `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java` |
| `edit-music` Edit Music | `audio-media` | 2 Activity, 1 Class | `NvsMultiThumbnailSequenceView`, `NvsAudioClip`, `NvsAudioTrack`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` | method-snippets; snippets=18; sdk-lines=32 | `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicSqLayout.java`, `app/src/main/java/com/meishe/sdkdemo/edit/music/SelectMusicActivity.java` |
| `glitter` Glitter | `audio-media` | 1 Activity, 1 Fragment | `NvsCaptureVideoFx`, `NvsStreamingContext`, `NvsLiveWindow`, `NvsTimeline` | method-snippets; snippets=2; sdk-lines=18 | `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectActivity.java`, `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java` |
| `particle` Particle | `effects-transforms` | 4 Activity, 2 Class, 1 Adapter | `NvsAssetPackageParticleDescParser`, `NvsSize`, `NvsStreamingContext`, `NvsAVFileInfo`, `NvsVideoStreamInfo`, `NvsMultiThumbnailSequenceView`, `NvsTimeline`, `NvsLiveWindow` | method-snippets; snippets=32; sdk-lines=91 | `app/src/main/java/com/meishe/sdkdemo/particle/LiveWindow.java`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureFxAdapter.java`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleSqLayout.java` |
| `picinpic` Picture-in-picture editing | `audio-media` | 2 Activity | `NvsStreamingContext`, `NvsTimeline`, `NvsAVFileInfo`, `NvsAssetPackageManager`, `NvsLiveWindow`, `NvsVideoClip`, `NvsVideoFx`, `NvsVideoResolution` | method-snippets; snippets=17; sdk-lines=49 | `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PicturInPicturePreviewActivity.java` |
| `selectmedia` Media selection workflow | `audio-media` | 1 Activity, 1 Adapter | `NvsAVFileInfo`, `NvsStreamingContext`, `NvsVideoResolution` | method-snippets; snippets=1; sdk-lines=7 | `app/src/main/java/com/meishe/sdkdemo/selectmedia/adapter/AgendaSimpleSectionAdapter.java`, `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java` |
| `urledit` Urledit | `audio-media` | 1 Activity | `NvsAVFileInfo`, `NvsStreamingContext`, `NvsVideoResolution` | method-snippets; snippets=2; sdk-lines=4 | `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java` |
| `dialog` Dialog | `captions-stickers` | 1 Pop, 1 Dialog | `NvsStreamingContext`, `NvsColor` | method-snippets; snippets=2; sdk-lines=6 | `app/src/main/java/com/meishe/sdkdemo/dialog/CaptionEditPop.java`, `app/src/main/java/com/meishe/sdkdemo/dialog/TopMoreDialog.java` |
| `douvideo` DouVideo capture/edit workflow | `captions-stickers` | 3 Activity, 2 Class | `NvsStreamingContext`, `NvsVideoClip`, `NvsAVFileInfo`, `NvsTimeline`, `NvsLiveWindow`, `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsMediaFileConvertor` | method-snippets; snippets=53; sdk-lines=141 | `app/src/main/java/com/meishe/sdkdemo/douvideo/bean/RecordClip.java`, `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java` |
| `edit` Edit | `captions-stickers` | 1 Activity, 2 Fragment | `NvsStreamingContext`, `NvsTimeline`, `NvsTimelineAnimatedSticker`, `NvsRational`, `NvsTimelineVideoFx`, `NvsVideoClip`, `NvsAssetPackageManager`, `NvsAudioTrack` | method-snippets; snippets=62; sdk-lines=146 | `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java`, `app/src/main/java/com/meishe/sdkdemo/edit/EditBaseActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java` |
| `edit-animatesticker` Edit Animatesticker | `captions-stickers` | 4 Activity | `NvsStreamingContext`, `NvsTimeline`, `NvsTimelineAnimatedSticker`, `NvsVideoTrack`, `NvsAVFileInfo`, `NvsSize`, `NvsAnimatedSticker`, `NvsAssetPackageManager` | method-snippets; snippets=34; sdk-lines=87 | `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java` |
| `edit-caption` Edit Caption | `captions-stickers` | 2 Activity, 1 Presenter | `NvsStreamingContext`, `NvsCaption`, `NvsControlPointPair`, `NvsTimeline`, `NvsTimelineCaption`, `NvsVideoTrack`, `NvsMultiThumbnailSequenceView`, `NvsPointD` | method-snippets; snippets=57; sdk-lines=271 | `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/presenter/CaptionPresenter.java` |
| `edit-clipedit` Edit Clipedit | `captions-stickers` | 14 Activity, 2 Fragment, 2 Class, 1 View | `NvsTimeline`, `NvsStreamingContext`, `NvsVideoClip`, `NvsVideoTrack`, `NvsMultiThumbnailSequenceView`, `NvsAVFileInfo`, `NvsVideoResolution`, `NvsSize` | method-snippets; snippets=170; sdk-lines=388 | `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CuttingMenuView.java`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/ICutRegionFragment.java`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java` |
| `edit-compoundcaption` Edit Compoundcaption | `captions-stickers` | 2 Activity | `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsColor`, `NvsMultiThumbnailSequenceView`, `NvsTimeline`, `NvsTimelineCompoundCaption`, `NvsVideoClip`, `NvsVideoTrack` | method-snippets; snippets=15; sdk-lines=49 | `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionStyleActivity.java` |
| `edit-createpic` Edit Createpic | `captions-stickers` | 1 Activity | `NvsMultiThumbnailSequenceView`, `NvsRational`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` | method-snippets; snippets=6; sdk-lines=20 | `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java` |
| `edit-mask` Edit Mask | `captions-stickers` | 1 Activity, 1 Helper | `NvsAVFileInfo`, `NvsLiveWindow`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoFx`, `NvsVideoResolution`, `NvsVideoTrack` | method-snippets; snippets=27; sdk-lines=66 | `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java` |
| `edit-record` Edit Record | `captions-stickers` | 1 Activity, 1 Class, 1 View | `NvsMultiThumbnailSequenceView`, `NvsAudioClip`, `NvsAudioFx`, `NvsAudioTrack`, `NvsStreamingContext`, `NvsTimeline`, `NvsTimelineAnimatedSticker`, `NvsVideoClip` | method-snippets; snippets=21; sdk-lines=34 | `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/record/SqLayout.java`, `app/src/main/java/com/meishe/sdkdemo/edit/record/SqView.java` |
| `edit-theme` Edit Theme | `captions-stickers` | 1 Activity | `NvsStreamingContext`, `NvsTimeline`, `NvsTimelineCaption`, `NvsVideoClip`, `NvsVideoTrack` | method-snippets; snippets=12; sdk-lines=29 | `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java` |
| `edit-timelineeditor` Edit Timelineeditor | `captions-stickers` | 3 Class | `NvsMultiThumbnailSequenceView`, `NvsStreamingContext`, `NvsTimeline` | method-snippets; snippets=9; sdk-lines=39 | `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java`, `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpan.java`, `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpanExt.java` |
| `edit-transition` Edit Transition | `captions-stickers` | 1 Activity | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack`, `NvsVideoTransition` | method-snippets; snippets=4; sdk-lines=11 | `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java` |
| `edit-watermark` Edit Watermark | `captions-stickers` | 2 Activity, 1 Util | `NvsTimeline`, `NvsTimelineVideoFx`, `NvsAssetPackageManager`, `NvsStreamingContext` | method-snippets; snippets=9; sdk-lines=11 | `app/src/main/java/com/meishe/sdkdemo/edit/watermark/SingleClickActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java` |
| `flipcaption` Flipcaption | `captions-stickers` | 2 Activity | `NvsColor`, `NvsStreamingContext`, `NvsTimeline`, `NvsTimelineVideoFx`, `NvsVideoClip`, `NvsVideoResolution`, `NvsVideoTrack` | method-snippets; snippets=5; sdk-lines=15 | `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java`, `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionEditActivity.java` |
| `musiclyrics` Music lyrics workflow | `captions-stickers` | 2 Activity | `NvsAudioTrack`, `NvsStreamingContext`, `NvsTimeline`, `NvsTimelineCaption`, `NvsVideoTrack` | method-snippets; snippets=7; sdk-lines=19 | `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MultiVideoSelectActivity.java`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java` |
| `photoalbum` Photo album workflow | `captions-stickers` | 2 Activity | `NvsAVFileInfo`, `NvsAudioResolution`, `NvsLiveWindow`, `NvsRational`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoResolution` | method-snippets; snippets=11; sdk-lines=43 | `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumActivity.java`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java` |
| `quicksplicing` Quick splicing / passthrough convert | `captions-stickers` | 1 Activity | `NvsMultiThumbnailSequenceView`, `NvsPassthroughConvertor`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` | method-snippets; snippets=6; sdk-lines=20 | `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java` |
| `themeshoot` Theme shoot workflow | `captions-stickers` | 4 Activity, 3 Class, 1 Bean, 1 View | `NvsLiveWindow`, `NvsTimelineVideoFx`, `NvsRational`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack`, `NvsTimelineCompoundCaption`, `NvsAVFileInfo` | method-snippets; snippets=37; sdk-lines=132 | `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeEditCaptionActivity.java`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeSelectActivity.java`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java` |
| `utils-datainfo` Utils Datainfo | `captions-stickers` | 5 Class, 1 Data | `NvsVideoClip`, `NvsVideoFx`, `NvsCaptionSpan`, `NvsVideoStreamInfo`, `NvsVideoResolution`, `NvsVideoTransition`, `NvsColor` | method-snippets; snippets=10; sdk-lines=21 | `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/CaptionInfo.java`, `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/ClipInfo.java`, `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java`, `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java`, `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TransitionInfo.java`, `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/VideoClipFxInfo.java` |
| `feedback` Feedback | `core-lifecycle` | 1 Activity | `NvsStreamingContext` | method-snippets; snippets=2; sdk-lines=1 | `app/src/main/java/com/meishe/sdkdemo/feedback/FeedBackActivity.java` |
| `libnet` Libnet | `core-lifecycle` | 1 Callback, 1 Class | `NvsServerClient` | method-snippets; snippets=2; sdk-lines=8 | `libNet/src/main/java/com/meishe/net/custom/JsonCallback.java`, `libNet/src/main/java/com/meishe/net/NvsServerClient.java` |
| `main` Main | `core-lifecycle` | 1 Activity | - | manifest-only; snippets=0; sdk-lines=0 | `app/src/main/java/com/meishe/sdkdemo/main/MainWebViewActivity.java` |
| `repository` Repository | `core-lifecycle` | 1 Class | `NvsStreamingContext` | method-snippets; snippets=2; sdk-lines=1 | `app/src/main/java/com/meishe/sdkdemo/repository/AppRepository.java` |
| `utils-permission` Utils Permission | `core-lifecycle` | 1 Activity | - | manifest-only; snippets=0; sdk-lines=0 | `app/src/main/java/com/meishe/sdkdemo/utils/permission/PermissionsActivity.java` |
| `base` Base | `effects-transforms` | 1 Activity, 1 Manager | `NvsEffectSdkContext`, `NvsStreamingContext` | method-snippets; snippets=15; sdk-lines=27 | `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java`, `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java` |
| `bean` Bean | `effects-transforms` | 1 Class | `NvsColor` | method-snippets; snippets=2; sdk-lines=3 | `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java` |
| `edit-anim` Edit Anim | `effects-transforms` | 1 Activity, 1 Adapter | `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack`, `NvsStreamingContext`, `NvsVideoFx` | method-snippets; snippets=13; sdk-lines=34 | `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationClipAdapter.java` |
| `edit-background` Edit Background | `effects-transforms` | 1 Activity, 1 View | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoResolution`, `NvsVideoTrack`, `NvsColor` | method-snippets; snippets=10; sdk-lines=37 | `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java`, `app/src/main/java/com/meishe/sdkdemo/edit/background/view/MultiColorView.java` |
| `edit-data` Edit Data | `effects-transforms` | 1 Class, 1 Data | `NvsColor`, `NvsMaskRegionInfo` | method-snippets; snippets=3; sdk-lines=6 | `app/src/main/java/com/meishe/sdkdemo/edit/data/FilterItem.java`, `app/src/main/java/com/meishe/sdkdemo/edit/data/mask/MaskInfoData.java` |
| `makecover` Make cover workflow | `effects-transforms` | 1 Activity, 1 Fragment | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoFx`, `NvsVideoTrack`, `NvsRational`, `NvsLiveWindow` | method-snippets; snippets=14; sdk-lines=44 | `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java` |
| `edit-livephoto` Edit Livephoto | `preview-export` | 1 Activity | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` | method-snippets; snippets=5; sdk-lines=15 | `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java` |
| `sequencenesting` Sequencenesting | `preview-export` | 1 Activity | `NvsMultiThumbnailSequenceView`, `NvsRational`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` | method-snippets; snippets=9; sdk-lines=20 | `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java` |
| `activity` Activity | `template-mimo-cutsame` | 4 Activity | `NvsStreamingContext`, `NvsTimeline`, `NvsLiveWindow`, `NvsVideoResolution` | method-snippets; snippets=6; sdk-lines=31 | `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java`, `app/src/main/java/com/meishe/sdkdemo/activity/CutSameActivity.java`, `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java`, `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java` |
| `ar-scene` AR scene beauty module | `ar-makeup-segmentation` | 2 Fragment, 1 Manager, 1 Helper | `NvsStreamingContext`, `Logger`, `NvsAssetPackageManager`, `NvsCaptureVideoFx`, `NvsFx`, `NvsVideoClip`, `NvsVideoFx` | method-snippets; snippets=39; sdk-lines=61 | `MArScene/src/main/java/com/meishe/arscene/BeautyDataManager.java`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java`, `MArScene/src/main/java/com/meishe/arscene/BeautyTabFragment.java`, `MArScene/src/main/java/com/meishe/arscene/template/BeautyEditTabFragment.java` |
| `cutsame-template` CutSame/template module | `template-mimo-cutsame` | 6 Activity, 4 Fragment, 2 Class, 2 View | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsAssetPackageManager`, `NvsVideoTrack`, `NvsRational`, `NvsTimelineCaption`, `NvsVideoResolution` | method-snippets; snippets=70; sdk-lines=252 | `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java`, `MCutSame/src/main/java/com/meishe/cutsame/fragment/adapter/CutVideoAdapter.java` |
| `engine-meishe` Engine Meishe | `template-mimo-cutsame` | 36 Class, 3 Data, 3 Util, 1 Controller | `NvsTimeline`, `NvsVideoResolution`, `NvsVideoClip`, `NvsAVFileInfo`, `NvsStreamingContext`, `NvsVideoTrack`, `NvsVideoFx`, `NvsTimelineCompoundCaption` | method-snippets; snippets=293; sdk-lines=868 | `libEngine/src/main/java/com/meishe/engine/bean/background/MeicamStoryboardInfo.java`, `libEngine/src/main/java/com/meishe/engine/bean/ClipInfo.java`, `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioFx.java`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioTrack.java` |
| `mimodemo` Mimo demo workflow | `template-mimo-cutsame` | 6 Activity, 8 Class, 3 Util, 1 Data | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoResolution`, `NvsTimelineCompoundCaption`, `NvsTimelineAnimatedSticker`, `NvsMultiThumbnailSequenceView`, `NvsAssetPackageManager`, `NvsTimelineCaption` | method-snippets; snippets=73; sdk-lines=266 | `app/src/main/java/com/meishe/sdkdemo/mimodemo/base/BaseEditActivity.java`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/ClipInfo.java`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/permission/PermissionsActivity.java`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java` |

## Per-Feature Details

### `app-root` App Root

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Class`(2)
- Method snippets from this feature's source files: 4
- SDK-related code lines: 47
- Primary SDK imports: `com.meicam.effect.sdk.NvsEffectSdkContext`(2), `com.meicam.sdk.NvsStreamingContext`(2)
- Direct API/member tokens: `NvsStreamingContext.initHumanDetectionExt`(5), `NvsStreamingContext.getInstance`(4), `NvsEffectSdkContext.initHumanDetectionExt`(4), `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`(3), `NvsStreamingContext.setupHumanDetectionData`(3), `NvsEffectSdkContext.setupHumanDetectionData`(3), `NvsStreamingContext.SdkVersion`(2), `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK`(2), `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION`(2), `NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE`(2), `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND`(2), `NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK`(2)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java` `Class` sdk-import; 40 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/MSApplication.java` `Class` sdk-import; 7 sdk-lines

### `base-meishe` Base Meishe

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `libBase`(17)
- Roles: `Class`(13), `Util`(2), `Fragment`(1), `Activity`(1)
- Method snippets from this feature's source files: 26
- SDK-related code lines: 107
- Manifest activities: `com.meishe.base.utils.UtilsTransActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(3), `com.meicam.sdk.NvsLiveWindowExt`(2), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(2), `com.meicam.sdk.NvsAssetPackageManager`(2), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsFx`(1), `com.meicam.sdk.NvsLiveWindow`(1), `com.meicam.sdk.NvsColor`(1), `com.meicam.nvconvertorlib.Logger`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(5), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`(2), `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED`(2), `NvsVideoClip.VIDEO_CLIP_TYPE_AV`(1), `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE`(1), `NvsStreamingContext.PlaybackCallback`(1), `NvsStreamingContext.PlaybackCallback2`(1), `NvsStreamingContext.StreamingEngineCallback`(1)
- Source labels:
  - `libBase/src/main/java/com/meishe/base/constants/NvsConstants.java` `Class` sdk-import; 3 sdk-lines
  - `libBase/src/main/java/com/meishe/base/model/BaseMvpActivity.java` `Class` 1 sdk-lines
  - `libBase/src/main/java/com/meishe/base/model/BaseMvpFragment.java` `Class` 1 sdk-lines
  - `libBase/src/main/java/com/meishe/base/model/IBaseView.java` `Class` 1 sdk-lines
  - `libBase/src/main/java/com/meishe/base/model/NvsError.java` `Class` 2 sdk-lines
  - `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java` `Fragment` sdk-import; 20 sdk-lines
  - `libBase/src/main/java/com/meishe/base/utils/Utils.java` `Class` sdk-import; 4 sdk-lines
  - `libBase/src/main/java/com/meishe/base/utils/UtilsTransActivity.java` `Activity` manifest
  - `libBase/src/main/java/com/meishe/base/view/MSLiveWindow.java` `Class` sdk-import; 2 sdk-lines
  - `libBase/src/main/java/com/meishe/base/view/MSLiveWindowExt.java` `Class` sdk-import; 1 sdk-lines
  - `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java` `Class` sdk-import; 29 sdk-lines
  - `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpan.java` `Class` 3 sdk-lines
  - `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpanExt.java` `Class` sdk-import; 5 sdk-lines
  - `libBase/src/main/java/com/meishe/utils/ColorUtil.java` `Util` sdk-import; 4 sdk-lines
  - `libBase/src/main/java/com/meishe/utils/NvAsset.java` `Class` sdk-import; 24 sdk-lines
  - `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java` `Util` sdk-import; 7 sdk-lines
  - `libBase/src/main/java/com/meishe/utils/PathUtils.java` `Class` sdk-import

### `capture` Capture

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(7)
- Roles: `Fragment`(5), `Activity`(1), `ViewModel`(1)
- Method snippets from this feature's source files: 37
- SDK-related code lines: 110
- Manifest activities: `com.meishe.sdkdemo.capture.CaptureActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(5), `com.meicam.sdk.NvsAssetPackageManager`(4), `com.meicam.effect.sdk.NvsEffectSdkContext`(2), `com.meicam.effect.sdk.NvsEffect`(1), `com.meicam.effect.sdk.NvsEffectRenderCore`(1), `com.meicam.effect.sdk.NvsVideoEffect`(1), `com.meicam.effect.sdk.NvsVideoEffectAnimatedSticker`(1), `com.meicam.effect.sdk.NvsVideoEffectCompoundCaption`(1), `com.meicam.sdk.NvsARSceneManipulate`(1), `com.meicam.sdk.NvsAVFileInfo`(1), `com.meicam.sdk.NvsCaption`(1), `com.meicam.sdk.NvsCaptureAnimatedSticker`(1)
- Direct API/member tokens: `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`(4), `NvsStreamingContext.getInstance`(4), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(3), `NvsCaptureSceneInfo.ClipData`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`(3), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`(2), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW`(2), `NvsEffectSdkContext.getInstance`(2), `NvsStreamingContext.CaptureDeviceCallback`(1), `NvsStreamingContext.CaptureRecordingDurationCallback`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java` `Activity` manifest; sdk-import; 88 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseFragment.java` `Fragment` sdk-import; 4 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseHorizontalLoadMoreAndRefreshFragment.java` `Fragment` sdk-import; 4 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/CaptureEffectTabFragment.java` `Fragment` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java` `Fragment` sdk-import; 4 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java` `Fragment` sdk-import; 6 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capture/viewmodel/CaptureEffectTabViewModel.java` `ViewModel` sdk-import; 1 sdk-lines

### `capture-beauty` Capture Beauty

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Fragment`(1), `Presenter`(1)
- Method snippets from this feature's source files: 7
- SDK-related code lines: 9
- Primary SDK imports: `com.meicam.sdk.NvsFx`(2)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCaptureFragment.java` `Fragment` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java` `Presenter` sdk-import; 8 sdk-lines

### `edit-makeup` Edit Makeup

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 9
- SDK-related code lines: 19
- Manifest activities: `com.meishe.sdkdemo.edit.makeup.BeautyMakeupActivity`
- Primary SDK imports: `com.meicam.sdk.NvsColor`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoFx`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`(1), `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java` `Activity` manifest; sdk-import; 19 sdk-lines

### `edit-view` Edit View

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `View`(1)
- Method snippets from this feature's source files: 4
- SDK-related code lines: 3
- Primary SDK imports: `com.meicam.sdk.NvsColor`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java` `View` sdk-import; 3 sdk-lines

### `makeup` Makeup module

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `MMakeup`(3)
- Roles: `Manager`(1), `Helper`(1), `Class`(1)
- Method snippets from this feature's source files: 40
- SDK-related code lines: 54
- Primary SDK imports: `com.meicam.sdk.NvsAssetPackageManager`(3), `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.sdk.NvsCaptureVideoFx`(1), `com.meicam.sdk.NvsColor`(1), `com.meicam.sdk.NvsFx`(1), `com.meicam.sdk.NvsMakeupEffectInfo`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoFx`(1)
- Direct API/member tokens: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP`(2), `NvsStreamingContext.hasARModule`(2), `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL`(2), `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`(1)
- Source labels:
  - `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java` `Manager` sdk-import; 5 sdk-lines
  - `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java` `Helper` sdk-import; 48 sdk-lines
  - `MMakeup/src/main/java/com/meishe/makeup/utils/DataConvertUtils.java` `Class` sdk-import; 1 sdk-lines

### `presenter` Presenter

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Presenter`(2)
- Method snippets from this feature's source files: 8
- SDK-related code lines: 23
- Primary SDK imports: `com.meicam.sdk.NvsARSceneManipulate`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoFx`(1), `com.meicam.sdk.NvsVideoTrack`(1), `com.meicam.sdk.NvsStreamingContext`(1)
- Direct API/member tokens: `NvsARSceneManipulate.CheckedFunctionType_Matte`(1), `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java` `Presenter` sdk-import; 22 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/presenter/MainPresenter.java` `Presenter` sdk-import; 1 sdk-lines

### `superzoom` SuperZoom AI workflow

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(2)
- Method snippets from this feature's source files: 8
- SDK-related code lines: 28
- Manifest activities: `com.meishe.sdkdemo.superzoom.SuperZoomActivity`, `com.meishe.sdkdemo.superzoom.SuperZoomPreviewActivity`
- Primary SDK imports: `com.meicam.ai.sdk.NvsAIContext`(1), `com.meicam.ai.sdk.NvsFaceDetector`(1), `com.meicam.sdk.NvsRational`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsAVFileInfo`(1), `com.meicam.sdk.NvsSize`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1)
- Direct API/member tokens: `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_180`(2), `NvsFaceDetector.NvsFaceData`(2), `NvsAIContext.getInstance`(1), `NvsAIContext.init`(1), `NvsFaceDetector.createNvsFaceDetector`(1), `NvsFaceDetector.AI_SDK_DETECTION_FRAME_VIDEO_MODE`(1), `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_0`(1), `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_90`(1), `NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_270`(1), `NvsFaceDetector.AI_SDK_DETECTION_BUFFER_FORMAT_RGBA`(1), `NvsStreamingContext.CompileCallback`(1), `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java` `Activity` manifest; sdk-import; 20 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java` `Activity` manifest; sdk-import; 8 sdk-lines

### `utils` Utils

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(7)
- Roles: `Util`(4), `Class`(3)
- Method snippets from this feature's source files: 61
- SDK-related code lines: 439
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(6), `com.meicam.sdk.NvsVideoResolution`(6), `com.meicam.sdk.NvsTimeline`(3), `com.meicam.sdk.NvsTimelineAnimatedSticker`(3), `com.meicam.sdk.NvsTimelineCaption`(3), `com.meicam.sdk.NvsVideoClip`(3), `com.meicam.sdk.NvsAVFileInfo`(3), `com.meicam.sdk.NvsSize`(3), `com.meicam.sdk.NvsAudioClip`(2), `com.meicam.sdk.NvsAudioFx`(2), `com.meicam.sdk.NvsAudioResolution`(2), `com.meicam.sdk.NvsAudioTrack`(2)
- Direct API/member tokens: `NvsFxDescription.ParamInfoObject`(15), `NvsStreamingContext.getInstance`(7), `NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D`(7), `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN`(6), `NvsConstants.KEY_MASK_GENERATOR_TYPE`(6), `NvsConstants.Crop`(5), `NvsConstants.PROPERTY_KEY_BACKGROUND_MODE`(4), `NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM`(4), `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE`(3), `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN`(3), `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_RIGHT_GAIN`(3), `NvsConstants.KEY_MASK_GENERATOR`(3)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java` `Class` sdk-import; 52 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/ImageConverter.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/ParameterSettingValues.java` `Class` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/StoryboardUtil.java` `Util` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java` `Util` sdk-import; 335 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/Util.java` `Util` sdk-import; 18 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java` `Util` sdk-import; 27 sdk-lines

### `utils-asset` Utils Asset

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Class`(1), `Manager`(1)
- Method snippets from this feature's source files: 4
- SDK-related code lines: 32
- Primary SDK imports: `com.meicam.sdk.NvsAssetPackageManager`(2), `com.meicam.sdk.NvsStreamingContext`(1)
- Direct API/member tokens: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`(2), `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR`(2), `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java` `Class` sdk-import; 25 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java` `Manager` sdk-import; 7 sdk-lines

### `view` View

- Category: `ar-makeup-segmentation`
- Coverage: `method-snippets`
- Modules: `app`(5)
- Roles: `View`(5)
- Method snippets from this feature's source files: 5
- SDK-related code lines: 27
- Primary SDK imports: `com.meicam.sdk.NvsExpressionParam`(1), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(1), `com.meicam.sdk.NvsARSceneManipulate`(1), `com.meicam.sdk.NvsFx`(1), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsColor`(1)
- Direct API/member tokens: `NvsARSceneManipulate.NvsFaceFeatureInfo`(2), `NvsExpressionParam.TYPE_COLOR`(1), `NvsMultiThumbnailSequenceView.THUMBNAIL_IMAGE_FILLMODE_ASPECTCROP`(1), `NvsARSceneManipulate.NvsARSceneManipulateCallback`(1), `NvsARSceneManipulate.NvsFaceBoundingRectInfo`(1), `NvsARSceneManipulate.NvsHandFeatureInfo`(1), `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/view/AdjustSpecialEffectsView.java` `View` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java` `View` sdk-import; 15 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java` `View` sdk-import; 7 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/view/FaceUPropView.java` `View` sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/view/MakeUpSingleView.java` `View` sdk-import; 2 sdk-lines

### `capture-filter` Capture Filter

- Category: `assets-packages`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Fragment`(2)
- Method snippets from this feature's source files: 4
- SDK-related code lines: 7
- Primary SDK imports: `com.meicam.sdk.NvsAssetPackageManager`(2), `com.meicam.sdk.NvsStreamingContext`(1)
- Direct API/member tokens: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(4), `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED`(1), `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java` `Fragment` sdk-import; 4 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java` `Fragment` sdk-import; 3 sdk-lines

### `download` Download

- Category: `assets-packages`
- Coverage: `manifest-only`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 0
- SDK-related code lines: 0
- Manifest activities: `com.meishe.sdkdemo.download.AssetDownloadActivity`
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/download/AssetDownloadActivity.java` `Activity` manifest

### `edit-filter` Edit Filter

- Category: `assets-packages`
- Coverage: `method-snippets`
- Modules: `app`(6)
- Roles: `Activity`(3), `View`(2), `Presenter`(1)
- Method snippets from this feature's source files: 29
- SDK-related code lines: 100
- Manifest activities: `com.meishe.sdkdemo.edit.filter.ClipFilterActivity`, `com.meishe.sdkdemo.edit.filter.FilterActivity`
- Primary SDK imports: `com.meicam.sdk.NvsTimeline`(6), `com.meicam.sdk.NvsStreamingContext`(4), `com.meicam.sdk.NvsExpressionParam`(3), `com.meicam.sdk.NvsVideoClip`(3), `com.meicam.sdk.NvsVideoTrack`(3), `com.meicam.sdk.NvsAssetPackageManager`(2), `com.meicam.sdk.NvsColor`(2), `com.meicam.sdk.NvsVideoFx`(2), `com.meicam.sdk.NvsFx`(2), `com.meicam.sdk.NvsTimelineVideoFx`(1), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(1)
- Direct API/member tokens: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(8), `NvsStreamingContext.getInstance`(4), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(4), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(3), `NvsExpressionParam.TYPE_COLOR`(2), `NvsExpressionParam.TYPE_FLOAT`(2), `NvsExpressionParam.FloatParam`(2), `NvsExpressionParam.TYPE_INT`(2), `NvsExpressionParam.IntParam`(2), `NvsExpressionParam.TYPE_BOOLEAN`(2), `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER`(2), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(2)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java` `Activity` sdk-import; 37 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java` `Activity` manifest; sdk-import; 20 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java` `Activity` manifest; sdk-import; 14 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java` `View` sdk-import; 15 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java` `Presenter` sdk-import; 12 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/filter/KeyFramePointView.java` `View` sdk-import; 2 sdk-lines

### `boomrang` BoomRang capture/playback workflow

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(4)
- Roles: `Activity`(2), `Fragment`(1), `Class`(1)
- Method snippets from this feature's source files: 19
- SDK-related code lines: 35
- Manifest activities: `com.meishe.sdkdemo.boomrang.BoomRangActivity`, `com.meishe.sdkdemo.boomrang.BoomRangPreviewActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(4), `com.meicam.sdk.NvsTimeline`(2), `com.meicam.sdk.NvsLiveWindow`(2), `com.meicam.sdk.NvsAVFileInfo`(1), `com.meicam.sdk.NvsSize`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsStreamingContextUtil.getInstance`(5), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`(3), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(2), `NvsStreamingContext.RECORD_GOP_SIZE`(1), `NvsStreamingContext.CompileCallback`(1), `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM`(1), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(1), `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO`(1), `NvsStreamingContext.CaptureDeviceCallback`(1), `NvsStreamingContext.CaptureRecordingDurationCallback`(1), `NvsStreamingContext.CaptureRecordingStartedCallback`(1), `NvsStreamingContext.CaptureDeviceCapability`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java` `Activity` manifest; sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java` `Activity` manifest; sdk-import; 10 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java` `Fragment` sdk-import; 12 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java` `Class` sdk-import; 11 sdk-lines

### `capturescene` Capture scene workflow

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(7)
- Roles: `Activity`(2), `Fragment`(2), `View`(2), `Util`(1)
- Method snippets from this feature's source files: 27
- SDK-related code lines: 74
- Manifest activities: `com.meishe.sdkdemo.capturescene.CaptureSceneActivity`, `com.meishe.sdkdemo.capturescene.PreviewActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(6), `com.meicam.sdk.NvsAssetPackageManager`(2), `com.meicam.sdk.NvsCaptureVideoFx`(2), `com.meicam.sdk.NvsLiveWindow`(2), `com.meicam.sdk.NvsTimeline`(2), `com.meicam.sdk.NvsAVFileInfo`(1), `com.meicam.sdk.NvsCaptureSceneInfo`(1), `com.meicam.sdk.NvsColor`(1), `com.meicam.sdk.NvsSize`(1), `com.meicam.sdk.NvsVideoStreamInfo`(1)
- Direct API/member tokens: `NvsStreamingContextUtil.getInstance`(7), `NvsCaptureSceneInfo.ClipData`(3), `NvsStreamingContext.getInstance`(3), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`(2), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(2), `NvsAssetPackageManager.AssetPackageManagerCallback`(1), `NvsStreamingContext.CaptureDeviceCallback`(1), `NvsStreamingContext.CaptureRecordingDurationCallback`(1), `NvsStreamingContext.CaptureRecordingStartedCallback`(1), `NvsVideoStreamInfo.VIDEO_ROTATION_90`(1), `NvsVideoStreamInfo.VIDEO_ROTATION_270`(1), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java` `Activity` manifest; sdk-import; 25 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneFragment.java` `Fragment` sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java` `Util` sdk-import; 13 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewActivity.java` `Activity` manifest
  - `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java` `Fragment` sdk-import; 27 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneBottomView.java` `View` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneEffectView.java` `View` sdk-import; 4 sdk-lines

### `edit-audio` Edit Audio

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 10
- SDK-related code lines: 20
- Manifest activities: `com.meishe.sdkdemo.edit.audio.AudioEqualizerActivity`
- Primary SDK imports: `com.meicam.sdk.NvsAudioFx`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java` `Activity` manifest; sdk-import; 20 sdk-lines

### `edit-music` Edit Music

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(3)
- Roles: `Activity`(2), `Class`(1)
- Method snippets from this feature's source files: 18
- SDK-related code lines: 32
- Manifest activities: `com.meishe.sdkdemo.edit.music.MusicActivity`, `com.meishe.sdkdemo.edit.music.SelectMusicActivity`
- Primary SDK imports: `com.meicam.sdk.NvsMultiThumbnailSequenceView`(2), `com.meicam.sdk.NvsAudioClip`(1), `com.meicam.sdk.NvsAudioTrack`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(4), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(2), `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java` `Activity` manifest; sdk-import; 31 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicSqLayout.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/music/SelectMusicActivity.java` `Activity` manifest

### `glitter` Glitter

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(1), `Fragment`(1)
- Method snippets from this feature's source files: 2
- SDK-related code lines: 18
- Manifest activities: `com.meishe.sdkdemo.glitter.GlitterEffectActivity`
- Primary SDK imports: `com.meicam.sdk.NvsCaptureVideoFx`(2), `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.sdk.NvsLiveWindow`(1), `com.meicam.sdk.NvsTimeline`(1)
- Direct API/member tokens: `NvsStreamingContextUtil.getInstance`(3), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`(2), `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO`(1), `NvsStreamingContext.CaptureDeviceCallback`(1), `NvsStreamingContext.CaptureRecordingDurationCallback`(1), `NvsStreamingContext.CaptureRecordingStartedCallback`(1), `NvsStreamingContext.StreamingEngineCallback`(1), `NvsStreamingContext.CaptureDeviceCapability`(1), `NvsStreamingContext.getInstance`(1), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW`(1), `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME`(1), `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectActivity.java` `Activity` manifest; sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java` `Fragment` sdk-import; 16 sdk-lines

### `particle` Particle

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(7)
- Roles: `Activity`(4), `Class`(2), `Adapter`(1)
- Method snippets from this feature's source files: 32
- SDK-related code lines: 91
- Manifest activities: `com.meishe.sdkdemo.particle.ParticleCaptureActivity`, `com.meishe.sdkdemo.particle.ParticleEditActivity`, `com.meishe.sdkdemo.particle.ParticlePreviewActivity`, `com.meishe.sdkdemo.particle.SelectVideoActivity`
- Primary SDK imports: `com.meicam.sdk.NvsAssetPackageParticleDescParser`(3), `com.meicam.sdk.NvsSize`(3), `com.meicam.sdk.NvsStreamingContext`(3), `com.meicam.sdk.NvsAVFileInfo`(2), `com.meicam.sdk.NvsVideoStreamInfo`(2), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(2), `com.meicam.sdk.NvsTimeline`(2), `com.meicam.sdk.NvsLiveWindow`(1), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsCaptureVideoFx`(1), `com.meicam.sdk.NvsAudioResolution`(1), `com.meicam.sdk.NvsParticleSystemContext`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(5), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(4), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(4), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(4), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`(3), `NvsVideoStreamInfo.VIDEO_ROTATION_90`(2), `NvsVideoStreamInfo.VIDEO_ROTATION_270`(2), `NvsStreamingContext.PlaybackCallback`(2), `NvsStreamingContext.StreamingEngineCallback`(2), `NvsStreamingContext.PlaybackCallback2`(2), `NvsStreamingContext.CaptureDeviceCallback`(1), `NvsStreamingContext.CaptureRecordingDurationCallback`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/particle/LiveWindow.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java` `Activity` manifest; sdk-import; 21 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureFxAdapter.java` `Adapter` sdk-import
  - `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java` `Activity` manifest; sdk-import; 45 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java` `Activity` manifest; sdk-import; 23 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/particle/ParticleSqLayout.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/particle/SelectVideoActivity.java` `Activity` manifest

### `picinpic` Picture-in-picture editing

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(2)
- Method snippets from this feature's source files: 17
- SDK-related code lines: 49
- Manifest activities: `com.meishe.sdkdemo.picinpic.PictureInPictureActivity`, `com.meishe.sdkdemo.picinpic.PicturInPicturePreviewActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.sdk.NvsTimeline`(2), `com.meicam.sdk.NvsAVFileInfo`(1), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsLiveWindow`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoFx`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsVideoFx.VIDEOFX_TYPE_BUILTIN`(2), `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`(2), `NvsVideoFx.VIDEOFX_TYPE_PACKAGE`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(1), `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT`(1), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(1), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java` `Activity` manifest; sdk-import; 43 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/picinpic/PicturInPicturePreviewActivity.java` `Activity` manifest; sdk-import; 6 sdk-lines

### `selectmedia` Media selection workflow

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Adapter`(1), `Activity`(1)
- Method snippets from this feature's source files: 1
- SDK-related code lines: 7
- Manifest activities: `com.meishe.sdkdemo.selectmedia.SelectMediaActivity`
- Primary SDK imports: `com.meicam.sdk.NvsAVFileInfo`(2), `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.sdk.NvsVideoResolution`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(2), `NvsStreamingContext.AV_FILEINFO_EXTRA_INFO`(2), `NvsStreamingContext.getAVInfoFromFile`(2), `NvsAVFileInfo.AV_FILE_INFO_FLAGS_HAS_VIDEO_PART_IN_IMAGE`(1), `NvsAVFileInfo.ExtendsDataInfo`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/selectmedia/adapter/AgendaSimpleSectionAdapter.java` `Adapter` sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java` `Activity` manifest; sdk-import; 5 sdk-lines

### `urledit` Urledit

- Category: `audio-media`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 2
- SDK-related code lines: 4
- Manifest activities: `com.meishe.sdkdemo.urledit.UrlMaterialActivity`
- Primary SDK imports: `com.meicam.sdk.NvsAVFileInfo`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsVideoResolution`(1)
- Direct API/member tokens: `NvsStreamingContext.getAVInfoFromFile`(3)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java` `Activity` manifest; sdk-import; 4 sdk-lines

### `dialog` Dialog

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Pop`(1), `Dialog`(1)
- Method snippets from this feature's source files: 2
- SDK-related code lines: 6
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.sdk.NvsColor`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1), `NvsStreamingContext.CaptureDeviceCapability`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/dialog/CaptionEditPop.java` `Pop` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/dialog/TopMoreDialog.java` `Dialog` sdk-import; 3 sdk-lines

### `douvideo` DouVideo capture/edit workflow

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(5)
- Roles: `Activity`(3), `Class`(2)
- Method snippets from this feature's source files: 53
- SDK-related code lines: 141
- Manifest activities: `com.meishe.sdkdemo.douvideo.DouVideoCaptureActivity`, `com.meishe.sdkdemo.douvideo.DouVideoEditActivity`, `com.meishe.sdkdemo.douvideo.DouVideoTrimActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(4), `com.meicam.sdk.NvsVideoClip`(3), `com.meicam.sdk.NvsAVFileInfo`(3), `com.meicam.sdk.NvsTimeline`(3), `com.meicam.sdk.NvsLiveWindow`(2), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(2), `com.meicam.sdk.NvsVideoTrack`(2), `com.meicam.sdk.NvsMediaFileConvertor`(1), `com.meicam.sdk.NvsCaptureVideoFx`(1), `com.meicam.sdk.NvsFxDescription`(1), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsAudioClip`(1)
- Direct API/member tokens: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(6), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(5), `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0`(3), `NvsStreamingContext.getInstance`(2), `NvsStreamingContext.StreamingEngineCallback`(2), `NvsFxDescription.ParamInfoObject`(2), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`(2), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(2), `NvsVideoStreamInfo.VIDEO_ROTATION_90`(2), `NvsVideoStreamInfo.VIDEO_ROTATION_270`(2), `NvsVideoStreamInfo.VIDEO_ROTATION_180`(2), `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90`(2)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/douvideo/bean/RecordClip.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java` `Class` sdk-import; 6 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java` `Activity` manifest; sdk-import; 23 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java` `Activity` manifest; sdk-import; 87 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java` `Activity` manifest; sdk-import; 24 sdk-lines

### `edit` Edit

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(4)
- Roles: `Fragment`(2), `Activity`(2)
- Method snippets from this feature's source files: 62
- SDK-related code lines: 146
- Manifest activities: `com.meishe.sdkdemo.edit.VideoEditActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(4), `com.meicam.sdk.NvsTimeline`(4), `com.meicam.sdk.NvsTimelineAnimatedSticker`(2), `com.meicam.sdk.NvsRational`(2), `com.meicam.sdk.NvsTimelineVideoFx`(2), `com.meicam.sdk.NvsVideoClip`(2), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsAudioTrack`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsVideoTrack`(1), `com.meicam.sdk.NvsAnimatedSticker`(1), `com.meicam.sdk.NvsCaption`(1)
- Direct API/member tokens: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(7), `NvsStreamingContext.getInstance`(5), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`(5), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(4), `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`(3), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`(3), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(3), `NvsTimelineCaption.TEXT_ALIGNMENT_LEFT`(2), `NvsTimelineCaption.TEXT_ALIGNMENT_CENTER`(2), `NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT`(2), `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java` `Fragment` sdk-import; 18 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/EditBaseActivity.java` `Activity` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java` `Activity` manifest; sdk-import; 21 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java` `Fragment` sdk-import; 104 sdk-lines

### `edit-animatesticker` Edit Animatesticker

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(4)
- Roles: `Activity`(4)
- Method snippets from this feature's source files: 34
- SDK-related code lines: 87
- Manifest activities: `com.meishe.sdkdemo.edit.animatesticker.AnimatedStickerActivity`, `com.meishe.sdkdemo.edit.animatesticker.AnimatedStickerAnimationActivity`, `com.meishe.sdkdemo.edit.animatesticker.customsticker.CustomAnimateStickerActivity`, `com.meishe.sdkdemo.edit.animatesticker.customsticker.CustomAnimateStickerEffectActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(4), `com.meicam.sdk.NvsTimeline`(3), `com.meicam.sdk.NvsTimelineAnimatedSticker`(3), `com.meicam.sdk.NvsVideoTrack`(2), `com.meicam.sdk.NvsAVFileInfo`(2), `com.meicam.sdk.NvsSize`(2), `com.meicam.sdk.NvsAnimatedSticker`(1), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoResolution`(1)
- Direct API/member tokens: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(5), `NvsStreamingContext.getInstance`(4), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`(3), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(3), `NvsTimelineEditor.OnScrollChangeListener`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`(1), `NvsTimelineTimeSpan.OnTrimInChangeListener`(1), `NvsTimelineTimeSpan.OnTrimOutChangeListener`(1), `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`(1), `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java` `Activity` manifest; sdk-import; 60 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java` `Activity` manifest; sdk-import; 8 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerActivity.java` `Activity` manifest; sdk-import; 4 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java` `Activity` manifest; sdk-import; 15 sdk-lines

### `edit-caption` Edit Caption

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(3)
- Roles: `Activity`(2), `Presenter`(1)
- Method snippets from this feature's source files: 57
- SDK-related code lines: 271
- Manifest activities: `com.meishe.sdkdemo.edit.Caption.CaptionActivity`, `com.meishe.sdkdemo.edit.Caption.CaptionStyleActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(3), `com.meicam.sdk.NvsCaption`(2), `com.meicam.sdk.NvsControlPointPair`(2), `com.meicam.sdk.NvsTimeline`(2), `com.meicam.sdk.NvsTimelineCaption`(2), `com.meicam.sdk.NvsVideoTrack`(2), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(1), `com.meicam.sdk.NvsPointD`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsBodyOpacitySpan`(1), `com.meicam.sdk.NvsCaptionSpan`(1), `com.meicam.sdk.NvsColor`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(6), `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`(6), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(4), `NvsCaptionSpan.SPAN_TYPE_RENDER_ID`(4), `NvsCaptionSpan.SPAN_TYPE_NORMAL_TEXT`(4), `NvsCaptionSpan.SPAN_TYPE_OUTLINE_WIDTH`(4), `NvsCaptionSpan.SPAN_TYPE_FONT_FAMILY`(4), `NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY`(4), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(3), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(3), `NvsTimelineCaption.THEME_CATEGORY`(3), `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`(3)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java` `Activity` manifest; sdk-import; 63 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java` `Activity` manifest; sdk-import; 207 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/Caption/presenter/CaptionPresenter.java` `Presenter` sdk-import; 1 sdk-lines

### `edit-clipedit` Edit Clipedit

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(19)
- Roles: `Activity`(14), `Fragment`(2), `Class`(2), `View`(1)
- Method snippets from this feature's source files: 170
- SDK-related code lines: 388
- Manifest activities: `com.meishe.sdkdemo.edit.clipEdit.adjust.AdjustActivity`, `com.meishe.sdkdemo.edit.clipEdit.animatedSticker.ClipAnimatedStickerActivity`, `com.meishe.sdkdemo.edit.clipEdit.animatedSticker.ClipAnimatedStickerAnimationActivity`, `com.meishe.sdkdemo.edit.clipEdit.caption.ClipCaptionActivity`, `com.meishe.sdkdemo.edit.clipEdit.caption.ClipCaptionStyleActivity`, `com.meishe.sdkdemo.edit.clipEdit.correctionColor.CorrectionColorActivity`, `com.meishe.sdkdemo.edit.clipEdit.EditActivity`, `com.meishe.sdkdemo.edit.clipEdit.noise.NoiseSuppressionActivity`, `com.meishe.sdkdemo.edit.clipEdit.photo.DurationActivity`, `com.meishe.sdkdemo.edit.clipEdit.photo.PhotoMovementActivity`, `com.meishe.sdkdemo.edit.clipEdit.speed.SpeedActivity`, `com.meishe.sdkdemo.edit.clipEdit.spilt.SpiltActivity`
- Primary SDK imports: `com.meicam.sdk.NvsTimeline`(16), `com.meicam.sdk.NvsStreamingContext`(15), `com.meicam.sdk.NvsVideoClip`(13), `com.meicam.sdk.NvsVideoTrack`(13), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(7), `com.meicam.sdk.NvsAVFileInfo`(3), `com.meicam.sdk.NvsVideoResolution`(3), `com.meicam.sdk.NvsSize`(2), `com.meicam.sdk.NvsVideoFx`(2), `com.meicam.sdk.NvsLiveWindow`(2), `com.meicam.sdk.NvsClipAnimatedSticker`(2), `com.meicam.sdk.NvsCaption`(2)
- Direct API/member tokens: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(25), `NvsStreamingContext.getInstance`(21), `NvsConstants.AspectRatio`(20), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(18), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(13), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`(5), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(5), `NvsClipAnimatedSticker.getInPoint`(5), `NvsTimelineEditor.OnScrollChangeListener`(4), `NvsClipAnimatedSticker.removeKeyframeAtTime`(4), `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`(4), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`(3)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java` `Activity` manifest; sdk-import; 18 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CuttingMenuView.java` `View` 4 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java` `Fragment` sdk-import; 37 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/ICutRegionFragment.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java` `Activity` manifest; sdk-import; 66 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java` `Activity` manifest; sdk-import; 10 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java` `Activity` manifest; sdk-import; 64 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java` `Activity` manifest; sdk-import; 35 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java` `Activity` manifest; sdk-import; 14 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/EditActivity.java` `Activity` manifest; sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java` `Activity` manifest; sdk-import; 23 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/DurationActivity.java` `Activity` manifest; sdk-import; 6 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java` `Activity` manifest; sdk-import; 12 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java` `Fragment` sdk-import; 25 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java` `Activity` manifest; sdk-import; 21 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java` `Activity` manifest; sdk-import; 9 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltTimeSpan.java` `Class` sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java` `Activity` manifest; sdk-import; 17 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java` `Activity` manifest; sdk-import; 22 sdk-lines

### `edit-compoundcaption` Edit Compoundcaption

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(2)
- Method snippets from this feature's source files: 15
- SDK-related code lines: 49
- Manifest activities: `com.meishe.sdkdemo.edit.compoundcaption.CompoundCaptionActivity`, `com.meishe.sdkdemo.edit.compoundcaption.CompoundCaptionStyleActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsColor`(1), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsTimelineCompoundCaption`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(3), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(3), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(3), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(2), `NvsTimelineEditor.OnScrollChangeListener`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`(1), `NvsTimelineTimeSpan.OnTrimInChangeListener`(1), `NvsTimelineTimeSpan.OnTrimOutChangeListener`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java` `Activity` manifest; sdk-import; 47 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionStyleActivity.java` `Activity` manifest; sdk-import; 2 sdk-lines

### `edit-createpic` Edit Createpic

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 6
- SDK-related code lines: 20
- Manifest activities: `com.meishe.sdkdemo.edit.createPic.CreatePicActivity`
- Primary SDK imports: `com.meicam.sdk.NvsMultiThumbnailSequenceView`(1), `com.meicam.sdk.NvsRational`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(3), `NvsStreamingContext.getInstance`(2), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(2), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`(2), `NvsTimelineEditor.OnScrollChangeListener`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java` `Activity` manifest; sdk-import; 20 sdk-lines

### `edit-mask` Edit Mask

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(1), `Helper`(1)
- Method snippets from this feature's source files: 27
- SDK-related code lines: 66
- Manifest activities: `com.meishe.sdkdemo.edit.mask.MaskActivity`
- Primary SDK imports: `com.meicam.sdk.NvsAVFileInfo`(2), `com.meicam.sdk.NvsLiveWindow`(2), `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoFx`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsVideoTrack`(1), `com.meicam.sdk.NvsMaskRegionInfo`(1), `com.meicam.sdk.NvsPosition2D`(1)
- Direct API/member tokens: `NvsMaskRegionInfo.RegionInfo`(13), `NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON`(3), `NvsStreamingContext.getAVInfoFromFile`(2), `NvsMaskRegionInfo.Transform2D`(2), `NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE`(2), `NvsConstants.ANIMATION_POST_PACKAGE_ID`(1), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`(1), `NvsMaskRegionInfo.MASK_REGION_TYPE_ELLIPSE2D`(1), `NvsMaskRegionInfo.Ellipse2D`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java` `Activity` manifest; sdk-import; 24 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java` `Helper` sdk-import; 42 sdk-lines

### `edit-record` Edit Record

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(3)
- Roles: `Activity`(1), `Class`(1), `View`(1)
- Method snippets from this feature's source files: 21
- SDK-related code lines: 34
- Manifest activities: `com.meishe.sdkdemo.edit.record.RecordActivity`
- Primary SDK imports: `com.meicam.sdk.NvsMultiThumbnailSequenceView`(3), `com.meicam.sdk.NvsAudioClip`(1), `com.meicam.sdk.NvsAudioFx`(1), `com.meicam.sdk.NvsAudioTrack`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsTimelineAnimatedSticker`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(4), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(2), `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java` `Activity` manifest; sdk-import; 32 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/record/SqLayout.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/record/SqView.java` `View` sdk-import; 1 sdk-lines

### `edit-theme` Edit Theme

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 12
- SDK-related code lines: 29
- Manifest activities: `com.meishe.sdkdemo.edit.theme.ThemeActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsTimelineCaption`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsTimelineCaption.ROLE_IN_THEME_TITLE`(2), `NvsVideoClip.ROLE_IN_THEME_TITLE`(2), `NvsVideoClip.ROLE_IN_THEME_TRAILER`(2), `NvsTimelineCaption.THEME_CATEGORY`(2), `NvsStreamingContext.getInstance`(1), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(1), `NvsTimelineCaption.ROLE_IN_THEME_TRAILER`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(1), `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java` `Activity` manifest; sdk-import; 29 sdk-lines

### `edit-timelineeditor` Edit Timelineeditor

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(3)
- Roles: `Class`(3)
- Method snippets from this feature's source files: 9
- SDK-related code lines: 39
- Primary SDK imports: `com.meicam.sdk.NvsMultiThumbnailSequenceView`(2), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(1), `NvsMultiThumbnailSequenceView.OnScrollChangeListener`(1), `NvsTimelineTimeSpan.OnMarginChangeListener`(1), `NvsTimelineTimeSpanExt.OnMarginChangeListener`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java` `Class` sdk-import; 31 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpan.java` `Class` 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpanExt.java` `Class` sdk-import; 5 sdk-lines

### `edit-transition` Edit Transition

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 4
- SDK-related code lines: 11
- Manifest activities: `com.meishe.sdkdemo.edit.transition.TransitionActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1), `com.meicam.sdk.NvsVideoTransition`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1), `NvsVideoTransition.VIDEO_TRANSITION_TYPE_BUILTIN`(1), `NvsVideoTransition.VIDEO_TRANSITION_TYPE_PACKAGE`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java` `Activity` manifest; sdk-import; 11 sdk-lines

### `edit-watermark` Edit Watermark

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(3)
- Roles: `Activity`(2), `Util`(1)
- Method snippets from this feature's source files: 9
- SDK-related code lines: 11
- Manifest activities: `com.meishe.sdkdemo.edit.watermark.SingleClickActivity`, `com.meishe.sdkdemo.edit.watermark.WaterMarkActivity`
- Primary SDK imports: `com.meicam.sdk.NvsTimeline`(2), `com.meicam.sdk.NvsTimelineVideoFx`(2), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsStreamingContext`(1)
- Direct API/member tokens: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`(1), `NvsTimeline.NvsTimelineWatermarkPosition_TopRight`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/watermark/SingleClickActivity.java` `Activity` manifest; sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java` `Activity` manifest; sdk-import; 6 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java` `Util` sdk-import; 4 sdk-lines

### `flipcaption` Flipcaption

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(2)
- Method snippets from this feature's source files: 5
- SDK-related code lines: 15
- Manifest activities: `com.meishe.sdkdemo.flipcaption.FlipCaptionActivity`, `com.meishe.sdkdemo.flipcaption.FlipCaptionEditActivity`
- Primary SDK imports: `com.meicam.sdk.NvsColor`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsTimelineVideoFx`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java` `Activity` manifest; sdk-import; 15 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionEditActivity.java` `Activity` manifest

### `musiclyrics` Music lyrics workflow

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(2)
- Method snippets from this feature's source files: 7
- SDK-related code lines: 19
- Manifest activities: `com.meishe.sdkdemo.musicLyrics.MultiVideoSelectActivity`, `com.meishe.sdkdemo.musicLyrics.MusicLyricsActivity`
- Primary SDK imports: `com.meicam.sdk.NvsAudioTrack`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsTimelineCaption`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE`(1), `NvsStreamingContext.getInstance`(1), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MultiVideoSelectActivity.java` `Activity` manifest
  - `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java` `Activity` manifest; sdk-import; 19 sdk-lines

### `photoalbum` Photo album workflow

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(2)
- Method snippets from this feature's source files: 11
- SDK-related code lines: 43
- Manifest activities: `com.meishe.sdkdemo.photoalbum.PhotoAlbumActivity`, `com.meishe.sdkdemo.photoalbum.PhotoAlbumPreviewActivity`
- Primary SDK imports: `com.meicam.sdk.NvsAVFileInfo`(1), `com.meicam.sdk.NvsAudioResolution`(1), `com.meicam.sdk.NvsLiveWindow`(1), `com.meicam.sdk.NvsRational`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(3), `NvsStreamingContext.PlaybackCallback`(2), `NvsStreamingContext.PlaybackCallback2`(2), `NvsStreamingContext.StreamingEngineCallback`(2), `NvsStreamingContext.CompileCallback`(2), `NvsStreamingContext.CompileCallback2`(2), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(2), `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN`(1), `NvsVideoClip.ClIP_BACKGROUNDMODE_BLUR`(1), `NvsStreamingContext.ImageGrabberCallback`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumActivity.java` `Activity` manifest
  - `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java` `Activity` manifest; sdk-import; 43 sdk-lines

### `quicksplicing` Quick splicing / passthrough convert

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 6
- SDK-related code lines: 20
- Manifest activities: `com.meishe.sdkdemo.quicksplicing.FileQuickSplicingActivity`
- Primary SDK imports: `com.meicam.sdk.NvsMultiThumbnailSequenceView`(1), `com.meicam.sdk.NvsPassthroughConvertor`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsPassthroughConvertor.NvsPassthroughFileInfo`(3), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(3), `NvsStreamingContext.getInstance`(1), `NvsPassthroughConvertor.PassthroughConvertorCallback`(1), `NvsTimelineTimeSpanExt.OnTrimInChangeListener`(1), `NvsTimelineTimeSpanExt.OnTrimOutChangeListener`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java` `Activity` manifest; sdk-import; 20 sdk-lines

### `themeshoot` Theme shoot workflow

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(9)
- Roles: `Activity`(4), `Class`(3), `Bean`(1), `View`(1)
- Method snippets from this feature's source files: 37
- SDK-related code lines: 132
- Manifest activities: `com.meishe.sdkdemo.themeshoot.ThemeCaptureActivity`, `com.meishe.sdkdemo.themeshoot.ThemeEditCaptionActivity`, `com.meishe.sdkdemo.themeshoot.ThemePreviewActivity`, `com.meishe.sdkdemo.themeshoot.ThemeSelectActivity`
- Primary SDK imports: `com.meicam.sdk.NvsLiveWindow`(5), `com.meicam.sdk.NvsTimelineVideoFx`(3), `com.meicam.sdk.NvsRational`(3), `com.meicam.sdk.NvsStreamingContext`(3), `com.meicam.sdk.NvsTimeline`(3), `com.meicam.sdk.NvsVideoTrack`(3), `com.meicam.sdk.NvsTimelineCompoundCaption`(2), `com.meicam.sdk.NvsAVFileInfo`(2), `com.meicam.sdk.NvsAudioResolution`(2), `com.meicam.sdk.NvsVideoClip`(2), `com.meicam.sdk.NvsVideoResolution`(2), `com.meicam.sdk.NvsAssetPackageManager`(1)
- Direct API/member tokens: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`(4), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE`(3), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(3), `NvsStreamingContext.getInstance`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(2), `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT`(2), `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME`(2), `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_LOW_PIPELINE_SIZE`(2), `NvsStreamingContext.PlaybackCallback`(2), `NvsStreamingContext.CaptureRecordingDurationCallback`(1), `NvsStreamingContext.CaptureDeviceCapability`(1), `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java` `Bean` sdk-import; 6 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java` `Activity` manifest; sdk-import; 27 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeEditCaptionActivity.java` `Activity` manifest
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java` `Activity` manifest; sdk-import; 42 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeSelectActivity.java` `Activity` manifest
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java` `Class` sdk-import; 14 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCaptureLiveWindow.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java` `View` sdk-import; 41 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemePreviewLiveWindow.java` `Class` sdk-import; 1 sdk-lines

### `utils-datainfo` Utils Datainfo

- Category: `captions-stickers`
- Coverage: `method-snippets`
- Modules: `app`(6)
- Roles: `Class`(5), `Data`(1)
- Method snippets from this feature's source files: 10
- SDK-related code lines: 21
- Primary SDK imports: `com.meicam.sdk.NvsVideoClip`(2), `com.meicam.sdk.NvsVideoFx`(2), `com.meicam.sdk.NvsCaptionSpan`(1), `com.meicam.sdk.NvsVideoStreamInfo`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsVideoTransition`(1), `com.meicam.sdk.NvsColor`(1)
- Direct API/member tokens: `NvsVideoStreamInfo.VIDEO_ROTATION_0`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/CaptionInfo.java` `Class` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/ClipInfo.java` `Class` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java` `Class` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java` `Data` sdk-import; 6 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TransitionInfo.java` `Class` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/VideoClipFxInfo.java` `Class` sdk-import; 3 sdk-lines

### `feedback` Feedback

- Category: `core-lifecycle`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 2
- SDK-related code lines: 1
- Manifest activities: `com.meishe.sdkdemo.feedback.FeedBackActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(1)
- Direct API/member tokens: `NvsStreamingContext.SdkVersion`(1), `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/feedback/FeedBackActivity.java` `Activity` manifest; sdk-import; 1 sdk-lines

### `libnet` Libnet

- Category: `core-lifecycle`
- Coverage: `method-snippets`
- Modules: `libNet`(2)
- Roles: `Callback`(1), `Class`(1)
- Method snippets from this feature's source files: 2
- SDK-related code lines: 8
- Direct API/member tokens: `NvsServerClient.get`(3)
- Source labels:
  - `libNet/src/main/java/com/meishe/net/custom/JsonCallback.java` `Callback` 3 sdk-lines
  - `libNet/src/main/java/com/meishe/net/NvsServerClient.java` `Class` 5 sdk-lines

### `main` Main

- Category: `core-lifecycle`
- Coverage: `manifest-only`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 0
- SDK-related code lines: 0
- Manifest activities: `com.meishe.sdkdemo.main.MainWebViewActivity`
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/main/MainWebViewActivity.java` `Activity` manifest

### `repository` Repository

- Category: `core-lifecycle`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Class`(1)
- Method snippets from this feature's source files: 2
- SDK-related code lines: 1
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/repository/AppRepository.java` `Class` sdk-import; 1 sdk-lines

### `utils-permission` Utils Permission

- Category: `core-lifecycle`
- Coverage: `manifest-only`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 0
- SDK-related code lines: 0
- Manifest activities: `com.meishe.sdkdemo.utils.permission.PermissionsActivity`
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/utils/permission/PermissionsActivity.java` `Activity` manifest

### `base` Base

- Category: `effects-transforms`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(1), `Manager`(1)
- Method snippets from this feature's source files: 15
- SDK-related code lines: 27
- Primary SDK imports: `com.meicam.effect.sdk.NvsEffectSdkContext`(1), `com.meicam.sdk.NvsStreamingContext`(1)
- Direct API/member tokens: `NvsServerClient.get`(12), `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`(1), `NvsStreamingContext.class`(1), `NvsStreamingContext.getInstance`(1), `NvsEffectSdkContext.class`(1), `NvsEffectSdkContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java` `Activity` sdk-import; 15 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java` `Manager` 12 sdk-lines

### `bean` Bean

- Category: `effects-transforms`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Class`(1)
- Method snippets from this feature's source files: 2
- SDK-related code lines: 3
- Primary SDK imports: `com.meicam.sdk.NvsColor`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java` `Class` sdk-import; 3 sdk-lines

### `edit-anim` Edit Anim

- Category: `effects-transforms`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(1), `Adapter`(1)
- Method snippets from this feature's source files: 13
- SDK-related code lines: 34
- Manifest activities: `com.meishe.sdkdemo.edit.anim.AnimationActivity`
- Primary SDK imports: `com.meicam.sdk.NvsTimeline`(2), `com.meicam.sdk.NvsVideoClip`(2), `com.meicam.sdk.NvsVideoTrack`(2), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsVideoFx`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java` `Activity` manifest; sdk-import; 30 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationClipAdapter.java` `Adapter` sdk-import; 4 sdk-lines

### `edit-background` Edit Background

- Category: `effects-transforms`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(1), `View`(1)
- Method snippets from this feature's source files: 10
- SDK-related code lines: 37
- Manifest activities: `com.meishe.sdkdemo.edit.background.BackgroundActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoResolution`(1), `com.meicam.sdk.NvsVideoTrack`(1), `com.meicam.sdk.NvsColor`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java` `Activity` manifest; sdk-import; 36 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/background/view/MultiColorView.java` `View` sdk-import; 1 sdk-lines

### `edit-data` Edit Data

- Category: `effects-transforms`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Class`(1), `Data`(1)
- Method snippets from this feature's source files: 3
- SDK-related code lines: 6
- Primary SDK imports: `com.meicam.sdk.NvsColor`(1), `com.meicam.sdk.NvsMaskRegionInfo`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/data/FilterItem.java` `Class` sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/edit/data/mask/MaskInfoData.java` `Data` sdk-import; 3 sdk-lines

### `makecover` Make cover workflow

- Category: `effects-transforms`
- Coverage: `method-snippets`
- Modules: `app`(2)
- Roles: `Activity`(1), `Fragment`(1)
- Method snippets from this feature's source files: 14
- SDK-related code lines: 44
- Manifest activities: `com.meishe.sdkdemo.makecover.MakeCoverActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.sdk.NvsTimeline`(2), `com.meicam.sdk.NvsVideoClip`(2), `com.meicam.sdk.NvsVideoFx`(2), `com.meicam.sdk.NvsVideoTrack`(2), `com.meicam.sdk.NvsRational`(1), `com.meicam.sdk.NvsLiveWindow`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(3), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(3), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(3), `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE`(1), `NvsVideoClip.VIDEO_CLIP_TYPE_AV`(1), `NvsStreamingContext.PlaybackCallback`(1), `NvsStreamingContext.PlaybackCallback2`(1), `NvsStreamingContext.StreamingEngineCallback`(1), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`(1), `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT`(1), `NvsVideoFx.VIDEOFX_TYPE_BUILTIN`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java` `Activity` manifest; sdk-import; 15 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java` `Fragment` sdk-import; 29 sdk-lines

### `edit-livephoto` Edit Livephoto

- Category: `preview-export`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 5
- SDK-related code lines: 15
- Manifest activities: `com.meishe.sdkdemo.edit.livephoto.LivePhotoActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(1), `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`(1), `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java` `Activity` manifest; sdk-import; 15 sdk-lines

### `sequencenesting` Sequencenesting

- Category: `preview-export`
- Coverage: `method-snippets`
- Modules: `app`(1)
- Roles: `Activity`(1)
- Method snippets from this feature's source files: 9
- SDK-related code lines: 20
- Manifest activities: `com.meishe.sdkdemo.sequenceNesting.SequenceNestingActivity`
- Primary SDK imports: `com.meicam.sdk.NvsMultiThumbnailSequenceView`(1), `com.meicam.sdk.NvsRational`(1), `com.meicam.sdk.NvsStreamingContext`(1), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoTrack`(1)
- Direct API/member tokens: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(3), `NvsStreamingContext.getInstance`(1), `NvsStreamingContext.CompileCallback`(1), `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`(1)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java` `Activity` manifest; sdk-import; 20 sdk-lines

### `activity` Activity

- Category: `template-mimo-cutsame`
- Coverage: `method-snippets`
- Modules: `app`(4)
- Roles: `Activity`(4)
- Method snippets from this feature's source files: 6
- SDK-related code lines: 31
- Manifest activities: `com.meishe.sdkdemo.activity.BeautyActivity`, `com.meishe.sdkdemo.activity.CutSameActivity`, `com.meishe.sdkdemo.activity.MainActivity`, `com.meishe.sdkdemo.activity.SettingActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(3), `com.meicam.sdk.NvsTimeline`(1), `com.meicam.sdk.NvsLiveWindow`(1), `com.meicam.sdk.NvsVideoResolution`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(3), `NvsLiveWindow.HDR_DISPLAY_MODE_SDR`(3), `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT`(3), `NvsLiveWindow.HDR_DISPLAY_MODE_DEPEND_DEVICE`(2), `NvsLiveWindow.HDR_DISPLAY_MODE_TONE_MAP_SDR`(2), `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_16_BIT_FLOAT`(2), `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_AUTO`(2), `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH`(2), `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH`(2), `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_EXTREMELY_HIGH`(2), `NvsConstants.SIZE_4K_WIDTH`(2), `NvsConstants.SIZE_4K_HEIGHT`(2)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java` `Activity` manifest; sdk-import; 5 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/activity/CutSameActivity.java` `Activity` manifest
  - `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java` `Activity` manifest; sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java` `Activity` manifest; sdk-import; 23 sdk-lines

### `ar-scene` AR scene beauty module

- Category: `template-mimo-cutsame`
- Coverage: `method-snippets`
- Modules: `MArScene`(4)
- Roles: `Fragment`(2), `Manager`(1), `Helper`(1)
- Method snippets from this feature's source files: 39
- SDK-related code lines: 61
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(2), `com.meicam.nvconvertorlib.Logger`(2), `com.meicam.sdk.NvsAssetPackageManager`(1), `com.meicam.sdk.NvsCaptureVideoFx`(1), `com.meicam.sdk.NvsFx`(1), `com.meicam.sdk.NvsVideoClip`(1), `com.meicam.sdk.NvsVideoFx`(1)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(2), `NvsStreamingContext.hasARModule`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(2), `NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH`(1), `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`(1), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`(1)
- Source labels:
  - `MArScene/src/main/java/com/meishe/arscene/BeautyDataManager.java` `Manager` sdk-import; 3 sdk-lines
  - `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java` `Helper` sdk-import; 58 sdk-lines
  - `MArScene/src/main/java/com/meishe/arscene/BeautyTabFragment.java` `Fragment` sdk-import
  - `MArScene/src/main/java/com/meishe/arscene/template/BeautyEditTabFragment.java` `Fragment` sdk-import

### `cutsame-template` CutSame/template module

- Category: `template-mimo-cutsame`
- Coverage: `method-snippets`
- Modules: `MCutSame`(21)
- Roles: `Activity`(8), `Fragment`(4), `Class`(2), `View`(2), `Presenter`(2), `Adapter`(1), `Util`(1), `Dialog`(1)
- Method snippets from this feature's source files: 70
- SDK-related code lines: 252
- Manifest activities: `com.meishe.cutsame.CutCompileActivity`, `com.meishe.cutsame.CutSameEditorActivity`, `com.meishe.cutsame.MaterialSelectActivity`, `com.meishe.cutsame.TailorActivity`, `com.meishe.cutsame.TailorFreeActivity`, `com.meishe.cutsame.TemplatePreviewActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(10), `com.meicam.sdk.NvsTimeline`(8), `com.meicam.sdk.NvsVideoClip`(6), `com.meicam.sdk.NvsAssetPackageManager`(5), `com.meicam.sdk.NvsVideoTrack`(3), `com.meicam.sdk.NvsRational`(2), `com.meicam.sdk.NvsTimelineCaption`(2), `com.meicam.sdk.NvsVideoResolution`(2), `com.meicam.sdk.NvsAVFileInfo`(2), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(2), `com.meicam.sdk.NvsAudioClip`(1), `com.meicam.sdk.NvsAudioTrack`(1)
- Direct API/member tokens: `NvsServerClient.get`(7), `NvsConstants.AspectRatio`(7), `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720`(6), `NvsStreamingContext.getInstance`(6), `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo`(5), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(4), `NvsStreamingContext.ImageGrabberCallback`(3), `NvsStreamingContext.templateFootageInfo`(3), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(3), `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360`(2), `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480`(2), `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080`(2)
- Source labels:
  - `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java` `Activity` manifest; sdk-import; 14 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java` `Activity` manifest; sdk-import; 51 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java` `Class` 7 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java` `Activity` sdk-import; 31 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java` `Activity` sdk-import; 12 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/adapter/CutVideoAdapter.java` `Adapter` sdk-import; 4 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java` `Fragment` sdk-import; 13 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java` `Fragment` sdk-import; 12 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java` `Fragment` sdk-import; 7 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/iview/CutEditorVpView.java` `View` sdk-import; 1 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java` `Class` sdk-import; 25 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutSameEditorPresenter.java` `Presenter` sdk-import; 4 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/TemplatePresenter.java` `Presenter` sdk-import; 2 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/fragment/TemplateFragment.java` `Fragment` sdk-import; 1 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/MaterialSelectActivity.java` `Activity` manifest; sdk-import; 1 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java` `Activity` manifest; sdk-import; 8 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java` `Activity` manifest; sdk-import; 30 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/TemplatePreviewActivity.java` `Activity` manifest; sdk-import; 5 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/util/ExportTemplateUtil.java` `Util` 1 sdk-lines
  - `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java` `Dialog` sdk-import; 8 sdk-lines

### `engine-meishe` Engine Meishe

- Category: `template-mimo-cutsame`
- Coverage: `method-snippets`
- Modules: `libEngine`(45)
- Roles: `Class`(36), `Data`(3), `Util`(3), `Controller`(1), `Manager`(1), `View`(1)
- Method snippets from this feature's source files: 293
- SDK-related code lines: 868
- Primary SDK imports: `com.meicam.sdk.NvsTimeline`(13), `com.meicam.sdk.NvsVideoResolution`(10), `com.meicam.sdk.NvsVideoClip`(8), `com.meicam.sdk.NvsAVFileInfo`(8), `com.meicam.sdk.NvsStreamingContext`(8), `com.meicam.sdk.NvsVideoTrack`(7), `com.meicam.sdk.NvsVideoFx`(6), `com.meicam.sdk.NvsTimelineCompoundCaption`(6), `com.meicam.sdk.NvsAudioTrack`(5), `com.meicam.sdk.NvsColor`(5), `com.meicam.sdk.NvsTimelineCaption`(5), `com.meicam.sdk.NvsRational`(5)
- Direct API/member tokens: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(26), `NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST`(18), `NvsUtils.checkFunctionInMainThread`(16), `NvsStreamingContext.getInstance`(10), `NvsConstants.ADJUST_TINT`(9), `NvsConstants.AspectRatio`(8), `NvsConstants.POST_PACKAGE_ID`(8), `NvsConstants.KEY_VIDEO_MODE`(8), `NvsAssetPackageManager.NvsTemplateFootageDesc`(8), `NvsConstants.KEY_BACKGROUND_MODE`(7), `NvsAssetPackageManager.NvsTemplateCaptionDesc`(7), `NvsConstants.KEY_BACKGROUND_COLOR`(6)
- Source labels:
  - `libEngine/src/main/java/com/meishe/engine/bean/background/MeicamStoryboardInfo.java` `Class` sdk-import; 4 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/ClipInfo.java` `Class` 1 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java` `Data` 6 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java` `Class` sdk-import; 12 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioFx.java` `Class` sdk-import; 1 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioTrack.java` `Class` sdk-import; 3 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java` `Class` sdk-import; 32 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java` `Class` sdk-import; 20 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamMaskRegionInfo.java` `Class` sdk-import; 3 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java` `Class` sdk-import; 6 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java` `Class` sdk-import; 5 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java` `Class` sdk-import; 7 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java` `Class` sdk-import; 145 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java` `Class` sdk-import; 20 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoTrack.java` `Class` sdk-import; 4 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/MeicamWaterMark.java` `Class` sdk-import; 2 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/NvsObject.java` `Class` 3 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageCorrespondingClipInfo.java` `Class` sdk-import; 2 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageDesc.java` `Class` sdk-import; 3 sdk-lines
  - `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java` `Class` sdk-import; 13 sdk-lines

### `mimodemo` Mimo demo workflow

- Category: `template-mimo-cutsame`
- Coverage: `method-snippets`
- Modules: `app`(22)
- Roles: `Activity`(8), `Class`(8), `Util`(3), `Data`(1), `Manager`(1), `Fragment`(1)
- Method snippets from this feature's source files: 73
- SDK-related code lines: 266
- Manifest activities: `com.meishe.sdkdemo.mimodemo.common.permission.PermissionsActivity`, `com.meishe.sdkdemo.mimodemo.CompoundCaptionEditorActivity`, `com.meishe.sdkdemo.mimodemo.mediapaker.SelectMediaActivity`, `com.meishe.sdkdemo.mimodemo.MimoActivity`, `com.meishe.sdkdemo.mimodemo.MimoEditActivity`, `com.meishe.sdkdemo.mimodemo.TrimEditActivity`
- Primary SDK imports: `com.meicam.sdk.NvsStreamingContext`(7), `com.meicam.sdk.NvsTimeline`(6), `com.meicam.sdk.NvsVideoResolution`(5), `com.meicam.sdk.NvsTimelineCompoundCaption`(4), `com.meicam.sdk.NvsTimelineAnimatedSticker`(3), `com.meicam.sdk.NvsMultiThumbnailSequenceView`(3), `com.meicam.sdk.NvsAssetPackageManager`(2), `com.meicam.sdk.NvsTimelineCaption`(2), `com.meicam.sdk.NvsVideoClip`(2), `com.meicam.sdk.NvsVideoTrack`(2), `com.meicam.sdk.NvsAVFileInfo`(2), `com.meicam.sdk.NvsMediaFileConvertor`(2)
- Direct API/member tokens: `NvsStreamingContext.getInstance`(12), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`(6), `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`(4), `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`(3), `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`(3), `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`(3), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`(2), `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`(2), `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR`(2), `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED`(2)
- Source labels:
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/base/BaseEditActivity.java` `Activity` sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java` `Activity` sdk-import; 4 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/ClipInfo.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java` `Data` sdk-import; 6 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/permission/PermissionsActivity.java` `Activity` manifest
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java` `Class` sdk-import; 12 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java` `Manager` sdk-import; 7 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/CaptionUtil.java` `Util` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/ImageConverter.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoCommonUtil.java` `Util` sdk-import; 4 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java` `Util` sdk-import; 100 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java` `Class` sdk-import; 26 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpan.java` `Class` 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpanExt.java` `Class` sdk-import; 5 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/CompoundCaptionEditorActivity.java` `Activity` manifest
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/adapter/BaseRecyclerHolder.java` `Class` sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/adapter/BottomMenuViewHolder.java` `Class` sdk-import; 2 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/SelectMediaActivity.java` `Activity` manifest; sdk-import; 3 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoActivity.java` `Activity` manifest; sdk-import; 1 sdk-lines
  - `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java` `Activity` manifest; sdk-import; 16 sdk-lines
