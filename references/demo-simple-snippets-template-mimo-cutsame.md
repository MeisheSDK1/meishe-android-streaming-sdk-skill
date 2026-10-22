# Demo Simple Snippets - Template Mimo CutSame

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: template package parsing, template footage replacement, Mimo timeline creation, CutSame editing, and template/cut-same compile flows.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [template-mimo-cutsame-001 bindLayout](#template-mimo-cutsame-001-bindlayout)
- [template-mimo-cutsame-002 initData](#template-mimo-cutsame-002-initdata)
- [template-mimo-cutsame-003 initData](#template-mimo-cutsame-003-initdata)
- [template-mimo-cutsame-004 onCompileProgress](#template-mimo-cutsame-004-oncompileprogress)
- [template-mimo-cutsame-005 onCompileFinished](#template-mimo-cutsame-005-oncompilefinished)
- [template-mimo-cutsame-006 onCompileFailed](#template-mimo-cutsame-006-oncompilefailed)
- [template-mimo-cutsame-007 onCompileFailed](#template-mimo-cutsame-007-oncompilefailed)
- [template-mimo-cutsame-008 bindLayout](#template-mimo-cutsame-008-bindlayout)
- [template-mimo-cutsame-009 onProgressChanged](#template-mimo-cutsame-009-onprogresschanged)
- [template-mimo-cutsame-010 parseNvsVideoClip](#template-mimo-cutsame-010-parsenvsvideoclip)
- [template-mimo-cutsame-011 createTimeline](#template-mimo-cutsame-011-createtimeline)
- [template-mimo-cutsame-012 changeVideoClipPath](#template-mimo-cutsame-012-changevideoclippath)
- [template-mimo-cutsame-013 changeVideoClipPath](#template-mimo-cutsame-013-changevideoclippath)
- [template-mimo-cutsame-014 changeVideoClipPath](#template-mimo-cutsame-014-changevideoclippath)
- [template-mimo-cutsame-015 onSeekingTimelinePosition](#template-mimo-cutsame-015-onseekingtimelineposition)
- [template-mimo-cutsame-016 onActivityResult](#template-mimo-cutsame-016-onactivityresult)
- [template-mimo-cutsame-017 onActivityResult](#template-mimo-cutsame-017-onactivityresult)
- [template-mimo-cutsame-018 deleteAddedHeadAndTail](#template-mimo-cutsame-018-deleteaddedheadandtail)
- [template-mimo-cutsame-019 getMaterialList](#template-mimo-cutsame-019-getmateriallist)
- [template-mimo-cutsame-020 getTemplateCategory](#template-mimo-cutsame-020-gettemplatecategory)
- [template-mimo-cutsame-021 getTemplateList](#template-mimo-cutsame-021-gettemplatelist)
- [template-mimo-cutsame-022 uploadUsedTemplate](#template-mimo-cutsame-022-uploadusedtemplate)
- [template-mimo-cutsame-023 download](#template-mimo-cutsame-023-download)
- [template-mimo-cutsame-024 cancelAll](#template-mimo-cutsame-024-cancelall)
- [template-mimo-cutsame-025 cancelRequest](#template-mimo-cutsame-025-cancelrequest)
- [template-mimo-cutsame-026 onResume](#template-mimo-cutsame-026-onresume)
- [template-mimo-cutsame-027 initCaptionData](#template-mimo-cutsame-027-initcaptiondata)
- [template-mimo-cutsame-028 initCaptionData](#template-mimo-cutsame-028-initcaptiondata)
- [template-mimo-cutsame-029 onCompileFailed](#template-mimo-cutsame-029-oncompilefailed)
- [template-mimo-cutsame-030 initVideoClip](#template-mimo-cutsame-030-initvideoclip)
- [template-mimo-cutsame-031 initVideoClip](#template-mimo-cutsame-031-initvideoclip)
- [template-mimo-cutsame-032 initVideoClip](#template-mimo-cutsame-032-initvideoclip)
- [template-mimo-cutsame-033 saveNeedVideoClip](#template-mimo-cutsame-033-saveneedvideoclip)
- [template-mimo-cutsame-034 saveNeedVideoClip](#template-mimo-cutsame-034-saveneedvideoclip)
- [template-mimo-cutsame-035 onProgressChanged](#template-mimo-cutsame-035-onprogresschanged)
- [template-mimo-cutsame-036 setPlayControlViewProgress](#template-mimo-cutsame-036-setplaycontrolviewprogress)
- [template-mimo-cutsame-037 initVideoFragment](#template-mimo-cutsame-037-initvideofragment)
- [template-mimo-cutsame-038 initVideoFragment](#template-mimo-cutsame-038-initvideofragment)
- [template-mimo-cutsame-039 playStopped](#template-mimo-cutsame-039-playstopped)
- [template-mimo-cutsame-040 bindLayout](#template-mimo-cutsame-040-bindlayout)
- [template-mimo-cutsame-041 bindLayout](#template-mimo-cutsame-041-bindlayout)
- [template-mimo-cutsame-042 initMultiSequence](#template-mimo-cutsame-042-initmultisequence)
- [template-mimo-cutsame-043 addTimeSpan](#template-mimo-cutsame-043-addtimespan)
- [template-mimo-cutsame-044 seekMultiThumbnailSequenceView](#template-mimo-cutsame-044-seekmultithumbnailsequenceview)
- [template-mimo-cutsame-045 seekMultiThumbnailSequenceView](#template-mimo-cutsame-045-seekmultithumbnailsequenceview)
- [template-mimo-cutsame-046 playBackEOF](#template-mimo-cutsame-046-playbackeof)
- [template-mimo-cutsame-047 onSeekingTimelinePosition](#template-mimo-cutsame-047-onseekingtimelineposition)
- [template-mimo-cutsame-048 onFinishAssetPackageInstallation](#template-mimo-cutsame-048-onfinishassetpackageinstallation)
- [template-mimo-cutsame-049 setLiveWindowRatio](#template-mimo-cutsame-049-setlivewindowratio)
- [template-mimo-cutsame-050 setLiveWindowRatio](#template-mimo-cutsame-050-setlivewindowratio)
- [template-mimo-cutsame-051 getVideoData](#template-mimo-cutsame-051-getvideodata)
- [template-mimo-cutsame-052 getVideoData](#template-mimo-cutsame-052-getvideodata)
- [template-mimo-cutsame-053 updateVideoData](#template-mimo-cutsame-053-updatevideodata)
- [template-mimo-cutsame-054 setTemplateType](#template-mimo-cutsame-054-settemplatetype)
- [template-mimo-cutsame-055 getCaptionBitmap](#template-mimo-cutsame-055-getcaptionbitmap)
- [template-mimo-cutsame-056 changeCaptionText](#template-mimo-cutsame-056-changecaptiontext)
- [template-mimo-cutsame-057 changeCaptionText](#template-mimo-cutsame-057-changecaptiontext)
- [template-mimo-cutsame-058 seekToCaptionStartTime](#template-mimo-cutsame-058-seektocaptionstarttime)
- [template-mimo-cutsame-059 seekToCaptionStartTime](#template-mimo-cutsame-059-seektocaptionstarttime)
- [template-mimo-cutsame-060 getCaptionPointList](#template-mimo-cutsame-060-getcaptionpointlist)
- [template-mimo-cutsame-061 dealVideoReplace](#template-mimo-cutsame-061-dealvideoreplace)
- [template-mimo-cutsame-062 dealVideoReplace](#template-mimo-cutsame-062-dealvideoreplace)
- [template-mimo-cutsame-063 createAuxiliaryTimeline](#template-mimo-cutsame-063-createauxiliarytimeline)
- [template-mimo-cutsame-064 getTemplateListByKeyword](#template-mimo-cutsame-064-gettemplatelistbykeyword)
- [template-mimo-cutsame-065 getTemplateListByKeyword](#template-mimo-cutsame-065-gettemplatelistbykeyword)
- [template-mimo-cutsame-066 scanAndFilterAndAnimation](#template-mimo-cutsame-066-scanandfilterandanimation)
- [template-mimo-cutsame-067 scanAndFilterAndAnimation](#template-mimo-cutsame-067-scanandfilterandanimation)
- [template-mimo-cutsame-068 scanAndFilterAndAnimation](#template-mimo-cutsame-068-scanandfilterandanimation)
- [template-mimo-cutsame-069 scanAndFilterAndAnimation](#template-mimo-cutsame-069-scanandfilterandanimation)
- [template-mimo-cutsame-070 getVideoResolution](#template-mimo-cutsame-070-getvideoresolution)
- [template-mimo-cutsame-071 gifToCafStickerTemplateinstall](#template-mimo-cutsame-071-giftocafstickertemplateinstall)
- [template-mimo-cutsame-072 gifToCafStickerTemplateinstall](#template-mimo-cutsame-072-giftocafstickertemplateinstall)
- [template-mimo-cutsame-073 resetEngine](#template-mimo-cutsame-073-resetengine)
- [template-mimo-cutsame-074 initEditData](#template-mimo-cutsame-074-initeditdata)
- [template-mimo-cutsame-075 initListener](#template-mimo-cutsame-075-initlistener)
- [template-mimo-cutsame-076 initListener](#template-mimo-cutsame-076-initlistener)
- [template-mimo-cutsame-077 onClick](#template-mimo-cutsame-077-onclick)
- [template-mimo-cutsame-078 getVideoDuration](#template-mimo-cutsame-078-getvideoduration)
- [template-mimo-cutsame-079 initCompileVideoFragment](#template-mimo-cutsame-079-initcompilevideofragment)
- [template-mimo-cutsame-080 initCompileVideoFragment](#template-mimo-cutsame-080-initcompilevideofragment)
- [template-mimo-cutsame-081 compileProgress](#template-mimo-cutsame-081-compileprogress)
- [template-mimo-cutsame-082 compileFinished](#template-mimo-cutsame-082-compilefinished)
- [template-mimo-cutsame-083 compileFailed](#template-mimo-cutsame-083-compilefailed)
- [template-mimo-cutsame-084 selectCaptionAndTimeSpan](#template-mimo-cutsame-084-selectcaptionandtimespan)
- [template-mimo-cutsame-085 getCurCaption](#template-mimo-cutsame-085-getcurcaption)
- [template-mimo-cutsame-086 initListener](#template-mimo-cutsame-086-initlistener)
- [template-mimo-cutsame-087 initListener](#template-mimo-cutsame-087-initlistener)
- [template-mimo-cutsame-088 setOnSeekBarChangeListener](#template-mimo-cutsame-088-setonseekbarchangelistener)
- [template-mimo-cutsame-089 connectTimelineWithLiveWindow](#template-mimo-cutsame-089-connecttimelinewithlivewindow)
- [template-mimo-cutsame-090 connectTimelineWithLiveWindow](#template-mimo-cutsame-090-connecttimelinewithlivewindow)
- [template-mimo-cutsame-091 onPlaybackPreloadingCompletion](#template-mimo-cutsame-091-onplaybackpreloadingcompletion)
- [template-mimo-cutsame-092 onPlaybackStopped](#template-mimo-cutsame-092-onplaybackstopped)
- [template-mimo-cutsame-093 onPlaybackEOF](#template-mimo-cutsame-093-onplaybackeof)
- [template-mimo-cutsame-094 onDetach](#template-mimo-cutsame-094-ondetach)
- [template-mimo-cutsame-095 playVideoButtonClick](#template-mimo-cutsame-095-playvideobuttonclick)
- [template-mimo-cutsame-096 playVideo](#template-mimo-cutsame-096-playvideo)
- [template-mimo-cutsame-097 playVideoFromStartPosition](#template-mimo-cutsame-097-playvideofromstartposition)
- [template-mimo-cutsame-098 initDrawRectListener](#template-mimo-cutsame-098-initdrawrectlistener)
- [template-mimo-cutsame-099 onAlignClick](#template-mimo-cutsame-099-onalignclick)
- [template-mimo-cutsame-100 onAlignClick](#template-mimo-cutsame-100-onalignclick)
- [template-mimo-cutsame-101 onHorizFlipClick](#template-mimo-cutsame-101-onhorizflipclick)
- [template-mimo-cutsame-102 onHorizFlipClick](#template-mimo-cutsame-102-onhorizflipclick)
- [template-mimo-cutsame-103 setStickerMuteIndex](#template-mimo-cutsame-103-setstickermuteindex)
- [template-mimo-cutsame-104 setAlignIndex](#template-mimo-cutsame-104-setalignindex)
- [template-mimo-cutsame-105 setCurCaption](#template-mimo-cutsame-105-setcurcaption)
- [template-mimo-cutsame-106 getCurCaption](#template-mimo-cutsame-106-getcurcaption)
- [template-mimo-cutsame-107 setCurCompoundCaption](#template-mimo-cutsame-107-setcurcompoundcaption)
- [template-mimo-cutsame-108 curPointIsInnerDrawRect](#template-mimo-cutsame-108-curpointisinnerdrawrect)
- [template-mimo-cutsame-109 isDrawRectVisible](#template-mimo-cutsame-109-isdrawrectvisible)
- [template-mimo-cutsame-110 initRootView](#template-mimo-cutsame-110-initrootview)
- [template-mimo-cutsame-111 convertVideoFile](#template-mimo-cutsame-111-convertvideofile)
- [template-mimo-cutsame-112 onProgress](#template-mimo-cutsame-112-onprogress)
- [template-mimo-cutsame-113 onFinish](#template-mimo-cutsame-113-onfinish)
- [template-mimo-cutsame-114 onStop](#template-mimo-cutsame-114-onstop)
- [template-mimo-cutsame-115 onStop](#template-mimo-cutsame-115-onstop)
- [template-mimo-cutsame-116 getStreamingContext](#template-mimo-cutsame-116-getstreamingcontext)
- [template-mimo-cutsame-117 setMakeRatio](#template-mimo-cutsame-117-setmakeratio)
- [template-mimo-cutsame-118 setVideoResolution](#template-mimo-cutsame-118-setvideoresolution)
- [template-mimo-cutsame-119 getVideoResolution](#template-mimo-cutsame-119-getvideoresolution)
- [template-mimo-cutsame-120 setRecordAudioData](#template-mimo-cutsame-120-setrecordaudiodata)
- [template-mimo-cutsame-121 saveCompoundCaptionData](#template-mimo-cutsame-121-savecompoundcaptiondata)
- [template-mimo-cutsame-122 createTimeline](#template-mimo-cutsame-122-createtimeline)
- [template-mimo-cutsame-123 createTimeline](#template-mimo-cutsame-123-createtimeline)
- [template-mimo-cutsame-124 rebuildTimelineByTemplate](#template-mimo-cutsame-124-rebuildtimelinebytemplate)
- [template-mimo-cutsame-125 addShotVideo](#template-mimo-cutsame-125-addshotvideo)
- [template-mimo-cutsame-126 appendAudioClip](#template-mimo-cutsame-126-appendaudioclip)
- [template-mimo-cutsame-127 setTrackTransition](#template-mimo-cutsame-127-settracktransition)
- [template-mimo-cutsame-128 appendVideoClip](#template-mimo-cutsame-128-appendvideoclip)
- [template-mimo-cutsame-129 changeSpeed](#template-mimo-cutsame-129-changespeed)
- [template-mimo-cutsame-130 createSingleClipTimeline](#template-mimo-cutsame-130-createsinglecliptimeline)
- [template-mimo-cutsame-131 reBuildSingleVideoTrack](#template-mimo-cutsame-131-rebuildsinglevideotrack)
- [template-mimo-cutsame-132 buildTimelineRecordAudio](#template-mimo-cutsame-132-buildtimelinerecordaudio)
- [template-mimo-cutsame-133 getPackageType](#template-mimo-cutsame-133-getpackagetype)
- [template-mimo-cutsame-134 getPackageType](#template-mimo-cutsame-134-getpackagetype)
- [template-mimo-cutsame-135 onDestroy](#template-mimo-cutsame-135-ondestroy)
- [template-mimo-cutsame-136 setOnScrollListener](#template-mimo-cutsame-136-setonscrolllistener)
- [template-mimo-cutsame-137 initTimelineEditor](#template-mimo-cutsame-137-inittimelineeditor)
- [template-mimo-cutsame-138 addTimeSpan](#template-mimo-cutsame-138-addtimespan)
- [template-mimo-cutsame-139 addTimeSpanExt](#template-mimo-cutsame-139-addtimespanext)
- [template-mimo-cutsame-140 selectTimeSpan](#template-mimo-cutsame-140-selecttimespan)
- [template-mimo-cutsame-141 getSequenceWidth](#template-mimo-cutsame-141-getsequencewidth)
- [template-mimo-cutsame-142 timeSpanCount](#template-mimo-cutsame-142-timespancount)
- [template-mimo-cutsame-143 getRightHandleView](#template-mimo-cutsame-143-getrighthandleview)
- [template-mimo-cutsame-144 onProgress](#template-mimo-cutsame-144-onprogress)
- [template-mimo-cutsame-145 onFinish](#template-mimo-cutsame-145-onfinish)
- [template-mimo-cutsame-146 applyVideoFxTemplate](#template-mimo-cutsame-146-applyvideofxtemplate)
- [template-mimo-cutsame-147 addMusicInfoData](#template-mimo-cutsame-147-addmusicinfodata)
- [template-mimo-cutsame-148 getTemplateAspectRatio](#template-mimo-cutsame-148-gettemplateaspectratio)
- [template-mimo-cutsame-149 setRealInpoint](#template-mimo-cutsame-149-setrealinpoint)
- [template-mimo-cutsame-150 setClipIndexInTimelineList](#template-mimo-cutsame-150-setclipindexintimelinelist)
- [template-mimo-cutsame-151 getCaptionType](#template-mimo-cutsame-151-getcaptiontype)
- [template-mimo-cutsame-152 setNvsCaption](#template-mimo-cutsame-152-setnvscaption)
- [template-mimo-cutsame-153 getNvsCaption](#template-mimo-cutsame-153-getnvscaption)
- [template-mimo-cutsame-154 setNvsCompoundCaption](#template-mimo-cutsame-154-setnvscompoundcaption)
- [template-mimo-cutsame-155 create](#template-mimo-cutsame-155-create)
- [template-mimo-cutsame-156 create](#template-mimo-cutsame-156-create)
- [template-mimo-cutsame-157 create](#template-mimo-cutsame-157-create)
- [template-mimo-cutsame-158 clone](#template-mimo-cutsame-158-clone)
- [template-mimo-cutsame-159 getTemplateFootageDesc](#template-mimo-cutsame-159-gettemplatefootagedesc)
- [template-mimo-cutsame-160 getTemplateFootageDescVideo](#template-mimo-cutsame-160-gettemplatefootagedescvideo)
- [template-mimo-cutsame-161 getAllNvsTemplateFootageDescs](#template-mimo-cutsame-161-getallnvstemplatefootagedescs)
- [template-mimo-cutsame-162 getAllNvsTemplateFootageDescs](#template-mimo-cutsame-162-getallnvstemplatefootagedescs)
- [template-mimo-cutsame-163 getTemplateVideoClip](#template-mimo-cutsame-163-gettemplatevideoclip)
- [template-mimo-cutsame-164 getTemplateVideoClip](#template-mimo-cutsame-164-gettemplatevideoclip)
- [template-mimo-cutsame-165 getTemplateVideoClip](#template-mimo-cutsame-165-gettemplatevideoclip)
- [template-mimo-cutsame-166 needDealFootageDesc](#template-mimo-cutsame-166-needdealfootagedesc)
- [template-mimo-cutsame-167 getTemplateCaptionsForStandard](#template-mimo-cutsame-167-gettemplatecaptionsforstandard)
- [template-mimo-cutsame-168 getTemplateCaptions](#template-mimo-cutsame-168-gettemplatecaptions)
- [template-mimo-cutsame-169 getTemplateCompoundCaptions](#template-mimo-cutsame-169-gettemplatecompoundcaptions)
- [template-mimo-cutsame-170 getTemplateCaptions](#template-mimo-cutsame-170-gettemplatecaptions)
- [template-mimo-cutsame-171 hasTemplateCaptions](#template-mimo-cutsame-171-hastemplatecaptions)
- [template-mimo-cutsame-172 createTimeline](#template-mimo-cutsame-172-createtimeline)
- [template-mimo-cutsame-173 createTimeline](#template-mimo-cutsame-173-createtimeline)
- [template-mimo-cutsame-174 getCaptionByTemplateCaptionDesc](#template-mimo-cutsame-174-getcaptionbytemplatecaptiondesc)
- [template-mimo-cutsame-175 loadTimelineToTemplate](#template-mimo-cutsame-175-loadtimelinetotemplate)
<!-- END GENERATED CONTENTS -->

## `template-mimo-cutsame-001` `bindLayout`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:56`

API classes: `NvsStreamingContext`, `NvsRational`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720`, `NvsStreamingContext.ImageGrabberCallback`
Common calls: `getExtras()`, `getString()`, `getInt()`, `getInstance()`, `grabImageFromTimelineAsync()`, `ImageGrabberCallback()`, `setImageBitmap()`, `updateTemplateInteraction()`

Simple sequence:

```java
if (intent != null) {
Bundle bundle = intent.getExtras();
if (bundle != null) {
mTemplateId = bundle.getString(TEMPLATE_ID);
mCompileResolution = bundle.getInt(COMPILE_RESOLUTION, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720);
EditorController.getInstance().grabImageFromTimelineAsync(0, new NvsRational(1, 1), 0, new NvsStreamingContext.ImageGrabberCallback() {
if (mCutCompileSource != null) {
mCutCompileSource.setImageBitmap(bitmap);
```

## `template-mimo-cutsame-002` `initData`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:58`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720`
Common calls: `getExtras()`, `getString()`, `getInt()`

Simple sequence:

```java
if (intent != null) {
Bundle bundle = intent.getExtras();
if (bundle != null) {
mTemplateId = bundle.getString(TEMPLATE_ID);
mCompileResolution = bundle.getInt(COMPILE_RESOLUTION, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720);
```

## `template-mimo-cutsame-003` `initData`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:60`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720`
Common calls: `getString()`, `getInt()`

Simple sequence:

```java
if (bundle != null) {
mTemplateId = bundle.getString(TEMPLATE_ID);
mCompileResolution = bundle.getInt(COMPILE_RESOLUTION, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720);
```

## `template-mimo-cutsame-004` `onCompileProgress`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:139`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onCompileFinished(NvsTimeline nvsTimeline) {
```

## `template-mimo-cutsame-005` `onCompileFinished`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:144`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onCompileFailed(NvsTimeline nvsTimeline) {
```

## `template-mimo-cutsame-006` `onCompileFailed`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:147`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.CompileCallback2`
Common calls: `CompileCallback2()`

Simple sequence:

```java
}, new NvsStreamingContext.CompileCallback2() {
```

## `template-mimo-cutsame-007` `onCompileFailed`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutCompileActivity.java:149`

API classes: `NvsTimeline`
Common calls: `setVisibility()`, `getInstance()`, `setText()`, `exists()`, `scanFile()`, `clearCompileConfigurations()`, `changeVideoSize()`

Simple sequence:

```java
public void onCompileCompleted(NvsTimeline nvsTimeline, boolean b) {
if (!b) {
mCutCompileProgress.setVisibility(View.GONE);
mCutCompileProgressText.setVisibility(View.GONE);
mCutCompileCancel.setVisibility(View.GONE);
mCutCompileTip.setText(R.string.activity_cut_compile_tip2);
mCutCompileOk.setVisibility(View.VISIBLE);
EditorController.getInstance().clearCompileConfigurations();
EditorController.getInstance().changeVideoSize(mBeforeChangeVideoPoint.x, mBeforeChangeVideoPoint.y);
```

## `template-mimo-cutsame-008` `bindLayout`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:98`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getInstance()`, `e()`, `getStringExtra()`, `equals()`, `createAuxiliaryStreamingContext()`, `setAuxiliaryTimeline()`, `getVideoResolutionByRatio()`, `appendVideoTrack()`, `appendClip()`, `getFilePath()`, `applyThemeTemplate()`, `getParcelableArrayListExtra()`

Simple sequence:

```java
if (intent != null) {
mTemplateClips = intent.getParcelableArrayListExtra(CustomConstants.TEMPLATE_CLIP_LIST);
mTemplateId = intent.getStringExtra(CustomConstants.TEMPLATE_ID);
mTemplateType = intent.getStringExtra(CustomConstants.TEMPLATE_TYPE);
mBeforeTimeLine = createTimeline(EditorController.getInstance().getStreamingContext());
if (mBeforeTimeLine == null) {
LogUtils.e("failed to create timeline");
NvsTimeline auxiliaryTimeline = createTimeline(EditorController.getInstance().createAuxiliaryStreamingContext());
EditorController.getInstance().setAuxiliaryTimeline(auxiliaryTimeline);
int ratio = getIntent().getIntExtra(CustomConstants.TEMPLATE_RATIO, 1);
mBeforeTimeLine = TimelineUtil.newTimeline(EditorController.getInstance().getVideoResolutionByRatio(ratio));
if (mBeforeTimeLine == null) {
LogUtils.e("failed to create timeline");
NvsVideoTrack nvsVideoTrack = mBeforeTimeLine.appendVideoTrack();
nvsVideoTrack.setVolumeGain(0, 0);
for (TemplateClip templateClip : mTemplateClips) {
NvsVideoClip nvsVideoClip = nvsVideoTrack.appendClip(templateClip.getFilePath());
mBeforeTimeLine.applyThemeTemplate(mTemplateId);
NvsTimeline auxiliaryTimeline = mPresenter.createAuxiliaryTimeline(EditorController.getInstance().createAuxiliaryStreamingContext(), EditorController.getInstance().getVideoResolutionByRatio(ratio));
NvsVideoTrack auxiliaryTrack = auxiliaryTimeline.appendVideoTrack();
for (TemplateClip templateClip : mTemplateClips) {
NvsVideoClip nvsVideoClip = auxiliaryTrack.appendClip(templateClip.getFilePath());
auxiliaryTimeline.applyThemeTemplate(mTemplateId);
EditorController.getInstance().setAuxiliaryTimeline(auxiliaryTimeline);
// ... 1 more SDK-related lines omitted in this compressed snippet ...
```

## `template-mimo-cutsame-009` `onProgressChanged`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:334`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`
Common calls: `getInstance()`, `seekTimeline()`

Simple sequence:

```java
if (mState != TailorView.FROM_VIDEO) {
EditorController.getInstance().seekTimeline(nvTime, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
```

## `template-mimo-cutsame-010` `parseNvsVideoClip`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:398`

API classes: `NvsVideoClip`
Common calls: `getTrimIn()`, `getTrimOut()`, `setInPoint()`, `getInPoint()`, `setOutPoint()`, `getOutPoint()`, `setTrimIn()`, `setTrimOut()`, `setDuration()`, `setFilePath()`, `getFilePath()`

Simple sequence:

```java
private void parseNvsVideoClip(NvsVideoClip nvsVideoClip, TemplateClip templateClip) {
if (nvsVideoClip != null) {
templateClip.setInPoint(nvsVideoClip.getInPoint());
templateClip.setOutPoint(nvsVideoClip.getOutPoint());
templateClip.setTrimIn(nvsVideoClip.getTrimIn());
templateClip.setTrimOut(nvsVideoClip.getTrimOut());
templateClip.setDuration(nvsVideoClip.getTrimOut() - nvsVideoClip.getTrimIn());
templateClip.setFilePath(nvsVideoClip.getFilePath());
```

## `template-mimo-cutsame-011` `createTimeline`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:411`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.templateFootageInfo`
Common calls: `templateFootageInfo()`, `getFootageId()`, `getReversePath()`, `getFilePath()`, `add()`

Simple sequence:

```java
for (TemplateClip templateClip : mTemplateClips) {
NvsStreamingContext.templateFootageInfo footageInfo = new NvsStreamingContext.templateFootageInfo();
footageInfo.footageId = templateClip.getFootageId();
footageInfo.reverseFilePath = templateClip.getReversePath();
footageInfo.filePath = templateClip.getFilePath();
```

## `template-mimo-cutsame-012` `changeVideoClipPath`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:433`

API classes: `NvsVideoClip`, `NvsTimeline`, `NvsVideoTrack`
Common calls: `changeFilePath()`, `getTrackIndex()`, `getInPoint()`, `getNeedReverse()`, `getReversePath()`, `getFilePath()`, `videoTrackCount()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `getInstance()`, `getClipIndexInTimelineList()`

Simple sequence:

```java
private void changeVideoClipPath(NvsTimeline timeLine) {
NvsVideoTrack nvsVideoTrack = timeLine.getVideoTrackByIndex(i);
for (int j = 0; j < nvsVideoTrack.getClipCount(); j++) {
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(j);
for (TemplateClip clip : mTemplateClips) {
if (clip.getTrackIndex() == i && clip.getInPoint() == nvsVideoClip.getInPoint()) {
if (clip.getNeedReverse()) {
nvsVideoClip.changeFilePath(clip.getReversePath());
nvsVideoClip.changeFilePath(clip.getFilePath());
for (TemplateClip clip : mTemplateClips) {
NvsVideoClip nvsVideoClip = EditorController.getInstance().
getVideoClipByTemplateFootageCorrespondingClipInfo(timeLine, clip.getClipIndexInTimelineList(),
clip.getClipTrackIndexInTimelineList()
, clip.getTrackIndex(), clip.getClipIndex());
if (nvsVideoClip != null) {
if (clip.getNeedReverse()) {
nvsVideoClip.changeFilePath(clip.getReversePath());
nvsVideoClip.changeFilePath(clip.getFilePath());
```

## `template-mimo-cutsame-013` `changeVideoClipPath`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:434`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getInPoint()`, `changeFilePath()`, `videoTrackCount()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `getTrackIndex()`, `getNeedReverse()`, `getReversePath()`, `getFilePath()`

Simple sequence:

```java
NvsVideoTrack nvsVideoTrack = timeLine.getVideoTrackByIndex(i);
for (int j = 0; j < nvsVideoTrack.getClipCount(); j++) {
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(j);
for (TemplateClip clip : mTemplateClips) {
if (clip.getTrackIndex() == i && clip.getInPoint() == nvsVideoClip.getInPoint()) {
if (clip.getNeedReverse()) {
nvsVideoClip.changeFilePath(clip.getReversePath());
nvsVideoClip.changeFilePath(clip.getFilePath());
```

## `template-mimo-cutsame-014` `changeVideoClipPath`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:436`

API classes: `NvsVideoClip`
Common calls: `getInPoint()`, `changeFilePath()`, `getClipCount()`, `getClipByIndex()`, `getTrackIndex()`, `getNeedReverse()`, `getReversePath()`, `getFilePath()`

Simple sequence:

```java
for (int j = 0; j < nvsVideoTrack.getClipCount(); j++) {
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(j);
for (TemplateClip clip : mTemplateClips) {
if (clip.getTrackIndex() == i && clip.getInPoint() == nvsVideoClip.getInPoint()) {
if (clip.getNeedReverse()) {
nvsVideoClip.changeFilePath(clip.getReversePath());
nvsVideoClip.changeFilePath(clip.getFilePath());
```

## `template-mimo-cutsame-015` `onSeekingTimelinePosition`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:515`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onSeekingTimelinePosition(NvsTimeline timeline, long position) {
```

## `template-mimo-cutsame-016` `onActivityResult`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:580`

API classes: `NvsVideoClip`, `NvsVideoTrack`
Common calls: `getInstance()`, `get()`, `equals()`, `setNvsTimeline()`, `connectTimelineWithLiveWindow()`, `getLongExtra()`, `getSelectedTabPosition()`, `getClipByIndex()`, `size()`, `getDuration()`, `changClipTrim()`, `getVideoTrackByIndex()`

Simple sequence:

```java
EditorController.getInstance().setNvsTimeline(mBeforeTimeLine);
mBaseVideoFragment.connectTimelineWithLiveWindow();
long newTrim = data != null ? data.getLongExtra(INTENT_TRAM, 0) : 0;
CutEditorVpFragment cutEditorVpFragment = mFragmentList.get(mTableLayout.getSelectedTabPosition());
EditorController.getInstance().setNvsTimeline(mBeforeTimeLine);
mBaseVideoFragment.connectTimelineWithLiveWindow();
NvsVideoTrack nvsVideoTrack = mBeforeTimeLine.getVideoTrackByIndex(0);
int curIndex = data.getIntExtra(INTENT_EDIT_CLIP_INDEX, 0);
long newTrimIn = data != null ? data.getLongExtra(INTENT_TRAM_IN, 0) : 0;
long newTrimOut = data != null ? data.getLongExtra(INTENT_TRAM_OUT, 0) : 0;
NvsVideoClip clipByIndex = nvsVideoTrack.getClipByIndex(curIndex);
if (null != clipByIndex) {
clipByIndex.changeTrimInPoint(newTrimIn, true);
clipByIndex.changeTrimOutPoint(newTrimOut, true);
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(i);
CutEditorVpFragment cutEditorVpFragment = mFragmentList.get(mTableLayout.getSelectedTabPosition());
List<TemplateCaptionDesc> templateCaptions = EditorController.getInstance().getTemplateCaptions(mBeforeTimeLine);
String nvStringTime = FormatUtils.microsecond2Time(mBeforeTimeLine.getDuration());
mPlayControlView.setCurrentText(nvStringTime);
int duration = (int) (mBeforeTimeLine.getDuration() / 1000f);
mPlayControlView.setMax(duration);
EditorController.getInstance().setNvsTimeline(mBeforeTimeLine);
TimelineUtil.loadTimelineToTemplate(EditorController.getInstance().getNvsTimeline());
mBaseVideoFragment.connectTimelineWithLiveWindow();
```

## `template-mimo-cutsame-017` `onActivityResult`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:582`

API classes: `NvsVideoClip`, `NvsVideoTrack`
Common calls: `get()`, `getInstance()`, `getLongExtra()`, `equals()`, `setNvsTimeline()`, `connectTimelineWithLiveWindow()`, `getSelectedTabPosition()`, `getClipByIndex()`, `size()`, `getDuration()`, `changClipTrim()`, `getVideoTrackByIndex()`

Simple sequence:

```java
EditorController.getInstance().setNvsTimeline(mBeforeTimeLine);
mBaseVideoFragment.connectTimelineWithLiveWindow();
long newTrim = data != null ? data.getLongExtra(INTENT_TRAM, 0) : 0;
CutEditorVpFragment cutEditorVpFragment = mFragmentList.get(mTableLayout.getSelectedTabPosition());
EditorController.getInstance().setNvsTimeline(mBeforeTimeLine);
mBaseVideoFragment.connectTimelineWithLiveWindow();
NvsVideoTrack nvsVideoTrack = mBeforeTimeLine.getVideoTrackByIndex(0);
int curIndex = data.getIntExtra(INTENT_EDIT_CLIP_INDEX, 0);
long newTrimIn = data != null ? data.getLongExtra(INTENT_TRAM_IN, 0) : 0;
long newTrimOut = data != null ? data.getLongExtra(INTENT_TRAM_OUT, 0) : 0;
NvsVideoClip clipByIndex = nvsVideoTrack.getClipByIndex(curIndex);
if (null != clipByIndex) {
clipByIndex.changeTrimInPoint(newTrimIn, true);
clipByIndex.changeTrimOutPoint(newTrimOut, true);
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(i);
CutEditorVpFragment cutEditorVpFragment = mFragmentList.get(mTableLayout.getSelectedTabPosition());
List<TemplateCaptionDesc> templateCaptions = EditorController.getInstance().getTemplateCaptions(mBeforeTimeLine);
String nvStringTime = FormatUtils.microsecond2Time(mBeforeTimeLine.getDuration());
mPlayControlView.setCurrentText(nvStringTime);
int duration = (int) (mBeforeTimeLine.getDuration() / 1000f);
mPlayControlView.setMax(duration);
```

## `template-mimo-cutsame-018` `deleteAddedHeadAndTail`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameEditorActivity.java:725`

API classes: `NvsTimeline`, `NvsVideoTrack`
Common calls: `removeClip()`, `isEmpty()`, `getVideoTrackByIndex()`, `getClipCount()`, `size()`

Simple sequence:

```java
private void deleteAddedHeadAndTail(NvsTimeline mBeforeTimeLine, List<TemplateClip> mTemplateClips) {
NvsVideoTrack videoTrackByIndex = mBeforeTimeLine.getVideoTrackByIndex(0);
int clipCount = videoTrackByIndex.getClipCount();
if (clipCount > mTemplateClips.size()) {
videoTrackByIndex.removeClip(clipCount - 1, false);
videoTrackByIndex.removeClip(0, false);
```

## `template-mimo-cutsame-019` `getMaterialList`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:39`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `valueOf()`, `getType()`, `getCategory()`, `getKind()`, `getSorted()`, `get()`, `requestGet()`

Simple sequence:

```java
params.put("type", assetType.getType());
params.put("category", assetType.getCategory());
params.put("kind", assetType.getKind());
params.put("sorted", String.valueOf(assetType.getSorted()));
NvsServerClient.get().requestGet(tag, apiName, params, callback);
```

## `template-mimo-cutsame-020` `getTemplateCategory`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:67`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `isZh()`, `get()`, `requestGet()`

Simple sequence:

```java
NvsServerClient.get().requestGet(tag, CUT_SAME_TEMPLATE_CATEGORY, "", params, callback);
```

## `template-mimo-cutsame-021` `getTemplateList`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:84`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `valueOf()`, `isZh()`, `get()`, `requestGet()`

Simple sequence:

```java
NvsServerClient.get().requestGet(tag, apiName, params, callback);
```

## `template-mimo-cutsame-022` `uploadUsedTemplate`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:104`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `put()`, `get()`, `requestPost()`

Simple sequence:

```java
NvsServerClient.get().requestPost(tag, apiName, params, callback);
```

## `template-mimo-cutsame-023` `download`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:123`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `get()`, `download()`

Simple sequence:

```java
NvsServerClient.get().download(tag, url, filePath, fileName, listener);
```

## `template-mimo-cutsame-024` `cancelAll`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:131`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `get()`, `cancelAll()`

Simple sequence:

```java
NvsServerClient.get().cancelAll();
```

## `template-mimo-cutsame-025` `cancelRequest`

Source: `MCutSame/src/main/java/com/meishe/cutsame/CutSameNetApi.java:141`

API classes: `NvsServerClient`
Static/constants: `NvsServerClient.get`
Common calls: `get()`, `cancelRequest()`

Simple sequence:

```java
NvsServerClient.get().cancelRequest(tag);
```

## `template-mimo-cutsame-026` `onResume`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:192`

API classes: `NvsMediaFileConvertor`
Common calls: `getInstance()`, `getSerializableExtra()`, `isEmpty()`, `getCurrentTimeline()`, `e()`, `getStreamingContext()`, `getMakeRatio()`, `grabImageFromTimeline()`, `randomUUID()`, `toString()`, `toUpperCase()`

Simple sequence:

```java
if (intent != null) {
mData = (List<ExportTemplateSection>) intent.getSerializableExtra(CustomConstants.TEMPLATE_CLIP_DATA);
EditorEngine mEditorEngine = EditorEngine.getInstance();
mTimeLine = EditorEngine.getInstance().getCurrentTimeline();
if (mTimeLine == null) {
LogUtils.e("timeline is null !!!");
mStreamingContext = mEditorEngine.getStreamingContext();
mRatio = TimelineData.getInstance().getMakeRatio();
mCoverBitmap = mStreamingContext.grabImageFromTimeline(mTimeLine, 0, null);
if (mMediaFileConverter == null) {
mMediaFileConverter = new NvsMediaFileConvertor();
```

## `template-mimo-cutsame-027` `initCaptionData`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:231`

API classes: `NvsTimelineCaption`, `NvsVideoClip`
Static/constants: `NvsVideoClip.TEMPLATE_KEY_REPLACE_ID`
Common calls: `getFirstCaption()`, `setTemplateAttachment()`, `valueOf()`, `getNextCaption()`

Simple sequence:

```java
NvsTimelineCaption firstCaption = mTimeLine.getFirstCaption();
firstCaption.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_REPLACE_ID, String.valueOf(index));
firstCaption = mTimeLine.getNextCaption(firstCaption);
```

## `template-mimo-cutsame-028` `initCaptionData`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:234`

API classes: `NvsVideoClip`
Static/constants: `NvsVideoClip.TEMPLATE_KEY_REPLACE_ID`
Common calls: `setTemplateAttachment()`, `valueOf()`, `getNextCaption()`

Simple sequence:

```java
firstCaption.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_REPLACE_ID, String.valueOf(index));
firstCaption = mTimeLine.getNextCaption(firstCaption);
```

## `template-mimo-cutsame-029` `onCompileFailed`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:312`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.CompileCallback2`
Common calls: `setCompileCallback2()`, `CompileCallback2()`, `setCompileConfigurations()`, `showShort()`

Simple sequence:

```java
mStreamingContext.setCompileCallback2(new NvsStreamingContext.CompileCallback2() {
public void onCompileCompleted(NvsTimeline nvsTimeline, boolean b) {
mStreamingContext.setCompileConfigurations(null);
```

## `template-mimo-cutsame-030` `initVideoClip`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:408`

API classes: `NvsAudioClip`, `NvsVideoClip`, `NvsVideoTrack`, `NvsAudioTrack`
Static/constants: `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NAME`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TYPE`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_ID`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TAGS`
Common calls: `setTemplateAttachment()`, `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `isLock()`, `exists()`, `getName()`, `getFootageGroupsId()`, `clear()`, `getVideoTrackByIndex()`, `add()`, `getImagePath()`

Simple sequence:

```java
for (int m = 0; m < MAX_TRACK_COUNT; m++) {
NvsVideoTrack videoTrackByIndex = mTimeLine.getVideoTrackByIndex(m);
if (videoTrackByIndex != null) {
int clipCount = videoTrackByIndex.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrackByIndex.getClipByIndex(i);
ExportTemplateClip exportTemplateClip = findExportTemplateClip(m, videoClip.getInPoint());
String imagePath = exportTemplateClip.getImagePath();
if (file.exists()) {
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME, file.getName());
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID, "footage" + (exportTemplateClip.getFootageGroupsId() == 0 ?
exportTemplateClip.getFootageId() : exportTemplateClip.getFootageGroupsId() * FOOTAGE_ID_BASE_NUMBER));
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE, exportTemplateClip.getFootageType());
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE, exportTemplateClip.isLock() ? "false" : "true");
MeicamVideoClip meicamVideoClip = (MeicamVideoClip) TimelineDataUtil.getVideoClip(videoTrackByIndex.getIndex(), videoClip.getInPoint());
if (meicamVideoClip != null) {
videoClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE, meicamVideoClip.getVideoReverse() + "");
NvsAudioTrack nvsAudioTrack = mTimeLine.getAudioTrackByIndex(m);
if (nvsAudioTrack != null) {
for (int i = 0; i < nvsAudioTrack.getClipCount(); i++) {
NvsAudioClip nvsAudioClip = nvsAudioTrack.getClipByIndex(i);
String imagePath = nvsAudioClip.getFilePath();
if (file.exists()) {
nvsAudioClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NAME, file.getName());
// ... 4 more SDK-related lines omitted in this compressed snippet ...
```

## `template-mimo-cutsame-031` `initVideoClip`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:411`

API classes: `NvsAudioClip`, `NvsVideoClip`, `NvsVideoTrack`, `NvsAudioTrack`
Static/constants: `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NAME`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TYPE`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_ID`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_TAGS`
Common calls: `setTemplateAttachment()`, `getClipCount()`, `getClipByIndex()`, `getInPoint()`, `isLock()`, `exists()`, `getName()`, `getFootageGroupsId()`, `getVideoTrackByIndex()`, `add()`, `getImagePath()`, `getFootageId()`

Simple sequence:

```java
for (int m = 0; m < MAX_TRACK_COUNT; m++) {
NvsVideoTrack videoTrackByIndex = mTimeLine.getVideoTrackByIndex(m);
if (videoTrackByIndex != null) {
int clipCount = videoTrackByIndex.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrackByIndex.getClipByIndex(i);
ExportTemplateClip exportTemplateClip = findExportTemplateClip(m, videoClip.getInPoint());
String imagePath = exportTemplateClip.getImagePath();
if (file.exists()) {
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME, file.getName());
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID, "footage" + (exportTemplateClip.getFootageGroupsId() == 0 ?
exportTemplateClip.getFootageId() : exportTemplateClip.getFootageGroupsId() * FOOTAGE_ID_BASE_NUMBER));
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE, exportTemplateClip.getFootageType());
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE, exportTemplateClip.isLock() ? "false" : "true");
MeicamVideoClip meicamVideoClip = (MeicamVideoClip) TimelineDataUtil.getVideoClip(videoTrackByIndex.getIndex(), videoClip.getInPoint());
if (meicamVideoClip != null) {
videoClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE, meicamVideoClip.getVideoReverse() + "");
NvsAudioTrack nvsAudioTrack = mTimeLine.getAudioTrackByIndex(m);
if (nvsAudioTrack != null) {
for (int i = 0; i < nvsAudioTrack.getClipCount(); i++) {
NvsAudioClip nvsAudioClip = nvsAudioTrack.getClipByIndex(i);
String imagePath = nvsAudioClip.getFilePath();
if (file.exists()) {
nvsAudioClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NAME, file.getName());
// ... 4 more SDK-related lines omitted in this compressed snippet ...
```

## `template-mimo-cutsame-032` `initVideoClip`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:413`

API classes: `NvsVideoClip`, `NvsAudioClip`
Static/constants: `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE`, `NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE`, `NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE`
Common calls: `setTemplateAttachment()`, `getInPoint()`, `isLock()`, `getFootageGroupsId()`, `getClipCount()`, `getClipByIndex()`, `add()`, `getImagePath()`, `exists()`, `getName()`, `getFootageId()`, `getFootageType()`

Simple sequence:

```java
if (videoTrackByIndex != null) {
int clipCount = videoTrackByIndex.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrackByIndex.getClipByIndex(i);
ExportTemplateClip exportTemplateClip = findExportTemplateClip(m, videoClip.getInPoint());
String imagePath = exportTemplateClip.getImagePath();
if (file.exists()) {
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_NAME, file.getName());
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_ID, "footage" + (exportTemplateClip.getFootageGroupsId() == 0 ?
exportTemplateClip.getFootageId() : exportTemplateClip.getFootageGroupsId() * FOOTAGE_ID_BASE_NUMBER));
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_TYPE, exportTemplateClip.getFootageType());
videoClip.setTemplateAttachment(NvsVideoClip.TEMPLATE_KEY_FOOTAGE_CAN_REPLACE, exportTemplateClip.isLock() ? "false" : "true");
MeicamVideoClip meicamVideoClip = (MeicamVideoClip) TimelineDataUtil.getVideoClip(videoTrackByIndex.getIndex(), videoClip.getInPoint());
if (meicamVideoClip != null) {
videoClip.setTemplateAttachment(NvsAudioClip.TEMPLATE_KEY_FOOTAGE_NEED_REVERSE, meicamVideoClip.getVideoReverse() + "");
```

## `template-mimo-cutsame-033` `saveNeedVideoClip`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:519`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT`
Common calls: `endsWith()`, `isEmpty()`, `convertMeidaFile()`, `isVideoReverse()`, `size()`, `get()`, `getImagePath()`, `exists()`, `getName()`, `createOrExistsFile()`, `copySdcardFile()`, `getTrimIn()`

Simple sequence:

```java
String imagePath = exportTemplateClip.getImagePath();
String fileName = file.getName();
long trimIn = exportTemplateClip.getTrimIn();
long trimOut = exportTemplateClip.getTrimOut();
hashtable.put(NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT, 1080);
```

## `template-mimo-cutsame-034` `saveNeedVideoClip`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateActivity.java:523`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT`
Common calls: `endsWith()`, `convertMeidaFile()`, `isVideoReverse()`, `size()`, `get()`, `getImagePath()`, `isEmpty()`, `exists()`, `getName()`, `createOrExistsFile()`, `copySdcardFile()`, `getTrimIn()`

Simple sequence:

```java
String imagePath = exportTemplateClip.getImagePath();
String fileName = file.getName();
long trimIn = exportTemplateClip.getTrimIn();
long trimOut = exportTemplateClip.getTrimOut();
hashtable.put(NvsMediaFileConvertor.CONVERTOR_CUSTOM_VIDEO_HEIGHT, 1080);
```

## `template-mimo-cutsame-035` `onProgressChanged`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:168`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`
Common calls: `getInstance()`, `seekTimeline()`

Simple sequence:

```java
if (fromUser) {
EditorController.getInstance().seekTimeline(nvTime, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
```

## `template-mimo-cutsame-036` `setPlayControlViewProgress`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:209`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `setProgress()`, `seekTimeline()`, `beginTransaction()`, `PlayEventListener()`, `getDuration()`, `getTimelineCurrentPosition()`, `setStartText()`, `microsecond2Time()`, `changPlayState()`, `getInstance()`, `isPlaying()`, `add()`

Simple sequence:

```java
public void playBackEOF(NvsTimeline timeline) {
if (timeline.getDuration() - mStreamingContext.getTimelineCurrentPosition(mTimeLine) <= 40000) {
mPlayControlView.setStartText(FormatUtils.microsecond2Time(0));
mPlayControlView.setProgress(0);
mPlayerFragment.seekTimeline(0, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (!mTouchToChangeProgress) {
mPlayControlView.setProgress((int) (stamp / 1000));
mPlayControlView.changPlayState(EditorController.getInstance().isPlaying());
mPlayerFragment = new PlayerFragment(mTimeLine, mStreamingContext, listener);
mPlayerFragment.seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `template-mimo-cutsame-037` `initVideoFragment`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:212`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `setProgress()`, `PlayEventListener()`, `getDuration()`, `getTimelineCurrentPosition()`, `setStartText()`, `microsecond2Time()`, `seekTimeline()`, `changPlayState()`, `getInstance()`, `isPlaying()`

Simple sequence:

```java
public void playBackEOF(NvsTimeline timeline) {
if (timeline.getDuration() - mStreamingContext.getTimelineCurrentPosition(mTimeLine) <= 40000) {
mPlayControlView.setStartText(FormatUtils.microsecond2Time(0));
mPlayControlView.setProgress(0);
mPlayerFragment.seekTimeline(0, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (!mTouchToChangeProgress) {
mPlayControlView.setProgress((int) (stamp / 1000));
mPlayControlView.changPlayState(EditorController.getInstance().isPlaying());
```

## `template-mimo-cutsame-038` `initVideoFragment`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:214`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getDuration()`, `getTimelineCurrentPosition()`, `setStartText()`, `microsecond2Time()`, `setProgress()`, `seekTimeline()`

Simple sequence:

```java
public void playBackEOF(NvsTimeline timeline) {
if (timeline.getDuration() - mStreamingContext.getTimelineCurrentPosition(mTimeLine) <= 40000) {
mPlayControlView.setStartText(FormatUtils.microsecond2Time(0));
mPlayControlView.setProgress(0);
mPlayerFragment.seekTimeline(0, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `template-mimo-cutsame-039` `playStopped`

Source: `MCutSame/src/main/java/com/meishe/cutsame/ExportTemplateSettingActivity.java:229`

API classes: `NvsTimeline`
Common calls: `setProgress()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (!mTouchToChangeProgress) {
mPlayControlView.setProgress((int) (stamp / 1000));
```

## `template-mimo-cutsame-040` `bindLayout`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TailorActivity.java:63`

API classes: `NvsTimeline`
Common calls: `getInstance()`, `getLong()`, `add()`, `getExtras()`, `getString()`, `getInt()`, `isEmpty()`, `newTimeline()`, `getVideoEditResolutionByClip()`, `setNvsTimeline()`, `seekTimeline()`, `getVideoDuration()`

Simple sequence:

```java
Bundle extras = getIntent().getExtras();
if (null != extras) {
mVideoPath = extras.getString(VIDEO_PATH);
mVideoLimit = extras.getLong(VIDEO_LIMIT);
mVideoType = extras.getInt(VIDEO_TYPE);
mStartTrim = extras.getLong(START_TRIM);
if (!TextUtils.isEmpty(mVideoPath)) {
NvsTimeline nvsTimeline = TimelineUtil.newTimeline(TimelineUtil.getVideoEditResolutionByClip(mVideoPath));
EditorController.getInstance().setNvsTimeline(nvsTimeline);
EditorController.getInstance().seekTimeline(mNowStartTime);
if (mVideoType == StreamingConstant.VideoClipType.VIDEO_CLIP_TYPE_AV) {
duration = EditorController.getInstance().getVideoDuration(mVideoPath);
newClip.setTrimOut(duration);
meicamVideoTrack.getClipInfoList().add(newClip);
TimelineUtil.fillTrack(EditorController.getInstance().getNvsTimeline(), videoTrackList);
```

## `template-mimo-cutsame-041` `bindLayout`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:84`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `getInt()`, `getLong()`, `add()`, `getExtras()`, `getString()`, `isEmpty()`, `newTimeline()`, `getVideoEditResolutionByClip()`, `setNvsTimeline()`, `seekTimeline()`, `getVideoDuration()`

Simple sequence:

```java
Bundle extras = getIntent().getExtras();
if (null != extras) {
mVideoPath = extras.getString(VIDEO_PATH);
mVideoType = extras.getInt(VIDEO_TYPE);
mStartTrim = extras.getLong(START_TRIM);
mEndTrim = extras.getLong(END_TRIM);
clipIndex = extras.getInt(CLIP_INDEX);
mNvsStreamingContext = NvsStreamingContext.getInstance();
if (!TextUtils.isEmpty(mVideoPath)) {
mNvsTimeline = TimelineUtil.newTimeline(TimelineUtil.getVideoEditResolutionByClip(mVideoPath));
EditorController.getInstance().setNvsTimeline(mNvsTimeline);
EditorController.getInstance().seekTimeline(mNowStartTime);
if (mVideoType == StreamingConstant.VideoClipType.VIDEO_CLIP_TYPE_AV) {
duration = EditorController.getInstance().getVideoDuration(mVideoPath);
newClip.setTrimOut(duration);
meicamVideoTrack.getClipInfoList().add(newClip);
TimelineUtil.fillTrack(EditorController.getInstance().getNvsTimeline(), videoTrackList);
```

## `template-mimo-cutsame-042` `initMultiSequence`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:211`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getDuration()`, `getLayoutParams()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mNvsTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();
for (int index = 0; index < clipCount; ++index) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
sequenceDescs.mediaFilePath = videoClip.getFilePath();
sequenceDescs.trimIn = videoClip.getTrimIn();
sequenceDescs.trimOut = videoClip.getTrimOut();
sequenceDescs.inPoint = videoClip.getInPoint();
sequenceDescs.outPoint = videoClip.getOutPoint();
long duration = mNvsTimeline.getDuration();
LinearLayout.LayoutParams layoutParams = (LinearLayout.LayoutParams) mVideoPlay.getLayoutParams();
int halfScreenWidth = ScreenUtils.getScreenWidth() / 2;
mTimelineEditor.setSequencLeftPadding(sequenceLeftPadding);
mTimelineEditor.setSequencRightPadding(halfScreenWidth);
mTimelineEditor.setTimeSpanLeftPadding(sequenceLeftPadding);
```

## `template-mimo-cutsame-043` `addTimeSpan`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:258`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnTrimInChangeListener`, `NvsTimelineTimeSpan.OnTrimOutChangeListener`
Common calls: `getInstance()`, `isPlaying()`, `onPause()`, `setOnChangeListener()`, `setTimeSpanType()`, `addTimeSpan()`, `e()`, `OnTrimInChangeListener()`, `OnTrimOutChangeListener()`, `setOnClickListener()`, `OnClickListener()`

Simple sequence:

```java
private NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {
mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");
final NvsTimelineTimeSpan timelineTimeSpan = mTimelineEditor.addTimeSpan(inPoint, outPoint);
timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {
if (EditorController.getInstance().isPlaying()) {
timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimOutChangeListener() {
if (EditorController.getInstance().isPlaying()) {
timelineTimeSpan.setOnClickListener(new View.OnClickListener() {
if (EditorController.getInstance().isPlaying()) {
```

## `template-mimo-cutsame-044` `seekMultiThumbnailSequenceView`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:321`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `getTimelineCurrentPosition()`, `getDuration()`, `scrollTo()`, `round()`, `getSequenceWidth()`

Simple sequence:

```java
if (mMultiThumbnailSequenceView != null) {
long curPos = NvsStreamingContext.getInstance().getTimelineCurrentPosition(mNvsTimeline);
long duration = mNvsTimeline.getDuration();
mMultiThumbnailSequenceView.scrollTo(Math.round(((float) curPos) / (float) duration * mTimelineEditor.getSequenceWidth()), 0);
```

## `template-mimo-cutsame-045` `seekMultiThumbnailSequenceView`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:322`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `getTimelineCurrentPosition()`, `getDuration()`, `scrollTo()`, `round()`, `getSequenceWidth()`

Simple sequence:

```java
if (mMultiThumbnailSequenceView != null) {
long curPos = NvsStreamingContext.getInstance().getTimelineCurrentPosition(mNvsTimeline);
long duration = mNvsTimeline.getDuration();
mMultiThumbnailSequenceView.scrollTo(Math.round(((float) curPos) / (float) duration * mTimelineEditor.getSequenceWidth()), 0);
```

## `template-mimo-cutsame-046` `playBackEOF`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:331`

API classes: `NvsTimeline`
Common calls: `changePlayButtonState()`, `getDuration()`

Simple sequence:

```java
public void playBackEOF(NvsTimeline timeline) {
if (mBaseVideoFragment != null) {
mBaseVideoFragment.changePlayButtonState(true);
updateCurrentTime(timeline.getDuration());
```

## `template-mimo-cutsame-047` `onSeekingTimelinePosition`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TailorFreeActivity.java:387`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onSeekingTimelinePosition(NvsTimeline timeline, long position) {
```

## `template-mimo-cutsame-048` `onFinishAssetPackageInstallation`

Source: `MCutSame/src/main/java/com/meishe/cutsame/TemplatePreviewActivity.java:342`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo`
Common calls: `size()`, `add()`, `setHasGroup()`, `setGroupIndex()`, `getUseNum()`, `setText()`, `format()`, `sec2Time()`, `getDuration()`, `isEmpty()`, `setDuration()`, `setTrimDuration()`

Simple sequence:

```java
ArrayList<NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo> correspondingClipInfos = footage.correspondingClipInfos;
for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo : correspondingClipInfos) {
.setDuration(clipInfo.outpoint - clipInfo.inpoint)
.setTrimDuration(clipInfo.trimOut - clipInfo.trimIn)
.setInPoint(clipInfo.inpoint)
.setNeedReverse(clipInfo.needReverse)
.setTrackIndex(clipInfo.trackIndex)
.setType(footage.type)
.setHasGroup(hasGroup)
.setGroupIndex(groupIndex)
.setClipIndex(clipInfo.clipIndex)
.setClipIndexInTimelineList(footage.getClipIndexInTimelineList())
.setClipTrackIndexInTimelineList(footage.getClipTrackIndexInTimelineList())
.setFootageId(footage.id));
for (TemplateClip templateClip : mClipList) {
key = templateClip.getFootageId();
for (TemplateClip templateClip : templateClips) {
templateClip.setGroupIndex(groupIndex);
templateClip.setHasGroup(true);
mTemplate.setShotsNumber(mClipList == null ? 0 : mClipList.size());
```

## `template-mimo-cutsame-049` `setLiveWindowRatio`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:133`

API classes: `NvsVideoResolution`
Common calls: `getHeight()`, `getInstance()`, `getNvsTimeline()`, `getVideoRes()`, `getWidth()`, `post()`

Simple sequence:

```java
NvsVideoResolution videoRes = EditorController.getInstance().getNvsTimeline().getVideoRes();
if (mPlayerLayout.getWidth() == 0 && mPlayerLayout.getHeight() == 0) {
setLiveWindowRatio(makeRatio, mPlayerLayout.getHeight(), ratio);
```

## `template-mimo-cutsame-050` `setLiveWindowRatio`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/BaseVideoFragment.java:181`

API classes: `NvsConstants`
Static/constants: `NvsConstants.AspectRatio`

Simple sequence:

```java
if (ratioType == NvsConstants.AspectRatio.AspectRatio_NoFitRatio) {
} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_16v9) { // 16:9
} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_1v1) { //1:1
} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_9v16) { //9:16
} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_3v4) { // 3:4
} else if (ratioType == NvsConstants.AspectRatio.AspectRatio_4v3) { //4:3
```

## `template-mimo-cutsame-051` `getVideoData`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:298`

API classes: `NvsVideoClip`
Common calls: `getRealInpoint()`, `getInstance()`, `setBeforeSelectIndex()`, `seekTimeline()`, `seekPosition()`, `setTemplateType()`, `setOnItemClickListener()`, `OnItemClickListener()`, `setSelectIndex()`, `get()`, `getBeforeSelectIndex()`, `getVideoClipByTemplateFootageCorrespondingClipInfo()`

Simple sequence:

```java
mCutVideoAdapter.setTemplateType(mTemplateType);
mCutVideoAdapter.setOnItemClickListener(new BaseQuickAdapter.OnItemClickListener() {
mCutVideoAdapter.setSelectIndex(position);
int beforeSelectIndex = mCutVideoAdapter.getBeforeSelectIndex();
final NvsVideoClip videoClip = EditorController.getInstance().getVideoClipByTemplateFootageCorrespondingClipInfo(selectedClipInfo);
if (!selectedClipInfo.canReplace) {
mCutVideoAdapter.setBeforeSelectIndex(position);
EditorController.getInstance().seekTimeline(selectedClipInfo.getRealInpoint());
if (mSeekPositionListener != null) {
mSeekPositionListener.seekPosition(selectedClipInfo.getRealInpoint());
EditorController.getInstance().seekTimeline(selectedClipInfo.getRealInpoint());
if (mSeekPositionListener != null) {
mSeekPositionListener.seekPosition(selectedClipInfo.getRealInpoint());
mCutVideoAdapter.setBeforeSelectIndex(position);
mFragmentRecyclerView.setAdapter(mCutVideoAdapter);
mCutVideoAdapter.setNewData(templateClipList);
```

## `template-mimo-cutsame-052` `getVideoData`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:302`

API classes: `NvsVideoClip`
Common calls: `getRealInpoint()`, `getInstance()`, `setBeforeSelectIndex()`, `seekTimeline()`, `seekPosition()`, `setOnItemClickListener()`, `OnItemClickListener()`, `setSelectIndex()`, `get()`, `getBeforeSelectIndex()`, `getVideoClipByTemplateFootageCorrespondingClipInfo()`, `e()`

Simple sequence:

```java
mCutVideoAdapter.setOnItemClickListener(new BaseQuickAdapter.OnItemClickListener() {
mCutVideoAdapter.setSelectIndex(position);
int beforeSelectIndex = mCutVideoAdapter.getBeforeSelectIndex();
final NvsVideoClip videoClip = EditorController.getInstance().getVideoClipByTemplateFootageCorrespondingClipInfo(selectedClipInfo);
if (!selectedClipInfo.canReplace) {
mCutVideoAdapter.setBeforeSelectIndex(position);
EditorController.getInstance().seekTimeline(selectedClipInfo.getRealInpoint());
if (mSeekPositionListener != null) {
mSeekPositionListener.seekPosition(selectedClipInfo.getRealInpoint());
EditorController.getInstance().seekTimeline(selectedClipInfo.getRealInpoint());
if (mSeekPositionListener != null) {
mSeekPositionListener.seekPosition(selectedClipInfo.getRealInpoint());
mCutVideoAdapter.setBeforeSelectIndex(position);
```

## `template-mimo-cutsame-053` `updateVideoData`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/CutEditorVpFragment.java:476`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo`
Common calls: `get()`, `isEmpty()`, `dismiss()`, `size()`, `getInPoint()`, `getOutPoint()`, `getTrimOut()`, `getTrimIn()`, `notifyDataSetChanged()`

Simple sequence:

```java
for (int i = 0; i < mVideoData.size(); i++) {
NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo nvsTemplateFootageCorrespondingClipInfo = mVideoData.get(i);
nvsTemplateFootageCorrespondingClipInfo.inpoint = mTemplateClips.get(i).getInPoint();
nvsTemplateFootageCorrespondingClipInfo.outpoint = mTemplateClips.get(i).getOutPoint();
nvsTemplateFootageCorrespondingClipInfo.trimOut = mTemplateClips.get(i).getTrimOut();
nvsTemplateFootageCorrespondingClipInfo.trimIn = mTemplateClips.get(i).getTrimIn();
```

## `template-mimo-cutsame-054` `setTemplateType`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/adapter/CutVideoAdapter.java:56`

API classes: `NvsVideoClip`
Common calls: `getFilePath()`, `setImageResource()`, `getInstance()`, `getVideoClipByTemplateFootageCorrespondingClipInfo()`, `isEmpty()`, `loadUrl()`

Simple sequence:

```java
NvsVideoClip nvsVideoClip = EditorController.getInstance().getVideoClipByTemplateFootageCorrespondingClipInfo(item);
if (nvsVideoClip != null) {
if (TextUtils.isEmpty(nvsVideoClip.getFilePath())) {
imageView.setImageResource(0);
ImageLoader.loadUrl(mContext, "file://" + nvsVideoClip.getFilePath(), imageView, mRoundCornerOptions);
imageView.setImageResource(0);
```

## `template-mimo-cutsame-055` `getCaptionBitmap`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:112`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.ImageGrabberCallback`
Common calls: `get()`, `getInstance()`, `grabBitmapFromAuxiliaryTimelineAsync()`, `getInPoint()`, `isEmpty()`, `ImageGrabberCallback()`, `runOnUiThread()`, `isIndexAvailable()`, `setBitmap()`, `getCaptionBitmap()`, `size()`

Simple sequence:

```java
EditorController.getInstance().grabBitmapFromAuxiliaryTimelineAsync(captionDescList.get(currentIndex[0]).getInPoint(),
new NvsStreamingContext.ImageGrabberCallback() {
NvsStreamingContext.ImageGrabberCallback callback = this;
if (CommonUtils.isIndexAvailable(currentIndex[0], captionDescList)) {
captionDescList.get(currentIndex[0]).setBitmap(bitmap);
if (getView() != null) {
getView().getCaptionBitmap(currentIndex[0]);
if (currentIndex[0] < captionDescList.size()) {
EditorController.getInstance().grabBitmapFromAuxiliaryTimelineAsync(captionDescList.get(currentIndex[0]).getInPoint(),
```

## `template-mimo-cutsame-056` `changeCaptionText`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:225`

API classes: `NvsTimelineCaption`
Common calls: `setText()`, `getCaptionType()`, `getNvsCaption()`, `getNvsCompoundCaption()`, `getCaptionIndex()`, `equals()`, `getInstance()`, `getCaptionByAttachment()`, `e()`

Simple sequence:

```java
NvsTimelineCaption nvsTimelineCaption = EditorController.getInstance().getCaptionByAttachment(nvsTemplateCaptionDesc.replaceId);
nvsTimelineCaption.setText(text);
if (nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.CLIP_CAPTION ||
nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.TIMELINE_CAPTION) {
nvsTemplateCaptionDesc.getNvsCaption().setText(text);
nvsTemplateCaptionDesc.getNvsCompoundCaption().setText(nvsTemplateCaptionDesc.getCaptionIndex(), text);
if (nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.CLIP_CAPTION ||
nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.TIMELINE_CAPTION) {
nvsTemplateCaptionDesc.getNvsCaption().setText(text);
nvsTemplateCaptionDesc.getNvsCompoundCaption().setText(nvsTemplateCaptionDesc.getCaptionIndex(), text);
```

## `template-mimo-cutsame-057` `changeCaptionText`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:227`

API classes: `NvsTimelineCaption`
Common calls: `setText()`, `getCaptionType()`, `equals()`, `getInstance()`, `getCaptionByAttachment()`, `e()`, `getNvsCaption()`, `getNvsCompoundCaption()`, `getCaptionIndex()`

Simple sequence:

```java
NvsTimelineCaption nvsTimelineCaption = EditorController.getInstance().getCaptionByAttachment(nvsTemplateCaptionDesc.replaceId);
nvsTimelineCaption.setText(text);
if (nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.CLIP_CAPTION ||
nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.TIMELINE_CAPTION) {
nvsTemplateCaptionDesc.getNvsCaption().setText(text);
nvsTemplateCaptionDesc.getNvsCompoundCaption().setText(nvsTemplateCaptionDesc.getCaptionIndex(), text);
```

## `template-mimo-cutsame-058` `seekToCaptionStartTime`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:260`

API classes: `NvsStreamingContext`, `NvsTimelineCaption`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getCaptionType()`, `getInstance()`, `getInPoint()`, `needSeekPosition()`, `seekTimeline()`, `getCaptionByAttachment()`, `e()`

Simple sequence:

```java
if (nvsTemplateCaptionDesc.getCaptionType() == 0) {
NvsTimelineCaption nvsTimelineCaption = EditorController.getInstance().getCaptionByAttachment(nvsTemplateCaptionDesc.replaceId);
EditorController.getInstance().seekTimeline(nvsTimelineCaption.getInPoint(), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (getView() != null) {
getView().needSeekPosition(nvsTimelineCaption.getInPoint(), null);
long inPoint = nvsTemplateCaptionDesc.getInPoint();
EditorController.getInstance().seekTimeline(inPoint, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (getView() != null) {
if (nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.CLIP_CAPTION ||
nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.TIMELINE_CAPTION) {
```

## `template-mimo-cutsame-059` `seekToCaptionStartTime`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:261`

API classes: `NvsStreamingContext`, `NvsTimelineCaption`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getCaptionType()`, `getInstance()`, `getInPoint()`, `needSeekPosition()`, `seekTimeline()`, `getCaptionByAttachment()`, `e()`

Simple sequence:

```java
if (nvsTemplateCaptionDesc.getCaptionType() == 0) {
NvsTimelineCaption nvsTimelineCaption = EditorController.getInstance().getCaptionByAttachment(nvsTemplateCaptionDesc.replaceId);
EditorController.getInstance().seekTimeline(nvsTimelineCaption.getInPoint(), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (getView() != null) {
getView().needSeekPosition(nvsTimelineCaption.getInPoint(), null);
long inPoint = nvsTemplateCaptionDesc.getInPoint();
EditorController.getInstance().seekTimeline(inPoint, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (getView() != null) {
if (nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.CLIP_CAPTION ||
nvsTemplateCaptionDesc.getCaptionType() == TemplateCaptionDesc.TemplateCaptionType.TIMELINE_CAPTION) {
```

## `template-mimo-cutsame-060` `getCaptionPointList`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:291`

API classes: `NvsAssetPackageManager`, `NvsTemplateCaptionDesc`, `NvsTimelineCaption`
Static/constants: `NvsAssetPackageManager.NvsTemplateCaptionDesc`
Common calls: `getInstance()`, `getCaptionByAttachment()`, `getCaptionBoundingVertices()`

Simple sequence:

```java
public List<PointF> getCaptionPointList(NvsAssetPackageManager.NvsTemplateCaptionDesc nvsTemplateCaptionDesc) {
NvsTimelineCaption caption = EditorController.getInstance().getCaptionByAttachment(nvsTemplateCaptionDesc.replaceId);
return caption.getCaptionBoundingVertices(BOUNDING_TYPE_TEXT);
```

## `template-mimo-cutsame-061` `dealVideoReplace`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:308`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getInstance()`, `getInPoint()`, `changeFilePath()`, `getNvsTimeline()`, `getVideoTrackByIndex()`, `getTrackIndex()`, `getClipCount()`, `getClipByIndex()`, `getNeedReverse()`, `getReversePath()`, `getFilePath()`, `seekTimeline()`

Simple sequence:

```java
NvsTimeline nvsTimeline = EditorController.getInstance().getNvsTimeline();
NvsVideoTrack nvsVideoTrack = nvsTimeline.getVideoTrackByIndex(templateClip.getTrackIndex());
if (nvsVideoTrack != null) {
for (int j = 0; j < nvsVideoTrack.getClipCount(); j++) {
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(j);
if (templateClip.getInPoint() == nvsVideoClip.getInPoint()) {
if (templateClip.getNeedReverse()) {
nvsVideoClip.changeFilePath(templateClip.getReversePath());
nvsVideoClip.changeFilePath(templateClip.getFilePath());
EditorController.getInstance().seekTimeline();
```

## `template-mimo-cutsame-062` `dealVideoReplace`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutEditorVpPresenter.java:336`

API classes: `NvsVideoClip`, `NvsTimeline`, `NvsStreamingContext`, `NvsAVFileInfo`
Static/constants: `NvsVideoClip.VIDEO_CLIP_TYPE_AV`
Common calls: `getInstance()`, `getReversePath()`, `changeFilePath()`, `getFilePath()`, `getTrimIn()`, `getNvsTimeline()`, `e()`, `getVideoClipByTemplateFootageCorrespondingClipInfo()`, `getClipIndexInTimelineList()`, `getClipTrackIndexInTimelineList()`, `getTrackIndex()`, `getClipIndex()`

Simple sequence:

```java
NvsTimeline nvsTimeline = EditorController.getInstance().getNvsTimeline();
if (nvsTimeline == null) {
LogUtils.e("timeline is null!");
NvsVideoClip nvsVideoClip = EditorController.getInstance().getVideoClipByTemplateFootageCorrespondingClipInfo(
nvsTimeline, templateClip.getClipIndexInTimelineList(), templateClip.getClipTrackIndexInTimelineList(),
templateClip.getTrackIndex(), templateClip.getClipIndex());
if (templateClip.getMediaType() == MediaData.TYPE_VIDEO && templateClip.getNeedReverse()
&& (!TextUtils.isEmpty(templateClip.getReversePath()))) {
nvsVideoClip.changeFilePath(templateClip.getReversePath());
nvsVideoClip.changeFilePath(templateClip.getFilePath());
if (nvsVideoClip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV && nvsVideoClip.getTrimIn() > 0) {
NvsStreamingContext streamingContext = EditorController.getInstance().getStreamingContext();
if (streamingContext != null) {
NvsAVFileInfo avFileInfo = streamingContext.getAVFileInfo(nvsVideoClip.getFilePath());
nvsVideoClip.moveTrimPoint(-nvsVideoClip.getTrimIn());
EditorController.getInstance().seekTimeline();
```

## `template-mimo-cutsame-063` `createAuxiliaryTimeline`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/CutSameEditorPresenter.java:28`

API classes: `NvsRational`, `NvsAudioResolution`, `NvsTimeline`, `NvsStreamingContext`, `NvsVideoResolution`
Common calls: `createTimeline()`

Simple sequence:

```java
public NvsTimeline createAuxiliaryTimeline(NvsStreamingContext context, NvsVideoResolution nvsVideoResolution) {
nvsVideoResolution.imagePAR = new NvsRational(1, 1);
NvsAudioResolution nvsAudioResolution = new NvsAudioResolution();
return context.createTimeline(nvsVideoResolution, new NvsRational(25, 1), nvsAudioResolution);
```

## `template-mimo-cutsame-064` `getTemplateListByKeyword`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/TemplatePresenter.java:109`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`, `NvsStreamingContext.SdkVersion`
Common calls: `getData()`, `equals()`, `getSdkVersion()`, `getElements()`, `onTemplateListBack()`, `getInstance()`, `getMaterialList()`, `getTemplate()`, `getTotal()`, `onMoreTemplateBack()`

Simple sequence:

```java
NvsStreamingContext instance = NvsStreamingContext.getInstance();
if (instance != null && instance.getSdkVersion() != null) {
NvsStreamingContext.SdkVersion version = instance.getSdkVersion();
CutSameNetApi.getMaterialList(null, assetType, 1, ratio,
if (response != null && response.getData() != null) {
if (response.getData().getElements() != null && getView() != null) {
List<Template> templates = TemplateUtils.getTemplate(response.getData().getElements(), categoryId);
canLoadMore = response.getData().getTotal() > page * PAGE_NUM;
```

## `template-mimo-cutsame-065` `getTemplateListByKeyword`

Source: `MCutSame/src/main/java/com/meishe/cutsame/fragment/presenter/TemplatePresenter.java:112`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.SdkVersion`
Common calls: `getSdkVersion()`

Simple sequence:

```java
if (instance != null && instance.getSdkVersion() != null) {
NvsStreamingContext.SdkVersion version = instance.getSdkVersion();
```

## `template-mimo-cutsame-066` `scanAndFilterAndAnimation`

Source: `MCutSame/src/main/java/com/meishe/cutsame/util/ExportTemplateUtil.java:215`

API classes: `NvsConstants`
Static/constants: `NvsConstants.POST_PACKAGE_ID`
Common calls: `isEmpty()`, `equals()`, `getSubType()`, `getDesc()`, `getInstance()`, `getMeicamVideoTrackList()`, `getClipInfoList()`, `findPropertyFx()`, `getStringVal()`, `getAnimationGroup()`, `getAnimationIn()`, `getAnimationOut()`

Simple sequence:

```java
List<MeicamVideoTrack> meicamVideoTracks = TimelineData.getInstance().getMeicamVideoTrackList();
for (MeicamVideoTrack meicamVideoTrack : meicamVideoTracks) {
List<ClipInfo<?>> clipInfos = meicamVideoTrack.getClipInfoList();
String keyword = meicamVideoFx.getStringVal(NvsConstants.POST_PACKAGE_ID);
String combCaptionAnimation = PathUtils.getAnimationGroup();
String combCaptionAnimation = PathUtils.getAnimationIn();
String combCaptionAnimation = PathUtils.getAnimationOut();
List<MeicamVideoFx> videoFxes = meicamVideoClip.getVideoFxs();
for (MeicamVideoFx videoFx : videoFxes) {
if (MeicamVideoFx.SUB_TYPE_CLIP_FILTER.equals(videoFx.getSubType()) ||
MeicamVideoFx.SUB_TYPE_TIMELINE_FILTER.equals(videoFx.getSubType())) {
String fileName = findFileFromAssets(context, videoFx.getDesc(), "videofx", "filter");
String effectFrameFileFolder = PathUtils.getFilterFolder();
if (findAndCopyFileToSdCard(videoFx.getDesc(), effectFrameFileFolder, destEffectFolderPath, "videofx")) {
```

## `template-mimo-cutsame-067` `scanAndFilterAndAnimation`

Source: `MCutSame/src/main/java/com/meishe/cutsame/util/ExportTemplateUtil.java:217`

API classes: `NvsConstants`
Static/constants: `NvsConstants.POST_PACKAGE_ID`
Common calls: `isEmpty()`, `equals()`, `getSubType()`, `getDesc()`, `getClipInfoList()`, `findPropertyFx()`, `getStringVal()`, `getAnimationGroup()`, `getAnimationIn()`, `getAnimationOut()`, `getVideoFxs()`, `getFilterFolder()`

Simple sequence:

```java
for (MeicamVideoTrack meicamVideoTrack : meicamVideoTracks) {
List<ClipInfo<?>> clipInfos = meicamVideoTrack.getClipInfoList();
String keyword = meicamVideoFx.getStringVal(NvsConstants.POST_PACKAGE_ID);
String combCaptionAnimation = PathUtils.getAnimationGroup();
String combCaptionAnimation = PathUtils.getAnimationIn();
String combCaptionAnimation = PathUtils.getAnimationOut();
List<MeicamVideoFx> videoFxes = meicamVideoClip.getVideoFxs();
for (MeicamVideoFx videoFx : videoFxes) {
if (MeicamVideoFx.SUB_TYPE_CLIP_FILTER.equals(videoFx.getSubType()) ||
MeicamVideoFx.SUB_TYPE_TIMELINE_FILTER.equals(videoFx.getSubType())) {
String fileName = findFileFromAssets(context, videoFx.getDesc(), "videofx", "filter");
String effectFrameFileFolder = PathUtils.getFilterFolder();
if (findAndCopyFileToSdCard(videoFx.getDesc(), effectFrameFileFolder, destEffectFolderPath, "videofx")) {
```

## `template-mimo-cutsame-068` `scanAndFilterAndAnimation`

Source: `MCutSame/src/main/java/com/meishe/cutsame/util/ExportTemplateUtil.java:219`

API classes: `NvsConstants`
Static/constants: `NvsConstants.POST_PACKAGE_ID`
Common calls: `isEmpty()`, `equals()`, `getSubType()`, `getDesc()`, `findPropertyFx()`, `getStringVal()`, `getAnimationGroup()`, `getAnimationIn()`, `getAnimationOut()`, `getVideoFxs()`, `getFilterFolder()`

Simple sequence:

```java
String keyword = meicamVideoFx.getStringVal(NvsConstants.POST_PACKAGE_ID);
String combCaptionAnimation = PathUtils.getAnimationGroup();
String combCaptionAnimation = PathUtils.getAnimationIn();
String combCaptionAnimation = PathUtils.getAnimationOut();
List<MeicamVideoFx> videoFxes = meicamVideoClip.getVideoFxs();
for (MeicamVideoFx videoFx : videoFxes) {
if (MeicamVideoFx.SUB_TYPE_CLIP_FILTER.equals(videoFx.getSubType()) ||
MeicamVideoFx.SUB_TYPE_TIMELINE_FILTER.equals(videoFx.getSubType())) {
String fileName = findFileFromAssets(context, videoFx.getDesc(), "videofx", "filter");
String effectFrameFileFolder = PathUtils.getFilterFolder();
if (findAndCopyFileToSdCard(videoFx.getDesc(), effectFrameFileFolder, destEffectFolderPath, "videofx")) {
```

## `template-mimo-cutsame-069` `scanAndFilterAndAnimation`

Source: `MCutSame/src/main/java/com/meishe/cutsame/util/ExportTemplateUtil.java:220`

API classes: `NvsConstants`
Static/constants: `NvsConstants.POST_PACKAGE_ID`
Common calls: `isEmpty()`, `equals()`, `getSubType()`, `getDesc()`, `findPropertyFx()`, `getStringVal()`, `getAnimationGroup()`, `getAnimationIn()`, `getAnimationOut()`, `getVideoFxs()`, `getFilterFolder()`

Simple sequence:

```java
String keyword = meicamVideoFx.getStringVal(NvsConstants.POST_PACKAGE_ID);
String combCaptionAnimation = PathUtils.getAnimationGroup();
String combCaptionAnimation = PathUtils.getAnimationIn();
String combCaptionAnimation = PathUtils.getAnimationOut();
List<MeicamVideoFx> videoFxes = meicamVideoClip.getVideoFxs();
for (MeicamVideoFx videoFx : videoFxes) {
if (MeicamVideoFx.SUB_TYPE_CLIP_FILTER.equals(videoFx.getSubType()) ||
MeicamVideoFx.SUB_TYPE_TIMELINE_FILTER.equals(videoFx.getSubType())) {
String fileName = findFileFromAssets(context, videoFx.getDesc(), "videofx", "filter");
String effectFrameFileFolder = PathUtils.getFilterFolder();
if (findAndCopyFileToSdCard(videoFx.getDesc(), effectFrameFileFolder, destEffectFolderPath, "videofx")) {
```

## `template-mimo-cutsame-070` `getVideoResolution`

Source: `MCutSame/src/main/java/com/meishe/cutsame/view/ResolutionBottomDialog.java:172`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720`, `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360`, `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480`, `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080`, `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_2160`
Common calls: `getShowData()`, `equals()`, `getResources()`, `getString()`

Simple sequence:

```java
if (itemData.getShowData().equals(mContext.getResources().getString(R.string.compile_int360))) {
return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360;
} else if (itemData.getShowData().equals(mContext.getResources().getString(R.string.compile_int480))) {
return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480;
} else if (itemData.getShowData().equals(mContext.getResources().getString(R.string.compile_int720))) {
return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720;
} else if (itemData.getShowData().equals(mContext.getResources().getString(R.string.compile_int1080))) {
return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080;
} else if (itemData.getShowData().equals(mContext.getResources().getString(R.string.compile_int4K))) {
return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_2160;
return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720;
```

## `template-mimo-cutsame-071` `gifToCafStickerTemplateinstall`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1385`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`
Common calls: `installAssetPackage()`

Simple sequence:

```java
PackageManagerUtil.installAssetPackage(stickerTemplatePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER);
```

## `template-mimo-cutsame-072` `gifToCafStickerTemplateinstall`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1387`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`
Common calls: `installAssetPackage()`

Simple sequence:

```java
PackageManagerUtil.installAssetPackage(stickerTemplatePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER);
```

## `template-mimo-cutsame-073` `resetEngine`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoActivity.java:235`

API classes: `NvsTimeline`
Common calls: `isEmpty()`, `getTimeLine()`, `getCurrentData()`, `getVideoPath()`, `getVideoUrl()`, `getMimoPreviewVideoPath()`, `exists()`, `setVideoPath()`, `put()`, `createTimeline()`, `reBuildSingleVideoTrack()`, `setTimeLine()`

Simple sequence:

```java
mCurrentData = templateListFragment.getCurrentData();
NvsTimeline timeline;
String videoPath = mCurrentData.getVideoPath();
if (TextUtils.isEmpty(videoPath)) {
String videoUrl = mCurrentData.getVideoUrl();
String cachePath = PathUtils.getMimoPreviewVideoPath(MimoActivity.this, videoUrl);
if (cacheVideoFile.exists()) {
mCurrentData.setVideoPath(cachePath);
if (mMimoVideoFragment.getTimeLine() == null) {
timeline = MimoTimelineUtil.createTimeline(videoPath);
timeline = MimoTimelineUtil.reBuildSingleVideoTrack(mMimoVideoFragment.getTimeLine(), videoPath);
mMimoVideoFragment.setTimeLine(timeline);
```

## `template-mimo-cutsame-074` `initEditData`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:189`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`, `NvsTimelineAnimatedSticker`
Static/constants: `NvsStreamingContext.getInstance`, `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`
Common calls: `getInstance()`, `stopEngine()`, `getResources()`, `getString()`, `getDuration()`, `setOnItemClickListener()`, `OnItemClickListener()`, `currentTimeMillis()`, `getSelectedMimoData()`, `getTotalShotVideoInfos()`, `isEmpty()`, `size()`

Simple sequence:

```java
mBottomMenu.setOnItemClickListener(new SelectBottomMenu.OnItemClickListener() {
MiMoLocalData templateInfo = NvMiMoContext.getInstance().getSelectedMimoData();
List<ShotVideoInfo> shotVideoInfos = templateInfo.getTotalShotVideoInfos();
String videoClipPath = shotVideoInfo.getVideoClipPath();
NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(videoClipPath);
if (avFileInfo != null && avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_IMAGE) {
AppManager.getInstance().jumpActivityForResult(MimoEditActivity.this, TrimEditActivity.class, bundle, REQUEST_CODE_VIDEO_TRIM);
mSwitch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
String hint = isChecked ? MimoEditActivity.this.getResources().getString(R.string.hint_open_last_water) :
MimoEditActivity.this.getResources().getString(R.string.hint_close_last_water);
mSwitchHint.setText(hint);
if (mTimeline != null) {
if (!isChecked) {
NvsTimelineAnimatedSticker sticker = mTimeline.getFirstAnimatedSticker();
while (sticker != null) {
if (TextUtils.equals(endingFilter, sticker.getAnimatedStickerPackageId())) {
sticker = mTimeline.removeAnimatedSticker(sticker);
sticker = mTimeline.getNextAnimatedSticker(sticker);
mTimeline.addAnimatedSticker(mTimeline.getDuration() - endingFilterLen, mTimeline.getDuration(), endingFilter);
```

## `template-mimo-cutsame-075` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:190`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`, `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`
Common calls: `getInstance()`, `setOnItemClickListener()`, `OnItemClickListener()`, `currentTimeMillis()`, `getSelectedMimoData()`, `getTotalShotVideoInfos()`, `isEmpty()`, `size()`, `get()`, `getVideoClipPath()`, `getAVFileInfo()`, `getAVFileType()`

Simple sequence:

```java
mBottomMenu.setOnItemClickListener(new SelectBottomMenu.OnItemClickListener() {
MiMoLocalData templateInfo = NvMiMoContext.getInstance().getSelectedMimoData();
List<ShotVideoInfo> shotVideoInfos = templateInfo.getTotalShotVideoInfos();
String videoClipPath = shotVideoInfo.getVideoClipPath();
NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(videoClipPath);
if (avFileInfo != null && avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_IMAGE) {
AppManager.getInstance().jumpActivityForResult(MimoEditActivity.this, TrimEditActivity.class, bundle, REQUEST_CODE_VIDEO_TRIM);
```

## `template-mimo-cutsame-076` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:192`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`, `NvsAVFileInfo.AV_FILE_TYPE_IMAGE`
Common calls: `getInstance()`, `currentTimeMillis()`, `getSelectedMimoData()`, `getTotalShotVideoInfos()`, `isEmpty()`, `size()`, `get()`, `getVideoClipPath()`, `getAVFileInfo()`, `getAVFileType()`, `stopEngine()`, `putInt()`

Simple sequence:

```java
MiMoLocalData templateInfo = NvMiMoContext.getInstance().getSelectedMimoData();
List<ShotVideoInfo> shotVideoInfos = templateInfo.getTotalShotVideoInfos();
String videoClipPath = shotVideoInfo.getVideoClipPath();
NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(videoClipPath);
if (avFileInfo != null && avFileInfo.getAVFileType() == NvsAVFileInfo.AV_FILE_TYPE_IMAGE) {
AppManager.getInstance().jumpActivityForResult(MimoEditActivity.this, TrimEditActivity.class, bundle, REQUEST_CODE_VIDEO_TRIM);
```

## `template-mimo-cutsame-077` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:281`

API classes: `NvsTimeline`, `NvsVideoResolution`
Common calls: `instance()`, `getVideoResolution()`, `newTimeline()`

Simple sequence:

```java
protected NvsTimeline initTimeLine() {
NvsVideoResolution videoResolution = TimelineData.instance().getVideoResolution();
NvsTimeline timeline = MimoTimelineUtil.newTimeline(videoResolution);
if (timeline == null) {
getCurCaption(timeline);
return timeline;
```

## `template-mimo-cutsame-078` `getVideoDuration`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:299`

API classes: `NvsTimeline`
Common calls: `setTimeline()`, `setCompileVideoListener()`, `OnCompileVideoListener()`, `beginTransaction()`, `add()`, `commit()`

Simple sequence:

```java
mCompileVideoFragment.setTimeline(mTimeline);
mCompileVideoFragment.setCompileVideoListener(new CompileVideoFragment.OnCompileVideoListener() {
public void compileProgress(NvsTimeline timeline, int progress) {
public void compileFinished(NvsTimeline timeline) {
public void compileFailed(NvsTimeline timeline) {
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
```

## `template-mimo-cutsame-079` `initCompileVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:302`

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

## `template-mimo-cutsame-080` `initCompileVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:304`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileProgress(NvsTimeline timeline, int progress) {
```

## `template-mimo-cutsame-081` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:308`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
```

## `template-mimo-cutsame-082` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:313`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
```

## `template-mimo-cutsame-083` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:318`

API classes: `NvsTimeline`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
```

## `template-mimo-cutsame-084` `selectCaptionAndTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:350`

API classes: `NvsTimelineCompoundCaption`
Common calls: `get()`, `getZValue()`, `getTimelineCurrentPosition()`, `getCompoundCaptionsByTimelinePosition()`, `size()`

Simple sequence:

```java
if (mTimeline == null) {
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsTimelineCompoundCaption> captionList = mTimeline.getCompoundCaptionsByTimelinePosition(curPos);
if (captionCount > 0) {
float zVal = captionList.get(0).getZValue();
for (int i = 0; i < captionCount; i++) {
float tmpZVal = captionList.get(i).getZValue();
```

## `template-mimo-cutsame-085` `getCurCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoEditActivity.java:388`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `onDestroy()`, `getInstance()`, `clearCachedResources()`

Simple sequence:

```java
NvsStreamingContext context = NvsStreamingContext.getInstance();
```

## `template-mimo-cutsame-086` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:128`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `onPlayStateChanged()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mTimeline == null) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
```

## `template-mimo-cutsame-087` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:129`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `onPlayStateChanged()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mTimeline == null) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
```

## `template-mimo-cutsame-088` `setOnSeekBarChangeListener`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:152`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`

Simple sequence:

```java
seekTimeline(currentTime, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
```

## `template-mimo-cutsame-089` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:230`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`
Common calls: `setPlaybackCallback()`, `PlaybackCallback()`, `sendEmptyMessage()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `template-mimo-cutsame-090` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:232`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
```

## `template-mimo-cutsame-091` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:237`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `template-mimo-cutsame-092` `onPlaybackStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:241`

API classes: `NvsTimeline`
Common calls: `sendEmptyMessage()`

Simple sequence:

```java
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
```

## `template-mimo-cutsame-093` `onPlaybackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:246`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.PlaybackCallback2`
Common calls: `setPlaybackCallback2()`, `PlaybackCallback2()`, `onPlayProgressChanged()`

Simple sequence:

```java
mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {
```

## `template-mimo-cutsame-094` `onDetach`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:348`

API classes: `NvsTimeline`

Simple sequence:

```java
public void setTimeLine(NvsTimeline timeline) {
mTimeline = timeline;
```

## `template-mimo-cutsame-095` `playVideoButtonClick`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:364`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `template-mimo-cutsame-096` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:368`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
mStreamingContext.playbackTimeline(mTimeline, mStartTime, mStartTime + getDuration(), NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `template-mimo-cutsame-097` `playVideoFromStartPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:372`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `seekTimeline()`

Simple sequence:

```java
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);
```

## `template-mimo-cutsame-098` `initDrawRectListener`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:396`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getTimelineCurrentPosition()`, `mapViewToCanonical()`, `translateCaption()`, `setupInputCacheForCaption()`, `translateAnimatedSticker()`, `getDrawRect()`, `onAssetTranstion()`

Simple sequence:

```java
PointF pre = mLiveWindow.mapViewToCanonical(prePointF);
PointF p = mLiveWindow.mapViewToCanonical(nowPointF);
if (mCurCaption != null) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
updateWaterMarkPositionOnDrag(timeLinePointF.x, timeLinePointF.y, mDrawRect.getDrawRect());
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `template-mimo-cutsame-099` `onAlignClick`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:507`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsTimelineCaption.TEXT_ALIGNMENT_LEFT`, `NvsTimelineCaption.TEXT_ALIGNMENT_CENTER`, `NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setTextAlignment()`, `getTextAlignment()`, `getTimelineCurrentPosition()`, `onAssetAlign()`

Simple sequence:

```java
switch (mCurCaption.getTextAlignment()) {
case NvsTimelineCaption.TEXT_ALIGNMENT_LEFT:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_CENTER);
case NvsTimelineCaption.TEXT_ALIGNMENT_CENTER:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT);
case NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_LEFT);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (mAssetEditListener != null) {
mAssetEditListener.onAssetAlign(mCurCaption.getTextAlignment());
```

## `template-mimo-cutsame-100` `onAlignClick`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:508`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.TEXT_ALIGNMENT_LEFT`, `NvsTimelineCaption.TEXT_ALIGNMENT_CENTER`, `NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT`
Common calls: `setTextAlignment()`, `getTextAlignment()`

Simple sequence:

```java
switch (mCurCaption.getTextAlignment()) {
case NvsTimelineCaption.TEXT_ALIGNMENT_LEFT:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_CENTER);
case NvsTimelineCaption.TEXT_ALIGNMENT_CENTER:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT);
case NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_LEFT);
```

## `template-mimo-cutsame-101` `onHorizFlipClick`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:531`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getHorizontalFlip()`, `setHorizontalFlip()`, `getTimelineCurrentPosition()`, `onAssetHorizFlip()`

Simple sequence:

```java
boolean isHorizFlip = !mCurAnimateSticker.getHorizontalFlip();
mCurAnimateSticker.setHorizontalFlip(isHorizFlip);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `template-mimo-cutsame-102` `onHorizFlipClick`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:532`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getHorizontalFlip()`, `setHorizontalFlip()`, `getTimelineCurrentPosition()`, `onAssetHorizFlip()`

Simple sequence:

```java
boolean isHorizFlip = !mCurAnimateSticker.getHorizontalFlip();
mCurAnimateSticker.setHorizontalFlip(isHorizFlip);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `template-mimo-cutsame-103` `setStickerMuteIndex`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:624`

API classes: `NvsTimelineAnimatedSticker`

Simple sequence:

```java
public NvsTimelineAnimatedSticker getCurAnimateSticker() {
```

## `template-mimo-cutsame-104` `setAlignIndex`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:698`

API classes: `NvsTimelineCaption`

Simple sequence:

```java
public void setCurCaption(NvsTimelineCaption caption) {
```

## `template-mimo-cutsame-105` `setCurCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:702`

API classes: `NvsTimelineCaption`

Simple sequence:

```java
public NvsTimelineCaption getCurCaption() {
```

## `template-mimo-cutsame-106` `getCurCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:706`

API classes: `NvsTimelineCompoundCaption`

Simple sequence:

```java
public void setCurCompoundCaption(NvsTimelineCompoundCaption caption) {
```

## `template-mimo-cutsame-107` `setCurCompoundCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:710`

API classes: `NvsTimelineCompoundCaption`

Simple sequence:

```java
public NvsTimelineCompoundCaption getCurrCompoundCaption() {
```

## `template-mimo-cutsame-108` `curPointIsInnerDrawRect`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:749`

API classes: `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`
Common calls: `size()`, `getCompoundCaptionsByTimelinePosition()`, `getTimelineCurrentPosition()`, `get()`, `getCompoundBoundingVertices()`, `clickPointIsInnerDrawRect()`, `setDrawRectVisible()`, `setDrawRect()`

Simple sequence:

```java
if (mTimeline == null) {
List<NvsTimelineCompoundCaption> captionList = mTimeline.getCompoundCaptionsByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));
for (int j = 0; j < captionList.size(); j++) {
NvsTimelineCompoundCaption caption = captionList.get(j);
List<PointF> list = caption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);
if (isSelected) {
mDrawRect.setDrawRectVisible(true);
mDrawRect.setDrawRect(newList, Constants.EDIT_MODE_COMPOUND_CAPTION);
```

## `template-mimo-cutsame-109` `isDrawRectVisible`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/MimoVideoFragment.java:823`

API classes: `NvsTimeline`

Simple sequence:

```java
public NvsTimeline getTimeLine() {
return mTimeline;
```

## `template-mimo-cutsame-110` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:97`

API classes: `NvsTimelineEditor`
Common calls: `getExtras()`, `getInt()`, `getBoolean()`, `setOnTouchListener()`, `OnTouchListener()`

Simple sequence:

```java
if (intent != null) {
Bundle extras = intent.getExtras();
if (extras != null) {
mSelectPosition = extras.getInt(Constants.IntentKey.INTENT_KEY_SHOT_ID);
mIsFromResult = extras.getBoolean(INTENT_KEY_FROM_WHAT, true);
mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.timeline_editor);
mWaitLayout.setOnTouchListener(new View.OnTouchListener() {
```

## `template-mimo-cutsame-111` `convertVideoFile`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:255`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.MeidaFileConvertorCallback`, `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR`
Common calls: `setMeidaFileConvertorCallback()`, `MeidaFileConvertorCallback()`, `d()`, `currentThread()`, `setConverClipPath()`, `setVisibility()`, `getInstance()`, `finishActivity()`, `putExtra()`

Simple sequence:

```java
mFileConvertor.setMeidaFileConvertorCallback(new NvsMediaFileConvertor.MeidaFileConvertorCallback() {
if (errorCode == NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR) {
mSelectShotVideoInfo.setConverClipPath(s1);
mWaitLayout.setVisibility(View.GONE);
```

## `template-mimo-cutsame-112` `onProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:262`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR`
Common calls: `d()`, `currentThread()`, `setConverClipPath()`, `setVisibility()`, `getInstance()`, `finishActivity()`, `putExtra()`

Simple sequence:

```java
if (errorCode == NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR) {
mSelectShotVideoInfo.setConverClipPath(s1);
mWaitLayout.setVisibility(View.GONE);
```

## `template-mimo-cutsame-113` `onFinish`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/TrimEditActivity.java:264`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR`
Common calls: `setConverClipPath()`

Simple sequence:

```java
if (errorCode == NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR) {
mSelectShotVideoInfo.setConverClipPath(s1);
```

## `template-mimo-cutsame-114` `onStop`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java:49`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.class`, `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `initStreamingContext()`

Simple sequence:

```java
public NvsStreamingContext getStreamingContext() {
if (mStreamingContext == null) {
synchronized (NvsStreamingContext.class) {
if (mStreamingContext == null) {
mStreamingContext = NvsStreamingContext.getInstance();
if (mStreamingContext == null) {
mStreamingContext = TimelineUtil.initStreamingContext(getApplicationContext(), licensePath);
return mStreamingContext;
```

## `template-mimo-cutsame-115` `onStop`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java:50`

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

## `template-mimo-cutsame-116` `getStreamingContext`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/base/BaseActivity.java:52`

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

## `template-mimo-cutsame-117` `setMakeRatio`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:103`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public void setVideoResolution(NvsVideoResolution resolution) {
```

## `template-mimo-cutsame-118` `setVideoResolution`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:107`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public NvsVideoResolution getVideoResolution() {
```

## `template-mimo-cutsame-119` `getVideoResolution`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:111`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public NvsVideoResolution cloneVideoResolution() {
NvsVideoResolution resolution = new NvsVideoResolution();
```

## `template-mimo-cutsame-120` `setRecordAudioData`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/dataInfo/TimelineData.java:329`

API classes: `NvsVideoResolution`

Simple sequence:

```java
m_videoResolution = new NvsVideoResolution();
```

## `template-mimo-cutsame-121` `saveCompoundCaptionData`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/CaptionUtil.java:16`

API classes: `NvsTimelineCompoundCaption`
Common calls: `clone()`, `getInPoint()`, `setInPoint()`, `getOutPoint()`, `setOutPoint()`, `getCaptionCount()`, `CompoundCaptionAttr()`, `setCaptionFontName()`, `getCaptionFontName()`, `setCaptionText()`, `getText()`, `addCaptionAttributeList()`

Simple sequence:

```java
public static CompoundCaptionInfo saveCompoundCaptionData(NvsTimelineCompoundCaption caption, CompoundCaptionInfo compoundCaptionInfo) {
long inPoint = caption.getInPoint();
captionInfo.setInPoint(inPoint);
long outPoint = caption.getOutPoint();
captionInfo.setOutPoint(outPoint);
int captionCount = caption.getCaptionCount();
compoundCaptionAttr.setCaptionFontName(compoundCaptionInfo.getCaptionFontName());
compoundCaptionAttr.setCaptionText(caption.getText(idx));
captionInfo.setCaptionZVal((int) caption.getZValue());
captionInfo.setAnchor(caption.getAnchorPoint());
PointF pointF = caption.getCaptionTranslation();
captionInfo.setTranslation(pointF);
```

## `template-mimo-cutsame-122` `createTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:69`

API classes: `NvsTimeline`
Common calls: `instance()`, `appendAudioTrack()`, `getClipInfoData()`, `isEmpty()`, `getVideoResolution()`, `e()`

Simple sequence:

```java
public static NvsTimeline createTimeline() {
ArrayList<ClipInfo> clipInfoData = TimelineData.instance().getClipInfoData();
NvsTimeline timeline = newTimeline(TimelineData.instance().getVideoResolution());
if (timeline == null) {
Log.e(TAG, "failed to create timeline");
if (!buildVideoTrack(timeline)) {
return timeline;
timeline.appendAudioTrack(); // 音乐轨道 Musical track
setTimelineData(timeline);
return timeline;
```

## `template-mimo-cutsame-123` `createTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:104`

API classes: `NvsTimeline`
Common calls: `getVideoEditResolution()`, `e()`

Simple sequence:

```java
public static NvsTimeline createTimeline(String clipPath) {
NvsTimeline timeline = newTimeline(MimoCommonUtil.getVideoEditResolution(Constants.AspectRatio.AspectRatio_16v9));
if (timeline == null) {
Log.e(TAG, "failed to create timeline");
if (!buildSingleClipVideoTrackExt(timeline, clipPath)) {
return timeline;
```

## `template-mimo-cutsame-124` `rebuildTimelineByTemplate`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:122`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `clearCachedResources()`, `getSelectedMimoData()`

Simple sequence:

```java
public static void rebuildTimelineByTemplate(NvsTimeline timeline) {
if (timeline == null) {
NvsStreamingContext context = NvsStreamingContext.getInstance();
removeAllTimelineAsset(timeline);
removeVideoTrack(timeline);
removeAudioTrack(timeline);
MiMoLocalData selectTemplate = NvMiMoContext.getInstance().getSelectedMimoData();
addShotVideo(timeline, selectTemplate);
```

## `template-mimo-cutsame-125` `addShotVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:179`

API classes: `NvsVideoTrack`, `NvsTimeline`
Common calls: `isEmpty()`, `getVideoTrackByIndex()`, `size()`, `get()`, `appendVideoTrack()`, `setVolumeGain()`, `getTrackClipInfos()`, `addAll()`, `getFilter()`, `getShotDataInfos()`, `getMainTrackVideoInfo()`, `getShot()`

Simple sequence:

```java
private static void addShotVideo(NvsTimeline timeline, MiMoLocalData selectTemplate) {
List<ShotDataInfo> shotDataInfos = selectTemplate.getShotDataInfos();
NvsVideoTrack mainVideoTrack = timeline.getVideoTrackByIndex(0);
if (mainVideoTrack == null) {
mainVideoTrack = timeline.appendVideoTrack();
mainVideoTrack.setVolumeGain(0f, 0f);
ShotVideoInfo mainTrackVideoInfo = shotDataInfo.getMainTrackVideoInfo();
List<TrackClipInfo> mainTrackClipInfos = mainTrackVideoInfo.getTrackClipInfos();
int shot = mainTrackVideoInfo.getShot();
String videoFilePath = mainTrackVideoInfo.getVideoClipPath();
String converFilePath = mainTrackVideoInfo.getConverClipPath();
long timelineDuration = timeline.getDuration();
trackClipInfo.setDurationRatio(durationRatio);
if (!TextUtils.isEmpty(mainTrackVideoInfo.getFilter()) && clipCount > 1) {
appendTimelineFilter(timeline, timelineDuration, mainTrackVideoInfo.getFilter());
List<ShotVideoInfo> subTrackVideoInfos = shotDataInfo.getSubTrackVideoInfos();
int trackIndex = subShotVideoInfo.getTrackIndex();
NvsVideoTrack subVideoTrack = timeline.getVideoTrackByIndex(trackIndex);
if (subVideoTrack == null) {
subVideoTrack = timeline.appendVideoTrack();
subVideoTrack.setVolumeGain(0f, 0f);
List<TrackClipInfo> subTrackClips = subShotVideoInfo.getTrackClipInfos();
appendAudioClip(timeline, selectTemplate);
NvsVideoTrack subVideoTrack = timeline.getVideoTrackByIndex(1);
// ... 1 more SDK-related lines omitted in this compressed snippet ...
```

## `template-mimo-cutsame-126` `appendAudioClip`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:420`

API classes: `NvsTimeline`, `NvsAudioTrack`
Common calls: `getMusicFilePath()`, `isEmpty()`, `millisecondToMicrosecond()`, `getMusicDuration()`, `getAudioTrackByIndex()`, `appendAudioTrack()`, `appendClip()`

Simple sequence:

```java
private static void appendAudioClip(NvsTimeline timeline, MiMoLocalData selectTemplate) {
if (timeline == null) {
String musicFilePath = selectTemplate.getMusicFilePath();
long musicDuration = MiMoFileUtils.millisecondToMicrosecond(selectTemplate.getMusicDuration());
NvsAudioTrack mainAudioTrack = timeline.getAudioTrackByIndex(0);
if (mainAudioTrack == null) {
mainAudioTrack = timeline.appendAudioTrack();
mainAudioTrack.appendClip(musicFilePath, 0, musicDuration);
```

## `template-mimo-cutsame-127` `setTrackTransition`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:443`

API classes: `NvsVideoTrack`, `NvsVideoTransition`
Common calls: `isEmpty()`, `getClipCount()`, `setBuiltinTransition()`, `setPackagedTransition()`, `size()`, `d()`, `get()`, `getTrans()`, `getTransitionBySourceClipIndex()`, `enableTimelineTransition()`

Simple sequence:

```java
private static void setTrackTransition(NvsVideoTrack videoTrack, List<TrackClipInfo> trackClipInfos) {
int trackClipCount = videoTrack.getClipCount();
videoTrack.setBuiltinTransition(index, null);
videoTrack.setPackagedTransition(index, null);
String transitionName = videoClipInfo.getTrans();
if (isBuiltInTransition) {
videoTrack.setBuiltinTransition(index, transitionName);
videoTrack.setPackagedTransition(index, transitionName);
int clipCount = videoTrack.getClipCount();
for (int index = 0; index < clipCount; index++) {
NvsVideoTransition videoTransition = videoTrack.getTransitionBySourceClipIndex(index);
```

## `template-mimo-cutsame-128` `appendVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:540`

API classes: `NvsVideoClip`
Static/constants: `NvsVideoClip.VIDEO_CLIP_TYPE_AV`
Common calls: `d()`, `isEmpty()`, `getTrimIn()`, `getRealNeedDuration()`, `getDurationRatio()`, `addClip()`, `appendClip()`, `getVideoType()`, `setPanAndScan()`, `getTrackFilter()`, `getFilter()`, `getInPoint()`

Simple sequence:

```java
long clipTrimIn = trackClipInfo.getTrimIn();
long realNeedDuration = trackClipInfo.getRealNeedDuration();
float durationRatio = trackClipInfo.getDurationRatio();
NvsVideoClip videoClip = (inPoint > 0)
: videoTrack.appendClip(videoFilePath, clipTrimIn, clipTrimOut);
int videoType = videoClip.getVideoType();
if (videoType == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {
videoClip.setPanAndScan(0f, 1f);
String trackFilter = trackClipInfo.getTrackFilter();
if (!timelineFilterFlag) {
String filter = trackClipInfo.getFilter();
return videoClip.getInPoint();
```

## `template-mimo-cutsame-129` `changeSpeed`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:608`

API classes: `NvsVideoClip`
Common calls: `getSpeed0()`, `getSpeed1()`, `getDurationRatio()`, `changeSpeed()`, `changeVariableSpeed()`

Simple sequence:

```java
private static void changeSpeed(NvsVideoClip videoClip, TrackClipInfo trackClipInfo) {
float speed0 = trackClipInfo.getSpeed0();
float speed1 = trackClipInfo.getSpeed1();
float durationRatio = trackClipInfo.getDurationRatio();
videoClip.changeSpeed(speed0);
videoClip.changeVariableSpeed(speed0, speed1, true);
```

## `template-mimo-cutsame-130` `createSingleClipTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:672`

API classes: `NvsTimeline`
Common calls: `getVideoEditResolution()`, `e()`

Simple sequence:

```java
public static NvsTimeline createSingleClipTimeline(ClipInfo clipInfo, boolean isTrimClip) {
NvsTimeline timeline = newTimeline(MimoCommonUtil.getVideoEditResolution(Constants.AspectRatio.AspectRatio_16v9));
if (timeline == null) {
Log.e(TAG, "failed to create timeline");
buildSingleClipVideoTrack(timeline, clipInfo, isTrimClip);
return timeline;
```

## `template-mimo-cutsame-131` `reBuildSingleVideoTrack`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:799`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `e()`, `videoTrackCount()`, `appendVideoTrack()`, `getVideoTrackByIndex()`, `removeAllClips()`, `appendClip()`

Simple sequence:

```java
public static NvsTimeline reBuildSingleVideoTrack(NvsTimeline timeline, String clipPath) {
if (timeline == null) {
int videoTrackCount = timeline.videoTrackCount();
NvsVideoTrack videoTrack = videoTrackCount == 0 ? timeline.appendVideoTrack() : timeline.getVideoTrackByIndex(0);
videoTrack.removeAllClips();
NvsVideoClip videoClip = videoTrack.appendClip(clipPath);
return timeline;
```

## `template-mimo-cutsame-132` `buildTimelineRecordAudio`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/MimoTimelineUtil.java:1119`

API classes: `NvsAudioClip`
Common calls: `getFxID()`, `getInPoint()`, `getTrimIn()`, `setVolumeGain()`, `getVolume()`, `removeAllClips()`, `size()`, `get()`, `addClip()`, `getPath()`, `getOutPoint()`, `equals()`

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
float audioVolume = TimelineData.instance().getRecordVolume();
audioTrack.setVolumeGain(audioVolume, audioVolume);
```

## `template-mimo-cutsame-133` `getPackageType`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:156`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`

Simple sequence:

```java
if (assetType == NvAsset.ASSET_THEME) {
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;
```

## `template-mimo-cutsame-134` `getPackageType`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAsset.java:157`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`

Simple sequence:

```java
if (assetType == NvAsset.ASSET_THEME) {
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;
```

## `template-mimo-cutsame-135` `onDestroy`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/utils/asset/NvAssetManager.java:194`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `sharedInstance()`, `getInstance()`, `getSharedPreferences()`, `getAssetPackageManager()`, `setCallbackInterface()`

Simple sequence:

```java
streamingContext = NvsStreamingContext.getInstance();
preferences = context.getSharedPreferences(assetdata, Context.MODE_PRIVATE);
packageManager = streamingContext.getAssetPackageManager();
packageManager.setCallbackInterface(this);
```

## `template-mimo-cutsame-136` `setOnScrollListener`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:94`

API classes: `NvsTimelineEditor`, `NvsMultiThumbnailSequenceView`
Common calls: `setOrientation()`

Simple sequence:

```java
public NvsTimelineEditor(Context context, AttributeSet attrs) {
m_sequenceLinearLayout.setOrientation(LinearLayout.HORIZONTAL);
m_multiThumbnailSequenceView = new NvsMultiThumbnailSequenceView(context);
```

## `template-mimo-cutsame-137` `initTimelineEditor`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:134`

API classes: `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt`, `NvsTimelineTimeSpan`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`, `NvsMultiThumbnailSequenceView.OnScrollChangeListener`
Common calls: `size()`, `scrollTo()`, `addView()`, `mapTimelinePosFromX()`, `getParent()`, `setThumbnailSequenceDescArray()`, `setPixelPerMicrosecond()`, `setStartPadding()`, `setEndPadding()`, `setOnScrollChangeListenser()`, `OnScrollChangeListener()`, `compareTo()`

Simple sequence:

```java
public void initTimelineEditor(ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDesc, final long timelineDuration, final long trimInPoint) {
m_multiThumbnailSequenceView.setThumbnailSequenceDescArray(sequenceDesc);
m_multiThumbnailSequenceView.setPixelPerMicrosecond(m_pixelPerMicrosecond);
m_multiThumbnailSequenceView.setStartPadding(m_sequencLeftPadding);
m_multiThumbnailSequenceView.setEndPadding(m_sequencRightPadding);
m_multiThumbnailSequenceView.setOnScrollChangeListenser(new NvsMultiThumbnailSequenceView.OnScrollChangeListener() {
public void onScrollChanged(NvsMultiThumbnailSequenceView nvsMultiThumbnailSequenceView, int i, int i1) {
if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") == 0)
NvsTimelineTimeSpan timeSpan = m_timelineTimeSpanArray.get(index);
long inPoint = timeSpan.getInPoint();
long outPoint = timeSpan.getOutPoint();
if (add) {
if (timeSpan.getParent() == null) {
if (timeSpan.getParent() != null) {
m_timeSpanRelativeLayout.removeView(timeSpan);
```

## `template-mimo-cutsame-138` `addTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:200`

API classes: `NvsTimelineTimeSpan`
Common calls: `floor()`, `setMinTimeSpanPixel()`, `setMaxTimeSpanPixel()`

Simple sequence:

```java
public NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {
NvsTimelineTimeSpan timelineTimeSpan = createTimeSpan(inPoint, outPoint);
timelineTimeSpan.setMinTimeSpanPixel(minTimeSpanPixel);
timelineTimeSpan.setMaxTimeSpanPixel(maxTimeSpanPixel);
```

## `template-mimo-cutsame-139` `addTimeSpanExt`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:221`

API classes: `NvsTimelineTimeSpanExt`
Static/constants: `NvsTimelineTimeSpanExt.OnMarginChangeListener`
Common calls: `setMargins()`, `setLayoutParams()`, `addView()`, `floor()`, `setBackgroundColor()`, `addRule()`, `getLayoutParams()`, `compareTo()`, `setMultiThumbnailSequenceView()`, `setInPoint()`, `setOutPoint()`, `setPixelPerMicrosecond()`

Simple sequence:

```java
public NvsTimelineTimeSpanExt addTimeSpanExt(long inPoint, long outPoint) {
if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") != 0)
NvsTimelineTimeSpanExt timeSpanExt = new NvsTimelineTimeSpanExt(m_context);
timeSpanExt.setMultiThumbnailSequenceView(m_multiThumbnailSequenceView);
timeSpanExt.setInPoint(inPoint);
timeSpanExt.setOutPoint(outPoint);
timeSpanExt.setPixelPerMicrosecond(m_pixelPerMicrosecond);
int lLeftHandleWidth = timeSpanExt.getLLeftHandleWidth();
timeSpanExt.setTotalWidth(totalWidth);
spanItemParams.setMargins(leftMargin, LayoutParams.MATCH_PARENT, totalWidth - (leftMargin + spanWidth), 0);
timeSpanExt.setLayoutParams(spanItemParams);
viewLeftMargin.setBackgroundColor(backgrdColor);
int tmpMarginHeight = timeSpanExt.getLTopHandleHeight();
viewLeftMarginParams.setMargins(tmpLLeftHandleWidth, 0, tmpTotalWidth - tmpLLeftHandleWidth - leftMargin, 0);
viewRightMargin.setBackgroundColor(backgrdColor);
viewRightMarginParams.setMargins(leftMargin + spanWidth - lLeftHandleWidth, 0, lLeftHandleWidth, 0);
timeSpanExt.setMarginChangeListener(new NvsTimelineTimeSpanExt.OnMarginChangeListener() {
LayoutParams viewLeftMarginParams = (LayoutParams) viewLeftMargin.getLayoutParams();
viewLeftMarginParams.setMargins(tmpLLeftHandleWidth, 0, tmpTotalWidth - leftMargin, 0);
viewLeftMargin.setLayoutParams(viewLeftMarginParams);
LayoutParams viewRightMarginParams = (LayoutParams) viewRightMargin.getLayoutParams();
viewRightMarginParams.setMargins(leftMargin + timeSpanWidth, 0, tmpLLeftHandleWidth, 0);
viewRightMargin.setLayoutParams(viewRightMarginParams);
```

## `template-mimo-cutsame-140` `selectTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:392`

API classes: `NvsTimelineTimeSpan`
Common calls: `setHasSelected()`, `requestLayout()`, `bringToFront()`

Simple sequence:

```java
public void selectTimeSpan(NvsTimelineTimeSpan timeSpan) {
timeSpan.setHasSelected(true);
```

## `template-mimo-cutsame-141` `getSequenceWidth`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:403`

API classes: `NvsMultiThumbnailSequenceView`

Simple sequence:

```java
public NvsMultiThumbnailSequenceView getMultiThumbnailSequenceView() {
```

## `template-mimo-cutsame-142` `timeSpanCount`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineEditor.java:411`

API classes: `NvsTimelineTimeSpan`
Common calls: `getChildCount()`, `removeView()`, `remove()`

Simple sequence:

```java
public void deleteSelectedTimeSpan(NvsTimelineTimeSpan timeSpan) {
int count = m_timeSpanRelativeLayout.getChildCount();
if (count > 0) {
m_timeSpanRelativeLayout.removeView(timeSpan);
```

## `template-mimo-cutsame-143` `getRightHandleView`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/common/view/timelineEditor/NvsTimelineTimeSpan.java:73`

API classes: `NvsTimelineTimeSpan`
Common calls: `findViewById()`, `from()`, `inflate()`, `getLayoutParams()`

Simple sequence:

```java
public NvsTimelineTimeSpan(Context context) {
mHandleWidth = leftHandleView.getLayoutParams().width;
```

## `template-mimo-cutsame-144` `onProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/SelectMediaActivity.java:447`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR`
Common calls: `d()`, `currentThread()`, `get()`, `setConverClipPath()`, `size()`

Simple sequence:

```java
if (errorCode == NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR) {
mShotVideoInfos.get(mShotVideoIndex).setConverClipPath(s1);
```

## `template-mimo-cutsame-145` `onFinish`

Source: `app/src/main/java/com/meishe/sdkdemo/mimodemo/mediapaker/SelectMediaActivity.java:449`

API classes: `NvsMediaFileConvertor`
Static/constants: `NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR`
Common calls: `get()`, `setConverClipPath()`

Simple sequence:

```java
if (errorCode == NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR) {
mShotVideoInfos.get(mShotVideoIndex).setConverClipPath(s1);
```

## `template-mimo-cutsame-146` `applyVideoFxTemplate`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:910`

API classes: `NvsVideoFx`
Common calls: `get()`, `size()`, `appendPackagedFx()`, `getTempatePackageID()`, `e()`

Simple sequence:

```java
if (mPiPTemplateAssetsArray != null && index >= 0 && index < mPiPTemplateAssetsArray.size()) {
NvsVideoFx secondVideoFx = firstClip.appendPackagedFx(mPiPTemplateAssetsArray.get(index).getTempatePackageID().get(0));
```

## `template-mimo-cutsame-147` `addMusicInfoData`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:783`

API classes: `NvsAVFileInfo`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `isBuildInTemp()`, `getTemplateAssetsFilePath()`, `getFolderPath()`, `getMusic()`, `getInstance()`, `setFilePath()`, `setIsAsset()`, `setAssetPath()`, `setTrimIn()`, `setInPoint()`, `getNeedControlMusicFading()`, `setFadeDuration()`

Simple sequence:

```java
musicInfo.setFilePath(
MiMoFileUtils.getTemplateAssetsFilePath(mThemeModel.getFolderPath(), mThemeModel.getMusic(), mThemeModel.isBuildInTemp()));
musicInfo.setIsAsset(mThemeModel.isBuildInTemp());
musicInfo.setAssetPath(MiMoFileUtils.getTemplateAssetsFilePath(mThemeModel.getFolderPath(), mThemeModel.getMusic(), !mThemeModel.isBuildInTemp()));
musicInfo.setTrimIn(0);
musicInfo.setInPoint(0);
if (mThemeModel.getNeedControlMusicFading() == 1) {
musicInfo.setFadeDuration(mThemeModel.getMusicFadingTime() * Constants.US_TIME_BASE);
NvsAVFileInfo avFileInfo = NvsStreamingContext.getInstance().getAVFileInfo(
MiMoFileUtils.getTemplateAssetsFilePath(mThemeModel.getFolderPath(),
mThemeModel.getMusic(),
if (avFileInfo != null) {
musicInfo.setTrimOut(mThemeModel.getMusicDuration() * Constants.US_TIME_BASE);
AudioPlayer.getInstance(ThemeCaptureActivity.this).setCurrentMusic(musicInfo, false);
TimelineData.instance().setMusicList(musicInfos);
```

## `template-mimo-cutsame-148` `getTemplateAspectRatio`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1022`

API classes: `NvsVideoResolution`
Common calls: `getInstance()`, `getVideoResolution()`, `getTemplateAspect()`

Simple sequence:

```java
NvsVideoResolution videoResolution = TimelineData.getInstance().getVideoResolution();
return CommonData.AspectRatio.getTemplateAspect(ratio);
```

## `template-mimo-cutsame-149` `setRealInpoint`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageCorrespondingClipInfo.java:77`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo`

Simple sequence:

```java
public void setNvsTemplateFootageCorrespondingClipInfo(NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo correspondingClipInfo) {
```

## `template-mimo-cutsame-150` `setClipIndexInTimelineList`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/MeicamNvsTemplateFootageDesc.java:44`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageDesc`

Simple sequence:

```java
public void setNvsTemplateFootageDesc(NvsAssetPackageManager.NvsTemplateFootageDesc desc) {
```

## `template-mimo-cutsame-151` `getCaptionType`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:81`

API classes: `NvsCaption`

Simple sequence:

```java
public void setNvsCaption(NvsCaption nvsCaption) {
```

## `template-mimo-cutsame-152` `setNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:85`

API classes: `NvsCaption`

Simple sequence:

```java
public NvsCaption getNvsCaption() {
```

## `template-mimo-cutsame-153` `getNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:89`

API classes: `NvsCompoundCaption`

Simple sequence:

```java
public void setNvsCompoundCaption(NvsCompoundCaption nvsCompoundCaption) {
```

## `template-mimo-cutsame-154` `setNvsCompoundCaption`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:93`

API classes: `NvsCompoundCaption`

Simple sequence:

```java
public NvsCompoundCaption getNvsCompoundCaption() {
```

## `template-mimo-cutsame-155` `create`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:152`

API classes: `NvsAssetPackageManager`, `NvsTemplateCompoundCaptionDesc`, `NvsTemplateCompoundCaptionItemDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc`, `NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc`
Common calls: `add()`, `create()`, `isEmpty()`, `clone()`, `e()`

Simple sequence:

```java
public static TemplateCaptionDesc create(NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc nvsTemplateCaptionDesc) {
for (NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc nvsTemplateCompoundCaptionItemDesc
for (NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc nvsTemplateCompoundCaptionDesc
```

## `template-mimo-cutsame-156` `create`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:155`

API classes: `NvsAssetPackageManager`, `NvsTemplateCompoundCaptionItemDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc`
Common calls: `add()`, `isEmpty()`, `create()`, `clone()`, `e()`

Simple sequence:

```java
for (NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc nvsTemplateCompoundCaptionItemDesc
```

## `template-mimo-cutsame-157` `create`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:191`

API classes: `NvsAssetPackageManager`, `NvsTemplateCaptionDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateCaptionDesc`
Common calls: `add()`, `create()`

Simple sequence:

```java
public static TemplateCaptionDesc create(NvsAssetPackageManager.NvsTemplateCaptionDesc nvsTemplateCaptionDesc) {
for (NvsAssetPackageManager.NvsTemplateCaptionDesc nvsTemplateCaption : nvsTemplateCaptionDesc.subCaptions) {
```

## `template-mimo-cutsame-158` `clone`

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:316`

API classes: `NvsAssetPackageManager`, `NvsTemplateCompoundCaptionItemDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc`

Simple sequence:

```java
public static TemplateCompoundCaptionItemDesc create(NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc nvsTemplateCompoundCaptionItemDesc) {
```

## `template-mimo-cutsame-159` `getTemplateFootageDesc`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:675`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageDesc`
Common calls: `e()`, `getAssetPackageManager()`, `getTemplateFootages()`

Simple sequence:

```java
public List<NvsAssetPackageManager.NvsTemplateFootageDesc> getTemplateFootageDesc(String uuidString) {
List<NvsAssetPackageManager.NvsTemplateFootageDesc> nvsTemplateFootageDescs = new ArrayList<>();
if (mStreamingContext == null) {
Log.e(TAG, "getTemplateFootageDesc: mStreamingContext is null!");
nvsTemplateFootageDescs = mStreamingContext.getAssetPackageManager().getTemplateFootages(uuidString);
```

## `template-mimo-cutsame-160` `getTemplateFootageDescVideo`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:692`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageDesc`
Common calls: `e()`, `getAssetPackageManager()`, `getTemplateFootages()`, `setNvsTemplateFootageDesc()`, `add()`

Simple sequence:

```java
if (mStreamingContext == null) {
Log.e(TAG, "getTemplateFootageDesc: mStreamingContext is null!");
List<NvsAssetPackageManager.NvsTemplateFootageDesc> nvsTemplateFootageDescList = mStreamingContext.getAssetPackageManager().getTemplateFootages(uuidString);
for (NvsAssetPackageManager.NvsTemplateFootageDesc desc : nvsTemplateFootageDescList) {
meicamNvsTemplateFootageDesc.setNvsTemplateFootageDesc(desc);
```

## `template-mimo-cutsame-161` `getAllNvsTemplateFootageDescs`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:723`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageDesc`
Common calls: `get()`, `size()`, `add()`, `addClipTrackIndexInTimeline()`, `addClipIndexInTimeline()`, `setNvsTemplateFootageDesc()`, `setClipIndexInTimelineList()`, `getClipIndexInTimelineList()`, `setClipTrackIndexInTimelineList()`, `getClipTrackIndexInTimelineList()`

Simple sequence:

```java
for (NvsAssetPackageManager.NvsTemplateFootageDesc desc : nvsTemplateFootageDesc.timelineClipFootages) {
meicamNvsTemplateFootageDesc.setNvsTemplateFootageDesc(desc);
if (needDealFootageDesc(timelineTemplateFootageDesc)) {
timelineTemplateFootageDesc.setClipIndexInTimelineList(nvsTemplateFootageDesc.getClipIndexInTimelineList());
timelineTemplateFootageDesc.setClipTrackIndexInTimelineList(nvsTemplateFootageDesc.getClipTrackIndexInTimelineList());
```

## `template-mimo-cutsame-162` `getAllNvsTemplateFootageDescs`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:724`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageDesc`
Common calls: `get()`, `size()`, `add()`, `addClipTrackIndexInTimeline()`, `addClipIndexInTimeline()`, `setNvsTemplateFootageDesc()`, `setClipIndexInTimelineList()`, `getClipIndexInTimelineList()`, `setClipTrackIndexInTimelineList()`, `getClipTrackIndexInTimelineList()`

Simple sequence:

```java
for (NvsAssetPackageManager.NvsTemplateFootageDesc desc : nvsTemplateFootageDesc.timelineClipFootages) {
meicamNvsTemplateFootageDesc.setNvsTemplateFootageDesc(desc);
if (needDealFootageDesc(timelineTemplateFootageDesc)) {
timelineTemplateFootageDesc.setClipIndexInTimelineList(nvsTemplateFootageDesc.getClipIndexInTimelineList());
timelineTemplateFootageDesc.setClipTrackIndexInTimelineList(nvsTemplateFootageDesc.getClipTrackIndexInTimelineList());
```

## `template-mimo-cutsame-163` `getTemplateVideoClip`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:757`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo`
Common calls: `add()`, `setNvsTemplateFootageCorrespondingClipInfo()`, `setClipTrackIndexInTimelineList()`, `getClipTrackIndexInTimelineList()`, `setClipIndexInTimelineList()`, `getClipIndexInTimelineList()`, `getInstance()`, `isPlaceHolder()`, `setFootageID()`, `sort()`, `getFootageID()`, `get()`

Simple sequence:

```java
for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo : footage.correspondingClipInfos) {
correspondingClipInfo.setNvsTemplateFootageCorrespondingClipInfo(clipInfo);
for (MeicamNvsTemplateFootageCorrespondingClipInfo info : correspondingClipInfos) {
info.setClipTrackIndexInTimelineList(footage.getClipTrackIndexInTimelineList());
info.setClipIndexInTimelineList(footage.getClipIndexInTimelineList());
if (!EditorController.getInstance().isPlaceHolder(info.trackIndex, info.clipIndex)) {
info.setFootageID(footage.id);
for (MeicamNvsTemplateFootageCorrespondingClipInfo templateClip : mClipList) {
key = templateClip.getFootageID();
for (MeicamNvsTemplateFootageCorrespondingClipInfo templateClip : templateClips) {
templateClip.setGroupIndex(groupIndex);
```

## `template-mimo-cutsame-164` `getTemplateVideoClip`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:760`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo`
Common calls: `add()`, `setNvsTemplateFootageCorrespondingClipInfo()`, `setClipTrackIndexInTimelineList()`, `getClipTrackIndexInTimelineList()`, `setClipIndexInTimelineList()`, `getClipIndexInTimelineList()`, `getInstance()`, `isPlaceHolder()`, `setFootageID()`, `sort()`, `getFootageID()`, `get()`

Simple sequence:

```java
for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo : footage.correspondingClipInfos) {
correspondingClipInfo.setNvsTemplateFootageCorrespondingClipInfo(clipInfo);
for (MeicamNvsTemplateFootageCorrespondingClipInfo info : correspondingClipInfos) {
info.setClipTrackIndexInTimelineList(footage.getClipTrackIndexInTimelineList());
info.setClipIndexInTimelineList(footage.getClipIndexInTimelineList());
if (!EditorController.getInstance().isPlaceHolder(info.trackIndex, info.clipIndex)) {
info.setFootageID(footage.id);
for (MeicamNvsTemplateFootageCorrespondingClipInfo templateClip : mClipList) {
key = templateClip.getFootageID();
for (MeicamNvsTemplateFootageCorrespondingClipInfo templateClip : templateClips) {
templateClip.setGroupIndex(groupIndex);
```

## `template-mimo-cutsame-165` `getTemplateVideoClip`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:761`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageCorrespondingClipInfo`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo`
Common calls: `add()`, `setNvsTemplateFootageCorrespondingClipInfo()`, `setClipTrackIndexInTimelineList()`, `getClipTrackIndexInTimelineList()`, `setClipIndexInTimelineList()`, `getClipIndexInTimelineList()`, `getInstance()`, `isPlaceHolder()`, `setFootageID()`

Simple sequence:

```java
for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo : footage.correspondingClipInfos) {
correspondingClipInfo.setNvsTemplateFootageCorrespondingClipInfo(clipInfo);
for (MeicamNvsTemplateFootageCorrespondingClipInfo info : correspondingClipInfos) {
info.setClipTrackIndexInTimelineList(footage.getClipTrackIndexInTimelineList());
info.setClipIndexInTimelineList(footage.getClipIndexInTimelineList());
if (!EditorController.getInstance().isPlaceHolder(info.trackIndex, info.clipIndex)) {
info.setFootageID(footage.id);
```

## `template-mimo-cutsame-166` `needDealFootageDesc`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:857`

API classes: `NvsAssetPackageManager`, `NvsTemplateFootageDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateFootageDesc`, `NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_AUDIO`

Simple sequence:

```java
private boolean needDealFootageDesc(NvsAssetPackageManager.NvsTemplateFootageDesc nvsTemplateFootageDesc) {
return nvsTemplateFootageDesc.type != NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_AUDIO;
```

## `template-mimo-cutsame-167` `getTemplateCaptionsForStandard`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:868`

API classes: `NvsAssetPackageManager`, `NvsTemplateCaptionDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateCaptionDesc`
Common calls: `e()`, `getAssetPackageManager()`, `getTemplateCaptions()`, `size()`, `setOriginalText()`, `setText()`, `add()`

Simple sequence:

```java
List<NvsAssetPackageManager.NvsTemplateCaptionDesc> templateCaptionDescs = new ArrayList<>();
if (mStreamingContext == null) {
Log.e(TAG, "getTemplateFootageDesc: mStreamingContext is null!");
templateCaptionDescs = mStreamingContext.getAssetPackageManager().getTemplateCaptions(uuidString);
if (null != templateCaptionDescs && templateCaptionDescs.size() > 0) {
for (NvsAssetPackageManager.NvsTemplateCaptionDesc desc : templateCaptionDescs) {
templateCaptionDesc.setOriginalText(desc.text);
templateCaptionDesc.setText(desc.text);
```

## `template-mimo-cutsame-168` `getTemplateCaptions`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:918`

API classes: `NvsAssetPackageManager`, `NvsTemplateCaptionDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateCaptionDesc`
Common calls: `e()`, `getAssetPackageManager()`, `getTemplateCaptions()`, `add()`, `create()`

Simple sequence:

```java
if (mStreamingContext == null) {
Log.e(TAG, "getTemplateFootageDesc: mStreamingContext is null!");
List<NvsAssetPackageManager.NvsTemplateCaptionDesc> nvsTemplateCaptionDescs = mStreamingContext.getAssetPackageManager().getTemplateCaptions(uuidString);
for (NvsAssetPackageManager.NvsTemplateCaptionDesc nvsTemplateCaptionDesc : nvsTemplateCaptionDescs) {
```

## `template-mimo-cutsame-169` `getTemplateCompoundCaptions`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:963`

API classes: `NvsAssetPackageManager`, `NvsTemplateCompoundCaptionDesc`
Static/constants: `NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc`
Common calls: `e()`, `getAssetPackageManager()`, `getTemplateCompoundCaptions()`, `add()`, `create()`

Simple sequence:

```java
if (mStreamingContext == null) {
Log.e(TAG, "getTemplateCompoundCaptions: mStreamingContext is null!");
List<NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc> nvsTemplateCaptionDescs =
mStreamingContext.getAssetPackageManager().getTemplateCompoundCaptions(uuidString);
for (NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc nvsTemplateCaptionDesc : nvsTemplateCaptionDescs) {
```

## `template-mimo-cutsame-170` `getTemplateCaptions`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:990`

API classes: `NvsTimelineCompoundCaption`, `NvsTimeline`, `NvsTimelineCaption`, `NvsVideoTrack`, `NvsVideoClip`, `NvsClipCaption`, `NvsClipCompoundCaption`
Common calls: `getText()`, `setInPoint()`, `getInPoint()`, `setCaptionType()`, `add()`, `getNextCaption()`, `e()`, `getFirstCaption()`, `setNvsCaption()`, `getFirstCompoundCaption()`, `getCaptionCount()`, `setNvsCompoundCaption()`

Simple sequence:

```java
public List<TemplateCaptionDesc> getTemplateCaptions(NvsTimeline nvsTimeline) {
if (mStreamingContext == null) {
Log.e(TAG, "getTemplateFootageDesc: mStreamingContext is null!");
NvsTimelineCaption firstCaption = nvsTimeline.getFirstCaption();
templateCaptionDesc.text = firstCaption.getText();
templateCaptionDesc.setInPoint(firstCaption.getInPoint());
templateCaptionDesc.setNvsCaption(firstCaption);
templateCaptionDesc.setCaptionType(TemplateCaptionDesc.TemplateCaptionType.TIMELINE_CAPTION);
firstCaption = nvsTimeline.getNextCaption(firstCaption);
NvsTimelineCompoundCaption firstCompoundCaption = nvsTimeline.getFirstCompoundCaption();
while (null != firstCompoundCaption) {
Log.e("caption", "NvsTimelineCompoundCaption");
int captionCount = firstCompoundCaption.getCaptionCount();
templateCaptionDesc.text = firstCompoundCaption.getText(i);
templateCaptionDesc.setInPoint(firstCompoundCaption.getInPoint());
templateCaptionDesc.setNvsCompoundCaption(firstCompoundCaption);
templateCaptionDesc.setCaptionIndex(i);
templateCaptionDesc.setCaptionType(TemplateCaptionDesc.TemplateCaptionType.TIMELINE_COMPOUND_CAPTION);
firstCompoundCaption = nvsTimeline.getNextCaption(firstCompoundCaption);
NvsVideoTrack videoTrackByIndex = nvsTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrackByIndex.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip clipByIndex = videoTrackByIndex.getClipByIndex(i);
NvsClipCaption clipCaption = clipByIndex.getFirstCaption();
// ... 15 more SDK-related lines omitted in this compressed snippet ...
```

## `template-mimo-cutsame-171` `hasTemplateCaptions`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1081`

API classes: `NvsTimeline`, `NvsTimelineCaption`, `NvsTimelineCompoundCaption`, `NvsVideoTrack`, `NvsVideoClip`, `NvsClipCaption`, `NvsClipCompoundCaption`
Common calls: `getFirstCaption()`, `getFirstCompoundCaption()`, `e()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`

Simple sequence:

```java
public boolean hasTemplateCaptions(NvsTimeline nvsTimeline) {
if (nvsTimeline == null) {
Log.e(TAG, "getTemplateFootageDesc: mStreamingContext is null!");
NvsTimelineCaption firstCaption = nvsTimeline.getFirstCaption();
NvsTimelineCompoundCaption firstCompoundCaption = nvsTimeline.getFirstCompoundCaption();
NvsVideoTrack videoTrackByIndex = nvsTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrackByIndex.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip clipByIndex = videoTrackByIndex.getClipByIndex(i);
if (null != clipByIndex) {
NvsClipCaption clipCaption = clipByIndex.getFirstCaption();
NvsClipCompoundCaption clipCompoundCaption = clipByIndex.getFirstCompoundCaption();
```

## `template-mimo-cutsame-172` `createTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1128`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.templateFootageInfo`
Common calls: `e()`, `createTimeline()`

Simple sequence:

```java
public NvsTimeline createTimeline(String templateId, List<NvsStreamingContext.templateFootageInfo> templateFootAges) {
if (mStreamingContext == null) {
Log.e(TAG, "createTimeline: mStreamingContext is null!");
return mStreamingContext.createTimeline(templateId, templateFootAges);
```

## `template-mimo-cutsame-173` `createTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1145`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.templateFootageInfo`
Common calls: `e()`, `createTimeline()`

Simple sequence:

```java
public NvsTimeline createTimeline(NvsStreamingContext context, String templateId, List<NvsStreamingContext.templateFootageInfo> templateFootAges) {
if (context == null) {
Log.e(TAG, "createTimeline: mStreamingContext is null!");
return context.createTimeline(templateId, templateFootAges);
```

## `template-mimo-cutsame-174` `getCaptionByTemplateCaptionDesc`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1425`

API classes: `NvsVideoTrack`
Common calls: `getClipTrackIndexInTimelineList()`, `get()`, `size()`, `getClipIndexInTimelineList()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getInPoint()`, `getInternalTimeline()`, `add()`

Simple sequence:

```java
for (int i = 0; i < templateCaptionDesc.getClipTrackIndexInTimelineList().size(); i++) {
int trackIndexTimeline = templateCaptionDesc.getClipTrackIndexInTimelineList().get(i);
int clipIndexTimeline = templateCaptionDesc.getClipIndexInTimelineList().get(i);
NvsVideoTrack meicamVideoTrack = meicamTimeline.getVideoTrackByIndex(trackIndexTimeline);
meicamVideoClip = meicamVideoTrack.getClipByIndex(clipIndexTimeline);
clipInPoint += meicamVideoClip.getInPoint();
meicamTimeline = meicamVideoClip.getInternalTimeline();
```

## `template-mimo-cutsame-175` `loadTimelineToTemplate`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:888`

API classes: `NvsTimeline`, `NvsVideoTrack`
Common calls: `getInstance()`, `clear()`, `add()`, `getMeicamStickerCaptionTrackList()`, `e()`, `getMeicamVideoTrackList()`, `videoTrackCount()`, `getVideoTrackByIndex()`, `loadData()`, `getClipInfoList()`, `getFirstCaption()`

Simple sequence:

```java
public static void loadTimelineToTemplate(NvsTimeline timeline) {
if (timeline == null) {
LogUtils.e("timeline == null");
List<MeicamVideoTrack> meicamVideoTrackList = TimelineData.getInstance().getMeicamVideoTrackList();
int trackCount = timeline.videoTrackCount();
for (int i = 0; i < trackCount; i++) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(i);
List<MeicamStickerCaptionTrack> captionTrackList = TimelineData.getInstance().getMeicamStickerCaptionTrackList();
List<ClipInfo<?>> clipInfoList = meicamStickerCaptionTrack.getClipInfoList();
loadTimelineCaptionToTemplate(timeline, timeline.getFirstCaption(), clipInfoList);
TimelineData.getInstance().getMeicamStickerCaptionTrackList().add(meicamStickerCaptionTrack);
```
