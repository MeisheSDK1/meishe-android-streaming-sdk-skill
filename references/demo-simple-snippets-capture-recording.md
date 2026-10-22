# Demo Simple Snippets - Capture Recording

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: camera capture preview, capture callbacks, capture effects, recording toggles, capture flags, device capability checks, and picture/video capture.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [capture-recording-001 onClick](#capture-recording-001-onclick)
- [capture-recording-002 onClick](#capture-recording-002-onclick)
- [capture-recording-003 changeFlash](#capture-recording-003-changeflash)
- [capture-recording-004 setRecordVideoBitrateMultiplier](#capture-recording-004-setrecordvideobitratemultiplier)
- [capture-recording-005 setRecordVideoBitrateMultiplier](#capture-recording-005-setrecordvideobitratemultiplier)
- [capture-recording-006 onPause](#capture-recording-006-onpause)
- [capture-recording-007 getDialog](#capture-recording-007-getdialog)
- [capture-recording-008 initRootView](#capture-recording-008-initrootview)
- [capture-recording-009 isCaptureRecording](#capture-recording-009-iscapturerecording)
- [capture-recording-010 startCapturePreview](#capture-recording-010-startcapturepreview)
- [capture-recording-011 startCapturePreview](#capture-recording-011-startcapturepreview)
- [capture-recording-012 updateSettingsWithCapability](#capture-recording-012-updatesettingswithcapability)
- [capture-recording-013 onClick](#capture-recording-013-onclick)
- [capture-recording-014 onPause](#capture-recording-014-onpause)
- [capture-recording-015 startCapturePreview](#capture-recording-015-startcapturepreview)
- [capture-recording-016 startCapturePreview](#capture-recording-016-startcapturepreview)
- [capture-recording-017 onPlaybackPreloadingCompletion](#capture-recording-017-onplaybackpreloadingcompletion)
- [capture-recording-018 onPlaybackStopped](#capture-recording-018-onplaybackstopped)
- [capture-recording-019 seekTimeline](#capture-recording-019-seektimeline)
<!-- END GENERATED CONTENTS -->

## `capture-recording-001` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java:163`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `getStreamingEngineState()`, `changeCurrentDeviceIndex()`, `changeFlash()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
previewFragment.changeCurrentDeviceIndex();
previewFragment.changeFlash();
```

## `capture-recording-002` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java:166`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `getStreamingEngineState()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
```

## `capture-recording-003` `changeFlash`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangActivity.java:193`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.RECORD_GOP_SIZE`
Common calls: `setRecordVideoBitrateMultiplier()`, `put()`, `getBoomrangRecordingDirectory()`, `startRecord()`, `setEnabled()`

Simple sequence:

```java
previewFragment.setRecordVideoBitrateMultiplier(1.5f);
config.put(com.meicam.sdk.NvsStreamingContext.RECORD_GOP_SIZE, 5);
recordFilePath = PathUtils.getBoomrangRecordingDirectory("_record");
boomRangRecordBtn.setEnabled(false);
```

## `capture-recording-004` `setRecordVideoBitrateMultiplier`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:201`

API classes: `NvsStreamingContextUtil`, `NvsStreamingContext`
Static/constants: `NvsStreamingContextUtil.getInstance`, `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `getInstance()`, `getEngineState()`, `startRecording()`

Simple sequence:

```java
if (NvsStreamingContextUtil.getInstance().getEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
return mStreamingContext.startRecording(path, i, config);
```

## `capture-recording-005` `setRecordVideoBitrateMultiplier`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:202`

API classes: `NvsStreamingContextUtil`, `NvsStreamingContext`
Static/constants: `NvsStreamingContextUtil.getInstance`, `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `getInstance()`, `getEngineState()`, `startRecording()`

Simple sequence:

```java
if (NvsStreamingContextUtil.getInstance().getEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
return mStreamingContext.startRecording(path, i, config);
```

## `capture-recording-006` `onPause`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3632`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW`
Common calls: `stop()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW) {
mStreamingContext.stop();
```

## `capture-recording-007` `getDialog`

Source: `app/src/main/java/com/meishe/sdkdemo/dialog/TopMoreDialog.java:328`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CaptureDeviceCapability`
Common calls: `setEnabled()`, `getProgress()`, `e()`, `setMaxProgress()`, `setProgress()`, `getZoom()`, `d()`, `setText()`, `getExposureCompensation()`

Simple sequence:

```java
public void checkCapability(NvsStreamingContext.CaptureDeviceCapability capability) {
if (capability.supportFlash) {
mLlFlash.setEnabled(true);
if (capability.supportZoom) {
mZoomSeekBar.setMaxProgress(capability.maxZoom);
mZoomSeekBar.setProgress(mStreamingContext.getZoom());
mTvZoomNum.setText("1.0X");
mZoomSeekBar.setEnabled(true);
mExposeSeekBar.setMaxProgress(EXPOSE_ZOOM_FACTOR * (capability.maxExposureCompensation - mMinExpose));
mExposeSeekBar.setProgress(EXPOSE_ZOOM_FACTOR * (mStreamingContext.getExposureCompensation() - mMinExpose));
mExposeSeekBar.setEnabled(true);
String exposeText = (int) (mExposeSeekBar.getProgress() * 1f / EXPOSE_ZOOM_FACTOR + mMinExpose) + ".0";
mTvExposureNum.setText(exposeText);
```

## `capture-recording-008` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:302`

API classes: `NvsLiveWindow`
Common calls: `findViewById()`, `getInt()`, `inflate()`, `from()`, `getExtras()`, `getBoolean()`

Simple sequence:

```java
mLivewindow = (NvsLiveWindow) findViewById(R.id.livewidow);
if (getIntent() != null) {
Bundle bundle = getIntent().getExtras();
if (bundle != null) {
mInitArScene = bundle.getBoolean("initArScene");
mIntentStrength = bundle.getInt(INTENT_KEY_STRENGTH, -1);
mIntentCheekThinning = bundle.getInt(INTENT_KEY_CHEEK, -1);
mIntentEyeEnlarging = bundle.getInt(INTENT_KEY_EYE, -1);
```

## `capture-recording-009` `isCaptureRecording`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1170`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`

Simple sequence:

```java
return getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING;
```

## `capture-recording-010` `startCapturePreview`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1313`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW`, `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER`, `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME`, `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE`
Common calls: `instance()`, `getCaptureResolutionGrade()`, `startCapturePreview()`, `e()`

Simple sequence:

```java
int captureResolutionGrade = ParameterSettingValues.instance().getCaptureResolutionGrade();
if (deviceChanged || getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW) {
if (!mStreamingContext.startCapturePreview(mCurrentDeviceIndex,
captureResolutionGrade, NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER |
NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME
| NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE, null)) {
```

## `capture-recording-011` `startCapturePreview`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1315`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW`, `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER`, `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME`, `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE`
Common calls: `startCapturePreview()`, `e()`

Simple sequence:

```java
if (deviceChanged || getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW) {
if (!mStreamingContext.startCapturePreview(mCurrentDeviceIndex,
captureResolutionGrade, NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER |
NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME
| NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE, null)) {
```

## `capture-recording-012` `updateSettingsWithCapability`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1454`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CaptureDeviceCapability`
Common calls: `getCaptureDeviceCapability()`

Simple sequence:

```java
NvsStreamingContext.CaptureDeviceCapability capability = mStreamingContext.getCaptureDeviceCapability(deviceIndex);
```

## `capture-recording-013` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:426`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `setEnabled()`, `setImageResource()`, `setImageAlpha()`, `setOnClickListener()`, `OnClickListener()`, `getStreamingEngineState()`

Simple sequence:

```java
mSwitchFacingLayout.setOnClickListener(new View.OnClickListener() {
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
mFlashLayout.setEnabled(false);
mFlashButton.setImageResource(R.mipmap.icon_flash_off);
mFlashButton.setImageAlpha(128);
mFlashLayout.setEnabled(true);
mFlashButton.setImageResource(R.mipmap.icon_flash_off);
mFlashButton.setImageAlpha(255);
```

## `capture-recording-014` `onPause`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:945`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
```

## `capture-recording-015` `startCapturePreview`

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:948`

API classes: `NvsVideoResolution`, `NvsRational`
Common calls: `d()`, `canDetectOrientation()`, `enable()`, `startPreview()`, `getPreviewSize()`, `isFlipHorizontal()`

Simple sequence:

```java
Camera.Size size = mCameraProxy.getPreviewSize();
mCurrentVideoResolution = new NvsVideoResolution();
mCurrentVideoResolution.imagePAR = new NvsRational(1, 1);
```

## `capture-recording-016` `startCapturePreview`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:602`

API classes: `NvsRational`

Simple sequence:

```java
if (ratioType == NvAsset.AspectRatio_9v16) {
nvsRational = new NvsRational(9, 16);
nvsRational = new NvsRational(9, 21);
nvsRational = new NvsRational(16, 9);
nvsRational = new NvsRational(21, 9);
```

## `capture-recording-017` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:285`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `capture-recording-018` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/view/ThemeCapturePreviewView.java:290`

API classes: `NvsTimeline`
Common calls: `getDuration()`

Simple sequence:

```java
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
playTimeline(nvsTimeline, 0, nvsTimeline.getDuration());
```

## `capture-recording-019` `seekTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:275`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_SOFTWARE_VIDEO_INTRA_FRAME_ONLY_FAST_STOP`
Common calls: `getStreamingEngineState()`, `stop()`

Simple sequence:

```java
if (mNvsTimeline != null && mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mStreamingContext.stop(NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_SOFTWARE_VIDEO_INTRA_FRAME_ONLY_FAST_STOP);
```
