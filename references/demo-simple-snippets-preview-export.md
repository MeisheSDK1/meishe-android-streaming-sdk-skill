# Demo Simple Snippets - Preview Playback Export

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: live window connection, playback, seek, engine state checks, compile/export, image grab, thumbnail generation, and retriever flows.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [preview-export-001 onStop](#preview-export-001-onstop)
- [preview-export-002 onStop](#preview-export-002-onstop)
- [preview-export-003 initListener](#preview-export-003-initlistener)
- [preview-export-004 setCompileCallback](#preview-export-004-setcompilecallback)
- [preview-export-005 onCompileProgress](#preview-export-005-oncompileprogress)
- [preview-export-006 onResume](#preview-export-006-onresume)
- [preview-export-007 LiveWindow](#preview-export-007-livewindow)
- [preview-export-008 onPlaybackPreloadingCompletion](#preview-export-008-onplaybackpreloadingcompletion)
- [preview-export-009 onPlaybackStopped](#preview-export-009-onplaybackstopped)
- [preview-export-010 onPlaybackStopped](#preview-export-010-onplaybackstopped)
- [preview-export-011 onPlaybackEOF](#preview-export-011-onplaybackeof)
- [preview-export-012 playVideo](#preview-export-012-playvideo)
- [preview-export-013 isFlashOn](#preview-export-013-isflashon)
- [preview-export-014 initRootView](#preview-export-014-initrootview)
- [preview-export-015 seekTimeline](#preview-export-015-seektimeline)
- [preview-export-016 getEngineState](#preview-export-016-getenginestate)
- [preview-export-017 initCompileVideoFragment](#preview-export-017-initcompilevideofragment)
- [preview-export-018 initCompileVideoFragment](#preview-export-018-initcompilevideofragment)
- [preview-export-019 compileProgress](#preview-export-019-compileprogress)
- [preview-export-020 compileFinished](#preview-export-020-compilefinished)
- [preview-export-021 compileFailed](#preview-export-021-compilefailed)
- [preview-export-022 connectTimelineWithLiveWindow](#preview-export-022-connecttimelinewithlivewindow)
- [preview-export-023 connectTimelineWithLiveWindow](#preview-export-023-connecttimelinewithlivewindow)
- [preview-export-024 onPlaybackPreloadingCompletion](#preview-export-024-onplaybackpreloadingcompletion)
- [preview-export-025 onPlaybackStopped](#preview-export-025-onplaybackstopped)
- [preview-export-026 onPlaybackTimelinePosition](#preview-export-026-onplaybacktimelineposition)
- [preview-export-027 changeProgress](#preview-export-027-changeprogress)
- [preview-export-028 stop](#preview-export-028-stop)
- [preview-export-029 isPlaying](#preview-export-029-isplaying)
- [preview-export-030 onTouch](#preview-export-030-ontouch)
- [preview-export-031 compileProgress](#preview-export-031-compileprogress)
- [preview-export-032 compileFinished](#preview-export-032-compilefinished)
- [preview-export-033 compileFailed](#preview-export-033-compilefailed)
- [preview-export-034 onPlaybackPreloadingCompletion](#preview-export-034-onplaybackpreloadingcompletion)
- [preview-export-035 onPlaybackStopped](#preview-export-035-onplaybackstopped)
- [preview-export-036 onPlaybackEOF](#preview-export-036-onplaybackeof)
- [preview-export-037 startPlay](#preview-export-037-startplay)
- [preview-export-038 startPlay](#preview-export-038-startplay)
- [preview-export-039 updateSequenceView](#preview-export-039-updatesequenceview)
- [preview-export-040 updateSequenceView](#preview-export-040-updatesequenceview)
- [preview-export-041 playBackEOF](#preview-export-041-playbackeof)
- [preview-export-042 playbackTimelinePosition](#preview-export-042-playbacktimelineposition)
- [preview-export-043 streamingEngineStateChanged](#preview-export-043-streamingenginestatechanged)
- [preview-export-044 onClick](#preview-export-044-onclick)
- [preview-export-045 seekTimeline](#preview-export-045-seektimeline)
- [preview-export-046 stopEngine](#preview-export-046-stopengine)
- [preview-export-047 stopEngine](#preview-export-047-stopengine)
- [preview-export-048 onHiddenChanged](#preview-export-048-onhiddenchanged)
- [preview-export-049 onHiddenChanged](#preview-export-049-onhiddenchanged)
- [preview-export-050 initCompileCallBack](#preview-export-050-initcompilecallback)
- [preview-export-051 onCompileProgress](#preview-export-051-oncompileprogress)
- [preview-export-052 initListener](#preview-export-052-initlistener)
- [preview-export-053 OnCenterTextClick](#preview-export-053-oncentertextclick)
- [preview-export-054 OnRightTextClick](#preview-export-054-onrighttextclick)
- [preview-export-055 OnRightTextClick](#preview-export-055-onrighttextclick)
- [preview-export-056 compileProgress](#preview-export-056-compileprogress)
- [preview-export-057 compileFinished](#preview-export-057-compilefinished)
- [preview-export-058 compileFailed](#preview-export-058-compilefailed)
- [preview-export-059 initDrawRectListener](#preview-export-059-initdrawrectlistener)
- [preview-export-060 connectTimelineWithLiveWindow](#preview-export-060-connecttimelinewithlivewindow)
- [preview-export-061 connectTimelineWithLiveWindow](#preview-export-061-connecttimelinewithlivewindow)
- [preview-export-062 onPlaybackPreloadingCompletion](#preview-export-062-onplaybackpreloadingcompletion)
- [preview-export-063 onResume](#preview-export-063-onresume)
- [preview-export-064 playVideo](#preview-export-064-playvideo)
- [preview-export-065 seekTimeline](#preview-export-065-seektimeline)
- [preview-export-066 seekTimeline](#preview-export-066-seektimeline)
- [preview-export-067 stopEngine](#preview-export-067-stopengine)
- [preview-export-068 stopEngine](#preview-export-068-stopengine)
- [preview-export-069 controllerOperation](#preview-export-069-controlleroperation)
- [preview-export-070 controllerOperation](#preview-export-070-controlleroperation)
- [preview-export-071 onStartTrackingTouch](#preview-export-071-onstarttrackingtouch)
- [preview-export-072 playBackEOF](#preview-export-072-playbackeof)
- [preview-export-073 connectTimelineWithLiveWindow](#preview-export-073-connecttimelinewithlivewindow)
- [preview-export-074 connectTimelineWithLiveWindow](#preview-export-074-connecttimelinewithlivewindow)
- [preview-export-075 onPlaybackPreloadingCompletion](#preview-export-075-onplaybackpreloadingcompletion)
- [preview-export-076 getCurrentEngineState](#preview-export-076-getcurrentenginestate)
- [preview-export-077 onHiddenChanged](#preview-export-077-onhiddenchanged)
- [preview-export-078 controllerOperation](#preview-export-078-controlleroperation)
- [preview-export-079 onClick](#preview-export-079-onclick)
- [preview-export-080 onStartTrackingTouch](#preview-export-080-onstarttrackingtouch)
- [preview-export-081 initListener](#preview-export-081-initlistener)
- [preview-export-082 initListener](#preview-export-082-initlistener)
- [preview-export-083 initListener](#preview-export-083-initlistener)
- [preview-export-084 playBackEOF](#preview-export-084-playbackeof)
- [preview-export-085 initListener](#preview-export-085-initlistener)
- [preview-export-086 initListener](#preview-export-086-initlistener)
- [preview-export-087 initListener](#preview-export-087-initlistener)
- [preview-export-088 initListener](#preview-export-088-initlistener)
- [preview-export-089 OnCenterTextClick](#preview-export-089-oncentertextclick)
- [preview-export-090 playBackEOF](#preview-export-090-playbackeof)
- [preview-export-091 onTouch](#preview-export-091-ontouch)
- [preview-export-092 playBackEOF](#preview-export-092-playbackeof)
- [preview-export-093 playStopped](#preview-export-093-playstopped)
- [preview-export-094 compileProgress](#preview-export-094-compileprogress)
- [preview-export-095 compileFinished](#preview-export-095-compilefinished)
- [preview-export-096 compileFailed](#preview-export-096-compilefailed)
- [preview-export-097 removeTimeline](#preview-export-097-removetimeline)
- [preview-export-098 updateSequenceView](#preview-export-098-updatesequenceview)
- [preview-export-099 getSqView](#preview-export-099-getsqview)
- [preview-export-100 playBackEOF](#preview-export-100-playbackeof)
- [preview-export-101 setOnScrollListener](#preview-export-101-setonscrolllistener)
- [preview-export-102 getSequenceWidth](#preview-export-102-getsequencewidth)
- [preview-export-103 playBackEOF](#preview-export-103-playbackeof)
- [preview-export-104 initLiveWindowListener](#preview-export-104-initlivewindowlistener)
- [preview-export-105 onPlaybackPreloadingCompletion](#preview-export-105-onplaybackpreloadingcompletion)
- [preview-export-106 configureLiveWindow](#preview-export-106-configurelivewindow)
- [preview-export-107 setTimeline](#preview-export-107-settimeline)
- [preview-export-108 getCurrentEngineState](#preview-export-108-getcurrentenginestate)
- [preview-export-109 onDestroy](#preview-export-109-ondestroy)
- [preview-export-110 initUiListener](#preview-export-110-inituilistener)
- [preview-export-111 onClick](#preview-export-111-onclick)
- [preview-export-112 setOnClickListener](#preview-export-112-setonclicklistener)
- [preview-export-113 onClick](#preview-export-113-onclick)
- [preview-export-114 onTouch](#preview-export-114-ontouch)
- [preview-export-115 compileProgress](#preview-export-115-compileprogress)
- [preview-export-116 compileFinished](#preview-export-116-compilefinished)
- [preview-export-117 compileFailed](#preview-export-117-compilefailed)
- [preview-export-118 initStreamingContext](#preview-export-118-initstreamingcontext)
- [preview-export-119 onPlaybackPreloadingCompletion](#preview-export-119-onplaybackpreloadingcompletion)
- [preview-export-120 onPlaybackStopped](#preview-export-120-onplaybackstopped)
- [preview-export-121 onFirstVideoFramePresented](#preview-export-121-onfirstvideoframepresented)
- [preview-export-122 initSequenceView](#preview-export-122-initsequenceview)
- [preview-export-123 initSequenceView](#preview-export-123-initsequenceview)
- [preview-export-124 seekTimeline](#preview-export-124-seektimeline)
- [preview-export-125 setOnClickListener](#preview-export-125-setonclicklistener)
- [preview-export-126 onTouch](#preview-export-126-ontouch)
- [preview-export-127 compileProgress](#preview-export-127-compileprogress)
- [preview-export-128 compileFinished](#preview-export-128-compilefinished)
- [preview-export-129 compileFailed](#preview-export-129-compilefailed)
- [preview-export-130 compileVideoCancel](#preview-export-130-compilevideocancel)
- [preview-export-131 onPlaybackPreloadingCompletion](#preview-export-131-onplaybackpreloadingcompletion)
- [preview-export-132 onPlaybackStopped](#preview-export-132-onplaybackstopped)
- [preview-export-133 onBackPressed](#preview-export-133-onbackpressed)
- [preview-export-134 onPlaybackPreloadingCompletion](#preview-export-134-onplaybackpreloadingcompletion)
- [preview-export-135 onPlaybackStopped](#preview-export-135-onplaybackstopped)
- [preview-export-136 OnCancelBtnClicked](#preview-export-136-oncancelbtnclicked)
- [preview-export-137 onFirstVideoFramePresented](#preview-export-137-onfirstvideoframepresented)
- [preview-export-138 onCompileProgress](#preview-export-138-oncompileprogress)
- [preview-export-139 onCompileFailed](#preview-export-139-oncompilefailed)
- [preview-export-140 onClick](#preview-export-140-onclick)
- [preview-export-141 onClick](#preview-export-141-onclick)
- [preview-export-142 playVideo](#preview-export-142-playvideo)
- [preview-export-143 seekTimeline](#preview-export-143-seektimeline)
- [preview-export-144 OnCenterTextClick](#preview-export-144-oncentertextclick)
- [preview-export-145 compileProgress](#preview-export-145-compileprogress)
- [preview-export-146 compileFinished](#preview-export-146-compilefinished)
- [preview-export-147 compileFailed](#preview-export-147-compilefailed)
- [preview-export-148 initRootView](#preview-export-148-initrootview)
- [preview-export-149 compileProgress](#preview-export-149-compileprogress)
- [preview-export-150 compileFinished](#preview-export-150-compilefinished)
- [preview-export-151 compileFailed](#preview-export-151-compilefailed)
- [preview-export-152 setLiveWindowRatio](#preview-export-152-setlivewindowratio)
- [preview-export-153 playBackEOF](#preview-export-153-playbackeof)
- [preview-export-154 onResume](#preview-export-154-onresume)
- [preview-export-155 onCompileProgress](#preview-export-155-oncompileprogress)
- [preview-export-156 updateSequenceView](#preview-export-156-updatesequenceview)
- [preview-export-157 updateSequenceView](#preview-export-157-updatesequenceview)
- [preview-export-158 addCutTimeline](#preview-export-158-addcuttimeline)
- [preview-export-159 onBackPressed](#preview-export-159-onbackpressed)
- [preview-export-160 onBackPressed](#preview-export-160-onbackpressed)
- [preview-export-161 initListener](#preview-export-161-initlistener)
- [preview-export-162 onCompileProgress](#preview-export-162-oncompileprogress)
- [preview-export-163 playTimeline](#preview-export-163-playtimeline)
- [preview-export-164 initListener](#preview-export-164-initlistener)
- [preview-export-165 onProgressChange](#preview-export-165-onprogresschange)
- [preview-export-166 onClick](#preview-export-166-onclick)
- [preview-export-167 onFirstVideoFramePresented](#preview-export-167-onfirstvideoframepresented)
- [preview-export-168 onPlaybackPreloadingCompletion](#preview-export-168-onplaybackpreloadingcompletion)
- [preview-export-169 onPlaybackStopped](#preview-export-169-onplaybackstopped)
- [preview-export-170 onPlaybackEOF](#preview-export-170-onplaybackeof)
- [preview-export-171 setCompileVideoRes](#preview-export-171-setcompilevideores)
- [preview-export-172 compileVideo](#preview-export-172-compilevideo)
- [preview-export-173 getCompileConfigurations](#preview-export-173-getcompileconfigurations)
- [preview-export-174 setLiveWindowRatio](#preview-export-174-setlivewindowratio)
- [preview-export-175 setLiveWindowSize](#preview-export-175-setlivewindowsize)
- [preview-export-176 connectTimeline](#preview-export-176-connecttimeline)
- [preview-export-177 connectTimeline](#preview-export-177-connecttimeline)
- [preview-export-178 onPlaybackPreloadingCompletion](#preview-export-178-onplaybackpreloadingcompletion)
- [preview-export-179 playVideo](#preview-export-179-playvideo)
- [preview-export-180 playVideo](#preview-export-180-playvideo)
- [preview-export-181 playVideo](#preview-export-181-playvideo)
- [preview-export-182 seekTimeline](#preview-export-182-seektimeline)
- [preview-export-183 setOnScrollListener](#preview-export-183-setonscrolllistener)
- [preview-export-184 getSequenceWidth](#preview-export-184-getsequencewidth)
- [preview-export-185 seekTimeline](#preview-export-185-seektimeline)
- [preview-export-186 playVideo](#preview-export-186-playvideo)
- [preview-export-187 setLiveWindrowSize](#preview-export-187-setlivewindrowsize)
- [preview-export-188 getLiveWindrowSize](#preview-export-188-getlivewindrowsize)
- [preview-export-189 connectTimelineWithLiveWindow](#preview-export-189-connecttimelinewithlivewindow)
- [preview-export-190 connectTimelineWithLiveWindow](#preview-export-190-connecttimelinewithlivewindow)
- [preview-export-191 onPlaybackPreloadingCompletion](#preview-export-191-onplaybackpreloadingcompletion)
- [preview-export-192 onFirstVideoFramePresented](#preview-export-192-onfirstvideoframepresented)
- [preview-export-193 isPlaying](#preview-export-193-isplaying)
- [preview-export-194 grabImageFromTimelineAsync](#preview-export-194-grabimagefromtimelineasync)
- [preview-export-195 grabImageFromTimelineAsync](#preview-export-195-grabimagefromtimelineasync)
- [preview-export-196 grabImageFromTimelineAsync](#preview-export-196-grabimagefromtimelineasync)
- [preview-export-197 setImageGrabberCallback](#preview-export-197-setimagegrabbercallback)
- [preview-export-198 grabBitmapFromTimeline](#preview-export-198-grabbitmapfromtimeline)
- [preview-export-199 compileTimeLineCustom](#preview-export-199-compiletimelinecustom)
- [preview-export-200 compileTimeLine](#preview-export-200-compiletimeline)
- [preview-export-201 setThumbnailSequenceDescArray](#preview-export-201-setthumbnailsequencedescarray)
- [preview-export-202 setThumbnailImageFillMode](#preview-export-202-setthumbnailimagefillmode)
- [preview-export-203 setThumbnailAspectRatio](#preview-export-203-setthumbnailaspectratio)
- [preview-export-204 setPixelPerMicrosecond](#preview-export-204-setpixelpermicrosecond)
- [preview-export-205 setStartPadding](#preview-export-205-setstartpadding)
- [preview-export-206 setEndPadding](#preview-export-206-setendpadding)
- [preview-export-207 setMaxTimelinePosToScroll](#preview-export-207-setmaxtimelinepostoscroll)
- [preview-export-208 mapTimelinePosFromX](#preview-export-208-maptimelineposfromx)
- [preview-export-209 mapXFromTimelinePos](#preview-export-209-mapxfromtimelinepos)
- [preview-export-210 scaleWithAnchor](#preview-export-210-scalewithanchor)
- [preview-export-211 setOnScrollChangeListenser](#preview-export-211-setonscrollchangelistenser)
- [preview-export-212 getOnScrollChangeListenser](#preview-export-212-getonscrollchangelistenser)
- [preview-export-213 onLayout](#preview-export-213-onlayout)
- [preview-export-214 onAttachedToWindow](#preview-export-214-onattachedtowindow)
<!-- END GENERATED CONTENTS -->

## `preview-export-001` `onStop`

Source: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:68`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `getStreamingEngineState()`, `stop()`

Simple sequence:

```java
if (isBackgroud) {
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
mStreamingContext.stop();
```

## `preview-export-002` `onStop`

Source: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:69`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `getStreamingEngineState()`, `stop()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
mStreamingContext.stop();
```

## `preview-export-003` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:92`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CompileCallback`
Common calls: `setOnClickListener()`, `setCompileCallback()`, `CompileCallback()`, `scheduleThread()`, `scanFile()`, `setOnTouchListener()`, `OnTouchListener()`

Simple sequence:

```java
boomRangPreviewCloseButton.setOnClickListener(this);
boomRangPreviewCreate.setOnClickListener(this);
mStreamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
public void onCompileFinished(NvsTimeline nvsTimeline) {
public void onCompileFailed(NvsTimeline nvsTimeline) {
mCompilePage.setOnTouchListener(new View.OnTouchListener() {
```

## `preview-export-004` `setCompileCallback`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:101`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
```

## `preview-export-005` `onCompileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:106`

API classes: `NvsTimeline`
Common calls: `scheduleThread()`, `scanFile()`

Simple sequence:

```java
public void onCompileFinished(NvsTimeline nvsTimeline) {
```

## `preview-export-006` `onResume`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/BoomRangPreviewActivity.java:213`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `playVideo()`

Simple sequence:

```java
mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mLiveWindow.playVideo(mTimeline);
```

## `preview-export-007` `LiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:25`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.getInstance`, `NvsStreamingContext.PlaybackCallback`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `getInstance()`, `e()`, `setPlaybackCallback()`, `PlaybackCallback()`, `post()`, `playbackTimeline()`

Simple sequence:

```java
m_streamingContext = NvsStreamingContext.getInstance();
if(m_isRecycle) {
m_streamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(final NvsTimeline nvsTimeline) {
m_streamingContext.playbackTimeline(nvsTimeline, 0, -1,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-008` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:43`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-009` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:47`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `post()`, `playbackTimeline()`

Simple sequence:

```java
public void onPlaybackEOF(final NvsTimeline nvsTimeline) {
m_streamingContext.playbackTimeline(nvsTimeline, 0, -1,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-010` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:48`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `post()`, `playbackTimeline()`

Simple sequence:

```java
m_streamingContext.playbackTimeline(nvsTimeline, 0, -1,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-011` `onPlaybackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:50`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
m_streamingContext.playbackTimeline(nvsTimeline, 0, -1,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-012` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/LiveWindow.java:66`

API classes: `NvsTimeline`, `NvsLiveWindow`, `NvsStreamingContext`
Static/constants: `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `e()`, `getVideoRes()`, `setFillMode()`, `connectTimelineWithLiveWindow()`, `playbackTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
public void playVideo(NvsTimeline nvsTimeline) {
if (nvsTimeline.getVideoRes().imageWidth >= nvsTimeline.getVideoRes().imageHeight) {
this.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);
m_streamingContext.connectTimelineWithLiveWindow(nvsTimeline, this);
m_streamingContext.playbackTimeline(nvsTimeline, m_streamingContext.getTimelineCurrentPosition(nvsTimeline), -1,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-013` `isFlashOn`

Source: `app/src/main/java/com/meishe/sdkdemo/boomrang/fragment/BaseRecordFragment.java:235`

API classes: `NvsLiveWindow`
Common calls: `findViewById()`

Simple sequence:

```java
mLiveWindow = (NvsLiveWindow) rootView.findViewById(R.id.liveWindow);
```

## `preview-export-014` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:97`

API classes: `NvsLiveWindow`

Simple sequence:

```java
mLiveWindow = (NvsLiveWindow) findViewById(R.id.liveWindow);
```

## `preview-export-015` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:41`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `getDuration()`, `seekTimeline()`

Simple sequence:

```java
public void seekTimeline(NvsTimeline mTimeline, long timestamp, int seekShowMode) {
assert mStreamingContext != null;
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);
```

## `preview-export-016` `getEngineState`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/NvsStreamingContextUtil.java:62`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
public void start(NvsTimeline mTimeline, long startTime, long endTime) {
assert mStreamingContext != null;
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-017` `initCompileVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:62`

API classes: `NvsTimeline`
Common calls: `setCompileVideoListener()`, `OnCompileVideoListener()`

Simple sequence:

```java
mCompileVideoFragment.setCompileVideoListener(new CompileVideoFragment.OnCompileVideoListener() {
public void compileProgress(NvsTimeline timeline, int progress) {
public void compileFinished(NvsTimeline timeline) {
public void compileFailed(NvsTimeline timeline) {
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
```

## `preview-export-018` `initCompileVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:64`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileProgress(NvsTimeline timeline, int progress) {
```

## `preview-export-019` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:68`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
```

## `preview-export-020` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:73`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
```

## `preview-export-021` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:78`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
```

## `preview-export-022` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:109`

API classes: `NvsTimeline`, `NvsStreamingContext`, `NvsStreamingContextUtil`
Static/constants: `NvsStreamingContextUtil.getInstance`, `NvsStreamingContext.PlaybackCallback`, `NvsStreamingContext.PlaybackCallback2`, `NvsStreamingContext.StreamingEngineCallback`, `NvsStreamingContext.CompileCallback`, `NvsStreamingContext.CompileCallback2`
Common calls: `getInstance()`, `getmStreamingContext()`, `setPlaybackCallback()`, `PlaybackCallback()`, `setPlaybackCallback2()`, `PlaybackCallback2()`, `setStreamingEngineCallback()`, `StreamingEngineCallback()`, `setVisibility()`, `setCompileCallback()`, `CompileCallback()`, `setCompileConfigurations()`

Simple sequence:

```java
NvsStreamingContext mStreamingContext = NvsStreamingContextUtil.getInstance().getmStreamingContext();
if (mStreamingContext == null || mTimeline == null || mLiveWindow == null)
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {
mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {
previewImageStop.setVisibility(isPlaying(i) ? View.GONE : View.VISIBLE);
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
mStreamingContext.setCompileCallback2(new NvsStreamingContext.CompileCallback2() {
public void onCompileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mStreamingContext.connectTimelineWithLiveWindow(mTimeline, mLiveWindow);
```

## `preview-export-023` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:113`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-024` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:120`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-025` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:124`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-026` `onPlaybackTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:137`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.StreamingEngineCallback`
Common calls: `setStreamingEngineCallback()`, `StreamingEngineCallback()`, `setVisibility()`

Simple sequence:

```java
mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {
previewImageStop.setVisibility(isPlaying(i) ? View.GONE : View.VISIBLE);
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
```

## `preview-export-027` `changeProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:182`

API classes: `NvsStreamingContext`, `NvsLiveWindow`, `NvsStreamingContextUtil`
Static/constants: `NvsStreamingContextUtil.getInstance`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`, `NvsStreamingContext.getInstance`
Common calls: `findViewById()`, `setOnClickListener()`, `OnClickListener()`, `getInstance()`, `startNow()`, `finish()`, `compileVideo()`, `setOnSeekBarChangeListener()`, `OnSeekBarChangeListener()`, `setTimelineScaleForSeek()`, `getDuration()`, `getWidth()`

Simple sequence:

```java
mLiveWindow = (NvsLiveWindow) rootView.findViewById(R.id.liveWindow);
mLiveWindow.setOnClickListener(new View.OnClickListener() {
previewImageStop.setOnClickListener(new View.OnClickListener() {
NvsStreamingContextUtil.getInstance().startNow(mTimeline);
previewImageBack.setOnClickListener(new View.OnClickListener() {
previewImageCreate.setOnClickListener(new View.OnClickListener() {
previewSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
if (fromUser) {
seekTimeline(progress, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeline, mTimeline.getDuration() / 1000000D / seekBar.getWidth());
seekTimeline(seekBar.getProgress(), 0);
```

## `preview-export-028` `stop`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:250`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`

Simple sequence:

```java
return state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK;
```

## `preview-export-029` `isPlaying`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/PreviewFragment.java:254`

API classes: `NvsStreamingContextUtil`
Static/constants: `NvsStreamingContextUtil.getInstance`
Common calls: `getInstance()`, `seekTimeline()`

Simple sequence:

```java
NvsStreamingContextUtil.getInstance().seekTimeline(mTimeline, timestamp, seekShowMode);
```

## `preview-export-030` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:408`

API classes: `NvsTimeline`
Common calls: `setCompileVideoListener()`, `OnCompileVideoListener()`

Simple sequence:

```java
if (mCompileVideoFragment != null) {
mCompileVideoFragment.setCompileVideoListener(new CompileVideoFragment.OnCompileVideoListener() {
public void compileProgress(NvsTimeline timeline, int progress) {
public void compileFinished(NvsTimeline timeline) {
public void compileFailed(NvsTimeline timeline) {
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
```

## `preview-export-031` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:415`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
```

## `preview-export-032` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:420`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
```

## `preview-export-033` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:425`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
```

## `preview-export-034` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:568`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-035` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:573`

API classes: `NvsTimeline`
Common calls: `sendEmptyMessage()`

Simple sequence:

```java
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-036` `onPlaybackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:578`

API classes: `NvsTimeline`
Common calls: `getDuration()`, `setFirstValue()`

Simple sequence:

```java
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long curPos) {
long duration = mTimeline.getDuration();
mFxSeekView.setFirstValue(mProgress);
```

## `preview-export-037` `startPlay`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1009`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `stop()`

Simple sequence:

```java
if (getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mStreamingContext.stop();
```

## `preview-export-038` `startPlay`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1010`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `stop()`

Simple sequence:

```java
if (getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mStreamingContext.stop();
```

## `preview-export-039` `updateSequenceView`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1122`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getScreenWidth()`, `dip2px()`, `getDuration()`

Simple sequence:

```java
final ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray = new ArrayList<>();
for (int i = 0; i < mVideoTrack.getClipCount(); i++) {
NvsVideoClip clip = mVideoTrack.getClipByIndex(i);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
infoDesc.mediaFilePath = clip.getFilePath();
infoDesc.trimIn = clip.getTrimIn();
infoDesc.trimOut = clip.getTrimOut();
infoDesc.inPoint = clip.getInPoint();
infoDesc.outPoint = clip.getOutPoint();
int screenWidth = ScreenUtils.getScreenWidth(this) - ScreenUtils.dip2px(this, 20);
double duration = (double) mTimeline.getDuration();
mSequenceView.setPixelPerMicrosecond(pixelPerMicrosecond);
mSequenceView.setThumbnailSequenceDescArray(infoDescArray);
```

## `preview-export-040` `updateSequenceView`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1125`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`

Simple sequence:

```java
for (int i = 0; i < mVideoTrack.getClipCount(); i++) {
NvsVideoClip clip = mVideoTrack.getClipByIndex(i);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
infoDesc.mediaFilePath = clip.getFilePath();
infoDesc.trimIn = clip.getTrimIn();
infoDesc.trimOut = clip.getTrimOut();
infoDesc.inPoint = clip.getInPoint();
infoDesc.outPoint = clip.getOutPoint();
```

## `preview-export-041` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:193`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `preview-export-042` `playbackTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:203`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setVisibility()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoPlayButton.setVisibility(View.GONE);
mVideoPlayButton.setVisibility(View.VISIBLE);
```

## `preview-export-043` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:204`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setVisibility()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoPlayButton.setVisibility(View.GONE);
mVideoPlayButton.setVisibility(View.VISIBLE);
```

## `preview-export-044` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:226`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `stopEngine()`

Simple sequence:

```java
if (mClipFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
```

## `preview-export-045` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:368`

API classes: `NvsVideoClip`
Static/constants: `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0`, `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90`, `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180`, `NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270`
Common calls: `setExtraVideoRotation()`, `getExtraVideoRotation()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
int rotateAngle = mVideoClip.getExtraVideoRotation();
switch (rotateAngle) {
case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0:
mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90);
case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_90:
mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180);
case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_180:
mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270);
case NvsVideoClip.ClIP_EXTRAVIDEOROTATION_270:
mVideoClip.setExtraVideoRotation(NvsVideoClip.ClIP_EXTRAVIDEOROTATION_0);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `preview-export-046` `stopEngine`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:144`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `getStreamingEngineState()`, `stop()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
if (mStreamingContext != null) {
mStreamingContext.stop();
```

## `preview-export-047` `stopEngine`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:145`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `getStreamingEngineState()`, `stop()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
if (mStreamingContext != null) {
mStreamingContext.stop();
```

## `preview-export-048` `onHiddenChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:205`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CompileCallback`, `NvsStreamingContext.CompileCallback2`
Common calls: `append()`, `currentTimeMillis()`, `e()`, `setCompileConfigurations()`, `scanFile()`, `getStringArray()`, `setVisibility()`, `toString()`, `setCompileCallback()`, `CompileCallback()`, `makeText()`, `getApplicationContext()`

Simple sequence:

```java
mStreamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
public void onCompileFinished(NvsTimeline nvsTimeline) {
mStreamingContext.setCompileConfigurations(null);
public void onCompileFailed(NvsTimeline nvsTimeline) {
String[] tipsName = getResources().getStringArray(R.array.compile_video_failed_tips);
mStreamingContext.setCompileCallback2(new NvsStreamingContext.CompileCallback2() {
public void onCompileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
if (!isCanceled) {
mStreamingContext.setCompileConfigurations(null);
mCompileVideoRect.setVisibility(View.GONE);
mCompileVideoFinished.setVisibility(View.VISIBLE);
String[] tipsName = getResources().getStringArray(R.array.compile_video_success_tips);
```

## `preview-export-049` `onHiddenChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:206`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CompileCallback`
Common calls: `currentTimeMillis()`, `setCompileCallback()`, `CompileCallback()`, `makeText()`, `getApplicationContext()`, `show()`, `e()`, `setCompileConfigurations()`, `scanFile()`, `compileFinished()`, `getStringArray()`, `showDialog()`

Simple sequence:

```java
mStreamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
public void onCompileFinished(NvsTimeline nvsTimeline) {
mStreamingContext.setCompileConfigurations(null);
public void onCompileFailed(NvsTimeline nvsTimeline) {
String[] tipsName = getResources().getStringArray(R.array.compile_video_failed_tips);
```

## `preview-export-050` `initCompileCallBack`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:208`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
```

## `preview-export-051` `onCompileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:213`

API classes: `NvsTimeline`
Common calls: `currentTimeMillis()`, `makeText()`, `getApplicationContext()`, `show()`, `e()`, `setCompileConfigurations()`, `scanFile()`, `compileFinished()`

Simple sequence:

```java
public void onCompileFinished(NvsTimeline nvsTimeline) {
mStreamingContext.setCompileConfigurations(null);
```

## `preview-export-052` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:464`

API classes: `NvsRational`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
Common calls: `dismiss()`, `getString()`, `getInstance()`, `setOnTitleBarClickListener()`, `create()`, `getForwardLayout()`, `OnBottomViewClickListener()`, `setVisibility()`, `compileVideo()`, `getTimelineCurrentPosition()`, `grabImageFromTimeline()`, `currentTimeMillis()`

Simple sequence:

```java
mTitleBar.setOnTitleBarClickListener(new OnTitleBarClickListener() {
if (mBasePopupView == null) {
mBasePopupView = PopCompileAndMakePicBottomView.create(mContext, mTitleBar.getForwardLayout(), new PopCompileAndMakePicBottomView.OnBottomViewClickListener() {
mCompilePage.setVisibility(View.VISIBLE);
long timelineCurrentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
Bitmap bitmap = mStreamingContext.grabImageFromTimeline(mTimeline, timelineCurrentPosition,
new NvsRational(1, 1), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
String filePath = com.meishe.engine.util.PathUtils.getVideoSavePath(fileName);
if (ret) {
ToastUtil.showToastCenter(mContext, String.format(getResources().getString(R.string.compile_save_path), filePath));
ToastUtil.showToast(mContext, getResources().getString(R.string.compile_save_failed));
AppManager.getInstance().jumpActivity(AppManager.getInstance().currentActivity(), LivePhotoActivity.class);
```

## `preview-export-053` `OnCenterTextClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:477`

API classes: `NvsRational`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
Common calls: `dismiss()`, `getString()`, `getInstance()`, `create()`, `getForwardLayout()`, `OnBottomViewClickListener()`, `setVisibility()`, `compileVideo()`, `getTimelineCurrentPosition()`, `grabImageFromTimeline()`, `currentTimeMillis()`, `getVideoSavePath()`

Simple sequence:

```java
if (mBasePopupView == null) {
mBasePopupView = PopCompileAndMakePicBottomView.create(mContext, mTitleBar.getForwardLayout(), new PopCompileAndMakePicBottomView.OnBottomViewClickListener() {
mCompilePage.setVisibility(View.VISIBLE);
long timelineCurrentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
Bitmap bitmap = mStreamingContext.grabImageFromTimeline(mTimeline, timelineCurrentPosition,
new NvsRational(1, 1), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
String filePath = com.meishe.engine.util.PathUtils.getVideoSavePath(fileName);
if (ret) {
ToastUtil.showToastCenter(mContext, String.format(getResources().getString(R.string.compile_save_path), filePath));
ToastUtil.showToast(mContext, getResources().getString(R.string.compile_save_failed));
AppManager.getInstance().jumpActivity(AppManager.getInstance().currentActivity(), LivePhotoActivity.class);
```

## `preview-export-054` `OnRightTextClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:478`

API classes: `NvsRational`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
Common calls: `dismiss()`, `getString()`, `getInstance()`, `create()`, `getForwardLayout()`, `OnBottomViewClickListener()`, `setVisibility()`, `compileVideo()`, `getTimelineCurrentPosition()`, `grabImageFromTimeline()`, `currentTimeMillis()`, `getVideoSavePath()`

Simple sequence:

```java
if (mBasePopupView == null) {
mBasePopupView = PopCompileAndMakePicBottomView.create(mContext, mTitleBar.getForwardLayout(), new PopCompileAndMakePicBottomView.OnBottomViewClickListener() {
mCompilePage.setVisibility(View.VISIBLE);
long timelineCurrentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
Bitmap bitmap = mStreamingContext.grabImageFromTimeline(mTimeline, timelineCurrentPosition,
new NvsRational(1, 1), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
String filePath = com.meishe.engine.util.PathUtils.getVideoSavePath(fileName);
if (ret) {
ToastUtil.showToastCenter(mContext, String.format(getResources().getString(R.string.compile_save_path), filePath));
ToastUtil.showToast(mContext, getResources().getString(R.string.compile_save_failed));
AppManager.getInstance().jumpActivity(AppManager.getInstance().currentActivity(), LivePhotoActivity.class);
```

## `preview-export-055` `OnRightTextClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:479`

API classes: `NvsRational`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
Common calls: `dismiss()`, `getString()`, `getInstance()`, `create()`, `getForwardLayout()`, `OnBottomViewClickListener()`, `setVisibility()`, `compileVideo()`, `getTimelineCurrentPosition()`, `grabImageFromTimeline()`, `currentTimeMillis()`, `getVideoSavePath()`

Simple sequence:

```java
mBasePopupView = PopCompileAndMakePicBottomView.create(mContext, mTitleBar.getForwardLayout(), new PopCompileAndMakePicBottomView.OnBottomViewClickListener() {
mCompilePage.setVisibility(View.VISIBLE);
long timelineCurrentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
Bitmap bitmap = mStreamingContext.grabImageFromTimeline(mTimeline, timelineCurrentPosition,
new NvsRational(1, 1), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
String filePath = com.meishe.engine.util.PathUtils.getVideoSavePath(fileName);
if (ret) {
ToastUtil.showToastCenter(mContext, String.format(getResources().getString(R.string.compile_save_path), filePath));
ToastUtil.showToast(mContext, getResources().getString(R.string.compile_save_failed));
AppManager.getInstance().jumpActivity(AppManager.getInstance().currentActivity(), LivePhotoActivity.class);
```

## `preview-export-056` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:596`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-057` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:601`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-058` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoEditActivity.java:606`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-059` `initDrawRectListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:617`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `stop()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mStreamingContext.stop();
```

## `preview-export-060` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1879`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `sendEmptyMessage()`, `playBackEOF()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-061` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1881`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
```

## `preview-export-062` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1886`

API classes: `NvsTimeline`
Common calls: `playStopped()`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-063` `onResume`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2023`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `getTimelineCurrentPosition()`, `e()`, `postDelayed()`

Simple sequence:

```java
if (currEngineState != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
long stamp = mStreamingContext.getTimelineCurrentPosition(mTimeline);
```

## `preview-export-064` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2067`

API classes: `NvsRational`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
if (compileHeight == SettingActivity.CompileVideoRes_2160) {
NvsRational nvsRational = new NvsRational(1, 2);
if (mPlayFlag == 0) {
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, nvsRational, true, flag);
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, nvsRational, true, mPlayFlag | flag);
if (mPlayFlag == 0) {
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, flag);
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, mPlayFlag | flag);
```

## `preview-export-065` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2089`

API classes: `NvsStreamingContext`, `NvsRational`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `seekTimeline()`, `instance()`, `getCompileVideoRes()`

Simple sequence:

```java
int compileHeight = settingValues.getCompileVideoRes();
if (compileHeight == SettingActivity.CompileVideoRes_2160) {
NvsRational nvsRational = new NvsRational(1, 2);
mStreamingContext.seekTimeline(mTimeline, timestamp,
seekShowMode | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
mStreamingContext.seekTimeline(mTimeline, timestamp,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
seekShowMode | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
```

## `preview-export-066` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2092`

API classes: `NvsStreamingContext`, `NvsRational`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `seekTimeline()`

Simple sequence:

```java
if (compileHeight == SettingActivity.CompileVideoRes_2160) {
NvsRational nvsRational = new NvsRational(1, 2);
mStreamingContext.seekTimeline(mTimeline, timestamp,
seekShowMode | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
mStreamingContext.seekTimeline(mTimeline, timestamp,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
seekShowMode | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
```

## `preview-export-067` `stopEngine`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2118`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `stop()`

Simple sequence:

```java
if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
if (mStreamingContext != null) {
mStreamingContext.stop();
```

## `preview-export-068` `stopEngine`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2121`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `stop()`

Simple sequence:

```java
if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
if (mStreamingContext != null) {
mStreamingContext.stop();
```

## `preview-export-069` `controllerOperation`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2229`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `getDuration()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mTimeline == null) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
if (mPlayBarVisibleState) {
mPlayStartFlag = mStreamingContext.getTimelineCurrentPosition(mTimeline);
```

## `preview-export-070` `controllerOperation`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2230`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `getDuration()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mTimeline == null) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
if (mPlayBarVisibleState) {
mPlayStartFlag = mStreamingContext.getTimelineCurrentPosition(mTimeline);
```

## `preview-export-071` `onStartTrackingTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2282`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `setTimelineScaleForSeek()`, `getDuration()`, `getWidth()`

Simple sequence:

```java
NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeline, mTimeline.getDuration() / 1000000D / seekBar.getWidth());
```

## `preview-export-072` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:146`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `preview-export-073` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:300`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `sendEmptyMessage()`, `playBackEOF()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-074` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:302`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
```

## `preview-export-075` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:307`

API classes: `NvsTimeline`
Common calls: `playStopped()`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-076` `getCurrentEngineState`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:375`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `getDuration()`, `seekTimeline()`

Simple sequence:

```java
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);
```

## `preview-export-077` `onHiddenChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:433`

API classes: `NvsLiveWindow`
Static/constants: `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT`
Common calls: `getLayoutParams()`, `getStatusBarHeight()`, `getScreenWidth()`, `getScreenHeight()`, `setLayoutParams()`, `setFillMode()`

Simple sequence:

```java
ViewGroup.LayoutParams layoutParams = mLiveWindow.getLayoutParams();
int statusHeight = ScreenUtils.getStatusBarHeight(getActivity());
int screenWidth = ScreenUtils.getScreenWidth(getActivity());
int screenHeight = ScreenUtils.getScreenHeight(getActivity());
mLiveWindow.setLayoutParams(layoutParams);
mLiveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);
```

## `preview-export-078` `controllerOperation`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:501`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `getDuration()`

Simple sequence:

```java
if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
```

## `preview-export-079` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:506`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `getDuration()`

Simple sequence:

```java
if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
```

## `preview-export-080` `onStartTrackingTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:533`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `setTimelineScaleForSeek()`, `getDuration()`, `getWidth()`

Simple sequence:

```java
NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeline, mTimeline.getDuration() / 1000000D / seekBar.getWidth());
```

## `preview-export-081` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:149`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setOnClickListener()`, `OnClickListener()`, `getStreamingEngineState()`, `stopEngine()`, `playVideo()`, `getDuration()`

Simple sequence:

```java
mPlayBtn.setOnClickListener(new View.OnClickListener() {
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.playVideo(startPlayTime, mTimeline.getDuration());
```

## `preview-export-082` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:151`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `stopEngine()`, `playVideo()`, `getDuration()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.playVideo(startPlayTime, mTimeline.getDuration());
```

## `preview-export-083` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:152`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `stopEngine()`, `playVideo()`, `getDuration()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.playVideo(startPlayTime, mTimeline.getDuration());
```

## `preview-export-084` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:295`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `preview-export-085` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:199`

API classes: `NvsStreamingContext`, `NvsTimelineEditor`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsTimelineEditor.OnScrollChangeListener`, `NvsStreamingContext.getInstance`
Common calls: `setOnClickListener()`, `OnClickListener()`, `getTimelineCurrentPosition()`, `equals()`, `applyVolumeKeyInfo()`, `getKeyTime()`, `getStreamingEngineState()`, `stopEngine()`, `playVideo()`, `ZoomInSequence()`, `ZoomOutSequence()`, `getProgress()`

Simple sequence:

```java
mPlayBtn.setOnClickListener(new View.OnClickListener() {
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), -1);
findViewById(R.id.iv_zoom_out).setOnClickListener(new View.OnClickListener() {
findViewById(R.id.iv_zoom_in).setOnClickListener(new View.OnClickListener() {
addOrDeleteFrame.setOnClickListener(new View.OnClickListener() {
long currentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
float volume = VIDEOVOLUME_MAXVOLUMEVALUE * mVolumeSeekBar.getProgress() / VIDEOVOLUME_MAXSEEKBAR_VALUE;
TimelineUtil.applyVolumeKeyInfo(videoClip, volumeKeyInfoMap);
lastFrame.setOnClickListener(new View.OnClickListener() {
nextFrame.setOnClickListener(new View.OnClickListener() {
mTvKeyFrame.setOnClickListener(new View.OnClickListener() {
updateVolumeRelativeView(mStreamingContext.getTimelineCurrentPosition(mTimeline));
curveLayout.setVisibility(View.VISIBLE);
mVolumeFinish.setOnClickListener(new View.OnClickListener() {
mVolumeSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
if (volumeKeyInfo != null) {
volumeKeyInfo.setVolumeValue(volumeGain);
TimelineUtil.applyVolumeKeyInfo(videoClip, volumeKeyInfoMap);
long timelineCurrentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
mTimelineEditor.setOnScrollListener(new NvsTimelineEditor.OnScrollChangeListener() {
switch (event.getAction()) {
mTimelineEditor.setTimelineScaleForSeek(mTimeline, mTimelineEditor.getDurationWidth());
if (mTimeline != null) {
// ... 6 more SDK-related lines omitted in this compressed snippet ...
```

## `preview-export-086` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:200`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setOnClickListener()`, `OnClickListener()`, `getStreamingEngineState()`, `stopEngine()`, `playVideo()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mPlayBtn.setOnClickListener(new View.OnClickListener() {
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), -1);
```

## `preview-export-087` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:202`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `stopEngine()`, `playVideo()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), -1);
```

## `preview-export-088` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:203`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `stopEngine()`, `playVideo()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), -1);
```

## `preview-export-089` `OnCenterTextClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:139`

API classes: `NvsRational`
Common calls: `getTimelineCurrentPosition()`, `grabImageFromTimeline()`

Simple sequence:

```java
long timelineCurrentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
Bitmap bitmap = mStreamingContext.grabImageFromTimeline(mTimeline, timelineCurrentPosition, new NvsRational(1, 1));
```

## `preview-export-090` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:155`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `preview-export-091` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:197`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `setTimelineScaleForSeek()`, `getDurationWidth()`, `getInstance()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (action == MotionEvent.ACTION_DOWN) {
mTimelineEditor.setTimelineScaleForSeek(mTimeline, mTimelineEditor.getDurationWidth());
seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));
```

## `preview-export-092` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:119`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `preview-export-093` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:124`

API classes: `NvsTimeline`
Common calls: `seekToPosition()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `preview-export-094` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:218`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-095` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:223`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-096` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/livephoto/LivePhotoActivity.java:228`

API classes: `NvsTimeline`
Common calls: `setVisibility()`, `post()`, `getCompileVideoPath()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
compileLivePhoto(mCompileVideoFragment.getCompileVideoPath());
```

## `preview-export-097` `removeTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:664`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `getTimelineCurrentPosition()`, `getDuration()`, `playVideo()`, `stopEngine()`

Simple sequence:

```java
if (m_videoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
long startTime = m_streamingContext.getTimelineCurrentPosition(m_timeLine);
long endTime = m_timeLine.getDuration();
```

## `preview-export-098` `updateSequenceView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:782`

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

## `preview-export-099` `getSqView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/SqLayout.java:99`

API classes: `NvsMultiThumbnailSequenceView`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `LayoutParams()`, `addView()`, `initData()`, `getSequenceWidth()`, `getStartPadding()`, `getEndPadding()`

Simple sequence:

```java
public void initData(long total_duration, ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray) {
LinearLayout.LayoutParams recordAreaParams = new LinearLayout.LayoutParams(m_sqView.getSequenceWidth(), ViewGroup.LayoutParams.MATCH_PARENT);
LinearLayout.LayoutParams leftMarginViewParams = new LinearLayout.LayoutParams(m_sqView.getStartPadding(), LayoutParams.MATCH_PARENT);
LinearLayout.LayoutParams reghtMarginViewParams = new LinearLayout.LayoutParams(m_sqView.getEndPadding(), LayoutParams.MATCH_PARENT);
```

## `preview-export-100` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:137`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `preview-export-101` `setOnScrollListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:105`

API classes: `NvsTimelineEditor`, `NvsMultiThumbnailSequenceView`
Common calls: `setOrientation()`

Simple sequence:

```java
public NvsTimelineEditor(Context context, AttributeSet attrs) {
m_sequenceLinearLayout.setOrientation(LinearLayout.HORIZONTAL);
m_multiThumbnailSequenceView = new NvsMultiThumbnailSequenceView(context);
```

## `preview-export-102` `getSequenceWidth`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:478`

API classes: `NvsMultiThumbnailSequenceView`

Simple sequence:

```java
public NvsMultiThumbnailSequenceView getMultiThumbnailSequenceView() {
```

## `preview-export-103` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:142`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `preview-export-104` `initLiveWindowListener`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:138`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `sendEmptyMessage()`, `playBackEOF()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-105` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:144`

API classes: `NvsTimeline`
Common calls: `playStopped()`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-106` `configureLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:263`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInt()`, `getBoolean()`, `setVisibility()`, `getInstance()`, `connectTimelineWithLiveWindow()`

Simple sequence:

```java
if (bundle != null) {
mMakeRatio = bundle.getInt("ratio", NvAsset.AspectRatio_16v9);
titleHeight = bundle.getInt("titleHeight");
bottomHeight = bundle.getInt("bottomHeight");
mPlayBarVisibleState = bundle.getBoolean("playBarVisible", true);
mPlayBarLayout.setVisibility(mPlayBarVisibleState ? View.VISIBLE : View.GONE);
mStreamingContext = NvsStreamingContext.getInstance();
if (null == mTimeline) {
if (mStreamingContext == null || mTimeline == null || mLiveWindow == null)
mStreamingContext.connectTimelineWithLiveWindow(mTimeline, mLiveWindow);
```

## `preview-export-107` `setTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:287`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-108` `getCurrentEngineState`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:295`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `seekTimeline()`

Simple sequence:

```java
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);
```

## `preview-export-109` `onDestroy`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:324`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`, `NvsStreamingContext.getInstance`
Common calls: `getDuration()`, `setOnClickListener()`, `OnClickListener()`, `getTimelineCurrentPosition()`, `aVPlayStartedByButton()`, `aVPlayStopedByButton()`, `setOnSeekBarChangeListener()`, `OnSeekBarChangeListener()`, `getInstance()`, `setTimelineScaleForSeek()`, `getWidth()`, `getProgress()`

Simple sequence:

```java
mPlayButtonLayout.setOnClickListener(new View.OnClickListener() {
if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
mPlaySeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
if (fromUser) {
seekTimeline(progress, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeline, mTimeline.getDuration() / 1000000D / seekBar.getWidth());
seekTimeline(seekBar.getProgress(), 0);
```

## `preview-export-110` `initUiListener`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:327`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `getDuration()`, `aVPlayStartedByButton()`, `aVPlayStopedByButton()`

Simple sequence:

```java
if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
```

## `preview-export-111` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:332`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `getDuration()`, `aVPlayStartedByButton()`, `aVPlayStopedByButton()`

Simple sequence:

```java
if (getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
```

## `preview-export-112` `setOnClickListener`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:389`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING`, `NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`, `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `playbackTimeline()`, `getTimelineCurrentPosition()`, `stop()`

Simple sequence:

```java
if (NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING == state || NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED == state) {
mStreamingContext.playbackTimeline(mTimeline, mStreamingContext.getTimelineCurrentPosition(mTimeline), -1, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
} else if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
mStreamingContext.stop();
```

## `preview-export-113` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:391`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`

Simple sequence:

```java
} else if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
```

## `preview-export-114` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:404`

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

## `preview-export-115` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:411`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-116` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:416`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-117` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:421`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-118` `initStreamingContext`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:890`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `post()`, `sendMessage()`, `start()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-119` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:897`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-120` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:902`

API classes: `NvsTimeline`
Common calls: `post()`, `sendMessage()`, `start()`

Simple sequence:

```java
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-121` `onFirstVideoFramePresented`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:935`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.PlaybackCallback2`
Common calls: `setPlaybackCallback2()`, `PlaybackCallback2()`, `updateIndicator()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long l) {
```

## `preview-export-122` `initSequenceView`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1052`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getSqView()`, `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getScreenWidth()`, `dip2px()`

Simple sequence:

```java
if (mTimeline == null || mVideoTrack == null)
mSequenceView = mSequenceLayout.getSqView();
ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray = new ArrayList<>();
for (int i = 0; i < mVideoTrack.getClipCount(); i++) {
NvsVideoClip clip = mVideoTrack.getClipByIndex(i);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
infoDesc.mediaFilePath = clip.getFilePath();
infoDesc.trimIn = clip.getTrimIn();
infoDesc.trimOut = clip.getTrimOut();
infoDesc.inPoint = clip.getInPoint();
infoDesc.outPoint = clip.getOutPoint();
int screenWidth = ScreenUtils.getScreenWidth(this) - ScreenUtils.dip2px(this, 20);
double duration = (double) mTimeline.getDuration();
mSequenceView.setPixelPerMicrosecond(pixelPerMicrosecond);
mSequenceView.setPixelPerMicrosecond2(pixelPerMicrosecond);
mSequenceView.setThumbnailSequenceDescArray(infoDescArray);
```

## `preview-export-123` `initSequenceView`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1057`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`

Simple sequence:

```java
for (int i = 0; i < mVideoTrack.getClipCount(); i++) {
NvsVideoClip clip = mVideoTrack.getClipByIndex(i);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
infoDesc.mediaFilePath = clip.getFilePath();
infoDesc.trimIn = clip.getTrimIn();
infoDesc.trimOut = clip.getTrimOut();
infoDesc.inPoint = clip.getInPoint();
infoDesc.outPoint = clip.getOutPoint();
```

## `preview-export-124` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:1157`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `seekTimeline()`

Simple sequence:

```java
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);
```

## `preview-export-125` `setOnClickListener`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:96`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `stop()`, `getTimelineCurrentPosition()`, `playbackTimeline()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mStreamingContext.stop();
mPlayStartFlag = mStreamingContext.getTimelineCurrentPosition(mTimeline);
mStreamingContext.playbackTimeline(mTimeline, mPlayStartFlag, -1,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-126` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:125`

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

## `preview-export-127` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:132`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-128` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:137`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-129` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:142`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-130` `compileVideoCancel`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:152`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`, `NvsStreamingContext.getInstance`
Common calls: `setOnSeekBarChangeListener()`, `OnSeekBarChangeListener()`, `getInstance()`, `setTimelineScaleForSeek()`, `getDuration()`, `getWidth()`, `getProgress()`

Simple sequence:

```java
mPlaySeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
if(fromUser) {
seekTimeline(i, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
NvsStreamingContext.getInstance().setTimelineScaleForSeek(mTimeline, mTimeline.getDuration() / 1000000D / seekBar.getWidth());
seekTimeline(seekBar.getProgress(), 0);
```

## `preview-export-131` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:179`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-132` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:183`

API classes: `NvsTimeline`
Common calls: `post()`, `setProgress()`

Simple sequence:

```java
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
mPlaySeekBar.setProgress(0);
```

## `preview-export-133` `onBackPressed`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticlePreviewActivity.java:242`

API classes: `NvsSize`
Common calls: `createTimeline()`, `setMax()`, `getDuration()`, `post()`, `getWidth()`, `getHeight()`, `getLiveWindowSize()`, `getTimelineSize()`, `getLayoutParams()`, `setLayoutParams()`, `connectTimelineWithLiveWindow()`

Simple sequence:

```java
mTimeline = TimelineUtil.createTimeline();
if (mStreamingContext == null || mTimeline == null || mLiveWindow == null)
mPlaySeekBar.setMax((int) mTimeline.getDuration());
mLiveWindow.post(new Runnable() {
int width = mLiveWindow.getWidth();
int height = mLiveWindow.getHeight();
NvsSize liveWindowSize = Util.getLiveWindowSize(TimelineUtil.getTimelineSize(mTimeline), new NvsSize(width, height), false);
ViewGroup.LayoutParams params = mLiveWindow.getLayoutParams();
mLiveWindow.setLayoutParams(params);
mStreamingContext.connectTimelineWithLiveWindow(mTimeline, mLiveWindow);
```

## `preview-export-134` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:197`

API classes: `NvsTimeline`
Common calls: `e()`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-135` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:202`

API classes: `NvsTimeline`
Common calls: `e()`, `setProgress()`

Simple sequence:

```java
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
mProgressBar.setProgress(0);
```

## `preview-export-136` `OnCancelBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:230`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.PlaybackCallback2`
Common calls: `PlaybackCallback2()`, `setProgress()`

Simple sequence:

```java
mPlaybackCallback2Listener = new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long l) {
mProgressBar.setProgress((int) l);
```

## `preview-export-137` `onFirstVideoFramePresented`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:256`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CompileCallback`
Common calls: `dismiss()`, `CompileCallback()`, `setProgress()`, `scanFile()`

Simple sequence:

```java
mCompileCallback = new NvsStreamingContext.CompileCallback() {
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
mCompileDialog.setProgress(i);
public void onCompileFinished(NvsTimeline nvsTimeline) {
public void onCompileFailed(NvsTimeline nvsTimeline) {
```

## `preview-export-138` `onCompileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:263`

API classes: `NvsTimeline`
Common calls: `scanFile()`, `dismiss()`

Simple sequence:

```java
public void onCompileFinished(NvsTimeline nvsTimeline) {
```

## `preview-export-139` `onCompileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:278`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.CompileCallback2`
Common calls: `CompileCallback2()`, `dismiss()`, `setProgress()`

Simple sequence:

```java
mCompileCallback2 = new NvsStreamingContext.CompileCallback2() {
public void onCompileCompleted(NvsTimeline nvsTimeline, boolean cancel) {
mCompileDialog.setProgress(0);
```

## `preview-export-140` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:297`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `stop()`, `getTimelineCurrentPosition()`, `getVisibility()`, `performClick()`

Simple sequence:

```java
if (id == R.id.playBtn) {
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mStreamingContext.stop();
playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), -1);
if (mPlayBtn.getVisibility() != View.VISIBLE) {
```

## `preview-export-141` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:298`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `stop()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mStreamingContext.stop();
playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), -1);
```

## `preview-export-142` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:448`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `e()`, `playbackTimeline()`

Simple sequence:

```java
if (mStreamingContext == null) {
Log.e(TAG, "playVideo: mStreamingContext is null");
if (mTimeline == null) {
Log.e(TAG, "playVideo: mTimeline is null");
mStreamingContext.playbackTimeline(mTimeline, start, end,
NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `preview-export-143` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:465`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `e()`, `seekTimeline()`

Simple sequence:

```java
if (mStreamingContext == null) {
Log.e(TAG, "seekTimeline: mStreamingContext is null");
if (mTimeline == null) {
Log.e(TAG, "seekTimeline: mTimeline is null");
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);
```

## `preview-export-144` `OnCenterTextClick`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PicturInPicturePreviewActivity.java:84`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `stopEngine()`, `setVisibility()`, `compileVideo()`

Simple sequence:

```java
if(mClipFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)
mCompilePage.setVisibility(View.VISIBLE);
```

## `preview-export-145` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PicturInPicturePreviewActivity.java:99`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-146` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PicturInPicturePreviewActivity.java:104`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-147` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PicturInPicturePreviewActivity.java:109`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-148` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:138`

API classes: `NvsLiveWindow`

Simple sequence:

```java
mLiveWindow = (NvsLiveWindow) findViewById(R.id.liveWindow);
```

## `preview-export-149` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:210`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-150` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:215`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-151` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:220`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `preview-export-152` `setLiveWindowRatio`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:985`

API classes: `NvsLiveWindow`
Static/constants: `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT`
Common calls: `getLayoutParams()`, `getStatusBarHeight()`, `getNavigationBarHeight()`, `getScreenWidth()`, `getScreenHeight()`, `setLayoutParams()`, `setFillMode()`, `connectTimelineWithLiveWindow()`

Simple sequence:

```java
RelativeLayout.LayoutParams liveWindowParams = (RelativeLayout.LayoutParams) mLiveWindow.getLayoutParams();
int statusHeight = ScreenUtils.getStatusBarHeight(this);
int navBarHeight = ScreenUtils.getNavigationBarHeight(this);
int screenWidth = ScreenUtils.getScreenWidth(this);
int screenHeight = ScreenUtils.getScreenHeight(this);
int titleHeight = mTitleBar.getLayoutParams().height;
int bottomHeight = mBottomLayout.getLayoutParams().height;
mLiveWindow.setLayoutParams(liveWindowParams);
mLiveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);
mStreamingContext.connectTimelineWithLiveWindow(mTimeline, mLiveWindow);
```

## `preview-export-153` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:180`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `preview-export-154` `onResume`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:204`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CompileCallback`
Common calls: `setVisibility()`, `setCompileCallback()`, `CompileCallback()`, `refreshAlbum()`, `makeText()`, `getString()`, `show()`

Simple sequence:

```java
mStreamingContext.setCompileCallback(b ? null : new NvsStreamingContext.CompileCallback() {
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
public void onCompileFinished(NvsTimeline nvsTimeline) {
compilePage.setVisibility(View.GONE);
Toast.makeText(getApplicationContext(), getResources().getString(R.string.completedTips), Toast.LENGTH_SHORT).show();
public void onCompileFailed(NvsTimeline nvsTimeline) {
compilePage.setVisibility(View.GONE);
```

## `preview-export-155` `onCompileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:212`

API classes: `NvsTimeline`
Common calls: `setVisibility()`, `refreshAlbum()`, `makeText()`, `getString()`, `show()`

Simple sequence:

```java
public void onCompileFinished(NvsTimeline nvsTimeline) {
compilePage.setVisibility(View.GONE);
Toast.makeText(getApplicationContext(), getResources().getString(R.string.completedTips), Toast.LENGTH_SHORT).show();
```

## `preview-export-156` `updateSequenceView`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:242`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getScreenWidth()`, `dip2px()`, `getDuration()`

Simple sequence:

```java
if (mVideoTrack == null) return;
final ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray = new ArrayList<>();
for (int i = 0; i < mVideoTrack.getClipCount(); i++) {
NvsVideoClip clip = mVideoTrack.getClipByIndex(i);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
infoDesc.mediaFilePath = clip.getFilePath();
infoDesc.trimIn = clip.getTrimIn();
infoDesc.trimOut = clip.getTrimOut();
infoDesc.inPoint = clip.getInPoint();
infoDesc.outPoint = clip.getOutPoint();
int screenWidth = ScreenUtils.getScreenWidth(this) - ScreenUtils.dip2px(this, 144);
double duration = (double) mTimeline.getDuration();
thumbnailView.setPixelPerMicrosecond(pixelPerMicrosecond);
thumbnailView.setThumbnailSequenceDescArray(infoDescArray);
```

## `preview-export-157` `updateSequenceView`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:245`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`

Simple sequence:

```java
for (int i = 0; i < mVideoTrack.getClipCount(); i++) {
NvsVideoClip clip = mVideoTrack.getClipByIndex(i);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc infoDesc = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
infoDesc.mediaFilePath = clip.getFilePath();
infoDesc.trimIn = clip.getTrimIn();
infoDesc.trimOut = clip.getTrimOut();
infoDesc.inPoint = clip.getInPoint();
infoDesc.outPoint = clip.getOutPoint();
```

## `preview-export-158` `addCutTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:310`

API classes: `NvsVideoClip`, `NvsTimeline`, `NvsRational`, `NvsVideoTrack`
Common calls: `setVisibility()`, `setImageBitmap()`, `e()`, `getDuration()`, `grabImageFromTimeline()`, `getVideoTrackByIndex()`, `insertTimelineClip()`, `appendTimelineClip()`

Simple sequence:

```java
private void addCutTimeline(NvsTimeline timeline) {
if (timeline == null) return;
Log.e("variablecompose", "addCutTimeline duration:" + timeline.getDuration());
Bitmap bitmap = mStreamingContext.grabImageFromTimeline(timeline, 0, new NvsRational(1, 2));
NvsVideoTrack videoTrack = null;
if (mTimeline != null) {
videoTrack = mTimeline.getVideoTrackByIndex(0);
if (videoTrack != null) {
NvsVideoClip videoClip = videoTrack.insertTimelineClip(timeline, 0);
if (hasHead) {
tvHead.setVisibility(View.GONE);
if (bitmap != null) {
ivHead.setImageBitmap(bitmap);
iv_head_delete.setVisibility(View.VISIBLE);
if (videoTrack != null) {
NvsVideoClip videoClip = videoTrack.appendTimelineClip(timeline);
if (hasTail) {
tvTail.setVisibility(View.GONE);
if (bitmap != null) {
ivTail.setImageBitmap(bitmap);
iv_tail_delete.setVisibility(View.VISIBLE);
```

## `preview-export-159` `onBackPressed`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:351`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `getStreamingEngineState()`, `onBackPressed()`

Simple sequence:

```java
if (mStreamingContext != null &&
mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
```

## `preview-export-160` `onBackPressed`

Source: `app/src/main/java/com/meishe/sdkdemo/sequenceNesting/SequenceNestingActivity.java:353`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE`
Common calls: `getStreamingEngineState()`

Simple sequence:

```java
mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
```

## `preview-export-161` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:104`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CompileCallback`
Common calls: `setCompileCallback()`, `CompileCallback()`, `scheduleThread()`, `scanFile()`, `playVideo()`

Simple sequence:

```java
mStreamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {
public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
public void onCompileFinished(NvsTimeline nvsTimeline) {
mLiveWindow.playVideo(mTimeline);
public void onCompileFailed(NvsTimeline nvsTimeline) {
```

## `preview-export-162` `onCompileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomPreviewActivity.java:111`

API classes: `NvsTimeline`
Common calls: `scheduleThread()`, `scanFile()`, `playVideo()`

Simple sequence:

```java
public void onCompileFinished(NvsTimeline nvsTimeline) {
mLiveWindow.playVideo(mTimeline);
```

## `preview-export-163` `playTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:585`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`, `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME`, `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_LOW_PIPELINE_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
public void playTimeline(NvsTimeline mTimeLine, long startTime, long endTime) {
mStreamingContext.playbackTimeline(mTimeLine, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true,
NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME | NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_LOW_PIPELINE_SIZE);
```

## `preview-export-164` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:593`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `setOnPlayClickListener()`, `OnPlayClickListener()`, `getTimelineCurrentPosition()`, `stop()`, `seekTimeline()`

Simple sequence:

```java
playView.setOnPlayClickListener(new ThemePlayView.OnPlayClickListener() {
if (isPlaying) {
playTimeline(mTimeline, mStreamingContext.getTimelineCurrentPosition(mTimeline), endDuration);
mStreamingContext.stop();
if (!fromUser) {
mStreamingContext.seekTimeline(mTimeline, progressPosition, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);
```

## `preview-export-165` `onProgressChange`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:605`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `seekTimeline()`

Simple sequence:

```java
if (!fromUser) {
mStreamingContext.seekTimeline(mTimeline, progressPosition, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);
```

## `preview-export-166` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:638`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.StreamingEngineCallback`, `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setStreamingEngineCallback()`, `StreamingEngineCallback()`, `updatePlaying()`

Simple sequence:

```java
mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {
playView.updatePlaying(i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK);
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
```

## `preview-export-167` `onFirstVideoFramePresented`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:649`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
playTimeline(mTimeline, startDuration, endDuration);
```

## `preview-export-168` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:656`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-169` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:661`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
playTimeline(mTimeline, startDuration, endDuration);
```

## `preview-export-170` `onPlaybackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:665`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.PlaybackCallback2`
Common calls: `setPlaybackCallback2()`, `PlaybackCallback2()`, `setCurrentProgress()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long l) {
playView.setCurrentProgress((int) l);
```

## `preview-export-171` `setCompileVideoRes`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/ParameterSettingValues.java:51`

API classes: `NvsStreamingContext`, `NvsLiveWindow`, `NvsVideoResolution`
Static/constants: `NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH`, `NvsLiveWindow.HDR_DISPLAY_MODE_SDR`, `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT`

Simple sequence:

```java
m_captureResolutionGrade = NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_SUPER_HIGH;
liveWindowModel = NvsLiveWindow.HDR_DISPLAY_MODE_SDR;
bitDepth = NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT;
```

## `preview-export-172` `compileVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:100`

API classes: `NvsVideoResolution`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM`
Common calls: `getVideoRes()`, `getCustomHeight()`

Simple sequence:

```java
NvsVideoResolution videoRes = timeline.getVideoRes();
int resultHeight = Util.getCustomHeight(videoRes.imageWidth, videoRes.imageHeight);
compileVideo(context, timeline, compileVideoPath, startTime, endTime, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, resultHeight);
```

## `preview-export-173` `getCompileConfigurations`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:114`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.COMPILE_USE_OPERATING_RATE`
Common calls: `putAll()`, `instance()`, `isQuickPack()`, `put()`

Simple sequence:

```java
compileConfigurations.put(NvsStreamingContext.COMPILE_USE_OPERATING_RATE, quickPack);
```

## `preview-export-174` `setLiveWindowRatio`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:71`

API classes: `NvsVideoResolution`
Common calls: `getWidth()`, `getHeight()`, `post()`

Simple sequence:

```java
public void setLiveWindowRatio(final NvsVideoResolution videoResolution) {
if (isInitView && videoResolution != null) {
if (mLiveWindow.getWidth() == 0 && mLiveWindow.getHeight() == 0) {
mLiveWindow.post(new Runnable() {
```

## `preview-export-175` `setLiveWindowSize`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:90`

API classes: `NvsVideoResolution`
Common calls: `getWidth()`, `getHeight()`, `getLayoutParams()`, `setLayoutParams()`

Simple sequence:

```java
private void setLiveWindowSize(NvsVideoResolution videoResolution) {
int viewWidth = mLiveWindow.getWidth();
int viewHeight = mLiveWindow.getHeight();
ViewGroup.LayoutParams layoutParams = mLiveWindow.getLayoutParams();
mLiveWindow.setLayoutParams(layoutParams);
```

## `preview-export-176` `connectTimeline`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:110`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`, `NvsStreamingContext.PlaybackCallback2`, `NvsStreamingContext.StreamingEngineCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `playBackEOF()`, `setPlaybackCallback2()`, `PlaybackCallback2()`, `playbackTimelinePosition()`, `setStreamingEngineCallback()`, `StreamingEngineCallback()`, `streamingEngineStateChanged()`, `connectTimelineWithLiveWindowExt()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long currentPosition) {
mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
mStreamingContext.connectTimelineWithLiveWindowExt(mTimeline, mLiveWindow);
```

## `preview-export-177` `connectTimeline`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:113`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `playBackEOF()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-178` `onPlaybackPreloadingCompletion`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:120`

API classes: `NvsTimeline`
Common calls: `playStopped()`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-179` `playVideo`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:164`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `getTimelineCurrentPosition()`, `getDuration()`

Simple sequence:

```java
if (mStreamingContext != null && mTimeline != null) {
playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), mTimeline.getDuration(), NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag);
```

## `preview-export-180` `playVideo`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:165`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `getTimelineCurrentPosition()`, `getDuration()`

Simple sequence:

```java
if (mStreamingContext != null && mTimeline != null) {
playVideo(mStreamingContext.getTimelineCurrentPosition(mTimeline), mTimeline.getDuration(), NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag);
```

## `preview-export-181` `playVideo`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:178`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`

Simple sequence:

```java
playVideo(startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag);
```

## `preview-export-182` `seekTimeline`

Source: `libBase/src/main/java/com/meishe/base/play/PlayerFragment.java:216`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`

Simple sequence:

```java
seekTimeline(timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag);
```

## `preview-export-183` `setOnScrollListener`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:97`

API classes: `NvsTimelineEditor`, `NvsMultiThumbnailSequenceView`
Common calls: `setOrientation()`

Simple sequence:

```java
public NvsTimelineEditor(Context context, AttributeSet attrs) {
m_sequenceLinearLayout.setOrientation(LinearLayout.HORIZONTAL);
m_multiThumbnailSequenceView = new NvsMultiThumbnailSequenceView(context);
```

## `preview-export-184` `getSequenceWidth`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:456`

API classes: `NvsMultiThumbnailSequenceView`

Simple sequence:

```java
public NvsMultiThumbnailSequenceView getMultiThumbnailSequenceView() {
```

## `preview-export-185` `seekTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:975`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`

Simple sequence:

```java
if (useFaceShape) {
flag = NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME;
```

## `preview-export-186` `playVideo`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:992`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME`

Simple sequence:

```java
if (useFaceShape) {
flag = NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME;
```

## `preview-export-187` `setLiveWindrowSize`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:3008`

API classes: `NvsLiveWindowExt`
Common calls: `getWidth()`, `getHeight()`

Simple sequence:

```java
public void setLiveWindrowSize(NvsLiveWindowExt liveWindow) {
mLiveWindowSize = frameForTimeline(liveWindow.getWidth(), liveWindow.getHeight());
```

## `preview-export-188` `getLiveWindrowSize`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:3019`

API classes: `NvsLiveWindowExt`
Common calls: `getWidth()`, `getHeight()`

Simple sequence:

```java
public PointF getLiveWindrowSize(NvsLiveWindowExt liveWindow) {
if (mLiveWindowSize == null) {
mLiveWindowSize = frameForTimeline(liveWindow.getWidth(), liveWindow.getHeight());
```

## `preview-export-189` `connectTimelineWithLiveWindow`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:331`

API classes: `NvsTimeline`, `NvsStreamingContext`, `NvsLiveWindow`, `NvsLiveWindowExt`
Static/constants: `NvsStreamingContext.PlaybackCallback`, `NvsStreamingContext.SeekingCallback`, `NvsStreamingContext.PlaybackCallback2`, `NvsStreamingContext.StreamingEngineCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `playBackEOF()`, `setSeekingCallback()`, `SeekingCallback()`, `onSeekingTimelinePosition()`, `setPlaybackCallback2()`, `PlaybackCallback2()`, `playbackTimelinePosition()`, `setStreamingEngineCallback()`, `StreamingEngineCallback()`

Simple sequence:

```java
public void connectTimelineWithLiveWindow(Object mLiveWindow, final VideoFragmentListener mVideoFragmentCallBack) {
if (mStreamingContext == null || mNvsTimeline == null || mLiveWindow == null) {
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
mStreamingContext.setSeekingCallback(new NvsStreamingContext.SeekingCallback() {
public void onSeekingTimelinePosition(NvsTimeline nvsTimeline, long l) {
mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {
mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
if (mLiveWindow instanceof NvsLiveWindow) {
NvsLiveWindow liveWindow = (NvsLiveWindow) mLiveWindow;
mStreamingContext.connectTimelineWithLiveWindow(mNvsTimeline, liveWindow);
} else if (mLiveWindow instanceof NvsLiveWindowExt) {
NvsLiveWindowExt liveWindow = (NvsLiveWindowExt) mLiveWindow;
mStreamingContext.connectTimelineWithLiveWindowExt(mNvsTimeline, liveWindow);
```

## `preview-export-190` `connectTimelineWithLiveWindow`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:335`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `playBackEOF()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `preview-export-191` `onPlaybackPreloadingCompletion`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:342`

API classes: `NvsTimeline`
Common calls: `playStopped()`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `preview-export-192` `onFirstVideoFramePresented`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:384`

API classes: `NvsLiveWindow`, `NvsLiveWindowExt`
Common calls: `connectTimelineWithLiveWindow()`, `connectTimelineWithLiveWindowExt()`

Simple sequence:

```java
if (mLiveWindow instanceof NvsLiveWindow) {
NvsLiveWindow liveWindow = (NvsLiveWindow) mLiveWindow;
mStreamingContext.connectTimelineWithLiveWindow(mNvsTimeline, liveWindow);
} else if (mLiveWindow instanceof NvsLiveWindowExt) {
NvsLiveWindowExt liveWindow = (NvsLiveWindowExt) mLiveWindow;
mStreamingContext.connectTimelineWithLiveWindowExt(mNvsTimeline, liveWindow);
```

## `preview-export-193` `isPlaying`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:399`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `e()`, `getStreamingEngineState()`

Simple sequence:

```java
if (mStreamingContext == null) {
Log.e(TAG, "isPlaying: mStreamingContext is null!");
int state = mStreamingContext.getStreamingEngineState();
return state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK;
```

## `preview-export-194` `grabImageFromTimelineAsync`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:469`

API classes: `NvsStreamingContext`, `NvsRational`
Static/constants: `NvsStreamingContext.ImageGrabberCallback`
Common calls: `setImageGrabberCallback()`, `grabImageFromTimelineAsync()`

Simple sequence:

```java
public void grabImageFromTimelineAsync(long timestamp, NvsStreamingContext.ImageGrabberCallback callback) {
mStreamingContext.setImageGrabberCallback(callback);
mStreamingContext.grabImageFromTimelineAsync(mNvsTimeline, timestamp, new NvsRational(1, 1), 0);
```

## `preview-export-195` `grabImageFromTimelineAsync`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:480`

API classes: `NvsRational`
Common calls: `grabImageFromTimelineAsync()`

Simple sequence:

```java
mStreamingContext.grabImageFromTimelineAsync(mNvsTimeline, timestamp, new NvsRational(1, 1), 0);
```

## `preview-export-196` `grabImageFromTimelineAsync`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:493`

API classes: `NvsRational`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.ImageGrabberCallback`
Common calls: `setImageGrabberCallback()`, `grabImageFromTimelineAsync()`

Simple sequence:

```java
public void grabImageFromTimelineAsync(long timestamp, NvsRational proxyScale, int flags, NvsStreamingContext.ImageGrabberCallback callback) {
mStreamingContext.setImageGrabberCallback(callback);
mStreamingContext.grabImageFromTimelineAsync(mNvsTimeline, timestamp, proxyScale, flags);
```

## `preview-export-197` `setImageGrabberCallback`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:504`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.ImageGrabberCallback`
Common calls: `setImageGrabberCallback()`

Simple sequence:

```java
public void setImageGrabberCallback(NvsStreamingContext.ImageGrabberCallback callback) {
mStreamingContext.setImageGrabberCallback(callback);
```

## `preview-export-198` `grabBitmapFromTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:515`

API classes: `NvsRational`

Simple sequence:

```java
return grabBitmapFromTimeline(timestamp, new NvsRational(1, 1));
```

## `preview-export-199` `compileTimeLineCustom`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:567`

API classes: `NvsStreamingContext`, `NvsVideoResolution`
Static/constants: `NvsStreamingContext.CompileCallback`, `NvsStreamingContext.CompileCallback2`, `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM`, `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_ALIGN_VIDEO_SIZE`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
Common calls: `setCompileConfigurations()`, `d()`, `setCompileCallback()`, `setCompileCallback2()`, `setCustomCompileVideoHeight()`, `getVideoRes()`, `compileTimeline()`, `getDuration()`, `onCompileFailed()`, `e()`

Simple sequence:

```java
NvsStreamingContext.CompileCallback compileCallback, NvsStreamingContext.CompileCallback2 compileCallback2) {
mStreamingContext.setCompileConfigurations(null);
mStreamingContext.setCompileCallback(compileCallback);
mStreamingContext.setCompileCallback2(compileCallback2);
mStreamingContext.setCompileConfigurations(mParamsTable);
mStreamingContext.setCustomCompileVideoHeight(videoHeight);
NvsVideoResolution videoRes = mNvsTimeline.getVideoRes();
if (mStreamingContext.compileTimeline(mNvsTimeline, 0, mNvsTimeline.getDuration(),
path, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM,
NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_ALIGN_VIDEO_SIZE
| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE
| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME)) {
```

## `preview-export-200` `compileTimeLine`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:604`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CompileCallback`, `NvsStreamingContext.CompileCallback2`, `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
Common calls: `setCompileCallback()`, `setCompileCallback2()`, `setCompileConfigurations()`, `compileTimeline()`, `getDuration()`, `d()`, `onCompileFailed()`, `e()`

Simple sequence:

```java
NvsStreamingContext.CompileCallback compileCallback, NvsStreamingContext.CompileCallback2 compileCallback2) {
mStreamingContext.setCompileCallback(compileCallback);
mStreamingContext.setCompileCallback2(compileCallback2);
mStreamingContext.setCompileConfigurations(mParamsTable);
if (mStreamingContext.compileTimeline(mNvsTimeline, 0, mNvsTimeline.getDuration(),
NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME
| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME)) {
```

## `preview-export-201` `setThumbnailSequenceDescArray`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:312`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`, `clear()`, `e()`, `add()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-202` `setThumbnailImageFillMode`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:376`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-203` `setThumbnailAspectRatio`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:412`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`, `abs()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-204` `setPixelPerMicrosecond`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:448`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-205` `setStartPadding`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:479`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-206` `setEndPadding`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:510`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-207` `setMaxTimelinePosToScroll`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:542`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`, `max()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-208` `mapTimelinePosFromX`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:578`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`, `floor()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-209` `mapXFromTimelinePos`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:597`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`, `floor()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-210` `scaleWithAnchor`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:614`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-211` `setOnScrollChangeListenser`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:639`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-212` `getOnScrollChangeListenser`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:653`

API classes: `NvsUtils`
Static/constants: `NvsUtils.checkFunctionInMainThread`
Common calls: `checkFunctionInMainThread()`

Simple sequence:

```java
NvsUtils.checkFunctionInMainThread();
```

## `preview-export-213` `onLayout`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:697`

API classes: `NvsIconGenerator`
Common calls: `onAttachedToWindow()`, `setIconCallback()`

Simple sequence:

```java
if (!isInEditMode()) {
m_iconGenerator = new NvsIconGenerator();
m_iconGenerator.setIconCallback(this);
```

## `preview-export-214` `onAttachedToWindow`

Source: `libEngine/src/main/java/com/meishe/engine/view/MultiThumbnailSequenceView.java:700`

API classes: `NvsIconGenerator`
Common calls: `setIconCallback()`

Simple sequence:

```java
if (!isInEditMode()) {
m_iconGenerator = new NvsIconGenerator();
m_iconGenerator.setIconCallback(this);
```
