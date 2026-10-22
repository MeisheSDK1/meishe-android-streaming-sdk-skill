# Demo Simple Snippets - Core Lifecycle

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: SDK initialization, singleton access, callbacks, permissions, AV file info, thumbnail views, main-thread checks, and lifecycle cleanup.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [core-lifecycle-001 getSdkVersion](#core-lifecycle-001-getsdkversion)
- [core-lifecycle-002 getSdkVersion](#core-lifecycle-002-getsdkversion)
- [core-lifecycle-003 OnRightTextClick](#core-lifecycle-003-onrighttextclick)
- [core-lifecycle-004 checkSupport4K](#core-lifecycle-004-checksupport4k)
- [core-lifecycle-005 support4kAvcEncoding](#core-lifecycle-005-support4kavcencoding)
- [core-lifecycle-006 support4kAvcEncoding](#core-lifecycle-006-support4kavcencoding)
- [core-lifecycle-007 getStreamingContext](#core-lifecycle-007-getstreamingcontext)
- [core-lifecycle-008 getStreamingContext](#core-lifecycle-008-getstreamingcontext)
- [core-lifecycle-009 getStreamingContext](#core-lifecycle-009-getstreamingcontext)
- [core-lifecycle-010 getMaterialList](#core-lifecycle-010-getmateriallist)
- [core-lifecycle-011 getMaterialList](#core-lifecycle-011-getmateriallist)
- [core-lifecycle-012 getMaterialList](#core-lifecycle-012-getmateriallist)
- [core-lifecycle-013 getMaterialTypeAndCategory](#core-lifecycle-013-getmaterialtypeandcategory)
- [core-lifecycle-014 getMaterialTypeAndCategory](#core-lifecycle-014-getmaterialtypeandcategory)
- [core-lifecycle-015 getOldObjectGet](#core-lifecycle-015-getoldobjectget)
- [core-lifecycle-016 download](#core-lifecycle-016-download)
- [core-lifecycle-017 cancelAll](#core-lifecycle-017-cancelall)
- [core-lifecycle-018 cancelRequest](#core-lifecycle-018-cancelrequest)
- [core-lifecycle-019 onCreateView](#core-lifecycle-019-oncreateview)
- [core-lifecycle-020 getInstance](#core-lifecycle-020-getinstance)
- [core-lifecycle-021 onClick](#core-lifecycle-021-onclick)
- [core-lifecycle-022 start](#core-lifecycle-022-start)
- [core-lifecycle-023 initRootView](#core-lifecycle-023-initrootview)
- [core-lifecycle-024 getRotation](#core-lifecycle-024-getrotation)
- [core-lifecycle-025 getRotation](#core-lifecycle-025-getrotation)
- [core-lifecycle-026 onFirstVideoFramePresented](#core-lifecycle-026-onfirstvideoframepresented)
- [core-lifecycle-027 onHardwareError](#core-lifecycle-027-onhardwareerror)
- [core-lifecycle-028 onClick](#core-lifecycle-028-onclick)
- [core-lifecycle-029 onClick](#core-lifecycle-029-onclick)
- [core-lifecycle-030 getRemoteAssetsWithPage](#core-lifecycle-030-getremoteassetswithpage)
- [core-lifecycle-031 resetVideoRatioFromRotation](#core-lifecycle-031-resetvideoratiofromrotation)
- [core-lifecycle-032 initParameterSetting](#core-lifecycle-032-initparametersetting)
- [core-lifecycle-033 initViews](#core-lifecycle-033-initviews)
- [core-lifecycle-034 onError](#core-lifecycle-034-onerror)
- [core-lifecycle-035 initStreamContext](#core-lifecycle-035-initstreamcontext)
- [core-lifecycle-036 getAspect](#core-lifecycle-036-getaspect)
- [core-lifecycle-037 createAuxiliaryStreamingContext](#core-lifecycle-037-createauxiliarystreamingcontext)
- [core-lifecycle-038 getStreamingContext](#core-lifecycle-038-getstreamingcontext)
- [core-lifecycle-039 getStreamingContext](#core-lifecycle-039-getstreamingcontext)
- [core-lifecycle-040 getStreamingContext](#core-lifecycle-040-getstreamingcontext)
- [core-lifecycle-041 getStreamingContext](#core-lifecycle-041-getstreamingcontext)
- [core-lifecycle-042 getCustomHeight](#core-lifecycle-042-getcustomheight)
- [core-lifecycle-043 getCustomHeight](#core-lifecycle-043-getcustomheight)
- [core-lifecycle-044 getVideoResolutionByRatio](#core-lifecycle-044-getvideoresolutionbyratio)
- [core-lifecycle-045 NvsServerClient](#core-lifecycle-045-nvsserverclient)
- [core-lifecycle-046 convertResponse](#core-lifecycle-046-convertresponse)
<!-- END GENERATED CONTENTS -->

## `core-lifecycle-001` `getSdkVersion`

Source: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:57`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`, `NvsStreamingContext.SdkVersion`
Common calls: `getInstance()`, `getSdkVersion()`

Simple sequence:

```java
NvsStreamingContext instance = NvsStreamingContext.getInstance();
if (instance != null) {
NvsStreamingContext.SdkVersion version = instance.getSdkVersion();
```

## `core-lifecycle-002` `getSdkVersion`

Source: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:59`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.SdkVersion`
Common calls: `getSdkVersion()`

Simple sequence:

```java
if (instance != null) {
NvsStreamingContext.SdkVersion version = instance.getSdkVersion();
```

## `core-lifecycle-003` `OnRightTextClick`

Source: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:459`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH`, `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH`, `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_EXTREMELY_HIGH`
Common calls: `setOnCheckedChangeListener()`, `OnCheckedChangeListener()`

Simple sequence:

```java
mCapture_ratio_sex.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
mCaptureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH;
mCaptureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH;
mCaptureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_EXTREMELY_HIGH;
```

## `core-lifecycle-004` `checkSupport4K`

Source: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:651`

API classes: `NvsConstants`
Static/constants: `NvsConstants.SIZE_4K_WIDTH`, `NvsConstants.SIZE_4K_HEIGHT`
Common calls: `getCameraCharacteristics()`, `get()`, `getCameraIdList()`, `getSystemService()`, `isEmpty()`, `isOutputSupportedFor()`, `getOutputSizes()`, `getWidth()`, `getHeight()`, `printStackTrace()`

Simple sequence:

```java
CameraManager manager = (CameraManager) this.getSystemService(Context.CAMERA_SERVICE);
try {
String s = manager.getCameraIdList()[0];
CameraCharacteristics characteristic = manager.getCameraCharacteristics(s);
for (String id : manager.getCameraIdList()) {
= manager.getCameraCharacteristics(id);
CameraCharacteristics cameraCharacteristics = manager.getCameraCharacteristics(cameraId);
Size[] outputSizes = streamConfMap.getOutputSizes(ImageFormat.YUV_420_888);
for (Size outputSize : outputSizes) {
int width = outputSize.getWidth();
int height = outputSize.getHeight();
if (width == NvsConstants.SIZE_4K_WIDTH && height == NvsConstants.SIZE_4K_HEIGHT) {
```

## `core-lifecycle-005` `support4kAvcEncoding`

Source: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:702`

API classes: `NvsConstants`
Static/constants: `NvsConstants.SIZE_4K_WIDTH`, `NvsConstants.SIZE_4K_HEIGHT`
Common calls: `getUpper()`, `getCapabilitiesForType()`, `getVideoCapabilities()`, `getSupportedWidths()`, `getSupportedHeights()`, `printStackTrace()`

Simple sequence:

```java
for (MediaCodecInfo codecInfo : avcEncoderInfos) {
final MediaCodecInfo.CodecCapabilities codecCaps = codecInfo.getCapabilitiesForType("video/avc");
final MediaCodecInfo.VideoCapabilities videoCaps = codecCaps.getVideoCapabilities();
final Range<Integer> supportedWidths = videoCaps.getSupportedWidths();
final Range<Integer> supportedHeights = videoCaps.getSupportedHeights();
if (supportedWidths.getUpper() >= NvsConstants.SIZE_4K_WIDTH && supportedHeights.getUpper() >= NvsConstants.SIZE_4K_HEIGHT) {
```

## `core-lifecycle-006` `support4kAvcEncoding`

Source: `app/src/main/java/com/meishe/sdkdemo/activity/SettingActivity.java:704`

API classes: `NvsConstants`
Static/constants: `NvsConstants.SIZE_4K_WIDTH`, `NvsConstants.SIZE_4K_HEIGHT`
Common calls: `getUpper()`, `getCapabilitiesForType()`, `getVideoCapabilities()`, `getSupportedWidths()`, `getSupportedHeights()`

Simple sequence:

```java
for (MediaCodecInfo codecInfo : avcEncoderInfos) {
final MediaCodecInfo.CodecCapabilities codecCaps = codecInfo.getCapabilitiesForType("video/avc");
final MediaCodecInfo.VideoCapabilities videoCaps = codecCaps.getVideoCapabilities();
final Range<Integer> supportedWidths = videoCaps.getSupportedWidths();
final Range<Integer> supportedHeights = videoCaps.getSupportedHeights();
if (supportedWidths.getUpper() >= NvsConstants.SIZE_4K_WIDTH && supportedHeights.getUpper() >= NvsConstants.SIZE_4K_HEIGHT) {
```

## `core-lifecycle-007` `getStreamingContext`

Source: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:76`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.class`, `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `initStreamingContext()`

Simple sequence:

```java
if (mStreamingContext == null) {
synchronized (NvsStreamingContext.class) {
if (mStreamingContext == null) {
mStreamingContext = NvsStreamingContext.getInstance();
if (mStreamingContext == null) {
mStreamingContext = TimelineUtil.initStreamingContext(getApplicationContext(), licensePath);
```

## `core-lifecycle-008` `getStreamingContext`

Source: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:77`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.class`, `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `initStreamingContext()`

Simple sequence:

```java
synchronized (NvsStreamingContext.class) {
if (mStreamingContext == null) {
mStreamingContext = NvsStreamingContext.getInstance();
if (mStreamingContext == null) {
mStreamingContext = TimelineUtil.initStreamingContext(getApplicationContext(), licensePath);
```

## `core-lifecycle-009` `getStreamingContext`

Source: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:78`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `initStreamingContext()`

Simple sequence:

```java
if (mStreamingContext == null) {
mStreamingContext = NvsStreamingContext.getInstance();
if (mStreamingContext == null) {
mStreamingContext = TimelineUtil.initStreamingContext(getApplicationContext(), licensePath);
```

## `core-lifecycle-010` `getMaterialList`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:41`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `valueOf()`, `getCategory()`, `getType()`, `isEmpty()`, `getCategories()`, `getKind()`, `getLocaleLanguage()`, `getSorted()`, `get()`, `requestGet()`

Simple sequence:

```java
params.put("type", assetType.getType());
if (!TextUtils.isEmpty(assetType.getCategory())) {
params.put("category", assetType.getCategory());
params.put("categories", assetType.getCategories());
params.put("kind", assetType.getKind());
params.put("lang", Util.getLocaleLanguage());
params.put("sorted", String.valueOf(assetType.getSorted()));
NvsServerClient.get().requestGet(tag, apiName, params, callback);
```

## `core-lifecycle-011` `getMaterialList`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:79`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `valueOf()`, `getType()`, `getCategory()`, `getLocaleLanguage()`, `getSorted()`, `get()`, `requestGet()`

Simple sequence:

```java
params.put("type", assetType.getType());
params.put("category", assetType.getCategory());
params.put("lang", Util.getLocaleLanguage());
params.put("sorted", String.valueOf(assetType.getSorted()));
NvsServerClient.get().requestGet(tag, apiName, params, callback);
```

## `core-lifecycle-012` `getMaterialList`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:102`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `valueOf()`, `getLocaleLanguage()`, `get()`, `requestGet()`

Simple sequence:

```java
params.put("lang", Util.getLocaleLanguage());
NvsServerClient.get().requestGet(tag, apiName, params, callback);
```

## `core-lifecycle-013` `getMaterialTypeAndCategory`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:151`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `getType()`, `getCategory()`, `get()`, `requestGet()`

Simple sequence:

```java
params.put("types", assetType.getType());
params.put("categories", assetType.getCategory());
NvsServerClient.get().requestGet(tag, apiName, params, callback);
```

## `core-lifecycle-014` `getMaterialTypeAndCategory`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:168`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `get()`, `requestGet()`

Simple sequence:

```java
NvsServerClient.get().requestGet(tag, apiName, params, callback);
```

## `core-lifecycle-015` `getOldObjectGet`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:197`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `get()`, `requestObjectGet()`

Simple sequence:

```java
NvsServerClient.get().requestObjectGet(url, callBack);
```

## `core-lifecycle-016` `download`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:211`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `get()`, `download()`

Simple sequence:

```java
NvsServerClient.get().download(tag, url, filePath, fileName, listener);
```

## `core-lifecycle-017` `cancelAll`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:219`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `get()`, `cancelAll()`

Simple sequence:

```java
NvsServerClient.get().cancelAll();
```

## `core-lifecycle-018` `cancelRequest`

Source: `app/src/main/java/com/meishe/sdkdemo/base/http/HttpManager.java:229`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `get()`, `cancelRequest()`

Simple sequence:

```java
NvsServerClient.get().cancelRequest(tag);
```

## `core-lifecycle-019` `onCreateView`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneFragment.java:49`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `inflate()`, `findViewById()`, `getInstance()`, `addView()`, `setStreamingContext()`

Simple sequence:

```java
mStreamingContext = NvsStreamingContext.getInstance();
mCaptureSceneEffectView.setStreamingContext(mStreamingContext, getActivity(), mType);
```

## `core-lifecycle-020` `getInstance`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:29`

API classes: `NvsStreamingContextUtil`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `initStreamingContext()`, `getContext()`

Simple sequence:

```java
private NvsStreamingContextUtil() {
mStreamingContext = NvsStreamingContext.getInstance();
if (mStreamingContext == null) {
mStreamingContext= TimelineUtil.initStreamingContext(MSApplication.getContext(), licensePath);
```

## `core-lifecycle-021` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:191`

API classes: `NvsStreamingContextUtil`
Static/constants: `NvsStreamingContextUtil.getInstance`
Common calls: `setOnClickListener()`, `OnClickListener()`, `getInstance()`, `startNow()`

Simple sequence:

```java
previewImageStop.setOnClickListener(new View.OnClickListener() {
NvsStreamingContextUtil.getInstance().startNow(mTimeline);
```

## `core-lifecycle-022` `start`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:246`

API classes: `NvsStreamingContextUtil`
Static/constants: `NvsStreamingContextUtil.getInstance`
Common calls: `getInstance()`, `stop()`

Simple sequence:

```java
NvsStreamingContextUtil.getInstance().stop();
```

## `core-lifecycle-023` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:297`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
mStreamingContext = NvsStreamingContext.getInstance();
```

## `core-lifecycle-024` `getRotation`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1664`

API classes: `NvsVideoStreamInfo`
Static/constants: `NvsVideoStreamInfo.VIDEO_ROTATION_90`, `NvsVideoStreamInfo.VIDEO_ROTATION_270`, `NvsVideoStreamInfo.VIDEO_ROTATION_180`
Common calls: `getVideoStreamCount()`, `getVideoStreamRotation()`

Simple sequence:

```java
if (fileInfo != null) {
int videoStreamCount = fileInfo.getVideoStreamCount();
if (videoStreamCount > 0) {
rotation = fileInfo.getVideoStreamRotation(0);
if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_90) {
rotation = NvsVideoStreamInfo.VIDEO_ROTATION_270;
} else if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_180) {
rotation = NvsVideoStreamInfo.VIDEO_ROTATION_180;
} else if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_270) {
rotation = NvsVideoStreamInfo.VIDEO_ROTATION_90;
```

## `core-lifecycle-025` `getRotation`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1666`

API classes: `NvsVideoStreamInfo`
Static/constants: `NvsVideoStreamInfo.VIDEO_ROTATION_90`, `NvsVideoStreamInfo.VIDEO_ROTATION_270`, `NvsVideoStreamInfo.VIDEO_ROTATION_180`
Common calls: `getVideoStreamRotation()`

Simple sequence:

```java
if (videoStreamCount > 0) {
rotation = fileInfo.getVideoStreamRotation(0);
if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_90) {
rotation = NvsVideoStreamInfo.VIDEO_ROTATION_270;
} else if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_180) {
rotation = NvsVideoStreamInfo.VIDEO_ROTATION_180;
} else if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_270) {
rotation = NvsVideoStreamInfo.VIDEO_ROTATION_90;
```

## `core-lifecycle-026` `onFirstVideoFramePresented`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1948`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.HardwareErrorCallback`
Common calls: `setHardwareErrorCallback()`, `HardwareErrorCallback()`, `e()`

Simple sequence:

```java
mStreamingContext.setHardwareErrorCallback(new NvsStreamingContext.HardwareErrorCallback() {
```

## `core-lifecycle-027` `onHardwareError`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1954`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.WebCallback`
Common calls: `setWebCallback()`, `WebCallback()`, `setVisibility()`

Simple sequence:

```java
mStreamingContext.setWebCallback(new NvsStreamingContext.WebCallback() {
mVideoLoading.setVisibility(isWaiting ? View.VISIBLE : View.GONE);
```

## `core-lifecycle-028` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/feedback/FeedBackActivity.java:107`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.SdkVersion`, `NvsStreamingContext.getInstance`
Common calls: `valueOf()`, `toString()`, `getText()`, `getId()`, `getInstance()`, `getSdkVersion()`, `getBrand()`, `getMode()`, `getAndroidVersion()`, `toJson()`, `postAsynJson()`, `e()`

Simple sequence:

```java
if (v.getId() == R.id.feedback_commit) {
NvsStreamingContext.SdkVersion sdkVersion = NvsStreamingContext.getInstance().getSdkVersion();
FeedBackData feedBackData = new FeedBackData(feedbackEditText.getText().toString(), feedbackEditTextNumber.getText().toString()
, sdkVersionNum, BuildHelper.getBrand() + "-" + BuildHelper.getMode() + "-" + BuildHelper.getAndroidVersion());
if (response != null && response.getErrNo() == 0) {
```

## `core-lifecycle-029` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/feedback/FeedBackActivity.java:108`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.SdkVersion`, `NvsStreamingContext.getInstance`
Common calls: `valueOf()`, `toString()`, `getText()`, `getInstance()`, `getSdkVersion()`, `getBrand()`, `getMode()`, `getAndroidVersion()`, `toJson()`, `postAsynJson()`, `e()`, `getErrNo()`

Simple sequence:

```java
NvsStreamingContext.SdkVersion sdkVersion = NvsStreamingContext.getInstance().getSdkVersion();
FeedBackData feedBackData = new FeedBackData(feedbackEditText.getText().toString(), feedbackEditTextNumber.getText().toString()
, sdkVersionNum, BuildHelper.getBrand() + "-" + BuildHelper.getMode() + "-" + BuildHelper.getAndroidVersion());
if (response != null && response.getErrNo() == 0) {
```

## `core-lifecycle-030` `getRemoteAssetsWithPage`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:261`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
mStreamingContext = NvsStreamingContext.getInstance();
```

## `core-lifecycle-031` `resetVideoRatioFromRotation`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:947`

API classes: `NvsVideoStreamInfo`
Static/constants: `NvsVideoStreamInfo.VIDEO_ROTATION_90`, `NvsVideoStreamInfo.VIDEO_ROTATION_180`, `NvsVideoStreamInfo.VIDEO_ROTATION_270`
Common calls: `getVideoStreamRotation()`

Simple sequence:

```java
if (videoStreamCount > 0) {
rotation = fileInfo.getVideoStreamRotation(0);
if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_90) {
} else if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_180) {
} else if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_270) {
```

## `core-lifecycle-032` `initParameterSetting`

Source: `app/src/main/java/com/meishe/sdkdemo/presenter/MainPresenter.java:154`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `instance()`, `getInstance()`, `isAndroidCameraPreferDualBufferAR()`, `d()`, `setSingleBufferMode()`

Simple sequence:

```java
boolean androidCameraPreferDualBufferAR = NvsStreamingContext.getInstance().isAndroidCameraPreferDualBufferAR();
parameterValues.setSingleBufferMode(!androidCameraPreferDualBufferAR);
```

## `core-lifecycle-033` `initViews`

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:293`

API classes: `NvsAIContext`
Static/constants: `NvsAIContext.init`
Common calls: `init()`

Simple sequence:

```java
mAISdkContext = NvsAIContext.init(getApplicationContext(), licensePath, 0);
```

## `core-lifecycle-034` `onError`

Source: `libBase/src/main/java/com/meishe/base/model/BaseMvpFragment.java:116`

API classes: `NvsError`
Common calls: `getErrorMessage()`

Simple sequence:

```java
public void onError(NvsError error) {
```

## `core-lifecycle-035` `initStreamContext`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:175`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.init`, `NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT`
Common calls: `init()`, `getApp()`

Simple sequence:

```java
public NvsStreamingContext initStreamContext() {
mStreamingContext = NvsStreamingContext.init(Utils.getApp(), licensePath, NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT);
return mStreamingContext;
```

## `core-lifecycle-036` `getAspect`

Source: `libEngine/src/main/java/com/meishe/engine/bean/CommonData.java:225`

API classes: `NvsConstants`
Static/constants: `NvsConstants.AspectRatio`
Common calls: `values()`, `abs()`

Simple sequence:

```java
return NvsConstants.AspectRatio.AspectRatio_NoFitRatio;
```

## `core-lifecycle-037` `createAuxiliaryStreamingContext`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:151`

API classes: `NvsStreamingContext`
Common calls: `createAuxiliaryStreamingContext()`

Simple sequence:

```java
public NvsStreamingContext createAuxiliaryStreamingContext() {
if (mAuxiliaryStreamingContext == null) {
mAuxiliaryStreamingContext = mStreamingContext.createAuxiliaryStreamingContext(0);
```

## `core-lifecycle-038` `getStreamingContext`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:313`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.class`, `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
public NvsStreamingContext getStreamingContext() {
if (mStreamingContext == null) {
synchronized (NvsStreamingContext.class) {
if (mStreamingContext == null) {
mStreamingContext = NvsStreamingContext.getInstance();
return mStreamingContext;
```

## `core-lifecycle-039` `getStreamingContext`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:314`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.class`, `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
if (mStreamingContext == null) {
synchronized (NvsStreamingContext.class) {
if (mStreamingContext == null) {
mStreamingContext = NvsStreamingContext.getInstance();
```

## `core-lifecycle-040` `getStreamingContext`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:315`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.class`, `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
synchronized (NvsStreamingContext.class) {
if (mStreamingContext == null) {
mStreamingContext = NvsStreamingContext.getInstance();
```

## `core-lifecycle-041` `getStreamingContext`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:316`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
if (mStreamingContext == null) {
mStreamingContext = NvsStreamingContext.getInstance();
```

## `core-lifecycle-042` `getCustomHeight`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1352`

API classes: `NvsVideoResolution`
Common calls: `getVideoRes()`

Simple sequence:

```java
if (mRatio == 0) {
NvsVideoResolution videoResolution = getNvsTimeline().getVideoRes();
```

## `core-lifecycle-043` `getCustomHeight`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1354`

API classes: `NvsVideoResolution`
Common calls: `getVideoRes()`

Simple sequence:

```java
if (mRatio == 0) {
NvsVideoResolution videoResolution = getNvsTimeline().getVideoRes();
```

## `core-lifecycle-044` `getVideoResolutionByRatio`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1382`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public NvsVideoResolution getVideoResolutionByRatio(int ratio) {
NvsVideoResolution nvsVideoResolution = new NvsVideoResolution();
```

## `core-lifecycle-045` `NvsServerClient`

Source: `libNet/src/main/java/com/meishe/net/NvsServerClient.java:53`

API classes: `NvsServerClient`

Simple sequence:

```java
private static NvsServerClient INSTANCE = new NvsServerClient();
```

## `core-lifecycle-046` `convertResponse`

Source: `libNet/src/main/java/com/meishe/net/custom/JsonCallback.java:68`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `get()`, `getDefaultGson()`, `fromJson()`, `optInt()`, `optString()`, `toString()`, `getGenericSuperclass()`, `getActualTypeArguments()`, `convertResponse()`, `body()`, `string()`, `optJSONObject()`

Simple sequence:

```java
if (clazz == null) {
Type genType = getClass().getGenericSuperclass();
if (genType != null) {
type = ((ParameterizedType) genType).getActualTypeArguments()[0];
if (data != null) {
t = NvsServerClient.get().getDefaultGson().fromJson(data.toString(), type);
t = NvsServerClient.get().getDefaultGson().fromJson(dataArray.toString(), type);
t = NvsServerClient.get().getDefaultGson().fromJson(body, type);
baseResponse.setCode(code);
baseResponse.setErrNo(errNo);
baseResponse.setMsg(msg);
baseResponse.setEnMsg(enMsg);
baseResponse.setData(t);
```
