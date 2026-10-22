# Demo Simple Snippets - Timeline Editing

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: timeline/video/audio track creation, clip append/insert/remove/split, timeline data binding, clip transforms, timeline mutation, and edit-state reconstruction.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [timeline-editing-001 initTimeline](#timeline-editing-001-inittimeline)
- [timeline-editing-002 onStreamingEngineStateChanged](#timeline-editing-002-onstreamingenginestatechanged)
- [timeline-editing-003 rebuildTimelineStructure](#timeline-editing-003-rebuildtimelinestructure)
- [timeline-editing-004 localVideoTrim](#timeline-editing-004-localvideotrim)
- [timeline-editing-005 muteVideoTrack](#timeline-editing-005-mutevideotrack)
- [timeline-editing-006 muteVideoTrack](#timeline-editing-006-mutevideotrack)
- [timeline-editing-007 setPanAndScan](#timeline-editing-007-setpanandscan)
- [timeline-editing-008 getClipRange](#timeline-editing-008-getcliprange)
- [timeline-editing-009 splitClip](#timeline-editing-009-splitclip)
- [timeline-editing-010 initRootView](#timeline-editing-010-initrootview)
- [timeline-editing-011 playStopped](#timeline-editing-011-playstopped)
- [timeline-editing-012 rotateClip](#timeline-editing-012-rotateclip)
- [timeline-editing-013 playStopped](#timeline-editing-013-playstopped)
- [timeline-editing-014 initListener](#timeline-editing-014-initlistener)
- [timeline-editing-015 initListener](#timeline-editing-015-initlistener)
- [timeline-editing-016 playStopped](#timeline-editing-016-playstopped)
- [timeline-editing-017 getClipDuration](#timeline-editing-017-getclipduration)
- [timeline-editing-018 getClipStartTime](#timeline-editing-018-getclipstarttime)
- [timeline-editing-019 getClipEndTime](#timeline-editing-019-getclipendtime)
- [timeline-editing-020 onBindViewHolder](#timeline-editing-020-onbindviewholder)
- [timeline-editing-021 onBindViewHolder](#timeline-editing-021-onbindviewholder)
- [timeline-editing-022 setTimeline](#timeline-editing-022-settimeline)
- [timeline-editing-023 onClick](#timeline-editing-023-onclick)
- [timeline-editing-024 playStopped](#timeline-editing-024-playstopped)
- [timeline-editing-025 removeTimeline](#timeline-editing-025-removetimeline)
- [timeline-editing-026 updateOpenMoveButton](#timeline-editing-026-updateopenmovebutton)
- [timeline-editing-027 setVideoFragmentCallBack](#timeline-editing-027-setvideofragmentcallback)
- [timeline-editing-028 playStopped](#timeline-editing-028-playstopped)
- [timeline-editing-029 removeTimeline](#timeline-editing-029-removetimeline)
- [timeline-editing-030 playStopped](#timeline-editing-030-playstopped)
- [timeline-editing-031 playStopped](#timeline-editing-031-playstopped)
- [timeline-editing-032 playStopped](#timeline-editing-032-playstopped)
- [timeline-editing-033 onClick](#timeline-editing-033-onclick)
- [timeline-editing-034 playStopped](#timeline-editing-034-playstopped)
- [timeline-editing-035 playStopped](#timeline-editing-035-playstopped)
- [timeline-editing-036 initStreamingContext](#timeline-editing-036-initstreamingcontext)
- [timeline-editing-037 playStopped](#timeline-editing-037-playstopped)
- [timeline-editing-038 onTouch](#timeline-editing-038-ontouch)
- [timeline-editing-039 setCallbackEnable](#timeline-editing-039-setcallbackenable)
- [timeline-editing-040 initListener](#timeline-editing-040-initlistener)
- [timeline-editing-041 onStreamingEngineStateChanged](#timeline-editing-041-onstreamingenginestatechanged)
- [timeline-editing-042 initStreamingContext](#timeline-editing-042-initstreamingcontext)
- [timeline-editing-043 createTimeline](#timeline-editing-043-createtimeline)
- [timeline-editing-044 createSingleClipTimeline](#timeline-editing-044-createsinglecliptimeline)
- [timeline-editing-045 createSingleClipTimelineExt](#timeline-editing-045-createsinglecliptimelineext)
- [timeline-editing-046 removeTimeline](#timeline-editing-046-removetimeline)
- [timeline-editing-047 buildVideoTrack](#timeline-editing-047-buildvideotrack)
- [timeline-editing-048 buildTimelineAnimation](#timeline-editing-048-buildtimelineanimation)
- [timeline-editing-049 setVideoResolution](#timeline-editing-049-setvideoresolution)
- [timeline-editing-050 getVideoResolution](#timeline-editing-050-getvideoresolution)
- [timeline-editing-051 connectTimeline](#timeline-editing-051-connecttimeline)
- [timeline-editing-052 createTimeline](#timeline-editing-052-createtimeline)
- [timeline-editing-053 getCurrentTimeline](#timeline-editing-053-getcurrenttimeline)
- [timeline-editing-054 getEditType](#timeline-editing-054-getedittype)
- [timeline-editing-055 handleCutClip](#timeline-editing-055-handlecutclip)
- [timeline-editing-056 checkVideoResolution](#timeline-editing-056-checkvideoresolution)
- [timeline-editing-057 checkVideoResolution](#timeline-editing-057-checkvideoresolution)
- [timeline-editing-058 checkVideoResolution](#timeline-editing-058-checkvideoresolution)
- [timeline-editing-059 checkVideoResolution](#timeline-editing-059-checkvideoresolution)
- [timeline-editing-060 onHandActionUp](#timeline-editing-060-onhandactionup)
- [timeline-editing-061 onChangeTrimTimelineObject](#timeline-editing-061-onchangetrimtimelineobject)
- [timeline-editing-062 getPipVideoClipIndex](#timeline-editing-062-getpipvideoclipindex)
- [timeline-editing-063 getPipVideoClipIndex](#timeline-editing-063-getpipvideoclipindex)
- [timeline-editing-064 frameForTimeline](#timeline-editing-064-framefortimeline)
- [timeline-editing-065 isMute](#timeline-editing-065-ismute)
- [timeline-editing-066 setCoverImagePath](#timeline-editing-066-setcoverimagepath)
- [timeline-editing-067 getVideoResolution](#timeline-editing-067-getvideoresolution)
- [timeline-editing-068 getNvsRational](#timeline-editing-068-getnvsrational)
- [timeline-editing-069 getPipTrackMaxDuration](#timeline-editing-069-getpiptrackmaxduration)
- [timeline-editing-070 getCustomHeight](#timeline-editing-070-getcustomheight)
- [timeline-editing-071 getCustomHeight](#timeline-editing-071-getcustomheight)
- [timeline-editing-072 changeAllBaseItemInpoint](#timeline-editing-072-changeallbaseiteminpoint)
- [timeline-editing-073 changeAllBaseItemInpoint](#timeline-editing-073-changeallbaseiteminpoint)
- [timeline-editing-074 getNvsTimeline](#timeline-editing-074-getnvstimeline)
- [timeline-editing-075 setNvsTimeline](#timeline-editing-075-setnvstimeline)
- [timeline-editing-076 setAuxiliaryTimeline](#timeline-editing-076-setauxiliarytimeline)
- [timeline-editing-077 getAuxiliaryTimeline](#timeline-editing-077-getauxiliarytimeline)
- [timeline-editing-078 isPlaceHolder](#timeline-editing-078-isplaceholder)
- [timeline-editing-079 getVideoClipByIndex](#timeline-editing-079-getvideoclipbyindex)
- [timeline-editing-080 getTimelineWidthAndHeight](#timeline-editing-080-gettimelinewidthandheight)
- [timeline-editing-081 setCoverImagePath](#timeline-editing-081-setcoverimagepath)
- [timeline-editing-082 getVideoResolution](#timeline-editing-082-getvideoresolution)
- [timeline-editing-083 getNvsRational](#timeline-editing-083-getnvsrational)
- [timeline-editing-084 createTimeline](#timeline-editing-084-createtimeline)
- [timeline-editing-085 buildVideoTrack](#timeline-editing-085-buildvideotrack)
- [timeline-editing-086 newTimeline](#timeline-editing-086-newtimeline)
- [timeline-editing-087 alignedResolution](#timeline-editing-087-alignedresolution)
- [timeline-editing-088 rebuildTimeline](#timeline-editing-088-rebuildtimeline)
<!-- END GENERATED CONTENTS -->

## `timeline-editing-001` `initTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:140`

API classes: `NvsVideoTrack`
Common calls: `e()`, `createTimeline()`, `getVideoTrackByIndex()`, `setVolumeGain()`, `playVideo()`, `getDuration()`

Simple sequence:

```java
mTimeline = NvBoomErang.createTimeline(mRecordVideoPath);
if (mTimeline == null) {
Log.e(TAG, "initTimeline： timeline buildFx failed");
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
videoTrack.setVolumeGain(0, 0);
mLiveWindow.playVideo(mTimeline);
Log.e(TAG, "initTimeline： timeline duration: " + mTimeline.getDuration());
```

## `timeline-editing-002` `onStreamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:144`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
```

## `timeline-editing-003` `rebuildTimelineStructure`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1564`

API classes: `NvsVideoClip`
Common calls: `getDuration()`, `e()`, `size()`, `get()`, `removeAllClips()`, `getReverseClipList()`, `setSoftWareDecoding()`, `getIsConvertSuccess()`, `getClipList()`, `removeRange()`

Simple sequence:

```java
videoTrack.removeAllClips();
if (fxMode == TIMELINE_FX_MODE_REVERSE) {
ArrayList<RecordClip> videoClipArray = clipsInfo.getReverseClipList();
NvsVideoClip videoClip = appendClip(videoTrack, clipInfo, needRotate);
if (videoClip != null) {
if (!clipInfo.getIsConvertSuccess()) {
Logger.e(TAG, "TimeLine Duratoin REVERSE -->" + mTimeline.getDuration());
ArrayList<RecordClip> videoClipArray = clipsInfo.getClipList();
NvsVideoClip videoClip = appendClip(videoTrack, clipInfo, needRotate);
Logger.e(TAG, "TimeLine Duratoin Normal timelineFx -->" + mTimeline.getDuration());
if (videoTrack != null && videoTrack.getDuration() > MAXTIME) {
videoTrack.removeRange(MAXTIME, videoTrack.getDuration(), false);
```

## `timeline-editing-004` `localVideoTrim`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1648`

API classes: `NvsVideoClip`
Common calls: `isCaptureVideo()`, `changeTrimInPoint()`, `getTrimIn()`, `changeTrimOutPoint()`, `getTrimOut()`

Simple sequence:

```java
private void localVideoTrim(NvsVideoClip videoClip, RecordClip clipInfo) {
videoClip.changeTrimInPoint(clipInfo.getTrimIn(), true);
videoClip.changeTrimOutPoint(clipInfo.getTrimOut(), true);
```

## `timeline-editing-005` `muteVideoTrack`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1924`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `setVolumeGain()`

Simple sequence:

```java
public boolean muteVideoTrack(NvsVideoTrack videoTrack) {
for (int i = 0; i < videoTrack.getClipCount(); i++) {
NvsVideoClip clip = videoTrack.getClipByIndex(i);
if (clip != null)
clip.setVolumeGain(0, 0);
```

## `timeline-editing-006` `muteVideoTrack`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1928`

API classes: `NvsVideoClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `setVolumeGain()`

Simple sequence:

```java
for (int i = 0; i < videoTrack.getClipCount(); i++) {
NvsVideoClip clip = videoTrack.getClipByIndex(i);
if (clip != null)
clip.setVolumeGain(0, 0);
```

## `timeline-editing-007` `setPanAndScan`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1941`

API classes: `NvsVideoClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `setPanAndScan()`

Simple sequence:

```java
for (int i = 0; i < videoTrack.getClipCount(); i++) {
NvsVideoClip clip = videoTrack.getClipByIndex(i);
if (clip != null)
clip.setPanAndScan(0, 1);
```

## `timeline-editing-008` `getClipRange`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1953`

API classes: `NvsVideoClip`
Common calls: `getClipByTimelinePosition()`, `getOutPoint()`, `add()`

Simple sequence:

```java
while (ptIndex < (point + duration)) {
NvsVideoClip clip = videoTrack.getClipByTimelinePosition(ptIndex);
ptIndex = clip.getOutPoint();
```

## `timeline-editing-009` `splitClip`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1972`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getClipByTimelinePosition()`, `getInPoint()`, `splitClip()`, `getIndex()`

Simple sequence:

```java
public boolean splitClip(long point, NvsVideoTrack videoTrack) {
NvsVideoClip splitClip = videoTrack.getClipByTimelinePosition(point);
if (splitClip.getInPoint() != point) {
boolean flag = videoTrack.splitClip(splitClip.getIndex(), point);
```

## `timeline-editing-010` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:112`

API classes: `NvsTimelineEditor`

Simple sequence:

```java
mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.timelineEditor);
```

## `timeline-editing-011` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:198`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `timeline-editing-012` `rotateClip`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:372`

API classes: `NvsVideoClip`
Static/constants: `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0`, `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90`, `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180`, `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270`
Common calls: `setExtraVideoRotation()`

Simple sequence:

```java
switch (rotateAngle) {
case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0:
mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90);
case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90:
mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180);
case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180:
mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270);
case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270:
mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0);
```

## `timeline-editing-013` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:351`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `timeline-editing-014` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:140`

API classes: `NvsTimeline`
Common calls: `setVideoFragmentCallBack()`, `VideoFragmentListener()`, `setDrawRectVisible()`

Simple sequence:

```java
mVideoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `timeline-editing-015` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:142`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playBackEOF(NvsTimeline timeline) {
```

## `timeline-editing-016` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:150`

API classes: `NvsTimeline`
Common calls: `setDrawRectVisible()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `timeline-editing-017` `getClipDuration`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:626`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `i()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getInPoint()`, `getOutPoint()`

Simple sequence:

```java
NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(0);
if (nvsVideoTrack == null) {
Log.i(TAG, "timeline get video track is null");
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(mSelectedClipPosition);
if (nvsVideoClip == null) {
Log.i(TAG, "timeline get video clip is null");
long clipInPoint = nvsVideoClip.getInPoint();
long clipOutPoint = nvsVideoClip.getOutPoint();
```

## `timeline-editing-018` `getClipStartTime`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:649`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `i()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getInPoint()`

Simple sequence:

```java
NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(0);
if (nvsVideoTrack == null) {
Log.i(TAG, "timeline get video track is null");
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(mSelectedClipPosition);
if (nvsVideoClip == null) {
Log.i(TAG, "timeline get video clip is null");
long clipInPoint = nvsVideoClip.getInPoint();
```

## `timeline-editing-019` `getClipEndTime`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:671`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `i()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getOutPoint()`

Simple sequence:

```java
NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(0);
if (nvsVideoTrack == null) {
Log.i(TAG, "timeline get video track is null");
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(mSelectedClipPosition);
if (nvsVideoClip == null) {
Log.i(TAG, "timeline get video clip is null");
long clipOutPoint = nvsVideoClip.getOutPoint();
```

## `timeline-editing-020` `onBindViewHolder`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationClipAdapter.java:111`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `getInPoint()`, `getOutPoint()`, `setText()`

Simple sequence:

```java
if(null != mTimeline){
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
if(null != videoTrack){
NvsVideoClip clip =videoTrack .getClipByIndex(position);
if(null != clip){
long clipInPoint = clip.getInPoint();
long clipOutPoint = clip.getOutPoint();
holder.item_assetName.setText((currentItemDuration / 1000000)+"s");
```

## `timeline-editing-021` `onBindViewHolder`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationClipAdapter.java:113`

API classes: `NvsVideoClip`
Common calls: `getClipByIndex()`, `getInPoint()`, `getOutPoint()`, `setText()`

Simple sequence:

```java
if(null != videoTrack){
NvsVideoClip clip =videoTrack .getClipByIndex(position);
if(null != clip){
long clipInPoint = clip.getInPoint();
long clipOutPoint = clip.getOutPoint();
holder.item_assetName.setText((currentItemDuration / 1000000)+"s");
```

## `timeline-editing-022` `setTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:272`

API classes: `NvsTimeline`

Simple sequence:

```java
public void setTimeline(NvsTimeline timeline) {
this.mTimeline = timeline;
```

## `timeline-editing-023` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:177`

API classes: `NvsTimelineEditor`
Static/constants: `NvsTimelineEditor.OnScrollChangeListener`
Common calls: `formatUsToString2()`, `setOnScrollListener()`, `OnScrollChangeListener()`, `updateCurPlayTime()`, `setText()`, `getDuration()`

Simple sequence:

```java
mTimelineEditor.setOnScrollListener(new NvsTimelineEditor.OnScrollChangeListener() {
if (null != mTimeline) {
tvCurTime.setText(TimeFormatUtil.formatUsToString2(timeStamp) + "/" + TimeFormatUtil.formatUsToString2(mTimeline.getDuration()));
```

## `timeline-editing-024` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:300`

API classes: `NvsTimeline`
Common calls: `d()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `timeline-editing-025` `removeTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/DurationActivity.java:132`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `changeTrimOutPoint()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
videoClip.changeTrimOutPoint(trimOut,true);
```

## `timeline-editing-026` `updateOpenMoveButton`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:322`

API classes: `NvsVideoClip`
Common calls: `setImgSize()`, `setDrawRect()`, `setCurMakeRatio()`, `setOnDrawRectListener()`, `OnDrawRectListener()`, `getString()`, `getStartROI()`, `getEndROI()`, `instance()`, `getMakeRatio()`

Simple sequence:

```java
NvsVideoClip videoClip = getVideoClip();
RectF startROI = videoClip.getStartROI();
RectF endROI = videoClip.getEndROI();
int makeRatio = TimelineData.instance().getMakeRatio();
mAreaStartDrawROI.setCurMakeRatio(makeRatio);
mAreaStartDrawROI.setImgSize(mImageViewWidth, mImageViewHeight);
String startRect = getResources().getString(R.string.start_rect);
mAreaStartDrawROI.setDrawRect(startRect, Constants.EDIT_MODE_PHOTO_AREA_DISPLAY);
mAreaStartDrawROI.setOnDrawRectListener(new PhotoDrawRect.OnDrawRectListener() {
mAreaEndDrawROI.setCurMakeRatio(makeRatio);
mAreaEndDrawROI.setImgSize(mImageViewWidth, mImageViewHeight);
String endRect = getResources().getString(R.string.end_rect);
mAreaEndDrawROI.setDrawRect(endRect, Constants.EDIT_MODE_PHOTO_AREA_DISPLAY);
mAreaEndDrawROI.setOnDrawRectListener(new PhotoDrawRect.OnDrawRectListener() {
mCloseMoveDrawROI.setCurMakeRatio(makeRatio);
mCloseMoveDrawROI.setImgSize(mImageViewWidth, mImageViewHeight);
mCloseMoveDrawROI.setDrawRect("", Constants.EDIT_MODE_PHOTO_AREA_DISPLAY);
mCloseMoveDrawROI.setOnDrawRectListener(new PhotoDrawRect.OnDrawRectListener() {
mTotalDrawROI.setImgSize(mImageViewWidth, mImageViewHeight);
mTotalDrawROI.setDrawRect("", Constants.EDIT_MODE_PHOTO_TOTAL_DISPLAY);
```

## `timeline-editing-027` `setVideoFragmentCallBack`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:170`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {}
```

## `timeline-editing-028` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:173`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {}
```

## `timeline-editing-029` `removeTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:209`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getTrimIn()`, `getTrimOut()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `changeTrimIn()`, `changeTrimOut()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
long trimIn = mClipInfo.getTrimIn();
if(trimIn < 0)
mClipInfo.changeTrimIn(videoClip.getTrimIn());
long trimOut = mClipInfo.getTrimOut();
if(trimOut < 0)
mClipInfo.changeTrimOut(videoClip.getTrimOut());
```

## `timeline-editing-030` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:780`

API classes: `NvsTimeline`
Common calls: `d()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `timeline-editing-031` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:160`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `timeline-editing-032` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:290`

API classes: `NvsTimeline`
Common calls: `round()`, `getDuration()`, `getSequenceWidth()`, `smoothScrollTo()`, `updateRecordView()`, `setEnabled()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (m_sequenceView != null) {
int x = Math.round((stamp / (float) m_timeLine.getDuration() * m_sequenceView.getSequenceWidth()));
if (stamp - m_curRecordInPoint >= m_minRecordDuration) {
m_recordStopBtn.setEnabled(true);
```

## `timeline-editing-033` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:131`

API classes: `NvsTimeline`
Common calls: `setVideoFragmentCallBack()`, `VideoFragmentListener()`, `setDrawRectVisible()`

Simple sequence:

```java
mVideoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `timeline-editing-034` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:142`

API classes: `NvsTimeline`
Common calls: `setDrawRectVisible()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `timeline-editing-035` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:146`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `timeline-editing-036` `initStreamingContext`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:892`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
```

## `timeline-editing-037` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:184`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `timeline-editing-038` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:110`

API classes: `NvsVideoTrack`
Common calls: `setVisibility()`, `setOnClickListener()`, `OnClickListener()`, `getVideoTrackByIndex()`, `removeClip()`, `setImageBitmap()`

Simple sequence:

```java
iv_head_delete.setOnClickListener(new View.OnClickListener() {
if (mTimeline != null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
if (videoTrack != null) {
if (videoTrack.removeClip(0, false)) {
tvHead.setVisibility(View.VISIBLE);
ivHead.setImageBitmap(null);
iv_head_delete.setVisibility(View.GONE);
```

## `timeline-editing-039` `setCallbackEnable`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:207`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
```

## `timeline-editing-040` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:106`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
```

## `timeline-editing-041` `onStreamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:645`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
```

## `timeline-editing-042` `initStreamingContext`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:120`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.init`, `NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT`, `NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED`, `NvsStreamingContext.STREAMING_CONTEXT_FLAG_NEED_GIF_MOTION`, `NvsStreamingContext.STREAMING_CONTEXT_FLAG_INTERRUPT_STOP_FOR_INTERNAL_STOP`
Common calls: `init()`

Simple sequence:

```java
public static NvsStreamingContext initStreamingContext(Context mContext, String licensePath) {
return NvsStreamingContext.init(mContext, licensePath, NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT
| NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED
| NvsStreamingContext.STREAMING_CONTEXT_FLAG_NEED_GIF_MOTION
| NvsStreamingContext.STREAMING_CONTEXT_FLAG_INTERRUPT_STOP_FOR_INTERNAL_STOP);
```

## `timeline-editing-043` `createTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:138`

API classes: `NvsTimeline`

Simple sequence:

```java
public static NvsTimeline createTimeline() {
```

## `timeline-editing-044` `createSingleClipTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:178`

API classes: `NvsTimeline`
Common calls: `instance()`, `getVideoResolution()`, `e()`

Simple sequence:

```java
public static NvsTimeline createSingleClipTimeline(ClipInfo clipInfo, boolean isTrimClip) {
NvsTimeline timeline = newTimeline(TimelineData.instance().getVideoResolution());
if (timeline == null) {
Log.e(TAG, "failed to create timeline");
buildSingleClipVideoTrack(timeline, clipInfo, isTrimClip);
return timeline;
```

## `timeline-editing-045` `createSingleClipTimelineExt`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:192`

API classes: `NvsTimeline`, `NvsVideoResolution`
Common calls: `e()`

Simple sequence:

```java
public static NvsTimeline createSingleClipTimelineExt(NvsVideoResolution videoEditRes, String filePath) {
NvsTimeline timeline = newTimeline(videoEditRes);
if (timeline == null) {
Log.e(TAG, "failed to create timeline");
buildSingleClipVideoTrackExt(timeline, filePath);
return timeline;
```

## `timeline-editing-046` `removeTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:321`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `removeTimeline()`

Simple sequence:

```java
public static boolean removeTimeline(NvsTimeline timeline) {
if (timeline == null) {
NvsStreamingContext context = NvsStreamingContext.getInstance();
return context.removeTimeline(timeline);
```

## `timeline-editing-047` `buildVideoTrack`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:341`

API classes: `NvsTimeline`, `NvsVideoTrack`
Common calls: `instance()`, `appendVideoTrack()`, `e()`, `getClipInfoData()`, `size()`, `get()`, `getVideoRes()`, `getOriginVideoVolume()`, `setVolumeGain()`

Simple sequence:

```java
public static boolean buildVideoTrack(NvsTimeline timeline) {
if (timeline == null) {
NvsVideoTrack videoTrack = timeline.appendVideoTrack();
ArrayList<ClipInfo> videoClipArray = TimelineData.instance().getClipInfoData();
addVideoClip(videoTrack, clipInfo, true, timeline.getVideoRes());
float videoVolume = TimelineData.instance().getOriginVideoVolume();
videoTrack.setVolumeGain(videoVolume, videoVolume);
```

## `timeline-editing-048` `buildTimelineAnimation`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1897`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `i()`, `size()`, `getClipByIndex()`, `get()`, `getAnimationInfo()`

Simple sequence:

```java
public static void buildTimelineAnimation(NvsTimeline mTimeline, ArrayList<ClipInfo> clipInfoArrayList) {
if (null == clipInfoArrayList || null == mTimeline) {
NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(0);
if (nvsVideoTrack == null) {
Log.i(TAG, "timeline get video track is null");
for (int i = 0; i < clipInfoArrayList.size(); i++) {
NvsVideoClip videoClip = nvsVideoTrack.getClipByIndex(i);
applyAnimation(nvsVideoTrack, videoClip, clipInfo.getAnimationInfo());
```

## `timeline-editing-049` `setVideoResolution`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:164`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public NvsVideoResolution getVideoResolution() {
```

## `timeline-editing-050` `getVideoResolution`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:168`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public NvsVideoResolution cloneVideoResolution() {
NvsVideoResolution resolution = new NvsVideoResolution();
```

## `timeline-editing-051` `connectTimeline`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:115`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
```

## `timeline-editing-052` `createTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:204`

API classes: `NvsTimeline`
Common calls: `createTimeline()`

Simple sequence:

```java
public NvsTimeline createTimeline() {
mTimeline = TimelineUtil.createTimeline();
return mTimeline;
```

## `timeline-editing-053` `getCurrentTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:237`

API classes: `NvsTimeline`

Simple sequence:

```java
public NvsTimeline getCurrentTimeline() {
if (mTimeline == null) {
return mTimeline;
```

## `timeline-editing-054` `getEditType`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:263`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `isEmpty()`, `get()`, `getInstance()`, `getMeicamVideoTrackList()`, `isIndexAvailable()`, `getClipInfoList()`, `getObject()`, `e()`, `getClipByTimelinePosition()`, `getIndex()`, `size()`, `getInPoint()`

Simple sequence:

```java
List<MeicamVideoTrack> videoTrackList = TimelineData.getInstance().getMeicamVideoTrackList();
List<ClipInfo<?>> clipInfoList = meicamVideoTrack.getClipInfoList();
NvsVideoTrack object = meicamVideoTrack.getObject();
if (object == null) {
LogUtils.e("NvsVideoTrack is null");
NvsVideoClip videoClip = object.getClipByTimelinePosition(timeStamp);
int index = videoClip.getIndex();
if (clipInfo.getInPoint() <= timeStamp && clipInfo.getOutPoint() > timeStamp) {
```

## `timeline-editing-055` `handleCutClip`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:305`

API classes: `NvsVideoClip`
Common calls: `setTrimOut()`, `getIndex()`, `size()`, `getInPoint()`, `getOutPoint()`, `getTrimIn()`, `clone()`, `setTrimIn()`, `setInPoint()`, `add()`, `getObject()`, `getVideoClipsInTrackIndex()`

Simple sequence:

```java
NvsVideoClip editVideoClip = clipInfo.getObject();
if (isPip) {
List<ClipInfo<?>> videoClipsInTrackIndex = TimelineDataUtil.getVideoClipsInTrackIndex(trackIndex);
int index = editVideoClip.getIndex();
long inPoint = editVideoClip.getInPoint();//当前Clip的入点 The entry point of the current Clip
long outPoint = editVideoClip.getOutPoint();//当前Clip的出点 The outgoing point of the current Clip
long trimOut = timeStamp - inPoint + clipInfo.getTrimIn();
clipInfo.setTrimOut(trimOut);
newClip.setTrimIn(trimOut);
newClip.setTrimOut(newTrimOut);
newClip.setInPoint(timeStamp);
List<ClipInfo<?>> clipInfos = TimelineDataUtil.getMainTrackVideoClip();
int index = editVideoClip.getIndex();
long inPoint = editVideoClip.getInPoint();//当前Clip的入点 The entry point of the current Clip
long outPoint = editVideoClip.getOutPoint();//当前Clip的出点 The outgoing point of the current Clip
long trimOut = timeStamp - inPoint + clipInfo.getTrimIn();
clipInfo.setTrimOut(trimOut);
clipInfo.setOutPoint(timeStamp);
newClip.setTrimIn(trimOut);
newClip.setTrimOut(newTrimOut);
newClip.setInPoint(timeStamp);
```

## `timeline-editing-056` `checkVideoResolution`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:542`

API classes: `NvsVideoResolution`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getInstance()`, `getVideoResolution()`, `getVideoRes()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getVideoEditResolutionByClip()`, `getFilePath()`, `setVideoResolution()`

Simple sequence:

```java
if (TimelineData.getInstance().getVideoResolution() == null) {
if (mTimeline != null) {
NvsVideoResolution videoRes = mTimeline.getVideoRes();
if (videoRes == null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
if (videoTrack != null) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
if (videoClip != null) {
videoRes = TimelineUtil.getVideoEditResolutionByClip(videoClip.getFilePath());
TimelineData.getInstance().setVideoResolution(videoRes);
```

## `timeline-editing-057` `checkVideoResolution`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:543`

API classes: `NvsVideoResolution`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getInstance()`, `getVideoResolution()`, `getVideoRes()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getVideoEditResolutionByClip()`, `getFilePath()`, `setVideoResolution()`

Simple sequence:

```java
if (TimelineData.getInstance().getVideoResolution() == null) {
if (mTimeline != null) {
NvsVideoResolution videoRes = mTimeline.getVideoRes();
if (videoRes == null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
if (videoTrack != null) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
if (videoClip != null) {
videoRes = TimelineUtil.getVideoEditResolutionByClip(videoClip.getFilePath());
TimelineData.getInstance().setVideoResolution(videoRes);
```

## `timeline-editing-058` `checkVideoResolution`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:544`

API classes: `NvsVideoResolution`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoRes()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getVideoEditResolutionByClip()`, `getFilePath()`, `getInstance()`, `setVideoResolution()`

Simple sequence:

```java
if (mTimeline != null) {
NvsVideoResolution videoRes = mTimeline.getVideoRes();
if (videoRes == null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
if (videoTrack != null) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
if (videoClip != null) {
videoRes = TimelineUtil.getVideoEditResolutionByClip(videoClip.getFilePath());
TimelineData.getInstance().setVideoResolution(videoRes);
```

## `timeline-editing-059` `checkVideoResolution`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:546`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `getVideoEditResolutionByClip()`, `getFilePath()`

Simple sequence:

```java
if (videoRes == null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
if (videoTrack != null) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
if (videoClip != null) {
videoRes = TimelineUtil.getVideoEditResolutionByClip(videoClip.getFilePath());
```

## `timeline-editing-060` `onHandActionUp`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:794`

API classes: `NvsVideoClip`, `NvsVideoTrack`
Static/constants: `NvsVideoClip.VIDEO_CLIP_TYPE_AV`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `getTrimOut()`, `getVideoType()`, `getTrimIn()`

Simple sequence:

```java
if (mTimeline == null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
long trimPoint = videoClip.getTrimOut();
if (videoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV && isLeftHand) {
trimPoint = videoClip.getTrimIn();
```

## `timeline-editing-061` `onChangeTrimTimelineObject`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:820`

API classes: `NvsVideoClip`, `NvsVideoTrack`
Static/constants: `NvsVideoClip.VIDEO_CLIP_TYPE_AV`
Common calls: `getObject()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getVideoType()`, `getMainTrackVideoClip()`, `size()`, `get()`, `e()`, `setInPoint()`, `getInPoint()`, `setOutPoint()`, `getOutPoint()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
if (isLeftHand && videoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {
List<ClipInfo<?>> mainTrackVideoClip = TimelineDataUtil.getMainTrackVideoClip();
if ((clip == null) || (clip.getObject() == null)) {
NvsVideoClip nvsVideoClip = clip.getObject();
clip.setInPoint(nvsVideoClip.getInPoint());
clip.setOutPoint(nvsVideoClip.getOutPoint());
```

## `timeline-editing-062` `getPipVideoClipIndex`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1399`

API classes: `NvsVideoClip`, `NvsVideoTrack`
Common calls: `getOutPoint()`, `size()`, `get()`, `getInPoint()`, `getInstance()`, `getMeicamVideoTrackList()`, `getIndex()`, `getObject()`, `getClipByTimelinePosition()`, `getClipByIndex()`, `getClipCount()`, `getClipInfoList()`

Simple sequence:

```java
List<MeicamVideoTrack> meicamVideoTrackList = TimelineData.getInstance().getMeicamVideoTrackList();
for (MeicamVideoTrack meicamVideoTrack : meicamVideoTrackList) {
int nowTrackIndex = meicamVideoTrack.getIndex();
List<ClipInfo<?>> clipInfoList = meicamVideoTrack.getClipInfoList();
long nowInpoint = nowClipInfo.getInPoint();
long nowOutpoint = nowClipInfo.getOutPoint();
beforeOutpoint = beforeClipInfo.getOutPoint();
afterInPoint = afterClipInfo.getInPoint();
```

## `timeline-editing-063` `getPipVideoClipIndex`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1401`

API classes: `NvsVideoClip`, `NvsVideoTrack`
Common calls: `getOutPoint()`, `get()`, `size()`, `getInPoint()`, `getIndex()`, `getObject()`, `getClipByTimelinePosition()`, `getClipByIndex()`, `getClipCount()`, `getClipInfoList()`, `isEmpty()`

Simple sequence:

```java
for (MeicamVideoTrack meicamVideoTrack : meicamVideoTrackList) {
int nowTrackIndex = meicamVideoTrack.getIndex();
List<ClipInfo<?>> clipInfoList = meicamVideoTrack.getClipInfoList();
long nowInpoint = nowClipInfo.getInPoint();
long nowOutpoint = nowClipInfo.getOutPoint();
beforeOutpoint = beforeClipInfo.getOutPoint();
afterInPoint = afterClipInfo.getInPoint();
```

## `timeline-editing-064` `frameForTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:3055`

API classes: `NvsVideoResolution`
Common calls: `getInstance()`, `getVideoResolution()`

Simple sequence:

```java
NvsVideoResolution videoResolution = TimelineData.getInstance().getVideoResolution();
```

## `timeline-editing-065` `isMute`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoTrack.java:41`

API classes: `NvsVideoTrack`
Common calls: `setVolumeGain()`

Simple sequence:

```java
NvsVideoTrack object = getObject();
if (isMute) {
object.setVolumeGain(0, 0);
object.setVolumeGain(1, 1);
```

## `timeline-editing-066` `setCoverImagePath`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:300`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public NvsVideoResolution getVideoResolution() {
```

## `timeline-editing-067` `getVideoResolution`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:304`

API classes: `NvsVideoResolution`
Common calls: `alignedResolution()`

Simple sequence:

```java
public void setVideoResolution(NvsVideoResolution mVideoResolution) {
```

## `timeline-editing-068` `getNvsRational`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineData.java:344`

API classes: `NvsRational`

Simple sequence:

```java
public void setNvsRational(NvsRational nvsRational) {
```

## `timeline-editing-069` `getPipTrackMaxDuration`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:496`

API classes: `NvsVideoTrack`
Common calls: `size()`, `get()`, `getObject()`, `getDuration()`, `max()`

Simple sequence:

```java
NvsVideoTrack nvsVideoTrack = videoTrack.getObject();
if (nvsVideoTrack != null) {
long trackDuration = nvsVideoTrack.getDuration();
```

## `timeline-editing-070` `getCustomHeight`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1034`

API classes: `NvsVideoResolution`
Common calls: `getInstance()`, `getVideoResolution()`, `round()`

Simple sequence:

```java
if (ratio == 0) {
NvsVideoResolution videoResolution = TimelineData.getInstance().getVideoResolution();
```

## `timeline-editing-071` `getCustomHeight`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1036`

API classes: `NvsVideoResolution`
Common calls: `getInstance()`, `getVideoResolution()`, `round()`

Simple sequence:

```java
if (ratio == 0) {
NvsVideoResolution videoResolution = TimelineData.getInstance().getVideoResolution();
```

## `timeline-editing-072` `changeAllBaseItemInpoint`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1203`

API classes: `NvsVideoClip`
Common calls: `e()`, `getInPoint()`, `getOutPoint()`, `setInPoint()`, `setOutPoint()`, `getObject()`, `changeTrimInPoint()`, `changeTrimOutPoint()`

Simple sequence:

```java
for (ClipInfo infoPip : clipInfoPip) {
long inPoint = infoPip.getInPoint();
long outPoint = infoPip.getOutPoint();
infoPip.setInPoint(inPoint);
infoPip.setOutPoint(outPoint);
NvsVideoClip nvsVideoClip = (NvsVideoClip) infoPip.getObject();
nvsVideoClip.changeTrimInPoint(inPoint, false);
nvsVideoClip.changeTrimOutPoint(outPoint, false);
```

## `timeline-editing-073` `changeAllBaseItemInpoint`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1207`

API classes: `NvsVideoClip`
Common calls: `getInPoint()`, `getOutPoint()`, `setInPoint()`, `setOutPoint()`, `getObject()`, `changeTrimInPoint()`, `changeTrimOutPoint()`

Simple sequence:

```java
for (ClipInfo infoPip : clipInfoPip) {
long inPoint = infoPip.getInPoint();
long outPoint = infoPip.getOutPoint();
infoPip.setInPoint(inPoint);
infoPip.setOutPoint(outPoint);
NvsVideoClip nvsVideoClip = (NvsVideoClip) infoPip.getObject();
nvsVideoClip.changeTrimInPoint(inPoint, false);
nvsVideoClip.changeTrimOutPoint(outPoint, false);
```

## `timeline-editing-074` `getNvsTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:111`

API classes: `NvsTimeline`

Simple sequence:

```java
public NvsTimeline getNvsTimeline() {
```

## `timeline-editing-075` `setNvsTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:121`

API classes: `NvsTimeline`

Simple sequence:

```java
public void setNvsTimeline(NvsTimeline nvsTimeline) {
```

## `timeline-editing-076` `setAuxiliaryTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:131`

API classes: `NvsTimeline`

Simple sequence:

```java
public void setAuxiliaryTimeline(NvsTimeline nvsTimeline) {
```

## `timeline-editing-077` `getAuxiliaryTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:140`

API classes: `NvsTimeline`

Simple sequence:

```java
public NvsTimeline getAuxiliaryTimeline() {
```

## `timeline-editing-078` `isPlaceHolder`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:830`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getFilePath()`, `e()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `endsWith()`

Simple sequence:

```java
if (mNvsTimeline == null) {
LogUtils.e("timeline is null!");
NvsVideoTrack videoTrack = mNvsTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
NvsVideoClip videoClip = videoTrack.getClipByIndex(clipIndex);
return videoClip != null && videoClip.getFilePath() != null && videoClip.getFilePath().endsWith(CommonData.IMAGE_BLACK_FILE_NAME);
```

## `timeline-editing-079` `getVideoClipByIndex`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1162`

API classes: `NvsVideoClip`, `NvsVideoTrack`
Common calls: `e()`, `videoTrackCount()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`

Simple sequence:

```java
public NvsVideoClip getVideoClipByIndex(int trackIndex, int clipIndex) {
NvsVideoTrack nvsVideoTrack = mNvsTimeline.getVideoTrackByIndex(trackIndex);
int clipCount = nvsVideoTrack.getClipCount();
return nvsVideoTrack.getClipByIndex(clipIndex);
```

## `timeline-editing-080` `getTimelineWidthAndHeight`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1305`

API classes: `NvsVideoResolution`
Common calls: `e()`, `getVideoRes()`

Simple sequence:

```java
NvsVideoResolution nvsVideoResolution = mNvsTimeline.getVideoRes();
```

## `timeline-editing-081` `setCoverImagePath`

Source: `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:238`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public NvsVideoResolution getVideoResolution() {
```

## `timeline-editing-082` `getVideoResolution`

Source: `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:242`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public void setVideoResolution(NvsVideoResolution mVideoResolution) {
```

## `timeline-editing-083` `getNvsRational`

Source: `libEngine/src/main/java/com/meishe/engine/local/LTimelineData.java:265`

API classes: `NvsRational`

Simple sequence:

```java
public void setNvsRational(NvsRational nvsRational) {
```

## `timeline-editing-084` `createTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:66`

API classes: `NvsTimeline`
Common calls: `getInstance()`, `getVideoResolution()`, `e()`

Simple sequence:

```java
public static NvsTimeline createTimeline() {
NvsTimeline timeline = newTimeline(TimelineData.getInstance().getVideoResolution());
if (timeline == null) {
LogUtils.e("failed to create timeline");
if (!buildVideoTrack(timeline)) {
return timeline;
setTimelineData(timeline);
return timeline;
```

## `timeline-editing-085` `buildVideoTrack`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:480`

API classes: `NvsTimeline`
Common calls: `getInstance()`, `getMeicamVideoTrackList()`, `isEmpty()`, `e()`

Simple sequence:

```java
private static boolean buildVideoTrack(NvsTimeline timeline) {
if (timeline == null) {
List<MeicamVideoTrack> videoTrackList = TimelineData.getInstance().getMeicamVideoTrackList();
return fillTrack(timeline, videoTrackList);
```

## `timeline-editing-086` `newTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:499`

API classes: `NvsTimeline`

Simple sequence:

```java
public static NvsTimeline newTimeline(String firstVideoPath) {
```

## `timeline-editing-087` `alignedResolution`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:550`

API classes: `NvsVideoResolution`
Common calls: `e()`

Simple sequence:

```java
public static void alignedResolution(NvsVideoResolution resolution) {
```

## `timeline-editing-088` `rebuildTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:578`

API classes: `NvsTimeline`, `NvsVideoResolution`
Common calls: `getInstance()`, `getVideoResolution()`, `changeVideoSize()`, `getMeicamVideoTrackList()`, `isEmpty()`, `e()`, `videoTrackCount()`, `removeVideoTrack()`

Simple sequence:

```java
public static void rebuildTimeline(NvsTimeline timeline) {
if (timeline == null) {
NvsVideoResolution videoResolution = TimelineData.getInstance().getVideoResolution();
if (videoResolution != null) {
timeline.changeVideoSize(videoResolution.imageWidth, videoResolution.imageHeight);
List<MeicamVideoTrack> videoTrackList = TimelineData.getInstance().getMeicamVideoTrackList();
int count = timeline.videoTrackCount();
for (int index = count - 1; index >= 0; index--) {
timeline.removeVideoTrack(index);
if (!fillTrack(timeline, videoTrackList)) {
setTimelineData(timeline);
```
