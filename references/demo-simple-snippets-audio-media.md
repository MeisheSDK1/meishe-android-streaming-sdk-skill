# Demo Simple Snippets - Audio Media

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: audio tracks/clips/effects, music/lyrics, recording voiceover, media convertor, passthrough convertor, AV file info, and frame retrieval.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [audio-media-001 onClick](#audio-media-001-onclick)
- [audio-media-002 onClick](#audio-media-002-onclick)
- [audio-media-003 setOnClickListener](#audio-media-003-setonclicklistener)
- [audio-media-004 setOnClickListener](#audio-media-004-setonclicklistener)
- [audio-media-005 setOnClickListener](#audio-media-005-setonclicklistener)
- [audio-media-006 jumpToPreview](#audio-media-006-jumptopreview)
- [audio-media-007 onProgress](#audio-media-007-onprogress)
- [audio-media-008 cancelConvert](#audio-media-008-cancelconvert)
- [audio-media-009 convertFile](#audio-media-009-convertfile)
- [audio-media-010 onCaptureDeviceAutoFocusComplete](#audio-media-010-oncapturedeviceautofocuscomplete)
- [audio-media-011 initTitle](#audio-media-011-inittitle)
- [audio-media-012 initTimeline](#audio-media-012-inittimeline)
- [audio-media-013 addMusic](#audio-media-013-addmusic)
- [audio-media-014 onClick](#audio-media-014-onclick)
- [audio-media-015 refreshAudioEqualizer](#audio-media-015-refreshaudioequalizer)
- [audio-media-016 refreshAudioEqualizer](#audio-media-016-refreshaudioequalizer)
- [audio-media-017 setAudioEqualizer](#audio-media-017-setaudioequalizer)
- [audio-media-018 setAudioEqualizer](#audio-media-018-setaudioequalizer)
- [audio-media-019 playBackEOF](#audio-media-019-playbackeof)
- [audio-media-020 playStopped](#audio-media-020-playstopped)
- [audio-media-021 onTouch](#audio-media-021-ontouch)
- [audio-media-022 compileProgress](#audio-media-022-compileprogress)
- [audio-media-023 compileFinished](#audio-media-023-compilefinished)
- [audio-media-024 compileFailed](#audio-media-024-compilefailed)
- [audio-media-025 isImage](#audio-media-025-isimage)
- [audio-media-026 isImage](#audio-media-026-isimage)
- [audio-media-027 isImage](#audio-media-027-isimage)
- [audio-media-028 parseTransToTimeline](#audio-media-028-parsetranstotimeline)
- [audio-media-029 parseTransToView](#audio-media-029-parsetranstoview)
- [audio-media-030 getAudioFxPositionInClip](#audio-media-030-getaudiofxpositioninclip)
- [audio-media-031 getAudioFxPositionInClip](#audio-media-031-getaudiofxpositioninclip)
- [audio-media-032 getAudioFxPositionInClip](#audio-media-032-getaudiofxpositioninclip)
- [audio-media-033 initClipsData](#audio-media-033-initclipsdata)
- [audio-media-034 calculateScaleInBox](#audio-media-034-calculatescaleinbox)
- [audio-media-035 initListener](#audio-media-035-initlistener)
- [audio-media-036 onStart](#audio-media-036-onstart)
- [audio-media-037 onStop](#audio-media-037-onstop)
- [audio-media-038 playStopped](#audio-media-038-playstopped)
- [audio-media-039 streamingEngineStateChanged](#audio-media-039-streamingenginestatechanged)
- [audio-media-040 updateSequenceView](#audio-media-040-updatesequenceview)
- [audio-media-041 findAudioClipByCurPosition](#audio-media-041-findaudioclipbycurposition)
- [audio-media-042 findAudioClipByCurPosition](#audio-media-042-findaudioclipbycurposition)
- [audio-media-043 findAudioClipByCurPosition](#audio-media-043-findaudioclipbycurposition)
- [audio-media-044 findNextInPointByInPoint](#audio-media-044-findnextinpointbyinpoint)
- [audio-media-045 findNextInPointByInPoint](#audio-media-045-findnextinpointbyinpoint)
- [audio-media-046 findNextInPointByInPoint](#audio-media-046-findnextinpointbyinpoint)
- [audio-media-047 findLastOutPointByInPoint](#audio-media-047-findlastoutpointbyinpoint)
- [audio-media-048 findLastOutPointByInPoint](#audio-media-048-findlastoutpointbyinpoint)
- [audio-media-049 findLastOutPointByInPoint](#audio-media-049-findlastoutpointbyinpoint)
- [audio-media-050 addAudioClip](#audio-media-050-addaudioclip)
- [audio-media-051 setFadeInOut](#audio-media-051-setfadeinout)
- [audio-media-052 getSqView](#audio-media-052-getsqview)
- [audio-media-053 onClick](#audio-media-053-onclick)
- [audio-media-054 setVideoFragmentCallBack](#audio-media-054-setvideofragmentcallback)
- [audio-media-055 onClick](#audio-media-055-onclick)
- [audio-media-056 onClick](#audio-media-056-onclick)
- [audio-media-057 getRecordFxList](#audio-media-057-getrecordfxlist)
- [audio-media-058 getRecordFxList](#audio-media-058-getrecordfxlist)
- [audio-media-059 setAudioClipVolume](#audio-media-059-setaudioclipvolume)
- [audio-media-060 getAudioClipVolume](#audio-media-060-getaudioclipvolume)
- [audio-media-061 getAudioClipVolume](#audio-media-061-getaudioclipvolume)
- [audio-media-062 getAudioClipVolume](#audio-media-062-getaudioclipvolume)
- [audio-media-063 addNoiseSuppression](#audio-media-063-addnoisesuppression)
- [audio-media-064 getAudioFxPositionInClip](#audio-media-064-getaudiofxpositioninclip)
- [audio-media-065 getAudioFxPositionInClip](#audio-media-065-getaudiofxpositioninclip)
- [audio-media-066 getAudioFxPositionInClip](#audio-media-066-getaudiofxpositioninclip)
- [audio-media-067 updateMusicVoiceSeekBar](#audio-media-067-updatemusicvoiceseekbar)
- [audio-media-068 playStopped](#audio-media-068-playstopped)
- [audio-media-069 onTouch](#audio-media-069-ontouch)
- [audio-media-070 compileProgress](#audio-media-070-compileprogress)
- [audio-media-071 compileFinished](#audio-media-071-compilefinished)
- [audio-media-072 compileFailed](#audio-media-072-compilefailed)
- [audio-media-073 initTimeline](#audio-media-073-inittimeline)
- [audio-media-074 addVideoClip](#audio-media-074-addvideoclip)
- [audio-media-075 selectEditDrawRect](#audio-media-075-selecteditdrawrect)
- [audio-media-076 initTitle](#audio-media-076-inittitle)
- [audio-media-077 OnCenterTextClick](#audio-media-077-oncentertextclick)
- [audio-media-078 selectCreateRatio](#audio-media-078-selectcreateratio)
- [audio-media-079 onClick](#audio-media-079-onclick)
- [audio-media-080 jumpToPreview](#audio-media-080-jumptopreview)
- [audio-media-081 addMusic](#audio-media-081-addmusic)
- [audio-media-082 addMusic](#audio-media-082-addmusic)
- [audio-media-083 appendVideoClip](#audio-media-083-appendvideoclip)
- [audio-media-084 appendVideoClip](#audio-media-084-appendvideoclip)
- [audio-media-085 getSinglePool](#audio-media-085-getsinglepool)
- [audio-media-086 getSinglePool](#audio-media-086-getsinglepool)
- [audio-media-087 createTimeline](#audio-media-087-createtimeline)
- [audio-media-088 applyNoiseSuppression](#audio-media-088-applynoisesuppression)
- [audio-media-089 applyNoiseSuppression](#audio-media-089-applynoisesuppression)
- [audio-media-090 applyVolumeKeyInfo](#audio-media-090-applyvolumekeyinfo)
- [audio-media-091 getVolumeByKeyTime](#audio-media-091-getvolumebykeytime)
- [audio-media-092 buildTimelineRecordAudio](#audio-media-092-buildtimelinerecordaudio)
- [audio-media-093 applyCropData](#audio-media-093-applycropdata)
- [audio-media-094 setBaseUIClip](#audio-media-094-setbaseuiclip)
- [audio-media-095 setBaseUIClip](#audio-media-095-setbaseuiclip)
- [audio-media-096 onHandActionDown](#audio-media-096-onhandactiondown)
- [audio-media-097 getAvFileDuration](#audio-media-097-getavfileduration)
- [audio-media-098 openOriginalVoice](#audio-media-098-openoriginalvoice)
- [audio-media-099 freezeFrameClip](#audio-media-099-freezeframeclip)
- [audio-media-100 setVideoConvert](#audio-media-100-setvideoconvert)
- [audio-media-101 setKeepAudioPitch](#audio-media-101-setkeepaudiopitch)
- [audio-media-102 getSpeed](#audio-media-102-getspeed)
- [audio-media-103 getFadeInDuration](#audio-media-103-getfadeinduration)
- [audio-media-104 getFadeOutDuration](#audio-media-104-getfadeoutduration)
- [audio-media-105 getMeicamAudioFxes](#audio-media-105-getmeicamaudiofxes)
- [audio-media-106 loadData](#audio-media-106-loaddata)
- [audio-media-107 setTransitionInfoList](#audio-media-107-settransitioninfolist)
- [audio-media-108 getAudioTrackMaxDuration](#audio-media-108-getaudiotrackmaxduration)
- [audio-media-109 addAudioClipInfoByTrackIndex](#audio-media-109-addaudioclipinfobytrackindex)
- [audio-media-110 setThemeQuiet](#audio-media-110-setthemequiet)
- [audio-media-111 restoreThemeVolume](#audio-media-111-restorethemevolume)
- [audio-media-112 getVideoDuration](#audio-media-112-getvideoduration)
- [audio-media-113 convertFile](#audio-media-113-convertfile)
- [audio-media-114 convertFile](#audio-media-114-convertfile)
- [audio-media-115 buildTimelineMusic](#audio-media-115-buildtimelinemusic)
- [audio-media-116 buildTimelineMusic](#audio-media-116-buildtimelinemusic)
- [audio-media-117 buildTimelineRecordAudio](#audio-media-117-buildtimelinerecordaudio)
- [audio-media-118 newTimeline](#audio-media-118-newtimeline)
- [audio-media-119 applyTheme](#audio-media-119-applytheme)
- [audio-media-120 getVideoEditResolutionByClip](#audio-media-120-getvideoeditresolutionbyclip)
- [audio-media-121 checkVideoAssetIs4K](#audio-media-121-checkvideoassetis4k)
- [audio-media-122 checkVideoAssetIs4K](#audio-media-122-checkvideoassetis4k)
<!-- END GENERATED CONTENTS -->

## `audio-media-001` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:160`

API classes: `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM`
Common calls: `getId()`, `getInstance()`, `finishActivity()`, `setCompileConfigurations()`, `currentTimeMillis()`, `getVideoSavePath()`, `getAVFileInfo()`, `getVideoStreamDimension()`, `compileVideo()`, `getDuration()`

Simple sequence:

```java
int id = v.getId();
if (id == R.id.boomRang_preview_closeButton) {
AppManager.getInstance().finishActivity();
mStreamingContext.setCompileConfigurations(null);
mCompileVideoPath = PathUtils.getVideoSavePath(fileName);
NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(mRecordVideoPath);
if (fileInfo != null) {
NvsSize size = fileInfo.getVideoStreamDimension(0);
VideoCompileUtil.compileVideo(mStreamingContext, mTimeline, mCompileVideoPath, 0, mTimeline.getDuration(),
NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, compile_height);
```

## `audio-media-002` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:162`

API classes: `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM`
Common calls: `getInstance()`, `finishActivity()`, `setCompileConfigurations()`, `currentTimeMillis()`, `getVideoSavePath()`, `getAVFileInfo()`, `getVideoStreamDimension()`, `compileVideo()`, `getDuration()`

Simple sequence:

```java
if (id == R.id.boomRang_preview_closeButton) {
AppManager.getInstance().finishActivity();
mStreamingContext.setCompileConfigurations(null);
mCompileVideoPath = PathUtils.getVideoSavePath(fileName);
NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(mRecordVideoPath);
if (fileInfo != null) {
NvsSize size = fileInfo.getVideoStreamDimension(0);
VideoCompileUtil.compileVideo(mStreamingContext, mTimeline, mCompileVideoPath, 0, mTimeline.getDuration(),
NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, compile_height);
```

## `audio-media-003` `setOnClickListener`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2105`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `getInstance()`, `takeScreenshot()`, `setOnClickListener()`, `OnClickListener()`, `isStartNativeCamera()`, `getRecordVideoPath()`, `setEnabled()`, `startRecording()`, `setCurrentMusic()`, `seekPosition()`, `getTrimIn()`, `startPlay()`

Simple sequence:

```java
mFlStartRecord.setOnClickListener(new View.OnClickListener() {
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
mCurRecordVideoPath = PathUtils.getRecordVideoPath();
mFlStartRecord.setEnabled(false);
if (!mStreamingContext.startRecording(mCurRecordVideoPath)) {
if (mAllRecordingTime == 0) {
AudioPlayer.getInstance(mContext).setCurrentMusic(mSelectMusicInfo, true);
AudioPlayer.getInstance(mContext).seekPosition(mAllRecordingTime + mSelectMusicInfo.getTrimIn());
AudioPlayer.getInstance(mContext).startPlay();
if (mLiveWindow instanceof MSLiveWindow) {
mPictureBitmap = ((MSLiveWindow) mLiveWindow).takeScreenshot();
} else if (mLiveWindow instanceof MSLiveWindowExt) {
mPictureBitmap = ((MSLiveWindowExt) mLiveWindow).takeScreenshot();
if (mPictureBitmap != null) {
mPictureImage.setImageBitmap(mPictureBitmap);
```

## `audio-media-004` `setOnClickListener`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2107`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `getInstance()`, `takeScreenshot()`, `isStartNativeCamera()`, `getRecordVideoPath()`, `setEnabled()`, `startRecording()`, `setCurrentMusic()`, `seekPosition()`, `getTrimIn()`, `startPlay()`, `add()`, `setImageBitmap()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
mCurRecordVideoPath = PathUtils.getRecordVideoPath();
mFlStartRecord.setEnabled(false);
if (!mStreamingContext.startRecording(mCurRecordVideoPath)) {
if (mAllRecordingTime == 0) {
AudioPlayer.getInstance(mContext).setCurrentMusic(mSelectMusicInfo, true);
AudioPlayer.getInstance(mContext).seekPosition(mAllRecordingTime + mSelectMusicInfo.getTrimIn());
AudioPlayer.getInstance(mContext).startPlay();
if (mLiveWindow instanceof MSLiveWindow) {
mPictureBitmap = ((MSLiveWindow) mLiveWindow).takeScreenshot();
} else if (mLiveWindow instanceof MSLiveWindowExt) {
mPictureBitmap = ((MSLiveWindowExt) mLiveWindow).takeScreenshot();
if (mPictureBitmap != null) {
mPictureImage.setImageBitmap(mPictureBitmap);
```

## `audio-media-005` `setOnClickListener`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2200`

API classes: `NvsVideoStreamInfo`, `NvsAVFileInfo`, `NvsSize`
Static/constants: `NvsVideoStreamInfo.VIDEO_ROTATION_90`, `NvsVideoStreamInfo.VIDEO_ROTATION_270`
Common calls: `instance()`, `size()`, `get()`, `add()`, `setOutPoint()`, `getTrimOut()`, `getTrimIn()`, `getOriginalOutPoint()`, `setFilePath()`, `getAVFileInfo()`, `getFilePath()`, `clear()`

Simple sequence:

```java
clipInfo.setFilePath(mRecordFileList.get(i));
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(pathList.get(0).getFilePath());
NvsSize size = avFileInfo.getVideoStreamDimension(0);
int rotation = avFileInfo.getVideoStreamRotation(0);
if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_90
|| rotation == NvsVideoStreamInfo.VIDEO_ROTATION_270) {
TimelineData.instance().setVideoResolution(Util.getVideoEditResolution(makeRatio));
TimelineData.instance().setMakeRatio(makeRatio);
TimelineData.instance().setClipInfoData(pathList);
mSelectMusicInfo.setFadeDuration(1000000 * 3);
mSelectMusicInfo.setInPoint(0);
mSelectMusicInfo.setOutPoint(mSelectMusicInfo.getTrimOut() - mSelectMusicInfo.getTrimIn());
mSelectMusicInfo.setOriginalInPoint(mSelectMusicInfo.getInPoint());
mSelectMusicInfo.setOriginalOutPoint(mSelectMusicInfo.getOutPoint());
mSelectMusicInfo.setOriginalTrimIn(mSelectMusicInfo.getTrimIn());
mSelectMusicInfo.setOriginalTrimOut(mSelectMusicInfo.getTrimOut());
long cur_music_duration = mSelectMusicInfo.getOriginalOutPoint() - mSelectMusicInfo.getOriginalInPoint();
long extra_duration = mAllRecordingTime - mSelectMusicInfo.getOriginalOutPoint();
mSelectMusicInfo.setExtraMusic(extra_music);
mSelectMusicInfo.setExtraMusicLeft(extra_music_left);
mSelectMusicInfo.setOutPoint(mAllRecordingTime);
TimelineData.instance().setMusicList(musicInfoList);
mNext.setClickable(false);
AppManager.getInstance().jumpActivity(CaptureActivity.this, VideoEditActivity.class, bundle);
```

## `audio-media-006` `jumpToPreview`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:295`

API classes: `NvsVideoStreamInfo`, `NvsAVFileInfo`, `NvsSize`
Static/constants: `NvsVideoStreamInfo.VIDEO_ROTATION_90`, `NvsVideoStreamInfo.VIDEO_ROTATION_270`
Common calls: `instance()`, `get()`, `size()`, `setFilePath()`, `getPath()`, `add()`, `getAVFileInfo()`, `getFilePath()`, `clear()`, `getVideoStreamDimension()`, `getVideoStreamRotation()`, `setVideoResolution()`

Simple sequence:

```java
clipInfo.setFilePath(listOfRecordData.get(i).getPath());
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(pathList.get(0).getFilePath());
NvsSize size = avFileInfo.getVideoStreamDimension(0);
int rotation = avFileInfo.getVideoStreamRotation(0);
if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_90
|| rotation == NvsVideoStreamInfo.VIDEO_ROTATION_270) {
TimelineData.instance().setVideoResolution(Util.getVideoEditResolution(makeRatio));
TimelineData.instance().setMakeRatio(makeRatio);
TimelineData.instance().setClipInfoData(pathList);
AppManager.getInstance().jumpActivity(CaptureSceneActivity.this, PreviewActivity.class, bundle);
```

## `audio-media-007` `onProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:57`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR`
Common calls: `d()`, `post()`, `onCanceled()`

Simple sequence:

```java
errorCode == NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR);
```

## `audio-media-008` `cancelConvert`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:252`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.CONVERTOR_ENABLE_HDR`
Common calls: `get()`, `getTrimIn()`, `getTrimOut()`, `d()`, `size()`, `isEmpty()`, `setMeidaFileConvertorCallback()`, `getFilePath()`, `getFileName()`, `e()`, `put()`, `convertMeidaFile()`

Simple sequence:

```java
if (mMediaFileConvertor == null) {
mMediaFileConvertor = new NvsMediaFileConvertor();
mMediaFileConvertor.setMeidaFileConvertorCallback(this, null);
String mSrcPath = mClipList.get(mIndex).getFilePath();
mDstPath = mDir + File.separator + PathUtils.getFileName(mSrcPath);
Logger.e(TAG, "video convertStart =  " + mClipList.get(mIndex).getTrimIn() + "-->convertEnd" + mClipList.get(mIndex).getTrimOut());
table.put(NvsMediaFileConvertor.CONVERTOR_ENABLE_HDR, true);
mClipList.get(mIndex).getTrimIn(), mClipList.get(mIndex).getTrimOut(), table);
```

## `audio-media-009` `convertFile`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/ConvertFiles.java:257`

API classes: `NvsMediaFileConvertor`

Simple sequence:

```java
if (mMediaFileConvertor == null) {
mMediaFileConvertor = new NvsMediaFileConvertor();
```

## `audio-media-010` `onCaptureDeviceAutoFocusComplete`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1578`

API classes: `NvsAVFileInfo`
Common calls: `getClipsDurationBySpeed()`, `setCurVideoDuration()`, `d()`, `addClip()`, `updateRecordClipsInfo()`, `setEnabled()`, `stopPlay()`, `setPlay()`, `getAVFileInfo()`, `getDuration()`, `setCaptureVideo()`, `sendEmptyMessage()`

Simple sequence:

```java
mRecordBtn.setEnabled(true);
mCurMusicInfo.setPlay(false);
NvsAVFileInfo info = mStreamingContext.getAVFileInfo(mCurRecordVideoPath);
if (info != null) {
clipDur = info.getDuration();
clip.setCaptureVideo(true);
mRecordProgress.setCurVideoDuration(mRecordClipsInfo.getClipsDurationBySpeed());
if (MAX_RECORD_DURATION - mRecordClipsInfo.getClipsDurationBySpeed() <= CLIP_MIN_RECORD_DURATION / 2)
mRecordProgress.setCurVideoDuration(mRecordClipsInfo.getClipsDurationBySpeed());
Log.d(TAG, "onCaptureRecordingFinished: all duration:" + mRecordClipsInfo.getClipsDurationBySpeed());
if (mRecordClipsInfo.getClipsDurationBySpeed() >= MAX_RECORD_DURATION) {
```

## `audio-media-011` `initTitle`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:326`

API classes: `NvsSize`
Common calls: `getViewTreeObserver()`, `getExtras()`, `get()`, `getDouVideoConvertDir()`, `sendConvertFileMsg()`, `getClipList()`, `getDuration()`, `getVideoTrackByIndex()`, `getAudioTrackByIndex()`, `getMusicInfo()`, `connectTimelineWithLiveWindow()`, `addOnGlobalLayoutListener()`

Simple sequence:

```java
Bundle bundle = intent.getExtras();
if (hasAllPermission()) {
mConvertFiles = new ConvertFiles(mRecordInfo, PathUtils.getDouVideoConvertDir(), mHandler, MESSAGE_ALL_VIDEO_CONVERT_FINISHED);
mTimeline = initTimeline(mRecordInfo.getClipList());
if (mTimeline == null) {
mTimelineDuration = mTimeline.getDuration();
mVideoTrack = mTimeline.getVideoTrackByIndex(0);
mMusicTrack = mTimeline.getAudioTrackByIndex(0);
addMusic(mRecordInfo.getMusicInfo());
mStreamingContext.connectTimelineWithLiveWindow(mTimeline, mLiveWindow);
seekTimeline(mTimeline, 0);
ViewTreeObserver observer = mLiveWindow.getViewTreeObserver();
int width = mLiveWindow.getWidth();
int height = mLiveWindow.getHeight();
NvsSize liveWindowSize = Util.getLiveWindowSize(TimelineUtil.getTimelineSize(mTimeline), new NvsSize(width, height), false);
ViewGroup.LayoutParams params = mLiveWindow.getLayoutParams();
mLiveWindow.setLayoutParams(params);
mLiveWindow.getViewTreeObserver().removeOnGlobalLayoutListener(this);
mTipTxtShowAni.setDuration(200);
mTipTxtShowAni.setFillAfter(true);
mFxSeekView.setFilterMode();
```

## `audio-media-012` `initTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:948`

API classes: `NvsRational`, `NvsTimeline`, `NvsAudioResolution`, `NvsVideoResolution`, `NvsVideoTrack`, `NvsAudioTrack`, `NvsVideoClip`
Common calls: `e()`, `getVideoEditResolution()`, `createTimeline()`, `appendVideoTrack()`, `appendAudioTrack()`, `size()`, `get()`, `getDuration()`

Simple sequence:

```java
private NvsTimeline initTimeline(ArrayList<RecordClip> clips) {
NvsVideoResolution videoEditRes = Util.getVideoEditResolution(NvAsset.AspectRatio_9v16);
videoEditRes.imagePAR = new NvsRational(1, 1);
NvsRational videoFps = new NvsRational(30, 1);
NvsAudioResolution audioEditRes = new NvsAudioResolution();
NvsTimeline timeline = mStreamingContext.createTimeline(videoEditRes, videoFps, audioEditRes);
if (timeline == null) {
Log.e(TAG, "create timeline failed!");
NvsVideoTrack videoTrack = timeline.appendVideoTrack();
NvsAudioTrack audioTrack = timeline.appendAudioTrack();
NvsVideoClip videoClip = appendClip(videoTrack, recordClip, false);
Logger.e(TAG, "TimeLine Duratoin Normal -->" + timeline.getDuration());
return timeline;
```

## `audio-media-013` `addMusic`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1994`

API classes: `NvsAudioClip`
Common calls: `getDuration()`, `getTrimIn()`, `getTrimOut()`, `appendClip()`, `getFilePath()`, `e()`

Simple sequence:

```java
while (mMusicTrack.getDuration() < mVideoTrack.getDuration()) {
long trimIn = musicInfo.getTrimIn();
long trimOut = musicInfo.getTrimOut();
NvsAudioClip audioClip = mMusicTrack.appendClip(musicInfo.getFilePath(), trimIn, trimOut);
```

## `audio-media-014` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:225`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `stopEngine()`, `setClickable()`, `setCaptureVideo()`, `setRotateAngle()`, `getExtraVideoRotation()`, `addClip()`, `setMusicInfo()`, `putSerializable()`, `getInstance()`, `jumpActivity()`

Simple sequence:

```java
if (id == R.id.trimFinish) {
if (mClipFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mTrimFinish.setClickable(false);
clip.setCaptureVideo(false);
clip.setRotateAngle(mVideoClip.getExtraVideoRotation());
recordClipsInfo.setMusicInfo(null);
AppManager.getInstance().jumpActivity(DouVideoTrimActivity.this, DouVideoEditActivity.class, bundle);
```

## `audio-media-015` `refreshAudioEqualizer`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:284`

API classes: `NvsAudioFx`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getEffectKey()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `getAudioFxCount()`, `getAudioFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`, `appendAudioFx()`, `getFloatVal()`, `setValue()`, `d()`

Simple sequence:

```java
if (item == null || mTimeline == null) return;
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
if (videoTrack == null) return;
int clipCount = videoTrack.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
if(videoClip==null)continue;
NvsAudioFx audioFx = null;
int fxCount = videoClip.getAudioFxCount();
for (int j = 0; j < fxCount; j++) {
NvsAudioFx fxByIndex = videoClip.getAudioFxByIndex(j);
if (fxByIndex != null && TextUtils.equals(fxByIndex.getBuiltinAudioFxName(), Constants.AUDIO_EQ)) {
if (audioFx != null) {
int intVal = (int) audioFx.getFloatVal(item.getEffectKey());
item.setValue(intVal);
Log.d(TAG, "item key:" + item.getEffectKey() + "voiceValue:" + intVal);
```

## `audio-media-016` `refreshAudioEqualizer`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:289`

API classes: `NvsAudioFx`, `NvsVideoClip`
Common calls: `getEffectKey()`, `getClipByIndex()`, `getAudioFxCount()`, `getAudioFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`, `appendAudioFx()`, `getFloatVal()`, `setValue()`, `d()`

Simple sequence:

```java
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
if(videoClip==null)continue;
NvsAudioFx audioFx = null;
int fxCount = videoClip.getAudioFxCount();
for (int j = 0; j < fxCount; j++) {
NvsAudioFx fxByIndex = videoClip.getAudioFxByIndex(j);
if (fxByIndex != null && TextUtils.equals(fxByIndex.getBuiltinAudioFxName(), Constants.AUDIO_EQ)) {
if (audioFx != null) {
int intVal = (int) audioFx.getFloatVal(item.getEffectKey());
item.setValue(intVal);
Log.d(TAG, "item key:" + item.getEffectKey() + "voiceValue:" + intVal);
```

## `audio-media-017` `setAudioEqualizer`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:318`

API classes: `NvsAudioFx`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `isEmpty()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `getAudioFxCount()`, `getAudioFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`, `appendAudioFx()`, `getFloatVal()`, `d()`, `setFloatVal()`

Simple sequence:

```java
if (TextUtils.isEmpty(audioKey) || mTimeline == null) return;
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
if (videoTrack == null) return;
int clipCount = videoTrack.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
if (videoClip == null) return;
NvsAudioFx audioFx = null;
int fxCount = videoClip.getAudioFxCount();
for (int j = 0; j < fxCount; j++) {
NvsAudioFx fxByIndex = videoClip.getAudioFxByIndex(j);
if (fxByIndex != null && TextUtils.equals(fxByIndex.getBuiltinAudioFxName(), Constants.AUDIO_EQ)) {
if (audioFx != null) {
if (audioFx.getFloatVal(audioKey) != audioValue) {
audioFx.setFloatVal(audioKey, audioValue);
```

## `audio-media-018` `setAudioEqualizer`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:323`

API classes: `NvsAudioFx`, `NvsVideoClip`
Common calls: `getClipByIndex()`, `getAudioFxCount()`, `getAudioFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`, `appendAudioFx()`, `getFloatVal()`, `d()`, `setFloatVal()`

Simple sequence:

```java
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
if (videoClip == null) return;
NvsAudioFx audioFx = null;
int fxCount = videoClip.getAudioFxCount();
for (int j = 0; j < fxCount; j++) {
NvsAudioFx fxByIndex = videoClip.getAudioFxByIndex(j);
if (fxByIndex != null && TextUtils.equals(fxByIndex.getBuiltinAudioFxName(), Constants.AUDIO_EQ)) {
if (audioFx != null) {
if (audioFx.getFloatVal(audioKey) != audioValue) {
audioFx.setFloatVal(audioKey, audioValue);
```

## `audio-media-019` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:393`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `audio-media-020` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:398`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `audio-media-021` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:458`

API classes: `NvsTimeline`
Common calls: `setVisibility()`, `setCompileVideoListener()`, `OnCompileVideoListener()`

Simple sequence:

```java
mCompileVideoFragment.setCompileVideoListener(new CompileVideoFragment.OnCompileVideoListener() {
public void compileProgress(NvsTimeline timeline, int progress) {
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `audio-media-022` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:464`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `audio-media-023` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:469`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `audio-media-024` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/audio/AudioEqualizerActivity.java:474`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `audio-media-025` `isImage`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/EditActivity.java:529`

API classes: `NvsAVFileInfo`
Static/constants: `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`
Common calls: `getAVFileInfo()`, `getFilePath()`, `getAVFileType()`

Simple sequence:

```java
if (clipInfo != null) {
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(clipInfo.getFilePath());
if (avFileInfo != null) {
return avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_IMAGE;
```

## `audio-media-026` `isImage`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/EditActivity.java:530`

API classes: `NvsAVFileInfo`
Static/constants: `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`
Common calls: `getAVFileInfo()`, `getFilePath()`, `getAVFileType()`

Simple sequence:

```java
if (clipInfo != null) {
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(clipInfo.getFilePath());
if (avFileInfo != null) {
return avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_IMAGE;
```

## `audio-media-027` `isImage`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/EditActivity.java:532`

API classes: `NvsAVFileInfo`
Static/constants: `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`
Common calls: `getAVFileType()`

Simple sequence:

```java
if (avFileInfo != null) {
return avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_IMAGE;
```

## `audio-media-028` `parseTransToTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:384`

API classes: `NvsAVFileInfo`, `NvsSize`
Common calls: `get()`, `put()`, `getAVFileInfo()`, `getVideoStreamRotation()`, `getVideoStreamDimension()`

Simple sequence:

```java
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(filePath);
int videoStreamRotation = avFileInfo.getVideoStreamRotation(0);
NvsSize dimension = avFileInfo.getVideoStreamDimension(0);
```

## `audio-media-029` `parseTransToView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:455`

API classes: `NvsAVFileInfo`, `NvsSize`
Common calls: `get()`, `put()`, `getAVFileInfo()`, `getVideoStreamRotation()`, `getVideoStreamDimension()`

Simple sequence:

```java
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(filePath);
int videoStreamRotation = avFileInfo.getVideoStreamRotation(0);
NvsSize dimension = avFileInfo.getVideoStreamDimension(0);
```

## `audio-media-030` `getAudioFxPositionInClip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:381`

API classes: `NvsVideoClip`, `NvsAudioFx`
Common calls: `isEmpty()`, `getAudioFxCount()`, `getAudioFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`

Simple sequence:

```java
private int getAudioFxPositionInClip(NvsVideoClip nvsVideoClip, String fxName){
int count = nvsVideoClip.getAudioFxCount();
for (int i = 0; i < count; i++) {
NvsAudioFx fxByIndex = nvsVideoClip.getAudioFxByIndex(i);
if(TextUtils.equals(fxName,fxByIndex.getBuiltinAudioFxName())){
```

## `audio-media-031` `getAudioFxPositionInClip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:383`

API classes: `NvsAudioFx`
Common calls: `isEmpty()`, `getAudioFxCount()`, `getAudioFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`

Simple sequence:

```java
int count = nvsVideoClip.getAudioFxCount();
for (int i = 0; i < count; i++) {
NvsAudioFx fxByIndex = nvsVideoClip.getAudioFxByIndex(i);
if(TextUtils.equals(fxName,fxByIndex.getBuiltinAudioFxName())){
```

## `audio-media-032` `getAudioFxPositionInClip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:385`

API classes: `NvsAudioFx`
Common calls: `isEmpty()`, `getAudioFxCount()`, `getAudioFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`

Simple sequence:

```java
int count = nvsVideoClip.getAudioFxCount();
for (int i = 0; i < count; i++) {
NvsAudioFx fxByIndex = nvsVideoClip.getAudioFxByIndex(i);
if(TextUtils.equals(fxName,fxByIndex.getBuiltinAudioFxName())){
```

## `audio-media-033` `initClipsData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:366`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getAVInfoFromFile`
Common calls: `get()`, `getMaskZoomView()`, `size()`, `getVideoStreamDimension()`, `getMaskType()`, `scrollToPosition()`, `getSelectPos()`, `setLayoutManager()`, `setAdapter()`, `instance()`, `cloneClipInfoData()`, `getFilePath()`

Simple sequence:

```java
clipRecyclerView.setLayoutManager(linearLayoutManager);
clipRecyclerView.setAdapter(mClipAdapter);
String filePath = clipInfoDatum.getFilePath();
NvsAVFileInfo avInfoFromFile = NvsStreamingContext.getAVInfoFromFile(filePath, 0);
if (avInfoFromFile != null) {
int videoWidth = avInfoFromFile.getVideoStreamDimension(0).width;
int videoHeight = avInfoFromFile.getVideoStreamDimension(0).height;
int videoStreamRotation = avInfoFromFile.getVideoStreamRotation(0);
CutData cutData = clipInfoDatum.getCropInfo();
if (null != cutData) {
float value = cutData.getRatioValue();
clipInfoDatum.setFileRatio(fileRatio);
maskInfoDataMap.put(i, clipInfoDatum.getMaskInfoData());
mClipAdapter.setClipInfoList(clipInfoData);
mClipAdapter.setTimeLine(mTimeline);
mClipAdapter.setOnItemClickListener(new AnimationClipAdapter.OnItemClickListener() {
if (maskInfoData != null) {
mVideoFragment.getMaskZoomView().setMaskTypeAndInfo(maskInfoData.getMaskType(),
menuAdapter.setMaskType(maskInfoData.getMaskType());
menuAdapter.setSelectPos(0);
mVideoFragment.getMaskZoomView().clear();
mVideoFragment.getMaskZoomView().setVisibility(View.GONE);
if (menuAdapter.getSelectPos() > 3) {
menuRecyclerView.scrollToPosition(menuAdapter.getSelectPos());
```

## `audio-media-034` `calculateScaleInBox`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1162`

API classes: `NvsLiveWindow`, `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getAVInfoFromFile`
Common calls: `getVideoStreamDimension()`, `assetSizeInBox()`, `getSpecificValue()`, `getFileRatio()`, `getFilePath()`, `getAVInfoFromFile()`, `getVideoStreamRotation()`, `min()`

Simple sequence:

```java
private static float calculateScaleInBox(NvsLiveWindow liveWindow, ClipInfo info) {
float fileRatio = info.getFileRatio();
String filePath = info.getFilePath();
NvsAVFileInfo avInfoFromFile = NvsStreamingContext.getAVInfoFromFile(filePath, 0);
int videoWidth = avInfoFromFile.getVideoStreamDimension(0).width;
int videoHeight = avInfoFromFile.getVideoStreamDimension(0).height;
int videoStreamRotation = avInfoFromFile.getVideoStreamRotation(0);
PointF sizeBefore = NvMaskHelper.assetSizeInBox(liveWindow, beforeRatio);
PointF sizeAfter = NvMaskHelper.assetSizeInBox(liveWindow, fileRatio);
float scaleX = Util.getSpecificValue(sizeBefore.x, sizeAfter.x);
float scaleY = Util.getSpecificValue(sizeBefore.y, sizeAfter.y);
```

## `audio-media-035` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:146`

API classes: `NvsTimeline`, `NvsAudioClip`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setOnClickListener()`, `OnClickListener()`, `setVisibility()`, `getInstance()`, `setPlaySeekVisiable()`, `setTag()`, `nativeUrlMaterial()`, `putInt()`, `jumpActivityForResult()`, `currentActivity()`, `reLayoutAllViews()`, `selectAreaByInPoint()`

Simple sequence:

```java
m_titleBar.setOnTitleBarClickListener(new OnTitleBarClickListener() {
m_backBtn.setOnClickListener(new View.OnClickListener() {
m_navLayout.setVisibility(View.VISIBLE);
m_multiMusicLayout.setVisibility(View.GONE);
m_backBtn.setVisibility(View.GONE);
m_videoFragment.setPlaySeekVisiable(true);
m_musicSingleBtn.setOnClickListener(new View.OnClickListener() {
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(),
m_musicMultiBtn.setOnClickListener(new View.OnClickListener() {
m_navLayout.setVisibility(View.GONE);
m_multiMusicLayout.setVisibility(View.VISIBLE);
m_backBtn.setVisibility(View.VISIBLE);
m_videoFragment.setPlaySeekVisiable(false);
m_multiOkBtn.setOnClickListener(new View.OnClickListener() {
m_navLayout.setVisibility(View.VISIBLE);
m_multiMusicLayout.setVisibility(View.GONE);
m_backBtn.setVisibility(View.GONE);
m_videoFragment.setPlaySeekVisiable(true);
m_playBtn.setOnClickListener(new View.OnClickListener() {
m_zoomInBtn.setOnClickListener(new View.OnClickListener() {
m_sequenceLayout.selectAreaByInPoint(m_streamingContext.getTimelineCurrentPosition(m_timeLine));
m_zoomOutBtn.setOnClickListener(new View.OnClickListener() {
m_sequenceLayout.selectAreaByInPoint(m_streamingContext.getTimelineCurrentPosition(m_timeLine));
m_addMusicBtn.setOnClickListener(new View.OnClickListener() {
// ... 29 more SDK-related lines omitted in this compressed snippet ...
```

## `audio-media-036` `onStart`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:292`

API classes: `NvsAudioClip`
Common calls: `e()`, `setVolumeGain()`, `setVolume()`

Simple sequence:

```java
NvsAudioClip audioClip = findAudioClipByInPoint(m_curInPoint);
if (audioClip != null && cur_musicInfo != null) {
audioClip.setVolumeGain(value, value);
cur_musicInfo.setVolume(value);
```

## `audio-media-037` `onStop`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:309`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `setVideoFragmentCallBack()`, `VideoFragmentListener()`, `post()`, `fullScroll()`, `playVideo()`, `round()`, `getDuration()`, `getSequenceWidth()`, `smoothScrollTo()`

Simple sequence:

```java
m_videoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (m_sequenceView != null) {
int x = Math.round((stamp / (float) m_timeLine.getDuration() * m_sequenceView.getSequenceWidth()));
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_play);
```

## `audio-media-038` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:327`

API classes: `NvsTimeline`
Common calls: `round()`, `getDuration()`, `getSequenceWidth()`, `smoothScrollTo()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (m_sequenceView != null) {
int x = Math.round((stamp / (float) m_timeLine.getDuration() * m_sequenceView.getSequenceWidth()));
```

## `audio-media-039` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:337`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`

Simple sequence:

```java
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_play);
```

## `audio-media-040` `updateSequenceView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:496`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getSqView()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getDuration()`

Simple sequence:

```java
m_sequenceView = m_sequenceLayout.getSqView();
final ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray = new ArrayList<>();
NvsVideoTrack videoTrack = m_timeLine.getVideoTrackByIndex(0);
for (int i = 0; i < videoTrack.getClipCount(); i++) {
NvsVideoClip clip = videoTrack.getClipByIndex(i);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
infoDesc.mediaFilePath = clip.getFilePath();
infoDesc.trimIn = clip.getTrimIn();
infoDesc.trimOut = clip.getTrimOut();
infoDesc.inPoint = clip.getInPoint();
infoDesc.outPoint = clip.getOutPoint();
double duration = (double) m_timeLine.getDuration();
int halfScreenWidth = ScreenUtils.getScreenWidth(this) / 2;
RelativeLayout.LayoutParams layoutParams = (RelativeLayout.LayoutParams) m_playBtnLayout.getLayoutParams();
m_sequenceView.setStartPadding(sequenceLeftPadding);
m_sequenceView.setEndPadding(halfScreenWidth);
```

## `audio-media-041` `findAudioClipByCurPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:569`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `getOutPoint()`, `getClipCount()`, `getClipByIndex()`, `e()`

Simple sequence:

```java
private NvsAudioClip findAudioClipByCurPosition(long curPos) {
if (m_musicTrack != null) {
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
Log.e("===>", "find clip in: " + audioClip.getInPoint() + " out: " + audioClip.getOutPoint());
if (curPos >= audioClip.getInPoint() && curPos < audioClip.getOutPoint()) {
```

## `audio-media-042` `findAudioClipByCurPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:570`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `getOutPoint()`, `getClipCount()`, `getClipByIndex()`, `e()`

Simple sequence:

```java
if (m_musicTrack != null) {
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
Log.e("===>", "find clip in: " + audioClip.getInPoint() + " out: " + audioClip.getOutPoint());
if (curPos >= audioClip.getInPoint() && curPos < audioClip.getOutPoint()) {
```

## `audio-media-043` `findAudioClipByCurPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:571`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `getOutPoint()`, `getClipCount()`, `getClipByIndex()`, `e()`

Simple sequence:

```java
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
Log.e("===>", "find clip in: " + audioClip.getInPoint() + " out: " + audioClip.getOutPoint());
if (curPos >= audioClip.getInPoint() && curPos < audioClip.getOutPoint()) {
```

## `audio-media-044` `findNextInPointByInPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:592`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `getClipCount()`, `getClipByIndex()`, `getAttachment()`, `add()`, `size()`, `sort()`, `get()`

Simple sequence:

```java
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
if (audioClip.getInPoint() > curInPoint && audioClip.getAttachment(Constants.MUSIC_EXTRA_AUDIOCLIP) == null) {
next_point.add(audioClip.getInPoint());
```

## `audio-media-045` `findNextInPointByInPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:593`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `getClipCount()`, `getClipByIndex()`, `getAttachment()`, `add()`, `size()`, `sort()`, `get()`

Simple sequence:

```java
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
if (audioClip.getInPoint() > curInPoint && audioClip.getAttachment(Constants.MUSIC_EXTRA_AUDIOCLIP) == null) {
next_point.add(audioClip.getInPoint());
```

## `audio-media-046` `findNextInPointByInPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:595`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `getClipCount()`, `getClipByIndex()`, `getAttachment()`, `add()`

Simple sequence:

```java
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
if (audioClip.getInPoint() > curInPoint && audioClip.getAttachment(Constants.MUSIC_EXTRA_AUDIOCLIP) == null) {
next_point.add(audioClip.getInPoint());
```

## `audio-media-047` `findLastOutPointByInPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:620`

API classes: `NvsAudioClip`
Common calls: `size()`, `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `add()`, `getOutPoint()`, `sort()`, `get()`

Simple sequence:

```java
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
if (audioClip.getInPoint() < curInPoint) {
last_point.add(audioClip.getOutPoint());
```

## `audio-media-048` `findLastOutPointByInPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:621`

API classes: `NvsAudioClip`
Common calls: `size()`, `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `add()`, `getOutPoint()`, `sort()`, `get()`

Simple sequence:

```java
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
if (audioClip.getInPoint() < curInPoint) {
last_point.add(audioClip.getOutPoint());
```

## `audio-media-049` `findLastOutPointByInPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:623`

API classes: `NvsAudioClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `add()`, `getOutPoint()`

Simple sequence:

```java
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
if (audioClip.getInPoint() < curInPoint) {
last_point.add(audioClip.getOutPoint());
```

## `audio-media-050` `addAudioClip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:926`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `getExtraMusic()`, `getOriginalOutPoint()`, `setAttachment()`, `getExtraMusicLeft()`, `getFadeDuration()`, `addClip()`, `getFilePath()`, `getOriginalTrimIn()`, `setFadeOutDuration()`, `getOriginalInPoint()`, `getTrimIn()`

Simple sequence:

```java
NvsAudioClip audioClip = m_musicTrack.addClip(oneMusic.getFilePath(), oneMusic.getInPoint(), oneMusic.getTrimIn(), oneMusic.getTrimOut());
if (oneMusic.getExtraMusic() > 0) {
for (int i = 0; i < oneMusic.getExtraMusic(); ++i) {
NvsAudioClip extra_clip = m_musicTrack.addClip(oneMusic.getFilePath(),
oneMusic.getOriginalOutPoint() + i * (oneMusic.getOriginalOutPoint() - oneMusic.getOriginalInPoint()),
oneMusic.getOriginalTrimIn(), oneMusic.getOriginalTrimOut());
if (extra_clip != null) {
extra_clip.setAttachment(Constants.MUSIC_EXTRA_AUDIOCLIP, oneMusic.getInPoint());
if (i == oneMusic.getExtraMusic() - 1 && oneMusic.getExtraMusicLeft() <= 0) {
extra_clip.setAttachment(Constants.MUSIC_EXTRA_LAST_AUDIOCLIP, oneMusic.getInPoint());
extra_clip.setFadeOutDuration(oneMusic.getFadeDuration());
if (oneMusic.getExtraMusicLeft() > 0) {
NvsAudioClip extra_clip = m_musicTrack.addClip(oneMusic.getFilePath(),
oneMusic.getOriginalOutPoint() + oneMusic.getExtraMusic() * (oneMusic.getOriginalOutPoint() - oneMusic.getOriginalInPoint()),
oneMusic.getOriginalTrimIn(),
oneMusic.getOriginalTrimIn() + oneMusic.getExtraMusicLeft());
if (extra_clip != null) {
extra_clip.setAttachment(Constants.MUSIC_EXTRA_AUDIOCLIP, oneMusic.getInPoint());
extra_clip.setAttachment(Constants.MUSIC_EXTRA_LAST_AUDIOCLIP, oneMusic.getInPoint());
extra_clip.setFadeOutDuration(oneMusic.getFadeDuration());
if (audioClip != null) {
audioClip.setFadeInDuration(oneMusic.getFadeDuration());
if (oneMusic.getExtraMusic() <= 0 && oneMusic.getExtraMusicLeft() <= 0) {
audioClip.setFadeOutDuration(oneMusic.getFadeDuration());
```

## `audio-media-051` `setFadeInOut`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicActivity.java:995`

API classes: `NvsAudioClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `setFadeOutDuration()`, `getInPoint()`, `setFadeDuration()`, `setFadeInDuration()`, `getExtraMusic()`, `getExtraMusicLeft()`, `getAttachment()`

Simple sequence:

```java
if (m_musicTrack != null && cur_musicInfo != null) {
for (int i = 0; i < m_musicTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_musicTrack.getClipByIndex(i);
if (audioClip.getInPoint() == m_curInPoint) {
cur_musicInfo.setFadeDuration(fade_duration);
audioClip.setFadeInDuration(fade_duration);
if (cur_musicInfo.getExtraMusic() > 0 || cur_musicInfo.getExtraMusicLeft() > 0) {
for (int j = 0; j < m_musicTrack.getClipCount(); ++j) {
NvsAudioClip extraAudioClip = m_musicTrack.getClipByIndex(j);
if (extraAudioClip.getAttachment(Constants.MUSIC_EXTRA_LAST_AUDIOCLIP) != null) {
extraAudioClip.setFadeOutDuration(fade_duration);
audioClip.setFadeOutDuration(fade_duration);
```

## `audio-media-052` `getSqView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/music/MusicSqLayout.java:133`

API classes: `NvsMultiThumbnailSequenceView`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `LayoutParams()`, `addView()`, `initData()`, `getSequenceWidth()`, `getStartPadding()`, `getEndPadding()`

Simple sequence:

```java
public void initData(long total_duration, ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray) {
LinearLayout.LayoutParams recordAreaParams = new LinearLayout.LayoutParams(m_sqView.getSequenceWidth() + 2*m_handleWidth, ViewGroup.LayoutParams.MATCH_PARENT);
LinearLayout.LayoutParams leftMarginViewParams = new LinearLayout.LayoutParams(m_sqView.getStartPadding() - m_handleWidth, LayoutParams.MATCH_PARENT);
LinearLayout.LayoutParams reghtMarginViewParams = new LinearLayout.LayoutParams(m_sqView.getEndPadding() - m_handleWidth, LayoutParams.MATCH_PARENT);
```

## `audio-media-053` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:251`

API classes: `NvsTimeline`, `NvsAudioClip`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `setVideoFragmentCallBack()`, `VideoFragmentListener()`, `post()`, `release()`, `scrollTo()`, `fullScroll()`, `seekTimeline()`, `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `round()`

Simple sequence:

```java
m_videoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
m_videoFragment.seekTimeline(0, 0);
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);
if (audioClip.getInPoint() == 0) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (m_sequenceView != null) {
int x = Math.round((stamp / (float) m_timeLine.getDuration() * m_sequenceView.getSequenceWidth()));
if (stamp - m_curRecordInPoint >= m_minRecordDuration) {
m_recordStopBtn.setEnabled(true);
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_play);
```

## `audio-media-054` `setVideoFragmentCallBack`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:256`

API classes: `NvsAudioClip`
Common calls: `release()`, `scrollTo()`, `fullScroll()`, `seekTimeline()`, `getClipCount()`, `getClipByIndex()`, `getInPoint()`

Simple sequence:

```java
m_videoFragment.seekTimeline(0, 0);
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);
if (audioClip.getInPoint() == 0) {
```

## `audio-media-055` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:401`

API classes: `NvsAudioClip`, `NvsAudioFx`
Common calls: `getBuiltinAudioFxName()`, `setItemSelectedByFxID()`, `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `getFxByIndex()`, `isEmpty()`

Simple sequence:

```java
if (m_recordAudioTrack != null) {
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);
if (audioClip.getInPoint() == m_curRecordInPoint) {
NvsAudioFx fx = audioClip.getFxByIndex(0);
if (fx == null || fx.getBuiltinAudioFxName() == null || fx.getBuiltinAudioFxName().isEmpty()) {
m_recordFxAdapter.setItemSelectedByFxID(Constants.NO_FX);
m_recordFxAdapter.setItemSelectedByFxID(fx.getBuiltinAudioFxName());
```

## `audio-media-056` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:402`

API classes: `NvsAudioClip`, `NvsAudioFx`
Common calls: `getBuiltinAudioFxName()`, `setItemSelectedByFxID()`, `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `getFxByIndex()`, `isEmpty()`

Simple sequence:

```java
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);
if (audioClip.getInPoint() == m_curRecordInPoint) {
NvsAudioFx fx = audioClip.getFxByIndex(0);
if (fx == null || fx.getBuiltinAudioFxName() == null || fx.getBuiltinAudioFxName().isEmpty()) {
m_recordFxAdapter.setItemSelectedByFxID(Constants.NO_FX);
m_recordFxAdapter.setItemSelectedByFxID(fx.getBuiltinAudioFxName());
```

## `audio-media-057` `getRecordFxList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:678`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `get()`, `getString()`, `getDrawable()`, `add()`, `listRecordFxFromJson()`, `addAll()`, `getStringArray()`, `setLayoutManager()`, `setAdapter()`, `setItemSelectedByFxID()`, `setOnItemClickListener()`

Simple sequence:

```java
item_none.fxName = getResources().getString(R.string.NO_FX);
item_none.image_drawable = ContextCompat.getDrawable(this, R.drawable.record_none_fx);
String[] effectList = getResources().getStringArray(R.array.effect_list);
m_recordFxRv.setLayoutManager(linearLayoutManager);
m_recordFxRv.setAdapter(m_recordFxAdapter);
m_recordFxAdapter.setItemSelectedByFxID(Constants.NO_FX);
m_recordFxAdapter.setOnItemClickListener(new RecordFxAdapter.OnItemClickListener() {
NvsAudioClip nvsAudioClip = null;
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
nvsAudioClip = m_recordAudioTrack.getClipByIndex(i);
if (nvsAudioClip != null && nvsAudioClip.getInPoint() == cur_recordAudioInfo.getInPoint()) {
if (audioFxPos >= 0) {
nvsAudioClip.removeFx(audioFxPos);
cur_recordAudioInfo.setFxID(audioFxListItem.fxID);
m_videoFragment.playVideo(cur_recordAudioInfo.getInPoint(), cur_recordAudioInfo.getOutPoint());
```

## `audio-media-058` `getRecordFxList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:679`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `get()`, `getString()`, `getDrawable()`, `add()`, `listRecordFxFromJson()`, `addAll()`, `getStringArray()`, `setLayoutManager()`, `setAdapter()`, `setItemSelectedByFxID()`, `setOnItemClickListener()`

Simple sequence:

```java
item_none.fxName = getResources().getString(R.string.NO_FX);
item_none.image_drawable = ContextCompat.getDrawable(this, R.drawable.record_none_fx);
String[] effectList = getResources().getStringArray(R.array.effect_list);
m_recordFxRv.setLayoutManager(linearLayoutManager);
m_recordFxRv.setAdapter(m_recordFxAdapter);
m_recordFxAdapter.setItemSelectedByFxID(Constants.NO_FX);
m_recordFxAdapter.setOnItemClickListener(new RecordFxAdapter.OnItemClickListener() {
NvsAudioClip nvsAudioClip = null;
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
nvsAudioClip = m_recordAudioTrack.getClipByIndex(i);
if (nvsAudioClip != null && nvsAudioClip.getInPoint() == cur_recordAudioInfo.getInPoint()) {
if (audioFxPos >= 0) {
nvsAudioClip.removeFx(audioFxPos);
cur_recordAudioInfo.setFxID(audioFxListItem.fxID);
m_videoFragment.playVideo(cur_recordAudioInfo.getInPoint(), cur_recordAudioInfo.getOutPoint());
```

## `audio-media-059` `setAudioClipVolume`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:994`

API classes: `NvsAudioClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `setVolumeGain()`, `setVolume()`

Simple sequence:

```java
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);
if (audioClip.getInPoint() == inPoint && cur_recordAudioInfo != null) {
audioClip.setVolumeGain(volume, volume);
cur_recordAudioInfo.setVolume(volume);
```

## `audio-media-060` `getAudioClipVolume`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1008`

API classes: `NvsAudioClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `getVolumeGain()`

Simple sequence:

```java
if (m_recordAudioTrack != null) {
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);
if (audioClip.getInPoint() == inPoint) {
return audioClip.getVolumeGain().leftVolume;
```

## `audio-media-061` `getAudioClipVolume`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1009`

API classes: `NvsAudioClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `getVolumeGain()`

Simple sequence:

```java
if (m_recordAudioTrack != null) {
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);
if (audioClip.getInPoint() == inPoint) {
return audioClip.getVolumeGain().leftVolume;
```

## `audio-media-062` `getAudioClipVolume`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1010`

API classes: `NvsAudioClip`
Common calls: `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `getVolumeGain()`

Simple sequence:

```java
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
NvsAudioClip audioClip = m_recordAudioTrack.getClipByIndex(i);
if (audioClip.getInPoint() == inPoint) {
return audioClip.getVolumeGain().leftVolume;
```

## `audio-media-063` `addNoiseSuppression`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1055`

API classes: `NvsAudioClip`
Common calls: `getInPoint()`, `get()`, `getClipCount()`, `getClipByTimelinePosition()`, `getTimelineCurrentPosition()`, `getClipByIndex()`, `appendFx()`, `removeFx()`, `setIntVal()`, `setNoiseSuppressionLevel()`, `playVideo()`, `getOutPoint()`

Simple sequence:

```java
NvsAudioClip nvsAudioClip = null;
for (int i = 0; i < m_recordAudioTrack.getClipCount(); ++i) {
nvsAudioClip = m_recordAudioTrack.getClipByIndex(i);
if (nvsAudioClip != null && nvsAudioClip.getInPoint() == cur_recordAudioInfo.getInPoint()) {
nvsAudioClip.removeFx(pos);
noiseAudioEffect.setIntVal(Constants.NOISE_SUPPRESSION_VALUE_KEY, mNoiseSuppressionLevel);
cur_recordAudioInfo.setNoiseSuppressionLevel(mNoiseSuppressionLevel);
m_videoFragment.playVideo(cur_recordAudioInfo.getInPoint(), cur_recordAudioInfo.getOutPoint());
```

## `audio-media-064` `getAudioFxPositionInClip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1112`

API classes: `NvsAudioClip`, `NvsAudioFx`
Common calls: `isEmpty()`, `getFxCount()`, `getFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`

Simple sequence:

```java
private int getAudioFxPositionInClip(NvsAudioClip nvsAudioClip, String fxName) {
int count = nvsAudioClip.getFxCount();
for (int i = 0; i < count; i++) {
NvsAudioFx fxByIndex = nvsAudioClip.getFxByIndex(i);
if (TextUtils.equals(fxName, fxByIndex.getBuiltinAudioFxName())) {
```

## `audio-media-065` `getAudioFxPositionInClip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1114`

API classes: `NvsAudioFx`
Common calls: `isEmpty()`, `getFxCount()`, `getFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`

Simple sequence:

```java
int count = nvsAudioClip.getFxCount();
for (int i = 0; i < count; i++) {
NvsAudioFx fxByIndex = nvsAudioClip.getFxByIndex(i);
if (TextUtils.equals(fxName, fxByIndex.getBuiltinAudioFxName())) {
```

## `audio-media-066` `getAudioFxPositionInClip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:1116`

API classes: `NvsAudioFx`
Common calls: `isEmpty()`, `getFxCount()`, `getFxByIndex()`, `equals()`, `getBuiltinAudioFxName()`

Simple sequence:

```java
int count = nvsAudioClip.getFxCount();
for (int i = 0; i < count; i++) {
NvsAudioFx fxByIndex = nvsAudioClip.getFxByIndex(i);
if (TextUtils.equals(fxName, fxByIndex.getBuiltinAudioFxName())) {
```

## `audio-media-067` `updateMusicVoiceSeekBar`

Source: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:307`

API classes: `NvsTimeline`
Common calls: `putInt()`, `seekTimeline()`, `getTimelineCurrentPosition()`, `getLayoutParams()`, `putBoolean()`, `beginTransaction()`, `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `setTimeline()`, `setAutoPlay()`, `setArguments()`, `add()`

Simple sequence:

```java
mVideoFragment.setFragmentLoadFinisedListener(new VideoFragment.OnFragmentLoadFinisedListener() {
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), 0);
mVideoFragment.setTimeline(mTimeline);
mVideoFragment.setAutoPlay(true);
bundle.putInt("titleHeight", mTitleBar.getLayoutParams().height);
bundle.putInt("bottomHeight", mBottomLayout.getLayoutParams().height);
mVideoFragment.setArguments(bundle);
mVideoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
if (timeline.getDuration() - mStreamingContext.getTimelineCurrentPosition(mTimeline) <= 40000) {
mVideoFragment.seekTimeline(0, 0);
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `audio-media-068` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:343`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `audio-media-069` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:436`

API classes: `NvsTimeline`
Common calls: `setVisibility()`, `setCompileVideoListener()`, `OnCompileVideoListener()`

Simple sequence:

```java
mCompileVideoFragment.setCompileVideoListener(new CompileVideoFragment.OnCompileVideoListener() {
public void compileProgress(NvsTimeline timeline, int progress) {
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `audio-media-070` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:442`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `audio-media-071` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:447`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `audio-media-072` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:452`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `audio-media-073` `initTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1084`

API classes: `NvsRational`, `NvsAudioResolution`, `NvsVideoResolution`, `NvsVideoClip`
Common calls: `e()`, `get()`, `getVideoEditResolution()`, `d()`, `showToast()`, `getString()`, `createTimeline()`, `getLayoutParams()`, `getDefaultDisplay()`, `getMetrics()`, `dip2px()`, `setLayoutParams()`

Simple sequence:

```java
if (null == mStreamingContext) {
Log.e(TAG, "mStreamingContext is null!");
NvsVideoResolution videoEditRes = Util.getVideoEditResolution(makeRatio);
if (videoEditRes.imageWidth * videoEditRes.imageHeight > 2160 * 3840) {
ToastUtil.showToast(this, getResources().getString(R.string.timeline_size_to_large));
videoEditRes.imagePAR = new NvsRational(1, 1);
NvsRational videoFps = new NvsRational(FRAME_RATION, 1);
NvsAudioResolution audioEditRes = new NvsAudioResolution();
mTimeline = mStreamingContext.createTimeline(videoEditRes, videoFps, audioEditRes);
if (null == mTimeline) {
Log.e(TAG, "mTimeline is null!");
RelativeLayout.LayoutParams params = (RelativeLayout.LayoutParams) mLiveWindow.getLayoutParams();
getWindowManager().getDefaultDisplay().getMetrics(metric);
mLiveWindow.setLayoutParams(params);
mStreamingContext.connectTimelineWithLiveWindow(mTimeline, mLiveWindow);
mVideoTrack = mTimeline.appendVideoTrack();
mVideoTrack.removeAllClips();
for (int i = 0; i < mPath.size(); i++) {
NvsVideoClip clip = mVideoTrack.appendClip(mPath.get(i));
if (mTimeline == null) {
Log.e(TAG, "mTimeline is null");
```

## `audio-media-074` `addVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:739`

API classes: `NvsVideoFx`, `NvsVideoClip`, `NvsAVFileInfo`
Static/constants: `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`
Common calls: `getFloatVal()`, `setFloatVal()`, `appendClip()`, `e()`, `setImageMotionAnimationEnabled()`, `appendBuiltinFx()`

Simple sequence:

```java
long trimOut, NvsVideoFx transformFx) {
NvsVideoClip videoClip;
if (trimIn >= 0 && trimOut > 0 && trimOut > trimIn) {
videoClip = videoTrack.appendClip(clipPath, trimIn, trimOut);
videoClip = videoTrack.appendClip(clipPath);
if (videoType == NvsAVFileInfo.AV_FILE_TYPE_IMAGE) {
videoClip.setImageMotionAnimationEnabled(false);
NvsVideoFx builtinFx = videoClip.appendBuiltinFx("Transform 2D");
if (builtinFx != null && transformFx != null) {
double scaleXValue = transformFx.getFloatVal("Scale X");
double scaleYValue = transformFx.getFloatVal("Scale Y");
double rotateAngle = transformFx.getFloatVal("Rotation");
double transX = transformFx.getFloatVal("Trans X");
double transY = transformFx.getFloatVal("Trans Y");
builtinFx.setFloatVal("Scale X", scaleXValue);
builtinFx.setFloatVal("Scale Y", scaleYValue);
builtinFx.setFloatVal("Rotation", rotateAngle);
builtinFx.setFloatVal("Trans X", transX);
builtinFx.setFloatVal("Trans Y", transY);
```

## `audio-media-075` `selectEditDrawRect`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:1065`

API classes: `NvsAVFileInfo`
Static/constants: `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`
Common calls: `setVisibility()`

Simple sequence:

```java
if (videoType == NvsAVFileInfo.AV_FILE_TYPE_IMAGE) {
mTrimImage.setVisibility(View.GONE);
mTrimImage.setVisibility(View.VISIBLE);
```

## `audio-media-076` `initTitle`

Source: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:85`

API classes: `NvsPassthroughConvertor`, `NvsPassthroughFileInfo`
Static/constants: `NvsPassthroughConvertor.NvsPassthroughFileInfo`
Common calls: `setOnTitleBarClickListener()`, `currentTimeMillis()`, `getQuickSplicingVideoSavePath()`, `stop()`, `NvsPassthroughFileInfo()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `add()`, `convertMediaFile()`, `setPassthroughConvertorCallback()`, `setVisibility()`

Simple sequence:

```java
mTitleBar.setOnTitleBarClickListener(new OnTitleBarClickListener() {
mCompileVideoPath = PathUtils.getQuickSplicingVideoSavePath(fileName);
mStreamingContext.stop();
NvsPassthroughConvertor nvsPassthroughConvertor = new NvsPassthroughConvertor();
List<NvsPassthroughConvertor.NvsPassthroughFileInfo> passthroughFileInfos = new ArrayList<>();
NvsPassthroughConvertor.NvsPassthroughFileInfo fileInfo = new NvsPassthroughConvertor.NvsPassthroughFileInfo();
fileInfo.filePath = mClipInfo.getFilePath();
fileInfo.trimIn = mClipInfo.getTrimIn();
fileInfo.trimOut = mClipInfo.getTrimOut();
nvsPassthroughConvertor.setPassthroughConvertorCallback(new FilePassThroughConvertorCallback(), null);
mProgressBar.setVisibility(View.VISIBLE);
```

## `audio-media-077` `OnCenterTextClick`

Source: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:97`

API classes: `NvsPassthroughConvertor`, `NvsPassthroughFileInfo`
Static/constants: `NvsPassthroughConvertor.NvsPassthroughFileInfo`
Common calls: `currentTimeMillis()`, `getQuickSplicingVideoSavePath()`, `stop()`, `NvsPassthroughFileInfo()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `add()`, `convertMediaFile()`, `setPassthroughConvertorCallback()`, `setVisibility()`

Simple sequence:

```java
mCompileVideoPath = PathUtils.getQuickSplicingVideoSavePath(fileName);
mStreamingContext.stop();
NvsPassthroughConvertor nvsPassthroughConvertor = new NvsPassthroughConvertor();
List<NvsPassthroughConvertor.NvsPassthroughFileInfo> passthroughFileInfos = new ArrayList<>();
NvsPassthroughConvertor.NvsPassthroughFileInfo fileInfo = new NvsPassthroughConvertor.NvsPassthroughFileInfo();
fileInfo.filePath = mClipInfo.getFilePath();
fileInfo.trimIn = mClipInfo.getTrimIn();
fileInfo.trimOut = mClipInfo.getTrimOut();
nvsPassthroughConvertor.setPassthroughConvertorCallback(new FilePassThroughConvertorCallback(), null);
mProgressBar.setVisibility(View.VISIBLE);
```

## `audio-media-078` `selectCreateRatio`

Source: `app/src/main/java/com/meishe/sdkdemo/selectmedia/SelectMediaActivity.java:392`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getAVInfoFromFile`
Common calls: `size()`, `get()`, `getFilePath()`, `getAVInfoFromFile()`, `getStringArray()`, `showToast()`

Simple sequence:

```java
String filePath = clipInfo.getFilePath();
NvsAVFileInfo avFileInfo = NvsStreamingContext.getAVInfoFromFile(filePath, 0);
if (null == avFileInfo) {
String[] versionName = getResources().getStringArray(R.array.clip_load_failed_tips);
```

## `audio-media-079` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:145`

API classes: `NvsAVFileInfo`, `NvsSize`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM`
Common calls: `setClickable()`, `getInstance()`, `finishActivity()`, `setCompileConfigurations()`, `currentTimeMillis()`, `getVideoSavePath()`, `getAVFileInfo()`, `getVideoStreamDimension()`, `compileVideo()`, `getDuration()`

Simple sequence:

```java
superZoomPreviewCloseButton.setClickable(false);
AppManager.getInstance().finishActivity();
mStreamingContext.setCompileConfigurations(null);
mCompileVideoPath = PathUtils.getVideoSavePath(fileName);
NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(mRecordVideoPath);
if (fileInfo != null) {
NvsSize size = fileInfo.getVideoStreamDimension(0);
VideoCompileUtil.compileVideo(mStreamingContext, mTimeline, mCompileVideoPath, 0, mTimeline.getDuration(),
NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, compile_height);
```

## `audio-media-080` `jumpToPreview`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:751`

API classes: `NvsVideoStreamInfo`, `NvsAVFileInfo`, `NvsSize`
Static/constants: `NvsVideoStreamInfo.VIDEO_ROTATION_90`, `NvsVideoStreamInfo.VIDEO_ROTATION_270`
Common calls: `instance()`, `get()`, `size()`, `setFilePath()`, `add()`, `getAVFileInfo()`, `getFilePath()`, `clear()`, `getVideoStreamDimension()`, `getVideoStreamRotation()`, `setVideoResolution()`, `getVideoEditResolution()`

Simple sequence:

```java
clipInfo.setFilePath(mRecordFileList.get(i));
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(pathList.get(0).getFilePath());
NvsSize size = avFileInfo.getVideoStreamDimension(0);
int rotation = avFileInfo.getVideoStreamRotation(0);
if (rotation == NvsVideoStreamInfo.VIDEO_ROTATION_90
|| rotation == NvsVideoStreamInfo.VIDEO_ROTATION_270) {
TimelineData.instance().setVideoResolution(Util.getVideoEditResolution(ratioType));
TimelineData.instance().setMakeRatio(ratioType);
TimelineData.instance().setClipInfoData(pathList);
AppManager.getInstance().jumpActivity(ThemeCaptureActivity.this, ThemePreviewActivity.class, bundle);
```

## `audio-media-081` `addMusic`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:53`

API classes: `NvsAudioClip`, `NvsTimeline`, `NvsAudioTrack`
Common calls: `e()`, `addClip()`, `getFolderPath()`, `getMusic()`, `isEmpty()`, `appendAudioTrack()`, `getMusicDuration()`, `equals()`, `getNeedControlMusicFading()`, `getMusicFadingTime()`, `setFadeOutDuration()`

Simple sequence:

```java
public static void addMusic(NvsTimeline mTimeline, ThemeModel mThemeModel) {
String music = mThemeModel.getMusic();
if (!TextUtils.isEmpty(music)) {
NvsAudioTrack nvsAudioTrack = mTimeline.appendAudioTrack();
if (nvsAudioTrack == null) {
Log.e(TAG, "mTimeline.appendAudioTrack failed");
NvsAudioClip nvsAudioClip = nvsAudioTrack.addClip(mThemeModel.getFolderPath() + File.separator + music, 0);
if ("1".equals(mThemeModel.getNeedControlMusicFading()+"")) {
long musicFadingTime = mThemeModel.getMusicFadingTime();
nvsAudioClip.setFadeOutDuration(musicFadingTime * Constants.US_TIME_BASE);
```

## `audio-media-082` `addMusic`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:56`

API classes: `NvsAudioClip`, `NvsAudioTrack`
Common calls: `e()`, `addClip()`, `getFolderPath()`, `isEmpty()`, `appendAudioTrack()`, `getMusicDuration()`, `equals()`, `getNeedControlMusicFading()`, `getMusicFadingTime()`, `setFadeOutDuration()`

Simple sequence:

```java
if (!TextUtils.isEmpty(music)) {
NvsAudioTrack nvsAudioTrack = mTimeline.appendAudioTrack();
if (nvsAudioTrack == null) {
Log.e(TAG, "mTimeline.appendAudioTrack failed");
NvsAudioClip nvsAudioClip = nvsAudioTrack.addClip(mThemeModel.getFolderPath() + File.separator + music, 0);
if ("1".equals(mThemeModel.getNeedControlMusicFading()+"")) {
long musicFadingTime = mThemeModel.getMusicFadingTime();
nvsAudioClip.setFadeOutDuration(musicFadingTime * Constants.US_TIME_BASE);
```

## `audio-media-083` `appendVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:134`

API classes: `NvsVideoClip`, `NvsTimeline`, `NvsVideoTrack`
Common calls: `getDuration()`, `getStartDuration()`, `appendClip()`, `e()`, `isEmpty()`, `getMusic()`, `setVolumeGain()`, `parseString2Long()`, `d()`, `getNeedDuration()`, `getSource()`, `size()`

Simple sequence:

```java
public static void appendVideoClip(NvsTimeline mTimeline, NvsVideoTrack nvsVideoTrack, ThemePreviewBean previewBean, ThemeModel.ShotInfo shotInfo, ThemeModel mThemeModel) {
String shotFilePath = shotInfo.canPlaced() ? shotInfo.getSource() : mThemeModel.getFolderPath() + File.separator + shotInfo.getSource();
List<ThemeModel.ShotInfo.SpeedInfo> speeds = shotInfo.getSpeed();
long speedStart = NumberUtils.parseString2Long(speedInfo.getStart());
long totalSpeedTime = (long) ((NumberUtils.parseString2Long(speedInfo.getEnd()) -
NumberUtils.parseString2Long(speedInfo.getStart())) *
(speedInfo.getSpeed1()
+ speedInfo.getSpeed0()) / 2);
if (mTimeline.getDuration() - previewBean.getStartDuration() < speedStart) {
long addDuration = speedStart - (mTimeline.getDuration() - previewBean.getStartDuration());
NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(shotFilePath,
if (!TextUtils.isEmpty(mThemeModel.getMusic())) {
nvsVideoClip.setVolumeGain(0, 0);
long duration = mTimeline.getDuration();
NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(shotFilePath,
if (!TextUtils.isEmpty(mThemeModel.getMusic())) {
nvsVideoClip.setVolumeGain(0, 0);
nvsVideoClip.changeVariableSpeed(speedInfo.getSpeed0()
, speedInfo.getSpeed1(), true);
long duration = mTimeline.getDuration() - previewBean.getStartDuration();
if (startSpeed < shotInfo.getNeedDuration()) {
NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(shotFilePath,
startSpeed * Constants.US_TIME_BASE, shotInfo.getNeedDuration() * Constants.US_TIME_BASE);
if (!TextUtils.isEmpty(mThemeModel.getMusic())) {
// ... 6 more SDK-related lines omitted in this compressed snippet ...
```

## `audio-media-084` `appendVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:139`

API classes: `NvsVideoClip`
Common calls: `getDuration()`, `getStartDuration()`, `appendClip()`, `e()`, `isEmpty()`, `getMusic()`, `setVolumeGain()`, `parseString2Long()`, `d()`, `getNeedDuration()`, `size()`, `getStart()`

Simple sequence:

```java
long speedStart = NumberUtils.parseString2Long(speedInfo.getStart());
long totalSpeedTime = (long) ((NumberUtils.parseString2Long(speedInfo.getEnd()) -
NumberUtils.parseString2Long(speedInfo.getStart())) *
(speedInfo.getSpeed1()
+ speedInfo.getSpeed0()) / 2);
if (mTimeline.getDuration() - previewBean.getStartDuration() < speedStart) {
long addDuration = speedStart - (mTimeline.getDuration() - previewBean.getStartDuration());
NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(shotFilePath,
if (!TextUtils.isEmpty(mThemeModel.getMusic())) {
nvsVideoClip.setVolumeGain(0, 0);
long duration = mTimeline.getDuration();
NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(shotFilePath,
if (!TextUtils.isEmpty(mThemeModel.getMusic())) {
nvsVideoClip.setVolumeGain(0, 0);
nvsVideoClip.changeVariableSpeed(speedInfo.getSpeed0()
, speedInfo.getSpeed1(), true);
long duration = mTimeline.getDuration() - previewBean.getStartDuration();
if (startSpeed < shotInfo.getNeedDuration()) {
NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(shotFilePath,
startSpeed * Constants.US_TIME_BASE, shotInfo.getNeedDuration() * Constants.US_TIME_BASE);
if (!TextUtils.isEmpty(mThemeModel.getMusic())) {
nvsVideoClip.setVolumeGain(0, 0);
long duration = mTimeline.getDuration() - previewBean.getStartDuration();
NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(shotFilePath,
// ... 3 more SDK-related lines omitted in this compressed snippet ...
```

## `audio-media-085` `getSinglePool`

Source: `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java:341`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getAVInfoFromFile`
Common calls: `getFilePath()`, `getAVInfoFromFile()`, `e()`, `getDataRate()`

Simple sequence:

```java
for (ClipInfo clipInfo : pathList) {
String filePath = clipInfo.getFilePath();
NvsAVFileInfo avFileInfo = NvsStreamingContext.getAVInfoFromFile(filePath, 0);
Log.e("meicam", ">>>>>>path:" + filePath + "    rate:" + avFileInfo.getDataRate());
```

## `audio-media-086` `getSinglePool`

Source: `app/src/main/java/com/meishe/sdkdemo/urledit/UrlMaterialActivity.java:388`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getAVInfoFromFile`
Common calls: `getDuration()`, `getFilePath()`, `getAVInfoFromFile()`, `setFilePath()`, `setDuration()`, `setInPoint()`, `setOutPoint()`, `setTrimIn()`, `getTrimIn()`, `setTrimOut()`, `getTrimOut()`

Simple sequence:

```java
for (ClipInfo clipInfo : pathList) {
String filePath = clipInfo.getFilePath();
NvsAVFileInfo avFileInfo = NvsStreamingContext.getAVInfoFromFile(filePath, 0);
musicInfo.setFilePath(filePath);
musicInfo.setDuration(avFileInfo.getDuration());
musicInfo.setInPoint(0);
musicInfo.setOutPoint(avFileInfo.getDuration());
musicInfo.setTrimIn(clipInfo.getTrimIn());
musicInfo.setTrimOut(clipInfo.getTrimOut());
```

## `audio-media-087` `createTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:146`

API classes: `NvsTimeline`, `NvsVideoResolution`, `NvsAudioTrack`
Common calls: `appendAudioTrack()`, `instance()`, `getVideoResolution()`, `e()`, `setAttachment()`

Simple sequence:

```java
public static NvsTimeline createTimeline(int width, int height) {
NvsVideoResolution videoResolution = TimelineData.instance().getVideoResolution();
NvsTimeline timeline = newTimeline(videoResolution);
if (timeline == null) {
Log.e(TAG, "failed to create timeline");
if (!buildVideoTrack(timeline)) {
return timeline;
timeline.appendAudioTrack();
setTimelineData(timeline);
return timeline;
```

## `audio-media-088` `applyNoiseSuppression`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:593`

API classes: `NvsVideoClip`, `NvsAudioFx`
Common calls: `appendAudioFx()`, `setIntVal()`

Simple sequence:

```java
private static void applyNoiseSuppression(int noiseSuppressionLevel, NvsVideoClip videoClip) {
if (noiseSuppressionLevel > 0 && null != videoClip) {
NvsAudioFx noiseAudioEffect = videoClip.appendAudioFx(Constants.NOISE_SUPPRESSION_KEY);
if (null != noiseAudioEffect) {
noiseAudioEffect.setIntVal(Constants.NOISE_SUPPRESSION_VALUE_KEY, noiseSuppressionLevel);
```

## `audio-media-089` `applyNoiseSuppression`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:594`

API classes: `NvsAudioFx`
Common calls: `appendAudioFx()`, `setIntVal()`

Simple sequence:

```java
if (noiseSuppressionLevel > 0 && null != videoClip) {
NvsAudioFx noiseAudioEffect = videoClip.appendAudioFx(Constants.NOISE_SUPPRESSION_KEY);
if (null != noiseAudioEffect) {
noiseAudioEffect.setIntVal(Constants.NOISE_SUPPRESSION_VALUE_KEY, noiseSuppressionLevel);
```

## `audio-media-090` `applyVolumeKeyInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:662`

API classes: `NvsConstants`, `NvsPointD`, `NvsControlPointPair`, `NvsVideoClip`, `NvsAudioFx`
Static/constants: `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN`, `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_RIGHT_GAIN`
Common calls: `getVolumeValue()`, `setKeyFrameControlPoint()`, `removeAllKeyframe()`, `setFloatValAtTime()`, `getPreControlPoint()`, `getNextControlPoint()`, `getAudioVolumeFx()`, `isEmpty()`, `entrySet()`, `getKey()`, `getValue()`, `getPreVolumeValue()`

Simple sequence:

```java
public static void applyVolumeKeyInfo(NvsVideoClip videoClip, Map<Long, VolumeKeyInfo> volumeKeyInfoMap) {
NvsAudioFx audioFx = videoClip.getAudioVolumeFx();
audioFx.removeAllKeyframe(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN);
for (Map.Entry<Long, VolumeKeyInfo> entry : entries) {
Long keyTime = entry.getKey();
VolumeKeyInfo value = entry.getValue();
audioFx.setFloatValAtTime(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN, value.getVolumeValue(), keyTime);
audioFx.setFloatValAtTime(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_RIGHT_GAIN, value.getVolumeValue(), keyTime);
if (value.getPreControlPoint() >= 0) {
NvsPointD forwardPoint = new NvsPointD(value.getPreControlPoint(), value.getPreVolumeValue());
NvsPointD backPoint = new NvsPointD(keyTime, value.getVolumeValue());
NvsControlPointPair prePoint = new NvsControlPointPair(forwardPoint, backPoint);
audioFx.setKeyFrameControlPoint(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN, keyTime, prePoint);
if (value.getNextControlPoint() >= 0) {
NvsPointD forwardPoint = new NvsPointD(keyTime, value.getVolumeValue());
NvsPointD backPoint = new NvsPointD(value.getNextControlPoint(), value.getNextVolumeValue());
NvsControlPointPair nextPoint = new NvsControlPointPair(forwardPoint, backPoint);
audioFx.setKeyFrameControlPoint(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_RIGHT_GAIN, keyTime, nextPoint);
```

## `audio-media-091` `getVolumeByKeyTime`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:707`

API classes: `NvsVideoClip`, `NvsAudioFx`, `NvsConstants`
Static/constants: `NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN`
Common calls: `getAudioVolumeFx()`, `getFloatValAtTime()`

Simple sequence:

```java
public static double getVolumeByKeyTime(NvsVideoClip videoClip, long timeStamp) {
NvsAudioFx audioFx = videoClip.getAudioVolumeFx();
return audioFx.getFloatValAtTime(NvsConstants.AUDIO_CLIP_KEY_AUDIO_VOLUME_LEFT_GAIN, timeStamp);
```

## `audio-media-092` `buildTimelineRecordAudio`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1288`

API classes: `NvsAudioClip`, `NvsAudioFx`
Common calls: `getFxID()`, `getInPoint()`, `getTrimIn()`, `setVolumeGain()`, `getVolume()`, `appendFx()`, `removeAllClips()`, `size()`, `get()`, `addClip()`, `getPath()`, `getOutPoint()`

Simple sequence:

```java
if (audioTrack != null) {
audioTrack.removeAllClips();
NvsAudioClip audioClip = audioTrack.addClip(recordAudioInfo.getPath(), recordAudioInfo.getInPoint(), recordAudioInfo.getTrimIn(),
recordAudioInfo.getOutPoint() - recordAudioInfo.getInPoint() + recordAudioInfo.getTrimIn());
if (audioClip != null) {
audioClip.setVolumeGain(recordAudioInfo.getVolume(), recordAudioInfo.getVolume());
if (recordAudioInfo.getFxID() != null && !recordAudioInfo.getFxID().equals(Constants.NO_FX)) {
audioClip.appendFx(recordAudioInfo.getFxID());
int noiseSuppressionLevel = recordAudioInfo.getNoiseSuppressionLevel();
if (noiseSuppressionLevel > 0) {
NvsAudioFx nvsAudioFx = audioClip.appendFx(Constants.NOISE_SUPPRESSION_KEY);
if (null != nvsAudioFx) {
nvsAudioFx.setIntVal(Constants.NOISE_SUPPRESSION_VALUE_KEY, noiseSuppressionLevel);
float audioVolume = TimelineData.instance().getRecordVolume();
audioTrack.setVolumeGain(audioVolume, audioVolume);
```

## `audio-media-093` `applyCropData`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2474`

API classes: `NvsConstants`, `NvsVideoFx`, `NvsTimeline`, `NvsVideoClip`, `NvsAVFileInfo`, `NvsStreamingContext`, `NvsSize`, `NvsVideoResolution`
Static/constants: `NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D`, `NvsConstants.Crop`, `NvsConstants.KEY_MASK_GENERATOR_TYPE`, `NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM`, `NvsConstants.KEY_CROPPER_SCALE_X`, `NvsConstants.KEY_CROPPER_SCALE_Y`, `NvsConstants.KEY_CROP_FULL_TRANSFORM`, `NvsConstants.VALUE_CROP_FULL_TRANSFORM`, `NvsConstants.CUT_KEY_MASK_GENERATOR`, `NvsConstants.CUT_KEY_IS_NORMALIZED_COORD`, `NvsConstants.CUT_FX_TYPE_FOR_TRANSFORM`, `NvsConstants.KEY_CROPPER_TRANS_X`
Common calls: `setFloatVal()`, `get()`, `equals()`, `getRawFxByIndex()`, `appendRawBuiltinFx()`, `setAttachment()`, `getAttachment()`, `getBuiltinVideoFxName()`, `abs()`, `getCropInfo()`, `getRawFxCount()`, `getTransformData()`

Simple sequence:

```java
public static void applyCropData(NvsTimeline mTimeline, NvsVideoClip videoClip, ClipInfo clipInfo) {
CutData cropInfo = clipInfo.getCropInfo();
if ((videoClip == null) || (cropInfo == null) || (null == mTimeline)) {
NvsVideoFx cropperVideoFx = null;
NvsVideoFx extraTransformVideoFx = null;
NvsVideoFx transformVideoFx = null;
int rawFxCount = videoClip.getRawFxCount();
for (int i = 0; i < rawFxCount; i++) {
NvsVideoFx rawVideoFx = videoClip.getRawFxByIndex(i);
if (rawVideoFx != null) {
String attachment = (String) rawVideoFx.getAttachment(NvsConstants.KEY_MASK_GENERATOR_TYPE);
if (TextUtils.equals(rawVideoFx.getBuiltinVideoFxName(), NvsConstants.CUT_KEY_MASK_GENERATOR)
for (int i = 0; i < rawFxCount; i++) {
NvsVideoFx rawVideoFx = videoClip.getRawFxByIndex(i);
if (rawVideoFx != null && TextUtils.equals(rawVideoFx.getBuiltinVideoFxName(), NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D)) {
for (int i = 0; i < rawFxCount; i++) {
NvsVideoFx rawVideoFx = videoClip.getRawFxByIndex(i);
if (rawVideoFx != null && rawVideoFx.getAttachment(NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM) != null) {
if (extraTransformVideoFx == null) {
extraTransformVideoFx = videoClip.appendRawBuiltinFx(NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D);
if (transformVideoFx == null) {
transformVideoFx = videoClip.appendRawBuiltinFx(NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D);
Map<String, Float> transFromData = cropInfo.getTransformData();
if (extraTransformVideoFx != null) {
// ... 44 more SDK-related lines omitted in this compressed snippet ...
```

## `audio-media-094` `setBaseUIClip`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:215`

API classes: `NvsAudioTrack`, `NvsAudioClip`
Common calls: `getInPoint()`, `getAudioTrackByIndex()`, `getIndex()`, `e()`, `getClipCount()`, `getClipByIndex()`

Simple sequence:

```java
mNvsAudioTrack = mTimeline.getAudioTrackByIndex(baseUIClip.getIndex());
if (mNvsAudioTrack == null) {
LogUtils.e("NvsAudioTrack is null");
for (int i = 0; i < mNvsAudioTrack.getClipCount(); i++) {
NvsAudioClip nvsAudioClip = mNvsAudioTrack.getClipByIndex(i);
if (nvsAudioClip.getInPoint() == mMeicamAudioClip.getInPoint()) {
```

## `audio-media-095` `setBaseUIClip`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:220`

API classes: `NvsAudioTrack`
Common calls: `e()`

Simple sequence:

```java
if (mNvsAudioTrack == null) {
LogUtils.e("NvsAudioTrack is null");
```

## `audio-media-096` `onHandActionDown`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:762`

API classes: `NvsVideoClip`, `NvsVideoTrack`, `NvsAVFileInfo`
Static/constants: `NvsVideoClip.VIDEO_CLIP_TYPE_AV`
Common calls: `getVideoType()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getAVFileInfo()`, `getFilePath()`, `getDuration()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
if (videoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {
NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(videoClip.getFilePath());
newDuration = fileInfo.getDuration();
if (videoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV && isLeftHand) {
```

## `audio-media-097` `getAvFileDuration`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:906`

API classes: `NvsVideoClip`, `NvsVideoTrack`, `NvsAVFileInfo`
Static/constants: `NvsVideoClip.VIDEO_CLIP_TYPE_AV`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `e()`, `getClipCount()`, `getVideoType()`, `getAVFileInfo()`, `getFilePath()`, `getDuration()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
if (videoClip == null) {
LogUtils.e("getAvFileDuration: getClipCount: " + videoTrack.getClipCount() + "  index: " + index);
if (videoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {
NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(videoClip.getFilePath());
newDuration = fileInfo.getDuration();
```

## `audio-media-098` `openOriginalVoice`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1020`

API classes: `NvsVideoTrack`
Common calls: `getVideoTrackByIndex()`, `setVolumeGain()`, `getInstance()`, `getMeicamVideoTrackList()`, `isEmpty()`, `get()`, `setIsMute()`

Simple sequence:

```java
if (mTimeline == null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
videoTrack.setVolumeGain(1, 1);
List<MeicamVideoTrack> meicamVideoTrackList = TimelineData.getInstance().getMeicamVideoTrackList();
meicamVideoTrack.setIsMute(false);
```

## `audio-media-099` `freezeFrameClip`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2255`

API classes: `NvsVideoClip`, `NvsVideoFrameRetriever`, `NvsVideoTrack`
Static/constants: `NvsVideoFrameRetriever.VIDEO_FRAME_HEIGHT_GRADE_720`
Common calls: `getObject()`, `getInPoint()`, `getVideoReverse()`, `getOutPoint()`, `getVideoTrackByIndex()`, `getIndex()`, `createVideoFrameRetriever()`, `getReverseFilePath()`, `getFilePath()`, `getFrameAtTime()`, `getTrimIn()`, `currentTimeMillis()`

Simple sequence:

```java
if (mTimeline == null) {
NvsVideoClip editVideoClip = meicamVideoClip.getObject();
boolean isReverseVideo = meicamVideoClip.getVideoReverse();
if (timeStamp <= editVideoClip.getInPoint() || timeStamp >= editVideoClip.getOutPoint()) {
NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(trackIndex);
NvsVideoClip nvsVideoClip = meicamVideoClip.getObject();
int clipIndex = nvsVideoClip.getIndex();
NvsVideoFrameRetriever videoFrameRetriever = mStreamingContext.createVideoFrameRetriever(
isReverseVideo ? meicamVideoClip.getReverseFilePath() : meicamVideoClip.getFilePath());
if (videoFrameRetriever != null) {
Bitmap frameAtTime = videoFrameRetriever.getFrameAtTime(meicamVideoClip.getTrimIn() + timeStamp - nvsVideoClip.getInPoint(),
NvsVideoFrameRetriever.VIDEO_FRAME_HEIGHT_GRADE_720);
String freezeFilePath = PathUtils.getVideoFreezeConvertDir() + File.separator + fileName;
List<MeicamVideoTrack> meicamVideoTrackList = TimelineData.getInstance().getMeicamVideoTrackList();
if (meicamVideoTrack != null) {
clipInfoList = meicamVideoTrack.getClipInfoList();
newMeicamVideoClip.setFilePath(freezeFilePath);
newMeicamVideoClip.setInPoint(getCurrentTimelinePosition());
newMeicamVideoClip.setOutPoint(getCurrentTimelinePosition() + duration);
newMeicamVideoClip.setTrimIn(0);
newMeicamVideoClip.setTrimOut(duration);
newMeicamVideoClip.setVideoType(CommonData.CLIP_IMAGE);
TimelineUtil.rebuildTimeline(mTimeline);
if (isPip) {
// ... 1 more SDK-related lines omitted in this compressed snippet ...
```

## `audio-media-100` `setVideoConvert`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2341`

API classes: `NvsVideoTrack`, `NvsAVFileInfo`, `NvsVideoClip`
Common calls: `getObject()`, `getTrimOut()`, `getTrimIn()`, `getInstance()`, `getMeicamVideoTrackList()`, `get()`, `getAVFileInfo()`, `getFilePath()`, `getDuration()`, `setVideoReverse()`, `getVideoReverse()`, `getIndex()`

Simple sequence:

```java
if (mTimeline == null) {
MeicamVideoTrack meicamVideoTrack = TimelineData.getInstance().getMeicamVideoTrackList().get(MAIN_TRACK_INDEX);
NvsVideoTrack videoTrack = meicamVideoTrack.getObject();
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(meicamVideoClip.getFilePath());
long duration = avFileInfo.getDuration();
long trimOut = meicamVideoClip.getTrimOut();
long clipDuration = meicamVideoClip.getTrimOut() - meicamVideoClip.getTrimIn();
meicamVideoClip.setVideoReverse(!meicamVideoClip.getVideoReverse());
NvsVideoClip nvsVideoClip = meicamVideoClip.getObject();
int index = nvsVideoClip.getIndex();
videoTrack.removeClip(index, false);
meicamVideoClip.setTrimIn(duration - trimOut);
meicamVideoClip.setTrimOut(meicamVideoClip.getTrimIn() + clipDuration);
TimelineUtil.clearAllBuildInTransition(mTimeline);
TimelineUtil.setTransition(mTimeline, meicamVideoTrack.getTransitionInfoList());
if (mOnTimelineChangeListener != null) {
mOnTimelineChangeListener.onTimelineChanged(mTimeline, true);
```

## `audio-media-101` `setKeepAudioPitch`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:109`

API classes: `NvsAudioClip`
Common calls: `setVolumeGain()`

Simple sequence:

```java
NvsAudioClip nvsAudioClip = getObject();
nvsAudioClip.setVolumeGain(volume, volume);
```

## `audio-media-102` `getSpeed`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:122`

API classes: `NvsAudioClip`
Common calls: `changeSpeed()`, `setKeepAudioPitch()`, `setInPoint()`, `getInPoint()`, `setOutPoint()`, `getOutPoint()`

Simple sequence:

```java
NvsAudioClip nvsAudioClip = getObject();
nvsAudioClip.changeSpeed(speed, isChangeVoice);
this.setKeepAudioPitch(isChangeVoice);
this.setInPoint(nvsAudioClip.getInPoint());
this.setOutPoint(nvsAudioClip.getOutPoint());
```

## `audio-media-103` `getFadeInDuration`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:139`

API classes: `NvsAudioClip`
Common calls: `setFadeInDuration()`

Simple sequence:

```java
NvsAudioClip nvsAudioClip = getObject();
nvsAudioClip.setFadeInDuration(fadeInDuration);
```

## `audio-media-104` `getFadeOutDuration`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:152`

API classes: `NvsAudioClip`
Common calls: `setFadeOutDuration()`

Simple sequence:

```java
NvsAudioClip nvsAudioClip = getObject();
nvsAudioClip.setFadeOutDuration(fadeOutDuration);
```

## `audio-media-105` `getMeicamAudioFxes`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:189`

API classes: `NvsAudioClip`
Common calls: `removeFx()`, `getType()`, `equals()`, `appendFx()`, `getDesc()`

Simple sequence:

```java
NvsAudioClip nvsAudioClip = getObject();
if (mMeicamAudioFxes == null) {
nvsAudioClip.removeFx(0);
for (MeicamAudioFx meicamAudioFx : mMeicamAudioFxes) {
String type = meicamAudioFx.getType();
if (TYPE_BUILD_IN.equals(type)) {
nvsAudioClip.removeFx(0);
nvsAudioClip.appendFx(meicamAudioFx.getDesc());
```

## `audio-media-106` `loadData`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:209`

API classes: `NvsAudioClip`, `NvsAudioFx`, `NvsVolume`
Common calls: `getFilePath()`, `getInPoint()`, `getOutPoint()`, `getTrimIn()`, `getTrimOut()`, `getSpeed()`, `getFadeInDuration()`, `getFadeOutDuration()`, `getFxCount()`, `clear()`, `getFxByIndex()`, `getBuiltinAudioFxName()`

Simple sequence:

```java
public void loadData(NvsAudioClip audioClip) {
setFilePath(audioClip.getFilePath());
setInPoint(audioClip.getInPoint());
setOutPoint(audioClip.getOutPoint());
trimIn = audioClip.getTrimIn();
trimOut = audioClip.getTrimOut();
speed = audioClip.getSpeed();
fadeInDuration = audioClip.getFadeInDuration();
fadeOutDuration = audioClip.getFadeOutDuration();
int count = audioClip.getFxCount();
if (count > 0) {
NvsAudioFx audioFx = audioClip.getFxByIndex(0);
MeicamAudioFx meicamAudioFx = new MeicamAudioFx(0, TYPE_BUILD_IN, audioFx.getBuiltinAudioFxName());
NvsVolume volumeGain = audioClip.getVolumeGain();
```

## `audio-media-107` `setTransitionInfoList`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioTrack.java:33`

API classes: `NvsAudioTrack`, `NvsTimeline`
Common calls: `appendAudioTrack()`

Simple sequence:

```java
public NvsAudioTrack bindToTimeline(NvsTimeline timeline) {
if (timeline == null) {
NvsAudioTrack track = timeline.appendAudioTrack();
```

## `audio-media-108` `getAudioTrackMaxDuration`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:511`

API classes: `NvsAudioTrack`
Common calls: `size()`, `get()`, `getObject()`, `getDuration()`, `max()`

Simple sequence:

```java
NvsAudioTrack nvsVideoTrack = videoTrack.getObject();
if (nvsVideoTrack != null) {
long trackDuration = nvsVideoTrack.getDuration();
```

## `audio-media-109` `addAudioClipInfoByTrackIndex`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:683`

API classes: `NvsAudioTrack`
Common calls: `setObject()`, `add()`, `getInstance()`, `getMeicamAudioTrackList()`, `getIndex()`, `size()`, `get()`, `getClipInfoList()`, `sort()`

Simple sequence:

```java
public static void addAudioClipInfoByTrackIndex(NvsAudioTrack nvsAudioTrack, MeicamAudioClip meicamAudioClip) {
List<MeicamAudioTrack> mMeicamAudioTrackList = TimelineData.getInstance().getMeicamAudioTrackList();
int trackIndex = nvsAudioTrack.getIndex();
meicamVideoTrack.setObject(nvsAudioTrack);
if (meicamVideoTrack != null) {
List<ClipInfo<?>> meicamVideoClipList = meicamVideoTrack.getClipInfoList();
```

## `audio-media-110` `setThemeQuiet`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1070`

API classes: `NvsTimeline`
Common calls: `getInstance()`, `getMeicamTheme()`, `getThemePackageId()`, `isEmpty()`, `setThemeMusicVolumeGain()`

Simple sequence:

```java
public static void setThemeQuiet(NvsTimeline nvsTimeline) {
MeicamTheme meicamTheme = TimelineData.getInstance().getMeicamTheme();
if (meicamTheme != null) {
String themePackageId = meicamTheme.getThemePackageId();
if (!TextUtils.isEmpty(themePackageId)) {
nvsTimeline.setThemeMusicVolumeGain(0f, 0f);
```

## `audio-media-111` `restoreThemeVolume`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1084`

API classes: `NvsTimeline`
Common calls: `getInstance()`, `getMeicamTheme()`, `getThemePackageId()`, `isEmpty()`, `setThemeMusicVolumeGain()`

Simple sequence:

```java
public static void restoreThemeVolume(NvsTimeline nvsTimeline) {
MeicamTheme meicamTheme = TimelineData.getInstance().getMeicamTheme();
if (meicamTheme != null) {
String themePackageId = meicamTheme.getThemePackageId();
if (!TextUtils.isEmpty(themePackageId)) {
nvsTimeline.setThemeMusicVolumeGain(1.0f, 1.0f);
```

## `audio-media-112` `getVideoDuration`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:429`

API classes: `NvsAVFileInfo`
Common calls: `e()`, `getAVFileInfo()`, `getDuration()`

Simple sequence:

```java
if (mStreamingContext == null) {
Log.e(TAG, "getVideoDuration: mStreamingContext is null!");
NvsAVFileInfo fileInfo = mStreamingContext.getAVFileInfo(videoPath);
return fileInfo.getDuration();
```

## `audio-media-113` `convertFile`

Source: `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java:85`

API classes: `NvsMediaFileConvertor`, `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`, `NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT`
Common calls: `convertMeidaFile()`, `isFileExists()`, `e()`, `getFileName()`, `getVideoConvertDir()`, `currentTimeMillis()`, `setMeidaFileConvertorCallback()`, `getInstance()`, `getAVFileInfo()`, `getDuration()`, `isCovert4KFileWhiteList()`, `put()`

Simple sequence:

```java
if (mMediaFileConvertor == null) {
mMediaFileConvertor = new NvsMediaFileConvertor();
String fileName = PathUtils.getFileName(path);
mDestFilePath = PathUtils.getVideoConvertDir() + File.separator + "MY_" + System.currentTimeMillis() + "_" + fileName;
mMediaFileConvertor.setMeidaFileConvertorCallback(this, null);
NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(path);
if (avFileInfo != null) {
duration = avFileInfo.getDuration();
hashtable.put(NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT, 1080);
```

## `audio-media-114` `convertFile`

Source: `libEngine/src/main/java/com/meishe/engine/util/ConvertFileManager.java:90`

API classes: `NvsMediaFileConvertor`

Simple sequence:

```java
if (mMediaFileConvertor == null) {
mMediaFileConvertor = new NvsMediaFileConvertor();
```

## `audio-media-115` `buildTimelineMusic`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:329`

API classes: `NvsAudioTrack`, `NvsTimeline`
Common calls: `getInstance()`, `isEmpty()`, `bindToTimeline()`, `audioTrackCount()`, `getAudioTrackByIndex()`, `removeAllClips()`, `getMeicamTheme()`, `getThemePackageId()`, `setThemeMusicVolumeGain()`, `getMeicamAudioTrackList()`, `e()`, `getClipInfoList()`

Simple sequence:

```java
public static boolean buildTimelineMusic(NvsTimeline timeline) {
int count = timeline.audioTrackCount();
for (int index = 0; index < count; index++) {
NvsAudioTrack audioTrackByIndex = timeline.getAudioTrackByIndex(index);
audioTrackByIndex.removeAllClips();
MeicamTheme meicamTheme = TimelineData.getInstance().getMeicamTheme();
if (meicamTheme != null) {
String themePackageId = meicamTheme.getThemePackageId();
if (!TextUtils.isEmpty(themePackageId)) {
timeline.setThemeMusicVolumeGain(1.0f, 1.0f);
List<MeicamAudioTrack> meicamAudioTrackList = TimelineData.getInstance().getMeicamAudioTrackList();
for (MeicamAudioTrack meicamAudioTrack : meicamAudioTrackList) {
NvsAudioTrack audioTrack = meicamAudioTrack.bindToTimeline(timeline);
List<ClipInfo<?>> meicamAudioClipList = meicamAudioTrack.getClipInfoList();
```

## `audio-media-116` `buildTimelineMusic`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:332`

API classes: `NvsAudioTrack`
Common calls: `getAudioTrackByIndex()`, `removeAllClips()`

Simple sequence:

```java
for (int index = 0; index < count; index++) {
NvsAudioTrack audioTrackByIndex = timeline.getAudioTrackByIndex(index);
audioTrackByIndex.removeAllClips();
```

## `audio-media-117` `buildTimelineRecordAudio`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:451`

API classes: `NvsTimeline`, `NvsAudioTrack`
Common calls: `size()`, `get()`, `getInstance()`, `getMeicamAudioTrackList()`, `getClipInfoList()`, `getAudioTrackByIndex()`, `getIndex()`, `appendAudioTrack()`, `bindToTimeline()`

Simple sequence:

```java
public static void buildTimelineRecordAudio(NvsTimeline timeline) {
if (timeline == null) {
List<MeicamAudioTrack> meicamAudioTrackList = TimelineData.getInstance().getMeicamAudioTrackList();
NvsAudioTrack audioTrack = null;
List<ClipInfo<?>> meicamAudioClipList = meicamAudioTrack.getClipInfoList();
audioTrack = timeline.getAudioTrackByIndex(meicamAudioTrack.getIndex());
if (audioTrack == null) {
audioTrack = timeline.appendAudioTrack();
```

## `audio-media-118` `newTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:510`

API classes: `NvsTimeline`, `NvsVideoResolution`, `NvsStreamingContext`, `NvsRational`, `NvsAudioResolution`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `e()`, `getInstance()`, `getMainTrackVideoClip()`, `size()`, `get()`, `getFilePath()`, `initStreamContext()`, `setNvsRational()`, `createTimeline()`, `getNvsRational()`

Simple sequence:

```java
public static NvsTimeline newTimeline(NvsVideoResolution videoResolution) {
List<ClipInfo<?>> clipInfos = TimelineDataUtil.getMainTrackVideoClip();
videoResolution = getVideoEditResolutionByClip(meicamVideoClip.getFilePath());
NvsStreamingContext context = NvsStreamingContext.getInstance();
if (context == null) {
context = EditorEngine.getInstance().initStreamContext();
if (context == null) {
LogUtils.e("failed to get streamingContext");
NvsVideoResolution nvsVideoResolution = videoResolution;
nvsVideoResolution.imagePAR = new NvsRational(1, 1);
TimelineData.getInstance().setNvsRational(new NvsRational(25, 1));
NvsAudioResolution nvsAudioResolution = new NvsAudioResolution();
NvsTimeline timeline = context.createTimeline(nvsVideoResolution, TimelineData.getInstance().getNvsRational(), nvsAudioResolution);
return timeline;
```

## `audio-media-119` `applyTheme`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:712`

API classes: `NvsTimeline`, `NvsAudioTrack`
Common calls: `getInstance()`, `setThemeMusicVolumeGain()`, `getMeicamAudioTrackList()`, `getMeicamTheme()`, `getThemePackageId()`, `removeCurrentTheme()`, `isEmpty()`, `applyTheme()`, `e()`, `size()`, `iterator()`, `hasNext()`

Simple sequence:

```java
public static boolean applyTheme(NvsTimeline timeline) {
if (timeline == null) {
MeicamTheme meicamTheme = TimelineData.getInstance().getMeicamTheme();
String themeId = meicamTheme.getThemePackageId();
timeline.removeCurrentTheme();
if (!timeline.applyTheme(themeId)) {
timeline.setThemeMusicVolumeGain(1.0f, 1.0f);
List<MeicamAudioTrack> meicamAudioTrackList = TimelineData.getInstance().getMeicamAudioTrackList();
NvsAudioTrack nvsAudioTrack = meicamAudioTrack.getObject();
timeline.removeAudioTrack(nvsAudioTrack.getIndex());
```

## `audio-media-120` `getVideoEditResolutionByClip`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:848`

API classes: `NvsVideoResolution`, `NvsAVFileInfo`, `NvsStreamingContext`, `NvsSize`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `getAVFileInfo()`, `getVideoStreamDimension()`, `getVideoStreamRotation()`, `d()`

Simple sequence:

```java
public static NvsVideoResolution getVideoEditResolutionByClip(String path) {
NvsVideoResolution videoEditRes = new NvsVideoResolution();
NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(path);
NvsSize dimension = avFileInfo.getVideoStreamDimension(0);
int streamRotation = avFileInfo.getVideoStreamRotation(0);
```

## `audio-media-121` `checkVideoAssetIs4K`

Source: `libEngine/src/main/java/com/meishe/engine/util/WhiteList.java:55`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`, `NvsSize`
Static/constants: `NvsStreamingContext.getInstance`, `NvsAVFileInfo.AV_FILE_TYPE_AUDIOVIDEO`
Common calls: `getInstance()`, `getAVFileInfo()`, `getAVFileType()`, `getVideoStreamDimension()`

Simple sequence:

```java
NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(path);
if (avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_AUDIOVIDEO) {
NvsSize nvsSize = avFileInfo.getVideoStreamDimension(0);
```

## `audio-media-122` `checkVideoAssetIs4K`

Source: `libEngine/src/main/java/com/meishe/engine/util/WhiteList.java:60`

API classes: `NvsAVFileInfo`, `NvsSize`
Static/constants: `NvsAVFileInfo.AV_FILE_TYPE_AUDIOVIDEO`
Common calls: `getAVFileType()`, `getVideoStreamDimension()`

Simple sequence:

```java
if (avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_AUDIOVIDEO) {
NvsSize nvsSize = avFileInfo.getVideoStreamDimension(0);
```
