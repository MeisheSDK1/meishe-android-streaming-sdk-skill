# Demo Reuse Inventory

This inventory preserves reusable knowledge discovered from the Android demo without requiring the demo folder at skill use time.
Use it to understand coverage, integration patterns, and where the simple snippets came from.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Module Coverage](#module-coverage)
- [Android Integration Patterns From Demo](#android-integration-patterns-from-demo)
- [Top SDK Classes](#top-sdk-classes)
- [Top Static Constants And Calls](#top-static-constants-and-calls)
- [SDK-Bearing Source Files](#sdk-bearing-source-files)
<!-- END GENERATED CONTENTS -->

## Module Coverage

| Module | Java files | SDK-bearing Java files | Simple snippets |
| --- | ---: | ---: | ---: |
| `MArScene` | 32 | 2 | 39 |
| `MCutSame` | 73 | 22 | 70 |
| `MMakeup` | 27 | 3 | 40 |
| `app` | 660 | 175 | 1021 |
| `libBase` | 222 | 15 | 26 |
| `libEngine` | 123 | 38 | 293 |
| `libNet` | 89 | 2 | 2 |

## Android Integration Patterns From Demo

### Gradle And Modules

Modules: `:app`, `:libBase`, `:libEngine`, `:libNet`, `:MArScene`, `:MCutSame`, `:MMakeup`

Version settings:
- `extCompileSdkVersion: 33`
- `extMinSdkVersion: 19`
- `extTargetSdkVersion: 35`
- `extBuildToolsVersion: "33.0.3"`

Reusable build patterns:
- Use `flatDir { dirs './libs' }` for local SDK JAR/AAR artifacts.
- Configure `ndk.abiFilters` for `arm64-v8a` and optionally `armeabi-v7a`.
- Enable multidex for the full demo dependency set.
- Compile with Java 8 source/target compatibility.
- The demo enables Android data binding; generated minimal apps only need it when requested.

Public dependency coordinates seen in demo config. Copy only what the generated app actually uses:
- extAndroidMultidex: `androidx.multidex:multidex:2.0.0`
- extConstraintLayout: `androidx.constraintlayout:constraintlayout:1.1.3`
- extAppcompat: `androidx.appcompat:appcompat:1.0.0`
- extAnnotation: `androidx.annotation:annotation:1.1.0`
- extAppcompatRecycler: `androidx.recyclerview:recyclerview:1.1.0`
- extAndroidXDesign: `com.google.android.material:material:1.0.0`
- extMutilDex: `androidx.multidex:multidex:2.0.0`
- extFresco: `com.facebook.fresco:fresco:1.12.0`
- extSoloader: `com.facebook.soloader:soloader:0.10.4`
- extFrescoGif: `com.facebook.fresco:animated-gif:1.12.0`
- extFrescoWebp: `com.facebook.fresco:animated-webp:1.12.0`
- extFrescoWebpSupport: `com.facebook.fresco:webpsupport:1.12.0`
- extBumptechGlide: `com.github.bumptech.glide:glide:4.11.0`
- extGlideAnnotation: `com.github.bumptech.glide:compiler:4.11.0`
- extWebpdecoder: `com.zlc.glide:webpdecoder:1.4.4.9.0`
- extGoogleGson: `com.google.code.gson:gson:2.8.5`
- extLifecycleCompiler: `androidx.lifecycle:lifecycle-compiler:2.2.0`
- extLifecycleKtx: `androidx.lifecycle:lifecycle-runtime-ktx:2.2.0`
- extLifecycleExtensions: `androidx.lifecycle:lifecycle-extensions:2.2.0`
- extDagger: `com.google.dagger:dagger:2.24`
- extDaggerCompiler: `com.google.dagger:dagger-compiler:2.24`
- extDaggerAndroid: `com.google.dagger:dagger-android:2.24`
- extDaggerAndroidProcessor: `com.google.dagger:dagger-android-processor:2.24`
- extRxjava: `io.reactivex.rxjava2:rxjava:2.2.8`
- extRxandroid: `io.reactivex.rxjava2:rxandroid:2.1.1`
- extSmartRefresh: `com.scwang.smart:refresh-layout-kernel:2.0.1`
- extSmartRefreshHorizontal: `com.scwang.smart:refresh-layout-horizontal:2.0.0`
- extSmartRefreshClassics: `com.scwang.smart:refresh-header-classics:2.0.1`
- extAndroidTestRunner: `androidx.test.ext:junit:1.1.1`
- extTestJunit: `junit:junit:4.12`
- extTestEspresso: `androidx.test.espresso:espresso-core:3.2.0`

### Manifest Patterns

Permissions seen in the full demo. Generated apps should request only the selected capability needs:
- `android.permission.ACCESS_MEDIA_LOCATION`
- `android.permission.ACCESS_NETWORK_STATE`
- `android.permission.ACCESS_NOTIFICATION_POLICY`
- `android.permission.ACCESS_WIFI_STATE`
- `android.permission.CAMERA`
- `android.permission.CHANGE_WIFI_STATE`
- `android.permission.INTERNET`
- `android.permission.READ_EXTERNAL_STORAGE`
- `android.permission.READ_MEDIA_AUDIO`
- `android.permission.READ_MEDIA_IMAGES`
- `android.permission.READ_MEDIA_VIDEO`
- `android.permission.RECORD_AUDIO`
- `android.permission.VIBRATE`
- `android.permission.WRITE_EXTERNAL_STORAGE`

Application attributes seen in demo:
- `android:largeHeap=true`
- `android:requestLegacyExternalStorage=true`
- `android:usesCleartextTraffic=true`
- `android:allowBackup=false`

Activity declarations: 86 total. Use as feature coverage evidence, not as a minimal-app manifest.

Do not copy demo signing configs, analytics keys, FTP upload tasks, private package suffixes, or release flavor metadata into generated apps.

## Top SDK Classes

| Class | Occurrences |
| --- | ---: |
| `NvsStreamingContext` | 970 |
| `NvsTimeline` | 688 |
| `NvsVideoClip` | 428 |
| `NvsConstants` | 342 |
| `NvsVideoTrack` | 262 |
| `NvsAssetPackageManager` | 251 |
| `NvsVideoFx` | 200 |
| `NvsTimelineCaption` | 175 |
| `NvsColor` | 171 |
| `NvsVideoResolution` | 168 |
| `NvsMultiThumbnailSequenceView` | 156 |
| `NvsTimelineTimeSpan` | 156 |
| `NvsAVFileInfo` | 102 |
| `NvsLiveWindow` | 94 |
| `NvsRational` | 93 |
| `NvsTimelineCompoundCaption` | 90 |
| `NvsTimelineAnimatedSticker` | 77 |
| `NvsCaptionSpan` | 73 |
| `NvsAudioClip` | 70 |
| `NvsTimelineVideoFx` | 66 |
| `NvsMaskRegionInfo` | 63 |
| `NvsTimelineEditor` | 59 |
| `NvsCaptureVideoFx` | 58 |
| `NvsFx` | 55 |
| `NvsSize` | 52 |
| `NvsAudioTrack` | 49 |
| `NvsTimelineTimeSpanExt` | 44 |
| `NvsClipCaption` | 43 |
| `NvsVideoTransition` | 43 |
| `NvsClipAnimatedSticker` | 41 |
| `NvsCaption` | 38 |
| `NvsControlPointPair` | 36 |
| `NvsAudioResolution` | 35 |
| `NvsPointD` | 35 |
| `NvsServerClient` | 33 |
| `NvsExpressionParam` | 31 |
| `NvsEffectSdkContext` | 30 |
| `NvsVideoStreamInfo` | 28 |
| `NvsMediaFileConvertor` | 26 |
| `NvsAudioFx` | 24 |
| `NvsStreamingContextUtil` | 23 |
| `NvsFxDescription` | 21 |
| `NvsObject` | 19 |
| `NvsARSceneManipulate` | 18 |
| `NvsLiveWindowExt` | 17 |
| `NvsUtils` | 17 |
| `NvsPosition2D` | 15 |
| `NvsColorSpan` | 15 |
| `NvsCaptureSceneInfo` | 14 |
| `NvsAnimatedSticker` | 13 |
| `NvsFaceDetector` | 12 |
| `NvsNormalTextSpan` | 12 |
| `NvsShadowOpacitySpan` | 12 |
| `NvsAssetPackageParticleDescParser` | 11 |
| `NvsOutlineWidthSpan` | 10 |
| `NvsVideoFrameRetriever` | 9 |
| `NvsBodyOpacitySpan` | 9 |
| `NvsOutlineColorSpan` | 9 |
| `NvsTemplateCaptionDesc` | 9 |
| `NvsCaptureCompoundCaption` | 8 |
| `NvsFontFamilySpan` | 8 |
| `NvsFontSizeRatioSpan` | 8 |
| `NvsItalicSpan` | 8 |
| `NvsOutlineOpacitySpan` | 8 |
| `NvsRendererIdSpan` | 8 |
| `NvsUnderlineSpan` | 8 |
| `NvsTemplateFootageDesc` | 8 |
| `NvsTemplateFootageCorrespondingClipInfo` | 8 |
| `NvsIconGenerator` | 8 |
| `NvsPassthroughConvertor` | 7 |
| `NvsOpacitySpan` | 7 |
| `NvsCaptureAnimatedSticker` | 5 |
| `NvsError` | 5 |
| `NvsArbitraryData` | 5 |
| `NvsTemplateCompoundCaptionDesc` | 5 |
| `NvsEffect` | 4 |
| `NvsEffectRenderCore` | 4 |
| `NvsParticleSystemContext` | 4 |
| `NvsAIContext` | 4 |
| `NvsCompoundCaption` | 4 |
| `NvsVideoEffect` | 3 |
| `NvsVideoFrameInfo` | 3 |
| `NvsPassthroughFileInfo` | 3 |
| `NvsClipCompoundCaption` | 3 |
| `NvsMakeupEffectInfo` | 3 |
| `NvsVideoEffectAnimatedSticker` | 2 |
| `NvsVideoEffectCompoundCaption` | 2 |
| `NvsCaptureAudioFx` | 2 |
| `NvsFaceData` | 2 |
| `NvsFaceFeatureInfo` | 2 |
| `NvsPanAndScan` | 2 |
| `NvsVolume` | 2 |
| `NvsTrackCaption` | 2 |
| `NvsTemplateCompoundCaptionItemDesc` | 2 |
| `NvsARSceneManipulateCallback` | 1 |
| `NvsFaceBoundingRectInfo` | 1 |
| `NvsHandFeatureInfo` | 1 |
| `NvsTimelineWatermarkPosition_TopRight` | 1 |
| `NvsStreaming` | 1 |
| `NvsTimelineWatermarkPosition_TopLeft` | 1 |

## Top Static Constants And Calls

| Token | Occurrences |
| --- | ---: |
| `NvsStreamingContext.getInstance` | 142 |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK` | 84 |
| `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc` | 66 |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER` | 65 |
| `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE` | 43 |
| `NvsConstants.AspectRatio` | 36 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX` | 33 |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER` | 26 |
| `NvsServerClient.get` | 23 |
| `NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST` | 18 |
| `NvsFxDescription.ParamInfoObject` | 17 |
| `NvsStreamingContext.PlaybackCallback` | 16 |
| `NvsStreamingContext.StreamingEngineCallback` | 16 |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING` | 16 |
| `NvsUtils.checkFunctionInMainThread` | 16 |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING` | 15 |
| `NvsStreamingContextUtil.getInstance` | 15 |
| `NvsMaskRegionInfo.RegionInfo` | 15 |
| `NvsStreamingContext.PlaybackCallback2` | 14 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER` | 14 |
| `NvsStreamingContext.CompileCallback` | 12 |
| `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE` | 12 |
| `NvsVideoClip.VIDEO_CLIP_TYPE_AV` | 10 |
| `NvsTimelineEditor.OnScrollChangeListener` | 10 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE` | 10 |
| `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT` | 9 |
| `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR` | 9 |
| `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED` | 9 |
| `NvsStreamingContext.getAVInfoFromFile` | 9 |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME` | 9 |
| `NvsTimelineCaption.THEME_CATEGORY` | 9 |
| `NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D` | 9 |
| `NvsConstants.ADJUST_TINT` | 9 |
| `NvsConstants.POST_PACKAGE_ID` | 9 |
| `NvsStreamingContext.hasARModule` | 8 |
| `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME` | 8 |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW` | 8 |
| `NvsStreamingContext.CompileCallback2` | 8 |
| `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE` | 8 |
| `NvsStreamingContext.ImageGrabberCallback` | 8 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION` | 8 |
| `NvsTimelineCaption.ROLE_IN_THEME_GENERAL` | 8 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE` | 8 |
| `NvsConstants.KEY_VIDEO_MODE` | 8 |
| `NvsAssetPackageManager.NvsTemplateFootageDesc` | 8 |
| `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo` | 8 |
| `NvsAssetPackageManager.NvsTemplateCaptionDesc` | 8 |
| `NvsStreamingContext.CaptureRecordingDurationCallback` | 7 |
| `NvsStreamingContext.CaptureDeviceCapability` | 7 |
| `NvsVideoStreamInfo.VIDEO_ROTATION_90` | 7 |
| `NvsVideoStreamInfo.VIDEO_ROTATION_270` | 7 |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER` | 7 |
| `NvsTimelineTimeSpan.OnTrimInChangeListener` | 7 |
| `NvsTimelineTimeSpan.OnTrimOutChangeListener` | 7 |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME` | 7 |
| `NvsConstants.KEY_MASK_GENERATOR_TYPE` | 7 |
| `NvsConstants.KEY_MASK_GENERATOR` | 7 |
| `NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY` | 7 |
| `NvsConstants.KEY_BACKGROUND_MODE` | 7 |
| `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE` | 6 |
| `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | 6 |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM` | 6 |
| `NvsStreamingContext.CaptureDeviceCallback` | 6 |
| `NvsStreamingContext.CaptureRecordingStartedCallback` | 6 |
| `NvsCaptureSceneInfo.ClipData` | 6 |
| `NvsAssetPackageManager.AssetPackageManagerCallback` | 6 |
| `NvsAVFileInfo.AV_FILE_TYPE_IMAGE` | 6 |
| `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN` | 6 |
| `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN` | 6 |
| `NvsCaptionSpan.SPAN_TYPE_FONT_FAMILY` | 6 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME` | 6 |
| `NvsConstants.KEY_BACKGROUND_COLOR` | 6 |
| `NvsConstants.IS_POST_STORY_BOARD_3D` | 6 |
| `NvsConstants.PACKAGE_EFFECT_IN` | 6 |
| `NvsConstants.PACKAGE_EFFECT_OUT` | 6 |
| `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720` | 6 |
| `NvsStreamingContext.SdkVersion` | 5 |
| `NvsStreamingContext.initHumanDetectionExt` | 5 |
| `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | 5 |
| `NvsLiveWindow.HDR_DISPLAY_MODE_SDR` | 5 |
| `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT` | 5 |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE` | 5 |
| `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0` | 5 |
| `NvsVideoFx.VIDEOFX_TYPE_BUILTIN` | 5 |
| `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE` | 5 |
| `NvsConstants.Crop` | 5 |
| `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH` | 5 |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME` | 5 |
| `NvsClipAnimatedSticker.getInPoint` | 5 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP` | 5 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH` | 5 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP` | 5 |
| `NvsConstants.VALUE_COLOR_BACKGROUND_MODE` | 5 |
| `NvsConstants.KEY_BACKGROUND_BLUR_RADIUS` | 5 |
| `NvsStreamingContext.templateFootageInfo` | 5 |
| `NvsEffectSdkContext.initHumanDetectionExt` | 4 |
| `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH` | 4 |
| `NvsExpressionParam.TYPE_COLOR` | 4 |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME` | 4 |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE` | 4 |
| `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME` | 4 |
| `NvsMediaFileConvertor.MeidaFileConvertorCallback` | 4 |
| `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR` | 4 |
| `NvsTimelineCaption.TEXT_ALIGNMENT_LEFT` | 4 |
| `NvsTimelineCaption.TEXT_ALIGNMENT_CENTER` | 4 |
| `NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT` | 4 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE` | 4 |
| `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION` | 4 |
| `NvsConstants.PROPERTY_KEY_BACKGROUND_MODE` | 4 |
| `NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM` | 4 |
| `NvsConstants.KEY_CROPPER_SCALE_X` | 4 |
| `NvsConstants.KEY_CROPPER_SCALE_Y` | 4 |
| `NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON` | 4 |
| `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME` | 4 |
| `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED` | 4 |
| `NvsCaptionSpan.SPAN_TYPE_RENDER_ID` | 4 |
| `NvsCaptionSpan.SPAN_TYPE_NORMAL_TEXT` | 4 |
| `NvsCaptionSpan.SPAN_TYPE_OUTLINE_WIDTH` | 4 |
| `NvsMultiThumbnailSequenceView.OnScrollChangeListener` | 4 |
| `NvsClipAnimatedSticker.removeKeyframeAtTime` | 4 |
| `NvsConstants.KEY_BACKGROUND_MUTLISAMPLE` | 4 |
| `NvsConstants.FX_TRANSFORM_2D_SCALE_X` | 4 |
| `NvsConstants.FX_TRANSFORM_2D_SCALE_Y` | 4 |
| `NvsConstants.FX_TRANSFORM_2D_TRANS_X` | 4 |
| `NvsConstants.FX_TRANSFORM_2D_TRANS_Y` | 4 |
| `NvsConstants.FX_TRANSFORM_2D_ROTATION` | 4 |
| `NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc` | 4 |
| `NvsObject.TEMPLATE_KEY_BEST_SEEK_TIME` | 4 |
| `NvsStreamingContext.setupHumanDetectionData` | 3 |
| `NvsEffectSdkContext.setupHumanDetectionData` | 3 |
| `NvsStreamingContext.class` | 3 |
| `NvsEffectSdkContext.getInstance` | 3 |
| `NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT` | 3 |
| `NvsExpressionParam.TYPE_FLOAT` | 3 |
| `NvsExpressionParam.FloatParam` | 3 |
| `NvsExpressionParam.TYPE_INT` | 3 |
| `NvsExpressionParam.IntParam` | 3 |
| `NvsExpressionParam.TYPE_BOOLEAN` | 3 |
| `NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED` | 3 |
| `NvsVideoStreamInfo.VIDEO_ROTATION_180` | 3 |

## SDK-Bearing Source Files

| Source label | SDK lines | Snippets | Top SDK classes |
| --- | ---: | ---: | --- |
| `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java` | 387 | 53 | `NvsConstants`, `NvsVideoFx`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack`, `NvsColor` |
| `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java` | 248 | 25 | `NvsCaptionSpan`, `NvsColor`, `NvsColorSpan`, `NvsNormalTextSpan`, `NvsShadowOpacitySpan`, `NvsOutlineWidthSpan` |
| `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java` | 246 | 52 | `NvsStreamingContext`, `NvsTimeline`, `NvsAssetPackageManager`, `NvsVideoClip`, `NvsVideoTrack`, `NvsObject` |
| `libEngine/src/main/java/com/meishe/engine/EditorEngine.java` | 190 | 100 | `NvsStreamingContext`, `NvsTimelineCaption`, `NvsVideoClip`, `NvsVideoTrack`, `NvsTimelineAnimatedSticker`, `NvsConstants` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java` | 157 | 13 | `NvsConstants`, `NvsVideoClip`, `NvsVideoFx`, `NvsVideoTrack`, `NvsStreamingContext`, `NvsARSceneManipulate` |
| `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java` | 118 | 48 | `NvsStreamingContext`, `NvsTimelineCaption`, `NvsTimeline`, `NvsTimelineCompoundCaption`, `NvsCaption`, `NvsClipAnimatedSticker` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java` | 117 | 11 | `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsStreamingContext`, `NvsVideoFx`, `NvsTimelineCaption` |
| `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java` | 112 | 29 | `NvsStreamingContext`, `NvsCaptureVideoFx`, `NvsExpressionParam`, `NvsCaptureSceneInfo`, `NvsColor`, `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java` | 107 | 30 | `NvsVideoClip`, `NvsTimeline`, `NvsStreamingContext`, `NvsVideoTrack`, `NvsVideoStreamInfo`, `NvsMultiThumbnailSequenceView` |
| `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java` | 86 | 24 | `NvsTimeline`, `NvsConstants`, `NvsVideoResolution`, `NvsTimelineCaption`, `NvsAudioTrack`, `NvsTimelineVideoFx` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java` | 76 | 24 | `NvsClipAnimatedSticker`, `NvsTimelineTimeSpan`, `NvsStreamingContext`, `NvsMultiThumbnailSequenceView`, `NvsTimeline`, `NvsTimelineEditor` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java` | 76 | 30 | `NvsClipCaption`, `NvsPointD`, `NvsTimelineTimeSpan`, `NvsControlPointPair`, `NvsStreamingContext`, `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java` | 75 | 29 | `NvsTimelineCaption`, `NvsPointD`, `NvsTimelineTimeSpan`, `NvsControlPointPair`, `NvsStreamingContext`, `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java` | 74 | 1 | `NvsFxDescription`, `NvsTimelineVideoFx`, `NvsTimeline`, `NvsVideoFx`, `NvsTimelineAnimatedSticker`, `NvsTimelineCaption` |
| `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java` | 70 | 24 | `NvsTimelineTimeSpan`, `NvsTimelineAnimatedSticker`, `NvsStreamingContext`, `NvsMultiThumbnailSequenceView`, `NvsTimeline`, `NvsTimelineEditor` |
| `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java` | 67 | 38 | `NvsCaptureVideoFx`, `NvsVideoClip`, `NvsVideoFx`, `NvsFx`, `NvsAssetPackageManager`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java` | 65 | 24 | `NvsStreamingContext`, `NvsTimelineCaption`, `NvsTimeline`, `NvsTimelineCompoundCaption`, `NvsTimelineAnimatedSticker`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java` | 59 | 18 | `NvsStreamingContext`, `NvsTimeline`, `NvsAssetPackageParticleDescParser`, `NvsAVFileInfo`, `NvsMultiThumbnailSequenceView`, `NvsParticleSystemContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java` | 58 | 15 | `NvsTimelineCompoundCaption`, `NvsStreamingContext`, `NvsTimelineTimeSpan`, `NvsColor`, `NvsMultiThumbnailSequenceView`, `NvsTimeline` |
| `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java` | 57 | 11 | `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack`, `NvsStreamingContext` |
| `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java` | 56 | 36 | `NvsVideoClip`, `NvsFx`, `NvsCaptureVideoFx`, `NvsColor`, `NvsVideoFx`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java` | 54 | 16 | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsTimelineCompoundCaption`, `NvsRational`, `NvsTimelineVideoFx` |
| `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java` | 52 | 11 | `NvsStreamingContext`, `NvsTimeline`, `NvsRational`, `NvsVideoClip`, `NvsAudioResolution`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java` | 52 | 13 | `NvsVideoFx`, `NvsVideoClip`, `NvsTimeline`, `NvsVideoTrack`, `NvsAVFileInfo`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java` | 49 | 2 | `NvsRational`, `NvsTimeline`, `NvsAudioResolution`, `NvsStreamingContext`, `NvsVideoResolution`, `NvsAVFileInfo` |
| `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java` | 47 | 15 | `NvsMaskRegionInfo`, `NvsLiveWindow`, `NvsPosition2D`, `NvsAVFileInfo`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java` | 45 | 6 | `NvsExpressionParam`, `NvsStreamingContext`, `NvsTimeline`, `NvsColor`, `NvsVideoFx`, `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java` | 44 | 17 | `NvsColor`, `NvsClipCaption`, `NvsStreamingContext`, `NvsCaption`, `NvsTimeline`, `NvsControlPointPair` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java` | 43 | 8 | `NvsConstants`, `NvsStreamingContext`, `NvsVideoFx`, `NvsAVFileInfo`, `NvsSize`, `NvsVideoClip` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java` | 43 | 14 | `NvsStreamingContext`, `NvsTimeline`, `NvsConstants`, `NvsLiveWindow`, `NvsLiveWindowExt`, `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java` | 43 | 9 | `NvsTimelineTimeSpan`, `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt`, `NvsTimelineEditor`, `NvsStreamingContext`, `NvsTimeline` |
| `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java` | 43 | 19 | `NvsVideoClip`, `NvsVideoTrack`, `NvsConstants`, `NvsVideoResolution`, `NvsTimeline`, `NvsAudioTrack` |
| `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java` | 42 | 3 | `NvsStreamingContext`, `NvsEffectSdkContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java` | 41 | 9 | `NvsVideoTrack`, `NvsVideoClip`, `NvsTimeline`, `NvsStreamingContext`, `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java` | 41 | 20 | `NvsAudioClip`, `NvsStreamingContext`, `NvsTimeline`, `NvsAudioFx`, `NvsAudioTrack`, `NvsMultiThumbnailSequenceView` |
| `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java` | 40 | 9 | `NvsStreamingContext`, `NvsAudioClip`, `NvsVideoClip`, `NvsTimeline`, `NvsMediaFileConvertor`, `NvsAudioTrack` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java` | 39 | 8 | `NvsVideoClip`, `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsTimelineCaption`, `NvsTimeline`, `NvsAVFileInfo` |
| `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java` | 38 | 17 | `NvsAudioClip`, `NvsStreamingContext`, `NvsTimeline`, `NvsMultiThumbnailSequenceView`, `NvsAudioTrack`, `NvsVideoClip` |
| `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java` | 38 | 9 | `NvsTimelineTimeSpan`, `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt`, `NvsTimelineEditor` |
| `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java` | 37 | 7 | `NvsTimeline`, `NvsTimelineTimeSpan`, `NvsMultiThumbnailSequenceView`, `NvsStreamingContext`, `NvsTimelineEditor`, `NvsVideoClip` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java` | 37 | 7 | `NvsTimelineTimeSpan`, `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt`, `NvsTimelineEditor` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java` | 37 | 18 | `NvsTimelineCaption`, `NvsColor`, `NvsTimeline`, `NvsVideoResolution`, `NvsCaption` |
| `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java` | 36 | 16 | `NvsTimeline`, `NvsStreamingContext`, `NvsStreamingContextUtil`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java` | 36 | 11 | `NvsVideoTrack`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoFx`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java` | 36 | 9 | `NvsStreamingContext`, `NvsRational`, `NvsAssetPackageManager`, `NvsAVFileInfo`, `NvsLiveWindow`, `NvsVideoStreamInfo` |
| `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java` | 35 | 5 | `NvsStreamingContext`, `NvsCaptureSceneInfo`, `NvsCaptureVideoFx`, `NvsAssetPackageManager`, `NvsColor`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java` | 35 | 10 | `NvsStreamingContext`, `NvsTimeline`, `NvsLiveWindow`, `NvsVideoFx`, `NvsVideoClip`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java` | 34 | 12 | `NvsTimelineCaption`, `NvsVideoClip`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java` | 33 | 12 | `NvsVideoClip`, `NvsVideoTrack`, `NvsTimeline`, `NvsStreamingContext`, `NvsAVFileInfo`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java` | 32 | 3 | `NvsStreamingContext`, `NvsTimeline`, `NvsAssetPackageManager`, `NvsTimelineAnimatedSticker`, `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java` | 31 | 10 | `NvsVideoClip`, `NvsTimeline`, `NvsTimelineTimeSpan`, `NvsMultiThumbnailSequenceView`, `NvsStreamingContext`, `NvsTimelineEditor` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java` | 31 | 13 | `NvsStreamingContext`, `NvsMultiThumbnailSequenceView`, `NvsTimeline`, `NvsVideoClip`, `NvsAudioFx`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java` | 29 | 10 | `NvsStreamingContext`, `NvsCaptureVideoFx`, `NvsFxDescription`, `NvsLiveWindow`, `NvsAVFileInfo`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java` | 29 | 8 | `NvsTimeline`, `NvsStreamingContext`, `NvsVideoTrack`, `NvsAudioTrack`, `NvsRational`, `NvsTimelineVideoFx` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java` | 29 | 11 | `NvsStreamingContext`, `NvsMultiThumbnailSequenceView`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack`, `NvsTimelineEditor` |
| `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java` | 29 | 14 | `NvsUtils`, `NvsIconGenerator`, `NvsStreamingContext`, `NvsAVFileInfo`, `NvsRational`, `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java` | 28 | 4 | `NvsStreamingContext`, `NvsLiveWindow`, `NvsVideoResolution`, `NvsConstants` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java` | 28 | 11 | `NvsStreamingContext`, `NvsTimeline`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java` | 28 | 4 | `NvsStreamingContext`, `NvsVideoStreamInfo`, `NvsAVFileInfo`, `NvsAssetPackageManager`, `NvsAssetPackageParticleDescParser`, `NvsCaptureVideoFx` |
| `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java` | 28 | 6 | `NvsPassthroughConvertor`, `NvsTimeline`, `NvsTimelineTimeSpanExt`, `NvsMultiThumbnailSequenceView`, `NvsStreamingContext`, `NvsTimelineEditor` |
| `app/src/main/java/com/meishe/sdkdemo/utils/Util.java` | 28 | 3 | `NvsVideoResolution`, `NvsSize`, `NvsClipCaption`, `NvsTimelineCaption`, `NvsAVFileInfo`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java` | 27 | 6 | `NvsStreamingContext`, `NvsMultiThumbnailSequenceView`, `NvsTimeline`, `NvsTimelineEditor`, `NvsRational`, `NvsVideoClip` |
| `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java` | 27 | 7 | `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack`, `NvsVideoFx`, `NvsARSceneManipulate` |
| `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java` | 26 | 9 | `NvsFx`, `NvsTimeline`, `NvsStreamingContext`, `NvsVideoClip`, `NvsVideoFx`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java` | 26 | 9 | `NvsStreamingContext`, `NvsTimeline`, `NvsSize` |
| `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java` | 26 | 9 | `NvsTimeline`, `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsStreamingContext`, `NvsVideoClip`, `NvsRational` |
| `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java` | 26 | 2 | `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java` | 25 | 10 | `NvsTimeline`, `NvsAudioFx`, `NvsVideoClip`, `NvsVideoTrack`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java` | 25 | 12 | `NvsVideoClip`, `NvsVideoTrack`, `NvsStreamingContext`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java` | 25 | 9 | `NvsVideoClip`, `NvsVideoFx`, `NvsVideoTrack`, `NvsColor`, `NvsStreamingContext`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java` | 25 | 7 | `NvsTimeline`, `NvsTimelineCaption`, `NvsStreamingContext`, `NvsAudioTrack`, `NvsVideoTrack`, `NvsAssetPackageManager` |
| `libBase/src/main/java/com/meishe/utils/NvAsset.java` | 25 | 2 | `NvsAssetPackageManager` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java` | 25 | 6 | `NvsVideoFx`, `NvsConstants`, `NvsArbitraryData`, `NvsMaskRegionInfo`, `NvsVideoClip`, `NvsObject` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java` | 24 | 5 | `NvsTimelineTimeSpanExt`, `NvsTimeline`, `NvsMultiThumbnailSequenceView`, `NvsStreamingContext`, `NvsTimelineEditor`, `NvsVideoClip` |
| `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java` | 24 | 4 | `NvsFaceDetector`, `NvsAIContext`, `NvsVideoResolution`, `NvsRational`, `NvsFaceData` |
| `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java` | 24 | 10 | `NvsTimeline`, `NvsStreamingContext`, `NvsVideoResolution`, `NvsLiveWindowExt` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java` | 23 | 2 | `NvsTimelineCompoundCaption`, `NvsColor`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java` | 22 | 6 | `NvsTimeline`, `NvsStreamingContext`, `NvsAssetPackageManager`, `NvsTimelineAnimatedSticker` |
| `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java` | 22 | 5 | `NvsTimeline`, `NvsVideoResolution`, `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext`, `NvsTimelineAnimatedSticker` |
| `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java` | 22 | 5 | `NvsTimeline`, `NvsStreamingContext`, `NvsTimelineVideoFx`, `NvsVideoResolution`, `NvsColor`, `NvsVideoClip` |
| `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java` | 22 | 1 | `NvsStreamingContext`, `NvsStreamingContextUtil`, `NvsCaptureVideoFx`, `NvsLiveWindow`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java` | 22 | 12 | `NvsTimeline`, `NvsStreamingContext`, `NvsTimelineCompoundCaption`, `NvsAVFileInfo`, `NvsTimelineAnimatedSticker`, `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java` | 22 | 7 | `NvsVideoClip`, `NvsTimeline`, `NvsVideoTransition`, `NvsAudioClip`, `NvsVideoTrack`, `NvsAudioTrack` |
| `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java` | 21 | 5 | `NvsMultiThumbnailSequenceView`, `NvsFx`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java` | 21 | 4 | `NvsTimeline`, `NvsVideoClip`, `NvsStreamingContext`, `NvsRational`, `NvsVideoFx`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java` | 19 | 10 | `NvsStreamingContext`, `NvsVideoFx`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java` | 19 | 5 | `NvsStreamingContext`, `NvsTimeline`, `NvsAssetPackageManager`, `NvsTimelineVideoFx`, `NvsExpressionParam` |
| `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java` | 19 | 5 | `NvsTimeline`, `NvsStreamingContext`, `NvsVideoClip`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java` | 18 | 4 | `NvsVideoClip`, `NvsStreamingContext`, `NvsAVFileInfo`, `NvsSize`, `NvsTimeline`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java` | 18 | 4 | `NvsMediaFileConvertor`, `NvsMultiThumbnailSequenceView`, `NvsTimelineEditor`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` |
| `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java` | 18 | 8 | `NvsAssetPackageManager`, `NvsCaption`, `NvsCompoundCaption`, `NvsTemplateCaptionDesc`, `NvsTemplateCompoundCaptionDesc`, `NvsTemplateCompoundCaptionItemDesc` |
| `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java` | 17 | 7 | `NvsStreamingContext`, `NvsTimeline`, `NvsRational` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java` | 17 | 2 | `NvsConstants`, `NvsLiveWindow`, `NvsVideoResolution` |
| `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java` | 17 | 0 | `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java` | 17 | 6 | `NvsStreamingContext`, `NvsEffectSdkContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java` | 17 | 4 | `NvsVideoTransition`, `NvsStreamingContext`, `NvsVideoClip`, `NvsTimeline`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java` | 17 | 0 | `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java` | 16 | 7 | `NvsTimeline`, `NvsStreamingContext`, `NvsAVFileInfo`, `NvsSize`, `NvsVideoTrack`, `NvsTimelineAnimatedSticker` |
| `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java` | 16 | 3 | `NvsStreamingContext`, `NvsStreamingContextUtil`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java` | 16 | 3 | `NvsExpressionParam`, `NvsTimeline`, `NvsColor` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java` | 16 | 6 | `NvsAudioClip`, `NvsAudioFx`, `NvsAudioTrack`, `NvsVolume` |
| `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java` | 15 | 3 | `NvsStreamingContext`, `NvsStreamingContextUtil`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java` | 15 | 4 | `NvsTimeline`, `NvsClipAnimatedSticker`, `NvsStreamingContext`, `NvsVideoClip`, `NvsVideoTrack` |
| `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java` | 14 | 5 | `NvsStreamingContext`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java` | 14 | 6 | `NvsStreamingContext`, `NvsTimeline`, `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java` | 14 | 0 | `NvsMultiThumbnailSequenceView`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java` | 13 | 0 | `NvsIconGenerator` |
| `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java` | 13 | 9 | `NvsServerClient` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java` | 13 | 2 | `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java` | 13 | 4 | `NvsTimeline`, `NvsStreamingContext`, `NvsAVFileInfo`, `NvsSize`, `NvsTimelineAnimatedSticker` |
| `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java` | 13 | 3 | `NvsRational`, `NvsVideoResolution`, `NvsConstants` |
| `libEngine/src/main/java/com/meishe/engine/local/LMeicamVideoClip.java` | 13 | 1 | `NvsVideoFx`, `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext`, `NvsVideoClip`, `NvsVideoResolution` |
| `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java` | 13 | 3 | `NvsRational`, `NvsVideoResolution`, `NvsConstants` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java` | 11 | 3 | `NvsVideoClip`, `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java` | 11 | 1 | `NvsAssetPackageManager`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneEffectView.java` | 11 | 2 | `NvsAssetPackageManager`, `NvsStreamingContext`, `NvsCaptureVideoFx` |
| `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java` | 11 | 4 | `NvsTimeline`, `NvsStreamingContext`, `NvsTimelineAnimatedSticker` |
| `app/src/main/java/com/meishe/sdkdemo/MSApplication.java` | 10 | 1 | `NvsStreamingContext`, `NvsEffectSdkContext`, `NvsServerClient` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/DurationActivity.java` | 10 | 3 | `NvsStreamingContext`, `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` |
| `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java` | 9 | 1 | `NvsTimeline` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutSameEditorPresenter.java` | 9 | 1 | `NvsAudioResolution`, `NvsRational`, `NvsStreamingContext`, `NvsTimeline`, `NvsVideoResolution` |
| `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java` | 9 | 1 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java` | 9 | 2 | `NvsAssetPackageManager`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java` | 9 | 6 | `NvsFx` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java` | 9 | 3 | `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java` | 9 | 3 | `NvsMediaFileConvertor`, `NvsAVFileInfo`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java` | 9 | 7 | `NvsTimeline`, `NvsStreamingContext`, `NvsTimelineVideoFx` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java` | 9 | 1 | `NvsAssetPackageManager`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java` | 9 | 2 | `NvsAssetPackageManager`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java` | 9 | 2 | `NvsVideoFx`, `NvsVideoClip` |
| `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java` | 9 | 3 | `NvsARSceneManipulate`, `NvsFx`, `NvsFaceFeatureInfo`, `NvsARSceneManipulateCallback`, `NvsFaceBoundingRectInfo`, `NvsHandFeatureInfo` |
| `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java` | 9 | 2 | `NvsAssetPackageManager`, `NvsStreamingContext` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java` | 9 | 1 | `NvsVideoTransition`, `NvsVideoTrack`, `NvsObject` |
| `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java` | 9 | 3 | `NvsColor` |
| `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java` | 9 | 2 | `NvsMediaFileConvertor`, `NvsAVFileInfo`, `NvsStreamingContext` |
| `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java` | 8 | 7 | `NvsServerClient` |
| `app/src/main/java/com/meishe/sdkdemo/picinpic/PicturInPicturePreviewActivity.java` | 8 | 4 | `NvsTimeline`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java` | 8 | 1 | `NvsAVFileInfo`, `NvsStreamingContext`, `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java` | 8 | 3 | `NvsTimelineCompoundCaption`, `NvsTimelineVideoFx` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java` | 8 | 2 | `NvsTimelineAnimatedSticker`, `NvsTimeline` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java` | 8 | 2 | `NvsTimelineVideoFx`, `NvsLiveWindowExt`, `NvsTimeline` |
| `MCutSame/src/main/java/com/meishe/cutsame/TemplatePreviewActivity.java` | 7 | 1 | `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo` |
| `MCutSame/src/main/java/com/meishe/cutsame/bean/Template.java` | 7 | 0 | `NvsAssetPackageManager` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/adapter/CutVideoAdapter.java` | 7 | 1 | `NvsVideoClip`, `NvsAssetPackageManager` |
| `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java` | 7 | 3 | `NvsAssetPackageManager`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java` | 7 | 0 | `NvsStreamingContext`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationClipAdapter.java` | 7 | 2 | `NvsTimeline`, `NvsVideoClip`, `NvsVideoTrack` |
| `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerActivity.java` | 7 | 1 | `NvsStreamingContext`, `NvsAVFileInfo`, `NvsSize` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java` | 7 | 4 | `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java` | 7 | 2 | `NvsAVFileInfo`, `NvsStreamingContext`, `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/utils/StoryboardUtil.java` | 7 | 0 | `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext`, `NvsVideoClip` |
| `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java` | 7 | 3 | `NvsVideoResolution` |
| `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java` | 7 | 1 | `NvsConstants` |
| `MCutSame/src/main/java/com/meishe/cutsame/MaterialSelectActivity.java` | 6 | 0 | `NvsAssetPackageManager`, `NvsAVFileInfo` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseFragment.java` | 6 | 0 | `NvsEffectSdkContext`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseHorizontalLoadMoreAndRefreshFragment.java` | 6 | 0 | `NvsEffectSdkContext`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java` | 6 | 3 | `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/dialog/CaptionEditPop.java` | 6 | 1 | `NvsStreamingContext`, `NvsColor` |
| `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpanExt.java` | 6 | 0 | `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt` |
| `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java` | 6 | 1 | `NvsTimeline`, `NvsTimelineVideoFx`, `NvsTimelineWatermarkPosition_TopRight` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpanExt.java` | 6 | 0 | `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt` |
| `app/src/main/java/com/meishe/sdkdemo/utils/ParameterSettingValues.java` | 6 | 1 | `NvsLiveWindow`, `NvsStreamingContext`, `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/ClipInfo.java` | 6 | 0 | `NvsVideoClip`, `NvsVideoFx`, `NvsVideoStreamInfo` |
| `libBase/src/main/java/com/meishe/base/constants/NvsConstants.java` | 6 | 0 | `NvsVideoClip`, `NvsConstants` |
| `libBase/src/main/java/com/meishe/base/utils/Utils.java` | 6 | 2 | `NvsStreamingContext`, `NvsFx` |
| `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpanExt.java` | 6 | 0 | `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoTrack.java` | 6 | 1 | `NvsVideoTrack`, `NvsTimeline` |
| `libEngine/src/main/java/com/meishe/engine/bean/background/MeicamStoryboardInfo.java` | 6 | 1 | `NvsVideoFx`, `NvsVideoClip` |
| `libEngine/src/main/java/com/meishe/engine/interf/VideoFragmentListener.java` | 6 | 0 | `NvsTimeline` |
| `libEngine/src/main/java/com/meishe/engine/util/WhiteList.java` | 6 | 2 | `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/CaptureEffectTabFragment.java` | 5 | 1 | `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/edit/EditBaseActivity.java` | 5 | 0 | `NvsStreamingContext`, `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CuttingMenuView.java` | 5 | 0 | `NvsConstants` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java` | 5 | 3 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoCommonUtil.java` | 5 | 0 | `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpan.java` | 5 | 1 | `NvsTimelineTimeSpan`, `NvsMultiThumbnailSequenceView` |
| `libBase/src/main/java/com/meishe/utils/ColorUtil.java` | 5 | 0 | `NvsColor` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioTrack.java` | 5 | 1 | `NvsAudioTrack`, `NvsTimeline` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamWaterMark.java` | 5 | 1 | `NvsLiveWindowExt`, `NvsTimeline`, `NvsVideoResolution` |
| `libNet/src/main/java/com/meishe/net/NvsServerClient.java` | 5 | 1 | `NvsServerClient` |
| `MArScene/src/main/java/com/meishe/arscene/BeautyDataManager.java` | 4 | 1 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java` | 4 | 2 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java` | 4 | 2 | `NvsColor` |
| `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneBottomView.java` | 4 | 0 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/dialog/TopMoreDialog.java` | 4 | 1 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/data/FilterItem.java` | 4 | 1 | `NvsColor` |
| `app/src/main/java/com/meishe/sdkdemo/edit/data/mask/MaskInfoData.java` | 4 | 2 | `NvsMaskRegionInfo` |
| `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpan.java` | 4 | 0 | `NvsTimelineTimeSpan` |
| `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java` | 4 | 4 | `NvsColor` |
| `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectActivity.java` | 4 | 1 | `NvsCaptureVideoFx`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/SelectMediaActivity.java` | 4 | 2 | `NvsMediaFileConvertor` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/adapter/BottomMenuViewHolder.java` | 4 | 0 | `NvsAVFileInfo`, `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/selectmedia/adapter/AgendaSimpleSectionAdapter.java` | 4 | 0 | `NvsStreamingContext`, `NvsAVFileInfo` |
| `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/CaptionInfo.java` | 4 | 2 | `NvsCaptionSpan` |
| `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TransitionInfo.java` | 4 | 2 | `NvsVideoTransition` |
| `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/VideoClipFxInfo.java` | 4 | 1 | `NvsColor` |
| `app/src/main/java/com/meishe/sdkdemo/view/FaceUPropView.java` | 4 | 0 | `NvsStreamingContext`, `NvsAssetPackageManager` |
| `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpan.java` | 4 | 0 | `NvsTimelineTimeSpan` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamMaskRegionInfo.java` | 4 | 2 | `NvsMaskRegionInfo` |
| `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageDesc.java` | 4 | 1 | `NvsAssetPackageManager`, `NvsTemplateFootageDesc` |
| `libEngine/src/main/java/com/meishe/engine/local/LMeicamCompoundCaptionClip.java` | 4 | 1 | `NvsColor`, `NvsTimelineCompoundCaption` |
| `libEngine/src/main/java/com/meishe/engine/local/LMeicamMaskRegionInfo.java` | 4 | 2 | `NvsMaskRegionInfo` |
| `libNet/src/main/java/com/meishe/net/custom/JsonCallback.java` | 4 | 1 | `NvsServerClient` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/iview/CutEditorVpView.java` | 3 | 0 | `NvsAssetPackageManager` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/TemplatePresenter.java` | 3 | 2 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java` | 3 | 3 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneFragment.java` | 3 | 1 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/EditActivity.java` | 3 | 3 | `NvsAVFileInfo` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltTimeSpan.java` | 3 | 1 | `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionStyleActivity.java` | 3 | 0 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/filter/KeyFramePointView.java` | 3 | 1 | `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/base/BaseEditActivity.java` | 3 | 0 | `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/adapter/BaseRecyclerHolder.java` | 3 | 0 | `NvsStreamingContext`, `NvsVideoFrameRetriever` |
| `app/src/main/java/com/meishe/sdkdemo/view/MakeUpSingleView.java` | 3 | 2 | `NvsColor` |
| `libBase/src/main/java/com/meishe/base/view/MSLiveWindow.java` | 3 | 0 | `NvsLiveWindow` |
| `libEngine/src/main/java/com/meishe/engine/bean/NvsObject.java` | 3 | 0 | `NvsObject` |
| `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageCorrespondingClipInfo.java` | 3 | 1 | `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo` |
| `libEngine/src/main/java/com/meishe/engine/constant/NvsConstants.java` | 3 | 0 | `NvsConstants` |
| `libEngine/src/main/java/com/meishe/engine/interf/StreamingConstant.java` | 3 | 0 | `NvsVideoClip` |
| `MCutSame/src/main/java/com/meishe/cutsame/fragment/TemplateFragment.java` | 2 | 0 | `NvsStreamingContext` |
| `MCutSame/src/main/java/com/meishe/cutsame/util/ExportTemplateUtil.java` | 2 | 4 | `NvsConstants` |
| `MMakeup/src/main/java/com/meishe/makeup/utils/DataConvertUtils.java` | 2 | 1 | `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCaptureFragment.java` | 2 | 1 | `NvsFx` |
| `app/src/main/java/com/meishe/sdkdemo/capture/viewmodel/CaptureEffectTabViewModel.java` | 2 | 2 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/douvideo/bean/RecordClip.java` | 2 | 0 | `NvsVideoClip` |
| `app/src/main/java/com/meishe/sdkdemo/edit/Caption/presenter/CaptionPresenter.java` | 2 | 3 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/edit/background/view/MultiColorView.java` | 2 | 1 | `NvsColor` |
| `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/ICutRegionFragment.java` | 2 | 0 | `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicSqLayout.java` | 2 | 1 | `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/edit/music/MyMusicFragment.java` | 2 | 0 | `NvsTimeline`, `NvsAudioTrack` |
| `app/src/main/java/com/meishe/sdkdemo/edit/record/SqLayout.java` | 2 | 1 | `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/edit/record/SqView.java` | 2 | 0 | `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/edit/watermark/SingleClickActivity.java` | 2 | 1 | `NvsAssetPackageManager` |
| `app/src/main/java/com/meishe/sdkdemo/feedback/FeedBackActivity.java` | 2 | 2 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoActivity.java` | 2 | 1 | `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/ClipInfo.java` | 2 | 0 | `NvsVideoStreamInfo` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/CaptionUtil.java` | 2 | 1 | `NvsTimelineCompoundCaption` |
| `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/ImageConverter.java` | 2 | 0 | `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/particle/LiveWindow.java` | 2 | 0 | `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/particle/ParticleSqLayout.java` | 2 | 1 | `NvsMultiThumbnailSequenceView` |
| `app/src/main/java/com/meishe/sdkdemo/presenter/MainPresenter.java` | 2 | 1 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/repository/AppRepository.java` | 2 | 2 | `NvsStreamingContext` |
| `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCaptureLiveWindow.java` | 2 | 0 | `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemePreviewLiveWindow.java` | 2 | 0 | `NvsLiveWindow` |
| `app/src/main/java/com/meishe/sdkdemo/utils/ImageConverter.java` | 2 | 0 | `NvsVideoResolution` |
| `app/src/main/java/com/meishe/sdkdemo/view/AdjustSpecialEffectsView.java` | 2 | 0 | `NvsExpressionParam` |
| `app/src/main/java/com/meishe/sdkdemo/view/MakeUpView.java` | 2 | 2 | `NvsColor` |
| `libBase/src/main/java/com/meishe/base/model/NvsError.java` | 2 | 0 | `NvsError` |
| `libBase/src/main/java/com/meishe/base/view/MSLiveWindowExt.java` | 2 | 0 | `NvsLiveWindowExt` |
| `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioFx.java` | 2 | 0 | `NvsAudioFx`, `NvsObject` |
| `libEngine/src/main/java/com/meishe/engine/interf/EditOperater.java` | 2 | 0 | `NvsTimeline` |
| `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureFxAdapter.java` | 1 | 0 | `NvsAssetPackageParticleDescParser` |
| `libBase/src/main/java/com/meishe/base/model/BaseMvpActivity.java` | 1 | 0 | `NvsError` |
| `libBase/src/main/java/com/meishe/base/model/BaseMvpFragment.java` | 1 | 1 | `NvsError` |
| `libBase/src/main/java/com/meishe/base/model/IBaseView.java` | 1 | 0 | `NvsError` |
| `libEngine/src/main/java/com/meishe/engine/bean/ClipInfo.java` | 1 | 0 | `NvsObject` |
| `libEngine/src/main/java/com/meishe/engine/bean/TrackInfo.java` | 1 | 0 | `NvsObject` |
