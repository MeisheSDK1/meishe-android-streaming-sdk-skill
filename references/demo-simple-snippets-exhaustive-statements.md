# Demo Simple Snippets - Exhaustive SDK Statements

This is the exhaustive compact statement layer extracted from every non-import Java line in the demo that references `Nvs*` or `com.meicam.*`.
Use it when method-level snippets are too curated and you need to confirm whether a specific SDK statement, constant, nested type, or edge-case call exists anywhere in the demo.

Each bullet is a unique sanitized SDK-related statement pattern with representative source labels.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Category Counts](#category-counts)
- [ar-makeup-segmentation](#ar-makeup-segmentation)
- [assets-packages](#assets-packages)
- [audio-media](#audio-media)
- [captions-stickers](#captions-stickers)
- [capture-recording](#capture-recording)
- [core-lifecycle](#core-lifecycle)
- [effects-transforms](#effects-transforms)
- [preview-export](#preview-export)
- [template-mimo-cutsame](#template-mimo-cutsame)
- [timeline-editing](#timeline-editing)
<!-- END GENERATED CONTENTS -->

## Category Counts

| Category | Unique statements | Source lines |
| --- | ---: | ---: |
| `ar-makeup-segmentation` | 216 | 291 |
| `assets-packages` | 39 | 66 |
| `audio-media` | 173 | 256 |
| `captions-stickers` | 619 | 1076 |
| `capture-recording` | 72 | 108 |
| `core-lifecycle` | 157 | 244 |
| `effects-transforms` | 618 | 849 |
| `preview-export` | 247 | 491 |
| `template-mimo-cutsame` | 543 | 634 |
| `timeline-editing` | 328 | 560 |

## ar-makeup-segmentation

- `, NvsStreamingContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK | NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:203`
- `arSceneManipulate.setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3288`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1307`
- `arSceneManipulate.setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2806`
- `beautyHelper = new BeautyHelper(NvsStreamingContext.getInstance()`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2193`
- `boolean advancedBeautySuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY, advancedBeautyPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:136`
- `boolean avatarSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:217`
- `boolean eyeBallSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(), eyeBallModelPath, null`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:202`
- `boolean faceCommonSuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON, faceCommonPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:123`
- `boolean fakefaceSuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE, fakeFacePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:150`
- `boolean handSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(), handPath, null,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:186`
- `boolean initSuccess = NvsStreamingContext.initHumanDetection(MSApplication.getContext(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:102`
- `boolean segSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:170`
- `boolean skySeguccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:231`
- `data, width, height, NvsFaceDetector.AI_SDK_DETECTION_BUFFER_FORMAT_RGBA, mDetectOrientation, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1440`
- `enableCaptureMakeupFlag(NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:111`
- `enableMakeupFlag(videoFx, NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:146`
- `eyeBallModelPath, null, NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:209`
- `for (NvsFaceDetector.NvsFaceData faceData : faceDataList) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1443`
- `if (!TextUtils.isEmpty(fxInfo.getPackageId()) && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:539`
- `if (level == NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyDataManager.java:229`
- `if (mNvsFaceDetector != null) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1235`
- `if (mStreamingContext != null && NvsStreamingContext.hasARModule() == 1) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:99`
- `if (null != mNvsFaceDetector) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1637`
- `if (null != NvsStreamingContext.getInstance()) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyDataManager.java:227`
- `if (NvsStreamingContext.hasARModule() == 1) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:72`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:141`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:128`
- `if (NvsStreamingContext.hasARModule() == HUMAN_AI_TYPE_MS) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java:624`
- `if (videoFx instanceof NvsCaptureVideoFx) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:580`
- `int level = NvsStreamingContext.getInstance().getDeviceCpuLevel();`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyDataManager.java:228`
- `int mCanUseArFaceType = NvsStreamingContext.hasARModule();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:71`
- `List<NvsFaceDetector.NvsFaceData> faceDataList = mNvsFaceDetector.detectBuffer(`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1439`
- `makeupHelper = new MakeupHelper(NvsStreamingContext.getInstance(), BuildConfig.FACE_MODEL == 240, false);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2132`
- `manipulate.setARSceneCallback(new NvsARSceneManipulate.NvsARSceneManipulateCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:108`
- `mBgSegEffect.setColorVal(Constants.KEY_SEGMENT_BACKGROUND_COLOR, new NvsColor(0.0f, 0.0f, 0.0f, 0.0f));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3528`
- `mCanUseARFaceType = NvsStreamingContext.hasARModule();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2943`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:800`
- `mEffectInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:104`
- `mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/CaptureEffectTabFragment.java:127`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java:65`
- `mIsSupportMatte = arSceneManipulate.isFunctionAvailable(NvsARSceneManipulate.CheckedFunctionType_Matte);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1785`
- `mMakeupHelper.setCaptureMakeupColor(makeupType, new NvsColor(0, 0, 0, 0));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2711`
- `mMakeupHelper.setMakeupColor(videoFx, makeupType, new NvsColor(0, 0, 0, 0));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:336`
- `mNvsFaceDetector = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1639`
- `mNvsFaceDetector = NvsFaceDetector.createNvsFaceDetector(destModelPath, NvsFaceDetector.AI_SDK_DETECTION_FRAME_VIDEO_MODE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:311`
- `mNvsFaceDetector.release();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1638`
- `mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java:61`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:68`
- `mVideoFragment.setPlayFlag(NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java:124`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:363`
- `NvsARSceneManipulate arSceneManipulate = mArSceneFaceEffect.getARSceneManipulate();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1783`
- `NvsARSceneManipulate arSceneManipulate = nvsVideoFx.getARSceneManipulate();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2804`
- `NvsARSceneManipulate arSceneManipulate = videoEffect.getARSceneManipulate();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3276`
- `NvsARSceneManipulate arSceneManipulate = videoFx.getARSceneManipulate();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:99`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1305`
- `NvsARSceneManipulate manipulate = mArScene.getARSceneManipulate();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:102`
- `NvsARSceneManipulate.NvsFaceFeatureInfo info = list.get(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:121`
- `NvsAssetPackageManager manager = streamingContext.getAssetPackageManager();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceUPropView.java:114`
- `NvsAssetPackageManager.ARSceneCameraPreset cameraPreset = mAssetPackageManager.getARSceneAssetPackageCameraPreset(packageId);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1616`
- `NvsCaptureVideoFx captureVideoFx = (NvsCaptureVideoFx) videoFx;`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:581`
- `NvsCaptureVideoFx captureVideoFx = mStreamingContext.getCaptureVideoFxByIndex(i);`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:323`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:693`
- `NvsCaptureVideoFx keyerFx = mStreamingContext.appendBuiltinCaptureVideoFx("Master Keyer");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:352`
- `NvsCaptureVideoFx keyerFx = mStreamingContext.getCaptureVideoFxByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:168`
- `NvsCaptureVideoFx videoFx = getCapturePackageFx(key);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:682`
- `NvsCaptureVideoFx videoFx = getCaptureVideoFx(key);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:669`
- `NvsCaptureVideoFx videoFx = mStreamingContext.getCaptureVideoFxByIndex(i);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:107`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:298`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:311`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:181`
- `NvsColor nvsColor = new NvsColor(red, green, blue, alphaF);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java:155`, `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java:487`, `app/src/main/java/com/meishe/sdkdemo/view/MakeUpSingleView.java:270`, `app/src/main/java/com/meishe/sdkdemo/view/MakeUpView.java:151`
- `NvsColor nvsColor = reset ? null : new NvsColor(red, green, blue, alpha);`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:606`
- `NvsEffectSdkContext.initHumanDetection(MSApplication.getContext(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:111`
- `NvsEffectSdkContext.initHumanDetectionExt(MSApplication.getContext(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:177`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:208`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:225`
- `NvsEffectSdkContext.initHumanDetectionExt(MSApplication.getContext(), handPath, null,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:194`
- `NvsEffectSdkContext.setupHumanDetectionData(NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY, advancedBeautyPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:142`
- `NvsEffectSdkContext.setupHumanDetectionData(NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON, faceCommonPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:128`
- `NvsEffectSdkContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE, fakeFacePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:156`
- `NvsFx mArScene = mBeautyHelper.getCaptureBeautyFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:308`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:599`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:651`
- `NvsFx mArScene = mMakeupHelper.getCaptureVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:759`
- `NvsFx nvsFx = mBeautyHelper.getCaptureBeautyFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCaptureFragment.java:222`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:287`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:578`
- `NvsFx nvsFx;`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:729`
- `NvsFxDescription fxDescription = mStreamingContext.getVideoFxDescription(beautyFxName);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1047`
- `NvsStreamingContext streamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceUPropView.java:110`
- `NvsStreamingContext.closeHumanDetection();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java:625`
- `NvsStreamingContext.getInstance().getAssetPackageManager().setCallbackInterface(callback);`
  Sources: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:182`
- `NvsStreamingContext.HUMAN_DETECTION_FEATURE_AVATAR_EXPRESSION);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:220`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:228`
- `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:105`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:114`
- `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:104`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:113`
- `NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:187`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:195`
- `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_SKY);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:234`
- `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:106`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:115`
- `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java:180`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:357`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:118`, `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:56`, `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:91`, `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:152`, `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:208` (+1 more)
- `NvsVideoClip videoClip = videoTrackByIndex.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:181`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:205`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:222`
- `NvsVideoEffect videoEffect = mNvsEffectSdkContext.createVideoEffect(Constants.AR_SCENE, nvsRational);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3270`
- `NvsVideoFx arSceneFx = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1088`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1179`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1225`
- `NvsVideoFx nvsVideoFx = mBeautyHelper.getBeautyFx(videoClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:61`
- `NvsVideoFx nvsVideoFx = mMakeupHelper.checkBuildClipArSceneFx(videoClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:226`
- `NvsVideoFx nvsVideoFx = videoClip.insertRawBuiltinFx(Constants.AR_SCENE, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2795`
- `NvsVideoFx videoFx = beautyHelper.getBeautyFx(videoClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2224`
- `NvsVideoFx videoFx = getVideoFx(videoClip, AR_SCENE);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:128`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:203`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:130`
- `NvsVideoFx videoFx = getVideoFx(videoClip, DEFINITION);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:269`
- `NvsVideoFx videoFx = getVideoFx(videoClip, SHARPEN);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:229`
- `NvsVideoFx videoFx = getVideoPackageFx(videoClip, fxInfo.getPackageId());`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:552`
- `NvsVideoFx videoFx = mBeautyHelper.getBeautyFx(videoClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:231`
- `NvsVideoFx videoFx = nvsVideoClip.getFxByIndex(i);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:327`
- `NvsVideoFx videoFx = nvsVideoClip.getRawFxByIndex(i);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:178`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:165`
- `NvsVideoFx videoFx = videoClip.getFxByIndex(i);`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:332`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:718`
- `NvsVideoFx videoFx = videoClip.insertBuiltinFx(Constants.AR_SCENE, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:95`
- `NvsVideoFx videoFx;`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:140`
- `NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:114`, `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:50`, `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:85`, `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:146`, `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:200`
- `NvsVideoTrack videoTrackByIndex = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:178`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:202`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:219`
- `PackageManagerUtil.installAssetPackage(ADJUST_COLOR_PATH, ADJUST_COLOR_LIC_PATH, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/utils/DataConvertUtils.java:172`
- `private boolean checkIsNull(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:238`
- `private final NvsStreamingContext mStreamingContext;`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:51`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:55`
- `private Makeup applyMakeupFx(File makeupFileDir, NvsVideoClip videoClip, NvsFx arSceneFx) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:405`
- `private NvsCaptureVideoFx getCaptureVideoFx(String buildInName) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:105`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:179`
- `private NvsCaptureVideoFx mARFaceU;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:236`
- `private NvsCaptureVideoFx mArSceneFaceEffect;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:305`
- `private NvsCaptureVideoFx mArSceneFx;`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:60`
- `private NvsCaptureVideoFx mBeautyFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:265`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:54`
- `private NvsCaptureVideoFx mBeautyVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:191`
- `private NvsCaptureVideoFx mDefinitionFx;`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:53`
- `private NvsCaptureVideoFx mLastFx;`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:55`
- `private NvsCaptureVideoFx mSharpenFx;`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:52`
- `private NvsFaceDetector mNvsFaceDetector;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:168`
- `private NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java:47`
- `private NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/BeautyActivity.java:48`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:60`
- `private NvsVideoFx getVideoFx(NvsVideoClip nvsVideoClip, String buildInName) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:176`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:163`
- `private NvsVideoFx getVideoPackageFx(NvsVideoClip nvsVideoClip, String packedId) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:325`
- `private NvsVideoFx setVideoPackageFx(NvsVideoClip nvsVideoClip, String packedId) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:342`
- `private static void applyFxParam(Map<String, FxParams> paramList, NvsCaptureVideoFx videoFx) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:692`
- `private String getFxDesc(NvsFx videoFx) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:579`
- `private void applyBeautyFx(NvsFx arSceneFx, List<? extends BaseParam> paramList, boolean reset, String assetsDirectory) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:624`
- `private void applyFilter(NvsVideoClip videoClip, List<BaseParam> filterParamList, boolean reset) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:686`
- `private void applyMakeupContentFx(List<MakeupParam> makeupParamList, NvsFx arSceneFx, boolean reset, String parentPath) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:591`
- `private void applyMakeupFx(Makeup makeup, NvsVideoClip videoClip, NvsFx arSceneFx) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:544`
- `private void applyMakeupFx(Makeup makeup, NvsVideoClip videoClip, NvsFx arSceneFx, boolean reset) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:557`
- `private void applyParam(NvsFx arSceneFx, List<BaseParam.Param> params, String assetsDirectory, boolean reset) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:645`
- `private void clearAllCustomMakeup(NvsVideoFx videoFx) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:322`
- `private void clearShape(int i, NvsVideoFx nvsVideoFx) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:289`
- `private void makeupColorChanged(String makeupId, NvsColor color) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:197`
- `private void setRegionData(NvsVideoFx arSceneFx) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1117`, `libEngine/src/main/java/com/meishe/engine/local/LMeicamVideoClip.java:456`
- `protected int mDetectOrientation = NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_180;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:130`
- `public BeautyHelper(@NonNull NvsStreamingContext context, boolean is240, boolean singleBuffer) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:60`
- `public boolean isSupportMatte(NvsTimeline mTimeline, BeautyFxInfo mBeautyParams) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:78`
- `public List<IFxInfo> getBuffingSkinData(NvsFx mArScene, Context mContext, List<BeautyParam> beautyParams) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:390`
- `public List<IFxInfo> getWhiteningSkinData(NvsFx mArScene, Context mContext, List<BeautyParam> beautyParams) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:459`
- `public Makeup applyMakeupFx(File makeupFileDir, NvsVideoClip videoClip) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:393`
- `public MakeupHelper(NvsStreamingContext streamingContext, boolean is240, boolean singleBuffer) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:70`
- `public NvsCaptureVideoFx checkBuildCaptureArSceneFx() {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:98`
- `public NvsCaptureVideoFx checkBuildCaptureBeautyFx() {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:70`
- `public NvsCaptureVideoFx checkBuildCaptureDefinitionFx() {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:251`
- `public NvsCaptureVideoFx checkBuildCaptureSharpenFx() {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:214`
- `public NvsCaptureVideoFx getCapturePackageFx(String packageId) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:296`
- `public NvsCaptureVideoFx getCaptureVideoFx() {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:119`
- `public NvsFx getCaptureBeautyFx() {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:119`
- `public NvsVideoFx checkBuildClipArSceneFx(NvsVideoClip videoClip) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:139`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:127`
- `public NvsVideoFx checkBuildClipDefinitionFx(NvsVideoClip videoClip) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:268`
- `public NvsVideoFx checkBuildClipSharpenFx(NvsVideoClip videoClip) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:228`
- `public NvsVideoFx getBeautyFx(NvsVideoClip videoClip) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:127`
- `public static void applyBeautyFx(NvsVideoClip videoClip, ClipInfo clipInfo, BeautyHelper beautyHelper) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2184`
- `public static void applyMakeupFx(NvsVideoClip videoClip, MakeupHelper makeupHelper) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2123`
- `public static void buildTimelineBeauty(NvsTimeline mTimeline, ArrayList<ClipInfo> clipInfoData, BeautyHelper beautyHelper) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2155`
- `public static void buildTimelineMakeup(NvsTimeline mTimeline, MakeupHelper makeupHelper) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2098`
- `public static void setAIFaceOcclusion(NvsFx arSceneFx) {`
  Sources: `libBase/src/main/java/com/meishe/base/utils/Utils.java:660`
- `public void applyBeautyFx(int type, NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:142`
- `public void applyBeautyFx(NvsVideoClip videoClip, IFxInfo fxInfo) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:491`
- `public void applyBeautyFx(NvsVideoClip videoClip, NvsFx arSceneFx, IFxInfo fxInfo) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:503`
- `public void applyDefinitionFx(NvsVideoClip videoClip, IFxInfo fxInfo) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:626`
- `public void applyMakeupFx(Makeup makeup, NvsVideoClip videoClip) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:491`
- `public void applySharpenFx(NvsVideoClip videoClip, IFxInfo fxInfo) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:605`
- `public void deleteBeauty(NvsVideoClip videoClip) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:201`
- `public void enableAdvancedBeauty(NvsFx arSceneFx, boolean enable) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:406`
- `public void enableAdvancedBeauty(NvsVideoClip videoClip, boolean enable) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:396`
- `public void enableBeauty(NvsFx arSceneFx, boolean enable) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:375`
- `public void enableBeauty(NvsVideoClip videoClip, boolean enable) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:365`
- `public void enableMakeupFlag(NvsFx arSceneFx, int flag) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:217`
- `public void enableMakeupFlag(NvsVideoClip videoClip, int flag) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:206`
- `public void enableShape(NvsFx arSceneFx, boolean enable) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:437`
- `public void enableShape(NvsVideoClip videoClip, boolean enable) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:427`
- `public void enableShapeNew(NvsFx arSceneFx, boolean enable) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:468`
- `public void enableShapeNew(NvsVideoClip videoClip, boolean enable) {`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:458`
- `public void notifyFaceBoundingRect(List<NvsARSceneManipulate.NvsFaceBoundingRectInfo> list) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:110`
- `public void notifyFaceFeatureInfos(List<NvsARSceneManipulate.NvsFaceFeatureInfo> list) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:116`
- `public void notifyHandFeatureInfos(List<NvsARSceneManipulate.NvsHandFeatureInfo> list) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:160`
- `public void onMakeupColorChanged(String makeupId, NvsColor color) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1671`, `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:143`
- `public void openBeautyFx(NvsVideoFx videoFx) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1301`
- `public void resetBeauty(NvsVideoFx nvsVideoFx) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1286`
- `public void resetBeautyShape(NvsVideoFx nvsVideoFx) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1271`
- `public void resetCustomMakeup(NvsVideoFx videoFx, String makeupType) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:334`
- `public void resetMakeupFilter(Makeup makeup, NvsVideoClip videoClip) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:523`
- `public void resetMakeupFx(Makeup makeup, NvsVideoClip videoClip) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:512`
- `public void setArSceneEffect(NvsFx mArScene) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:98`
- `public void setCancelDefaultFxValue(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, BeautyFxInfo mBeautyParams) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:196`
- `public void setCaptureMakeupColor(String makeupTypeId, NvsColor nvsColor) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:230`
- `public void setFaceApply(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:117`
- `public void setMakeupColor(NvsFx arSceneFx, String makeupTypeId, NvsColor nvsColor) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:254`
- `public void setMakeupColor(NvsVideoClip videoClip, String makeupTypeId, NvsColor nvsColor) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:242`
- `public void setMakeupFilterIntensity(NvsVideoClip videoClip, String videoFxName, float intensity) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:316`
- `public void setMakeupIntensity(NvsFx arSceneFx, String makeupTypeId, float intensity) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:302`
- `public void setMakeupIntensity(NvsVideoClip videoClip, String makeupTypeId, float intensity) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:290`
- `public void setMakeupPackageId(NvsFx arSceneFx, String makeupTypeId, String packageId) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:370`
- `public void setMakeupPackageId(NvsVideoClip videoClip, String makeupTypeId, String packageId) {`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:358`
- `public void setSharpenApply(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, boolean isSharpenOpen) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:49`
- `public void setSkinApply(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:37`
- `public void setSmallApply(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:129`
- `return arSceneManipulate.isFunctionAvailable(NvsARSceneManipulate.CheckedFunctionType_Matte);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:104`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:272`, `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:278`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:265`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:662`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:660`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:296`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:283`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:656`, `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java:314`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:829`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:294`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:281`, `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java:318`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:833`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:654`, `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java:312`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:827`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:298`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:285`, `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:658`, `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java:316`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:831`
- `return NvsEffectSdkContext.init(mContext, licensePath, NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:130`
- `return NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_0;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:473`
- `return NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_180;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:477`
- `return NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_270;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:479`
- `return NvsFaceDetector.AI_SDK_DETECTION_FRAME_ROTATION_90;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:475`
- `segPath, null, NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:171`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:178`
- `setMakeupColor(arSceneFx, param.getType(), new NvsColor(0, 0, 0, 0));`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:609`
- `String packageId = installFxPackage(fileItem.getAbsolutePath(), "", NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP);`
  Sources: `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java:170`
- `videoFx.getARSceneManipulate().setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);`
  Sources: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:153`, `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:144`
- `void onMakeupColorChanged(String makeupId, NvsColor color);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java:583`, `app/src/main/java/com/meishe/sdkdemo/view/MakeUpSingleView.java:791`, `app/src/main/java/com/meishe/sdkdemo/view/MakeUpView.java:547`
- `| NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:131`
- `| NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:188`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:196`

## assets-packages

- `filterItem.setParticleType(NvsAssetPackageParticleDescParser.PARTICLE_TYPE_NORMAL);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:1045`
- `if (code != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_WORKING_INPROGRESS) {`
  Sources: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:128`
- `if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {`
  Sources: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:116`
- `if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR || code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {`
  Sources: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:115`
- `if (error == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:107`, `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:132`
- `if (error == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR || error == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:1681`, `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:1696`
- `if (error == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:457`
- `if (packageStatus == NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:332`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:343`
- `if (particleType == NvsAssetPackageParticleDescParser.PARTICLE_TYPE_TOUCH) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:688`
- `int type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:815`
- `List<NvsExpressionParam> expValueList = mStreamingContext.getAssetPackageManager().getExpValueList(packageId,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1316`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:491`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:263`
- `mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java:68`
- `NvsAssetPackageManager assetPackageManager = mStreamingContext.getAssetPackageManager();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:329`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:340`
- `NvsAssetPackageManager manager = mStreamingContext.getAssetPackageManager();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1634`
- `NvsAssetPackageManager manager = NvsStreamingContext.getInstance().getAssetPackageManager();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:1192`, `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:223`
- `NvsAssetPackageManager manager = streamingContext.getAssetPackageManager();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:944`
- `NvsAssetPackageManager packageManager = NvsStreamingContext.getInstance().getAssetPackageManager();`
  Sources: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:106`
- `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1317`, `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1319`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:331`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:492`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:494` (+2 more)
- `NvsAssetPackageParticleDescParser desc = new NvsAssetPackageParticleDescParser(assetItem.getAsset().assetDescription);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1021`
- `NvsAssetPackageParticleDescParser parser = new NvsAssetPackageParticleDescParser(assetDescription);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:518`
- `NvsAssetPackageParticleDescParser particleDescParser = new NvsAssetPackageParticleDescParser(asset.assetDescription);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:684`
- `PackageManagerUtil.installAssetPackage(filterInfo.getId(), null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java:307`
- `PackageManagerUtil.installAssetPackage(scenePackageFilePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneEffectView.java:289`
- `private NvsAssetPackageManager mAssetPackageManager;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:376`
- `private NvsAssetPackageManager packageManager;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:134`
- `public class CaptureSceneActivity extends BasePermissionActivity implements NvsAssetPackageManager.AssetPackageManagerCallback,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:60`
- `public class NvAssetManager implements NvHttpRequest.NvHttpRequestListener, NvsAssetPackageManager.AssetPackageManagerCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:41`
- `public static void installAssetPackageAsynchronous(String packagePath, String licPath, int packageType, StringBuilder stringBuilder, NvsAssetPackageManager.AssetPackageManagerCallback callback) {`
  Sources: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:181`
- `public void installAssetPackagedNoSynchronous(String path, int type, StringBuilder stringBuilder, NvsAssetPackageManager.AssetPackageManagerCallback callback) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:636`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:268`, `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:274`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:257`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:261`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:252`, `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:300`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:241`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:287`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:254`, `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:270`, `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:292`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:243`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:259` (+1 more)
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:266`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:255`
- `return PackageManagerUtil.installAssetPackage(filterPackageFilePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:921`
- `return PackageManagerUtil.installAssetPackage(videoFxPackagePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:880`
- `String packageId = PackageManagerUtil.installAssetPackage(effectPackageFilePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:371`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java:283`
- `type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:817`
- `type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:823`
- `|| error == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:108`, `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:133`

## audio-media

- `audioFx.removeAllKeyframe(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:671`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:672`
- `audioFx.setFloatValAtTime(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN, value.getVolumeValue(), keyTime);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:680`
- `audioFx.setFloatValAtTime(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_RIGHT_GAIN, value.getVolumeValue(), keyTime);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:681`
- `audioFx.setKeyFrameControlPoint(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN, keyTime, prePoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:686`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:687`
- `audioFx.setKeyFrameControlPoint(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_RIGHT_GAIN, keyTime, nextPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:693`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:694`
- `Bitmap frameBitmap = videoFrameRetriever.getFrameAtTime(timeStamp, NvsVideoFrameRetriever.VIDEO_FRAME_HEIGHT_GRADE_480);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:201`
- `class FilePassThroughConvertorCallback implements NvsPassthroughConvertor.PassthroughConvertorCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:117`
- `errorCode == NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:75`, `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java:59`
- `final ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:500`
- `for (int i = 0; i < mNvsAudioTrack.getClipCount(); i++) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:226`
- `hashtable.put(NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT, 1080);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java:105`
- `if (avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_AUDIOVIDEO) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/WhiteList.java:60`
- `if (flag != NvsAVFileInfo.AV_FILE_INFO_FLAGS_HAS_VIDEO_PART_IN_IMAGE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java:413`
- `if (m_videoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:483`
- `if (mNvsAudioTrack == null) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:220`
- `if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:337`
- `if (videoType == NvsAVFileInfo.AV_FILE_TYPE_IMAGE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:752`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:1065`
- `List<NvsAudioClip> remove_list = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:879`
- `List<NvsPassthroughConvertor.NvsPassthroughFileInfo> passthroughFileInfos = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:102`
- `LogUtils.e("NvsAudioTrack is null");`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:221`
- `m_streamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:83`
- `mMediaFileConvertor = new NvsMediaFileConvertor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:258`, `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java:91`
- `mNvsAudioClip = nvsAudioClip;`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:229`
- `mNvsAudioTrack = mTimeline.getAudioTrackByIndex(baseUIClip.getIndex());`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:219`
- `mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:82`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:128`
- `mStreamingContext.playbackTimeline(mTimeline, 0, -1, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:252`
- `NvsAudioClip audioClip = audioTrack.addClip(oneMusic.getFilePath(), oneMusic.getInPoint(), oneMusic.getTrimIn(), oneMusic.getTrimOut());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1238`
- `NvsAudioClip audioClip = audioTrack.addClip(recordAudioInfo.getPath(), recordAudioInfo.getInPoint(), recordAudioInfo.getTrimIn(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1296`
- `NvsAudioClip audioClip = findAudioClipByCurPosition(cur_audio_inpoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:663`
- `NvsAudioClip audioClip = findAudioClipByInPoint(m_curInPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:295`
- `NvsAudioClip audioClip = m_musicTrack.addClip(oneMusic.getFilePath(), oneMusic.getInPoint(), oneMusic.getTrimIn(), oneMusic.getTrimOut());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:930`
- `NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:550`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:572`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:596`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:624`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:737` (+2 more)
- `NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:272`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:403`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:881`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:965`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:995` (+1 more)
- `NvsAudioClip audioClip = mMusicTrack.appendClip(musicInfo.getFilePath(), trimIn, trimOut);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1998`
- `NvsAudioClip del_audio_clip = findAudioClipByInPoint(del_point);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:802`
- `NvsAudioClip extra_clip = audioTrack.addClip(oneMusic.getFilePath(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1248`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1261`
- `NvsAudioClip extra_clip = m_musicTrack.addClip(oneMusic.getFilePath(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:933`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:947`
- `NvsAudioClip extraAudioClip = m_musicTrack.getClipByIndex(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:1012`
- `NvsAudioClip musicClip = findAudioClipByInPoint(m_curInPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:831`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:871`
- `NvsAudioClip newAudioClip = newAudioTrack.addClip(oldAudioClip.getFilePath(),oldAudioClip.getInPoint(),oldAudioClip.getTrimIn(),oldAudioClip.getTrimOut());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:68`
- `NvsAudioClip nvsAudioClip = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:111`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:124`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:141`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:154`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:191`
- `NvsAudioClip nvsAudioClip = mNvsAudioTrack.getClipByIndex(i);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:227`
- `NvsAudioClip nvsAudioClip = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:723`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1067`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:243`
- `NvsAudioClip nvsAudioClip = nvsAudioTrack.addClip(mThemeModel.getFolderPath() + File.separator + music, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:62`
- `NvsAudioClip oldAudioClip = oldAudioTrack.getClipByIndex(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:67`
- `NvsAudioFx audioFx = audioClip.getFxByIndex(0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:227`
- `NvsAudioFx audioFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:292`, `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:326`
- `NvsAudioFx audioFx = videoClip.getAudioVolumeFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:666`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:711`
- `NvsAudioFx fx = audioClip.getFxByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:408`
- `NvsAudioFx fxByIndex = nvsAudioClip.getFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1121`
- `NvsAudioFx fxByIndex = nvsVideoClip.getAudioFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:390`
- `NvsAudioFx fxByIndex = videoClip.getAudioFxByIndex(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:295`, `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:329`
- `NvsAudioFx newFx = newAudioClip.insertFx(oldFx.getBuiltinAudioFxName(),k);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:83`
- `NvsAudioFx noiseAudioEffect = videoClip.appendAudioFx(Constants.NOISE_SUPPRESSION_KEY);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:595`
- `NvsAudioFx nvsAudioFx = audioClip.appendFx(Constants.NOISE_SUPPRESSION_KEY);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1306`
- `NvsAudioFx oldFx = oldAudioClip.getFxByIndex(k);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:81`
- `NvsAudioResolution audioEditRes = new NvsAudioResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:953`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1104`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:493`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:351`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:331` (+4 more)
- `NvsAudioResolution audioEditRes = oldTimeline.getAudioRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:44`
- `NvsAudioResolution nvsAudioResolution = new NvsAudioResolution();`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:536`
- `NvsAudioTrack audioTrack = meicamAudioTrack.bindToTimeline(timeline);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:353`
- `NvsAudioTrack audioTrack = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:457`
- `NvsAudioTrack audioTrack = timeline.appendAudioTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:968`
- `NvsAudioTrack audioTrack = timeline.getAudioTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1217`
- `NvsAudioTrack audioTrack = timeline.getAudioTrackByIndex(1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1287`
- `NvsAudioTrack audioTrackByIndex = timeline.getAudioTrackByIndex(index);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:333`
- `NvsAudioTrack musicTrack = m_timeLine.getAudioTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:555`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:586`
- `NvsAudioTrack newAudioTrack = newTimeline.appendAudioTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:58`
- `NvsAudioTrack nvsAudioTrack = meicamAudioTrack.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:754`
- `NvsAudioTrack nvsAudioTrack = mTimeline.appendAudioTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:57`
- `NvsAudioTrack nvsVideoTrack = videoTrack.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:513`
- `NvsAudioTrack oldAudioTrack = oldTimeline.getAudioTrackByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:57`
- `NvsAudioTrack track = timeline.appendAudioTrack();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioTrack.java:37`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(clipInfo.getFilePath());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/EditActivity.java:531`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(clipPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:780`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(filePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:387`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:458`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(imagePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:262`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(meicamVideoClip.getFilePath());`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2358`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(path);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:425`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(pathList.get(0).getFilePath());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2214`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:302`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:538`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:758`
- `NvsAVFileInfo avFileInfo = NvsStreamingContext.getAVInfoFromFile(filePath, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java:395`, `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java:408`, `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java:343`, `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java:390`
- `NvsAVFileInfo avFileInfo = NvsStreamingContext.getAVInfoFromFile(path, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java:486`
- `NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:795`
- `NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(clipPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/StoryboardUtil.java:64`
- `NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(filePath);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1122`, `libEngine/src/main/java/com/meishe/engine/local/LMeicamVideoClip.java:461`
- `NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(path);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2266`, `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java:98`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:852`, `libEngine/src/main/java/com/meishe/engine/util/WhiteList.java:56`
- `NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(path, NvsStreamingContext.AV_FILEINFO_EXTRA_INFO);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/selectmedia/adapter/AgendaSimpleSectionAdapter.java:246`
- `NvsAVFileInfo avInfoFromFile = NvsStreamingContext.getAVInfoFromFile(filePath, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:375`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1168`
- `NvsAVFileInfo avInfoFromFile = NvsStreamingContext.getAVInfoFromFile(videoClip.getFilePath(), 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2551`
- `NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(mRecordVideoPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:170`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:157`
- `NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(pathList.get(i));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:880`
- `NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(videoClip.getFilePath());`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:775`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:918`
- `NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(videoPath);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:434`
- `NvsAVFileInfo fileInfo = nvsStreamingContext.getAVFileInfo(videoUrl);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:311`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:351`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:391`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:434`
- `NvsAVFileInfo fileInfo = streamingContext.getAVFileInfo(clipPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:176`
- `NvsAVFileInfo fileInfo = streamingContext.getAVFileInfo(filePath);`
  Sources: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:1079`
- `NvsAVFileInfo info = mStreamingContext.getAVFileInfo(mCurRecordVideoPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1585`
- `NvsAVFileInfo info = mStreamingContext.getAVFileInfo(path);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1337`
- `NvsAVFileInfo info = NvsStreamingContext.getInstance().getAVFileInfo(newPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:284`
- `NvsAVFileInfo mFileInfo = mStreamingContext.getAVFileInfo(pathList.get(0));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:872`
- `NvsAVFileInfo newAvFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(newPath, NvsStreamingContext.AV_FILEINFO_EXTRA_INFO);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/selectmedia/adapter/AgendaSimpleSectionAdapter.java:247`
- `NvsAVFileInfo.ExtendsDataInfo extendsDataInfo = avFileInfo.getExtendsDataInfo();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java:416`
- `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:508`
- `NvsPassthroughConvertor nvsPassthroughConvertor = new NvsPassthroughConvertor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:101`
- `NvsPassthroughConvertor.NvsPassthroughFileInfo fileInfo = new NvsPassthroughConvertor.NvsPassthroughFileInfo();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:103`
- `NvsSize dimension = avFileInfo.getVideoStreamDimension(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:389`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:460`, `app/src/main/java/com/meishe/sdkdemo/utils/StoryboardUtil.java:68`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2267`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1123` (+2 more)
- `NvsSize nvsSize = avFileInfo.getVideoStreamDimension(0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/WhiteList.java:61`
- `NvsSize size = avFileInfo.getVideoStreamDimension(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2223`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:307`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:548`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:763`
- `NvsSize videoSize = avFileInfo.getVideoStreamDimension(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:265`
- `NvsTimeline newTimeline = streamingContext.createTimeline(videoEditRes,videoFps,audioEditRes);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:46`
- `NvsTimeline nvsTimeline = mStreamingContext.createTimeline(videoEditRes, videoFps, audioEditRes);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:497`
- `NvsTimeline timeline = context.createTimeline(nvsVideoResolution, TimelineData.getInstance().getNvsRational(), nvsAudioResolution);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:540`
- `NvsTimeline timeline = mStreamingContext.createTimeline(videoEditRes, videoFps, audioEditRes);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:956`
- `NvsVideoClip clip = mVideoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:178`
- `NvsVideoClip clip = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:505`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:290`, `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:324`
- `NvsVideoFrameRetriever videoFrameRetriever = mStreamingContext.createVideoFrameRetriever(`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2285`
- `NvsVideoFrameRetriever videoFrameRetriever = streamingContext.createVideoFrameRetriever(clipPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:192`
- `NvsVideoFrameRetriever.VIDEO_FRAME_HEIGHT_GRADE_720);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2289`
- `NvsVideoTrack mVideoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:173`
- `NvsVideoTrack videoTrack = m_timeLine.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:501`
- `NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:286`, `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:320`
- `NvsVolume volumeGain = audioClip.getVolumeGain();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:233`
- `private int getAudioFxPositionInClip(NvsAudioClip nvsAudioClip, String fxName) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1112`
- `private int getAudioFxPositionInClip(NvsVideoClip nvsVideoClip, String fxName){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:381`
- `private NvsAudioClip findAudioClipByCurPosition(long curPos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:569`
- `private NvsAudioClip findAudioClipByInPoint(long inPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:547`
- `private NvsAudioClip mNvsAudioClip;`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:145`
- `private NvsAudioFx noiseAudioEffect;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:68`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:116`
- `private NvsAudioTrack m_musicTrack;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:75`
- `private NvsAudioTrack m_recordAudioTrack;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:110`
- `private NvsAudioTrack mMusicTrack;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:187`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:138`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:79`
- `private NvsAudioTrack mNvsAudioTrack = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:143`
- `private NvsAudioTrack mRecordAudioTrack;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:139`
- `private NvsCaptureAudioFx mNoiseAudioFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:257`
- `private NvsMediaFileConvertor mMediaFileConvertor;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:48`, `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java:20`
- `private NvsStreamingContext m_streamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:73`
- `private NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:63`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:76`
- `private NvsTimeline m_timeLine;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:74`
- `private NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:64`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:77`
- `private NvsVideoTrack mVideoTrack;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:78`
- `public class ConvertFileManager implements NvsMediaFileConvertor.MeidaFileConvertorCallback {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java:18`
- `public class ConvertFiles implements NvsMediaFileConvertor.MeidaFileConvertorCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:30`
- `public class LMeicamAudioFx extends LNvsObject implements Cloneable, LocalToTimelineDataAdapter<MeicamAudioFx> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LMeicamAudioFx.java:13`
- `public class MeicamAudioClip extends ClipInfo<NvsAudioClip> implements Cloneable, Serializable, IResourceParser {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:27`
- `public class MeicamAudioFx extends NvsObject<NvsAudioFx> implements Cloneable, TimelineDataToLocalAdapter<LMeicamAudioFx> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioFx.java:14`
- `public class MeicamAudioTrack extends TrackInfo<NvsAudioTrack> implements Cloneable, Serializable{`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioTrack.java:15`
- `public int getRotation(NvsAVFileInfo fileInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1662`
- `public NvsAudioClip bindToTimeline(NvsAudioTrack audioTrack) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:239`
- `public NvsAudioTrack bindToTimeline(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioTrack.java:33`
- `public NvsAVFileInfo getFileInfo(String path) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1332`
- `public static boolean buildTimelineMusic(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:329`
- `public static boolean buildTimelineMusic(NvsTimeline timeline, List<MusicInfo> musicInfos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1213`
- `public static void addAudioClipInfoByTrackIndex(NvsAudioTrack nvsAudioTrack, MeicamAudioClip meicamAudioClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:683`
- `public static void addMusic(NvsTimeline mTimeline, ThemeModel mThemeModel) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:53`
- `public static void buildTimelineRecordAudio(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:451`
- `public static void buildTimelineRecordAudio(NvsTimeline timeline, ArrayList<RecordAudioInfo> recordAudioInfos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1283`
- `public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:474`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:452`
- `public void compileFailed(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:469`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:447`
- `public void compileFinished(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:464`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:442`
- `public void compileProgress(NvsTimeline timeline, int progress) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:460`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:438`
- `public void getAudioCount(NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1061`
- `public void initData(long total_duration, ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicSqLayout.java:133`
- `public void loadData(NvsAudioClip audioClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:209`
- `public void playBackEOF(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:388`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:311`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:330`
- `public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:398`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:327`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:343`
- `public void playStopped(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:393`, `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:323`, `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:338`
- `public void resetVideoRatioFromRotation(NvsAVFileInfo fileInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:943`
- `public void setOtherAttribute(NvsAudioClip nvsAudioClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:254`
- `return audioFx.getFloatValAtTime(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN, timeStamp);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:715`
- `return avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_IMAGE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/EditActivity.java:533`
- `table.put(NvsMediaFileConvertor.CONVERTOR_ENABLE_HDR, true);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:265`
- `void audioEditCopyClip(long inPoint, NvsAudioTrack nvsAudioTrack);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2900`
- `void audioEditCutClip(NvsAudioTrack nvsAudioTrack, long inPoint);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2885`

## captions-stickers

- `!= NvsClipCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作处理 Subject subtitles are not processed`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:919`
- `&& caption.getRoleInTheme() != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:600`
- `&& caption.getRoleInTheme() != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作处理`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1509`
- `&& caption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:578`
- `&& mCurCaption.getRoleInTheme() != NvsClipCaption.ROLE_IN_THEME_GENERAL) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2187`
- `&& mCurCaption.getRoleInTheme() != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2267`
- `&& roleTheme != NvsClipCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作编辑处理 Subject captions are not edited`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2128`
- `&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1411`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2743`
- `&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作编辑处理`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2209`
- `&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不做删除 Subject subtitles will not be deleted`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:426`
- `((NvsBodyOpacitySpan) nvsCaptionSpan).setOpacity((Float) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5070`
- `((NvsColorSpan) nvsCaptionSpan).setB(((NvsColor) object).b);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5045`
- `((NvsColorSpan) nvsCaptionSpan).setG(((NvsColor) object).g);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5046`
- `((NvsColorSpan) nvsCaptionSpan).setR(((NvsColor) object).r);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5044`
- `((NvsFontFamilySpan) nvsCaptionSpan).setFontFamily((String) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5048`
- `((NvsFontSizeRatioSpan) nvsCaptionSpan).setFontSizeRatio((Float) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5068`
- `((NvsItalicSpan) nvsCaptionSpan).setItalic((Boolean) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5052`
- `((NvsNormalTextSpan) nvsCaptionSpan).setOutlineWidth((Float) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5066`
- `((NvsOpacitySpan) nvsCaptionSpan).setOpacity((Float) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5050`
- `((NvsOutlineColorSpan) nvsCaptionSpan).setOutlineColor((NvsColor) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5061`
- `((NvsOutlineColorSpan) nvsCaptionSpan).setOutlineColor(null);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5059`
- `((NvsOutlineOpacitySpan) nvsCaptionSpan).setOpacity((Float) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5072`
- `((NvsOutlineWidthSpan) nvsCaptionSpan).setOutlineWidth((Float) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5064`
- `((NvsRendererIdSpan) nvsCaptionSpan).setRendererId((String) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5056`
- `((NvsShadowOpacitySpan) nvsCaptionSpan).setOpacity((Float) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5074`
- `((NvsTimelineCaption) object).changeInPoint(inPoint);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:516`
- `((NvsTimelineCaption) object).changeOutPoint(outPoint);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:532`
- `((NvsUnderlineSpan) nvsCaptionSpan).setUnderline((Boolean) object);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5054`
- `addNvsCaption(areaAllAICaption);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:441`
- `addNvsCaption(fromAICaptionFromVideoClip);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:439`
- `addNvsCaption(toAICaptionFromVideoClip);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:440`
- `ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:2045`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1772`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:2038`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1699`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1648`
- `captionByIndex.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1430`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1442`
- `case NvsTimelineCaption.TEXT_ALIGNMENT_CENTER:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:845`
- `case NvsTimelineCaption.TEXT_ALIGNMENT_LEFT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:841`
- `case NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:849`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_COLOR,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3035`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_COLOR, captionInfo);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2343`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_FONT_FAMILY,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3601`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3611`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3617`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_ITALIC,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3668`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_NORMAL_TEXT,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3264`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3335`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_NORMAL_TEXT, captionInfo);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2340`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_OPACITY,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3071`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_OUTLINE_COLOR,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3333`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_OUTLINE_COLOR, captionInfo);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2342`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_OUTLINE_WIDTH,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3262`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3337`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_OUTLINE_WIDTH, captionInfo);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2341`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_RENDER_ID,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2354`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2879`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_RENDER_ID, captionInfo);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2333`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3800`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4400`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4494`
- `changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_UNDERLINE,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3741`
- `clip.setImageMotionMode(NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:396`
- `color = ColorUtil.colorStringtoNvsColor(mCaptionBackgroundList.get(pos).mColorValue);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:903`
- `ColorUtil.colorStringtoNvsColor(mCaptionBackgroundList.get(pos).mColorValue);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3431`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2439`
- `ColorUtil.colorStringtoNvsColor(mCaptionOutlineColorList.get(pos).mColorValue);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3174`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2283`
- `ColorUtil.colorStringtoNvsColor(mCaptionShadowList.get(pos).mColorValue);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4504`
- `currentCompoundCaption.setTextColor(selectCaptionIndex, ColorUtil.colorStringtoNvsColor(textColor));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1137`
- `false, currentCompoundCaption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:561`, `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:595`, `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1173`
- `final NvsTimelineTimeSpan timelineTimeSpan = mTimelineEditor.addTimeSpan(inPoint, outPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1754`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1754`
- `float b = ((NvsColorSpan) nvsCaptionSpan).getB();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5127`
- `float g = ((NvsColorSpan) nvsCaptionSpan).getG();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5126`
- `float r = ((NvsColorSpan) nvsCaptionSpan).getR();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5125`
- `for (NvsClipAnimatedSticker NvsClipAnimatedSticker : animateStickerList) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:646`
- `for (NvsTimelineAnimatedSticker nvsTimelineAnimatedSticker : animateStickerList) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:645`
- `if (capCategory == NvsClipCaption.THEME_CATEGORY`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2127`
- `if (capCategory == NvsTimelineCaption.THEME_CATEGORY`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2208`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1410`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2742`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:425`
- `if (caption instanceof NvsTimelineCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:486`
- `if (caption.getCategory() == NvsClipCaption.THEME_CATEGORY`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:917`
- `if (caption.getCategory() == NvsTimelineCaption.THEME_CATEGORY`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1508`, `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:577`, `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:599`
- `if (curAnimateSticker != null && curAnimateSticker instanceof NvsClipAnimatedSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:245`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:547`
- `if (curAnimateSticker != null && curAnimateSticker instanceof NvsTimelineAnimatedSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:243`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:546`
- `if (curCaption != null && curCaption instanceof NvsClipCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:529`
- `if (curCaption != null && curCaption instanceof NvsTimelineCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:522`
- `if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") != 0)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:295`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:277`
- `if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") == 0) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:173`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:156`
- `if (mCurAnimateSticker instanceof NvsClipAnimatedSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1996`
- `if (mCurCaption instanceof NvsTimelineCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1978`
- `if (mCurCaption.getCategory() == NvsClipCaption.THEME_CATEGORY`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2186`
- `if (mCurCaption.getCategory() == NvsTimelineCaption.THEME_CATEGORY`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2266`
- `if (mNvsTimelineCompoundCaption != null) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:171`
- `if (mNvsTimelineCompoundCaption == null) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:158`
- `if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:364`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:394`
- `if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1274`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1259`
- `if (mThemeCaption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:174`
- `if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1111`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1454`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1498`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1675`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1093` (+5 more)
- `if (newCaption instanceof NvsTimelineCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1574`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1770`
- `if (nvsCaptionSpan instanceof NvsColorSpan && object instanceof NvsColor) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5043`
- `if (nvsCaptionSpan instanceof NvsColorSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5124`
- `if (NvsCaptionSpan.SPAN_TYPE_OUTLINE_WIDTH.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5160`
- `if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:442`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:470`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1172`
- `if (object instanceof NvsTimelineCaption) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:460`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:515`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:531`
- `if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:451`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:414`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:452`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:432`
- `if (TimelineData.getInstance().isAddTitleTheme() && caption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1279`
- `inPoint = ((NvsClipAnimatedSticker) mCurAnimateSticker).getInPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1997`
- `inPoint = ((NvsClipCaption) caption).getInPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:490`
- `inPoint = ((NvsClipCaption) mCurCaption).getInPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1982`
- `inPoint = ((NvsClipCaption) newCaption).getInPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1578`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1774`
- `inPoint = ((NvsTimelineAnimatedSticker) mCurAnimateSticker).getInPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2000`
- `inPoint = ((NvsTimelineCaption) caption).getInPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:487`
- `inPoint = ((NvsTimelineCaption) mCurCaption).getInPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1979`
- `inPoint = ((NvsTimelineCaption) newCaption).getInPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1575`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1771`
- `int zVal = (int) NvsClipAnimatedSticker.getZValue();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:647`
- `item.name = NvsStreamingContext.getInstance().registerFontByFilePath(item.localDirPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/presenter/CaptionPresenter.java:116`
- `List<NvsCaptionSpan> spanList, CaptionInfo captionInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5033`
- `List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:789`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2345`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3030`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3063`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3185` (+8 more)
- `List<NvsClipAnimatedSticker> animatedStickers = curVideoClip.getAnimatedStickersByClipTimePosition(curPos);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:491`
- `List<NvsClipAnimatedSticker> animateStickerList = curVideoClip.getAnimatedStickersByClipTimePosition(curPos);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:645`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1186`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1927`
- `List<NvsClipAnimatedSticker> stickerList = videoClip.getAnimatedStickersByClipTimePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1851`
- `List<NvsClipCaption> captionList = curVideoClip.getCaptionsByClipTimePosition(curPos);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1575`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2154`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:3377`
- `List<NvsTimelineAnimatedSticker> animatedStickers = mTimeline.getAnimatedStickersByTimelinePosition(curPos);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:473`
- `List<NvsTimelineAnimatedSticker> animateStickerList = mTimeline.getAnimatedStickersByTimelinePosition(curPos);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:644`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1204`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1934`
- `List<NvsTimelineAnimatedSticker> stickerList = mTimeline.getAnimatedStickersByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1830`
- `List<NvsTimelineCaption> captionList = mTimeline.getCaptionsByTimelinePosition(curPos);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1648`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2233`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4827`, `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:592`
- `List<NvsTimelineCaption> captionList = mTimeline.getCaptionsByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1741`
- `List<NvsTimelineCompoundCaption> captionList = mTimeline.getCompoundCaptionsByTimelinePosition(curPos);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1542`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1884`
- `List<NvsTimelineCompoundCaption> captionList = mTimeline.getCompoundCaptionsByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1443`
- `List<PointF> captionBoundingVertices = currentCompoundCaption.getCaptionBoundingVertices(i, NvsCaption.BOUNDING_TYPE_TEXT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:935`
- `List<PointF> list = caption.getCaptionBoundingVertices(NvsCaption.BOUNDING_TYPE_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1381`
- `List<PointF> list = caption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1409`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1449`
- `List<PointF> pointFS = compoundCaption.getCaptionBoundingVertices(i, NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1188`
- `List<PointF> subList = caption.getCaptionBoundingVertices(index, NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1418`
- `List<PointF> vertices = currentCompoundCaption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1887`
- `Log.e("caption", "NvsTimelineCompoundCaption");`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1010`
- `Log.e(TAG, "getCaptionByAttachment: mNvsTimeline is null!");`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1235`
- `LogUtils.e("addCompoundCaptionFirst", "NvsTimelineCompoundCaption is null! inpoint: "+ getInPoint()`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:174`
- `LogUtils.e("NvsTimelineCompoundCaption bindToTimeline mNvsTimelineCompoundCaption==null");`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:159`
- `LogUtils.e("NvsTimelineCompoundCaption bindToTimeline timeline==null");`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:153`
- `mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:381`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:422`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:505`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:593`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:285` (+4 more)
- `mClipFragment.seekTimeline(timelinePosition, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:601`
- `mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2796`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2830`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2864`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2898`
- `mCurCaption = (NvsClipCaption) curCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:530`
- `mCurCaption = (NvsTimelineCaption) curCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:523`
- `mCurCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3911`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3947`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3984`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4022`
- `mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_CENTER);  //居中对齐 Center alignment`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:842`
- `mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_LEFT);  //居左或者居下对齐 Align left or bottom`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:850`
- `mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT);  //居右或者居上对齐 Align to the right or top`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:846`
- `mCurSelectAnimatedSticker = (NvsClipAnimatedSticker) curAnimateSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:246`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:548`
- `mCurSelectAnimatedSticker = (NvsTimelineAnimatedSticker) curAnimateSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:244`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:547`
- `mDouVideoTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:164`
- `mDouVideoTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimOutChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:174`
- `mEffectInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:96`
- `mEffectInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:100`
- `mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/CaptureEffectTabFragment.java:121`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java:59`
- `mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/CaptureEffectTabFragment.java:124`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java:62`
- `mNvsTimelineCompoundCaption.setClipAffinityEnabled(false);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:162`
- `mNvsTimelineCompoundCaption.setZValue(zValue);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:172`
- `moveAndRemoveNvsCaption(areaAllAICaption, areaOffset);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:421`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:436`
- `moveAndRemoveNvsCaption(fromAICaptionFromVideoClip, fromOffset);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:419`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:434`
- `moveAndRemoveNvsCaption(toAICaptionFromVideoClip, toOffset);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:420`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:435`
- `mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/dialog/CaptionEditPop.java:130`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:192`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerActivity.java:124`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:111`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:319` (+7 more)
- `mStreamingContext.seekTimeline(timeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:995`
- `mTimeline.removeCaption((NvsTimelineCaption) clipInfo.getObject());`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1492`
- `mTimeline.removeCaption((NvsTimelineCaption) object);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:461`
- `mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.caption_timeline_editor);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:232`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:241`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:245`
- `mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.timelineEditor);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:204`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:207`
- `mTimelineEditor.setOnScrollListener(new NvsTimelineEditor.OnScrollChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:328`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:386`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:328`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:414`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1114`
- `mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:323`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1753`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1879`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1753`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1808` (+3 more)
- `mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpanExt");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:247`, `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:260`
- `mTimlineTimeSpanExt.setOnChangeListener(new NvsTimelineTimeSpanExt.OnTrimInChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:127`, `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:148`
- `mTimlineTimeSpanExt.setOnChangeListener(new NvsTimelineTimeSpanExt.OnTrimOutChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:145`, `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:161`
- `mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:187`
- `mVideoFragment.seekTimeline(timestamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER | flag);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1902`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1894`
- `mVideoFragment.seekTimeline(timestamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER |flag);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:346`
- `mVideoFragment.seekTimeline(timestamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1898`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:462`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1898`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:480`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:350`
- `mVideoFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER | flag);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:174`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:182`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:219`
- `mVideoFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:177`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:186`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:223`
- `mVideoFragment.seekTimeline(videoClip.getInPoint(), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:609`
- `mVideoFragment.setPlayFlag(NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:2001`
- `new NvsBodyOpacitySpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3066`
- `new NvsFontSizeRatioSpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4318`
- `new NvsNormalTextSpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3187`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3255`
- `new NvsOutlineColorSpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3197`
- `new NvsOutlineOpacitySpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3302`
- `new NvsOutlineWidthSpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3192`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3253`
- `new NvsRendererIdSpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2347`
- `new NvsShadowOpacitySpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3797`
- `newCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1764`
- `NvsAnimatedSticker curAnimateSticker = mVideoFragment.getCurAnimateSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:242`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:545`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:244`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:546`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(imagePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerActivity.java:355`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:292`
- `NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(mImageSrcFilePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:419`
- `NvsBodyOpacitySpan nvsOpacitySpan =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3065`
- `NvsCaption curCaption = mVideoFragment.getCurCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:521`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:528`
- `nvsCaptionSpan = new NvsBodyOpacitySpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5171`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5181`
- `nvsCaptionSpan = new NvsColorSpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5163`
- `nvsCaptionSpan = new NvsFontFamilySpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5165`
- `nvsCaptionSpan = new NvsFontSizeRatioSpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5179`
- `nvsCaptionSpan = new NvsItalicSpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5167`
- `nvsCaptionSpan = new NvsNormalTextSpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5177`
- `nvsCaptionSpan = new NvsOutlineColorSpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5175`
- `nvsCaptionSpan = new NvsOutlineOpacitySpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5183`
- `nvsCaptionSpan = new NvsOutlineWidthSpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5161`
- `nvsCaptionSpan = new NvsRendererIdSpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5173`
- `nvsCaptionSpan = new NvsShadowOpacitySpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5185`
- `nvsCaptionSpan = new NvsUnderlineSpan(start, end);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5169`
- `NvsCaptionSpan nvsCaptionSpan = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5159`
- `NvsCaptionSpan nvsCaptionSpan = textSpanList.get(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:792`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:808`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5082`
- `NvsCaptionSpan spanByType = createSpanByType(type, mSelectionEnd, nvsCaptionSpan.getEnd());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5111`
- `NvsCaptureAnimatedSticker animatedSticker = mStreamingContext.getCaptureAnimatedStickerByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:825`, `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1859`
- `NvsCaptureAnimatedSticker captureAnimatedStickerByIndex = mStreamingContext.`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3403`
- `NvsCaptureCompoundCaption captureCompoundCaption = mStreamingContext.getCaptureCompoundCaptionByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3367`
- `NvsCaptureCompoundCaption compoundCaption = mStreamingContext.getCaptureCompoundCaptionByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:850`, `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1884`
- `NvsCaptureCompoundCaption nvsCaptureCompoundCaption = mStreamingContext.appendCaptureCompoundCaption(0, captionDuration, captionId);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:742`
- `NvsClipAnimatedSticker animatedSticker = curVideoClip.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1634`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1906`
- `NvsClipAnimatedSticker animatedSticker = isCutsomSticker ?`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:623`
- `NvsClipAnimatedSticker deleteSticker = videoClip.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:613`
- `NvsClipAnimatedSticker sticker = stickerList.get(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1856`
- `NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker RotZ", curPos - NvsClipAnimatedSticker.getInPoint());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:662`
- `NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker Scale", curPos - NvsClipAnimatedSticker.getInPoint());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:661`
- `NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker TransX", curPos - NvsClipAnimatedSticker.getInPoint());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:659`
- `NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker TransY", curPos - NvsClipAnimatedSticker.getInPoint());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:660`
- `NvsClipAnimatedSticker.setCurrentKeyFrameTime(curPos - NvsClipAnimatedSticker.getInPoint());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:654`
- `NvsClipCaption caption = curVideoClip.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1631`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2115`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:915`
- `NvsClipCaption clipCaption = clipByIndex.getFirstCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1036`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1103`
- `NvsClipCaption deleteCaption = videoClip.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2736`
- `NvsClipCaption firstCaption = meicamVideoClipCaption.getFirstCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1488`
- `NvsClipCaption mCurAddCaption = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:188`
- `NvsClipCaption newCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2752`
- `NvsClipCompoundCaption clipCompoundCaption = clipByIndex.getFirstCompoundCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1048`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1108`
- `NvsColor backgroundColor = ColorUtil.colorFloatToNvsColor(meicamCaptionClip.getBackgroundColor());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:600`
- `NvsColor backgroundColor = ColorUtil.colorStringtoNvsColor(caption.getCaptionBackground());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1638`
- `NvsColor backgroundColor = ColorUtil.colorStringtoNvsColor(captionAttr.getCaptionBackgroundColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1510`
- `NvsColor captionColor = captionByIndex.getTextColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1310`
- `NvsColor color =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3173`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3430`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4503`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2282`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2438`
- `NvsColor color = caption.getTextColor();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:647`
- `NvsColor color = ColorUtil.colorStringtoNvsColor(captionBackground);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1459`
- `NvsColor color = ColorUtil.colorStringtoNvsColor(captionColor);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:567`
- `NvsColor color = ColorUtil.colorStringtoNvsColor(captionInfo.getCaptionColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1303`
- `NvsColor color = ColorUtil.colorStringtoNvsColor(curCaptionInfo.getOutlineColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1371`
- `NvsColor color = ColorUtil.colorStringtoNvsColor(mCaptionColorList.get(pos).mColorValue);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3012`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2176`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:608`
- `NvsColor color = ColorUtil.colorStringtoNvsColor(mCaptionOutlineColorList.get(pos).mColorValue);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:731`
- `NvsColor color = ColorUtil.colorStringtoNvsColor(noColor);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3416`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2424`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:899`
- `NvsColor color = comCaption.getTextColor(index);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:129`
- `NvsColor curColor = mCurAddCaption.getBackgroundColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2376`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2470`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:878`
- `NvsColor curColor = mCurAddCaption.getOutlineColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2338`
- `NvsColor curColor = mCurAddCaption.getTextColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2195`
- `NvsColor curColor = mCurCaption.getBackgroundColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3363`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3465`
- `NvsColor curColor = mCurCaption.getBackgroundColor(editIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:941`
- `NvsColor curColor = mCurCaption.getOutlineColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3310`
- `NvsColor curColor = mCurCaption.getOutlineColor(editIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:835`
- `NvsColor curColor = mCurCaption.getTextColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3077`
- `NvsColor curColor = mCurCaption.getTextColor(editIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:644`
- `NvsColor nvsBgColor = caption.getBackgroundColor();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:680`
- `NvsColor nvsColor = caption.getOutlineColor();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:672`
- `NvsColor nvsColor = ColorUtil.colorFloatToNvsColor(backgroundColor);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:378`
- `NvsColor nvsColor = ColorUtil.colorFloatToNvsColor(outlineColor);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:326`
- `NvsColor nvsColor = ColorUtil.colorFloatToNvsColor(textColor);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:263`
- `NvsColor nvsColor = ColorUtil.colorStringtoNvsColor(caption.getShadowColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1716`
- `NvsColor nvsColor = ColorUtil.colorStringtoNvsColor(captionShadowColor);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1342`
- `NvsColor nvsColor = new NvsColor(0, 0, 0, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1352`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1476`
- `NvsColor nvsColor = new NvsColor(r, g, b, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5128`
- `NvsColor outlineColor = ColorUtil.colorFloatToNvsColor(meicamCaptionClip.getOutlineColor());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:594`
- `NvsColor outlineColor = ColorUtil.colorStringtoNvsColor(caption.getOutlineColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1684`
- `NvsColor shadowColor = mCurCaption.getShadowColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3802`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4402`
- `NvsColor shadowColor = new NvsColor(0, 0, 0, 0.5f);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2631`
- `NvsColor shadowColor = new NvsColor(0, 0, 0, 1.0f);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3696`
- `NvsColor strokeColor = ColorUtil.colorStringtoNvsColor(captionAttr.getCaptionStrokeColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1500`
- `NvsColor textColor = captureCompoundCaption.getTextColor(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3377`
- `NvsColor textColor = ColorUtil.colorFloatToNvsColor(compoundCaptionItem.getTextColor());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:195`, `libEngine/src/main/java/com/meishe/engine/local/LMeicamCompoundCaptionClip.java:125`
- `NvsColor textColor = ColorUtil.colorFloatToNvsColor(meicamCaptionClip.getTextColor());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:569`
- `NvsColor textColor = ColorUtil.colorStringtoNvsColor(caption.getCaptionColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1628`
- `NvsColor textColor = ColorUtil.colorStringtoNvsColor(captionAttr.getCaptionColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1482`
- `NvsColor textColor = ColorUtil.colorStringtoNvsColor(captionInfo.getCaptionColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2890`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2061`
- `NvsColor textColor = curCaption.getBackgroundColor();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1580`
- `NvsColor textColor = curCaption.getTextColor();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1653`
- `NvsColor textColor = mCurCaption.getTextColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2688`
- `NvsColorSpan nvsColorSpan = new NvsColorSpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3031`
- `NvsControlPointPair controlPointPair = mCurCaption.getKeyFrameControlPoint(controlType, currentKeyFrame);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1535`
- `NvsControlPointPair pairX = mCurAddCaption.getControlPoint(TRANS_X);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2110`
- `NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:808`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:829`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2056`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2944`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:801` (+2 more)
- `NvsControlPointPair pairX = newCaption.getControlPoint(TRANS_X);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1817`
- `NvsControlPointPair pairY = mCurAddCaption.getControlPoint(TRANS_Y);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2111`
- `NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:814`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:836`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2057`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2945`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:807` (+2 more)
- `NvsControlPointPair pairY = newCaption.getControlPoint(TRANS_Y);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1818`
- `NvsFontFamilySpan nvsFontFamilySpan = new NvsFontFamilySpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3593`
- `NvsFontSizeRatioSpan nvsFontSizeRatioSpan =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4317`
- `NvsItalicSpan nvsItalicSpan = new NvsItalicSpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3665`
- `NvsMultiThumbnailSequenceView multiThumbnailSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpanExt.java:35`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpanExt.java:34`
- `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:2052`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1778`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:2045`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1705`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1654`
- `NvsNormalTextSpan nvsNormalTextSpan =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3186`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3254`
- `NvsOutlineColorSpan nvsOutlineColorSpan =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3196`
- `NvsOutlineOpacitySpan nvsOutlineOpacitySpan =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3301`
- `NvsOutlineWidthSpan nvsOutlineWidthSpan =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3191`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3252`
- `NvsPanAndScan panAndScan = mVideoClip.getPanAndScan();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:250`
- `NvsRendererIdSpan nvsRendererIdSpan =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2346`
- `NvsShadowOpacitySpan nvsShadowOpacitySpan =`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3796`
- `NvsSize videoSize = avFileInfo.getVideoStreamDimension(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerActivity.java:359`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:295`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:422`
- `NvsStreamingContext.getInstance()`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1940`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:1600`
- `NvsStreamingContext.getInstance().registerFontByFilePath(assetItem.getAsset().localDirPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:1598`
- `NvsStreamingContext.getInstance().registerFontByFilePath(item.getAsset().localDirPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1938`
- `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:2002`
- `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1776`
- `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4805`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:3359`, `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:474`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:434`
- `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1775`
- `NvsTimeline timeline = TimelineUtil.newTimeline(videoResolution);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:440`
- `NvsTimelineAnimatedSticker animatedSticker = meicamStickerClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1360`
- `NvsTimelineAnimatedSticker animatedSticker = mTimeline.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1633`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1910`
- `NvsTimelineAnimatedSticker animatedSticker = stickerClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:660`
- `NvsTimelineAnimatedSticker curAnimateSticker = stickerInfo.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2050`
- `NvsTimelineAnimatedSticker deleteSticker = timeline.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1323`
- `NvsTimelineAnimatedSticker mLogoSticker = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:127`
- `NvsTimelineAnimatedSticker newSticker = newTimeline.addAnimatedSticker(oldSticker.getInPoint(),oldSticker.getOutPoint()-oldSticker.getInPoint(),oldSticker.getAnimatedStickerPackageId());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:288`
- `NvsTimelineAnimatedSticker next = oldTimeline.getNextAnimatedSticker(oldFirstSticker);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:200`
- `NvsTimelineAnimatedSticker nvsTimelineAnimatedSticker = isCustomSticker ?`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java:153`
- `NvsTimelineAnimatedSticker object = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java:239`
- `NvsTimelineAnimatedSticker oldFirstSticker = oldTimeline.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:196`
- `NvsTimelineAnimatedSticker sticker = m_timeLine.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:560`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:591`
- `NvsTimelineAnimatedSticker sticker = meicamStickerClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2393`
- `NvsTimelineAnimatedSticker sticker = stickerList.get(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1835`
- `NvsTimelineAnimatedSticker sticker = timeline.getFirstAnimatedSticker();`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:398`
- `NvsTimelineAnimatedSticker timelineAnimatedSticker = meicamStickerClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2418`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2690`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2745`
- `NvsTimelineAnimatedSticker timelineSticker = isCutsomSticker ?`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1331`
- `NvsTimelineCaption animatedSticker = meicamCaptionClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1366`
- `NvsTimelineCaption caption = ((MeicamCaptionClip) clipInfo).bindToTimeline(mTimeline, false, true);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:475`
- `NvsTimelineCaption caption = captionList.get(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:597`
- `NvsTimelineCaption caption = captionList.get(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1746`
- `NvsTimelineCaption caption = meicamCaptionClip.bindToTimeline(mTimeline, false, isIdentify);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1248`
- `NvsTimelineCaption caption = mTimeline.addCaption(text, start, durtion, mLrcCaptionPackagePath[0]);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:281`
- `NvsTimelineCaption caption = mTimeline.addCaption(text, start, durtion, mLrcCaptionPackagePath[mCurrentLrcIndex]);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:279`
- `NvsTimelineCaption caption = mTimeline.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1704`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2196`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1506`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4934`, `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:574` (+1 more)
- `NvsTimelineCaption caption = timeline.addModularCaption(getText(), getInPoint(),`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:485`
- `NvsTimelineCaption caption1 = mTimeline.addCaption(text, start, durtion, mLrcCaptionPackagePath[mCurrentLrcIndex].split(",")[0]);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:276`
- `NvsTimelineCaption caption2 = mTimeline.addCaption(text, start, durtion, mLrcCaptionPackagePath[mCurrentLrcIndex].split(",")[1]);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:277`
- `NvsTimelineCaption captionByIndex = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1278`
- `NvsTimelineCaption curCaption = captionInfo.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1508`
- `NvsTimelineCaption curCaption = meicamCaptionClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1576`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1603`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1649`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1677`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1760` (+9 more)
- `NvsTimelineCaption deleteCaption = timeline.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1404`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:420`
- `NvsTimelineCaption first = mTimeline.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:258`
- `NvsTimelineCaption firstCaption = meicamTimeline.getFirstCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1437`
- `NvsTimelineCaption firstCaption = mTimeline.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1494`
- `NvsTimelineCaption firstCaption = nvsTimeline.getFirstCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:997`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1086`
- `NvsTimelineCaption mCurCaption = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:225`
- `NvsTimelineCaption newCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:304`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1418`
- `NvsTimelineCaption next = mTimeline.getNextCaption(first);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:261`
- `NvsTimelineCaption next = oldTimeline.getNextCaption(oldFirstCaption);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:188`
- `NvsTimelineCaption nextCaption = mNvsTimeline.getFirstCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1238`
- `NvsTimelineCaption nextCaption = timeline.getNextCaption(caption);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1248`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:915`
- `NvsTimelineCaption nextCaption;`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1461`
- `NvsTimelineCaption nvsTimelineCaption = meicamCaptionClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2672`
- `NvsTimelineCaption object = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:204`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:212`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:225`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:237`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:249` (+11 more)
- `NvsTimelineCaption oldFirstCaption = oldTimeline.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:184`
- `NvsTimelineCaption timelineCaption = meicamCaptionClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2727`
- `NvsTimelineCompoundCaption animatedSticker = meicamCompoundCaptionClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1373`
- `NvsTimelineCompoundCaption caption = captionList.get(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1448`
- `NvsTimelineCompoundCaption caption = mTimeline.getFirstCompoundCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1600`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1869`
- `NvsTimelineCompoundCaption compoundCaption = timeline.getFirstCompoundCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:439`
- `NvsTimelineCompoundCaption compoundCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:70`
- `NvsTimelineCompoundCaption currCompoundCaption = meicamCompoundCaptionClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2078`
- `NvsTimelineCompoundCaption deleteCaption = timeline.getFirstCompoundCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1448`
- `NvsTimelineCompoundCaption firstCompoundCaption = nvsTimeline.getFirstCompoundCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1008`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1090`
- `NvsTimelineCompoundCaption mNvsTimelineCompoundCaption = timeline.addCompoundCaption(getInPoint(),`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:156`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:169`
- `NvsTimelineCompoundCaption newCaption = timeline.addCompoundCaption(caption.getInPoint(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1455`
- `NvsTimelineCompoundCaption nvsTimelineCompoundCaption = mTimeline.addCompoundCaption(0, mThemeModel.getEndingCaptionDuration() * Constants.US_TIME_BASE, endingCaption);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:524`
- `NvsTimelineCompoundCaption nvsTimelineCompoundCaption = mTimeline.addCompoundCaption(0, mThemeModel.getTitleCaptionDuration() * Constants.US_TIME_BASE, titleCaption);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:495`
- `NvsTimelineCompoundCaption nvsTimelineCompoundCaption = mTimeline.addCompoundCaption(itemStartDuration, mTimeline.getDuration(), compoundCaption);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:465`
- `NvsTimelineCompoundCaption timelineCompoundCaption = meicamCompoundCaptionClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2708`
- `NvsTimelineCompoundCaption timelineCompoundCaption = meicamCompoundClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2761`
- `NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:760`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:865`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:904`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:940`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1000` (+11 more)
- `NvsTimelineTimeSpan currentTimeSpanView = getCurrentTimeSpan();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:962`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:947`
- `NvsTimelineTimeSpan mDouVideoTimeSpan;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:56`
- `NvsTimelineTimeSpan timelineTimeSpan = createTimeSpan(inPoint, outPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:215`, `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:232`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:197`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:214`
- `NvsTimelineTimeSpan timelineTimeSpan = m_timelineTimeSpanArray.get(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:409`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:388`
- `NvsTimelineTimeSpan timelineTimeSpan = mTimelineEditor.addTimeSpan(inPoint, outPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1880`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1809`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1811`
- `NvsTimelineTimeSpan timelineTimeSpan = new NvsTimelineTimeSpan(m_context);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:430`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:408`
- `NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1914`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1832`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2215`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1910`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1759` (+2 more)
- `NvsTimelineTimeSpan timeSpan = addTimeSpan(mInPoint, endTime);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1609`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1610`
- `NvsTimelineTimeSpan timeSpan = addTimeSpan(mInPoint, outPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1774`
- `NvsTimelineTimeSpan timeSpan = m_timelineTimeSpanArray.get(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:184`, `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:547`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:167`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:525`
- `NvsTimelineTimeSpan timeSpan = mTimeSpanInfoList.get(i).mTimeSpan;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2315`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2228`
- `NvsTimelineTimeSpanExt mTimlineTimeSpanExt;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:49`, `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:50`
- `NvsTimelineTimeSpanExt timeSpanExt = new NvsTimelineTimeSpanExt(m_context);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:299`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:281`
- `NvsTimelineVideoFx timelineVideoFx = mTimeline.addBuiltinTimelineVideoFx(0, mTimeline.getDuration(), "Storyboard");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:591`
- `NvsTimelineVideoFx videoFx = mTimeline.getFirstTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:617`
- `NvsTrackCaption firstCaption = meicamVideoTrack.getFirstCaption();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1461`
- `NvsUnderlineSpan nvsUnderlineSpan = new NvsUnderlineSpan(mSelectionStart, mSelectionEnd);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3738`
- `NvsVideoClip meicamVideoClipCaption = meicamVideoTrackCaption.`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1486`
- `NvsVideoClip videoClip = videoTrack.appendClip(clipInfo.getFilePath());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:451`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:2047`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1774`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:2040`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1701`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1650`
- `NvsVideoEffectAnimatedSticker stickerFilter = mNvsEffectSdkContext.`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3408`
- `NvsVideoEffectCompoundCaption compoundCaptionFilter = mNvsEffectSdkContext.`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3369`
- `NvsVideoResolution videoRes = mTimeline.getVideoRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4060`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2934`
- `NvsVideoResolution videoRes = timeline.getVideoRes();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:496`
- `NvsVideoResolution videoResolution = getVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:333`
- `NvsVideoResolution videoResolution = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:421`, `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:437`
- `NvsVideoTrack meicamVideoTrackCaption = meicamTimeline.`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1484`
- `NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:2040`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:340`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1767`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1263`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:2033` (+5 more)
- `NvsVideoTrack videoTrack = timeline.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:444`
- `NvsVideoTrack videoTrackByIndex = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:443`
- `outPoint = ((NvsClipAnimatedSticker) mCurAnimateSticker).getOutPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1998`
- `outPoint = ((NvsClipCaption) caption).getOutPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:491`
- `outPoint = ((NvsClipCaption) mCurCaption).getOutPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1983`
- `outPoint = ((NvsClipCaption) newCaption).getOutPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1579`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1775`
- `outPoint = ((NvsTimelineAnimatedSticker) mCurAnimateSticker).getOutPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2001`
- `outPoint = ((NvsTimelineCaption) caption).getOutPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:488`
- `outPoint = ((NvsTimelineCaption) mCurCaption).getOutPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1980`
- `outPoint = ((NvsTimelineCaption) newCaption).getOutPoint();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1576`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1772`
- `pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:810`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:831`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:803`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:824`
- `pairX.backwardControlPoint = new NvsPointD(backwardControlPointX - mCurCaption.getInPoint(), backwardControlPointYForTransX);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:833`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:826`
- `pairX.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransX);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:812`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:805`
- `pairY = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:816`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:838`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:809`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:831`
- `pairY.backwardControlPoint = new NvsPointD(backwardControlPointX - mCurCaption.getInPoint(), backwardControlPointYForTransY);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:840`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:833`
- `pairY.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransY);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:818`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:811`
- `private ArrayList<NvsTimelineTimeSpan> m_timelineTimeSpanArray;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:56`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:53`
- `private KeyFrameInfo generateKeyFrameInfo(NvsClipAnimatedSticker sticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:790`
- `private KeyFrameInfo generateKeyFrameInfo(NvsClipCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1135`
- `private KeyFrameInfo generateKeyFrameInfo(NvsTimelineAnimatedSticker sticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:790`
- `private KeyFrameInfo generateKeyFrameInfo(NvsTimelineCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1142`
- `private List<List<PointF>> getCaptionList(NvsCaptureCompoundCaption compoundCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1183`
- `private List<NvsCaptionSpan> mList = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/CaptionInfo.java:301`
- `private NvsAnimatedSticker mCurAnimateSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:113`
- `private NvsCaption mCurCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:111`
- `private NvsCaptionSpan createSpanByType(String type, int start, int end) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5158`
- `private NvsCaptureAnimatedSticker currentAnimatedSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:313`
- `private NvsCaptureCompoundCaption currentCompoundCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:321`
- `private NvsClipAnimatedSticker curAnimatedSticker;//当前选中的贴纸 The currently selected sticker`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:66`
- `private NvsClipAnimatedSticker mAddAnimateSticker = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:135`
- `private NvsClipAnimatedSticker mCurSelectAnimatedSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:100`
- `private NvsClipCaption mCurCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:115`
- `private NvsMultiThumbnailSequenceView mMultiSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:106`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:110`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:102`
- `private NvsMultiThumbnailSequenceView mMultiThumbnailSequenceView = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltTimeSpan.java:33`
- `private NvsMultiThumbnailSequenceView mMultiThumbnailSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:95`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:96`
- `private NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/dialog/CaptionEditPop.java:91`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:92`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerActivity.java:72`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:70`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:112` (+7 more)
- `private NvsTimeline createTimeline() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:436`
- `private NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:93`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:58`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:71`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:108`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:206` (+6 more)
- `private NvsTimelineAnimatedSticker curAnimatedSticker;//当前选中的贴纸`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:61`
- `private NvsTimelineAnimatedSticker mAddAnimateSticker = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:135`
- `private NvsTimelineAnimatedSticker mCurrentAddCustomSticker = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:84`
- `private NvsTimelineAnimatedSticker mCurSelectAnimatedSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:99`
- `private NvsTimelineAnimatedSticker mLogoSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:40`
- `private NvsTimelineCaption mCurCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:111`
- `private NvsTimelineCaption mThemeCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:80`
- `private NvsTimelineCompoundCaption currentCompoundCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:109`
- `private NvsTimelineCompoundCaption mAddComCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:111`
- `private NvsTimelineCompoundCaption mCurCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:110`
- `private NvsTimelineCompoundCaption mCurCompoundCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:115`
- `private NvsTimelineEditor mTimelineEditor;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:82`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:94`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:83`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:98`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:95`
- `private NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1748`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1874`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1748`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1803`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1805`
- `private NvsTimelineTimeSpan createTimeSpan(long inPoint, long outPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:425`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:403`
- `private NvsTimelineTimeSpan getCurrentTimeSpan() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1101`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2169`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1083`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2093`
- `private NvsTimelineTimeSpan timelineTimeSpan;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:66`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:113`
- `private NvsVideoClip curVideoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:155`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:76`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:134`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:238`
- `private NvsVideoResolution getVideoResolution() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:418`
- `private Object getValueBySpan(NvsCaptionSpan nvsCaptionSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5123`
- `private static final String TAG = "NvsTimelineTimeSpanExt";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:40`
- `private static void copyCation(NvsTimeline newTimeline, NvsTimelineCaption oldCaption){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:303`
- `private static void copySticker(NvsTimeline newTimeline, NvsTimelineAnimatedSticker oldSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:287`
- `private static void removeAllCaption(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:415`
- `private static void removeAllCompoundCaption(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:434`
- `private static void removeAllSticker(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:393`
- `private static void updateCaptionAttribute(NvsCaption newCaption, CaptionInfo caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1536`
- `private static void updateCaptionAttribute(NvsTimelineCaption newCaption, MeicamCaptionClip meicamCaptionClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:522`
- `private static void updateCompoundCaptionAttribute(NvsTimelineCompoundCaption newCaption, CompoundCaptionInfo caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1469`
- `private static void updateCompoundCaptionAttribute(NvsTimelineCompoundCaption newCaption, LMeicamCompoundCaptionClip meicamCompoundCaptionClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LMeicamCompoundCaptionClip.java:114`
- `private static void updateCompoundCaptionAttribute(NvsTimelineCompoundCaption newCaption, MeicamCompoundCaptionClip meicamCompoundCaptionClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:181`
- `private String m_timeSpanType = "NvsTimelineTimeSpan";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:85`
- `private String m_timeSpanType = "NvsTimelineTimeSpan";//`
  Sources: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:82`
- `private String TAG = "NvsTimelineTimeSpan";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpan.java:28`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpan.java:28`
- `private String TAG = "NvsTimelineTimeSpanExt";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpanExt.java:18`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpanExt.java:19`
- `private void deleteCurCaptionTimeSpan(NvsTimelineCompoundCaption delCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1915`
- `private void deleteCurStickerTimeSpan(NvsClipAnimatedSticker animateSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1729`
- `private void deleteCurStickerTimeSpan(NvsTimelineAnimatedSticker animateSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1729`
- `private void refreshCompoundCaptionView(NvsTimelineCompoundCaption compoundCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:323`
- `private void removeCaption(NvsTimelineCompoundCaption delCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1795`
- `private void updateCaption(NvsTimelineCaption caption, String content) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1266`
- `private void updateTimeSpanShadow(NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:505`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:483`
- `public AnimateStickerTimeSpanInfo(NvsClipAnimatedSticker sticker, NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:187`
- `public AnimateStickerTimeSpanInfo(NvsTimelineAnimatedSticker sticker, NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:184`
- `public CaptionTimeSpanInfo(NvsClipCaption caption, NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2282`
- `public CaptionTimeSpanInfo(NvsTimelineCaption caption, NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2369`
- `public CaptionTimeSpanInfo(NvsTimelineCompoundCaption caption, NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1943`
- `public class MeicamCaptionClip extends ClipInfo<NvsTimelineCaption> implements Cloneable, Serializable {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:23`
- `public class MeicamCompoundCaptionClip extends ClipInfo<NvsTimelineCompoundCaption> implements Cloneable, Serializable {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:24`
- `public class MeicamStickerClip extends ClipInfo<NvsTimelineAnimatedSticker> implements Cloneable, IResourceParser {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java:18`
- `public class NvsTimelineTimeSpan extends RelativeLayout {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpan.java:27`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpan.java:27`
- `public class NvsTimelineTimeSpanExt extends RelativeLayout {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpanExt.java:17`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpanExt.java:18`
- `public List<NvsCaptionSpan> getList() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/CaptionInfo.java:789`
- `public NvsAnimatedSticker getCurAnimateSticker() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1781`
- `public NvsCaption getCurCaption() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1367`
- `public NvsClipAnimatedSticker mAnimateSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:184`
- `public NvsClipCaption mCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2279`
- `public NvsTimelineAnimatedSticker bindToTimeline(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java:147`
- `public NvsTimelineAnimatedSticker mAnimateSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:181`
- `public NvsTimelineCaption bindToTimeline(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:479`
- `public NvsTimelineCaption bindToTimeline(NvsTimeline timeline, boolean isNeedUpdateAttribute, boolean isIdentify) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:484`
- `public NvsTimelineCaption getCaptionByAttachment(String replaceId) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1233`
- `public NvsTimelineCaption getCaptionByIndex(int index) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1490`
- `public NvsTimelineCaption mCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2366`
- `public NvsTimelineCompoundCaption addCompoundCaptionFirst(NvsTimeline timeline, int zValue) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:168`
- `public NvsTimelineCompoundCaption bindToTimeline(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:151`
- `public NvsTimelineCompoundCaption getCompoundCaption() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:85`
- `public NvsTimelineCompoundCaption getCurrCompoundCaption() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1395`
- `public NvsTimelineCompoundCaption mCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1940`
- `public NvsTimelineTimeSpan addDouVideoTimeSpan(long inPoint, long outPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:231`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:213`
- `public NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:214`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:196`
- `public NvsTimelineTimeSpan mTimeSpan;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:182`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2367`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:185`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2280`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1941`
- `public NvsTimelineTimeSpan(Context context) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpan.java:140`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpan.java:138`
- `public NvsTimelineTimeSpanExt addTimeSpanExt(long inPoint, long outPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:292`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:274`
- `public NvsTimelineTimeSpanExt(Context context){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpanExt.java:55`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpanExt.java:54`
- `public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1392`
- `public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray, long themeDuration) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1396`
- `public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray, long themeDuration, boolean userRecordingFlag) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1400`
- `public static boolean setCompoundCaption(NvsTimeline timeline, ArrayList<CompoundCaptionInfo> captionArray) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1443`
- `public static boolean setSticker(NvsTimeline timeline, List<StickerInfo> stickerArray) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1319`
- `public static CaptionInfo saveCaptionData(NvsCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:482`
- `public static CompoundCaptionInfo saveCompoundCaptionData(NvsTimelineCompoundCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:507`
- `public static NvsTimelineAnimatedSticker addLogoWaterMark(Context context, NvsStreamingContext mStreamingContext, NvsTimeline mTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:126`
- `public static void applyAnimatedStickerAnimation(NvsAnimatedSticker animatedSticker, StickerInfo stickerInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1371`
- `public static void applyClipAnimatedSticker(NvsVideoClip videoClip, List<StickerInfo> stickerInfoList) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:609`
- `public static void applyClipCaption(NvsVideoClip videoClip, List<CaptionInfo> captionInfo, long clipDuration) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2732`
- `public static void removeLogoSticker(NvsTimelineAnimatedSticker mLogoSticker, NvsTimeline mTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:157`
- `public static void setSitckerCaptionObject(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:374`
- `public static void updateCaptionAttribute(NvsCaption newCaption, CaptionInfo caption, boolean userRecordingFlag) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1540`
- `public String setCompoundCaptionFont(NvsTimelineCompoundCaption caption, int captionIndex, String fftPath) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:935`
- `public void addNvsCaption(List<ClipInfo<?>> fromAICaptionFromVideoClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:469`
- `public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:314`
- `public void compileFailed(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:309`
- `public void compileFinished(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:304`
- `public void compileProgress(NvsTimeline timeline, int progress) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:299`
- `public void deleteSelectedTimeSpan(NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:486`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:464`
- `public void loadData(NvsTimelineAnimatedSticker sticker) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java:179`
- `public void loadData(NvsTimelineCaption caption) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:638`
- `public void loadData(NvsTimelineCompoundCaption comCaption) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:118`
- `public void moveAndRemoveNvsCaption(List<ClipInfo<?>> fromAICaptionFromVideoClip, long offset) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:452`
- `public void playBackEOF(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:424`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:396`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:161`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:419`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:648` (+5 more)
- `public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:438`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:408`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:171`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:429`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:661` (+5 more)
- `public void playStopped(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:429`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:403`, `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:166`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:424`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:653` (+5 more)
- `public void removeFromTimeline(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java:238`
- `public void selectClipAnimateStickerByHandClick(NvsVideoClip videoClip, PointF curPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1847`
- `public void selectTimeSpan(NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:467`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:445`
- `public void setCaptionTextColor(NvsColor color) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/dialog/CaptionEditPop.java:323`
- `public void setCompoundCaption(NvsTimelineCompoundCaption compoundCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:89`
- `public void setCurAnimateSticker(NvsAnimatedSticker animateSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1771`
- `public void setCurCaption(NvsCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1360`
- `public void setCurCompoundCaption(NvsTimelineCompoundCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1391`
- `public void setList(List<NvsCaptionSpan> list) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/CaptionInfo.java:785`
- `public void setMultiThumbnailSequenceView(NvsMultiThumbnailSequenceView multiThumbnailSequenceView) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltTimeSpan.java:42`
- `public void setMultiThumbnailSequenceView(NvsMultiThumbnailSequenceView thumbnailSequenceView) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineTimeSpanExt.java:208`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineTimeSpanExt.java:209`
- `public void setSpanList(NvsCaptionSpan nvsCaptionSpan, Object object,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5032`
- `public void setSpanValue(NvsCaptionSpan nvsCaptionSpan, Object object) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5042`
- `public void updateAnimateStickerCoordinate(NvsAnimatedSticker animateSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1789`
- `public void updateCaptionCoordinate(NvsCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1375`
- `public void updateCompoundCaptionCoordinate(NvsTimelineCompoundCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1403`
- `public void updateThemeCaptionCoordinate(NvsTimelineCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1327`
- `return ((NvsBodyOpacitySpan) nvsCaptionSpan).getOpacity();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5149`
- `return ((NvsFontFamilySpan) nvsCaptionSpan).getFontFamily();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5131`
- `return ((NvsFontSizeRatioSpan) nvsCaptionSpan).getFontSizeRatio();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5147`
- `return ((NvsItalicSpan) nvsCaptionSpan).isItalic();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5135`
- `return ((NvsNormalTextSpan) nvsCaptionSpan).getOutlineWidth();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5145`
- `return ((NvsOpacitySpan) nvsCaptionSpan).getOpacity();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5133`
- `return ((NvsOutlineColorSpan) nvsCaptionSpan).getOutlineColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5141`
- `return ((NvsOutlineOpacitySpan) nvsCaptionSpan).getOpacity();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5151`
- `return ((NvsOutlineWidthSpan) nvsCaptionSpan).getOutlineWidth();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5143`
- `return ((NvsRendererIdSpan) nvsCaptionSpan).getRendererId();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5139`
- `return ((NvsShadowOpacitySpan) nvsCaptionSpan).getOpacity();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5153`
- `return ((NvsUnderlineSpan) nvsCaptionSpan).isUnderline();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5137`
- `return mNvsTimelineCompoundCaption;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:165`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:177`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:258`, `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:276`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:247`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:263`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:260`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:249`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:262`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:251`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:264`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:253`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_ANIMATION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:286`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:273`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_CONTEXT;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:284`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:271`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_IN_ANIMATION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:288`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:275`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_OUT_ANIMATION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:290`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:277`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:282`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:269`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:256`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:245`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:280`, `libBase/src/main/java/com/meishe/utils/NvAsset.java:267`
- `return PackageManagerUtil.installAssetPackage(assetPackageFilePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1753`
- `seekTimeline((mAnimateStickerAssetLayout.getVisibility() == View.VISIBLE) ? mInPoint : timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:403`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:404`
- `seekTimeline(inPoint, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:646`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:746`
- `seekTimeline(inPoint, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1262`
- `seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:671`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:769`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:775`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:816`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:889` (+1 more)
- `seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:437`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:655`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:702`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:748`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:791` (+3 more)
- `seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:415`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:404`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:416`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:432`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1132`
- `seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2433`
- `seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:940`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:944`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1299`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1560`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1587` (+17 more)
- `seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:918`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:908`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1122`
- `setObject(mNvsTimelineCompoundCaption);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:163`
- `timelineTimeSpan.setMarginChangeListener(new NvsTimelineTimeSpan.OnMarginChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:269`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:251`
- `timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1761`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1885`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1759`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1814`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1816`
- `timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimOutChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1831`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1972`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1827`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1898`, `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1833`
- `timeSpanExt.setMarginChangeListener(new NvsTimelineTimeSpanExt.OnMarginChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:339`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:321`
- `type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:820`
- `updateCompoundCaptionAttribute(mNvsTimelineCompoundCaption, this);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:164`
- `videoClip.setImageMotionMode(NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:209`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:488`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:581`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2335`
- `| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:981`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:985`
- `| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:980`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:984`
- `} else if (caption instanceof NvsClipCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:489`
- `} else if (mCurAnimateSticker instanceof NvsTimelineAnimatedSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1999`
- `} else if (mCurCaption instanceof NvsClipCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1981`
- `} else if (mThemeCaption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TRAILER) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:176`
- `} else if (newCaption instanceof NvsClipCaption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1577`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1773`
- `} else if (nvsCaptionSpan instanceof NvsBodyOpacitySpan && object instanceof Float) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5069`
- `} else if (nvsCaptionSpan instanceof NvsBodyOpacitySpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5148`
- `} else if (nvsCaptionSpan instanceof NvsFontFamilySpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5047`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5130`
- `} else if (nvsCaptionSpan instanceof NvsFontSizeRatioSpan && object instanceof Float) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5067`
- `} else if (nvsCaptionSpan instanceof NvsFontSizeRatioSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5146`
- `} else if (nvsCaptionSpan instanceof NvsItalicSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5051`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5134`
- `} else if (nvsCaptionSpan instanceof NvsNormalTextSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5065`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5144`
- `} else if (nvsCaptionSpan instanceof NvsOpacitySpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5049`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5132`
- `} else if (nvsCaptionSpan instanceof NvsOutlineColorSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5057`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5140`
- `} else if (nvsCaptionSpan instanceof NvsOutlineOpacitySpan && object instanceof Float) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5071`
- `} else if (nvsCaptionSpan instanceof NvsOutlineOpacitySpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5150`
- `} else if (nvsCaptionSpan instanceof NvsOutlineWidthSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5063`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5142`
- `} else if (nvsCaptionSpan instanceof NvsRendererIdSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5055`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5138`
- `} else if (nvsCaptionSpan instanceof NvsShadowOpacitySpan && object instanceof Float) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5073`
- `} else if (nvsCaptionSpan instanceof NvsShadowOpacitySpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5152`
- `} else if (nvsCaptionSpan instanceof NvsUnderlineSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5053`, `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5136`
- `} else if (NvsCaptionSpan.SPAN_TYPE_BODY_OPACITY.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5180`
- `} else if (NvsCaptionSpan.SPAN_TYPE_COLOR.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5162`
- `} else if (NvsCaptionSpan.SPAN_TYPE_FONT_FAMILY.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5164`
- `} else if (NvsCaptionSpan.SPAN_TYPE_FONT_SIZE_RATIO.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5178`
- `} else if (NvsCaptionSpan.SPAN_TYPE_ITALIC.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5166`
- `} else if (NvsCaptionSpan.SPAN_TYPE_NORMAL_TEXT.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5176`
- `} else if (NvsCaptionSpan.SPAN_TYPE_OPACITY.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5170`
- `} else if (NvsCaptionSpan.SPAN_TYPE_OUTLINE_COLOR.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5174`
- `} else if (NvsCaptionSpan.SPAN_TYPE_OUTLINE_OPACITY.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5182`
- `} else if (NvsCaptionSpan.SPAN_TYPE_RENDER_ID.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5172`
- `} else if (NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5184`
- `} else if (NvsCaptionSpan.SPAN_TYPE_UNDERLINE.equals(type)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5168`

## capture-recording

- `clipData.imageFillMode = NvsCaptureSceneInfo.CAPTURESCENE_INFO_IMAGE_FILLMODE_CROP;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3567`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:486`
- `if (!mStreamingContext.startRecording(mCurRecordVideoPath, NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_IGNORE_VIDEO_ROTATION)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:211`
- `if (!NvsStreamingContextUtil.getInstance( ).getmStreamingContext( ).startCapturePreview(mCurrentDeviceIndex,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:219`
- `if (!NvsStreamingContextUtil.getInstance().getmStreamingContext().startCapturePreview(mCurrentDeviceIndex,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:182`
- `if ((deviceChanged || NvsStreamingContextUtil.getInstance( ).getEngineState( ) != com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:218`
- `if ((deviceChanged || NvsStreamingContextUtil.getInstance().getEngineState() != com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:181`
- `if (deviceChanged || getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3016`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1315`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:695`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:618`
- `if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3632`
- `if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2121`, `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3636`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:159`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:476`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:945`
- `if (i != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectActivity.java:333`
- `if (isInRecording || getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:196`
- `if (mPermissionGranted && (deviceChanged || getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:434`
- `if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java:166`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:429`
- `if (NvsStreamingContextUtil.getInstance().getEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:202`
- `List<NvsCaptureSceneInfo.ClipData> clipDataList = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3562`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:481`
- `mLiveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:165`
- `mRecordBtn.setBackgroundResource(i == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING ?`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1658`
- `mStreamingContext.stop(NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_SOFTWARE_VIDEO_INTRA_FRAME_ONLY_FAST_STOP);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:276`
- `NvsCaptureSceneInfo sceneInfo = new NvsCaptureSceneInfo();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3561`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:480`
- `NvsCaptureSceneInfo.ClipData clipData = new NvsCaptureSceneInfo.ClipData();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3563`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:482`
- `NvsCaptureVideoFx captureVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2651`, `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2671`
- `NvsCaptureVideoFx captureVideoFxByIndex = mStreamingContext.getCaptureVideoFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3267`, `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneEffectView.java:145`
- `NvsCaptureVideoFx curCaptureVideoFx = mStreamingContext.appendPackagedCaptureVideoFx(filterPackageId);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:733`
- `NvsCaptureVideoFx fx = mStreamingContext.getCaptureVideoFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2738`, `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2785`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1242`
- `NvsCaptureVideoFx nvsCaptureVideoFx = mStreamingContext.getCaptureVideoFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:181`
- `NvsRational videoFps = new NvsRational(30, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:330`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:370`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:413`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:456`
- `nvsStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:277`
- `NvsStreamingContext.CaptureDeviceCallback,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:185`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:62`, `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:46`
- `NvsStreamingContext.CaptureDeviceCallback, NvsStreamingContext.CaptureRecordingDurationCallback, NvsStreamingContext.CaptureRecordingStartedCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:46`
- `NvsStreamingContext.CaptureDeviceCapability capability = mStreamingContext.getCaptureDeviceCapability(deviceIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1455`
- `NvsStreamingContext.CaptureDeviceCapability mCapability = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:247`
- `NvsStreamingContext.CaptureRecordingDurationCallback,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:186`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:63`, `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:47`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:75`
- `NvsStreamingContext.CaptureRecordingDurationCallback, NvsStreamingContext.CaptureRecordingStartedCallback,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:87`
- `NvsStreamingContext.CaptureRecordingStartedCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:64`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:76`
- `NvsStreamingContext.CaptureRecordingStartedCallback,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:48`
- `NvsStreamingContext.CaptureRecordingStartedCallback, NvsStreamingContext.CapturedPictureCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:187`
- `nvsStreamingContext.playbackTimeline(mTimeLine, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:477`
- `nvsStreamingContext.seekTimeline(mTimeLine, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:304`
- `nvsStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:278`
- `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME | NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_LOW_PIPELINE_SIZE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:478`
- `NvsVideoResolution videoEditRes = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:318`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:358`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:400`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:443`
- `NvsVideoTrack mVideoTrack = mTimeLine16_9.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:465`
- `NvsVideoTrack mVideoTrack = mTimeLine21_9.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:422`
- `NvsVideoTrack mVideoTrack = mTimeLine9_16.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:339`
- `NvsVideoTrack mVideoTrack = mTimeLine9_21.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:379`
- `private NvsCaptureVideoFx mAdjustColorFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:310`
- `private NvsCaptureVideoFx mBgSegEffect;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:299`
- `private NvsCaptureVideoFx mCurCaptureVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:282`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:207`, `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectActivity.java:61`
- `private NvsCaptureVideoFx mCurrentCaptureVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:116`
- `private NvsCaptureVideoFx mGlitterFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:67`
- `private NvsStreamingContext nvsStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:50`
- `private NvsStreamingContext.CaptureDeviceCapability mCapability = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:60`, `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:63`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:104`
- `private NvsStreamingContext.CaptureDeviceCapability mCapability;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:124`
- `private NvsTimeline mTimeLine16_9;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:52`
- `private NvsTimeline mTimeLine21_9;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:64`
- `private NvsTimeline mTimeLine9_16;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:51`
- `private NvsTimeline mTimeLine9_21;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:63`
- `private void seekTimeline(NvsTimeline mTimeLine, long timestamp, int seekShowMode) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:303`
- `public class DouVideoCaptureActivity extends BasePermissionActivity implements NvsStreamingContext.CaptureDeviceCallback,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:86`
- `public class ParticleCaptureActivity extends BasePermissionActivity implements NvsStreamingContext.CaptureDeviceCallback,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:74`
- `public class ThemeCaptureActivity extends BasePermissionActivity implements NvsStreamingContext.CaptureRecordingDurationCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:57`
- `public NvsCaptureVideoFx setGlitterVideoFx(String effectFilePath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:137`
- `public void checkCapability(NvsStreamingContext.CaptureDeviceCapability capability) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/dialog/TopMoreDialog.java:328`
- `public void onPlaybackEOF(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:290`
- `public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:280`
- `public void onPlaybackStopped(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:285`
- `public void playTimeline(NvsTimeline mTimeLine, long startTime, long endTime) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:476`
- `return getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:216`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1171`
- `return NvsStreamingContextUtil.getInstance( ).getEngineState( ) == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:250`
- `return NvsStreamingContextUtil.getInstance().getEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:222`
- `seekShowMode | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:305`
- `videoEditRes.imagePAR = new NvsRational(1, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:329`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:369`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:412`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:455`

## core-lifecycle

- `"com.meicam.sdkdemo.utils.permission.extra_permission";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/permission/PermissionsActivity.java:48`
- `ASPECT_16V9(NvsConstants.AspectRatio.AspectRatio_16v9, 16.0f / 9, "16v9"),`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java:168`
- `ASPECT_1V1(NvsConstants.AspectRatio.AspectRatio_1v1, 1, "1v1"),`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java:169`
- `ASPECT_3V4(NvsConstants.AspectRatio.AspectRatio_3v4, 3.0f / 4, "3v4");`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java:172`
- `ASPECT_4V3(NvsConstants.AspectRatio.AspectRatio_4v3, 4.0f / 3, "4v3"),`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java:171`
- `ASPECT_9V16(NvsConstants.AspectRatio.AspectRatio_9v16, 9.0f / 16, "9v16"),`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java:170`
- `bitDepth = NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_16_BIT_FLOAT;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:205`
- `bitDepth = NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:203`, `app/src/main/java/com/meishe/sdkdemo/utils/ParameterSettingValues.java:61`
- `bitDepth = NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_AUTO;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:207`
- `boolean androidCameraPreferDualBufferAR = NvsStreamingContext.getInstance().isAndroidCameraPreferDualBufferAR();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/presenter/MainPresenter.java:156`
- `captureResolutionGrade, NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1317`
- `case NvsExpressionParam.TYPE_BOOLEAN:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1379`
- `case NvsExpressionParam.TYPE_FLOAT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1355`
- `case NvsExpressionParam.TYPE_INT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1367`
- `case NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_EXTREMELY_HIGH:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:355`
- `case NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:350`
- `case NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:345`
- `case NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_16_BIT_FLOAT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:306`
- `case NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:303`
- `case NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_AUTO:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:309`
- `com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:185`
- `config.put(com.meicam.sdk.NvsStreamingContext.RECORD_GOP_SIZE, 5);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java:197`
- `for (NvsExpressionParam nvsExpressionParam : expValueList) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1332`
- `if (level == NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH) {`
  Sources: `libBase/src/main/java/com/meishe/base/utils/Utils.java:668`
- `if (level == NvsStreamingContext.DEVICE_POWER_LEVEL_LOW) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:166`
- `if (null != NvsStreamingContext.getInstance()) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:163`
- `if (null == NvsStreamingContext.getInstance()) {`
  Sources: `libBase/src/main/java/com/meishe/base/utils/Utils.java:664`
- `if (rotation != NvsVideoStreamInfo.VIDEO_ROTATION_0) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1878`
- `if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_90`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2225`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:309`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:550`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:765`
- `if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_90) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1668`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:949`
- `if (supportedWidths.getUpper() >= NvsConstants.SIZE_4K_WIDTH && supportedHeights.getUpper() >= NvsConstants.SIZE_4K_HEIGHT) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:709`
- `if (width == NvsConstants.SIZE_4K_WIDTH && height == NvsConstants.SIZE_4K_HEIGHT) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:690`
- `int captureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:617`
- `int flags = NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:696`
- `int level = NvsStreamingContext.getInstance().getDeviceCpuLevel();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:164`, `libBase/src/main/java/com/meishe/base/utils/Utils.java:667`
- `int state = NvsStreamingContextUtil.getInstance().getEngineState();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:234`
- `m_captureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/ParameterSettingValues.java:52`
- `m_streamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:122`
- `mAISdkContext = NvsAIContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:292`
- `mAISdkContext = NvsAIContext.init(getApplicationContext(), licensePath, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:295`
- `mCaptureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_EXTREMELY_HIGH;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:476`
- `mCaptureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:471`
- `mCaptureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:466`
- `mCurrentVideoResolution = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:974`
- `mCurrentVideoResolution.imagePAR = new NvsRational(1, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3256`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:982`
- `mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:79`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseFragment.java:80`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseHorizontalLoadMoreAndRefreshFragment.java:78`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneFragment.java:52`, `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:30` (+15 more)
- `mStreamingContext = NvsStreamingContext.init(Utils.getApp(), licensePath, NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:177`
- `mStreamingContext = NvsStreamingContextUtil.getInstance().getmStreamingContext();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:89`
- `mStreamingContext.setHardwareErrorCallback(new NvsStreamingContext.HardwareErrorCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1948`
- `mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:137`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1925`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:169`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:919`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:209` (+3 more)
- `mStreamingContext.setWebCallback(new NvsStreamingContext.WebCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1954`
- `mStreamingEngineCallbackListener = new NvsStreamingContext.StreamingEngineCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:237`
- `NvsExpressionParam.FloatParam floatParam = nvsExpressionParam.getFloatParam();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1356`
- `NvsExpressionParam.IntParam intParam = nvsExpressionParam.getIntParam();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1368`
- `nvsRational = new NvsRational(16, 9);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:607`
- `nvsRational = new NvsRational(21, 9);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:609`
- `nvsRational = new NvsRational(9, 16);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:603`
- `nvsRational = new NvsRational(9, 21);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:605`
- `NvsRational nvsRational = new NvsRational(1, 2);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2068`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2093`
- `NvsRational nvsRational = new NvsRational(9, 16);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3264`
- `NvsRational nvsRational = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:601`
- `NvsRational rational = new NvsRational(1, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:394`
- `NvsRational videoFps = new NvsRational(30, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:951`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:491`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:350`
- `NvsRational videoFps = new NvsRational(FRAME_RATION, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1102`
- `NvsServerClient.get().cancelAll();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:220`
- `NvsServerClient.get().cancelRequest(tag);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:230`
- `NvsServerClient.get().download(tag, url, filePath, fileName, listener);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:212`
- `NvsServerClient.get().initConfig(this);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:55`
- `NvsServerClient.get().requestGet(tag, apiName, params, callback);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:62`, `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:96`, `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:114`, `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:129`, `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:139` (+3 more)
- `NvsServerClient.get().requestObjectGet(url, callBack);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:198`
- `NvsSize size = fileInfo.getVideoStreamDimension(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:172`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:159`
- `nvsStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/EditBaseActivity.java:22`
- `NvsStreamingContext instance = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:237`, `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:58`, `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:77`
- `NvsStreamingContext mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java:322`
- `NvsStreamingContext mStreamingContext = NvsStreamingContextUtil.getInstance().getmStreamingContext();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:110`
- `NvsStreamingContext streamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/repository/AppRepository.java:95`, `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:172`
- `NvsStreamingContext.close();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:115`
- `NvsStreamingContext.SdkVersion sdkVersion = NvsStreamingContext.getInstance().getSdkVersion();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/feedback/FeedBackActivity.java:113`
- `NvsStreamingContext.SdkVersion version = instance.getSdkVersion();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:60`, `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:79`
- `NvsStreamingContext.setIconSize(1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:69`
- `NvsStreamingContext.setMaxReaderCount(10);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:70`
- `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1318`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:697`
- `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3020`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:621`
- `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3019`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:620`
- `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER, null)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:438`
- `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_ENABLE_TAKE_PICTURE |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3021`
- `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE, null)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3022`
- `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE, nvsRational)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:622`
- `NvsStreamingContext.StreamingEngineCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:88`
- `NvsStreamingContextUtil.getInstance().stop();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:247`
- `NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA, false,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3431`
- `NvsVideoResolution mCurrentVideoResolution = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3253`
- `NvsVideoResolution nvsVideoResolution = new NvsVideoResolution();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1383`
- `NvsVideoResolution videoEditRes = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:487`, `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:643`, `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:683`
- `NvsVideoResolution videoEditRes = Util.getVideoEditResolution(makeRatio);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1093`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:549`
- `NvsVideoResolution videoEditRes = Util.getVideoEditResolution(NvAsset.AspectRatio_9v16);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:949`
- `NvsVideoResolution videoEditResolution = Util.getVideoEditResolution(makeRatio);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3259`, `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java:426`, `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java:359`
- `private int bitDepth = NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:98`
- `private NvsAIContext mAISdkContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:166`
- `private NvsServerClient() {`
  Sources: `libNet/src/main/java/com/meishe/net/NvsServerClient.java:49`
- `private NvsSize mVideoDimension;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:133`
- `private NvsStreamingContext m_streamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:85`
- `private NvsStreamingContext mAuxiliaryStreamingContext;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:90`
- `private NvsStreamingContext mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:99`
- `private NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:50`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneFragment.java:23`, `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:23`, `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneBottomView.java:40`, `app/src/main/java/com/meishe/sdkdemo/dialog/TopMoreDialog.java:38` (+14 more)
- `private NvsStreamingContext streamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:126`
- `private NvsStreamingContext.StreamingEngineCallback mStreamingEngineCallbackListener;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:70`
- `private NvsStreamingContextUtil() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:29`
- `private NvsVideoResolution mCurrentVideoResolution;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:167`
- `private static final NvsStreamingContextUtil ourInstance = new NvsStreamingContextUtil();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:17`
- `private static final String TAG = "NvsServerClient";`
  Sources: `libNet/src/main/java/com/meishe/net/NvsServerClient.java:40`
- `private static NvsServerClient INSTANCE = new NvsServerClient();`
  Sources: `libNet/src/main/java/com/meishe/net/NvsServerClient.java:54`
- `private String TAG = "NvsStreamingContextUtil";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:16`
- `protected NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseFragment.java:40`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseHorizontalLoadMoreAndRefreshFragment.java:38`
- `public class DouVideoEditActivity extends BasePermissionActivity implements NvsStreamingContext.StreamingEngineCallback,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:94`
- `public class LNvsObject implements Cloneable, Serializable {`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LNvsObject.java:8`
- `public class NvsConstants {`
  Sources: `libBase/src/main/java/com/meishe/base/constants/NvsConstants.java:17`, `libEngine/src/main/java/com/meishe/engine/constant/NvsConstants.java:16`
- `public class NvsError<T> {`
  Sources: `libBase/src/main/java/com/meishe/base/model/NvsError.java:9`
- `public class NvsObject<T> implements Cloneable, Serializable {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/NvsObject.java:8`
- `public class NvsStreamingContextUtil {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:15`
- `public final class NvsServerClient {`
  Sources: `libNet/src/main/java/com/meishe/net/NvsServerClient.java:39`
- `public NvsError(T error) {`
  Sources: `libBase/src/main/java/com/meishe/base/model/NvsError.java:13`
- `public NvsObject() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/NvsObject.java:15`
- `public NvsObject(T object) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/NvsObject.java:18`
- `public NvsStreamingContext createAuxiliaryStreamingContext() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:151`
- `public NvsStreamingContext getmStreamingContext() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:19`
- `public NvsStreamingContext getStreamingContext() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:75`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:313`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2905`
- `public NvsStreamingContext initStreamContext() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:175`
- `public NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:29`
- `public NvsStreamingContext nvsStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/EditBaseActivity.java:16`
- `public NvsVideoResolution getVideoResolutionByRatio(int ratio) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1382`
- `public static NvsServerClient get() {`
  Sources: `libNet/src/main/java/com/meishe/net/NvsServerClient.java:57`
- `public static NvsStreamingContextUtil getInstance() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:25`
- `public static NvsVideoResolution getVideoEditResolution(int ratio) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:640`
- `public static NvsVideoResolution getVideoEditResolution2(int ratio) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:680`
- `public static TopMoreDialog create(Context context, NvsStreamingContext streamingContext) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/dialog/TopMoreDialog.java:77`
- `public void onCapturedPictureArrived(final ByteBuffer byteBuffer, NvsVideoFrameInfo nvsVideoFrameInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3248`
- `public void onError(NvsError error) {`
  Sources: `libBase/src/main/java/com/meishe/base/model/BaseMvpActivity.java:116`, `libBase/src/main/java/com/meishe/base/model/BaseMvpFragment.java:116`
- `public void setStreamingContext(NvsStreamingContext streamingContext) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneBottomView.java:95`
- `public void show(final NvsStreamingContext streamingContext) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneBottomView.java:88`
- `return NvsConstants.AspectRatio.AspectRatio_NoFitRatio;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java:232`
- `rotation = NvsVideoStreamInfo.VIDEO_ROTATION_180;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1671`
- `rotation = NvsVideoStreamInfo.VIDEO_ROTATION_270;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1669`
- `rotation = NvsVideoStreamInfo.VIDEO_ROTATION_90;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1673`
- `streamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:229`
- `synchronized (NvsStreamingContext.class) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:77`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:315`
- `t = NvsServerClient.get().getDefaultGson().fromJson(body, type);`
  Sources: `libNet/src/main/java/com/meishe/net/custom/JsonCallback.java:119`
- `t = NvsServerClient.get().getDefaultGson().fromJson(data.toString(), type);`
  Sources: `libNet/src/main/java/com/meishe/net/custom/JsonCallback.java:113`
- `t = NvsServerClient.get().getDefaultGson().fromJson(dataArray.toString(), type);`
  Sources: `libNet/src/main/java/com/meishe/net/custom/JsonCallback.java:115`
- `videoEditRes.imagePAR = new NvsRational(1, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:950`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1101`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:490`
- `videoResolution.imagePAR = new NvsRational(1, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:349`
- `void onError(NvsError error);`
  Sources: `libBase/src/main/java/com/meishe/base/model/IBaseView.java:26`
- `| NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE, null)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1319`
- `| NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:698`
- `|| rotation == NvsVideoStreamInfo.VIDEO_ROTATION_270) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2226`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:310`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:551`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:766`
- `} else if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_180) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1670`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:953`
- `} else if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_270) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1672`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:955`

## effects-transforms

- `&& TextUtils.equals(attachment, NvsConstants.VALUE_CROP_FULL_TRANSFORM)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2589`
- `&& TextUtils.equals(type, NvsConstants.KEY_MASK_GENERATOR_SIGN_MASK)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2323`
- `, List<NvsExpressionParam> expValueList`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:130`
- `, NvsTimeline.NvsTimelineWatermarkPosition_TopLeft, waterMark.getWatermarkX(), waterMark.getWatermarkY());`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:305`
- `ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDesArray = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:158`
- `bgFx.setBooleanVal(NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR_NEW_MODE_ENABLE, true);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2423`
- `bgFx.setColorVal(NvsConstants.PROPERTY_KEY_BACKGROUND_COLOR, ColorUtil.colorStringtoNvsColor(backGroundInfo.getColorValue()));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2412`
- `bgFx.setColorVal(NvsConstants.PROPERTY_KEY_BACKGROUND_COLOR, new NvsColor(0, 0, 0, 0));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2419`
- `bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_BACKGROUND_BLUR_RADIUS, backGroundInfo.getValue());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2425`
- `bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_ROTATION, backGroundInfo.getRotation());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2431`
- `bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_SCALE_X, backGroundInfo.getScaleX());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2427`
- `bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_SCALE_Y, backGroundInfo.getScaleY());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2428`
- `bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_TRANS_X, backGroundInfo.getTransX());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2429`
- `bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_TRANS_Y, backGroundInfo.getTransY());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2430`
- `bgFx.setMenuVal(NvsConstants.PROPERTY_KEY_BACKGROUND_MODE, NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2422`
- `bgFx.setMenuVal(NvsConstants.PROPERTY_KEY_BACKGROUND_MODE, NvsConstants.PROPERTY_VALUE_BACKGROUND_COLOR_SOLID);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2410`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2418`
- `bgFx.setMenuVal(NvsConstants.PROPERTY_KEY_BACKGROUND_MODE, NvsConstants.PROPERTY_VALUE_BACKGROUND_IMAGE_FILE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2415`
- `bgFx.setStringVal(NvsConstants.PROPERTY_KEY_BACKGROUND_IMAGE, "");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2411`
- `bgFx.setStringVal(NvsConstants.PROPERTY_KEY_BACKGROUND_IMAGE, backGroundInfo.getFilePath());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2416`
- `ByteBuffer byteBufferResult = mEffectRenderCore.renderEffects(effects.toArray(new NvsEffect[effects.size()]),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3429`
- `case NvsExpressionParam.TYPE_BOOLEAN:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:545`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:174`
- `case NvsExpressionParam.TYPE_COLOR:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1346`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:512`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:147`
- `case NvsExpressionParam.TYPE_FLOAT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:521`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:154`
- `case NvsExpressionParam.TYPE_INT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:533`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:164`
- `case NvsFxDescription.ParamInfoObject.PARAM_TYPE_BOOL:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:246`
- `case NvsFxDescription.ParamInfoObject.PARAM_TYPE_COLOR:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:257`
- `case NvsFxDescription.ParamInfoObject.PARAM_TYPE_FLOAT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:243`
- `case NvsFxDescription.ParamInfoObject.PARAM_TYPE_INT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:239`
- `case NvsFxDescription.ParamInfoObject.PARAM_TYPE_MENU:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:250`
- `case NvsFxDescription.ParamInfoObject.PARAM_TYPE_POSITION2D:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:260`
- `case NvsFxDescription.ParamInfoObject.PARAM_TYPE_POSITION3D:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:263`
- `case NvsFxDescription.ParamInfoObject.PARAM_TYPE_STRING:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:253`
- `clip.setSourceBackgroundMode(NvsVideoClip.ClIP_BACKGROUNDMODE_BLUR);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:398`
- `colorInfo.setColorValue(ColorUtil.nvsColorToHexString(new NvsColor(colorInfo.r, colorInfo.g, colorInfo.b, 1.0F)));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/view/MultiColorView.java:87`
- `com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:222`
- `com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:221`
- `compileConfigurations.put(NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER, settingValues.getExportConfig());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:73`
- `ConcurrentHashMap<String, Long> mNvsVideoFxAnimationDurationMap = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:695`
- `cropperRatio = com.meishe.engine.constant.NvsConstants.VALUE_CROPPER_FREE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2537`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2680`
- `cropperVideoFx = videoClip.appendRawBuiltinFx(NvsConstants.Crop.NAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2543`
- `cropperVideoFx = videoClip.appendRawBuiltinFx(NvsConstants.KEY_MASK_GENERATOR);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2686`
- `cropperVideoFx.setArbDataVal(com.meishe.engine.constant.NvsConstants.KEY_CROPPER_REGION_INFO, nvsMaskRegionInfo);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2706`
- `cropperVideoFx.setAttachment(NvsConstants.KEY_MASK_GENERATOR_TYPE, KEY_MASK_GENERATOR_SIGN_CROP);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2544`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2693`
- `cropperVideoFx.setBooleanVal(com.meishe.engine.constant.NvsConstants.KEY_CROPPER_KEEP_RGB, true);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2707`
- `cropperVideoFx.setFloatVal(NvsConstants.Crop.BOUNDING_BOTTOM, bBottom);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2570`
- `cropperVideoFx.setFloatVal(NvsConstants.Crop.BOUNDING_LEFT, bLeft);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2567`
- `cropperVideoFx.setFloatVal(NvsConstants.Crop.BOUNDING_RIGHT, bRight);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2569`
- `cropperVideoFx.setFloatVal(NvsConstants.Crop.BOUNDING_TOP, bTop);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2568`
- `cropperVideoFx.setFloatVal(NvsConstants.KEY_CROPPER_ASSET_ASPECT_RATIO, ratioValue);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2549`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2695`
- `cropperVideoFx.setStringVal(NvsConstants.KEY_CROPPER_RATIO, cropperRatio);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2548`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2694`
- `effectsInfo.setColor(new NvsColor(red, green, blue, alphaF));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2368`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:126`
- `extraTransformVideoFx = videoClip.appendRawBuiltinFx(NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2509`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2650`
- `flag |= NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_SPEED_COMP_MODE;`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:996`
- `float angle, NvsLiveWindow liveWindow,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:554`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:597`
- `for (Map.Entry<String, NvsColor> entry : entries) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:798`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1019`
- `for (NvsExpressionParam nvsExpressionParam : expValueList) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:502`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:137`
- `for (NvsFxDescription.ParamInfoObject param : paramInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1049`, `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:234`
- `for (NvsVideoFx filterFx : filterFxs) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:100`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:130`
- `fullTransformFx = videoClip.appendRawBuiltinFx(NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2596`
- `fullTransformFx.setAttachment(NvsConstants.KEY_CROP_FULL_TRANSFORM, NvsConstants.VALUE_CROP_FULL_TRANSFORM);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2597`
- `fullTransformFx.setFloatVal(NvsConstants.KEY_CROPPER_SCALE_X, scale);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2599`
- `fullTransformFx.setFloatVal(NvsConstants.KEY_CROPPER_SCALE_Y, scale);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2600`
- `getVideoFxs().add(transformNvsVideoFx);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:688`
- `HashMap<String, NvsColor> filterColorParam = filterItem.getFilterColorParam();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:795`
- `HashMap<String, NvsColor> filterColorParam = mVideoClipFxInfo.getFilterColorParam();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:447`
- `HashMap<String, NvsColor> filterColorParam = videoClipFxData.getFilterColorParam();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1016`
- `if (adjustSpecialEffectsInfo.getType() == NvsExpressionParam.TYPE_COLOR) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/AdjustSpecialEffectsView.java:126`
- `if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:222`
- `if (i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:181`
- `if (mClipFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:380`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:421`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:504`
- `if (meicamFxParam != null && meicamFxParam.getValue().equals(NvsConstants.VALUE_COLOR_BACKGROUND_MODE)) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:850`
- `if (meicamVideoFx.getDesc().equals(NvsConstants.KEY_MASK_GENERATOR)) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2976`
- `if (mNvsEffectSdkContext == null) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:91`, `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:93`, `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:95`
- `if (mNvsVideoFxAnimationDurationMap.size() > 0) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:707`
- `if (mNvsVideoFxMap.containsKey(mSelectedClipPosition)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:582`
- `if (mRatio == NvsConstants.AspectRatio.AspectRatio_NoFitRatio) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1405`
- `if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:359`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:401`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:441`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:175`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:252`
- `if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:283`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:293`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:303`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:313`
- `if (NvsConstants.KEY_MASK_GENERATOR.equals(desc) && BaseConstants.EnableRawFilterMaskRender) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:249`
- `if (NvsConstants.KEY_MASK_GENERATOR.equals(type) && BaseConstants.EnableRawFilterMaskRender) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1018`
- `if (NvsConstants.PROPERTY_FX.equals(fx.desc)) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1254`
- `if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:570`
- `if (playState != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:527`
- `if (ratio == NvsConstants.AspectRatio.AspectRatio_NoFitRatio) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1040`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1047`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1236`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1248`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1294` (+1 more)
- `if (rawVideoFx != null && rawVideoFx.getAttachment(NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM) != null) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2503`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2643`
- `if (rawVideoFx != null && rawVideoFx.getAttachment(NvsConstants.CUT_FX_TYPE_FOR_TRANSFORM) != null) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2635`
- `if (rawVideoFx != null && TextUtils.equals(rawVideoFx.getBuiltinVideoFxName(), NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D)) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2496`
- `if (state != NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:130`
- `if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:236`
- `if (streamingEngineState != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:106`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:136`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:320`
- `if (SUB_TYPE_MASK.equals(meicamVideoFx.getSubType()) && meicamVideoFx.getDesc().equals(NvsConstants.KEY_MASK_GENERATOR)) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2980`
- `if (TextUtils.equals(fawFx.getBuiltinVideoFxName(), NvsConstants.KEY_MASK_GENERATOR)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2322`
- `if (TextUtils.equals(rawVideoFx.getBuiltinVideoFxName(), NvsConstants.CUT_KEY_MASK_GENERATOR)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2487`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2626`
- `if (TextUtils.equals(rawVideoFx.getBuiltinVideoFxName(), NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2588`
- `if (timelineVideoFx.getTimelineVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1125`
- `if (transformNvsVideoFx != null) {//最后添加transform2D特效  You need to add the transform2D effect at the end`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:686`
- `if (value instanceof NvsArbitraryData) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:236`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:294`
- `if (value instanceof NvsColor) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:476`
- `if (videoFx.getVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:461`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:716`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:959`
- `if (videoTransitionType == NvsVideoTransition.VIDEO_TRANSITION_TYPE_BUILTIN) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:192`
- `if(oldFx.getVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:145`
- `if(oldVideoFx.getTimelineVideoFxType() == NvsTimelineVideoFx.TIMELINE_VIDEOFX_TYPE_BUILTIN){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:273`
- `if(oldVideoTrack.getTransitionBySourceClipIndex(j).getVideoTransitionType() == NvsVideoTransition.VIDEO_TRANSITION_TYPE_BUILTIN){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:166`
- `info.setColor((NvsColor) value);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:477`
- `info.setColor(new NvsColor(red, green, blue, alphaF));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:193`
- `int flag = NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_SPEED_COMP_MODE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:289`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2064`
- `isPlaying = mClipFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:296`
- `List<NvsEffect> effects = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3263`
- `List<NvsFxDescription.ParamInfoObject> paramInfo = fxDescription.getAllParamsInfo();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1048`, `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:233`
- `List<NvsPosition2D> nvsPosition2DS = buildNvsPositionListFromPointFList(pointFList, liveWindow, size);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:844`
- `List<NvsPosition2D> nvsPosition2DS = buildNvsPositionListFromPointFList(pointFS, liveWindow, size);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:828`
- `List<NvsPosition2D> nvsPosition2DS = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:943`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1114`
- `List<NvsPosition2D> position2DList = buildNvsPositionListFromPointFList(allPoints, liveWindow, size);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:908`
- `List<NvsPosition2D> position2DList = buildNvsPositionListFromPointFList(pointArray, liveWindow, size);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:791`
- `List<NvsTimelineVideoFx> timelineVideoFxByTimelinePosition = mTimeline.getTimelineVideoFxByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:591`
- `List<NvsVideoFx> filterFxs = TimelineUtil.getFilterFxs();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:98`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:128`
- `Log.d("ParameterSetting", "compile name:" + NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER +`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:74`
- `long hasBeforeKeyFrame = mCurrentFx.findKeyframeTime(FILTER_INTENSITY, currentTimeStamp, NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:258`
- `long hasNextKeyFrame = mCurrentFx.findKeyframeTime(FILTER_INTENSITY, currentTimeStamp, NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:264`
- `long trimOut, NvsVideoFx transformFx) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:739`
- `map.put(NvsConstants.PACKAGE_EFFECT_IN, paramEle);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:883`
- `map.put(NvsConstants.PACKAGE_EFFECT_OUT, paramTwe);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:884`
- `maskFx = videoClip.appendRawBuiltinFx(NvsConstants.KEY_MASK_GENERATOR);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2338`
- `maskFx.setAttachment(NvsConstants.KEY_MASK_GENERATOR_TYPE, NvsConstants.KEY_MASK_GENERATOR_SIGN_MASK);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2341`
- `maskFx.setStringVal(NvsConstants.KEY_MASK_STORYBOARD_DESC, "");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2357`
- `maskFx.setStringVal(NvsConstants.KEY_MASK_STORYBOARD_DESC, infoData.getTextStoryboard());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2353`
- `mClipVideoFxAnimationDurationMap.put(mSelectedClipPosition, mNvsVideoFxAnimationDurationMap);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:700`
- `mCurrentNvsVideoClip = nvsVideoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:132`
- `mCurrentNvsVideoClip = videoTrack.getClipByIndex(position);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:240`
- `mEffectRenderCore = mNvsEffectSdkContext.createEffectRenderCore();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:401`
- `mEffectRenderCore.initialize(NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3427`
- `MeicamFxParam meicamFxParam = map.get(NvsConstants.KEY_BACKGROUND_MODE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:849`
- `MeicamFxParam param = map.get(NvsConstants.POST_PACKAGE_ID_OLD);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:892`
- `MeicamFxParam paramEle = new MeicamFxParam("float", NvsConstants.PACKAGE_EFFECT_IN, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:879`
- `MeicamFxParam paramNine = new MeicamFxParam("String", NvsConstants.POST_PACKAGE_ID, "");`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:877`
- `MeicamFxParam paramTen = new MeicamFxParam("boolean", NvsConstants.IS_POST_STORY_BOARD_3D, false);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:878`
- `MeicamFxParam paramTwe = new MeicamFxParam("float", NvsConstants.PACKAGE_EFFECT_OUT, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:880`
- `MeicamVideoFx transformNvsVideoFx = getVideoFx(NvsConstants.FX_TRANSFORM_2D);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:673`
- `meicamVideoFx.setBooleanVal(NvsConstants.IS_POST_STORY_BOARD_3D, false);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:832`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1271`
- `meicamVideoFx.setDesc(NvsConstants.PROPERTY_FX);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:804`
- `meicamVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_ROTATION, 0F);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:827`
- `meicamVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_SCALE_X, 1.0F);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:823`
- `meicamVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_SCALE_Y, 1.0F);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:824`
- `meicamVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_TRANS_X, 0F);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:825`
- `meicamVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_TRANS_Y, 0F);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:826`
- `meicamVideoFx.setFloatVal(NvsConstants.KEY_BACKGROUND_BLUR_RADIUS, -1);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:828`
- `meicamVideoFx.setFloatVal(NvsConstants.KEY_BACKGROUND_BLUR_RADIUS, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:794`
- `meicamVideoFx.setFloatVal(NvsConstants.PACKAGE_EFFECT_IN, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:833`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1272`
- `meicamVideoFx.setFloatVal(NvsConstants.PACKAGE_EFFECT_OUT, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:834`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1273`
- `meicamVideoFx.setStringVal(NvsConstants.KEY_BACKGROUND_COLOR, ColorsConstants.BACKGROUND_DEFAULT_COLOR);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:793`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:822`
- `meicamVideoFx.setStringVal(NvsConstants.KEY_BACKGROUND_IMAGE_PATH, "");`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:829`
- `meicamVideoFx.setStringVal(NvsConstants.KEY_BACKGROUND_MODE, NvsConstants.VALUE_COLOR_BACKGROUND_MODE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:821`
- `meicamVideoFx.setStringVal(NvsConstants.POST_PACKAGE_ID, "");`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:831`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1270`
- `meicamVideoFx.setStringVal(NvsConstants.POST_PACKAGE_ID, valuePackageId);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:896`
- `mKeyFrameSequenceView.setOnScrollChangeListenser(new NvsMultiThumbnailSequenceView.OnScrollChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:195`
- `mLiveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTCROP);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:201`
- `mNvsEffectSdkContext = getEffectContext();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:45`
- `mNvsEffectSdkContext = NvsEffectSdkContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:94`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseFragment.java:81`
- `mNvsEffectSdkContext = TimelineUtil.initEffectSdkContext(getApplicationContext(), licensePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:97`
- `mNvsEffectSdkContext= NvsEffectSdkContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseHorizontalLoadMoreAndRefreshFragment.java:79`
- `mNvsMultiThumbnailSequenceView.setThumbnailImageFillMode(NvsMultiThumbnailSequenceView.THUMBNAIL_IMAGE_FILLMODE_ASPECTCROP);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:111`
- `mNvsVideoFxAnimationDurationMap = mClipVideoFxAnimationDurationMap.get(mSelectedClipPosition);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:697`
- `mNvsVideoFxAnimationDurationMap = new ConcurrentHashMap<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:699`
- `mNvsVideoFxAnimationDurationMap.put(filterItem.getPackageId(), value);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:703`
- `mNvsVideoFxAnimationDurationMap.put(key, value);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:711`
- `mNvsVideoFxMap = new HashMap<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:278`
- `mNvsVideoFxMap.put(mSelectedClipPosition, mPositionerVideoFx);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:616`
- `mPositionerVideoFx = mNvsVideoFxMap.get(mSelectedClipPosition);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:583`
- `mRatio = NvsConstants.AspectRatio.AspectRatio_NoFitRatio;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1215`
- `mStreamingContext = NvsStreamingContext.getInstance( );`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:96`
- `mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java:94`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:126`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:85`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:71`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:74` (+6 more)
- `mStreamingContext.playbackTimeline(mTimeline, mStartTime, mStartTime + getDuration(), NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1371`
- `mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1367`
- `mStreamingContext.seekTimeline(mTimeline, beforeKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:173`
- `mStreamingContext.seekTimeline(mTimeline, nextKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:156`
- `mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1376`
- `mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:144`
- `mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:166`
- `mStreamingContext.setSeekingCallback(new NvsStreamingContext.SeekingCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:172`
- `mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:178`
- `mTimeline.addWatermark(waterMarkPath, pictureW,pictureH,1, NvsTimeline.NvsTimelineWatermarkPosition_TopRight , marginX, marginY);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java:34`
- `mVideoFragment.setPlayFlag(NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:250`
- `mVideoFragment.setVideoClipInfo(mCurrentClipInfo, mCurrentNvsVideoClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:250`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:351`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:478`
- `NvsColor color = new NvsColor(1, 1, 1, 1);`
  Sources: `libBase/src/main/java/com/meishe/utils/ColorUtil.java:33`, `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java:23`
- `NvsColor nvsColor = nvsExpressionParam.getColor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1347`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:513`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:148`
- `NvsColor sampledColor = getColorFromLiveWindow(event);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:163`
- `NvsColor value = entry.getValue();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:800`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1021`
- `NvsConstants.AspectRatio.AspectRatio_4v3, NvsConstants.AspectRatio.AspectRatio_18v9, NvsConstants.AspectRatio.AspectRatio_21v9};`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CuttingMenuView.java:61`
- `NvsConstants.AspectRatio.AspectRatio_9v16, NvsConstants.AspectRatio.AspectRatio_3v4, NvsConstants.AspectRatio.AspectRatio_9v18,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CuttingMenuView.java:59`
- `NvsConstants.AspectRatio.AspectRatio_9v21, NvsConstants.AspectRatio.AspectRatio_1v1, NvsConstants.AspectRatio.AspectRatio_16v9,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CuttingMenuView.java:60`
- `NvsConstants.AspectRatio.AspectRatio_NoFitRatio,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CuttingMenuView.java:58`
- `NvsEffect nvsEffect = effects.get(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3435`
- `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3428`
- `NvsEffectSdkContext.close();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:114`
- `NvsExpressionParam.FloatParam floatParam = nvsExpressionParam.getFloatParam();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:522`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:155`
- `NvsExpressionParam.IntParam intParam = nvsExpressionParam.getIntParam();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:534`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:165`
- `NvsFx fx = getFxFromClip();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:244`
- `NvsFx fxFromClip = getFxFromClip();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:147`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:164`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:181`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:196`
- `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:150`
- `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:167`
- `NvsFxDescription fxDescription =  streamingContext.getVideoFxDescription(oldBuiltFx.getDescription().getName());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:231`
- `NvsLiveWindow liveWindow, PointF size) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:806`
- `NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:561`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:602`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:808`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:846`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:869` (+2 more)
- `NvsMaskRegionInfo nvsMaskRegionInfo = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:971`
- `NvsMaskRegionInfo result = gson.fromJson(json, type);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:302`
- `NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:606`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:813`
- `NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_ELLIPSE2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:565`
- `NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:850`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:874`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1121`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2699`
- `NvsMaskRegionInfo.Transform2D transform2D = new NvsMaskRegionInfo.Transform2D();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:577`
- `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDes = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:159`
- `NvsParticleSystemContext particleContext = mCurrentVideoFx.getParticleSystemContext();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:175`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:532`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:565`
- `nvsPosition2DS.add(new NvsPosition2D(regionData[i], regionData[++i]));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1117`
- `nvsPosition2DS.add(new NvsPosition2D(result.x, result.y));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:947`
- `NvsStreamingContext streamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/viewmodel/CaptureEffectTabViewModel.java:55`
- `NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeline, mTimeline.getDuration() / 1000000D / seekBar.getWidth());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:254`
- `NvsStreamingContext.StreamingEngineCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:49`
- `NvsTimeline timeline = TimelineUtil.createSingleClipTimeline(mClipInfo, true);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:96`
- `NvsTimeline timeline = TimelineUtil.createTimeline();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:40`
- `NvsTimelineVideoFx fx = mTimeline.addBuiltinTimelineVideoFx(inPoint, duration, asset.uuid);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1354`
- `NvsTimelineVideoFx fx = mTimeline.addPackagedTimelineVideoFx(inPoint, duration, asset.uuid);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1364`
- `NvsTimelineVideoFx lastFx = mTimeline.getLastTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:713`
- `NvsTimelineVideoFx lastVideoFx = mTimeline.getLastTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:349`
- `NvsTimelineVideoFx mCurrentFx = timeline.getFirstTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:747`
- `NvsTimelineVideoFx newBuiltVideoFx = newTimeline.addBuiltinTimelineVideoFx(oldVideoFx.getInPoint(),oldVideoFx.getOutPoint()-oldVideoFx.getInPoint(),oldVideoFx.getBuiltinTimelineVideoFxName());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:274`
- `NvsTimelineVideoFx newPackageVideoFx =  newTimeline.addPackagedTimelineVideoFx(oldVideoFx.getInPoint(),oldVideoFx.getOutPoint()-oldVideoFx.getInPoint(),oldVideoFx.getTimelineVideoFxPackageId());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:280`
- `NvsTimelineVideoFx next = oldTimeline.getNextTimelineVideoFx(oldFirstVideoFx);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:213`
- `NvsTimelineVideoFx nextFx = timeline.removeTimelineVideoFx(timeline.getFirstTimelineVideoFx());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1043`
- `NvsTimelineVideoFx nvsTimelineVideoFx = meicamTimelineVideoFxClip.bindToTimeline(timeline);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:220`
- `NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.addBuiltinTimelineVideoFx(currentPreviewBean.getStartDuration(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:248`
- `NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.addPackagedTimelineVideoFx(0,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:488`
- `NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.addPackagedTimelineVideoFx(0, mTimeline.getDuration(), filterPackageId);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:40`
- `NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.addPackagedTimelineVideoFx(currentPreviewBean.getStartDuration(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:257`
- `NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.addPackagedTimelineVideoFx(inPoint,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:518`
- `NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.getFirstTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1878`
- `NvsTimelineVideoFx nvsTimelineVideoFx = timeline.getFirstTimelineVideoFx();`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:181`
- `NvsTimelineVideoFx nvsTimelineVideoFx = timelineVideoFxByTimelinePosition.get(i);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:594`
- `NvsTimelineVideoFx nvsTimelineVideoFx;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java:155`
- `NvsTimelineVideoFx oldFirstVideoFx = oldTimeline.getFirstTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:209`
- `NvsTimelineVideoFx sharpenVideoFx = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:590`
- `NvsTimelineVideoFx story = nvsTimeline.addBuiltinTimelineVideoFx(0, nvsTimeline.getDuration(), WATERMARK_DYNAMICS_FXNAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java:67`
- `NvsTimelineVideoFx timelineVideoFx = effect.bindToTimeline(mTimeline);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1164`
- `NvsTimelineVideoFx timelineVideoFx = mTimeline.getFirstTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1123`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2118`
- `NvsTimelineVideoFx timenlineSharpenVideoFx = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:180`
- `NvsTimelineVideoFx videoFx = mTimeline.getFirstTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:198`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:313`
- `NvsTimelineVideoFx videoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:755`
- `NvsTimelineVideoFx videoFx = timeline.getFirstTimelineVideoFx();`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:409`
- `NvsTimelineVideoFx videoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:75`
- `NvsVideoClip clip = mVideoTrack.getClipByIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:810`
- `NvsVideoClip clip = mVideoTrack.getClipByIndex(position);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:515`
- `NvsVideoClip clip = track.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:161`
- `NvsVideoClip clipByIndex = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:600`
- `NvsVideoClip clipByIndex = videoTrackByIndex.getClipByIndex(position);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:179`
- `NvsVideoClip nextClip = mVideoTrack.getClipByIndex(index + 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:818`
- `NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(mSelectedClipPosition);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:127`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:552`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:574`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:308`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:330` (+1 more)
- `NvsVideoClip videoClip = mVideoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:484`
- `NvsVideoClip videoClip = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:597`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:280`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:483`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:500`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:560`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:585` (+2 more)
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:592`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:213`
- `NvsVideoEffect videoEffect = mNvsEffectSdkContext.createVideoEffect(captureVideoFxPackageId, nvsRational);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3358`
- `NvsVideoFx animationVideoFx = mNvsVideoFxMap.get(mSelectedClipPosition);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:469`
- `NvsVideoFx bgFx = videoClip.getPropertyVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2403`
- `NvsVideoFx builtinFx = clip.appendBuiltinFx("Transform 2D");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:209`
- `NvsVideoFx builtinFx = videoClip.appendBuiltinFx("Transform 2D");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:755`
- `NvsVideoFx builtInFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:955`
- `NvsVideoFx clipFx = videoClip.getFxByIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:594`, `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java:141`, `libEngine/src/main/java/com/meishe/engine/bean/background/MeicamStoryboardInfo.java:107`
- `NvsVideoFx cropperVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2479`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2618`
- `NvsVideoFx extraTransformVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2480`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2619`
- `NvsVideoFx fawFx = videoClip.getRawFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2319`
- `NvsVideoFx fullTransformFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2583`
- `NvsVideoFx fx = videoClip.getRawFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1038`
- `NvsVideoFx fx = videoClip.getRawFxByIndex(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:599`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:220`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:366`
- `NvsVideoFx fxByIndex = clipByIndex.getFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2835`
- `NvsVideoFx fxByIndex = videoClip.getRawFxByIndex(count);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2783`
- `NvsVideoFx maskFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2317`
- `NvsVideoFx mColorVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2022`
- `NvsVideoFx mColorVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:437`
- `NvsVideoFx mDenoiseVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2026`
- `NvsVideoFx mDenoiseVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_DENOISE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:460`
- `NvsVideoFx mPositionerVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:581`
- `NvsVideoFx mSharpenVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2024`
- `NvsVideoFx mSharpenVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_SHARPEN);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:450`
- `NvsVideoFx mTintVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2025`
- `NvsVideoFx mTintVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_TINT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:454`
- `NvsVideoFx mVignetteVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2023`
- `NvsVideoFx mVignetteVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_VIGETTE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:446`
- `NvsVideoFx newBuiltFx = newVideoClip.insertBuiltinFx(oldFx.getBuiltinVideoFxName(),k);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:146`
- `NvsVideoFx newPackageFx = newVideoClip.insertPackagedFx(oldFx.getVideoFxPackageId(),k);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:151`
- `NvsVideoFx nvsVideoFx = backgroundInfo.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:511`
- `NvsVideoFx nvsVideoFx = backgroundInfo.getStoryboardFx(videoClip, backgroundInfo.getSubType());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/ClipInfo.java:693`
- `NvsVideoFx nvsVideoFx = filterFx.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:662`
- `NvsVideoFx nvsVideoFx = getStoryboardFx(videoClip, type);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/background/MeicamStoryboardInfo.java:79`
- `NvsVideoFx nvsVideoFx = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1055`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:564`, `libEngine/src/main/java/com/meishe/engine/local/LMeicamVideoClip.java:434`
- `NvsVideoFx nvsVideoFx = nvsVideoClip.getPropertyVideoFx();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:786`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:808`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:845`
- `NvsVideoFx object = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:131`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:151`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:206`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:222`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:234`
- `NvsVideoFx oldFx = oldVideoClip.getFxByIndex(k);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:143`
- `NvsVideoFx packagedFx = clip.appendRawPackagedFx(name);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:987`
- `NvsVideoFx propertyVideoFx = videoClip.getPropertyVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:486`
- `NvsVideoFx rawFx = videoClip.getRawFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2724`
- `NvsVideoFx rawVideoFx = videoClip.getRawFxByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2484`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2495`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2502`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2585`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2623` (+2 more)
- `NvsVideoFx transformFx = getTransform2DFx(firstTrackClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:689`
- `NvsVideoFx transformFx = getTransform2DFx(secondTrackClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:677`
- `NvsVideoFx transformVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2481`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2620`
- `NvsVideoFx videoFx = getTransformFx(mSelectNvsVideoClip, Constants.FX_TRANSFORM_2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:569`
- `NvsVideoFx videoFx = mVideoClip.getFxByIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:346`
- `NvsVideoFx videoFx = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:247`
- `NvsVideoFx videoFx = videoClip.getFxByIndex(fxIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:459`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:714`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:957`
- `NvsVideoFx videoFx = videoClip.getFxByIndex(i);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1058`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1090`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1181`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1227`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:567` (+1 more)
- `NvsVideoFx videoFx = videoClip.getFxByIndex(i2);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2860`
- `NvsVideoFx videoFx = videoClip.getFxByIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:286`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:935`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2028`
- `NvsVideoFx videoFx = videoClip.getPropertyVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1942`
- `NvsVideoFx videoFx = videoClipFxData.bindToTimeline(clip.getObject());`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:831`
- `NvsVideoFx videoFxTransform = videoClip.appendBuiltinFx(Constants.FX_TRANSFORM_2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:516`
- `nvsVideoFx.setBooleanVal(NvsConstants.IS_POST_STORY_BOARD_3D, valueStoryBoard3D);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:951`
- `nvsVideoFx.setBooleanVal(NvsConstants.KEY_BACKGROUND_MUTLISAMPLE, true);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:819`
- `nvsVideoFx.setBooleanVal(NvsConstants.KEY_BACKGROUND_ROTATION, false);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:788`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:811`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:846`
- `nvsVideoFx.setBooleanVal(NvsConstants.KEY_VIDEO_MODE, true);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1069`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1074`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:580`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:585`
- `nvsVideoFx.setColorVal(NvsConstants.KEY_BACKGROUND_COLOR, ColorUtil.colorToNvsColor((String) map.get(NvsConstants.KEY_BACKGROUND_COLOR).getValue()));`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:852`
- `nvsVideoFx.setColorVal(NvsConstants.KEY_BACKGROUND_COLOR, ColorUtil.colorToNvsColor(ColorsConstants.BACKGROUND_DEFAULT_COLOR));`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:790`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:813`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_ROTATION, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:818`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_ROTATION, ro);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:948`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_SCALE_X, 1.0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:814`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_SCALE_X, sx);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:944`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_SCALE_Y, 1.0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:815`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_SCALE_Y, sy);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:945`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_TRANS_X, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:816`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_TRANS_X, tx);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:946`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_TRANS_Y, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:817`
- `nvsVideoFx.setFloatVal(NvsConstants.FX_TRANSFORM_2D_TRANS_Y, ty);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:947`
- `nvsVideoFx.setFloatVal(NvsConstants.KEY_BACKGROUND_BLUR_RADIUS, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:791`
- `nvsVideoFx.setFloatVal(NvsConstants.KEY_BACKGROUND_BLUR_RADIUS, radius);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:867`
- `nvsVideoFx.setFloatVal(NvsConstants.PACKAGE_EFFECT_IN, effectIn);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:952`
- `nvsVideoFx.setFloatVal(NvsConstants.PACKAGE_EFFECT_OUT, effectOut);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:953`
- `nvsVideoFx.setMenuVal(NvsConstants.KEY_BACKGROUND_MODE, NvsConstants.VALUE_BLUR_BACKGROUND_MODE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:857`
- `nvsVideoFx.setMenuVal(NvsConstants.KEY_BACKGROUND_MODE, NvsConstants.VALUE_COLOR_BACKGROUND_MODE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:787`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:810`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:851`
- `nvsVideoFx.setMenuVal(NvsConstants.KEY_BACKGROUND_MODE, NvsConstants.VALUE_IMAGE_BACKGROUND_MODE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:854`
- `nvsVideoFx.setStringVal(NvsConstants.KEY_BACKGROUND_IMAGE_PATH, (String) map.get(NvsConstants.KEY_BACKGROUND_IMAGE_PATH).getValue());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:855`
- `nvsVideoFx.setStringVal(NvsConstants.POST_PACKAGE_ID, valuePackageId);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:950`
- `NvsVideoResolution resolution = nvsTimeline.getVideoRes();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamWaterMark.java:110`
- `NvsVideoResolution resolution = TimelineUtil.getVideoEditResolutionByClip(clipInfo.getFilePath(), 1080);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:98`
- `NvsVideoResolution videoRes = mTimeline.getVideoRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:323`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1077`
- `NvsVideoResolution videoResolution = TimelineData.instance().getVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:447`
- `NvsVideoTrack mVideoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:462`
- `NvsVideoTrack mVideoTrack = timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:478`
- `NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:122`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:547`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:569`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:303`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:325` (+1 more)
- `NvsVideoTrack track = timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:160`
- `NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:238`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:364`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:396`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:426`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:103` (+10 more)
- `NvsVideoTrack videoTrackByIndex = timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:178`
- `NvsVideoTransition nvsVideoTransition = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1132`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1185`
- `NvsVideoTransition nvsVideoTransition = nvsVideoTrack.setPackagedTransition(currentClip + addClip, trans);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:105`
- `NvsVideoTransition nvsVideoTransition = videoTrack.getTransitionBySourceClipIndex(i);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1238`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1287`
- `NvsVideoTransition object = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java:156`
- `NvsVideoTransition preTrans = nvsVideoTrack.getTransitionBySourceClipIndex(videoClip.getIndex() - 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1938`
- `NvsVideoTransition transition = mVideoTrack.getTransitionBySourceClipIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:184`
- `NvsVideoTransition transition = nvsVideoTrack.getTransitionBySourceClipIndex(videoClip.getIndex());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1939`
- `NvsVideoTransition videoBuiltTransition = newVideoTrack.setBuiltinTransition(j,oldVideoTrack.getTransitionBySourceClipIndex(j).getBuiltinVideoTransitionName());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:167`
- `NvsVideoTransition videoPackageTransition = newVideoTrack.setPackagedTransition(j,oldVideoTrack.getTransitionBySourceClipIndex(j).getVideoTransitionPackageId());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:171`
- `NvsVideoTransition videoTransition = meicamTransitionInfo.bindToTimeline(TimelineDataUtil.getMainTrack().getObject());`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1072`
- `NvsVideoTransition videoTransition = nvsVideoTrack.getTransitionBySourceClipIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:118`
- `NvsVideoTransition videoTransition = transitionInfo.getVideoTransition( );`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:404`
- `NvsVideoTransition videoTransition;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java:68`
- `nvsVideoTransition.setVideoTransitionDuration(shotInfo.getTransDuration()*1000, NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:107`
- `nvsVideoTransition.setVideoTransitionDuration(transitionInfo.getTransitionInterval(), NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1147`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1203`
- `nvsVideoTransition.setVideoTransitionDuration(transitionInfo.getTransitionInterval(), NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1145`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1201`
- `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java:77`
- `Object valueEffectIn = map.get(NvsConstants.PACKAGE_EFFECT_IN).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:905`
- `Object valueEffectOut = map.get(NvsConstants.PACKAGE_EFFECT_OUT).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:906`
- `Object valueRadius = map.get(NvsConstants.KEY_BACKGROUND_BLUR_RADIUS).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:859`
- `Object valueRO = map.get(NvsConstants.FX_TRANSFORM_2D_ROTATION).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:875`
- `Object valueSX = map.get(NvsConstants.FX_TRANSFORM_2D_SCALE_X).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:871`
- `Object valueSY = map.get(NvsConstants.FX_TRANSFORM_2D_SCALE_Y).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:872`
- `Object valueTX = map.get(NvsConstants.FX_TRANSFORM_2D_TRANS_X).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:873`
- `Object valueTY = map.get(NvsConstants.FX_TRANSFORM_2D_TRANS_Y).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:874`
- `object.setArbDataVal(key, (NvsArbitraryData) value);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:237`
- `object.setVideoTransitionDuration(duration, NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java:158`
- `PointF nextPoint, PointF prePoint, NvsLiveWindow liveWindow,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:781`
- `private HashMap<String, NvsColor> filterColorParam = new HashMap<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/data/FilterItem.java:84`, `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/VideoClipFxInfo.java:41`
- `private int mRatio = NvsConstants.AspectRatio.AspectRatio_NoFitRatio;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1224`
- `private Map<Integer, NvsVideoFx> mNvsVideoFxMap;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:90`
- `private NvsColor color;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java:34`
- `private NvsColor getColorFromLiveWindow(MotionEvent event) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:193`
- `private NvsEffectRenderCore mEffectRenderCore;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:344`
- `private NvsFx getFxFromClip() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:210`
- `private NvsFx mCurrentFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:71`
- `private NvsLiveWindow mLiveWindow;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:53`
- `private NvsLiveWindowExt mLiveWindow;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:59`
- `private NvsMaskRegionInfo maskRegionInfo;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/data/mask/MaskInfoData.java:98`
- `private NvsMaskRegionInfo nvsMaskRegionInfo;`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LMeicamMaskRegionInfo.java:13`
- `private NvsMultiThumbnailSequenceView mKeyFrameSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:49`
- `private NvsStreamingContext mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:61`
- `private NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneEffectView.java:73`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:73`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:53`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:56`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:59` (+4 more)
- `private NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:66`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:54`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:60`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:57`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:60` (+5 more)
- `private NvsTimelineVideoFx mCurrentVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:110`
- `private NvsTimelineVideoFx nvsTimelineVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1096`
- `private NvsTimelineVideoFx story;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:71`
- `private NvsVideoClip mCurrentNvsVideoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:76`
- `private NvsVideoClip mVideoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:56`
- `private NvsVideoFx getStoryboardFx(NvsVideoClip videoClip, String type) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/background/MeicamStoryboardInfo.java:104`
- `private NvsVideoFx getTransform2DFx(NvsVideoClip videoClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:711`
- `private NvsVideoFx mColorVideoFx, mVignetteVideoFx, mSharpenVideoFx, mTintVideoFx, mDenoiseVideoFx, mCurrentVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:58`
- `private NvsVideoFx mVideoFx;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:55`
- `private NvsVideoTrack mVideoTrack;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:75`, `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:57`
- `private NvsVideoTransition mVideoTransition;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TransitionInfo.java:18`
- `private static boolean removeAllVideoFx(NvsVideoClip videoClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1031`
- `private static final List<NvsVideoFx> mFilterFxs = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:114`
- `private static float calculateScaleInBox(NvsLiveWindow liveWindow, ClipInfo info) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1162`
- `private static List<NvsPosition2D> buildNvsPositionListFromPointFList(PointF[] pointFList, NvsLiveWindow liveWindow, PointF size) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:942`
- `private static PointF mapViewToNormalized(PointF pointF, NvsLiveWindow liveWindow, PointF size) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:922`
- `private static void addTimeLineEffect(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:308`
- `private static void appendFilterFx(NvsVideoClip clip, VideoClipFxInfo videoClipFxData) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:942`
- `private static void buildTimelineMasicEffect(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:216`
- `private static void buildTimelineWaterMark(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:295`
- `private static void copyBuiltFx(NvsStreamingContext streamingContext, NvsFx oldBuiltFx, NvsFx newBuiltFx){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:230`
- `private static void copyVideoFx(NvsStreamingContext streamingContext, NvsTimeline newTimeline, NvsTimelineVideoFx oldVideoFx) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:272`
- `private static void maskRegionInfoAddPoints(NvsMaskRegionInfo.RegionInfo info, PointF curPoint,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:780`
- `private static void removeAllTimelineEffect(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:404`
- `private static void setTimelineAdjustEffect(NvsTimeline timeline, float adjustData, String adjustKey, String attachmentKey) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:179`
- `private transient NvsMaskRegionInfo nvsMaskRegionInfo;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamMaskRegionInfo.java:15`
- `private void changeMaskByCrop(NvsLiveWindow liveWindow, ClipInfo clipInfo, MaskInfoData maskInfoData) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:627`
- `private void changeTrimPointOnTrimAdjust(NvsVideoClip videoClip, long trimPoint, boolean isInPoint) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2912`
- `private void initKeyFrameView(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:135`
- `private void readdFilterFx(ArrayList<FilterFxInfo> filterInfos, NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1056`
- `private void removeAllFilterFx(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1042`
- `private void removeNvsVideoFx(String type) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:658`
- `private void removeTimelineAnimal(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:475`
- `private void removeVideoFx(NvsVideoClip videoClip, int videoFxType) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:930`
- `private void resetFilterFx(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1551`
- `private void setAdjustEffect(NvsVideoClip videoClip, float adjustData, String adjustKey, String attachmentKey) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1054`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:563`, `libEngine/src/main/java/com/meishe/engine/local/LMeicamVideoClip.java:433`
- `private void setAdjustEffects(NvsVideoClip videoClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:701`
- `private void setDrawRectByEffectData(NvsTimelineVideoFx videoFx, int type) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1207`
- `private void setValue(NvsVideoFx videoFx) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:276`
- `private void updateBackground(ClipInfo clipInfo, NvsVideoClip nvsVideoClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:612`
- `private void updateTransform2DFx(NvsVideoTrack videoTrack, double scaleValue, double rotateAngle, double transX, double transY) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:951`
- `propertyVideoFx.setStringVal(NvsConstants.ANIMATION_POST_PACKAGE_ID, "");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:488`
- `protected abstract NvsTimeline initTimeLine();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:223`
- `protected abstract void onFilterChanged(NvsTimeline timeline, VideoClipFxInfo changedClipFilter);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:579`
- `protected NvsEffectSdkContext mNvsEffectSdkContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseFragment.java:41`, `app/src/main/java/com/meishe/sdkdemo/capture/fragment/BaseHorizontalLoadMoreAndRefreshFragment.java:39`
- `protected NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:67`
- `protected NvsTimeline initTimeLine() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:91`
- `protected NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:64`
- `protected void onFilterChanged(NvsTimeline timeline, VideoClipFxInfo changedClipFilter) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:274`
- `protected void playbackTimelinePositionFromParent(NvsTimeline timeline, long stamp) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:290`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:122`
- `public boolean setPanAndScan(NvsVideoTrack videoTrack) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1937`
- `public class LMeicamTransition extends LNvsObject implements Cloneable, Serializable, LocalToTimelineDataAdapter<MeicamTransition> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LMeicamTransition.java:15`
- `public class LMeicamVideoFx extends LNvsObject implements Cloneable, Serializable, LocalToTimelineDataAdapter<MeicamVideoFx> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LMeicamVideoFx.java:27`
- `public class MeicamTimelineVideoFxClip extends ClipInfo<NvsTimelineVideoFx> implements Serializable {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java:23`
- `public class MeicamTransition extends NvsObject<NvsVideoTransition> implements Cloneable, Serializable,`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java:22`
- `public class MeicamVideoFx extends NvsObject<NvsVideoFx> implements Cloneable, Serializable,`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:39`
- `public HashMap<String, NvsColor> getFilterColorParam() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/data/FilterItem.java:257`, `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/VideoClipFxInfo.java:130`
- `public NvsColor getColor() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java:112`
- `public NvsEffectSdkContext getEffectContext() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:90`
- `public NvsEffectSdkContext mNvsEffectSdkContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:30`
- `public NvsMaskRegionInfo getMaskRegionInfo() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/data/mask/MaskInfoData.java:344`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamMaskRegionInfo.java:36`, `libEngine/src/main/java/com/meishe/engine/local/LMeicamMaskRegionInfo.java:34`
- `public NvsTimeline createTimeline() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:39`
- `public NvsTimeline getTimeLine() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1390`
- `public NvsTimelineVideoFx bindToTimeline(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java:151`
- `public NvsTimelineVideoFx getNvsTimelineVideoFx() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1073`
- `public NvsTimelineVideoFx getVideoFx() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:77`
- `public NvsVideoFx bindToTimeline(NvsVideoClip videoClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:243`
- `public NvsVideoFx bindToTimelineByType(NvsVideoClip videoClip, String type) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java:154`, `libEngine/src/main/java/com/meishe/engine/bean/background/MeicamStoryboardInfo.java:74`
- `public NvsVideoFx getStoryboardFx(NvsVideoClip videoClip, String type) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java:138`
- `public NvsVideoFx getTransformFx(NvsVideoClip videoClip, String type) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:591`
- `public NvsVideoTransition bindToTimeline(NvsVideoTrack videoTrack) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java:67`
- `public NvsVideoTransition getVideoTransition() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TransitionInfo.java:37`
- `public static boolean buildClipFilter(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:800`
- `public static boolean buildFilterByClip(NvsTimeline timeline, VideoClipFxInfo videoClipFxData) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:814`
- `public static boolean buildSingleClipFilter(NvsTimeline timeline, ClipInfo clipInfo, VideoClipFxInfo clipFxData) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:896`
- `public static boolean buildTimelineFilter(NvsTimeline timeline, MeicamVideoFx videoClipFxData) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:774`
- `public static boolean calculateMaskByCrop(NvsLiveWindow liveWindow, ClipInfo clipInfo, MaskInfoData maskInfoData) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1137`
- `public static boolean clearAllBuildInTransition(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:682`
- `public static boolean setTransition(NvsTimeline timeline, ArrayList<TransitionInfo> transitionInfos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1108`
- `public static boolean setTransition(NvsTimeline timeline, List<MeicamTransition> meicamTransitions) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:642`
- `public static boolean setTransition(NvsTimeline timeline, TransitionInfo transitionInfo, int index) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1166`
- `public static float[] getColorArray(NvsColor nvsColor) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java:72`
- `public static int[] nvsColortoRgba(NvsColor color) {`
  Sources: `libBase/src/main/java/com/meishe/utils/ColorUtil.java:41`
- `public static List<NvsVideoFx> getFilterFxs() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2846`
- `public static NvsColor colorFloatToNvsColor(float[] colorString) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java:57`
- `public static NvsColor colorStringtoNvsColor(String colorString) {`
  Sources: `libBase/src/main/java/com/meishe/utils/ColorUtil.java:30`
- `public static NvsColor colorToNvsColor(String colorString) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java:20`
- `public static NvsEffectSdkContext initEffectSdkContext(Context mContext, String licensePath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:127`
- `public static NvsMaskRegionInfo buildCircleMaskRegionInfo(PointF center, float maskWidth, float maskHeight,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:553`
- `public static NvsMaskRegionInfo buildHeartMaskRegionInfo(PointF center, int radius, float angle,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:805`
- `public static NvsMaskRegionInfo buildMaskRegionRect(CropInfo cropInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1109`
- `public static NvsMaskRegionInfo buildPolygonMaskRegionInfo(PointF[] pointFList, NvsLiveWindow liveWindow, PointF size) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:843`
- `public static NvsMaskRegionInfo buildRectMaskRegionInfo(PointF center, int width, int height,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:596`
- `public static NvsMaskRegionInfo buildStarMaskRegionInfo(PointF center, int width, float rotation, NvsLiveWindow liveWindow, PointF size) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:867`
- `public static NvsTimelineVideoFx setDynamicWaterMark(NvsTimeline nvsTimeline,int sceneWidth, int sceneHeight, String fileName,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java:63`
- `public static NvsVideoFx applyAnimation(NvsVideoTrack nvsVideoTrack, NvsVideoClip videoClip, AnimationInfo animationInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1928`
- `public static NvsVideoFx findOrCrateVideoFxFromVideoClip(NvsVideoClip clipByIndex) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2818`
- `public static NvsVideoFx findOrCrateVideoFxFromVideoClip(NvsVideoClip videoClip, boolean remove) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2777`
- `public static NvsVideoFx findVideoFxFromVideoClip(NvsVideoClip clipByIndex) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2829`
- `public static PointF assetSizeInBox(NvsLiveWindow liveWindowExt, float assetAspectRatio) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1024`
- `public static String nvsColorToHexString(NvsColor color) {`
  Sources: `libBase/src/main/java/com/meishe/utils/ColorUtil.java:64`
- `public static void addTimelineFilter(NvsTimeline mTimeline, String filterPackageId) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:38`
- `public static void applyBackground(NvsVideoClip videoClip, BackGroundInfo backGroundInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2397`
- `public static void applyCropData(NvsTimeline mTimeline, NvsVideoClip videoClip, ClipInfo clipInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2474`
- `public static void applyCropMaskData(NvsVideoClip videoClip, ClipInfo clipInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2613`
- `public static void applyExprVarByFilter(NvsFx nvsFx, FilterItem filterItem) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:781`
- `public static void applyFilterByTimeline(NvsTimeline timeline, FilterItem filterItem) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:739`
- `public static void applyMask(NvsVideoClip videoClip, MaskInfoData infoData) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2310`
- `public static void buildAdjustCutInfo(NvsTimeline mTimeline, ArrayList<ClipInfo> clipInfoArrayList) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2237`
- `public static void buildColorAdjustInfo(NvsTimeline`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1992`
- `public static void buildFilterByTimeline(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:724`
- `public static void buildRealMaskInfoData(MaskInfoData maskData, NvsLiveWindow liveWindowExt,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:966`
- `public static void buildTimelineBackground(NvsTimeline mTimeline, ArrayList<ClipInfo> clipInfoData) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2371`
- `public static void buildTimelineMaskClipInfo(NvsTimeline timeline, List<ClipInfo> clipInfoData) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:299`
- `public static void checkAndDeleteExitFX(NvsTimeline mTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1877`
- `public static void removeRawBuildInFx(NvsVideoClip videoClip, String rawFxName) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2718`
- `public static void setAdjustEffects(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:158`
- `public static void setDefaultBackground(ClipInfo videoClip, NvsVideoClip nvsVideoClip,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/StoryboardUtil.java:212`
- `public static void setWaterMark(NvsTimeline mTimeline, WaterMarkData waterMarkData){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java:23`
- `public void initKeyFramePointView(HashMap<Long, Double> keyFramePointList, NvsTimeline timeline, double pixelPerMicrosecond) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/KeyFramePointView.java:101`
- `public void initKeyFrameView(String mediaPath, NvsTimeline timeline, HashMap<Long, Double> keyFramePoints) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:152`
- `public void loadData(NvsTimelineVideoFx effect) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java:167`
- `public void loadData(NvsVideoTransition videoTransition) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java:83`
- `public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:189`, `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:363`
- `public void onPlaybackEOF(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:158`
- `public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:146`
- `public void onPlaybackStopped(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:151`
- `public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:168`
- `public void onScrollChanged(NvsMultiThumbnailSequenceView nvsMultiThumbnailSequenceView, int i, int i1) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:197`
- `public void onSeekingTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:174`
- `public void playBackEOF(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:197`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:327`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:263`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:130`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:554` (+1 more)
- `public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:207`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:338`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:276`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:143`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:564` (+1 more)
- `public void playStopped(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:202`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:334`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:271`, `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:138`, `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:559` (+1 more)
- `public void putFilterColorParam(String key, NvsColor value) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/VideoClipFxInfo.java:134`
- `public void removeAllTransition(NvsVideoTrack videoTrack) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1687`
- `public void removeBackground(NvsVideoClip videoClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/ClipInfo.java:681`
- `public void setColor(NvsColor color) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java:116`
- `public void setCurrentFx(NvsFx currentFx) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:89`
- `public void setDefaultBackground(ClipInfo clipInfo, NvsVideoClip videoClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:600`
- `public void setFilterColorParam(String key, NvsColor value) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/data/FilterItem.java:262`
- `public void setMaskRegionInfo(NvsMaskRegionInfo maskRegionInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/data/mask/MaskInfoData.java:348`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamMaskRegionInfo.java:32`, `libEngine/src/main/java/com/meishe/engine/local/LMeicamMaskRegionInfo.java:30`
- `public void setPointList(NvsLiveWindowExt mLiveWindow) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java:187`
- `public void setPointList(NvsLiveWindowExt mLiveWindow, NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamWaterMark.java:98`
- `public void setStreamingContext(NvsStreamingContext streamingContext, Activity activity, int type) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneEffectView.java:121`
- `public void setTimeLine(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1349`
- `public void setVideoFx(NvsTimelineVideoFx videoFx) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:105`
- `public void setVideoTransition(NvsVideoTransition videoTransition) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TransitionInfo.java:41`
- `public void updateBackground(ClipInfo clipInfo, int position, NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:174`
- `regionInfo.setEllipse2D(new NvsMaskRegionInfo.Ellipse2D(new NvsPosition2D(center.x, center.y), widthPercent, heightPercent, 0));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:576`
- `removeNvsVideoFx(videoFx.getSubType());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:603`
- `removeVideoFx(firstClip, NvsVideoFx.VIDEOFX_TYPE_PACKAGE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:909`
- `removeVideoFx(NvsConstants.FX_TRANSFORM_2D);//需要最后添加transform2D特效  You need to add the transform2D effect at the end`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:674`
- `removeVideoFx(secondClip, NvsVideoFx.VIDEOFX_TYPE_PACKAGE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:920`
- `return mNvsEffectSdkContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:102`
- `return new NvsColor(colorString[0], colorString[1], colorString[2], colorString[3]);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java:61`
- `seekTimeline(currentTime, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:247`
- `Set<Map.Entry<String, NvsColor>> entries = filterColorParam.entrySet();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:797`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1018`
- `Set<String> keySet = mNvsVideoFxAnimationDurationMap.keySet();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:708`
- `setAdjustEffect(videoClip, meicamAdjustData.getAmount(), NvsConstants.ADJUST_AMOUNT, NvsConstants.FX_SHARPEN);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:706`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:727`
- `setAdjustEffect(videoClip, meicamAdjustData.getBlackPoint(), NvsConstants.ADJUST_BLACKPOINT, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:708`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:729`
- `setAdjustEffect(videoClip, meicamAdjustData.getBrightness(), NvsConstants.ADJUST_BRIGHTNESS, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:715`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:736`
- `setAdjustEffect(videoClip, meicamAdjustData.getContrast(), NvsConstants.ADJUST_CONTRAST, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:714`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:735`
- `setAdjustEffect(videoClip, meicamAdjustData.getDegree(), NvsConstants.ADJUST_DEGREE, NvsConstants.FX_VIGNETTE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:707`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:728`
- `setAdjustEffect(videoClip, meicamAdjustData.getHighlight(), NvsConstants.ADJUST_HIGHTLIGHT, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:712`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:733`
- `setAdjustEffect(videoClip, meicamAdjustData.getSaturation(), NvsConstants.ADJUST_SATURATION, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:713`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:734`
- `setAdjustEffect(videoClip, meicamAdjustData.getShadow(), NvsConstants.ADJUST_SHADOW, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:711`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:732`
- `setAdjustEffect(videoClip, meicamAdjustData.getTemperature(), NvsConstants.ADJUST_TEMPERATURE, NvsConstants.ADJUST_TINT);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:710`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:731`
- `setAdjustEffect(videoClip, meicamAdjustData.getTint(), NvsConstants.ADJUST_TINT, NvsConstants.ADJUST_TINT);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:709`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:730`
- `setDefaultBackground(mCurrentClipInfo, mCurrentNvsVideoClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:327`
- `setLiveWindowRatio(NvsConstants.AspectRatio.AspectRatio_NoFitRatio);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1206`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getAmount(), NvsConstants.ADJUST_AMOUNT, NvsConstants.FX_SHARPEN);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:166`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getBlackPoint(), NvsConstants.ADJUST_BLACKPOINT, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:168`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getBrightness(), NvsConstants.ADJUST_BRIGHTNESS, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:175`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getContrast(), NvsConstants.ADJUST_CONTRAST, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:174`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getDegree(), NvsConstants.ADJUST_DEGREE, NvsConstants.FX_VIGNETTE);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:167`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getHighlight(), NvsConstants.ADJUST_HIGHTLIGHT, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:172`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getSaturation(), NvsConstants.ADJUST_SATURATION, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:173`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getShadow(), NvsConstants.ADJUST_SHADOW, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:171`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getTemperature(), NvsConstants.ADJUST_TEMPERATURE, NvsConstants.ADJUST_TINT);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:170`
- `setTimelineAdjustEffect(timeline, meicamAdjustData.getTint(), NvsConstants.ADJUST_TINT, NvsConstants.ADJUST_TINT);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:169`
- `sharpenVideoFx.setBooleanVal(NvsConstants.KEY_VIDEO_MODE, true);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:604`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:609`
- `String attachment = (String) rawVideoFx.getAttachment(NvsConstants.KEY_CROP_FULL_TRANSFORM);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2587`
- `String attachment = (String) rawVideoFx.getAttachment(NvsConstants.KEY_MASK_GENERATOR_TYPE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2486`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2625`
- `String type = (String) fawFx.getAttachment(NvsConstants.KEY_MASK_GENERATOR_TYPE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2321`
- `synchronized (NvsEffectSdkContext.class) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:92`
- `TimelineUtil.applyBackground(mCurrentNvsVideoClip, mCurrentClipInfo.getBackGroundInfo());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:588`
- `TimelineUtil.removeRawBuildInFx(mVideoClip, NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:111`
- `timenlineSharpenVideoFx.setBooleanVal(NvsConstants.KEY_VIDEO_MODE, true);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:193`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:199`
- `transform2D.setAnchor(new NvsPosition2D(center.x, center.y));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:579`
- `transformNvsVideoFx.bindToTimeline(getObject());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:687`
- `transformVideoFx = videoClip.appendRawBuiltinFx(NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2512`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2653`
- `transformVideoFx.setAttachment(NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM, true);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2516`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2658`
- `transformVideoFx.setAttachment(NvsConstants.CUT_FX_TYPE_FOR_TRANSFORM, true);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2522`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2664`
- `transformVideoFx.setBooleanVal(NvsConstants.CUT_KEY_IS_NORMALIZED_COORD, true);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2521`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2663`
- `transformVideoFx.setFloatVal(NvsConstants.KEY_CROPPER_ROTATION, -(transFromData.get(STORYBOARD_KEY_ROTATION_Z)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2527`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2669`
- `transformVideoFx.setFloatVal(NvsConstants.KEY_CROPPER_SCALE_X, transFromData.get(STORYBOARD_KEY_SCALE_X));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2525`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2667`
- `transformVideoFx.setFloatVal(NvsConstants.KEY_CROPPER_SCALE_Y, transFromData.get(STORYBOARD_KEY_SCALE_Y));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2526`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2668`
- `transformVideoFx.setFloatVal(NvsConstants.KEY_CROPPER_TRANS_X, transFromData.get(STORYBOARD_KEY_TRANS_X));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2523`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2665`
- `transformVideoFx.setFloatVal(NvsConstants.KEY_CROPPER_TRANS_Y, transFromData.get(STORYBOARD_KEY_TRANS_Y));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2524`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2666`
- `Type type = new TypeToken<NvsMaskRegionInfo>() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:300`
- `updateBackground(mCurrentClipInfo, mCurrentNvsVideoClip);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:309`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:328`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:338`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:346`, `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:636`
- `videoClip.getPropertyVideoFx().setFloatVal(NvsConstants.PROPERTY_OPACITY, 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:644`
- `videoClip.getPropertyVideoFx().setFloatVal(NvsConstants.PROPERTY_OPACITY, getOpacity());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:646`
- `videoClip.setSourceBackgroundMode(NvsVideoClip.ClIP_BACKGROUNDMODE_BLUR);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:416`
- `videoFx = mSelectNvsVideoClip.appendBuiltinFx(Constants.FX_TRANSFORM_2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:571`
- `videoFx.setArbDataVal(key, (NvsArbitraryData) value);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:295`
- `videoFx.setArbDataVal(NvsConstants.KEY_MASK_REGION_INFO, meicamMaskRegionInfo.getMaskRegionInfo());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:267`
- `videoFx.setBooleanVal(NvsConstants.ANIMATION_ENABLE_MUTLISAMPLE, true);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1970`
- `videoFx.setBooleanVal(NvsConstants.ANIMATION_IS_POST_STORYBOARD_3D, false);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1968`
- `videoFx.setBooleanVal(NvsConstants.KEY_MASK_INVERSE_REGION, meicamMaskRegionInfo.isRevert());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:266`
- `videoFx.setBooleanVal(NvsConstants.KEY_MASK_KEEP_RGB, true);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:265`
- `videoFx.setFloatVal(NvsConstants.ANIMATION_PACKAGE_EFFECT_IN, in);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1977`
- `videoFx.setFloatVal(NvsConstants.ANIMATION_PACKAGE_EFFECT_OUT, out);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1978`
- `videoFx.setFloatVal(NvsConstants.KEY_MASK_FEATHER_WIDTH, meicamMaskRegionInfo.getFeatherWidth());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:268`
- `videoFx.setStringVal(NvsConstants.ANIMATION_PACKAGE_ID, "");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1961`
- `videoFx.setStringVal(NvsConstants.ANIMATION_PACKAGE_ID, animationInfo.getmPackageId());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1966`
- `videoFx.setStringVal(NvsConstants.ANIMATION_POST_PACKAGE_ID, "");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1962`
- `videoFx.setStringVal(NvsConstants.ANIMATION_POST_PACKAGE_ID, animationInfo.getmPackageId());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1964`
- `void playBackEOF(NvsTimeline timeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1586`
- `void playbackTimelinePosition(NvsTimeline timeline, long stamp);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1590`
- `void playStopped(NvsTimeline timeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1588`
- `void setTimeLine(NvsTimeline timeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/ICutRegionFragment.java:51`
- `} else if (meicamFxParam != null && meicamFxParam.getValue().equals(NvsConstants.VALUE_IMAGE_BACKGROUND_MODE)) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:853`
- `} else if (videoTransitionType == NvsVideoTransition.VIDEO_TRANSITION_TYPE_PACKAGE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:195`
- `}else if(oldFx.getVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_PACKAGE){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:150`
- `}else if(oldVideoFx.getTimelineVideoFxType() == NvsTimelineVideoFx.TIMELINE_VIDEOFX_TYPE_PACKAGE){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:279`
- `}else if(oldVideoTrack.getTransitionBySourceClipIndex(j).getVideoTransitionType() == NvsVideoTransition.VIDEO_TRANSITION_TYPE_PACKAGE){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:170`

## preview-export

- `ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1056`
- `ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:309`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:225`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java:123`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:226`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:407` (+2 more)
- `Bitmap bitmap = mStreamingContext.grabImageFromTimeline(mTimeline, timelineCurrentPosition, new NvsRational(1, 1));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:141`
- `Bitmap bitmap = mStreamingContext.grabImageFromTimeline(timeline, 0, new NvsRational(1, 2));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:314`
- `boolean b = mAuxiliaryStreamingContext.grabImageFromTimelineAsync(mAuxiliaryTimeline, timestamp, new NvsRational(1, 1), flag);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:536`
- `case NvsLiveWindow.HDR_DISPLAY_MODE_DEPEND_DEVICE:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:333`
- `case NvsLiveWindow.HDR_DISPLAY_MODE_SDR:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:330`
- `case NvsLiveWindow.HDR_DISPLAY_MODE_TONE_MAP_SDR:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:336`
- `com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:184`
- `compileCallback.onCompileFailed(mNvsTimeline);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:588`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:614`
- `compileConfigurations.put(NvsStreamingContext.COMPILE_BITRATE, bitrate * 1000000);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:65`
- `compileConfigurations.put(NvsStreamingContext.COMPILE_USE_OPERATING_RATE, quickPack);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:122`
- `compileConfigurations.put(NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME, Constants.HDR_EXPORT_HEVC);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:70`
- `compileVideo(context, timeline, compileVideoPath, startTime, endTime, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, resultHeight);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:103`
- `encoderFlag = NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_HARDWARE_ENCODER;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:62`
- `final ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1123`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:786`, `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:244`
- `flag = NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:258`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:993`
- `flag = NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:273`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:551`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:976`
- `flag |= NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:532`
- `flags = flags | NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:699`
- `if (currEngineState != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2023`
- `if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2121`
- `if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:506`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:332`
- `if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2230`
- `if (getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1010`
- `if (i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:338`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1929`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:172`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:212`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:240`
- `if (m_videoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:665`
- `if (mClipFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:226`
- `if (mLiveWindow instanceof NvsLiveWindow) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:384`
- `if (mNvsMultiThumbnailSequenceView != null) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:112`
- `if (mNvsMultiThumbnailSequenceView == null) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:175`
- `if (mNvsTimeline != null && mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:275`
- `if (mStreamingContext == null || mNvsTimeline == null || mLiveWindow == null) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:332`
- `if (mStreamingContext.compileTimeline(mNvsTimeline, 0, mNvsTimeline.getDuration(),`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:581`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:608`
- `if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:69`, `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:145`
- `if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1355`
- `if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:152`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:203`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:617`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:298`
- `if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:328`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:385`
- `if (mVideoFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:157`
- `if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:307`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:788`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:306`
- `if (NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING == state || NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED == state) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:389`
- `if (playState != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1258`
- `if (settingValues.getBitDepth() != NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:72`
- `if (state != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1378`
- `if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:590`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:204`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:167`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:96`
- `if(mClipFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PicturInPicturePreviewActivity.java:85`
- `if(mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:267`
- `implements NvsIconGenerator.IconCallback {`
  Sources: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:58`
- `layoutParams.leftMargin = EditorController.getInstance().durationToLength(position - startTime, mNvsMultiThumbnailSequenceView.getPixelPerMicrosecond());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:139`
- `liveWindowModel = NvsLiveWindow.HDR_DISPLAY_MODE_DEPEND_DEVICE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:191`
- `liveWindowModel = NvsLiveWindow.HDR_DISPLAY_MODE_SDR;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:189`, `app/src/main/java/com/meishe/sdkdemo/utils/ParameterSettingValues.java:60`
- `liveWindowModel = NvsLiveWindow.HDR_DISPLAY_MODE_TONE_MAP_SDR;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:193`
- `Log.d("ParameterSetting", "compile name:" + NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME + " value:" + Constants.HDR_EXPORT_HEVC);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:71`
- `LogUtils.e("getPixelPerMicrosecond: mNvsMultiThumbnailSequenceView is null!");`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:176`
- `m_iconGenerator = new NvsIconGenerator();`
  Sources: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:701`
- `m_maxPixelPerMicrosecond = m_pixelPerMicrosecond * Math.pow(1.25, 5);//NvsMultiThumbnailSequenceView放大的m_pixelPerMicrosecond最大值`
  Sources: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:549`
- `m_minPixelPerMicrosecond = m_pixelPerMicrosecond * Math.pow(0.8, 5);//NvsMultiThumbnailSequenceView缩小的m_pixelPerMicrosecond最小值`
  Sources: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:550`
- `m_multiThumbnailSequenceView = new NvsMultiThumbnailSequenceView(context);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:111`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:103`
- `m_multiThumbnailSequenceView.setOnScrollChangeListenser(new NvsMultiThumbnailSequenceView.OnScrollChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:169`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:152`
- `m_streamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:26`
- `m_streamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:37`
- `mClipFragment.seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline), 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:327`
- `mClipFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:626`
- `mCompileCallback = new NvsStreamingContext.CompileCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:256`
- `mCompileCallback2 = new NvsStreamingContext.CompileCallback2() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:278`
- `mLiveWindow = (NvsLiveWindow) findViewById(R.id.live_window);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:304`
- `mLivewindow = (NvsLiveWindow) findViewById(R.id.livewidow);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:317`
- `mLiveWindow = (NvsLiveWindow) findViewById(R.id.liveWindow);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:99`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:141`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:186`
- `mLiveWindow = (NvsLiveWindow) findViewById(R.id.nvsLivewidow);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:115`
- `mLiveWindow = (NvsLiveWindow) rootView.findViewById(R.id.liveWindow);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:236`, `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:183`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:146`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:388`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:378`
- `mLiveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:486`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2214`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:441`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:1041`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:166`
- `mMultiThumbnailSequenceView = (NvsMultiThumbnailSequenceView) findViewById(R.id.mutilSequenceView);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java:77`
- `mNvsMultiThumbnailSequenceView = parentView.findViewById(R.id.cut_view_sequence);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:63`
- `mNvsMultiThumbnailSequenceView.scrollBy(length, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:150`
- `mNvsMultiThumbnailSequenceView.setEndPadding(mCoverMargin);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:74`
- `mNvsMultiThumbnailSequenceView.setPixelPerMicrosecond(pixelPerMicrosecond);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:110`
- `mNvsMultiThumbnailSequenceView.setScrollListener(new MultiThumbnailSequenceView2.OnScrollListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:75`
- `mNvsMultiThumbnailSequenceView.setStartPadding(mCoverMargin);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:73`
- `mNvsMultiThumbnailSequenceView.setThumbnailSequenceDescArray(sequenceDescsArray);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:124`
- `mPlaybackCallback2Listener = new NvsStreamingContext.PlaybackCallback2() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:230`
- `mPlaybackCallbackListener = new NvsStreamingContext.PlaybackCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:190`
- `mSequenceView = (NvsMultiThumbnailSequenceView) findViewById(R.id.sequence_view);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:307`
- `mStreamingContext.connectTimelineWithLiveWindow(mNvsTimeline, liveWindow);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:386`
- `mStreamingContext.connectTimelineWithLiveWindowExt(mNvsTimeline, liveWindow);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:389`
- `mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:213`
- `mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:353`
- `mStreamingContext.grabImageFromTimelineAsync(grabImageTimeline, clip.getInPoint(), new NvsRational(1, 1),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:433`
- `mStreamingContext.grabImageFromTimelineAsync(mNvsTimeline, timestamp, new NvsRational(1, 1), 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:471`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:481`
- `mStreamingContext.grabImageFromTimelineAsync(mNvsTimeline, timestamp, proxyScale, flags);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:495`
- `mStreamingContext.playbackTimeline(mNvsTimeline, start, end, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, flag);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:260`
- `mStreamingContext.playbackTimeline(mTimeline, mStreamingContext.getTimelineCurrentPosition(mTimeline), -1, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:390`
- `mStreamingContext.playbackTimeline(mTimeLine, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:586`
- `mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:64`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:288`
- `mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, flag);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:290`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2076`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:998`
- `mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, mPlayFlag | flag);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2078`
- `mStreamingContext.playbackTimeline(timeline, startTime, -1, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1006`
- `mStreamingContext.seekTimeline(grabImageTimeline, clip.getInPoint(), NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:432`
- `mStreamingContext.seekTimeline(mNvsTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode | flag);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:278`
- `mStreamingContext.seekTimeline(mTimeline, progressPosition, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:606`
- `mStreamingContext.seekTimeline(mTimeline, startDuration, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:262`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:562`
- `mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:255`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:474`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:1056`
- `mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:983`
- `mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag | seekShowMode`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:979`
- `mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:49`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:382`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:296`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1158`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:279`
- `mStreamingContext.setCompileCallback(b ? null : new NvsStreamingContext.CompileCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:205`
- `mStreamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:99`, `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:206`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:104`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:684`
- `mStreamingContext.setCompileCallback2(new NvsStreamingContext.CompileCallback2() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:166`, `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:237`
- `mStreamingContext.setImageGrabberCallback(new NvsStreamingContext.ImageGrabberCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:402`
- `mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:113`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:300`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1879`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:138`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:890` (+4 more)
- `mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:130`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:325`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1903`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:161`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:935` (+4 more)
- `mStreamingContext.setSeekingCallback(new NvsStreamingContext.SeekingCallback() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:355`
- `mThumbnailCutView.seekNvsMultiThumbnailSequenceView(EditorController.getInstance().durationToLength(mStartTrim, mThumbnailCutView.getPixelPerMicrosecond()));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:187`
- `mVideoFragment.setPlayFlag(NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:100`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:324`
- `new NvsRational(1, 1), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:492`
- `NvsLiveWindow liveWindow = (NvsLiveWindow) mLiveWindow;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:385`
- `NvsLiveWindowExt liveWindow = (NvsLiveWindowExt) mLiveWindow;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:388`
- `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1130`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:794`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1062`, `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:250`
- `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:310`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:231`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java:124`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:227`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:413` (+2 more)
- `NvsRational fps = fileInfo.getVideoStreamFrameRate(0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:1086`
- `NvsSize liveWindowSize = Util.getLiveWindowSize(TimelineUtil.getTimelineSize(mTimeline), new NvsSize(width, height), false);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:359`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:253`
- `NvsStreamingContext streamingContext = NvsStreamingContext.getInstance();`
  Sources: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:1075`
- `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:610`
- `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_ALIGN_VIDEO_SIZE`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:583`
- `NvsStreamingContext.COMPILE_BITRATE_GRADE_MEDIUM, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:628`
- `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:627`
- `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, compile_height);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:178`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:166`
- `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, encoderFlag`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:83`
- `NvsStreamingContext.CompileCallback compileCallback, NvsStreamingContext.CompileCallback2 compileCallback2) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:567`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:604`
- `NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeline, mTimeline.getDuration() / 1000000D / seekBar.getWidth());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:223`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:534`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2285`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:363`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:162`
- `NvsStreamingContext.getInstance().setTimelineScaleForSeek(timeline, timeline.getDuration() / 1000000D / v);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:88`
- `NvsStreamingContext.PlaybackCallback, NvsStreamingContext.PlaybackCallback2, View.OnClickListener {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:95`
- `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME |`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:437`
- `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME | NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_LOW_PIPELINE_SIZE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:587`
- `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:101`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:325`
- `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2099`
- `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:52`, `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:81`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:102`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:458`
- `NvsStreamingContextUtil.getInstance().seekTimeline(mTimeline, timestamp, seekShowMode);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:255`
- `NvsTimeline grabImageTimeline = getGrabImageTimeline();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:381`
- `NvsTimeline timeline,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:45`, `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:97`
- `NvsUtils.checkFunctionInMainThread();`
  Sources: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:280`, `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:286`, `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:292`, `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:299`, `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:313` (+11 more)
- `NvsVideoResolution videoRes = timeline.getVideoRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:101`
- `NvsVideoTrack videoTrack = grabImageTimeline.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:383`
- `path, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM,`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:582`
- `playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), mTimeline.getDuration(), NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag);`
  Sources: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:166`
- `playVideo(startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag);`
  Sources: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:179`
- `playView.updatePlaying(i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:641`
- `previewBean.setBitmap(mStreamingContext.grabImageFromTimeline(mTimeline, itemStartDuration + previewBean.getDuration() / 5, new NvsRational(1, 1)));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:469`
- `private int liveModel = NvsLiveWindow.HDR_DISPLAY_MODE_SDR;`
  Sources: `libBase/src/main/java/com/meishe/base/view/MSLiveWindow.java:31`
- `private int liveWindowModel = NvsLiveWindow.HDR_DISPLAY_MODE_SDR;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:97`
- `private MultiThumbnailSequenceView2 mNvsMultiThumbnailSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:33`
- `private NvsIconGenerator m_iconGenerator = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:60`
- `private NvsLiveWindow mLiveWindow;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:49`, `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:70`, `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:30`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:110`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:43` (+5 more)
- `private NvsLiveWindow mLivewindow;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:263`
- `private NvsLiveWindowExt mLiveWindow;`
  Sources: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:24`
- `private NvsMultiThumbnailSequenceView m_multiThumbnailSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:62`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:59`
- `private NvsMultiThumbnailSequenceView mMultiSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:63`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:90`
- `private NvsMultiThumbnailSequenceView mMultiThumbnailSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java:52`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:58`
- `private NvsMultiThumbnailSequenceView mSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:113`
- `private NvsMultiThumbnailSequenceView thumbnailView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:54`
- `private NvsStreamingContext m_streamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:14`
- `private NvsStreamingContext mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:37`
- `private NvsStreamingContext.CompileCallback mCompileCallback;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:71`
- `private NvsStreamingContext.CompileCallback2 mCompileCallback2;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:72`
- `private NvsStreamingContext.PlaybackCallback mPlaybackCallbackListener;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:68`
- `private NvsStreamingContext.PlaybackCallback2 mPlaybackCallback2Listener;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:69`
- `private NvsTimeline getGrabImageTimeline() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:486`
- `private NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:38`
- `private void seekTimeline(NvsTimeline timeline, long timestamp) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:992`
- `private void setLiveWindowSize(NvsVideoResolution videoResolution) {`
  Sources: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:90`
- `public Bitmap grabBitmapFromTimeline(long timestamp, NvsRational proxyScale) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:548`
- `public class LiveWindow extends NvsLiveWindow {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:12`, `app/src/main/java/com/meishe/sdkdemo/particle/LiveWindow.java:8`
- `public class MSLiveWindow extends NvsLiveWindow {`
  Sources: `libBase/src/main/java/com/meishe/base/view/MSLiveWindow.java:17`
- `public class MSLiveWindowExt extends NvsLiveWindowExt {`
  Sources: `libBase/src/main/java/com/meishe/base/view/MSLiveWindowExt.java:17`
- `public class SqView extends NvsMultiThumbnailSequenceView {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/SqView.java:21`
- `public class ThemeCaptureLiveWindow extends NvsLiveWindow {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCaptureLiveWindow.java:8`
- `public class ThemePreviewLiveWindow extends NvsLiveWindow {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemePreviewLiveWindow.java:8`
- `public NvsLiveWindow getLiveWindow() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2340`
- `public NvsMultiThumbnailSequenceView getMultiThumbnailSequenceView() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:478`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:456`
- `public PointF getLiveWindrowSize(NvsLiveWindowExt liveWindow) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:3019`
- `public static NvsSize getLiveWindowSize(NvsSize timelineSize, NvsSize parentSize, boolean fullScreen) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:773`
- `public static NvsVideoResolution getVideoEditResolutionByClip(String path, int compileRes) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2262`
- `public static void compileVideo(NvsStreamingContext context,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:44`, `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:96`
- `public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:78`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:425`, `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:228`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:606`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:421` (+3 more)
- `public void compileFailed(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:73`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:420`, `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:223`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:601`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:416` (+3 more)
- `public void compileFinished(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:68`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:415`, `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:218`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:596`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:411` (+3 more)
- `public void compileProgress(NvsTimeline timeline, int progress) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:64`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:411`, `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:213`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:591`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:406` (+3 more)
- `public void grabBitmapFromAuxiliaryTimelineAsync(long timestamp, NvsStreamingContext.ImageGrabberCallback callback) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:526`
- `public void grabImageFromTimelineAsync(long timestamp, NvsRational proxyScale, int flags, NvsStreamingContext.ImageGrabberCallback callback) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:493`
- `public void grabImageFromTimelineAsync(long timestamp, NvsStreamingContext.ImageGrabberCallback callback) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:469`
- `public void initData(long total_duration, ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/SqLayout.java:99`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleSqLayout.java:76`
- `public void initTimelineEditor(ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDesc, final long timelineDuration) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:143`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:135`
- `public void onCompileCompleted(NvsTimeline nvsTimeline, boolean cancel) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:280`
- `public void onCompileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:168`, `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:239`
- `public void onCompileFailed(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:123`, `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:228`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:273`, `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:219`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:129` (+1 more)
- `public void onCompileFinished(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:106`, `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:213`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:263`, `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:212`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:111` (+1 more)
- `public void onCompileProgress(NvsTimeline nvsTimeline, int i) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:101`, `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:208`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:258`, `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:207`, `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:106` (+1 more)
- `public void onPlaybackEOF(final NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:47`
- `public void onPlaybackEOF(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:124`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:573`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:314`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1893`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:151` (+6 more)
- `public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:39`, `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:115`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:563`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:302`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1881` (+7 more)
- `public void onPlaybackStopped(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:43`, `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:120`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:568`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:307`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1886` (+7 more)
- `public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:132`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1905`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:196`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:365`
- `public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long curPos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:578`
- `public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long currentPosition) {`
  Sources: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:136`
- `public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long l) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:327`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:163`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:937`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:232`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:667`
- `public void onScrollChanged(NvsMultiThumbnailSequenceView nvsMultiThumbnailSequenceView, int i, int i1) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:172`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:155`
- `public void onSeekingTimelinePosition(NvsTimeline nvsTimeline, long l) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:357`
- `public void playBackEOF(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:188`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:142`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:290`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:769`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:150` (+6 more)
- `public void playBackEOF(NvsTimeline timeline) {}`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:167`
- `public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:198`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:150`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:300`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:780`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:160` (+6 more)
- `public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {}`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:173`
- `public void playVideo(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:66`
- `public void seekNvsMultiThumbnailSequenceView(final int length) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:149`
- `public void seekTimeline(NvsTimeline mTimeline, long timestamp, int seekShowMode) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:41`
- `public void setImageGrabberCallback(NvsStreamingContext.ImageGrabberCallback callback) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:504`
- `public void setLiveWindowRatio(final NvsVideoResolution videoResolution) {`
  Sources: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:71`
- `public void setLiveWindrowSize(NvsLiveWindowExt liveWindow) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:3008`
- `public void setTimeline(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:69`
- `public void setTimelineScaleForSeek(NvsTimeline timeline, double v) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:87`
- `return grabBitmapFromTimeline(timestamp, new NvsRational(1, 1));`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:516`
- `return mNvsMultiThumbnailSequenceView.getPixelPerMicrosecond();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/view/CustomThumbnailCutView.java:179`
- `return mStreamingContext.grabImageFromTimeline(mNvsTimeline, timestamp, proxyScale, flag);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:553`
- `return state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:251`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:405`
- `seekShowMode | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2096`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2100`
- `seekTimeline(currentTimeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2273`
- `seekTimeline(i, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:156`
- `seekTimeline(mStreamingContext.getTimelineCurrentPosition(mNvsTimeline), 0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:296`
- `seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:200`
- `seekTimeline(progress * BASE_VALUE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:524`
- `seekTimeline(progress, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:217`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:356`
- `seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:189`
- `seekTimeline(timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag);`
  Sources: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:217`
- `this.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:77`
- `videoResolutionGrade, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, encoderFlag`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:89`
- `void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:64`
- `void compileFailed(NvsTimeline timeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:62`
- `void compileFinished(NvsTimeline timeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:60`
- `void compileProgress(NvsTimeline timeline, int progress);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:58`
- `void onSeekingTimelinePosition(NvsTimeline timeline, long position);`
  Sources: `libEngine/src/main/java/com/meishe/engine/interf/VideoFragmentListener.java:20`
- `void playBackEOF(NvsTimeline timeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:111`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:201`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:74`, `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:246`, `libEngine/src/main/java/com/meishe/engine/interf/VideoFragmentListener.java:12`
- `void playbackTimelinePosition(NvsTimeline timeline, long stamp);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:115`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:205`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:78`, `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:250`, `libEngine/src/main/java/com/meishe/engine/interf/VideoFragmentListener.java:16`
- `| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:84`, `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:90`
- `| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:85`, `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:91`
- `| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME)) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:585`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:611`
- `| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:584`
- `| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:86`
- `} else if (mLiveWindow instanceof NvsLiveWindowExt) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:387`
- `} else if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:391`

## template-mimo-cutsame

- `"com.meicam.sdkdemo.utils.permission.extra_permission";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/permission/PermissionsActivity.java:19`
- `&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1188`
- `@NonNull BaseViewHolder helper,MeicamNvsTemplateFootageCorrespondingClipInfo item) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/adapter/CutVideoAdapter.java:78`
- `ArrayList<NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo> correspondingClipInfos = footage.correspondingClipInfos;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TemplatePreviewActivity.java:348`
- `ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:325`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:217`
- `bitmap = mNvsIconGenerator.getIconFromCache(exportTemplateClip.getReversePath(), exportTemplateClip.getTrimIn(), 0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:470`
- `bitmap = mNvsIconGenerator.getIconFromCache(filePath, exportTemplateClip.getTrimIn(), 0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:472`
- `case NvsTimelineCaption.TEXT_ALIGNMENT_CENTER:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:513`
- `case NvsTimelineCaption.TEXT_ALIGNMENT_LEFT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:509`
- `case NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:518`
- `Collections.sort(mClipList, new Comparator<MeicamNvsTemplateFootageCorrespondingClipInfo>() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:783`
- `correspondingClipInfo.setNvsTemplateFootageCorrespondingClipInfo(clipInfo);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:769`
- `cutTimeline = EditorController.getInstance().getNvsTimeline();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:174`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:180`
- `EditorController.getInstance().connectTimelineWithLiveWindow(mNvsLiveWindow, mVideoFragmentListener);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:101`, `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:125`
- `EditorController.getInstance().getNvsTimeline().getDuration() / 1000000D / seekBar.getWidth());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:320`
- `EditorController.getInstance().grabImageFromTimelineAsync(0, new NvsRational(1, 1), 0, new NvsStreamingContext.ImageGrabberCallback() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:66`
- `EditorController.getInstance().playNow(mTrimIn, mNvsTimeline.getDuration());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:406`
- `EditorController.getInstance().seekTimeline(inPoint, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:274`
- `EditorController.getInstance().seekTimeline(nvsTimelineCaption.getInPoint(), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:268`
- `EditorController.getInstance().seekTimeline(nvTime, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:335`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:169`
- `EditorController.getInstance().setNvsTimeline(mBeforeTimeLine);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:152`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:583`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:589`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:622`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:675`
- `EditorController.getInstance().setNvsTimeline(mNvsTimeline);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:97`
- `EditorController.getInstance().setNvsTimeline(mTimeLine);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:80`
- `EditorController.getInstance().setNvsTimeline(nvsTimeline);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:74`
- `final NvsTimelineTimeSpan timelineTimeSpan = mTimelineEditor.addTimeSpan(inPoint, outPoint);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:264`
- `final NvsVideoClip videoClip = EditorController.getInstance().getVideoClipByTemplateFootageCorrespondingClipInfo(selectedClipInfo);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:308`
- `firstCaption.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_REPLACE_ID, String.valueOf(index));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:236`
- `for (int i = 0; i < meicamNvsTemplateFootageDescList.size(); i++) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:735`
- `for (List<MeicamNvsTemplateFootageCorrespondingClipInfo> templateClips : map.values()) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:808`
- `for (MeicamNvsTemplateFootageCorrespondingClipInfo info : correspondingClipInfos) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:772`
- `for (MeicamNvsTemplateFootageCorrespondingClipInfo templateClip : mClipList) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:798`
- `for (MeicamNvsTemplateFootageCorrespondingClipInfo templateClip : templateClips) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:812`
- `for (MeicamNvsTemplateFootageDesc footage : templateList) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:761`, `MCutSame/src/main/java/com/meishe/cutsame/TemplatePreviewActivity.java:344`
- `for (MeicamNvsTemplateFootageDesc nvsTemplateFootageDesc : meicamNvsTemplateFootageDescList) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:707`
- `for (NvsAssetPackageManager.NvsTemplateCaptionDesc desc : templateCaptionDescs) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:877`
- `for (NvsAssetPackageManager.NvsTemplateCaptionDesc nvsTemplateCaption : nvsTemplateCaptionDesc.subCaptions) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:199`
- `for (NvsAssetPackageManager.NvsTemplateCaptionDesc nvsTemplateCaptionDesc : nvsTemplateCaptionDescs) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:927`
- `for (NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc nvsTemplateCaptionDesc : nvsTemplateCaptionDescs) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:972`
- `for (NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc nvsTemplateCompoundCaptionDesc`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:176`
- `for (NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc nvsTemplateCompoundCaptionItemDesc`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:157`
- `for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo : correspondingClipInfos) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TemplatePreviewActivity.java:354`
- `for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo : footage.correspondingClipInfos) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:767`
- `for (NvsAssetPackageManager.NvsTemplateFootageDesc desc : nvsTemplateFootageDesc.timelineClipFootages) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:730`
- `for (NvsAssetPackageManager.NvsTemplateFootageDesc desc : nvsTemplateFootageDescList) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:701`
- `getAllNvsTemplateCaptionDescs(templateCaptionDescs, templateCaptionDesc);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:932`
- `getAllNvsTemplateCaptionDescs(templateCaptionDescs, timelineTemplateFootageDesc);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:947`
- `getAllNvsTemplateCaptionDescs(templateCompoundCaptionDescs, templateCaptionDesc);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:977`
- `getAllNvsTemplateFootageDescs(nvsTemplateFootageDescs, nvsTemplateFootageDesc);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:709`
- `getAllNvsTemplateFootageDescs(nvsTemplateFootageDescs, timelineTemplateFootageDesc);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:740`
- `hashtable.put(NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT, 1080);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:551`
- `if (avFileInfo != null && avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_IMAGE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:210`
- `if (capCategory == NvsTimelineCaption.THEME_CATEGORY`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1187`
- `if (error == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR || error == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java:1137`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java:1152`
- `if (errorCode == NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/SelectMediaActivity.java:449`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:264`
- `if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:129`
- `if (i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:267`
- `if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") != 0)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:224`
- `if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") == 0)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:153`
- `if (mCompileResolution == NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:119`
- `if (mNvsIconGenerator != null) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:601`
- `if (mNvsMultiThumbnailSequenceView != null) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:109`
- `if (mNvsMultiThumbnailSequenceView == null) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:167`
- `if (nvsVideoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV && nvsVideoClip.getTrimIn() > 0) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:358`
- `if (ratioType == NvsConstants.AspectRatio.AspectRatio_NoFitRatio) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:181`
- `if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:378`
- `if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED || state == NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:673`
- `if (type == NvsAVFileInfo.AV_FILE_TYPE_IMAGE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/adapter/BottomMenuViewHolder.java:96`
- `if (videoType == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:567`
- `if (videoType == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {//当前片段是图片 The current fragment is a picture`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:859`
- `int error = mStreamingContext.getAssetPackageManager().installAssetPackage(logoTemplatePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER, true, packageId);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:106`, `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:131`
- `int x = Math.round((stamp / (float) mNvsTimeline.getDuration() * mTimelineEditor.getSequenceWidth()));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:311`
- `layoutParams.leftMargin = EditorController.getInstance().durationToLength(position - startTime, mNvsMultiThumbnailSequenceView.getPixelPerMicrosecond());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:134`
- `List<MeicamNvsTemplateFootageCorrespondingClipInfo> correspondingClipInfos = new ArrayList<>();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:766`
- `List<MeicamNvsTemplateFootageCorrespondingClipInfo> lists = new ArrayList<>();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:84`
- `List<MeicamNvsTemplateFootageCorrespondingClipInfo> mClipList = new ArrayList<>();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:758`
- `List<MeicamNvsTemplateFootageCorrespondingClipInfo> templateVideoClip = mPresenter.getTemplateVideoClip(clipList);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:181`
- `List<MeicamNvsTemplateFootageCorrespondingClipInfo> tempList = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:797`
- `List<MeicamNvsTemplateFootageDesc> meicamNvsTemplateFootageDescList = new ArrayList<>();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:700`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:729`
- `List<MeicamNvsTemplateFootageDesc> nvsTemplateFootageDescs = new ArrayList<>();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:693`
- `List<MeicamNvsTemplateFootageDesc> templateList = EditorController.getInstance().getTemplateFootageDescVideo(mTemplateId.toString());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TemplatePreviewActivity.java:341`
- `List<MeicamNvsTemplateFootageDesc> templateList = getTemplateFootageDescVideo(uuidString);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:759`
- `List<NvsAssetPackageManager.NvsTemplateCaptionDesc> nvsTemplateCaptionDescs = mStreamingContext.getAssetPackageManager().getTemplateCaptions(uuidString);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:926`
- `List<NvsAssetPackageManager.NvsTemplateCaptionDesc> templateCaptionDescs = new ArrayList<>();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:870`
- `List<NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc> nvsTemplateCaptionDescs =`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:970`
- `List<NvsAssetPackageManager.NvsTemplateFootageDesc> nvsTemplateFootageDescList = mStreamingContext.getAssetPackageManager().getTemplateFootages(uuidString);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:699`
- `List<NvsAssetPackageManager.NvsTemplateFootageDesc> nvsTemplateFootageDescs = new ArrayList<>();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:676`
- `List<NvsStreamingContext.templateFootageInfo> footageInfoList = new ArrayList<>();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:410`
- `List<NvsTimelineAnimatedSticker> stickerList = mTimeline.getAnimatedStickersByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:663`
- `List<NvsTimelineCompoundCaption> captionList = mTimeline.getCompoundCaptionsByTimelinePosition(curPos);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:355`
- `List<NvsTimelineCompoundCaption> captionList = mTimeline.getCompoundCaptionsByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:753`
- `List<PointF> list = caption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:720`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:760`
- `List<PointF> subList = caption.getCaptionBoundingVertices(index, NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:728`
- `LogUtils.e("getPixelPerMicrosecond: mNvsMultiThumbnailSequenceView is null!");`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:168`
- `long bestSeekTime = Long.parseLong(firstCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_BEST_SEEK_TIME));`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1465`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1492`
- `long bestSeekTime = Long.parseLong(meicamCaptionClip.getTemplateAttachment(NvsObject.TEMPLATE_KEY_BEST_SEEK_TIME));`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1440`
- `long curPos = NvsStreamingContext.getInstance().getTimelineCurrentPosition(mNvsTimeline);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:323`
- `long duration = mNvsTimeline.getDuration();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:234`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:324`
- `m_multiThumbnailSequenceView = new NvsMultiThumbnailSequenceView(context);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:100`
- `m_multiThumbnailSequenceView.setOnScrollChangeListenser(new NvsMultiThumbnailSequenceView.OnScrollChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:149`
- `m_videoResolution = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:334`
- `Map<String, List<MeicamNvsTemplateFootageCorrespondingClipInfo>> map = new HashMap<>();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:795`
- `mCompileResolution = bundle.getInt(COMPILE_RESOLUTION, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:62`
- `mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_CENTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:510`
- `mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_LEFT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:519`
- `mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:514`
- `MeicamNvsTemplateFootageCorrespondingClipInfo clipInfo =`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:90`
- `MeicamNvsTemplateFootageCorrespondingClipInfo clipInfo = mVideoData.get(i);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:412`
- `MeicamNvsTemplateFootageCorrespondingClipInfo correspondingClipInfo = new MeicamNvsTemplateFootageCorrespondingClipInfo();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:768`
- `MeicamNvsTemplateFootageDesc meicamNvsTemplateFootageDesc = new MeicamNvsTemplateFootageDesc();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:702`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:731`
- `MeicamNvsTemplateFootageDesc nvsTemplateFootageDesc) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:723`
- `MeicamNvsTemplateFootageDesc timelineTemplateFootageDesc = meicamNvsTemplateFootageDescList.get(i);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:736`
- `meicamNvsTemplateFootageDesc.setNvsTemplateFootageDesc(desc);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:703`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:732`
- `meicamNvsTemplateFootageDescList.add(meicamNvsTemplateFootageDesc);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:704`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:733`
- `mFileConvertor.setMeidaFileConvertorCallback(new NvsMediaFileConvertor.MeidaFileConvertorCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/SelectMediaActivity.java:440`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:255`
- `mLiveWindow = (NvsLiveWindow) rootView.findViewById(R.id.liveWindow);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:111`
- `mLiveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:112`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:334`
- `mMediaFileConverter = new NvsMediaFileConvertor();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:220`
- `mMimoVideoFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:268`
- `mNvsIconGenerator = new NvsIconGenerator();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:382`
- `mNvsIconGenerator = null;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:604`
- `mNvsIconGenerator.cancelTask(0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:602`
- `mNvsIconGenerator.release();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:603`
- `mNvsIconGenerator.setIconCallback(this);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:383`
- `mNvsLiveWindow = mRootView.findViewById(R.id.fragment_base_live_window);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:84`
- `mNvsLiveWindow.setOnClickListener(new View.OnClickListener() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:86`
- `mNvsMultiThumbnailSequenceView = parentView.findViewById(R.id.tailor_view_sequence);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:60`
- `mNvsMultiThumbnailSequenceView.scrollBy(length, 0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:144`
- `mNvsMultiThumbnailSequenceView.setEndPadding(mCoverMargin);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:71`
- `mNvsMultiThumbnailSequenceView.setPixelPerMicrosecond(pixelPerMicrosecond);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:107`
- `mNvsMultiThumbnailSequenceView.setScrollListener(new MultiThumbnailSequenceView2.OnScrollListener() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:72`
- `mNvsMultiThumbnailSequenceView.setStartPadding(mCoverMargin);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:70`
- `mNvsMultiThumbnailSequenceView.setThumbnailImageFillMode(NvsMultiThumbnailSequenceView.THUMBNAIL_IMAGE_FILLMODE_ASPECTCROP);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:108`
- `mNvsMultiThumbnailSequenceView.setThumbnailSequenceDescArray(sequenceDescsArray);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:120`
- `mNvsStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:94`
- `mNvsTimeline = TimelineUtil.newTimeline(TimelineUtil.getVideoEditResolutionByClip(mVideoPath));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:96`
- `mParamsTable.put(NvsStreamingContext.COMPILE_FPS, new NvsRational(30, 1));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:114`
- `mParamsTable.put(NvsStreamingContext.COMPILE_USE_OPERATING_RATE,true);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:115`
- `mPlayerFragment.seekTimeline(0, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:218`
- `mPlayerFragment.seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:246`
- `mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java:53`
- `mStreamingContext.playbackTimeline(mTimeline, mStartTime, mStartTime + getDuration(), NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:369`
- `mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:365`
- `mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:373`
- `mStreamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:286`
- `mStreamingContext.setCompileCallback2(new NvsStreamingContext.CompileCallback2() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:312`
- `mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:230`
- `mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:246`
- `mStreamingContext.setSeekingCallback(new NvsStreamingContext.SeekingCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:255`
- `mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:264`
- `mTailorView.seekNvsMultiThumbnailSequenceView(EditorController.getInstance().durationToLength(mStartTrim, mTailorView.getPixelPerMicrosecond()));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:149`
- `mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.timeline_editor);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:107`
- `mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.timelineEditor);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:161`
- `mTimelineEditor.getMultiThumbnailSequenceView().setThumbnailImageFillMode(NvsMultiThumbnailSequenceView.THUMBNAIL_IMAGE_FILLMODE_ASPECTCROP);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:350`
- `mTimelineEditor.setOnScrollListener(new NvsTimelineEditor.OnScrollChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:174`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:173`
- `mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:263`
- `mTrimOut = mNvsTimeline.getDuration();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:152`
- `new MeicamNvsTemplateFootageCorrespondingClipInfo();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:91`
- `new NvsAssetPackageManager.AssetPackageManagerCallback() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TemplatePreviewActivity.java:335`
- `new NvsStreamingContext.CompileCallback() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:132`
- `new NvsStreamingContext.ImageGrabberCallback() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:118`
- `NvsAssetPackageManager manager = streamingContext.getAssetPackageManager();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java:639`
- `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo nvsTemplateFootageCorrespondingClipInfo = mVideoData.get(i);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:484`
- `NvsAudioClip audioClip = audioTrack.addClip(oneMusic.getFilePath(), oneMusic.getInPoint(), oneMusic.getTrimIn(), oneMusic.getTrimOut());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1069`
- `NvsAudioClip audioClip = audioTrack.addClip(recordAudioInfo.getPath(), recordAudioInfo.getInPoint(), recordAudioInfo.getTrimIn(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1127`
- `NvsAudioClip extra_clip = audioTrack.addClip(oneMusic.getFilePath(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1078`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1091`
- `NvsAudioClip nvsAudioClip = nvsAudioTrack.getClipByIndex(i);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:446`
- `nvsAudioClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_ID, "footage" + (FOOTAGE_ID_AUDIO_BASE_NUMBER++));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:457`
- `nvsAudioClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NAME, file.getName());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:453`
- `nvsAudioClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE, "false");`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:456`
- `nvsAudioClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TAGS, "音频");`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:458`
- `nvsAudioClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TYPE, "audio");`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:455`
- `NvsAudioResolution audioEditRes = new NvsAudioResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1390`
- `NvsAudioResolution nvsAudioResolution = new NvsAudioResolution();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutSameEditorPresenter.java:33`
- `NvsAudioTrack audioTrack = timeline.getAudioTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1049`
- `NvsAudioTrack audioTrack = timeline.getAudioTrackByIndex(1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1118`
- `NvsAudioTrack mainAudioTrack = timeline.getAudioTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:432`
- `NvsAudioTrack nvsAudioTrack = mTimeLine.getAudioTrackByIndex(m);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:443`
- `NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(videoClipPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:209`
- `NvsAVFileInfo avFileInfo = streamingContext.getAVFileInfo(nvsVideoClip.getFilePath());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:361`
- `NvsAVFileInfo avInfoFromFile = NvsStreamingContext.getAVInfoFromFile(videoFilePath, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/adapter/BottomMenuViewHolder.java:91`
- `NvsAVFileInfo nvsAvFileInfo = EditorController.getInstance().getFileInfo(mediaData.getPath());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/MaterialSelectActivity.java:420`
- `NvsColor outlineColor = ColorUtil.colorStringtoNvsColor(caption.getOutlineColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1330`
- `NvsColor shadowColor = new NvsColor(0, 0, 0, 0.5f);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1361`
- `NvsColor textColor = ColorUtil.colorStringtoNvsColor(caption.getCaptionColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1305`
- `NvsColor textColor = ColorUtil.colorStringtoNvsColor(captionAttr.getCaptionColor());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1252`
- `NvsMultiThumbnailSequenceView multiThumbnailSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpanExt.java:35`
- `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:331`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:224`
- `NvsRational videoFps = new NvsRational(30, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1388`
- `NvsServerClient.get().cancelAll();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:132`
- `NvsServerClient.get().cancelRequest(tag);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:142`
- `NvsServerClient.get().download(tag, url, filePath, fileName, listener);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:124`
- `NvsServerClient.get().requestGet(tag, apiName, params, callback);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:57`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:93`
- `NvsServerClient.get().requestGet(tag, CUT_SAME_TEMPLATE_CATEGORY, "", params, callback);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:71`
- `NvsServerClient.get().requestPost(tag, apiName, params, callback);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:110`
- `NvsStreamingContext context = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:127`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:487`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:512`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:765`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1380` (+1 more)
- `NvsStreamingContext instance = NvsStreamingContext.getInstance();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/TemplatePresenter.java:111`
- `NvsStreamingContext streamingContext = EditorController.getInstance().getStreamingContext();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:359`
- `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:680`
- `NvsStreamingContext.getInstance().registerFontByFilePath(fontPathLocal);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/TemplateFragment.java:163`
- `NvsStreamingContext.getInstance().setTimelineScaleForSeek(EditorController.getInstance().getNvsTimeline(),`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:319`
- `NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeLine, mTimeLine.getDuration() / 1000000D / seekBar.getWidth());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:153`
- `NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeline, mTimeline.getDuration() / 1000000D / seekBar.getWidth());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:161`
- `NvsStreamingContext.ImageGrabberCallback callback = this;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:119`
- `NvsStreamingContext.SdkVersion version = instance.getSdkVersion();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/TemplatePresenter.java:113`
- `NvsStreamingContext.templateFootageInfo footageInfo = new NvsStreamingContext.templateFootageInfo();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:412`
- `nvsTemplateCaptionDesc.getNvsCaption().setText(text);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:239`, `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:247`
- `nvsTemplateCaptionDesc.getNvsCompoundCaption().setText(nvsTemplateCaptionDesc.getCaptionIndex(), text);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:241`, `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:249`
- `NvsTimeline auxiliaryTimeline = createTimeline(EditorController.getInstance().createAuxiliaryStreamingContext());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:115`
- `NvsTimeline auxiliaryTimeline = EditorController.getInstance().getAuxiliaryTimeline();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:678`
- `NvsTimeline auxiliaryTimeline = mPresenter.createAuxiliaryTimeline(EditorController.getInstance().createAuxiliaryStreamingContext(), EditorController.getInstance().getVideoResolutionByRatio(ratio));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:139`
- `NvsTimeline currentTimeline = CutSameEditorActivity.cutTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:174`
- `NvsTimeline nvsTimeline = EditorController.getInstance().getNvsTimeline();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:312`, `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:340`
- `NvsTimeline nvsTimeline = TimelineUtil.newTimeline(TimelineUtil.getVideoEditResolutionByClip(mVideoPath));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:73`
- `NvsTimeline timeline = context.createTimeline(videoEditRes, videoFps, audioEditRes);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1394`
- `NvsTimeline timeline = EditorController.getInstance().createTimeline(context, mTemplateId, footageInfoList);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:418`
- `NvsTimeline timeline = MimoTimelineUtil.newTimeline(videoResolution);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:286`
- `NvsTimeline timeline = newTimeline(MimoCommonUtil.getVideoEditResolution(Constants.AspectRatio.AspectRatio_16v9));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:105`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:673`
- `NvsTimeline timeline = newTimeline(TimelineData.instance().getVideoResolution());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:75`
- `NvsTimeline timeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoActivity.java:240`
- `NvsTimelineAnimatedSticker animatedSticker = timeline.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:154`
- `NvsTimelineAnimatedSticker deleteSticker = timeline.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1147`
- `NvsTimelineAnimatedSticker newSticker = isCutsomSticker ?`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1155`
- `NvsTimelineAnimatedSticker sticker = mTimeline.getFirstAnimatedSticker();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:234`
- `NvsTimelineAnimatedSticker sticker = stickerList.get(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:668`
- `NvsTimelineCaption caption = EditorController.getInstance().getCaptionByAttachment(nvsTemplateCaptionDesc.replaceId);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:295`
- `NvsTimelineCaption caption = timeline.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:162`
- `NvsTimelineCaption deleteCaption = timeline.getFirstCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1180`
- `NvsTimelineCaption firstCaption = mTimeLine.getFirstCaption();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:232`
- `NvsTimelineCaption meicamCaptionClip = loadTimelineCaptionToTemplate(meicamTimeline, firstCaption, templateCaptionDesc.replaceId);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1438`
- `NvsTimelineCaption newCaption = timeline.addCaption(caption.getText(), caption.getInPoint(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1197`
- `NvsTimelineCaption nvsTimelineCaption = EditorController.getInstance().getCaptionByAttachment(nvsTemplateCaptionDesc.replaceId);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:229`, `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:263`
- `NvsTimelineCompoundCaption caption = captionList.get(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:759`
- `NvsTimelineCompoundCaption compoundCaption = timeline.getFirstCompoundCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:166`
- `NvsTimelineCompoundCaption deleteCaption = timeline.getFirstCompoundCaption();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1210`
- `NvsTimelineCompoundCaption newCaption = timeline.addCompoundCaption(caption.getInPoint(),`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1221`
- `NvsTimelineTimeSpan timelineTimeSpan = createTimeSpan(inPoint, outPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:201`
- `NvsTimelineTimeSpan timelineTimeSpan = m_timelineTimeSpanArray.get(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:334`
- `NvsTimelineTimeSpan timelineTimeSpan = new NvsTimelineTimeSpan(m_context);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:354`
- `NvsTimelineTimeSpan timeSpan = m_timelineTimeSpanArray.get(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:164`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:472`
- `NvsTimelineTimeSpanExt timeSpanExt = new NvsTimelineTimeSpanExt(m_context);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:228`
- `NvsTimelineVideoFx videoFx = timeline.getFirstTimelineVideoFx();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:158`
- `NvsVideoClip auxiliaryClip = videoTrackByIndex.getClipByIndex(replaceIndex);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:682`
- `NvsVideoClip clip = EditorController.getInstance().getVideoClipByIndex(selectedClipInfo.trackIndex, selectedClipInfo.clipIndex);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:179`, `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:204`
- `NvsVideoClip clip = EditorController.getInstance().getVideoClipByTemplateFootageCorrespondingClipInfo(selectedClipInfo);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:155`
- `NvsVideoClip clip = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:936`
- `NvsVideoClip clipByIndex = nvsVideoTrack.getClipByIndex(curIndex);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:596`
- `NvsVideoClip clipByIndex = nvsVideoTrack.getClipByIndex(replaceIndex);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:658`
- `NvsVideoClip clipFirst = videoTrackByIndex.getClipByIndex(0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:365`
- `NvsVideoClip clipLast = videoTrackByIndex.getClipByIndex(clipCount - 1);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:366`
- `NvsVideoClip nvsVideoClip = auxiliaryTrack.appendClip(templateClip.getFilePath());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:146`
- `NvsVideoClip nvsVideoClip = EditorController.getInstance().`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:451`
- `NvsVideoClip nvsVideoClip = EditorController.getInstance().getVideoClipByTemplateFootageCorrespondingClipInfo(`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:345`
- `NvsVideoClip nvsVideoClip = EditorController.getInstance().getVideoClipByTemplateFootageCorrespondingClipInfo(item);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/adapter/CutVideoAdapter.java:57`
- `NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(templateClip.getFilePath());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:132`
- `NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(i);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:604`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:669`
- `NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(j);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:437`, `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:316`
- `NvsVideoClip videoClip = (inPoint > 0)`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:558`
- `NvsVideoClip videoClip = videoTrack.appendClip(clipPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:810`
- `NvsVideoClip videoClip = videoTrack.appendClip(filePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:706`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:823`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:327`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:219`
- `NvsVideoClip videoClip = videoTrackByIndex.getClipByIndex(i);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:416`
- `NvsVideoFrameRetriever videoFrameRetriever = NvsStreamingContext.getInstance().createVideoFrameRetriever(videoFilePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/adapter/BaseRecyclerHolder.java:33`
- `NvsVideoFx nvsVideoFx = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:593`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:954`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:997`
- `NvsVideoFx secondVideoFx = firstClip.appendPackagedFx(mPiPTemplateAssetsArray.get(index).getTempatePackageID().get(0));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:911`
- `NvsVideoFx secondVideoFx = secondClip.appendPackagedFx(mPiPTemplateAssetsArray.get(index).getTempatePackageID().get(1));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:922`
- `NvsVideoFx sharpenVideoFx = videoClip.appendBuiltinFx(Constants.FX_SHARPEN);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:855`
- `NvsVideoFx videoFxColor = videoClip.appendBuiltinFx(Constants.FX_COLOR_PROPERTY);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:837`
- `NvsVideoFx videoFxTransform = videoClip.appendBuiltinFx(Constants.FX_TRANSFORM_2D);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:894`
- `NvsVideoFx vignetteVideoFx = videoClip.appendBuiltinFx(Constants.FX_VIGNETTE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:851`
- `NvsVideoResolution m_videoResolution;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:16`
- `NvsVideoResolution nvsVideoResolution = TimelineData.instance().getVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/ImageConverter.java:87`
- `NvsVideoResolution resolution = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:115`
- `NvsVideoResolution videoEditRes = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoCommonUtil.java:47`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoCommonUtil.java:78`
- `NvsVideoResolution videoEditRes = videoResolution;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1386`
- `NvsVideoResolution videoRes = EditorController.getInstance().getNvsTimeline().getVideoRes();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:134`
- `NvsVideoResolution videoResolution = TimelineData.instance().getVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:282`
- `nvsVideoResolution.imagePAR = new NvsRational(1, 1);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutSameEditorPresenter.java:32`
- `NvsVideoTrack auxiliaryTrack = auxiliaryTimeline.appendVideoTrack();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:140`
- `NvsVideoTrack mainVideoTrack = timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:184`
- `NvsVideoTrack meicamVideoTrack = meicamTimeline.getVideoTrackByIndex(templateCaptionDesc.trackIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1460`
- `NvsVideoTrack nvsVideoTrack = mBeforeTimeLine.appendVideoTrack();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:125`
- `NvsVideoTrack nvsVideoTrack = mBeforeTimeLine.getVideoTrackByIndex(0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:592`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:651`
- `NvsVideoTrack nvsVideoTrack = nvsTimeline.getVideoTrackByIndex(templateClip.getTrackIndex());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:313`
- `NvsVideoTrack nvsVideoTrack = timeLine.getVideoTrackByIndex(i);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:435`
- `NvsVideoTrack subVideoTrack = timeline.getVideoTrackByIndex(1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:272`
- `NvsVideoTrack subVideoTrack = timeline.getVideoTrackByIndex(trackIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:254`
- `NvsVideoTrack videoTrack = mNvsTimeline.getVideoTrackByIndex(0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:212`
- `NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:321`
- `NvsVideoTrack videoTrack = timeline.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:687`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:701`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:778`
- `NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:928`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:974`
- `NvsVideoTrack videoTrack = videoTrackCount == 0 ? timeline.appendVideoTrack() : timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:804`
- `NvsVideoTrack videoTrackByIndex = auxiliaryTimeline.getVideoTrackByIndex(0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:680`
- `NvsVideoTrack videoTrackByIndex = mBeforeTimeLine.getVideoTrackByIndex(0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:356`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:732`
- `NvsVideoTrack videoTrackByIndex = mTimeLine.getVideoTrackByIndex(m);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:412`
- `NvsVideoTransition videoTransition = videoTrack.getTransitionBySourceClipIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:479`
- `PackageManagerUtil.installAssetPackage(stickerTemplatePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1387`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1389`
- `parseNvsVideoClip(clipFirst, templateClipHead);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:373`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:384`
- `parseNvsVideoClip(clipLast, templateClipTail);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:374`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:390`
- `parseNvsVideoClip(nvsVideoClip, templateClip);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:133`, `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:147`
- `PointF pointF = mNvsLiveWindow.mapCanonicalToView(list.get(i));`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:303`
- `private ArrayList<NvsTimelineTimeSpan> m_timelineTimeSpanArray;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:51`
- `private boolean needDealFootageDesc(NvsAssetPackageManager.NvsTemplateFootageDesc nvsTemplateFootageDesc) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:857`
- `private int mVideoResolution = NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:47`
- `private List<MeicamNvsTemplateFootageCorrespondingClipInfo> mVideoData = new ArrayList<>();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:63`
- `private MeicamNvsTemplateFootageCorrespondingClipInfo selectedClipInfo;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:69`
- `private MultiThumbnailSequenceView2 mNvsMultiThumbnailSequenceView;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:31`
- `private NvsAssetPackageManager packageManager;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java:117`
- `private NvsCaption nvsCaption;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:32`
- `private NvsCompoundCaption nvsCompoundCaption;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:33`
- `private NvsIconGenerator mNvsIconGenerator;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:63`
- `private NvsLiveWindow mLiveWindow;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:45`
- `private NvsLiveWindow mNvsLiveWindow;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:37`
- `private NvsMediaFileConvertor mFileConvertor = new NvsMediaFileConvertor();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/SelectMediaActivity.java:90`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:62`
- `private NvsMediaFileConvertor mMediaFileConverter;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:175`
- `private NvsMultiThumbnailSequenceView m_multiThumbnailSequenceView;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:57`
- `private NvsMultiThumbnailSequenceView mMultiThumbnailSequenceView;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:68`
- `private NvsStreamingContext mNvsStreamingContext;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:75`
- `private NvsStreamingContext mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:47`
- `private NvsStreamingContext mStreamingContext;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:101`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:68`
- `private NvsStreamingContext streamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java:109`
- `private NvsTimeline createTimeline(NvsStreamingContext context) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:409`
- `private NvsTimeline mBeforeTimeLine;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:82`
- `private NvsTimeline mNvsTimeline;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:69`
- `private NvsTimeline mTimeLine;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:99`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:58`
- `private NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:46`
- `private NvsTimelineAnimatedSticker mCurAnimateSticker;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:74`
- `private NvsTimelineCaption mCurCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:70`
- `private NvsTimelineCompoundCaption mAddComCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:71`
- `private NvsTimelineCompoundCaption mCurCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:70`
- `private NvsTimelineCompoundCaption mCurCompoundCaption;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:73`
- `private NvsTimelineEditor mTimelineEditor;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:48`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:67`
- `private NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:258`
- `private NvsTimelineTimeSpan createTimeSpan(long inPoint, long outPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:349`
- `private static final int DEFAULT_COMPILE_RESOLUTION = NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:71`
- `private static long appendVideoClip(NvsVideoTrack videoTrack,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:536`
- `private static NvsTimelineCaption loadTimelineCaptionToTemplate(NvsTimeline timeline, NvsTimelineCaption caption, String replaceId) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1242`
- `private static void addCompoundCaption(NvsTimeline timeline,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:381`
- `private static void addShotVideo(NvsTimeline timeline, MiMoLocalData selectTemplate) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:179`
- `private static void addSubTrackClip(NvsVideoTrack videoTrack, ShotVideoInfo shotVideoInfo, long inPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:292`
- `private static void addTimeLineFilter(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:747`
- `private static void addTimelineFilter(NvsTimeline timeline,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:398`
- `private static void addTimeWaterMark(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:754`
- `private static void addVideoClip(NvsVideoTrack videoTrack, ClipInfo clipInfo, boolean isTrimClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:818`
- `private static void appendAudioClip(NvsTimeline timeline, MiMoLocalData selectTemplate) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:420`
- `private static void appendFilter(NvsVideoClip videoClip, String filterName) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:585`
- `private static void appendTimelineFilter(NvsTimeline timeline, long inPoint, String filter) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:279`
- `private static void changeSpeed(NvsVideoClip videoClip, TrackClipInfo trackClipInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:608`
- `private static void loadTimelineCaptionToTemplate(NvsTimeline timeline, NvsTimelineCaption caption, List<ClipInfo<?>> clipInfoList) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:910`
- `private static void removeAllTimelineAsset(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:150`
- `private static void removeAudioTrack(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:653`
- `private static void removeVideoTrack(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:640`
- `private static void setTimelineData(NvsTimeline timeline, MiMoLocalData selectTemplate) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:340`
- `private static void setTrackTransition(NvsVideoTrack videoTrack, List<TrackClipInfo> trackClipInfos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:443`
- `private static void updateCaptionAttribute(NvsTimelineCaption newCaption, CaptionInfo caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1282`
- `private static void updateCompoundCaptionAttribute(NvsTimelineCompoundCaption newCaption, CompoundCaptionInfo caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1237`
- `private String m_timeSpanType = "NvsTimelineTimeSpan";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:79`
- `private String TAG = "NvsTimelineEditor";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:25`
- `private String TAG = "NvsTimelineTimeSpan";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpan.java:20`
- `private String TAG = "NvsTimelineTimeSpanExt";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpanExt.java:18`
- `private void changeVideoClipPath(NvsTimeline timeLine) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:433`
- `private void deleteAddedHeadAndTail(NvsTimeline mBeforeTimeLine, List<TemplateClip> mTemplateClips) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:725`
- `private void getAllNvsTemplateCaptionDescs(List<TemplateCaptionDesc> templateCaptionDescs,`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:937`
- `private void getAllNvsTemplateFootageDescs(List<MeicamNvsTemplateFootageDesc> nvsTemplateFootageDescs,`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:722`
- `private void getCurCaption(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:383`
- `private void parseNvsVideoClip(NvsVideoClip nvsVideoClip, TemplateClip templateClip) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:398`
- `private void parseVideoClip(TemplateClip templateClip, NvsVideoClip nvsVideoClip) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:743`
- `private void setBackGroundImage(ImageView imageView, MeicamNvsTemplateFootageCorrespondingClipInfo item) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/adapter/CutVideoAdapter.java:56`
- `private void showVideoEditPop(View view, final NvsVideoClip videoClip) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:343`
- `private void updateTimeSpanShadow(NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:430`
- `protected abstract NvsTimeline initTimeLine();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/base/BaseEditActivity.java:24`
- `protected NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java:24`
- `protected NvsTimeline initTimeLine() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:281`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:365`
- `protected NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/base/BaseEditActivity.java:13`
- `public boolean hasTemplateCaptions(NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1081`
- `public class ClipSettingFragment extends BaseFragment implements View.OnClickListener, NvsIconGenerator.IconCallback {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:51`
- `public class CutVideoAdapter extends BaseQuickAdapter<MeicamNvsTemplateFootageCorrespondingClipInfo, BaseViewHolder> {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/adapter/CutVideoAdapter.java:27`
- `public class MeicamNvsTemplateFootageCorrespondingClipInfo extends NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageCorrespondingClipInfo.java:16`
- `public class MeicamNvsTemplateFootageDesc extends NvsAssetPackageManager.NvsTemplateFootageDesc {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageDesc.java:16`
- `public class NvAssetManager implements NvHttpRequest.NvHttpRequestListener, NvsAssetPackageManager.AssetPackageManagerCallback {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java:37`
- `public class NvsTimelineEditor extends RelativeLayout {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:24`
- `public class NvsTimelineTimeSpan extends RelativeLayout {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpan.java:19`
- `public class NvsTimelineTimeSpanExt extends RelativeLayout {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpanExt.java:17`
- `public class TemplateCaptionDesc extends NvsAssetPackageManager.NvsTemplateCaptionDesc implements Comparable<TemplateCaptionDesc> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:21`
- `public int compare(MeicamNvsTemplateFootageCorrespondingClipInfo o1, MeicamNvsTemplateFootageCorrespondingClipInfo o2) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:785`
- `public int rotation = NvsVideoStreamInfo.VIDEO_ROTATION_0;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/ClipInfo.java:12`
- `public List<MeicamNvsTemplateFootageCorrespondingClipInfo> getTemplateVideoClip(List<TemplateClip> clipList) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:83`
- `public List<MeicamNvsTemplateFootageCorrespondingClipInfo> getTemplateVideoClip(String uuidString) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:757`
- `public List<MeicamNvsTemplateFootageDesc> getTemplateFootageDescVideo(String uuidString) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:692`
- `public List<NvsAssetPackageManager.NvsTemplateFootageDesc> getTemplateFootageDesc(String uuidString) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:675`
- `public List<PointF> getCaptionPointList(NvsAssetPackageManager.NvsTemplateCaptionDesc nvsTemplateCaptionDesc) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:291`
- `public List<TemplateCaptionDesc> getTemplateCaptions(NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:990`
- `public NvsCaption getCaptionByTemplateCaptionDesc(TemplateCaptionDesc templateCaptionDesc) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1420`
- `public NvsCaption getNvsCaption() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:85`
- `public NvsCompoundCaption getNvsCompoundCaption() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:93`
- `public NvsMultiThumbnailSequenceView getMultiThumbnailSequenceView() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:403`
- `public NvsStreamingContext getStreamingContext() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java:49`
- `public NvsTimeline createAuxiliaryTimeline(NvsStreamingContext context, NvsVideoResolution nvsVideoResolution) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutSameEditorPresenter.java:28`
- `public NvsTimeline createTimeline(NvsStreamingContext context, String templateId, List<NvsStreamingContext.templateFootageInfo> templateFootAges) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1145`
- `public NvsTimeline createTimeline(String templateId, List<NvsStreamingContext.templateFootageInfo> templateFootAges) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1128`
- `public NvsTimeline getTimeLine() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:823`
- `public NvsTimelineAnimatedSticker getCurAnimateSticker() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:624`
- `public NvsTimelineCaption getCurCaption() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:702`
- `public NvsTimelineCompoundCaption getCurrCompoundCaption() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:710`
- `public NvsTimelineEditor(Context context, AttributeSet attrs) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:94`
- `public NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:200`
- `public NvsTimelineTimeSpan(Context context) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpan.java:73`
- `public NvsTimelineTimeSpanExt addTimeSpanExt(long inPoint, long outPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:221`
- `public NvsTimelineTimeSpanExt(Context context){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpanExt.java:55`
- `public NvsVideoClip getVideoClipByTemplateFootageCorrespondingClipInfo`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1255`
- `public NvsVideoClip getVideoClipByTemplateFootageCorrespondingClipInfo(MeicamNvsTemplateFootageCorrespondingClipInfo item) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1181`
- `public NvsVideoResolution cloneVideoResolution() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:111`
- `public NvsVideoResolution getVideoResolution() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:107`
- `public static boolean applyTheme(NvsTimeline timeline, String themeId) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1010`
- `public static boolean buildClipFilter(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:923`
- `public static boolean buildClipTrans(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:969`
- `public static boolean buildSingleClipVideoTrack(NvsTimeline timeline, ClipInfo clipInfo, boolean isTrimClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:682`
- `public static boolean buildSingleClipVideoTrackExt(NvsTimeline timeline, String filePath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:696`
- `public static boolean buildTimelineMusic(NvsTimeline timeline, List<MusicInfo> musicInfos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1045`
- `public static boolean buildVideoTrack(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:773`
- `public static boolean removeTimeline(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:760`
- `public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1175`
- `public static boolean setCompoundCaption(NvsTimeline timeline, ArrayList<CompoundCaptionInfo> captionArray) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1205`
- `public static boolean setSticker(NvsTimeline timeline, ArrayList<StickerInfo> stickerArray) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1142`
- `public static CompoundCaptionInfo saveCompoundCaptionData(NvsTimelineCompoundCaption caption, CompoundCaptionInfo compoundCaptionInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/CaptionUtil.java:16`
- `public static NvsTimeline createSingleClipTimeline(ClipInfo clipInfo, boolean isTrimClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:672`
- `public static NvsTimeline createTimeline() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:69`
- `public static NvsTimeline createTimeline(String clipPath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:104`
- `public static NvsTimeline cutTimeline;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:85`
- `public static NvsTimeline newTimeline(NvsVideoResolution videoResolution) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1379`
- `public static NvsTimeline reBuildSingleVideoTrack(NvsTimeline timeline, String clipPath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:799`
- `public static NvsVideoResolution getVideoEditResolution(int ratio) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoCommonUtil.java:45`
- `public static NvsVideoResolution getVideoEditResolutionEx(int ratio) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoCommonUtil.java:76`
- `public static TemplateCaptionDesc create(NvsAssetPackageManager.NvsTemplateCaptionDesc nvsTemplateCaptionDesc) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:191`
- `public static TemplateCaptionDesc create(NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc nvsTemplateCaptionDesc) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:152`
- `public static TemplateCompoundCaptionItemDesc create(NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc nvsTemplateCompoundCaptionItemDesc) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:316`
- `public static void buildTimelineRecordAudio(NvsTimeline timeline, ArrayList<RecordAudioInfo> recordAudioInfos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1114`
- `public static void loadTimelineToTemplate(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:888`
- `public static void rebuildTimelineByTemplate(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:122`
- `public static void setTimelineData(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:714`
- `public void changClipTrim(long newTrim, MeicamNvsTemplateFootageCorrespondingClipInfo selectedClipInfo) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:151`
- `public void changClipTrimIn(long newTrim, NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo selectedClipInfo) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:175`
- `public void changClipTrimOut(long newTrim, NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo selectedClipInfo) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:200`
- `public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:318`
- `public void compileFailed(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:313`
- `public void compileFinished(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:308`
- `public void compileProgress(NvsTimeline timeline, int progress) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:304`
- `public void copy(MeicamNvsTemplateFootageDesc nvsTemplateFootageDesc) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageDesc.java:54`
- `public void deleteSelectedTimeSpan(NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:411`
- `public void getVideoData(List<MeicamNvsTemplateFootageCorrespondingClipInfo> templateClipList) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:298`
- `public void initTimelineEditor(ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDesc, final long timelineDuration, final long trimInPoint) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:134`
- `public void onCompileCompleted(NvsTimeline nvsTimeline, boolean b) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:149`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:314`
- `public void onCompileFailed(NvsTimeline nvsTimeline) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:144`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:307`
- `public void onCompileFinished(NvsTimeline nvsTimeline) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:139`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:295`
- `public void onCompileProgress(NvsTimeline nvsTimeline, int i) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:134`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:288`
- `public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:275`
- `public void onPlaybackEOF(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:241`
- `public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:232`
- `public void onPlaybackStopped(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:237`
- `public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:248`
- `public void onScrollChanged(NvsMultiThumbnailSequenceView nvsMultiThumbnailSequenceView, int i, int i1) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:152`
- `public void onSeekingTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:257`
- `public void onSeekingTimelinePosition(NvsTimeline timeline, long position) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:515`, `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:200`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:387`
- `public void playBackEOF(NvsTimeline timeline) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:474`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:214`, `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:166`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:331`
- `public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:490`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:229`, `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:181`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:349`
- `public void playStopped(NvsTimeline timeline) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:483`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:224`, `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:174`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:342`
- `public void seekNvsMultiThumbnailSequenceView(final int length) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:143`
- `public void selectTimeSpan(NvsTimelineTimeSpan timeSpan) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:392`
- `public void setCurAnimateSticker(NvsTimelineAnimatedSticker animateSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:615`
- `public void setCurCaption(NvsTimelineCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:698`
- `public void setCurCompoundCaption(NvsTimelineCompoundCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:706`
- `public void setMultiThumbnailSequenceView(NvsMultiThumbnailSequenceView thumbnailSequenceView) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpanExt.java:208`
- `public void setNvsCaption(NvsCaption nvsCaption) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:81`
- `public void setNvsCompoundCaption(NvsCompoundCaption nvsCompoundCaption) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:89`
- `public void setNvsTemplateFootageCorrespondingClipInfo(NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo correspondingClipInfo) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageCorrespondingClipInfo.java:77`
- `public void setNvsTemplateFootageDesc(NvsAssetPackageManager.NvsTemplateFootageDesc desc) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageDesc.java:44`
- `public void setTimeLine(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:348`
- `public void setVideoResolution(NvsVideoResolution resolution) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:103`
- `public void updateAnimateStickerCoordinate(NvsTimelineAnimatedSticker animateSticker) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:630`
- `public void updateCaptionCoordinate(NvsTimelineCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:602`
- `public void updateCompoundCaptionCoordinate(NvsTimelineCompoundCaption caption) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:716`
- `return context.createTimeline(nvsVideoResolution, new NvsRational(25, 1), nvsAudioResolution);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutSameEditorPresenter.java:36`
- `return getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:285`
- `return loadTimelineCaptionToTemplate(mNvsTimeline, nextCaption, replaceId);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1239`
- `return mNvsMultiThumbnailSequenceView.getPixelPerMicrosecond();`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/TailorView.java:171`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:164`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:174`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:176`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:162`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:168`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:172`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:178`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:158`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:180`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:160`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:170`
- `return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:166`
- `return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:183`
- `return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_2160;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:186`
- `return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:174`
- `return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:177`
- `return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720;`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:170`, `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:180`, `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:189`
- `return nvsTemplateFootageDesc.type != NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_AUDIO;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:858`
- `seekTimeline(currentTime, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:154`
- `seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:422`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:466`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:539`
- `seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:415`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:430`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:457`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:482`, `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:523`
- `streamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java:197`
- `String bestSeekTime = videoClip.getTemplateAttachment(NvsObject.TEMPLATE_KEY_BEST_SEEK_TIME);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1208`
- `String groupID = firstCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_FX_GROUP);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1473`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1500`
- `String groupID = meicamCaptionClip.getTemplateAttachment(NvsObject.TEMPLATE_KEY_FX_GROUP);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1452`
- `String id = caption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1244`
- `String id = firstCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1463`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1490`
- `String keyword = meicamVideoFx.getStringVal(NvsConstants.POST_PACKAGE_ID);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/util/ExportTemplateUtil.java:229`
- `String packageId = PackageManagerUtil.installAssetPackage(stickerTemplatePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/SingleClickActivity.java:450`
- `synchronized (NvsStreamingContext.class) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java:51`
- `taskId = mNvsIconGenerator.getIcon(exportTemplateClip.getReversePath(), exportTemplateClip.getTrimIn(), 0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:477`
- `taskId = mNvsIconGenerator.getIcon(filePath, exportTemplateClip.getTrimIn(), 0);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/ClipSettingFragment.java:479`
- `templateCaptionDesc.setNvsCaption(clipCaption);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1043`
- `templateCaptionDesc.setNvsCaption(firstCaption);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1003`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1472`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1499`
- `templateCaptionDesc.setNvsCaption(meicamCaptionClip);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1447`
- `templateCaptionDesc.setNvsCompoundCaption(clipCompoundCaption);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1058`
- `templateCaptionDesc.setNvsCompoundCaption(firstCompoundCaption);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1018`
- `templateCaptionDescList = EditorController.getInstance().getTemplateCaptions(EditorController.getInstance().getNvsTimeline());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:75`
- `timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:269`
- `timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimOutChangeListener() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:280`
- `TimelineUtil.fillTrack(EditorController.getInstance().getNvsTimeline(), videoTrackList);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:91`, `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:114`
- `TimelineUtil.loadTimelineToTemplate(EditorController.getInstance().getNvsTimeline());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:623`
- `timeSpanExt.setMarginChangeListener(new NvsTimelineTimeSpanExt.OnMarginChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:268`
- `videoClip.setImageMotionMode(NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:877`
- `videoClip.setImageMotionMode(NvsVideoClip.IMAGE_CLIP_MOTIONMMODE_ROI);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:870`
- `videoClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE, meicamVideoClip.getVideoReverse() + "");`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:438`
- `videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE, exportTemplateClip.isLock() ? "false" : "true");`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:435`
- `videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID, "footage" + (exportTemplateClip.getFootageGroupsId() == 0 ?`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:432`
- `videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME, file.getName());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:429`
- `videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE, exportTemplateClip.getFootageType());`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:434`
- `videoEditRes.imagePAR = new NvsRational(1, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1387`
- `void getVideoData(List<MeicamNvsTemplateFootageCorrespondingClipInfo> templateClipList);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/iview/CutEditorVpView.java:24`
- `| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME)) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:681`
- `| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:219`, `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:247`
- `} else if (mCompileResolution == NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:125`
- `} else if (mCompileResolution == NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:121`
- `} else if (mCompileResolution == NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720) {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:123`
- `} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_16v9) { // 16:9`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:189`
- `} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_1v1) { //1:1`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:192`
- `} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_3v4) { // 3:4`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:202`
- `} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_4v3) { //4:3`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:205`
- `} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_9v16) { //9:16`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:199`
- `}, new NvsStreamingContext.CompileCallback2() {`
  Sources: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:147`

## timeline-editing

- `(NvsTimeline meicamTimeline, List<Integer> clipList, List<Integer> trackList, int trackIndex, int clipIndex) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1256`
- `ArrayList<NvsVideoClip> afterClipArray = getClipRange(afterPoint, afterduration, videoTrack);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1743`
- `ArrayList<NvsVideoClip> clipArray = getClipRange(point, repeatDuration, videoTrack);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1799`
- `ArrayList<NvsVideoClip> clipArray = getClipRange(point, TIME_BASE, videoTrack);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1737`
- `ArrayList<NvsVideoClip> clipArray = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1951`
- `ArrayList<NvsVideoClip> preClipArray = getClipRange(prePoint, preduration, videoTrack);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1742`
- `boolean hasThemeTitle = (afterThemeFirstClip.getRoleInTheme() == NvsVideoClip.ROLE_IN_THEME_TITLE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:234`
- `boolean hasThemeTrailer = (afterThemeLastClip.getRoleInTheme() == NvsVideoClip.ROLE_IN_THEME_TRAILER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:236`
- `case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:373`
- `case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:379`
- `case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:382`
- `case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90:`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:376`
- `end = mNvsTimeline.getDuration();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:251`
- `if ((mStreamingContext == null) || (mNvsTimeline == null)) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:190`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:204`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:218`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:231`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:246`
- `if (clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) { // 图片`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:205`
- `if (isLeftHand && videoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:829`
- `if (map.get(NvsConstants.POST_PACKAGE_ID) == null) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:876`
- `if (mNvsTimeline == null) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:415`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:831`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1163`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1234`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1292` (+1 more)
- `if (videoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV && isLeftHand) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:781`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:806`
- `if (videoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:774`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:917`
- `if (videoType == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:470`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:580`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:614`
- `if(oldVideoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE){`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:134`
- `int trackCount = mNvsTimeline.videoTrackCount();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1167`
- `List<NvsPosition2D> positions = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2700`
- `List<NvsTimeline> allTimeline = new ArrayList<>();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1424`
- `localData.setNvsRational(mNvsRational);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:386`
- `Log.e(TAG, "changeVideoSize: mNvsTimeline is null!");`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1293`
- `Log.e(TAG, "getTimelineDuration: mNvsTimeline is null!");`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:416`
- `Log.e(TAG, "getTimelineWidthAndHeight: mNvsTimeline is null!");`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1307`
- `Log.e(TAG, "getVideoClipByIndex: mNvsTimeline is null!");`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1164`
- `Log.e(TAG, "nowTime: mStreamingContext or mNvsTimeline is null!");`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:232`
- `Log.e(TAG, "playNow: mStreamingContext or mNvsTimeline is null!");`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:191`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:205`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:219`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:247`
- `LogUtils.e("NvsVideoTrack is null");`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:278`
- `m_videoResolution = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:367`
- `map.put(NvsConstants.IS_POST_STORY_BOARD_3D, paramTen);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:882`
- `map.put(NvsConstants.POST_PACKAGE_ID, paramNine);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:881`
- `map.remove(NvsConstants.POST_PACKAGE_ID_OLD);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:895`
- `meicamTimeline = getNvsTimeline();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1188`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1259`
- `mHasThemeTitle = (theFirstClip.getRoleInTheme() == NvsVideoClip.ROLE_IN_THEME_TITLE);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:322`
- `mHasThemeTrailer = (theLastClip.getRoleInTheme() == NvsVideoClip.ROLE_IN_THEME_TRAILER);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:323`
- `mNvsRational = nvsRational;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:345`, `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:266`
- `mNvsTimeline = nvsTimeline;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:122`
- `mNvsTimeline.changeVideoSize(width, height);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1296`
- `mSelectNvsVideoClip = nvsVideoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:550`
- `mStreamingContext = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:73`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/DurationActivity.java:41`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:91`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:258`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java:67` (+2 more)
- `mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:335`
- `mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.timelineEditor);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:117`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:80`, `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:74`
- `mTimelineEditor = (NvsTimelineEditor)findViewById(R.id.timelineEditor);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:77`
- `mTimelineEditor.setOnScrollListener(new NvsTimelineEditor.OnScrollChangeListener() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:177`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:310`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:178`
- `mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:383`
- `mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:377`
- `mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:380`
- `mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:374`
- `NvsControlPointPair nextPoint = new NvsControlPointPair(forwardPoint, backPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:692`
- `NvsControlPointPair prePoint = new NvsControlPointPair(forwardPoint, backPoint);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:685`
- `NvsPointD backPoint = new NvsPointD(keyTime, value.getVolumeValue());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:684`
- `NvsPointD backPoint = new NvsPointD(value.getNextControlPoint(), value.getNextVolumeValue());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:691`
- `NvsPointD forwardPoint = new NvsPointD(keyTime, value.getVolumeValue());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:690`
- `NvsPointD forwardPoint = new NvsPointD(value.getPreControlPoint(), value.getPreVolumeValue());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:683`
- `NvsRational videoFps = new NvsRational(30, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1855`
- `NvsRational videoFps = oldTimeline.getVideoFps();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:43`
- `NvsSize nvsSize = avInfoFromFile.getVideoStreamDimension(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2552`
- `NvsSize size = new NvsSize(0, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1867`
- `NvsSize size = new NvsSize(timelineSize.width, timelineSize.height);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:777`
- `NvsStreamingContext context = NvsStreamingContext.getInstance();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:326`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1842`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:522`
- `NvsStreamingContextUtil.getInstance().start(mTimeline, startTime, endTime);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:243`
- `NvsStreamingContextUtil.getInstance().startNow(mTimeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:194`, `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:238`
- `NvsTimeline getCurrentTimeline();`
  Sources: `libEngine/src/main/java/com/meishe/engine/interf/EditOperater.java:18`
- `NvsTimeline meicamTimeline = getNvsTimeline();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1422`
- `NvsTimeline meicamTimeline = mNvsTimeline;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1186`
- `NvsTimeline timeline = newTimeline(TimelineData.getInstance().getVideoResolution());`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:67`
- `NvsTimeline timeline = newTimeline(TimelineData.instance().getVideoResolution());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:179`
- `NvsTimeline timeline = newTimeline(videoEditRes);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:193`
- `NvsTimeline timeline = newTimeline(videoResolution);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:152`
- `NvsVideoClip afterThemeFirstClip = mVidoeTrack.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:233`
- `NvsVideoClip afterThemeLastClip = mVidoeTrack.getClipByIndex(afterThemeClipsCount - 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:235`
- `NvsVideoClip clip = mTimeline.getVideoTrackByIndex(0).getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:204`
- `NvsVideoClip clip = mVideoTrack.appendClip(mPath.get(i));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1137`
- `NvsVideoClip clip = mVideoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1126`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1058`, `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:246`
- `NvsVideoClip clip = videoTrack.appendClip(strPhoto);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:394`
- `NvsVideoClip clip = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1929`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1942`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:791`, `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:423`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:306` (+2 more)
- `NvsVideoClip clip = videoTrack.getClipByIndex(index);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1191`
- `NvsVideoClip clip = videoTrack.getClipByTimelinePosition(ptIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1954`
- `NvsVideoClip clip = videoTrack.insertClip(orgFilePath, trimIn, trimOut, clipIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1872`
- `NvsVideoClip clip =videoTrack .getClipByIndex(position);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationClipAdapter.java:114`
- `NvsVideoClip clipByIndex = videoTrackByIndex.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:425`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:655`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:254`
- `NvsVideoClip clipByIndex = videoTrackByIndex.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2382`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1033`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1101`
- `NvsVideoClip editVideoClip = clipInfo.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:306`
- `NvsVideoClip editVideoClip = meicamVideoClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2264`
- `NvsVideoClip firClip = mVideoTrackFir.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:725`
- `NvsVideoClip firstClip = mVideoTrackFir.getClipByIndex(firstIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:908`
- `NvsVideoClip firstTrackClip = mVideoTrackFir.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:686`
- `NvsVideoClip lastClip = clipArray.get(clipArray.size() - 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1819`
- `NvsVideoClip meicamVideoClip = null;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1421`
- `NvsVideoClip meicamVideoClip;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1185`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1257`
- `NvsVideoClip mVideoClip = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2249`
- `NvsVideoClip newVideoClip = newVideoTrack.addClip(oldVideoClip.getFilePath(),oldVideoClip.getInPoint(),oldVideoClip.getTrimIn(),oldVideoClip.getTrimOut());`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:117`
- `NvsVideoClip nextClip = videoTrack.getClipByIndex(index + 1);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1199`
- `NvsVideoClip nvsVideoClip = (NvsVideoClip) infoPip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1217`
- `NvsVideoClip nvsVideoClip = clip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:841`
- `NvsVideoClip nvsVideoClip = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:783`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:799`
- `NvsVideoClip nvsVideoClip = meicamVideoClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2275`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2364`
- `NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(shotFilePath,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:409`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:422`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:439`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:451`, `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:153` (+3 more)
- `NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(clipPosition);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:575`
- `NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(mSelectedClipPosition);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:632`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:655`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:677`
- `NvsVideoClip nvsVideoClip = videoClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:839`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:559`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:594`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:640`
- `NvsVideoClip nvsVideoClip1 = (NvsVideoClip) clipInfo.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:568`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:607`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:647`
- `NvsVideoClip object = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:515`
- `NvsVideoClip oldVideoClip = oldVideoTrack.getClipByIndex(j);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:115`
- `NvsVideoClip orgClip = afterClipArray.get(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1756`
- `NvsVideoClip orgClip = clipArray.get(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1746`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1807`
- `NvsVideoClip orgClip = clipArray.get(n);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1837`
- `NvsVideoClip orgClip = preClipArray.get(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1751`
- `NvsVideoClip secClip = mVideoTrackSec.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:730`
- `NvsVideoClip secondClip = mVideoTrackSec.getClipByIndex(secIndex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:919`
- `NvsVideoClip secondTrackClip = mVideoTrackSec.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:673`
- `NvsVideoClip splitClip = videoTrack.getClipByTimelinePosition(point);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1976`
- `NvsVideoClip theFirstClip = mVidoeTrack.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:320`
- `NvsVideoClip theLastClip = mVidoeTrack.getClipByIndex(mCurentClipCount - 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:321`
- `NvsVideoClip videoClip = appendClip(videoTrack, clipInfo, needRotate);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1577`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1593`
- `NvsVideoClip videoClip = appendClip(videoTrack, recordClip, false);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:977`
- `NvsVideoClip videoClip = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:719`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1081`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1172`, `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1218`
- `NvsVideoClip videoClip = getVideoClip();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:192`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:323`
- `NvsVideoClip videoClip = meicamVideoTrack.getClipByIndex(clipIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1275`
- `NvsVideoClip videoClip = meicamVideoTrack.getClipByIndex(item.clipIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1205`
- `NvsVideoClip videoClip = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:402`
- `NvsVideoClip videoClip = nvsVideoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1908`
- `NvsVideoClip videoClip = object.getClipByTimelinePosition(timeStamp);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:281`
- `NvsVideoClip videoClip = videoTrack.addClip(videoFilePath, getInPoint(), getTrimIn(), getTrimOut());`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:564`
- `NvsVideoClip videoClip = videoTrack.appendClip(filePath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1619`
- `NvsVideoClip videoClip = videoTrack.appendClip(videoFilePath);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:532`
- `NvsVideoClip videoClip = videoTrack.appendClip(videoPath);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:574`
- `NvsVideoClip videoClip = videoTrack.appendTimelineClip(timeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:335`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/DurationActivity.java:136`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java:108`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:213`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:704`, `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:223` (+1 more)
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(clipIindex);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:456`, `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:954`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(clipIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:846`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:150`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:360`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2007`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2108`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2165`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(i1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2856`
- `NvsVideoClip videoClip = videoTrack.getClipByIndex(index);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:227`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:409`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:255`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:768`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:802` (+2 more)
- `NvsVideoClip videoClip = videoTrack.insertClip(videoFilePath, clipIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:584`
- `NvsVideoClip videoClip = videoTrack.insertTimelineClip(timeline, 0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:321`
- `NvsVideoClip videoClip1 = videoClip.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1302`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1339`
- `NvsVideoClip videoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:740`
- `NvsVideoResolution nvsVideoResolution = mNvsTimeline.getVideoRes();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1310`
- `NvsVideoResolution nvsVideoResolution = TimelineData.instance().getVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/ImageConverter.java:96`
- `NvsVideoResolution nvsVideoResolution = videoResolution;`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:532`
- `NvsVideoResolution resolution = mTimeline.getVideoRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2575`
- `NvsVideoResolution resolution = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:172`
- `NvsVideoResolution resolution = timeline.getVideoRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1869`
- `NvsVideoResolution resolution = TimelineData.getInstance().getVideoResolution();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1131`, `libEngine/src/main/java/com/meishe/engine/local/LMeicamVideoClip.java:470`
- `NvsVideoResolution videoEditRes = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2275`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:850`
- `NvsVideoResolution videoEditRes = oldTimeline.getVideoRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:42`
- `NvsVideoResolution videoEditRes = videoResolution;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1853`
- `NvsVideoResolution videoRes = mNvsTimeline.getVideoRes();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:576`
- `NvsVideoResolution videoRes = mTimeline.getVideoRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:203`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:545`
- `NvsVideoResolution videoRes = timeline.getVideoRes();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:211`
- `NvsVideoResolution videoResolution = getNvsTimeline().getVideoRes();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1355`
- `NvsVideoResolution videoResolution = TimelineData.getInstance().getVideoResolution();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1010`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1023`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1037`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1054`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:3056` (+1 more)
- `NvsVideoResolution videoResolution = TimelineData.instance().getVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:345`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:147`
- `nvsVideoResolution.imagePAR = new NvsRational(1, 1);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:534`
- `NvsVideoTrack meicamVideoTrack = meicamTimeline.getVideoTrackByIndex(item.trackIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1203`
- `NvsVideoTrack meicamVideoTrack = meicamTimeline.getVideoTrackByIndex(trackIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1273`
- `NvsVideoTrack meicamVideoTrack = meicamTimeline.getVideoTrackByIndex(trackIndexTimeline);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1193`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1264`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1428`
- `NvsVideoTrack newVideoTrack = newTimeline.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:106`
- `NvsVideoTrack nvsVideoTrack = mNvsTimeline.getVideoTrackByIndex(trackIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1172`
- `NvsVideoTrack nvsVideoTrack = mTimeline.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:359`
- `NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:570`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:627`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:650`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:672`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1901`
- `NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(trackIndex);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2271`
- `NvsVideoTrack nvsVideoTrack = nvsTimeline.appendVideoTrack();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoTrack.java:57`
- `NvsVideoTrack nvsVideoTrack = videoTrack.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:498`
- `NvsVideoTrack object = getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoTrack.java:42`
- `NvsVideoTrack object = meicamVideoTrack.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:276`
- `NvsVideoTrack oldVideoTrack = oldTimeline.getVideoTrackByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:105`
- `NvsVideoTrack track = meicamVideoTrack.bindToTimeline(timeline);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:613`
- `NvsVideoTrack videoTrack = m_timeLine.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:547`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:578`, `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:787`
- `NvsVideoTrack videoTrack = meicamVideoTrack.getObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:261`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1232`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1285`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2352`
- `NvsVideoTrack videoTrack = mNvsTimeline.getVideoTrackByIndex(0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:838`
- `NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:146`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:293`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationClipAdapter.java:112`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:134`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:220` (+18 more)
- `NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:547`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:763`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:798`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:821`, `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:907` (+2 more)
- `NvsVideoTrack videoTrack = null;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:315`
- `NvsVideoTrack videoTrack = timeline.appendVideoTrack();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:962`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:206`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:220`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:346`
- `NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:300`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:819`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:900`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1113`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1171`
- `NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:647`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:687`
- `NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(i);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2853`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:897`
- `NvsVideoTrack videoTrack = videoTrackCount == 0 ? timeline.appendVideoTrack() : timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:368`
- `NvsVideoTrack videoTrack,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1539`
- `NvsVideoTrack videoTrackByIndex = mTimeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:417`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:648`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2381`
- `NvsVideoTrack videoTrackByIndex = nvsTimeline.getVideoTrackByIndex(0);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1026`, `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1094`
- `NvsVideoTrack videoTrackByIndex = timeline.getVideoTrackByIndex(0);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:245`
- `Object getNvsObject();`
  Sources: `libEngine/src/main/java/com/meishe/engine/interf/IClip.java:17`
- `Object value = map.get(NvsConstants.IS_POST_STORY_BOARD_3D).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:901`
- `playNow(mStreamingContext.getTimelineCurrentPosition(mNvsTimeline), -1);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:194`
- `playNow(mStreamingContext.getTimelineCurrentPosition(mNvsTimeline), end);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:222`
- `positions.add(new NvsPosition2D(regionData[i], regionData[++i]));`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2702`
- `private  int mMakeRatio = NvsConstants.AspectRatio.AspectRatio_NoFitRatio;`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:64`
- `private int mMakeRatio = NvsConstants.AspectRatio.AspectRatio_NoFitRatio;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:67`
- `private int mRotateAngle = NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/bean/RecordClip.java:28`
- `private List<NvsVideoClip> mClipList = new ArrayList<>();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:93`
- `private long setTrimInPoint(NvsVideoClip videoClip, long trim, boolean affectSibling) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2930`
- `private long setTrimOutPoint(NvsVideoClip videoClip, long trim, boolean affectSibling) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2923`
- `private NvsRational mNvsRational;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:74`, `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:71`
- `private NvsStreamingContext mStreamingContext;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:58`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/DurationActivity.java:35`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:57`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:51`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltActivity.java:57` (+2 more)
- `private NvsTimeline initTimeline(ArrayList<RecordClip> clips) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:948`
- `private NvsTimeline m_timeLine;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:86`
- `private NvsTimeline mAuxiliaryTimeline;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:92`
- `private NvsTimeline mNvsTimeline;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:91`
- `private NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:45`, `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:29`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:185`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:57`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:70` (+25 more)
- `private NvsTimelineEditor mTimelineEditor;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:49`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:62`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:44`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:89`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:55` (+1 more)
- `private NvsVideoClip appendClip(NvsVideoTrack videoTrack, RecordClip clipInfo, boolean needRotate) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1615`
- `private NvsVideoClip getVideoClip() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:394`
- `private NvsVideoClip mSelectNvsVideoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:154`
- `private NvsVideoClip mVideoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:59`
- `private NvsVideoClip videoClip;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:67`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:115`
- `private NvsVideoResolution m_videoResolution;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:26`
- `private NvsVideoResolution mVideoResolution;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:72`, `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:69`
- `private NvsVideoTrack mVideoTrack;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:186`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:137`, `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:96`, `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:51`
- `private NvsVideoTrack mVideoTrackFir;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:97`
- `private NvsVideoTrack mVideoTrackSec;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:98`
- `private NvsVideoTrack mVidoeTrack;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:72`, `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:75`
- `private static boolean buildVideoTrack(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:480`
- `private static void addVideoClip(NvsVideoTrack videoTrack, ClipInfo clipInfo, boolean isTrimClip, NvsVideoResolution videoRes) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:396`
- `private static void addVideoClip(NvsVideoTrack videoTrack, String filePath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:568`
- `private static void applyNoiseSuppression(int noiseSuppressionLevel, NvsVideoClip videoClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:593`
- `private String TAG = "NvsTimelineEditor";`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:30`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:27`
- `private void addCutTimeline(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:310`
- `private void addVideoClip(NvsVideoTrack videoTrack,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:737`
- `private void changeVideoClipTrimPoint(NvsVideoTrack videoTrack, long trimIn, long trimOut) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:701`
- `private void localVideoTrim(NvsVideoClip videoClip, RecordClip clipInfo) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1648`
- `private void rebuildTimelineStructure(NvsVideoTrack videoTrack,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1560`
- `private void startPlay(NvsTimeline timeline, long startTime) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1005`
- `public ArrayList<NvsVideoClip> getClipRange(long point, long duration, NvsVideoTrack videoTrack) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1950`
- `public boolean doRepeatTimeline(long point, NvsVideoTrack videoTrack) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1765`
- `public boolean doSlowMotionTimeline(long point, NvsVideoTrack videoTrack) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1693`
- `public boolean muteVideoTrack(NvsVideoTrack videoTrack) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1924`
- `public boolean splitClip(long point, NvsVideoTrack videoTrack) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1972`
- `public class ClipInfo<T> extends NvsObject<T> implements Cloneable, Comparable<ClipInfo> , Serializable, TimelineDataToLocalAdapter<LClipInfo> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/ClipInfo.java:13`
- `public class LClipInfo extends LNvsObject implements Cloneable, Comparable<LClipInfo> , Serializable, LocalToTimelineDataAdapter<ClipInfo> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LClipInfo.java:13`
- `public class LTrackInfo extends LNvsObject implements Cloneable, LocalToTimelineDataAdapter<TrackInfo> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LTrackInfo.java:13`
- `public class MeicamVideoClip extends ClipInfo<NvsVideoClip> implements Cloneable, Serializable, IResourceParser {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:49`
- `public class MeicamVideoTrack extends TrackInfo<NvsVideoTrack> implements Cloneable, Serializable {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoTrack.java:15`
- `public class NvsTimelineEditor extends RelativeLayout {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:29`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:26`
- `public class TrackInfo<T> extends NvsObject<T> implements Cloneable, TimelineDataToLocalAdapter<LTrackInfo> {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TrackInfo.java:13`
- `public int rotation = NvsVideoStreamInfo.VIDEO_ROTATION_0;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/ClipInfo.java:27`
- `public NvsRational getNvsRational() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:340`, `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:261`
- `public NvsTimeline createTimeline() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:204`
- `public NvsTimeline getAuxiliaryTimeline() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:140`
- `public NvsTimeline getCurrentTimeline() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:237`
- `public NvsTimeline getNvsTimeline() {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:111`
- `public NvsTimeline nvsTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/EditBaseActivity.java:17`
- `public NvsTimelineEditor(Context context, AttributeSet attrs) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:105`, `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:97`
- `public NvsVideoClip addToTimeline(NvsVideoTrack videoTrack) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:543`
- `public NvsVideoClip appendToTimeline(NvsVideoTrack videoTrack) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:522`
- `public NvsVideoClip getVideoClipByIndex(int trackIndex, int clipIndex) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1162`
- `public NvsVideoClip insertToTimeline(NvsVideoTrack videoTrack, int clipIndex) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:574`
- `public NvsVideoResolution cloneVideoResolution() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:168`
- `public NvsVideoResolution getVideoResolution() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:164`, `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:300`, `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:238`
- `public NvsVideoTrack bindToTimeline(NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoTrack.java:53`
- `public PlayerFragment(NvsTimeline timeline, NvsStreamingContext streamingContext, PlayEventListener listener) {`
  Sources: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:29`
- `public static boolean applyTheme(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:712`
- `public static boolean applyTheme(NvsTimeline timeline, String themeId) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1061`
- `public static boolean buildSingleClipVideoTrack(NvsTimeline timeline, ClipInfo clipInfo, boolean isTrimClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:202`
- `public static boolean buildSingleClipVideoTrackExt(NvsTimeline timeline, String filePath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:216`
- `public static boolean buildVideoTrack(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:341`
- `public static boolean fillTrack(NvsTimeline timeline, List<MeicamVideoTrack> videoTrackList) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:611`
- `public static boolean reBuildVideoTrack(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:363`
- `public static boolean removeTimeline(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:321`
- `public static double getVolumeByKeyTime(NvsVideoClip videoClip, long timeStamp) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:707`
- `public static final int VIDEO_CLIP_TYPE_AV = NvsVideoClip.VIDEO_CLIP_TYPE_AV;`
  Sources: `libBase/src/main/java/com/meishe/base/constants/NvsConstants.java:76`, `libEngine/src/main/java/com/meishe/engine/interf/StreamingConstant.java:12`
- `public static final int VIDEO_CLIP_TYPE_IMAGE = NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE;`
  Sources: `libBase/src/main/java/com/meishe/base/constants/NvsConstants.java:78`, `libEngine/src/main/java/com/meishe/engine/interf/StreamingConstant.java:13`
- `public static NvsSize getTimelineSize(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1866`
- `public static NvsStreamingContext initStreamingContext(Context mContext, String licensePath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:120`
- `public static NvsTimeline copyTimeline(NvsTimeline oldTimeline, NvsStreamingContext streamingContext) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:35`
- `public static NvsTimeline createSingleClipTimeline(ClipInfo clipInfo, boolean isTrimClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:178`
- `public static NvsTimeline createSingleClipTimelineExt(NvsVideoResolution videoEditRes, String filePath) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:192`
- `public static NvsTimeline createTimeline() {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:138`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:66`
- `public static NvsTimeline createTimeline(int width, int height) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:146`
- `public static NvsTimeline mTimeline;`
  Sources: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:96`
- `public static NvsTimeline newTimeline(NvsVideoResolution videoResolution) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1841`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:510`
- `public static NvsTimeline newTimeline(String firstVideoPath) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:499`
- `public static NvsVideoResolution getVideoEditResolutionByClip(String path) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:848`
- `public static NvsVideoTrack getNvsVideoTrack(int trackIndex) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:970`
- `public static void alignedResolution(NvsVideoResolution resolution) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:550`
- `public static void appendVideoClip(NvsTimeline mTimeline, NvsVideoTrack nvsVideoTrack, ThemePreviewBean previewBean, ThemeModel.ShotInfo shotInfo, ThemeModel mThemeModel) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:134`
- `public static void applyVolumeKeyInfo(NvsVideoClip videoClip, Map<Long, VolumeKeyInfo> volumeKeyInfoMap) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:662`
- `public static void buildTimelineAnimation(NvsTimeline mTimeline, ArrayList<ClipInfo> clipInfoArrayList) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1897`
- `public static void logTimeline(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2850`
- `public static void rebuildTimeline(NvsTimeline timeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:578`
- `public static void restoreThemeVolume(NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1084`
- `public static void setThemeQuiet(NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1070`
- `public static void setTimelineData(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:229`, `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:88`
- `public static void setVideoClipTrans(NvsVideoTrack nvsVideoTrack, List<ThemeModel.ShotInfo> shotInfos) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:79`
- `public void loadData(NvsVideoClip videoClip) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:180`
- `public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:144`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1664`, `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:598`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:349`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1943` (+7 more)
- `public void playStopped(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:193`, `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:146`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:295`, `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:775`, `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:155` (+6 more)
- `public void playStopped(NvsTimeline timeline) {}`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:170`
- `public void playTimeline(NvsTimeline mTimeLine, long startTime, long endTime) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:585`
- `public void rebuildTimeline(NvsTimeline timeline,`
  Sources: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1538`
- `public void setAuxiliaryTimeline(NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:131`
- `public void setData(NvsVideoClip videoClip, int trackIndex) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:594`
- `public void setNvsRational(NvsRational nvsRational) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:344`, `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:265`
- `public void setNvsTimeline(NvsTimeline nvsTimeline) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:121`
- `public void setTimeLine(NvsTimeline mTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationClipAdapter.java:44`
- `public void setTimeline(NvsTimeline timeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:272`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:532`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:283`
- `public void setVideoClipInfo(ClipInfo clipInfo, NvsVideoClip nvsVideoClip) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:548`
- `public void setVideoResolution(NvsVideoResolution mVideoResolution) {`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:304`, `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:242`
- `public void setVideoResolution(NvsVideoResolution resolution) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:160`
- `public void start(NvsTimeline mTimeline, long startTime, long endTime) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:62`
- `public void startNow(NvsTimeline mTimeline) {`
  Sources: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:52`
- `return mNvsRational;`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:341`, `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:262`
- `return mNvsTimeline.getDuration();`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:419`
- `return mNvsTimeline;`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:112`
- `return mStreamingContext.getTimelineCurrentPosition(mNvsTimeline);`
  Sources: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:235`
- `return NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:299`
- `return NvsStreamingContext.init(mContext, licensePath, NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:121`
- `TimelineData.getInstance().setNvsRational(new NvsRational(25, 1));`
  Sources: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:535`
- `timelineData.setNvsRational(mNvsRational);`
  Sources: `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:330`
- `valuePackageId = (String) map.get(NvsConstants.POST_PACKAGE_ID).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:898`
- `valuePackageId = (String) map.get(NvsConstants.POST_PACKAGE_ID_OLD).getValue();`
  Sources: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:894`
- `videoClip.setImageMotionMode(NvsVideoClip.IMAGE_CLIP_MOTIONMMODE_ROI);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:200`, `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:480`
- `videoEditRes.imagePAR = new NvsRational(1, 1);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1854`
- `videoResolution = new NvsVideoResolution();`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1849`
- `void onTimelineChanged(NvsTimeline timeline, boolean needSave);`
  Sources: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2837`
- `void playStopped(NvsTimeline timeline);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:113`, `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:203`, `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:76`, `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:248`, `libEngine/src/main/java/com/meishe/engine/interf/VideoFragmentListener.java:14`
- `void setNvsObject(Object nvsObject);`
  Sources: `libEngine/src/main/java/com/meishe/engine/interf/IClip.java:24`
- `| NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:122`
- `| NvsStreamingContext.STREAMING_CONTEXT_FLAG_INTERRUPT_STOP_FOR_INTERNAL_STOP);`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:124`
- `| NvsStreamingContext.STREAMING_CONTEXT_FLAG_NEED_GIF_MOTION`
  Sources: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:123`
- `} else if (clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {// 视频`
  Sources: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:207`
