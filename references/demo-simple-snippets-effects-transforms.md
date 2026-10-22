# Demo Simple Snippets - Effects Transforms

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: built-in/package video effects, color adjust, transform/crop/background, transitions, masks, watermarks, speed, keyframes, and effect parameter setting.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [effects-transforms-001 initMeicamSdk](#effects-transforms-001-initmeicamsdk)
- [effects-transforms-002 onResume](#effects-transforms-002-onresume)
- [effects-transforms-003 getEffectContext](#effects-transforms-003-geteffectcontext)
- [effects-transforms-004 setStrength](#effects-transforms-004-setstrength)
- [effects-transforms-005 getColor](#effects-transforms-005-getcolor)
- [effects-transforms-006 clearShape](#effects-transforms-006-clearshape)
- [effects-transforms-007 clearShape](#effects-transforms-007-clearshape)
- [effects-transforms-008 clearShape](#effects-transforms-008-clearshape)
- [effects-transforms-009 clearMicroShape](#effects-transforms-009-clearmicroshape)
- [effects-transforms-010 clearMicroShape](#effects-transforms-010-clearmicroshape)
- [effects-transforms-011 clearMicroShape](#effects-transforms-011-clearmicroshape)
- [effects-transforms-012 clearMicroShape](#effects-transforms-012-clearmicroshape)
- [effects-transforms-013 removeAllFilterFx](#effects-transforms-013-removeallfilterfx)
- [effects-transforms-014 doBgSeg](#effects-transforms-014-dobgseg)
- [effects-transforms-015 setBgSeg](#effects-transforms-015-setbgseg)
- [effects-transforms-016 getColorFromLiveWindow](#effects-transforms-016-getcolorfromlivewindow)
- [effects-transforms-017 initData](#effects-transforms-017-initdata)
- [effects-transforms-018 onClick](#effects-transforms-018-onclick)
- [effects-transforms-019 removeAllFilterFx](#effects-transforms-019-removeallfilterfx)
- [effects-transforms-020 removeAllFilterFx](#effects-transforms-020-removeallfilterfx)
- [effects-transforms-021 removeAllFilterFx](#effects-transforms-021-removeallfilterfx)
- [effects-transforms-022 readdFilterFx](#effects-transforms-022-readdfilterfx)
- [effects-transforms-023 startFilterFx](#effects-transforms-023-startfilterfx)
- [effects-transforms-024 removeAllTransition](#effects-transforms-024-removealltransition)
- [effects-transforms-025 information](#effects-transforms-025-information)
- [effects-transforms-026 setVideoClipInfo](#effects-transforms-026-setvideoclipinfo)
- [effects-transforms-027 getTransformFx](#effects-transforms-027-gettransformfx)
- [effects-transforms-028 getTransformFx](#effects-transforms-028-gettransformfx)
- [effects-transforms-029 setEffectByPoint](#effects-transforms-029-seteffectbypoint)
- [effects-transforms-030 setDrawRectByEffectData](#effects-transforms-030-setdrawrectbyeffectdata)
- [effects-transforms-031 connectTimelineWithLiveWindow](#effects-transforms-031-connecttimelinewithlivewindow)
- [effects-transforms-032 setStreamingEngineCallback](#effects-transforms-032-setstreamingenginecallback)
- [effects-transforms-033 playVideo](#effects-transforms-033-playvideo)
- [effects-transforms-034 initAnimationViewList](#effects-transforms-034-initanimationviewlist)
- [effects-transforms-035 initAnimationViewList](#effects-transforms-035-initanimationviewlist)
- [effects-transforms-036 appendAnimationFxToVideoPackage](#effects-transforms-036-appendanimationfxtovideopackage)
- [effects-transforms-037 updateBackground](#effects-transforms-037-updatebackground)
- [effects-transforms-038 playBackEOF](#effects-transforms-038-playbackeof)
- [effects-transforms-039 playStopped](#effects-transforms-039-playstopped)
- [effects-transforms-040 setOnItemClickListener](#effects-transforms-040-setonitemclicklistener)
- [effects-transforms-041 onColorApplyAll](#effects-transforms-041-oncolorapplyall)
- [effects-transforms-042 onBlurApplyAll](#effects-transforms-042-onblurapplyall)
- [effects-transforms-043 getClipStartTime](#effects-transforms-043-getclipstarttime)
- [effects-transforms-044 getClipEndTime](#effects-transforms-044-getclipendtime)
- [effects-transforms-045 setDefaultBackground](#effects-transforms-045-setdefaultbackground)
- [effects-transforms-046 playVideo](#effects-transforms-046-playvideo)
- [effects-transforms-047 connectTimelineWithLiveWindow](#effects-transforms-047-connecttimelinewithlivewindow)
- [effects-transforms-048 getInitCutData](#effects-transforms-048-getinitcutdata)
- [effects-transforms-049 onItemClicked](#effects-transforms-049-onitemclicked)
- [effects-transforms-050 onVertical](#effects-transforms-050-onvertical)
- [effects-transforms-051 onRotation](#effects-transforms-051-onrotation)
- [effects-transforms-052 onHorizontal](#effects-transforms-052-onhorizontal)
- [effects-transforms-053 adjustClip](#effects-transforms-053-adjustclip)
- [effects-transforms-054 onPlaybackPreloadingCompletion](#effects-transforms-054-onplaybackpreloadingcompletion)
- [effects-transforms-055 onPlaybackTimelinePosition](#effects-transforms-055-onplaybacktimelineposition)
- [effects-transforms-056 onSeekingTimelinePosition](#effects-transforms-056-onseekingtimelineposition)
- [effects-transforms-057 onCreateView](#effects-transforms-057-oncreateview)
- [effects-transforms-058 initListener](#effects-transforms-058-initlistener)
- [effects-transforms-059 initListener](#effects-transforms-059-initlistener)
- [effects-transforms-060 setOnSeekBarChangeListener](#effects-transforms-060-setonseekbarchangelistener)
- [effects-transforms-061 setLiveWindowRatio](#effects-transforms-061-setlivewindowratio)
- [effects-transforms-062 updateRegionData](#effects-transforms-062-updateregiondata)
- [effects-transforms-063 onDetach](#effects-transforms-063-ondetach)
- [effects-transforms-064 playVideoButtonClick](#effects-transforms-064-playvideobuttonclick)
- [effects-transforms-065 playVideo](#effects-transforms-065-playvideo)
- [effects-transforms-066 playVideoFromStartPosition](#effects-transforms-066-playvideofromstartposition)
- [effects-transforms-067 getTimeLine](#effects-transforms-067-gettimeline)
- [effects-transforms-068 initColorAdjustVideoFx](#effects-transforms-068-initcoloradjustvideofx)
- [effects-transforms-069 onLoadFinished](#effects-transforms-069-onloadfinished)
- [effects-transforms-070 playStopped](#effects-transforms-070-playstopped)
- [effects-transforms-071 changeSpeed](#effects-transforms-071-changespeed)
- [effects-transforms-072 changeSpeedForCurve](#effects-transforms-072-changespeedforcurve)
- [effects-transforms-073 getClipDuration](#effects-transforms-073-getclipduration)
- [effects-transforms-074 playVideo](#effects-transforms-074-playvideo)
- [effects-transforms-075 playVideo](#effects-transforms-075-playvideo)
- [effects-transforms-076 getTimelinePositionFromClipPosition](#effects-transforms-076-gettimelinepositionfromclipposition)
- [effects-transforms-077 getClipPositionFromTimelinePosition](#effects-transforms-077-getclippositionfromtimelineposition)
- [effects-transforms-078 updateVolumeRelativeView](#effects-transforms-078-updatevolumerelativeview)
- [effects-transforms-079 onLoadFinished](#effects-transforms-079-onloadfinished)
- [effects-transforms-080 getFilterColorParam](#effects-transforms-080-getfiltercolorparam)
- [effects-transforms-081 setName](#effects-transforms-081-setname)
- [effects-transforms-082 getMaskRegionInfo](#effects-transforms-082-getmaskregioninfo)
- [effects-transforms-083 getLocalData](#effects-transforms-083-getlocaldata)
- [effects-transforms-084 playStopped](#effects-transforms-084-playstopped)
- [effects-transforms-085 streamingEngineStateChangedFromParent](#effects-transforms-085-streamingenginestatechangedfromparent)
- [effects-transforms-086 playbackTimelinePositionFromParent](#effects-transforms-086-playbacktimelinepositionfromparent)
- [effects-transforms-087 onIntensity](#effects-transforms-087-onintensity)
- [effects-transforms-088 streamingEngineStateChangedFromParent](#effects-transforms-088-streamingenginestatechangedfromparent)
- [effects-transforms-089 initKeyFrameView](#effects-transforms-089-initkeyframeview)
- [effects-transforms-090 nextFrameClick](#effects-transforms-090-nextframeclick)
- [effects-transforms-091 nextFrameClick](#effects-transforms-091-nextframeclick)
- [effects-transforms-092 beforeFrameClick](#effects-transforms-092-beforeframeclick)
- [effects-transforms-093 beforeFrameClick](#effects-transforms-093-beforeframeclick)
- [effects-transforms-094 beforeFrameClick](#effects-transforms-094-beforeframeclick)
- [effects-transforms-095 deleteFrameClick](#effects-transforms-095-deleteframeclick)
- [effects-transforms-096 onProgressChanged](#effects-transforms-096-onprogresschanged)
- [effects-transforms-097 initFilterAssets](#effects-transforms-097-initfilterassets)
- [effects-transforms-098 playStopped](#effects-transforms-098-playstopped)
- [effects-transforms-099 initFilterView](#effects-transforms-099-initfilterview)
- [effects-transforms-100 initListener](#effects-transforms-100-initlistener)
- [effects-transforms-101 setAddDeleteViewEnable](#effects-transforms-101-setadddeleteviewenable)
- [effects-transforms-102 FilterKeyFrameView](#effects-transforms-102-filterkeyframeview)
- [effects-transforms-103 onTouch](#effects-transforms-103-ontouch)
- [effects-transforms-104 updateAllKeyFrameViewStatusWhenScroll](#effects-transforms-104-updateallkeyframeviewstatuswhenscroll)
- [effects-transforms-105 updateAllKeyFrameViewStatusWhenScroll](#effects-transforms-105-updateallkeyframeviewstatuswhenscroll)
- [effects-transforms-106 setAdjustFilter](#effects-transforms-106-setadjustfilter)
- [effects-transforms-107 changeAdjustIntensity](#effects-transforms-107-changeadjustintensity)
- [effects-transforms-108 onSizeChanged](#effects-transforms-108-onsizechanged)
- [effects-transforms-109 getClipStartTime](#effects-transforms-109-getclipstarttime)
- [effects-transforms-110 getClipEndTime](#effects-transforms-110-getclipendtime)
- [effects-transforms-111 getClipDuration](#effects-transforms-111-getclipduration)
- [effects-transforms-112 setMaskCenter](#effects-transforms-112-setmaskcenter)
- [effects-transforms-113 removeTimelineAnimal](#effects-transforms-113-removetimelineanimal)
- [effects-transforms-114 playBackEOF](#effects-transforms-114-playbackeof)
- [effects-transforms-115 playStopped](#effects-transforms-115-playstopped)
- [effects-transforms-116 playbackTimelinePosition](#effects-transforms-116-playbacktimelineposition)
- [effects-transforms-117 streamingEngineStateChanged](#effects-transforms-117-streamingenginestatechanged)
- [effects-transforms-118 changeMaskByCrop](#effects-transforms-118-changemaskbycrop)
- [effects-transforms-119 buildCircleMaskRegionInfo](#effects-transforms-119-buildcirclemaskregioninfo)
- [effects-transforms-120 buildRectMaskRegionInfo](#effects-transforms-120-buildrectmaskregioninfo)
- [effects-transforms-121 maskRegionInfoAddPoints](#effects-transforms-121-maskregioninfoaddpoints)
- [effects-transforms-122 buildHeartMaskRegionInfo](#effects-transforms-122-buildheartmaskregioninfo)
- [effects-transforms-123 buildPolygonMaskRegionInfo](#effects-transforms-123-buildpolygonmaskregioninfo)
- [effects-transforms-124 buildStarMaskRegionInfo](#effects-transforms-124-buildstarmaskregioninfo)
- [effects-transforms-125 mapViewToNormalized](#effects-transforms-125-mapviewtonormalized)
- [effects-transforms-126 buildNvsPositionListFromPointFList](#effects-transforms-126-buildnvspositionlistfrompointflist)
- [effects-transforms-127 buildNvsPositionListFromPointFList](#effects-transforms-127-buildnvspositionlistfrompointflist)
- [effects-transforms-128 buildNvsPositionListFromPointFList](#effects-transforms-128-buildnvspositionlistfrompointflist)
- [effects-transforms-129 buildRealMaskInfoData](#effects-transforms-129-buildrealmaskinfodata)
- [effects-transforms-130 assetSizeInBox](#effects-transforms-130-assetsizeinbox)
- [effects-transforms-131 buildMaskRegionRect](#effects-transforms-131-buildmaskregionrect)
- [effects-transforms-132 calculateMaskByCrop](#effects-transforms-132-calculatemaskbycrop)
- [effects-transforms-133 streamingEngineStateChanged](#effects-transforms-133-streamingenginestatechanged)
- [effects-transforms-134 streamingEngineStateChanged](#effects-transforms-134-streamingenginestatechanged)
- [effects-transforms-135 onClick](#effects-transforms-135-onclick)
- [effects-transforms-136 removeTimeline](#effects-transforms-136-removetimeline)
- [effects-transforms-137 onAssetHorizFlip](#effects-transforms-137-onassethorizflip)
- [effects-transforms-138 playStopped](#effects-transforms-138-playstopped)
- [effects-transforms-139 playStopped](#effects-transforms-139-playstopped)
- [effects-transforms-140 playbackTimelinePosition](#effects-transforms-140-playbacktimelineposition)
- [effects-transforms-141 streamingEngineStateChanged](#effects-transforms-141-streamingenginestatechanged)
- [effects-transforms-142 streamingEngineStateChanged](#effects-transforms-142-streamingenginestatechanged)
- [effects-transforms-143 refreshLiveWindowFrame](#effects-transforms-143-refreshlivewindowframe)
- [effects-transforms-144 setDynamicWaterMark](#effects-transforms-144-setdynamicwatermark)
- [effects-transforms-145 onFragmentLoadFinished](#effects-transforms-145-onfragmentloadfinished)
- [effects-transforms-146 onStreamingEngineStateChanged](#effects-transforms-146-onstreamingenginestatechanged)
- [effects-transforms-147 removeTimeline](#effects-transforms-147-removetimeline)
- [effects-transforms-148 updateFxIntensity](#effects-transforms-148-updatefxintensity)
- [effects-transforms-149 setSelectCoverListener](#effects-transforms-149-setselectcoverlistener)
- [effects-transforms-150 updateTransform2DFx](#effects-transforms-150-updatetransform2dfx)
- [effects-transforms-151 onClick](#effects-transforms-151-onclick)
- [effects-transforms-152 setOnClickListener](#effects-transforms-152-setonclicklistener)
- [effects-transforms-153 getSqView](#effects-transforms-153-getsqview)
- [effects-transforms-154 onPlaybackTimelinePosition](#effects-transforms-154-onplaybacktimelineposition)
- [effects-transforms-155 addRemainVideoClip](#effects-transforms-155-addremainvideoclip)
- [effects-transforms-156 getTransform2DFx](#effects-transforms-156-gettransform2dfx)
- [effects-transforms-157 removeVideoFx](#effects-transforms-157-removevideofx)
- [effects-transforms-158 updateSecTrackTransform2DFx](#effects-transforms-158-updatesectracktransform2dfx)
- [effects-transforms-159 updateTransform2DFx](#effects-transforms-159-updatetransform2dfx)
- [effects-transforms-160 updateFilterVideoFx](#effects-transforms-160-updatefiltervideofx)
- [effects-transforms-161 updateFilterVideoFx](#effects-transforms-161-updatefiltervideofx)
- [effects-transforms-162 initTitle](#effects-transforms-162-inittitle)
- [effects-transforms-163 initFilterList](#effects-transforms-163-initfilterlist)
- [effects-transforms-164 setTransCount](#effects-transforms-164-settranscount)
- [effects-transforms-165 addTimelineFilter](#effects-transforms-165-addtimelinefilter)
- [effects-transforms-166 addTimelineFilter](#effects-transforms-166-addtimelinefilter)
- [effects-transforms-167 setVideoClipTrans](#effects-transforms-167-setvideocliptrans)
- [effects-transforms-168 copyBuiltFx](#effects-transforms-168-copybuiltfx)
- [effects-transforms-169 buildTimelineMaskClipInfo](#effects-transforms-169-buildtimelinemaskclipinfo)
- [effects-transforms-170 buildFilterByTimeline](#effects-transforms-170-buildfilterbytimeline)
- [effects-transforms-171 applyFilterByTimeline](#effects-transforms-171-applyfilterbytimeline)
- [effects-transforms-172 applyExprVarByFilter](#effects-transforms-172-applyexprvarbyfilter)
- [effects-transforms-173 buildFilterByClip](#effects-transforms-173-buildfilterbyclip)
- [effects-transforms-174 buildSingleClipFilter](#effects-transforms-174-buildsingleclipfilter)
- [effects-transforms-175 appendFilterFx](#effects-transforms-175-appendfilterfx)
- [effects-transforms-176 setTransition](#effects-transforms-176-settransition)
- [effects-transforms-177 setTransition](#effects-transforms-177-settransition)
- [effects-transforms-178 applyAnimation](#effects-transforms-178-applyanimation)
- [effects-transforms-179 buildColorAdjustInfo](#effects-transforms-179-buildcoloradjustinfo)
- [effects-transforms-180 buildAdjustCutInfo](#effects-transforms-180-buildadjustcutinfo)
- [effects-transforms-181 buildTimelineBackground](#effects-transforms-181-buildtimelinebackground)
- [effects-transforms-182 buildTimelineBackground](#effects-transforms-182-buildtimelinebackground)
- [effects-transforms-183 effect](#effects-transforms-183-effect)
- [effects-transforms-184 applyCropMaskData](#effects-transforms-184-applycropmaskdata)
- [effects-transforms-185 removeRawBuildInFx](#effects-transforms-185-removerawbuildinfx)
- [effects-transforms-186 removeRawBuildInFx](#effects-transforms-186-removerawbuildinfx)
- [effects-transforms-187 findOrCrateVideoFxFromVideoClip](#effects-transforms-187-findorcratevideofxfromvideoclip)
- [effects-transforms-188 findOrCrateVideoFxFromVideoClip](#effects-transforms-188-findorcratevideofxfromvideoclip)
- [effects-transforms-189 findVideoFxFromVideoClip](#effects-transforms-189-findvideofxfromvideoclip)
- [effects-transforms-190 findVideoFxFromVideoClip](#effects-transforms-190-findvideofxfromvideoclip)
- [effects-transforms-191 getFilterFxs](#effects-transforms-191-getfilterfxs)
- [effects-transforms-192 logTimeline](#effects-transforms-192-logtimeline)
- [effects-transforms-193 compileVideo](#effects-transforms-193-compilevideo)
- [effects-transforms-194 setClipTrans](#effects-transforms-194-setcliptrans)
- [effects-transforms-195 getStoryboardFx](#effects-transforms-195-getstoryboardfx)
- [effects-transforms-196 setTransitionInterval](#effects-transforms-196-settransitioninterval)
- [effects-transforms-197 getVideoTransition](#effects-transforms-197-getvideotransition)
- [effects-transforms-198 getFilterColorParam](#effects-transforms-198-getfiltercolorparam)
- [effects-transforms-199 setAdjustEffect](#effects-transforms-199-setadjusteffect)
- [effects-transforms-200 setAdjustEffect](#effects-transforms-200-setadjusteffect)
- [effects-transforms-201 setTimelineAdjustEffect](#effects-transforms-201-settimelineadjusteffect)
- [effects-transforms-202 setTimelineAdjustEffect](#effects-transforms-202-settimelineadjusteffect)
- [effects-transforms-203 applyTransform](#effects-transforms-203-applytransform)
- [effects-transforms-204 applyEffect](#effects-transforms-204-applyeffect)
- [effects-transforms-205 getMaskTargetFx](#effects-transforms-205-getmasktargetfx)
- [effects-transforms-206 setRevert](#effects-transforms-206-setrevert)
- [effects-transforms-207 setMaskRegionInfo](#effects-transforms-207-setmaskregioninfo)
- [effects-transforms-208 setMeicamFxParamList](#effects-transforms-208-setmeicamfxparamlist)
- [effects-transforms-209 clone](#effects-transforms-209-clone)
- [effects-transforms-210 getDuration](#effects-transforms-210-getduration)
- [effects-transforms-211 loadData](#effects-transforms-211-loaddata)
- [effects-transforms-212 getResourceId](#effects-transforms-212-getresourceid)
- [effects-transforms-213 removeNvsVideoFx](#effects-transforms-213-removenvsvideofx)
- [effects-transforms-214 removeNvsVideoFx](#effects-transforms-214-removenvsvideofx)
- [effects-transforms-215 setDefaultBackground](#effects-transforms-215-setdefaultbackground)
- [effects-transforms-216 removeVideoFx](#effects-transforms-216-removevideofx)
- [effects-transforms-217 removeVideoFx](#effects-transforms-217-removevideofx)
- [effects-transforms-218 setAdjustEffect](#effects-transforms-218-setadjusteffect)
- [effects-transforms-219 setMaskRegionInfoData](#effects-transforms-219-setmaskregioninfodata)
- [effects-transforms-220 setMeicamFxParam](#effects-transforms-220-setmeicamfxparam)
- [effects-transforms-221 bindToTimeline](#effects-transforms-221-bindtotimeline)
- [effects-transforms-222 bindToTimeline](#effects-transforms-222-bindtotimeline)
- [effects-transforms-223 setValue](#effects-transforms-223-setvalue)
- [effects-transforms-224 setValue](#effects-transforms-224-setvalue)
- [effects-transforms-225 setResourceId](#effects-transforms-225-setresourceid)
- [effects-transforms-226 verifyTransition](#effects-transforms-226-verifytransition)
- [effects-transforms-227 findPropertyFx](#effects-transforms-227-findpropertyfx)
- [effects-transforms-228 findPropertyFx](#effects-transforms-228-findpropertyfx)
- [effects-transforms-229 resetPropertyAnimation](#effects-transforms-229-resetpropertyanimation)
- [effects-transforms-230 resetPropertyAnimation](#effects-transforms-230-resetpropertyanimation)
- [effects-transforms-231 LogMainTrack](#effects-transforms-231-logmaintrack)
- [effects-transforms-232 setClipTrans](#effects-transforms-232-setcliptrans)
- [effects-transforms-233 setmRevert](#effects-transforms-233-setmrevert)
- [effects-transforms-234 setMaskRegionInfo](#effects-transforms-234-setmaskregioninfo)
- [effects-transforms-235 setAdjustEffect](#effects-transforms-235-setadjusteffect)
- [effects-transforms-236 colorToNvsColor](#effects-transforms-236-colortonvscolor)
- [effects-transforms-237 colorFloatToNvsColor](#effects-transforms-237-colorfloattonvscolor)
- [effects-transforms-238 getColorArray](#effects-transforms-238-getcolorarray)
- [effects-transforms-239 setTimelineData](#effects-transforms-239-settimelinedata)
- [effects-transforms-240 setAdjustEffects](#effects-transforms-240-setadjusteffects)
- [effects-transforms-241 buildTimelineWaterMark](#effects-transforms-241-buildtimelinewatermark)
- [effects-transforms-242 fillTrack](#effects-transforms-242-filltrack)
- [effects-transforms-243 fillTrack](#effects-transforms-243-filltrack)
- [effects-transforms-244 setTransition](#effects-transforms-244-settransition)
- [effects-transforms-245 clearAllBuildInTransition](#effects-transforms-245-clearallbuildintransition)
- [effects-transforms-246 buildTimelineFilter](#effects-transforms-246-buildtimelinefilter)
- [effects-transforms-247 buildClipFilter](#effects-transforms-247-buildclipfilter)
- [effects-transforms-248 appendFilterFx](#effects-transforms-248-appendfilterfx)
<!-- END GENERATED CONTENTS -->

## `effects-transforms-001` `initMeicamSdk`

Source: `app/src/main/java/com/meishe/sdkdemo/MSApplication.java:68`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.setIconSize`, `NvsStreamingContext.setMaxReaderCount`, `NvsStreamingContext.getInstance`, `NvsStreamingContext.SdkVersion`
Common calls: `setIconSize()`, `setMaxReaderCount()`, `instance()`, `isEnableAssetLicense()`, `e()`, `initStreamingContext()`, `initEffectSdkContext()`, `init()`, `getInstance()`, `getSdkVersion()`, `setColorGainForSDRToHDR()`

Simple sequence:

```java
NvsStreamingContext.setIconSize(1);
NvsStreamingContext.setMaxReaderCount(10);
NvsStreamingContext instance = NvsStreamingContext.getInstance();
if (instance != null) {
NvsStreamingContext.SdkVersion version = instance.getSdkVersion();
instance.setColorGainForSDRToHDR(2);
```

## `effects-transforms-002` `onResume`

Source: `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java:318`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `setLiveModel()`, `getLiveWindowModel()`, `getInstance()`, `setColorGainForSDRToHDR()`, `getColorGain()`

Simple sequence:

```java
MSLiveWindow.setLiveModel(parameterValues.getLiveWindowModel());
NvsStreamingContext mStreamingContext = NvsStreamingContext.getInstance();
if (mStreamingContext != null) {
mStreamingContext.setColorGainForSDRToHDR(parameterValues.getColorGain());
```

## `effects-transforms-003` `getEffectContext`

Source: `app/src/main/java/com/meishe/sdkdemo/base/BaseActivity.java:93`

API classes: `NvsEffectSdkContext`
Static/constants: `NvsEffectSdkContext.getInstance`
Common calls: `getInstance()`, `initEffectSdkContext()`

Simple sequence:

```java
if (mNvsEffectSdkContext == null) {
mNvsEffectSdkContext = NvsEffectSdkContext.getInstance();
```

## `effects-transforms-004` `setStrength`

Source: `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java:112`

API classes: `NvsColor`

Simple sequence:

```java
public NvsColor getColor() {
```

## `effects-transforms-005` `getColor`

Source: `app/src/main/java/com/meishe/sdkdemo/bean/AdjustSpecialEffectsInfo.java:116`

API classes: `NvsColor`

Simple sequence:

```java
public void setColor(NvsColor color) {
```

## `effects-transforms-006` `clearShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2648`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `getPackageId()`, `getFxName()`, `setFloatVal()`

Simple sequence:

```java
for (IFxInfo shapeInfo : mShapeDataList) {
if (shapeInfo instanceof CompoundFxInfo && !TextUtils.isEmpty(shapeInfo.getPackageId())) {
NvsCaptureVideoFx captureVideoFx;
String fxName = compoundFxInfo.getFxName();
if (!TextUtils.isEmpty(fxName)) {
captureVideoFx.setFloatVal(fxName, 0);
```

## `effects-transforms-007` `clearShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2649`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `getPackageId()`, `getFxName()`, `setFloatVal()`

Simple sequence:

```java
for (IFxInfo shapeInfo : mShapeDataList) {
if (shapeInfo instanceof CompoundFxInfo && !TextUtils.isEmpty(shapeInfo.getPackageId())) {
NvsCaptureVideoFx captureVideoFx;
String fxName = compoundFxInfo.getFxName();
if (!TextUtils.isEmpty(fxName)) {
captureVideoFx.setFloatVal(fxName, 0);
```

## `effects-transforms-008` `clearShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2650`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `getPackageId()`, `getFxName()`, `setFloatVal()`

Simple sequence:

```java
if (shapeInfo instanceof CompoundFxInfo && !TextUtils.isEmpty(shapeInfo.getPackageId())) {
NvsCaptureVideoFx captureVideoFx;
String fxName = compoundFxInfo.getFxName();
if (!TextUtils.isEmpty(fxName)) {
captureVideoFx.setFloatVal(fxName, 0);
```

## `effects-transforms-009` `clearMicroShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2667`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `getPackageId()`, `getFxName()`, `setFloatVal()`

Simple sequence:

```java
for (IFxInfo shapeInfo : mSmallShapeDataList) {
if (shapeInfo instanceof CompoundFxInfo && !TextUtils.isEmpty(shapeInfo.getPackageId())) {
NvsCaptureVideoFx captureVideoFx;
String fxName = compoundFxInfo.getFxName();
if (!TextUtils.isEmpty(fxName)) {
captureVideoFx.setFloatVal(fxName, 0);
```

## `effects-transforms-010` `clearMicroShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2668`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `getPackageId()`, `getFxName()`, `setFloatVal()`

Simple sequence:

```java
for (IFxInfo shapeInfo : mSmallShapeDataList) {
if (shapeInfo instanceof CompoundFxInfo && !TextUtils.isEmpty(shapeInfo.getPackageId())) {
NvsCaptureVideoFx captureVideoFx;
String fxName = compoundFxInfo.getFxName();
if (!TextUtils.isEmpty(fxName)) {
captureVideoFx.setFloatVal(fxName, 0);
```

## `effects-transforms-011` `clearMicroShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2669`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `getPackageId()`, `getFxName()`, `setFloatVal()`

Simple sequence:

```java
for (IFxInfo shapeInfo : mSmallShapeDataList) {
if (shapeInfo instanceof CompoundFxInfo && !TextUtils.isEmpty(shapeInfo.getPackageId())) {
NvsCaptureVideoFx captureVideoFx;
String fxName = compoundFxInfo.getFxName();
if (!TextUtils.isEmpty(fxName)) {
captureVideoFx.setFloatVal(fxName, 0);
```

## `effects-transforms-012` `clearMicroShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2670`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `getPackageId()`, `getFxName()`, `setFloatVal()`

Simple sequence:

```java
if (shapeInfo instanceof CompoundFxInfo && !TextUtils.isEmpty(shapeInfo.getPackageId())) {
NvsCaptureVideoFx captureVideoFx;
String fxName = compoundFxInfo.getFxName();
if (!TextUtils.isEmpty(fxName)) {
captureVideoFx.setFloatVal(fxName, 0);
```

## `effects-transforms-013` `removeAllFilterFx`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2737`

API classes: `NvsCaptureVideoFx`
Common calls: `equals()`, `add()`, `getAttachment()`, `isEmpty()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getBuiltinCaptureVideoFxName()`, `getCaptureVideoFxPackageId()`, `getName()`, `getId()`, `getEffectContent()`, `getFilterParams()`

Simple sequence:

```java
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx fx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (fx.getAttachment(Constants.BG_SEG_EFFECT_ATTACH_KEY) != null) {
boolean isBgSet = (boolean) fx.getAttachment(Constants.BG_SEG_EFFECT_ATTACH_KEY);
String name = fx.getBuiltinCaptureVideoFxName();
String packageId = fx.getCaptureVideoFxPackageId();
if (!"Beauty".equals(name) && !"Face Effect".equals(name) && !"AR Scene".equals(name)) {
if (TextUtils.isEmpty(packageId) && !TextUtils.isEmpty(name) && (mCurrentFilterInfo != null && TextUtils.equals(name, mCurrentFilterInfo.getName()))) {
} else if ((mCurrentFilterInfo != null && TextUtils.equals(packageId, mCurrentFilterInfo.getId()))) {
if (preMakeUp != null) {
MakeupParamContent effectContent = preMakeUp.getEffectContent();
if (effectContent != null) {
List<FilterParam> filterParamList = effectContent.getFilterParams();
for (FilterParam filterArgs : filterParamList) {
if (TextUtils.equals(packageId, filterArgs.getPackageId())) {
```

## `effects-transforms-014` `doBgSeg`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3508`

API classes: `NvsColor`
Common calls: `setBooleanVal()`, `isSingleBufferMode()`, `insertBuiltinCaptureVideoFx()`, `setAttachment()`, `setMenuVal()`, `isAndroidCameraPreferDualBufferAR()`, `addWhiteListFx()`, `setIntVal()`, `setColorVal()`

Simple sequence:

```java
mArSceneFaceEffect.setBooleanVal("Single Buffer Mode", parameterValues.isSingleBufferMode());
if (mBgSegEffect == null) {
mBgSegEffect = mStreamingContext.insertBuiltinCaptureVideoFx("Segmentation Background Fill", 0);
mBgSegEffect.setAttachment(Constants.BG_SEG_EFFECT_ATTACH_KEY, true);
mBgSegEffect.setMenuVal(Constants.KEY_SEGMENT_TYPE, Constants.SEGMENT_TYPE_BACKGROUND);
if (!mStreamingContext.isAndroidCameraPreferDualBufferAR()) {
mArSceneFaceEffect.setBooleanVal("Single Buffer Mode", false);
mBgSegEffect.setIntVal(Constants.KEY_SEGMENT_STRETCH_MODE, 1);
mBgSegEffect.setColorVal(Constants.KEY_SEGMENT_BACKGROUND_COLOR, new NvsColor(0.0f, 0.0f, 0.0f, 0.0f));
```

## `effects-transforms-015` `setBgSeg`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3550`

API classes: `NvsCaptureSceneInfo`
Static/constants: `NvsCaptureSceneInfo.ClipData`, `NvsCaptureSceneInfo.CAPTURESCENE_INFO_IMAGE_FILLMODE_CROP`
Common calls: `getStringExtra()`, `equals()`, `removeCurrentCaptureScene()`, `ClipData()`, `add()`, `applyCaptureScene()`

Simple sequence:

```java
String clickType = intent.getStringExtra(SINGLE_PICTURE_CLICK_TYPE);
if (TextUtils.equals(clickType, SINGLE_PICTURE_CLICK_CANCEL)) {
mStreamingContext.removeCurrentCaptureScene();
if (TextUtils.equals(clickType, SINGLE_PICTURE_CLICK_CONFIRM)) {
String filePath = intent.getStringExtra(SINGLE_PICTURE_PATH);
NvsCaptureSceneInfo sceneInfo = new NvsCaptureSceneInfo();
List<NvsCaptureSceneInfo.ClipData> clipDataList = new ArrayList<>();
NvsCaptureSceneInfo.ClipData clipData = new NvsCaptureSceneInfo.ClipData();
clipData.imageFillMode = NvsCaptureSceneInfo.CAPTURESCENE_INFO_IMAGE_FILLMODE_CROP;
mStreamingContext.applyCaptureScene(mBgSegPackageId, sceneInfo);
```

## `effects-transforms-016` `getColorFromLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:193`

API classes: `NvsColor`
Common calls: `getWidth()`, `getHeight()`, `getX()`, `getY()`, `sampleColorFromCapturedVideoFrame()`

Simple sequence:

```java
private NvsColor getColorFromLiveWindow(MotionEvent event) {
sampleRect.left = (int) (event.getX() - sampleWidth / 2);
} else if (sampleRect.left + sampleWidth > mLiveWindow.getWidth()) {
sampleRect.left = mLiveWindow.getWidth() - sampleWidth;
sampleRect.top = (int) (event.getY() - sampleHeight / 2);
} else if (sampleRect.top + sampleHeight > mLiveWindow.getHeight()) {
sampleRect.top = mLiveWindow.getHeight() - sampleHeight;
return mStreamingContext.sampleColorFromCapturedVideoFrame(sampleRect);
```

## `effects-transforms-017` `initData`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneEffectView.java:139`

API classes: `NvsCaptureVideoFx`
Common calls: `getPackageUrl()`, `getInstance()`, `post()`, `getTag()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getBuiltinCaptureVideoFxName()`, `equals()`, `removeCaptureVideoFx()`, `containsKey()`, `getType()`, `findViewById()`

Simple sequence:

```java
(CaptureSceneOnlineData.CaptureSceneDetails) view.getTag();
int captureVideoFxCount = mStreamingContext.getCaptureVideoFxCount();
for (int i = 0; i < captureVideoFxCount; i++) {
NvsCaptureVideoFx captureVideoFxByIndex = mStreamingContext.getCaptureVideoFxByIndex(i);
if (captureVideoFxByIndex.getBuiltinCaptureVideoFxName().equals("Storyboard")) {
mStreamingContext.removeCaptureVideoFx(i);
MSBus.getInstance().post(SUB_CAPTURE_SCENE_PACKAGE, captureSceneDetails.getPackageUrl());
if (mType == Constants.CAPTURE_SCENE_TYPE_IMAGE) {
MSBus.getInstance().post(SUB_CAPTURE_SCENE_ITEM_CLICK_TYPE, captureSceneDetails.getPackageUrl());
if (!downloadingURL.containsKey(captureSceneDetails.getPackageUrl()) &&
captureSceneDetails.getType() == CAPTURE_SCENE_ONLINE) {
downloadingURL.put(captureSceneDetails.getPackageUrl(), "");
downloadImage(captureSceneDetails.getCoverUrl(), position);
downloadPackage(captureSceneDetails.getPackageUrl(), circleBarView, position);
setCaptureSceneByPath(captureSceneDetails.getId(), captureSceneDetails.getPackageUrl());
```

## `effects-transforms-018` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/view/CaptureSceneEffectView.java:144`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxByIndex()`, `getBuiltinCaptureVideoFxName()`, `equals()`, `removeCaptureVideoFx()`

Simple sequence:

```java
for (int i = 0; i < captureVideoFxCount; i++) {
NvsCaptureVideoFx captureVideoFxByIndex = mStreamingContext.getCaptureVideoFxByIndex(i);
if (captureVideoFxByIndex.getBuiltinCaptureVideoFxName().equals("Storyboard")) {
mStreamingContext.removeCaptureVideoFx(i);
```

## `effects-transforms-019` `removeAllFilterFx`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1239`

API classes: `NvsCaptureVideoFx`
Common calls: `equals()`, `add()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getBuiltinCaptureVideoFxName()`, `isEmpty()`, `size()`, `removeCaptureVideoFx()`, `get()`

Simple sequence:

```java
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx fx = mStreamingContext.getCaptureVideoFxByIndex(i);
String name = fx.getBuiltinCaptureVideoFxName();
for (int i = 0; i < remove_list.size(); i++) {
mStreamingContext.removeCaptureVideoFx(remove_list.get(i));
```

## `effects-transforms-020` `removeAllFilterFx`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1241`

API classes: `NvsCaptureVideoFx`
Common calls: `equals()`, `add()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getBuiltinCaptureVideoFxName()`

Simple sequence:

```java
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx fx = mStreamingContext.getCaptureVideoFxByIndex(i);
String name = fx.getBuiltinCaptureVideoFxName();
```

## `effects-transforms-021` `removeAllFilterFx`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1042`

API classes: `NvsTimeline`, `NvsTimelineVideoFx`
Common calls: `removeTimelineVideoFx()`, `getFirstTimelineVideoFx()`

Simple sequence:

```java
private void removeAllFilterFx(NvsTimeline timeline) {
NvsTimelineVideoFx nextFx = timeline.removeTimelineVideoFx(timeline.getFirstTimelineVideoFx());
while (nextFx != null) {
nextFx = timeline.removeTimelineVideoFx(nextFx);
```

## `effects-transforms-022` `readdFilterFx`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1056`

API classes: `NvsTimeline`
Common calls: `getName()`, `getInPoint()`, `size()`, `get()`, `getOutPoint()`, `equalsIgnoreCase()`, `addBuiltinTimelineVideoFx()`, `addPackagedTimelineVideoFx()`

Simple sequence:

```java
private void readdFilterFx(ArrayList<FilterFxInfo> filterInfos, NvsTimeline timeline) {
long inpoint = filterInfo.getInPoint();
long duration = filterInfo.getOutPoint() - filterInfo.getInPoint();
if (filterInfo.getName().equalsIgnoreCase("Video Echo"))
timeline.addBuiltinTimelineVideoFx(inpoint, duration, filterInfo.getName());
else {
timeline.addPackagedTimelineVideoFx(inpoint, duration, filterInfo.getName());
```

## `effects-transforms-023` `startFilterFx`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1340`

API classes: `NvsTimelineVideoFx`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setAddResult()`, `setName()`, `e()`, `getAsset()`, `getTimelineCurrentPosition()`, `getDuration()`, `setInPoint()`, `getAssetMode()`, `addBuiltinTimelineVideoFx()`, `getBuiltinTimelineVideoFxName()`, `addPackagedTimelineVideoFx()`, `getTimelineVideoFxPackageId()`

Simple sequence:

```java
NvAsset asset = assetItem.getAsset();
removeAllFilterFx(mTimeline);
long inPoint = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long duration = mTimeline.getDuration() - inPoint;
mCurFilterFxInfo.setInPoint(inPoint);
if (assetItem.getAssetMode() == AssetItem.ASSET_BUILTIN) {//内建数据类型
NvsTimelineVideoFx fx = mTimeline.addBuiltinTimelineVideoFx(inPoint, duration, asset.uuid);
if (fx != null) {
mCurFilterFxInfo.setName(fx.getBuiltinTimelineVideoFxName());
mCurFilterFxInfo.setAddResult(true);
mCurFilterFxInfo.setAddResult(false);
NvsTimelineVideoFx fx = mTimeline.addPackagedTimelineVideoFx(inPoint, duration, asset.uuid);
if (fx != null) {
mCurFilterFxInfo.setName(fx.getTimelineVideoFxPackageId());
mCurFilterFxInfo.setAddResult(true);
mCurFilterFxInfo.setAddResult(false);
int state = mStreamingContext.getStreamingEngineState();
if (state != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)
startPlay(mTimeline, getCurPlayPos());
```

## `effects-transforms-024` `removeAllTransition`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:1687`

API classes: `NvsVideoTrack`
Common calls: `getClipCount()`, `setBuiltinTransition()`

Simple sequence:

```java
public void removeAllTransition(NvsVideoTrack videoTrack) {
for (int i = 0; i < videoTrack.getClipCount(); i++) {
videoTrack.setBuiltinTransition(i, null);
```

## `effects-transforms-025` `information`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:548`

API classes: `NvsVideoClip`, `NvsVideoFx`
Common calls: `setFloatVal()`, `getVideoRes()`, `getHeight()`, `getVideoFx()`, `setSubType()`, `getVideoFxs()`, `add()`, `setTransX()`, `setTransY()`, `setScaleX()`, `setScaleY()`, `setRotation()`

Simple sequence:

```java
public void setVideoClipInfo(ClipInfo clipInfo, NvsVideoClip nvsVideoClip) {
if (mTimeline != null && mSelectClipInfo != null) {
float timelineHeight = mTimeline.getVideoRes().imageHeight;
float liveWindowHeight = mLiveWindow.getHeight();
mTransformVideoFx = mSelectClipInfo.getVideoFx(Constants.FX_TRANSFORM_2D);
mTransformVideoFx.setSubType(Constants.FX_TRANSFORM_2D);
mSelectClipInfo.getVideoFxs().add(mTransformVideoFx);
mTransformVideoFx.setTransX(0F);
mTransformVideoFx.setTransY(0F);
mTransformVideoFx.setScaleX(1.0F);
mTransformVideoFx.setScaleY(1.0F);
mTransformVideoFx.setRotation(0F);
NvsVideoFx videoFx = getTransformFx(mSelectNvsVideoClip, Constants.FX_TRANSFORM_2D);
videoFx.setAttachment(StoryboardInfo.SUB_TYPE_BACKGROUND, Constants.FX_TRANSFORM_2D);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_TRANS_X, 0F);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_TRANS_Y, 0F);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_SCALE_X, 1.0F);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_SCALE_Y, 1.0F);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_ROTATION, 0F);
```

## `effects-transforms-026` `setVideoClipInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:552`

API classes: `NvsVideoFx`
Common calls: `setFloatVal()`, `getVideoRes()`, `getHeight()`, `getVideoFx()`, `setSubType()`, `getVideoFxs()`, `add()`, `setTransX()`, `setTransY()`, `setScaleX()`, `setScaleY()`, `setRotation()`

Simple sequence:

```java
if (mTimeline != null && mSelectClipInfo != null) {
float timelineHeight = mTimeline.getVideoRes().imageHeight;
float liveWindowHeight = mLiveWindow.getHeight();
mTransformVideoFx = mSelectClipInfo.getVideoFx(Constants.FX_TRANSFORM_2D);
mTransformVideoFx.setSubType(Constants.FX_TRANSFORM_2D);
mSelectClipInfo.getVideoFxs().add(mTransformVideoFx);
mTransformVideoFx.setTransX(0F);
mTransformVideoFx.setTransY(0F);
mTransformVideoFx.setScaleX(1.0F);
mTransformVideoFx.setScaleY(1.0F);
mTransformVideoFx.setRotation(0F);
NvsVideoFx videoFx = getTransformFx(mSelectNvsVideoClip, Constants.FX_TRANSFORM_2D);
videoFx.setAttachment(StoryboardInfo.SUB_TYPE_BACKGROUND, Constants.FX_TRANSFORM_2D);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_TRANS_X, 0F);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_TRANS_Y, 0F);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_SCALE_X, 1.0F);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_SCALE_Y, 1.0F);
videoFx.setFloatVal(Constants.FX_TRANSFORM_2D_ROTATION, 0F);
```

## `effects-transforms-027` `getTransformFx`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:591`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `getFxCount()`, `getFxByIndex()`, `getAttachment()`, `equals()`

Simple sequence:

```java
public NvsVideoFx getTransformFx(NvsVideoClip videoClip, String type) {
int fxCount = videoClip.getFxCount();
for (int index = 0; index < fxCount; index++) {
NvsVideoFx clipFx = videoClip.getFxByIndex(index);
Object attachment = clipFx.getAttachment(StoryboardInfo.SUB_TYPE_BACKGROUND);
```

## `effects-transforms-028` `getTransformFx`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:593`

API classes: `NvsVideoFx`
Common calls: `getFxByIndex()`, `getAttachment()`, `equals()`

Simple sequence:

```java
for (int index = 0; index < fxCount; index++) {
NvsVideoFx clipFx = videoClip.getFxByIndex(index);
Object attachment = clipFx.getAttachment(StoryboardInfo.SUB_TYPE_BACKGROUND);
```

## `effects-transforms-029` `setEffectByPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1111`

API classes: `NvsTimelineVideoFx`, `NvsVideoFx`
Static/constants: `NvsVideoFx.VIDEOFX_TYPE_BUILTIN`
Common calls: `setRegion()`, `setFilterIntensity()`, `equals()`, `setIntensity()`, `setDesc()`, `setType()`, `valueOf()`, `instance()`, `setTimelineVideoFx()`, `addBuiltinTimelineVideoFx()`, `getDuration()`, `setRegional()`

Simple sequence:

```java
setPointFListLiveWindow(mLiveWindow.getWidth(), mLiveWindow.getHeight());
if (mTimeline == null) {
if (mDrawRect != null) {
mDrawRect.setPicturePath("");
NvsTimelineVideoFx timelineVideoFx = mTimeline.getFirstTimelineVideoFx();
while (timelineVideoFx != null) {
if (timelineVideoFx.getTimelineVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN) {
String fxName = timelineVideoFx.getBuiltinTimelineVideoFxName();
timelineVideoFx.setFilterIntensity(0);
timelineVideoFx.setFilterIntensity(1);
timelineVideoFx = mTimeline.getNextTimelineVideoFx(timelineVideoFx);
if (type == EffectItemData.TYPE_MOSAIC) {
nvsTimelineVideoFx = mTimeline.addBuiltinTimelineVideoFx(0, mTimeline.getDuration(), MOSAICNAME);
nvsTimelineVideoFx.setRegional(true);
nvsTimelineVideoFx.setRegionalFeatherWidth(0f);
nvsTimelineVideoFx.setFloatVal("Unit Size", 0.1f);
nvsTimelineVideoFx.setFilterIntensity(1);
nvsTimelineVideoFx.setRegion(fx);
mVideoFx.setRegion(fx);
mVideoFx.setIntensity(1);
mVideoFx.setUnitSize(0.1f);
mVideoFx.setDesc(MOSAICNAME);
mVideoFx.setType(String.valueOf(type));
nvsTimelineVideoFx = mTimeline.addBuiltinTimelineVideoFx(0, mTimeline.getDuration(), BLURNAME);
// ... 25 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-030` `setDrawRectByEffectData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1207`

API classes: `NvsTimelineVideoFx`
Common calls: `add()`, `mapNormalizedToView()`, `getRegion()`, `setDrawRect()`

Simple sequence:

```java
private void setDrawRectByEffectData(NvsTimelineVideoFx videoFx, int type) {
float[] region = videoFx.getRegion();
pointFS.add(mLiveWindow.mapNormalizedToView(new PointF(region[0], region[1])));
pointFS.add(mLiveWindow.mapNormalizedToView(new PointF(region[2], region[3])));
pointFS.add(mLiveWindow.mapNormalizedToView(new PointF(region[4], region[5])));
pointFS.add(mLiveWindow.mapNormalizedToView(new PointF(region[6], region[7])));
mDrawRect.setDrawRect(pointFS, type);
```

## `effects-transforms-031` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1876`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.PlaybackCallback`, `NvsStreamingContext.PlaybackCallback2`, `NvsStreamingContext.StreamingEngineCallback`, `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.HardwareErrorCallback`, `NvsStreamingContext.WebCallback`
Common calls: `setVisibility()`, `setBackgroundResource()`, `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `sendEmptyMessage()`, `playBackEOF()`, `setPlaybackCallback2()`, `PlaybackCallback2()`, `playbackTimelinePosition()`, `setStreamingEngineCallback()`, `StreamingEngineCallback()`

Simple sequence:

```java
if (mStreamingContext == null || mTimeline == null || mLiveWindow == null)
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {
if (cur_position - mPlayStartFlag >= 4000000)
mPlayBarLayout.setVisibility(View.INVISIBLE);
mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {
if (i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mPlayImage.setBackgroundResource(R.mipmap.icon_edit_pause);
mPlayImage.setBackgroundResource(R.mipmap.icon_edit_play);
mPlayBarLayout.setVisibility(mPlayBarVisibleState ? View.VISIBLE : View.GONE);
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
mStreamingContext.setHardwareErrorCallback(new NvsStreamingContext.HardwareErrorCallback() {
mStreamingContext.setWebCallback(new NvsStreamingContext.WebCallback() {
mVideoLoading.setVisibility(isWaiting ? View.VISIBLE : View.GONE);
mStreamingContext.connectTimelineWithLiveWindow(mTimeline, mLiveWindow);
```

## `effects-transforms-032` `setStreamingEngineCallback`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1929`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `setVisibility()`

Simple sequence:

```java
if (i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mPlayImage.setBackgroundResource(R.mipmap.icon_edit_pause);
mPlayImage.setBackgroundResource(R.mipmap.icon_edit_play);
mPlayBarLayout.setVisibility(mPlayBarVisibleState ? View.VISIBLE : View.GONE);
```

## `effects-transforms-033` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:2063`

API classes: `NvsStreamingContext`, `NvsRational`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`, `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_SPEED_COMP_MODE`
Common calls: `playbackTimeline()`, `instance()`, `getCompileVideoRes()`

Simple sequence:

```java
int flag = NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_SPEED_COMP_MODE;
int compileHeight = settingValues.getCompileVideoRes();
if (compileHeight == SettingActivity.CompileVideoRes_2160) {
NvsRational nvsRational = new NvsRational(1, 2);
if (mPlayFlag == 0) {
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, nvsRational, true, flag);
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, nvsRational, true, mPlayFlag | flag);
if (mPlayFlag == 0) {
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, flag);
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, mPlayFlag | flag);
```

## `effects-transforms-034` `initAnimationViewList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:414`

API classes: `NvsVideoFx`
Common calls: `get()`, `putInt()`, `setAnimationDuration()`, `getInstance()`, `setFloatVal()`, `setFunctionListener()`, `OnFunctionListener()`, `getPackageId()`, `setSelectedProgress()`, `containsKey()`, `remove()`, `setVisibility()`

Simple sequence:

```java
mAnimationBottomView.setFunctionListener(new AnimationBottomView.OnFunctionListener() {
String mAnimationId = filterItem.getPackageId();
mAnimationBottomView.setSelectedProgress(value);
mAnimationClipAdapter.setAnimationDuration(mSelectedClipPosition, value, mAssetType);
mAnimationBottomView.setVisibility(View.GONE);
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(), AssetDownloadActivity.class, bundle, ANIMATION_REQUESTLIST);
NvsVideoFx animationVideoFx = mNvsVideoFxMap.get(mSelectedClipPosition);
animationVideoFx.setExprVar("amplitude", amplitude);
animationVideoFx.setFloatVal("Package Effect In", duration - progress);
animationVideoFx.setFloatVal("Package Effect Out", progress);
mAnimationClipAdapter.setAnimationDuration(mSelectedClipPosition, progress, mAssetType);
```

## `effects-transforms-035` `initAnimationViewList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:415`

API classes: `NvsVideoFx`
Common calls: `get()`, `putInt()`, `setAnimationDuration()`, `getInstance()`, `setFloatVal()`, `setFunctionListener()`, `OnFunctionListener()`, `getPackageId()`, `setSelectedProgress()`, `containsKey()`, `remove()`, `setVisibility()`

Simple sequence:

```java
mAnimationBottomView.setFunctionListener(new AnimationBottomView.OnFunctionListener() {
String mAnimationId = filterItem.getPackageId();
mAnimationBottomView.setSelectedProgress(value);
mAnimationClipAdapter.setAnimationDuration(mSelectedClipPosition, value, mAssetType);
mAnimationBottomView.setVisibility(View.GONE);
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(), AssetDownloadActivity.class, bundle, ANIMATION_REQUESTLIST);
NvsVideoFx animationVideoFx = mNvsVideoFxMap.get(mSelectedClipPosition);
animationVideoFx.setExprVar("amplitude", amplitude);
animationVideoFx.setFloatVal("Package Effect In", duration - progress);
animationVideoFx.setFloatVal("Package Effect Out", progress);
mAnimationClipAdapter.setAnimationDuration(mSelectedClipPosition, progress, mAssetType);
```

## `effects-transforms-036` `appendAnimationFxToVideoPackage`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:569`

API classes: `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoFx`
Common calls: `i()`, `getPackageId()`, `put()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `enablePropertyVideoFx()`, `containsKey()`, `get()`, `getPropertyVideoFx()`, `isEmpty()`, `getOutPoint()`, `getInPoint()`

Simple sequence:

```java
NvsVideoTrack nvsVideoTrack = mTimeline.getVideoTrackByIndex(0);
if (nvsVideoTrack == null) {
Log.i(TAG, "timeline get video track is null");
NvsVideoClip nvsVideoClip = nvsVideoTrack.getClipByIndex(clipPosition);
if (nvsVideoClip == null) {
Log.i(TAG, "timeline get video clip is null");
NvsVideoFx mPositionerVideoFx;
mPositionerVideoFx = nvsVideoClip.getPropertyVideoFx();
if (TextUtils.isEmpty(filterItem.getPackageId())) {
if (mAssetType == NvAsset.ASSET_ANIMATION_OUT) {
long clipDuration = nvsVideoClip.getOutPoint() - nvsVideoClip.getInPoint();
animationInfo.setmPackageId(filterItem.getPackageId());
animationInfo.setPostPackage(filterItem.isPostPackage());
mPositionerVideoFx = TimelineUtil.applyAnimation(nvsVideoTrack, nvsVideoClip, animationInfo);
```

## `effects-transforms-037` `updateBackground`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:174`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `applyBackground()`, `getBackGroundInfo()`

Simple sequence:

```java
public void updateBackground(ClipInfo clipInfo, int position, NvsTimeline timeline) {
NvsVideoTrack videoTrackByIndex = timeline.getVideoTrackByIndex(0);
NvsVideoClip clipByIndex = videoTrackByIndex.getClipByIndex(position);
TimelineUtil.applyBackground(clipByIndex, clipInfo.getBackGroundInfo());
```

## `effects-transforms-038` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:202`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `effects-transforms-039` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:207`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `effects-transforms-040` `setOnItemClickListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:235`

API classes: `NvsVideoTrack`
Common calls: `size()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `get()`, `getVisibility()`, `setSelectColor()`, `setVideoClipInfo()`, `setTransformViewVisible()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
if (videoTrack != null) {
mCurrentNvsVideoClip = videoTrack.getClipByIndex(position);
if (mBackgroundBottomView != null && mBackgroundBottomView.getVisibility() == View.VISIBLE) {
mBackgroundBottomView.setSelectColor(mCurrentClipInfo);
mVideoFragment.setVideoClipInfo(mCurrentClipInfo, mCurrentNvsVideoClip);
mVideoFragment.setTransformViewVisible(View.VISIBLE);
```

## `effects-transforms-041` `onColorApplyAll`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:387`

API classes: `NvsVideoTrack`
Common calls: `size()`, `getBackGroundInfo()`, `isEmpty()`, `getVideoTrackByIndex()`, `instance()`, `getClipInfoData()`, `get()`, `buildBackgroundInfo()`, `getType()`, `setColorValue()`, `getColorValue()`, `getClipByIndex()`

Simple sequence:

```java
if (mTimeline == null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
ArrayList<ClipInfo> clipInfoData = TimelineData.instance().getClipInfoData();
BackGroundInfo backGroundInfo = mCurrentClipInfo.getBackGroundInfo();
if (backGroundInfo != null) {
clipInfo.buildBackgroundInfo(backGroundInfo.getType());
clipInfo.getBackGroundInfo().setColorValue(backGroundInfo.getColorValue());
updateBackground(clipInfo, videoTrack.getClipByIndex(i));
```

## `effects-transforms-042` `onBlurApplyAll`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:420`

API classes: `NvsVideoTrack`
Common calls: `size()`, `getBackGroundInfo()`, `getVideoTrackByIndex()`, `instance()`, `getClipInfoData()`, `get()`, `buildBackgroundInfo()`, `getType()`, `setValue()`, `getValue()`, `getClipByIndex()`

Simple sequence:

```java
if (mTimeline == null) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
ArrayList<ClipInfo> clipInfoData = TimelineData.instance().getClipInfoData();
BackGroundInfo backGroundInfo = mCurrentClipInfo.getBackGroundInfo();
if (backGroundInfo != null) {
clipInfo.buildBackgroundInfo(backGroundInfo.getType());
clipInfo.getBackGroundInfo().setValue(backGroundInfo.getValue());
updateBackground(clipInfo, videoTrack.getClipByIndex(i));
```

## `effects-transforms-043` `getClipStartTime`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:546`

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

## `effects-transforms-044` `getClipEndTime`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:568`

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

## `effects-transforms-045` `setDefaultBackground`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/BackgroundActivity.java:600`

API classes: `NvsVideoClip`
Common calls: `buildBackgroundInfo()`, `setColorValue()`, `applyBackground()`, `getBackGroundInfo()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
public void setDefaultBackground(ClipInfo clipInfo, NvsVideoClip videoClip) {
backGroundInfo.setColorValue("#000000");
TimelineUtil.applyBackground(videoClip, clipInfo.getBackGroundInfo());
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), 0);
```

## `effects-transforms-046` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:288`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_SPEED_COMP_MODE`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
int flag = NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_SPEED_COMP_MODE;
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, flag);
```

## `effects-transforms-047` `connectTimelineWithLiveWindow`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/SingleClipFragment.java:297`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.PlaybackCallback`, `NvsStreamingContext.PlaybackCallback2`, `NvsStreamingContext.StreamingEngineCallback`, `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `setPlaybackCallback()`, `PlaybackCallback()`, `playStopped()`, `sendEmptyMessage()`, `playBackEOF()`, `setPlaybackCallback2()`, `PlaybackCallback2()`, `playbackTimelinePosition()`, `setStreamingEngineCallback()`, `StreamingEngineCallback()`, `streamingEngineStateChanged()`

Simple sequence:

```java
if (mStreamingContext == null || mTimeline == null || mLiveWindow == null)
mStreamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
public void onPlaybackPreloadingCompletion(NvsTimeline nvsTimeline) {
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
public void onPlaybackEOF(NvsTimeline nvsTimeline) {
mStreamingContext.setPlaybackCallback2(new NvsStreamingContext.PlaybackCallback2() {
public void onPlaybackTimelinePosition(NvsTimeline nvsTimeline, long l) {
mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {
if (i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mPlayImage.setBackgroundResource(R.mipmap.icon_edit_pause);
mPlayImage.setBackgroundResource(R.mipmap.icon_edit_play);
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
mLiveWindow.setOnClickListener(new View.OnClickListener() {
mStreamingContext.connectTimelineWithLiveWindow(mTimeline, mLiveWindow);
mPlaySeekBar.setMax((int) (mTimeline.getDuration() / BASE_VALUE));
```

## `effects-transforms-048` `getInitCutData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:140`

API classes: `NvsConstants`, `NvsVideoFx`, `NvsVideoClip`
Static/constants: `NvsConstants.KEY_MASK_GENERATOR_TYPE`, `NvsConstants.CUT_KEY_MASK_GENERATOR`, `NvsConstants.KEY_MASK_GENERATOR_SIGN_CROP`, `NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D`, `NvsConstants.KEY_CROPPER_TRANS_X`, `NvsConstants.KEY_CROPPER_TRANS_Y`, `NvsConstants.KEY_CROPPER_SCALE_X`, `NvsConstants.KEY_CROPPER_SCALE_Y`, `NvsConstants.KEY_CROPPER_ROTATION`, `NvsConstants.AspectRatio`
Common calls: `putTransformData()`, `getFloatVal()`, `equals()`, `getRawFxByIndex()`, `getBuiltinVideoFxName()`, `setRatio()`, `get()`, `getCropInfo()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getRawFxCount()`, `getAttachment()`

Simple sequence:

```java
CutData cutData = mClipArrayList.get(mCurClipIndex).getCropInfo();
```

## `effects-transforms-049` `onItemClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:273`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setFloatVal()`, `reset()`, `setProgress()`, `setPanAndScan()`, `getCurrentEngineState()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mCuttingMenuView.setProgress(0);
mVideoClip.setPanAndScan(0.0f, 0.0f);
mVideoFx.setFloatVal(Constants.FX_TRANSFORM_2D_SCALE_X, mScaleX);
mVideoFx.setFloatVal(Constants.FX_TRANSFORM_2D_SCALE_Y, mScaleY);
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `effects-transforms-050` `onVertical`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:293`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `effects-transforms-051` `onRotation`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:303`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `effects-transforms-052` `onHorizontal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:313`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `effects-transforms-053` `adjustClip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:345`

API classes: `NvsVideoFx`
Common calls: `getFxByIndex()`, `getBuiltinVideoFxName()`, `compareTo()`

Simple sequence:

```java
for (int index = 0; index < fxCount; ++index) {
NvsVideoFx videoFx = mVideoClip.getFxByIndex(index);
if (videoFx.getBuiltinVideoFxName().compareTo(Constants.FX_TRANSFORM_2D) == 0) {
```

## `effects-transforms-054` `onPlaybackPreloadingCompletion`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:151`

API classes: `NvsTimeline`
Common calls: `playStopped()`

Simple sequence:

```java
public void onPlaybackStopped(NvsTimeline nvsTimeline) {
```

## `effects-transforms-055` `onPlaybackTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:172`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.SeekingCallback`
Common calls: `setSeekingCallback()`, `SeekingCallback()`

Simple sequence:

```java
mStreamingContext.setSeekingCallback(new NvsStreamingContext.SeekingCallback() {
public void onSeekingTimelinePosition(NvsTimeline nvsTimeline, long cur_position) {
```

## `effects-transforms-056` `onSeekingTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:178`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.StreamingEngineCallback`, `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `setStreamingEngineCallback()`, `StreamingEngineCallback()`

Simple sequence:

```java
mStreamingContext.setStreamingEngineCallback(new NvsStreamingContext.StreamingEngineCallback() {
if (i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mPlayButtonImage.setBackgroundResource(R.mipmap.icon_pause);
mPlayButtonImage.setBackgroundResource(R.mipmap.icon_play);
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
```

## `effects-transforms-057` `onCreateView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:198`

API classes: `NvsLiveWindow`
Static/constants: `NvsLiveWindow.FILLMODE_PRESERVEASPECTCROP`
Common calls: `findViewById()`, `inflate()`, `setFillMode()`, `setVisibility()`, `getSystemService()`

Simple sequence:

```java
mLiveWindow = rootView.findViewById(R.id.liveWindow);
mLiveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTCROP);
if (IS_DEBUG) {
mTestView.setVisibility(View.VISIBLE);
mVibrator = (Vibrator) getActivity().getSystemService(Context.VIBRATOR_SERVICE);
```

## `effects-transforms-058` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:221`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `onPlayStateChanged()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mTimeline == null) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
```

## `effects-transforms-059` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:222`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getTimelineCurrentPosition()`, `onPlayStateChanged()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mTimeline == null) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
```

## `effects-transforms-060` `setOnSeekBarChangeListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:245`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`

Simple sequence:

```java
seekTimeline(currentTime, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
```

## `effects-transforms-061` `setLiveWindowRatio`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1040`

API classes: `NvsConstants`
Static/constants: `NvsConstants.AspectRatio`

Simple sequence:

```java
if (ratio == NvsConstants.AspectRatio.AspectRatio_NoFitRatio) {
```

## `effects-transforms-062` `updateRegionData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1283`

API classes: `NvsConstants`
Static/constants: `NvsConstants.AspectRatio`
Common calls: `setWidthHeightRatio()`, `onSizeChanged()`

Simple sequence:

```java
if (ratio == NvsConstants.AspectRatio.AspectRatio_NoFitRatio) {
mCutView.setWidthHeightRatio(-1);
mCutView.setWidthHeightRatio(size.x * 1.0F / size.y);
```

## `effects-transforms-063` `onDetach`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1349`

API classes: `NvsTimeline`

Simple sequence:

```java
public void setTimeLine(NvsTimeline timeline) {
mTimeline = timeline;
```

## `effects-transforms-064` `playVideoButtonClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1366`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
mStreamingContext.playbackTimeline(mTimeline, startTime, endTime, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `effects-transforms-065` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1370`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `playbackTimeline()`

Simple sequence:

```java
mStreamingContext.playbackTimeline(mTimeline, mStartTime, mStartTime + getDuration(), NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, 0);
```

## `effects-transforms-066` `playVideoFromStartPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1375`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `seekTimeline()`

Simple sequence:

```java
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, seekShowMode);
```

## `effects-transforms-067` `getTimeLine`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/CutVideoFragment.java:1395`

API classes: `NvsConstants`
Static/constants: `NvsConstants.AspectRatio`

Simple sequence:

```java
if (mRatio == NvsConstants.AspectRatio.AspectRatio_NoFitRatio) {
```

## `effects-transforms-068` `initColorAdjustVideoFx`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:275`

API classes: `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoFx`
Common calls: `equals()`, `appendBuiltinFx()`, `setAttachment()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getFxCount()`, `getFxByIndex()`, `getBuiltinVideoFxName()`, `isEmpty()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
int fxCount = videoClip.getFxCount();
for (int index = 0; index < fxCount; ++index) {
NvsVideoFx videoFx = videoClip.getFxByIndex(index);
String fxName = videoFx.getBuiltinVideoFxName();
mColorVideoFx.setAttachment(Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST, Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
mVignetteVideoFx.setAttachment(Constants.ADJUST_TYPE_VIGETTE, Constants.ADJUST_TYPE_VIGETTE);
mSharpenVideoFx.setAttachment(Constants.ADJUST_TYPE_SHARPEN, Constants.ADJUST_TYPE_SHARPEN);
mTintVideoFx.setAttachment(Constants.ADJUST_TYPE_TINT, Constants.ADJUST_TYPE_TINT);
mDenoiseVideoFx.setAttachment(Constants.ADJUST_TYPE_DENOISE, Constants.ADJUST_TYPE_DENOISE);
```

## `effects-transforms-069` `onLoadFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:288`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `setVideoFragmentCallBack()`, `VideoFragmentListener()`, `d()`

Simple sequence:

```java
mClipFragment.setVideoFragmentCallBack(new SingleClipFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
mPlayBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
mPlayBtn.setBackgroundResource(R.mipmap.icon_edit_play);
```

## `effects-transforms-070` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:338`

API classes: `NvsTimeline`
Common calls: `getVisibility()`, `isEmpty()`, `upDataPlayProgress()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if(changeSpeedCurveView.getVisibility() ==View.VISIBLE){
```

## `effects-transforms-071` `changeSpeed`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:477`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `changeSpeed()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
videoClip.changeSpeed(speed,keepAudioPitch);
```

## `effects-transforms-072` `changeSpeedForCurve`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:496`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `changeCurvesVariableSpeed()`, `e()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
boolean isSucess = videoClip.changeCurvesVariableSpeed(speed, true);
```

## `effects-transforms-073` `getClipDuration`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:556`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `getTrimOut()`, `getTrimIn()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
return videoClip.getTrimOut() - videoClip.getTrimIn();
```

## `effects-transforms-074` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:580`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `playVideo()`, `getTrimOut()`

Simple sequence:

```java
if(null != mClipFragment){
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
mClipFragment.playVideo(start,videoClip.getTrimOut());
```

## `effects-transforms-075` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:581`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `playVideo()`, `getTrimOut()`

Simple sequence:

```java
if(null != mClipFragment){
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
mClipFragment.playVideo(start,videoClip.getTrimOut());
```

## `effects-transforms-076` `getTimelinePositionFromClipPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:611`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `GetTimelinePosByClipPosCurvesVariableSpeed()`, `getTrimIn()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
long timelinePosition = videoClip.GetTimelinePosByClipPosCurvesVariableSpeed(timestamp) + videoClip.getTrimIn();
```

## `effects-transforms-077` `getClipPositionFromTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:629`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipByIndex()`, `GetClipPosByTimelinePosCurvesVariableSpeed()`, `getTrimIn()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(0);
long bzPosition = videoClip.GetClipPosByTimelinePosCurvesVariableSpeed(timelinePosition) - videoClip.getTrimIn();
```

## `effects-transforms-078` `updateVolumeRelativeView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:553`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`
Common calls: `setEnabled()`, `get()`, `setText()`, `setTextColor()`, `getColor()`, `setCompoundDrawablesWithIntrinsicBounds()`, `getDrawable()`, `size()`, `getVolumeByKeyTime()`, `getString()`, `formatUsToString2()`, `clear()`

Simple sequence:

```java
for (Map.Entry<Long, VolumeKeyInfo> entry : entries) {
keyMap.put(entry.getKey(), new KeyFrameInfo());
timelineTimeSpan.setCurrentTimelinePosition(timeStamp, keyMap);
double volume = TimelineUtil.getVolumeByKeyTime(videoClip, timeStamp);
lastFrame.setEnabled(hasPre);
nextFrame.setEnabled(hasNext);
addOrDeleteFrame.setText(getResources().getString(R.string.key_frame_delete_frame_text));
mTvKeyFrame.setEnabled(false);
mTvKeyFrame.setTextColor(getResources().getColor(R.color.white_20));
mTvKeyFrame.setCompoundDrawablesWithIntrinsicBounds(ContextCompat.getDrawable(this, R.mipmap.icon_curve_adjust_disable), null, null, null);
if (hasNext && hasPre) {
mTvKeyFrame.setEnabled(true);
mTvKeyFrame.setCompoundDrawablesWithIntrinsicBounds(ContextCompat.getDrawable(this, R.mipmap.icon_curve_adjust), null, null, null);
mTvKeyFrame.setTextColor(getResources().getColor(R.color.white));
mTvKeyFrame.setEnabled(false);
mTvKeyFrame.setTextColor(getResources().getColor(R.color.white_20));
mTvKeyFrame.setCompoundDrawablesWithIntrinsicBounds(ContextCompat.getDrawable(this, R.mipmap.icon_curve_adjust_disable), null, null, null);
addOrDeleteFrame.setText(getResources().getString(R.string.key_frame_add_frame_text));
double volume = TimelineUtil.getVolumeByKeyTime(videoClip, timeStamp);
mTvKeyFrame.setEnabled(true);
llKeyFrame.setVisibility(View.GONE);
tvCurTime.setText(TimeFormatUtil.formatUsToString2(timeStamp) + "/" + TimeFormatUtil.formatUsToString2(mTimeline.getDuration()));
if (mTimeline != null) {
mClipFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
```

## `effects-transforms-079` `onLoadFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:767`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `setVideoFragmentCallBack()`, `VideoFragmentListener()`, `d()`

Simple sequence:

```java
mClipFragment.setVideoFragmentCallBack(new SingleClipFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
mPlayBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
mPlayBtn.setBackgroundResource(R.mipmap.icon_edit_play);
```

## `effects-transforms-080` `getFilterColorParam`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/data/FilterItem.java:262`

API classes: `NvsColor`
Common calls: `put()`

Simple sequence:

```java
public void setFilterColorParam(String key, NvsColor value) {
```

## `effects-transforms-081` `setName`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/data/mask/MaskInfoData.java:344`

API classes: `NvsMaskRegionInfo`

Simple sequence:

```java
public NvsMaskRegionInfo getMaskRegionInfo() {
```

## `effects-transforms-082` `getMaskRegionInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/data/mask/MaskInfoData.java:348`

API classes: `NvsMaskRegionInfo`

Simple sequence:

```java
public void setMaskRegionInfo(NvsMaskRegionInfo maskRegionInfo) {
```

## `effects-transforms-083` `getLocalData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:241`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
Common calls: `putInt()`, `seekTimeline()`, `getTimelineCurrentPosition()`, `getLayoutParams()`, `beginTransaction()`, `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `setTimeline()`, `setPlayFlag()`, `putBoolean()`, `instance()`, `getMakeRatio()`

Simple sequence:

```java
mVideoFragment.setFragmentLoadFinisedListener(new VideoFragment.OnFragmentLoadFinisedListener() {
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), 0);
mVideoFragment.setTimeline(mTimeline);
mVideoFragment.setPlayFlag(NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
bundle.putInt("titleHeight", mTitleBar.getLayoutParams().height);
bundle.putInt("bottomHeight", mBottomLayout.getLayoutParams().height);
bundle.putInt("ratio", TimelineData.instance().getMakeRatio());
mVideoFragment.setArguments(bundle);
mVideoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
if (timeline.getDuration() - mStreamingContext.getTimelineCurrentPosition(mTimeline) <= 40000) {
mVideoFragment.seekTimeline(0, 0);
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
playbackTimelinePositionFromParent(timeline, stamp);
```

## `effects-transforms-084` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:276`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
playbackTimelinePositionFromParent(timeline, stamp);
```

## `effects-transforms-085` `streamingEngineStateChangedFromParent`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:290`

API classes: `NvsTimeline`

Simple sequence:

```java
protected void playbackTimelinePositionFromParent(NvsTimeline timeline, long stamp) {
```

## `effects-transforms-086` `playbackTimelinePositionFromParent`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:293`

API classes: `NvsStreamingContext`, `NvsColor`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setIntensityLayoutVisible()`, `setFxMode()`, `setFxId()`, `setVisibility()`, `playVideoButtonClick()`, `setIntensitySeekBarProgress()`, `setIsAdjusted()`, `getIsAdjusted()`, `setFxIntensity()`, `getStreamingEngineState()`, `setSelectedPos()`, `setIntensityTextVisible()`

Simple sequence:

```java
mFilterView.setFilterArrayList(mFilterItemArrayList);
mSelectedPos = AssetFxUtil.getSelectedFilterPos(mFilterItemArrayList, mVideoClipFxInfo);
mFilterView.setIntensityLayoutVisible(mSelectedPos <= 0 ? View.INVISIBLE : View.VISIBLE);
mFilterView.setIntensityTextVisible(View.VISIBLE);
mFilterView.setIntensitySeekBarMaxValue(100);
mFilterView.setFilterFxListBackgroud("#00000000");
mFilterView.setFilterListener(new FilterView.OnFilterListener() {
final int currentSelectedPos = mFilterView.getSelectedPos();
if (mVideoClipFxInfo.getKeyFrameInfoMap().isEmpty()) {
mFilterView.setIntensitySeekBarProgress(100);
if (null != mAdjustSpecialEffectsView) {
mAdjustSpecialEffectsView.setVisibility(View.GONE);
mFilterView.setIntensityLayoutVisible(View.INVISIBLE);
mVideoClipFxInfo.setFxMode(VideoClipFxInfo.FXMODE_BUILTIN);
mVideoClipFxInfo.setFxId(null);
String packageId = filterItem.getPackageId();
if ((null != mAdjustSpecialEffectsView) && isAdjust) {
mVideoClipFxInfo.setIsAdjusted(filterItem.getIsAdjusted());
mAdjustSpecialEffectsView.setVisibility(View.VISIBLE);
mFilterView.setIntensitySeekBarVisibility(View.GONE);
if (mAdjustSpecialEffectsView != null) {
mAdjustSpecialEffectsView.setVisibility(View.GONE);
mFilterView.setIntensitySeekBarVisibility(View.VISIBLE);
if (isNeedShowSeekBarWhenChangeFilterFromParent()) {
// ... 58 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-087` `onIntensity`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:441`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getStreamingEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), 0);
```

## `effects-transforms-088` `streamingEngineStateChangedFromParent`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:130`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING`
Common calls: `setSequenceViewIsSeekingStatus()`

Simple sequence:

```java
if (state != NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING) {
mFilterKeyFrameView.setSequenceViewIsSeekingStatus(false);
```

## `effects-transforms-089` `initKeyFrameView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:137`

API classes: `NvsFx`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`, `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER`, `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE`
Common calls: `getKeyFrameInfoMap()`, `putKeyFrameInfo()`, `getTimelineCurrentPosition()`, `updateKeyFramePointView()`, `seekTimeline()`, `findKeyframeTime()`, `setNextViewEnable()`, `setSequenceViewIsSeekingStatus()`, `scrollSequenceViewTo()`, `setBeforeViewEnable()`, `setOnKeyFrameViewClickListener()`, `OnKeyFrameViewClickListener()`

Simple sequence:

```java
mFilterKeyFrameView.setOnKeyFrameViewClickListener(new FilterKeyFrameView.OnKeyFrameViewClickListener() {
mStreamingContext.stop();
mVideoClipFxInfo.putKeyFrameInfo(mStreamingContext.getTimelineCurrentPosition(mTimeline), getFxIntensityAndApplyKeyFrame());
mFilterKeyFrameView.updateKeyFramePointView(mVideoClipFxInfo.getKeyFrameInfoMap());
NvsFx fxFromClip = getFxFromClip();
if (fxFromClip != null) {
long nextKeyFrame = fxFromClip.findKeyframeTime(FILTER_INTENSITY, mStreamingContext.getTimelineCurrentPosition(mTimeline),
NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER);
if (nextKeyFrame == -1) {
mFilterKeyFrameView.setNextViewEnable(false);
mFilterKeyFrameView.setNextViewEnable(true);
mFilterKeyFrameView.setSequenceViewIsSeekingStatus(true);
mStreamingContext.seekTimeline(mTimeline, nextKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);
NvsFx fxFromClip = getFxFromClip();
if (fxFromClip != null) {
long beforeKeyFrame = fxFromClip.findKeyframeTime(FILTER_INTENSITY, mStreamingContext.getTimelineCurrentPosition(mTimeline),
NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE);
if (beforeKeyFrame == -1) {
mFilterKeyFrameView.setBeforeViewEnable(false);
mFilterKeyFrameView.setBeforeViewEnable(true);
mFilterKeyFrameView.setSequenceViewIsSeekingStatus(true);
mStreamingContext.seekTimeline(mTimeline, beforeKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);
NvsFx fxFromClip = getFxFromClip();
if (fxFromClip != null) {
// ... 6 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-090` `nextFrameClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:148`

API classes: `NvsFx`, `NvsStreamingContext`
Static/constants: `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `setNextViewEnable()`, `findKeyframeTime()`, `getTimelineCurrentPosition()`, `setSequenceViewIsSeekingStatus()`, `seekTimeline()`, `scrollSequenceViewTo()`

Simple sequence:

```java
if (fxFromClip != null) {
long nextKeyFrame = fxFromClip.findKeyframeTime(FILTER_INTENSITY, mStreamingContext.getTimelineCurrentPosition(mTimeline),
NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER);
if (nextKeyFrame == -1) {
mFilterKeyFrameView.setNextViewEnable(false);
mFilterKeyFrameView.setNextViewEnable(true);
mFilterKeyFrameView.setSequenceViewIsSeekingStatus(true);
mStreamingContext.seekTimeline(mTimeline, nextKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);
```

## `effects-transforms-091` `nextFrameClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:151`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `setNextViewEnable()`, `setSequenceViewIsSeekingStatus()`, `seekTimeline()`, `scrollSequenceViewTo()`

Simple sequence:

```java
if (nextKeyFrame == -1) {
mFilterKeyFrameView.setNextViewEnable(false);
mFilterKeyFrameView.setNextViewEnable(true);
mFilterKeyFrameView.setSequenceViewIsSeekingStatus(true);
mStreamingContext.seekTimeline(mTimeline, nextKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);
```

## `effects-transforms-092` `beforeFrameClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:163`

API classes: `NvsFx`, `NvsStreamingContext`
Static/constants: `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `setBeforeViewEnable()`, `findKeyframeTime()`, `getTimelineCurrentPosition()`, `setSequenceViewIsSeekingStatus()`, `seekTimeline()`, `scrollSequenceViewTo()`

Simple sequence:

```java
NvsFx fxFromClip = getFxFromClip();
if (fxFromClip != null) {
long beforeKeyFrame = fxFromClip.findKeyframeTime(FILTER_INTENSITY, mStreamingContext.getTimelineCurrentPosition(mTimeline),
NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE);
if (beforeKeyFrame == -1) {
mFilterKeyFrameView.setBeforeViewEnable(false);
mFilterKeyFrameView.setBeforeViewEnable(true);
mFilterKeyFrameView.setSequenceViewIsSeekingStatus(true);
mStreamingContext.seekTimeline(mTimeline, beforeKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);
```

## `effects-transforms-093` `beforeFrameClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:165`

API classes: `NvsFx`, `NvsStreamingContext`
Static/constants: `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `setBeforeViewEnable()`, `findKeyframeTime()`, `getTimelineCurrentPosition()`, `setSequenceViewIsSeekingStatus()`, `seekTimeline()`, `scrollSequenceViewTo()`

Simple sequence:

```java
if (fxFromClip != null) {
long beforeKeyFrame = fxFromClip.findKeyframeTime(FILTER_INTENSITY, mStreamingContext.getTimelineCurrentPosition(mTimeline),
NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE);
if (beforeKeyFrame == -1) {
mFilterKeyFrameView.setBeforeViewEnable(false);
mFilterKeyFrameView.setBeforeViewEnable(true);
mFilterKeyFrameView.setSequenceViewIsSeekingStatus(true);
mStreamingContext.seekTimeline(mTimeline, beforeKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);
```

## `effects-transforms-094` `beforeFrameClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:168`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `setBeforeViewEnable()`, `setSequenceViewIsSeekingStatus()`, `seekTimeline()`, `scrollSequenceViewTo()`

Simple sequence:

```java
if (beforeKeyFrame == -1) {
mFilterKeyFrameView.setBeforeViewEnable(false);
mFilterKeyFrameView.setBeforeViewEnable(true);
mFilterKeyFrameView.setSequenceViewIsSeekingStatus(true);
mStreamingContext.seekTimeline(mTimeline, beforeKeyFrame, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, 0);
```

## `effects-transforms-095` `deleteFrameClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:180`

API classes: `NvsFx`
Common calls: `getKeyFrameInfoMap()`, `removeKeyframeAtTime()`, `remove()`, `updateKeyFramePointView()`

Simple sequence:

```java
NvsFx fxFromClip = getFxFromClip();
if (fxFromClip != null) {
fxFromClip.removeKeyframeAtTime(FILTER_INTENSITY, deleteStamp);
mVideoClipFxInfo.getKeyFrameInfoMap().remove(deleteStamp);
mFilterKeyFrameView.updateKeyFramePointView(mVideoClipFxInfo.getKeyFrameInfoMap());
```

## `effects-transforms-096` `onProgressChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/ClipFilterActivity.java:191`

API classes: `NvsFx`
Common calls: `putKeyFrameInfo()`, `updateKeyFramePointView()`, `getKeyFrameInfoMap()`, `setFloatValAtTime()`

Simple sequence:

```java
mFilterKeyFrameView.updateKeyFramePointView(mVideoClipFxInfo.getKeyFrameInfoMap());
NvsFx fxFromClip = getFxFromClip();
fxFromClip.setFloatValAtTime(FILTER_INTENSITY, intensity, currentStamp);
```

## `effects-transforms-097` `initFilterAssets`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:109`

API classes: `NvsTimeline`
Common calls: `putInt()`, `seekTimeline()`, `getTimelineCurrentPosition()`, `getLayoutParams()`, `beginTransaction()`, `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `setTimeline()`, `putBoolean()`, `instance()`, `getMakeRatio()`, `setArguments()`

Simple sequence:

```java
mVideoFragment.setFragmentLoadFinisedListener(new VideoFragment.OnFragmentLoadFinisedListener() {
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), 0);
mVideoFragment.setTimeline(mTimeline);
bundle.putInt("titleHeight", mTitleBar.getLayoutParams().height);
bundle.putInt("bottomHeight", mBottomLayout.getLayoutParams().height);
bundle.putInt("ratio", TimelineData.instance().getMakeRatio());
mVideoFragment.setArguments(bundle);
mVideoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
if (timeline.getDuration() - mStreamingContext.getTimelineCurrentPosition(mTimeline) <= 40000) {
mVideoFragment.seekTimeline(0, 0);
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `effects-transforms-098` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:143`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `effects-transforms-099` `initFilterView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:157`

API classes: `NvsStreamingContext`, `NvsTimelineVideoFx`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `playVideoButtonClick()`, `putInt()`, `getInstance()`, `changeAdjustIntensity()`, `setFilterListener()`, `OnFilterListener()`, `size()`, `isEmpty()`, `setVisibility()`, `setIntensityLayoutVisible()`, `applyFilterByTimeline()`, `getStreamingEngineState()`

Simple sequence:

```java
mFilterView.setFilterListener(new FilterView.OnFilterListener() {
if (position == 0) {
mAdjustView.setVisibility(View.GONE);
mFilterView.setIntensityLayoutVisible(View.INVISIBLE);
TimelineUtil.applyFilterByTimeline(mTimeline, null);
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
AppManager.getInstance().jumpActivityForResult(FilterActivity.this
if ((null == mTimeline) || (null == mFilterItem)) {
NvsTimelineVideoFx videoFx = mTimeline.getFirstTimelineVideoFx();
videoFx.setFilterIntensity(intensity);
mFilterItem.setIntensity(intensity);
mAdjustView.setOnItemProgressChangeListener(new AdjustSpecialEffectsView.OnItemProgressChangeListener() {
mPresenter.changeAdjustIntensity(info, mFilterItem, progress, false);
mPresenter.changeAdjustIntensity(effectsInfo, mFilterItem, color, true);
mFinish.setOnClickListener(new View.OnClickListener() {
TimelineData.instance().setFilterFx(mFilterItem);
AppManager.getInstance().finishActivity(FilterActivity.this);
```

## `effects-transforms-100` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:160`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `playVideoButtonClick()`, `size()`, `isEmpty()`, `setVisibility()`, `setIntensityLayoutVisible()`, `applyFilterByTimeline()`, `getStreamingEngineState()`

Simple sequence:

```java
if (position == 0) {
mAdjustView.setVisibility(View.GONE);
mFilterView.setIntensityLayoutVisible(View.INVISIBLE);
TimelineUtil.applyFilterByTimeline(mTimeline, null);
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
```

## `effects-transforms-101` `setAddDeleteViewEnable`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:89`

API classes: `NvsFx`
Common calls: `setCurrentKeyFramePosition()`, `duringToLength()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
public void setCurrentFx(NvsFx currentFx) {
if (mKeyFramePointView != null) {
mKeyFramePointView.setCurrentKeyFramePosition(LengthAndStampUtils.duringToLength(mStreamingContext.getTimelineCurrentPosition(mTimeline), mPixelPerMicrosecond));
```

## `effects-transforms-102` `FilterKeyFrameView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:125`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
mStreamingContext = NvsStreamingContext.getInstance();
```

## `effects-transforms-103` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:195`

API classes: `NvsMultiThumbnailSequenceView`
Static/constants: `NvsMultiThumbnailSequenceView.OnScrollChangeListener`
Common calls: `setOnScrollChangeListenser()`, `OnScrollChangeListener()`, `scrollTo()`, `floor()`, `getCircleToStampMap()`, `onScrollX()`

Simple sequence:

```java
mKeyFrameSequenceView.setOnScrollChangeListenser(new NvsMultiThumbnailSequenceView.OnScrollChangeListener() {
public void onScrollChanged(NvsMultiThumbnailSequenceView nvsMultiThumbnailSequenceView, int i, int i1) {
HashMap<Point, Long> circleToStampMap = mKeyFramePointView.getCircleToStampMap();
```

## `effects-transforms-104` `updateAllKeyFrameViewStatusWhenScroll`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:252`

API classes: `NvsFx`
Static/constants: `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE`, `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER`
Common calls: `findKeyframeTime()`, `hasKeyframeList()`, `duringToLength()`, `keySet()`, `setCurrentKeyFramePosition()`, `getFloatValAtTime()`, `setProgress()`

Simple sequence:

```java
if (hasKeyframeList) {
long hasBeforeKeyFrame = mCurrentFx.findKeyframeTime(FILTER_INTENSITY, currentTimeStamp, NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE);
long hasNextKeyFrame = mCurrentFx.findKeyframeTime(FILTER_INTENSITY, currentTimeStamp, NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER);
mKeyFramePointView.setCurrentKeyFramePosition(currentPos);
double intensityOfCurrentPos = mCurrentFx.getFloatValAtTime(FILTER_INTENSITY, currentTimeStamp);
mKeyFrameSeekBar.setProgress((int) (intensityOfCurrentPos * 100));
```

## `effects-transforms-105` `updateAllKeyFrameViewStatusWhenScroll`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterKeyFrameView.java:257`

API classes: `NvsFx`
Static/constants: `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE`, `NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER`
Common calls: `findKeyframeTime()`, `duringToLength()`, `keySet()`, `setCurrentKeyFramePosition()`

Simple sequence:

```java
if (hasKeyframeList) {
long hasBeforeKeyFrame = mCurrentFx.findKeyframeTime(FILTER_INTENSITY, currentTimeStamp, NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_BEFORE);
long hasNextKeyFrame = mCurrentFx.findKeyframeTime(FILTER_INTENSITY, currentTimeStamp, NvsFx.KEY_FRAME_FIND_MODE_INPUT_TIME_AFTER);
mKeyFramePointView.setCurrentKeyFramePosition(currentPos);
```

## `effects-transforms-106` `setAdjustFilter`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:132`

API classes: `NvsExpressionParam`, `NvsColor`
Static/constants: `NvsExpressionParam.TYPE_COLOR`, `NvsExpressionParam.TYPE_FLOAT`, `NvsExpressionParam.FloatParam`, `NvsExpressionParam.TYPE_INT`, `NvsExpressionParam.IntParam`, `NvsExpressionParam.TYPE_BOOLEAN`
Common calls: `getDefVal()`, `setDefVal()`, `setMaxVal()`, `getMaxVal()`, `setMinVal()`, `getMinVal()`, `setStrength()`, `setFilterParam()`, `getKey()`, `getStrength()`, `getType()`, `getName()`

Simple sequence:

```java
for (NvsExpressionParam nvsExpressionParam : expValueList) {
int type = nvsExpressionParam.getType();
key = nvsExpressionParam.getName();
adjustSpecialEffectsInfo.setPackageId(packageId);
adjustSpecialEffectsInfo.setAdjustmentCategoryName(name);
adjustSpecialEffectsInfo.setKey(key);
adjustSpecialEffectsInfo.setType(type);
switch (type) {
case NvsExpressionParam.TYPE_COLOR:
NvsColor nvsColor = nvsExpressionParam.getColor();
if (null != nvsColor) {
adjustSpecialEffectsInfo.setColor(nvsColor);
mFilterItem.setFilterColorParam(key, nvsColor);
case NvsExpressionParam.TYPE_FLOAT:
NvsExpressionParam.FloatParam floatParam = nvsExpressionParam.getFloatParam();
if (null != floatParam) {
adjustSpecialEffectsInfo.setDefVal(floatParam.getDefVal());
adjustSpecialEffectsInfo.setMaxVal(floatParam.getMaxVal());
adjustSpecialEffectsInfo.setMinVal(floatParam.getMinVal());
adjustSpecialEffectsInfo.setStrength(floatParam.getDefVal());
mFilterItem.setFilterParam(adjustSpecialEffectsInfo.getKey(), adjustSpecialEffectsInfo.getStrength());
case NvsExpressionParam.TYPE_INT:
NvsExpressionParam.IntParam intParam = nvsExpressionParam.getIntParam();
if (null != intParam) {
// ... 6 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-107` `changeAdjustIntensity`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:188`

API classes: `NvsColor`
Common calls: `alpha()`, `red()`, `green()`, `blue()`, `setColor()`, `setFilterColorParam()`, `getKey()`, `getColor()`, `onChangeAdjustFilter()`

Simple sequence:

```java
info.setColor(new NvsColor(red, green, blue, alphaF));
mFilterItem.setFilterColorParam(info.getKey(), info.getColor());
```

## `effects-transforms-108` `onSizeChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/KeyFramePointView.java:101`

API classes: `NvsTimeline`
Common calls: `getDuration()`

Simple sequence:

```java
public void initKeyFramePointView(HashMap<Long, Double> keyFramePointList, NvsTimeline timeline, double pixelPerMicrosecond) {
mTimeline = timeline;
layoutParams.width = duringToLength(timeline.getDuration());
```

## `effects-transforms-109` `getClipStartTime`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:302`

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

## `effects-transforms-110` `getClipEndTime`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:324`

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

## `effects-transforms-111` `getClipDuration`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:346`

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

## `effects-transforms-112` `setMaskCenter`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:443`

API classes: `NvsVideoResolution`
Common calls: `getTransX()`, `getLiveWindow()`, `getTransY()`, `getBackGroundInfo()`, `instance()`, `getVideoResolution()`, `getWidth()`, `getHeight()`, `d()`, `getScaleX()`, `getRotation()`, `getMaskZoomView()`

Simple sequence:

```java
if (clipInfo == null) return;
BackGroundInfo backGroundInfo = clipInfo.getBackGroundInfo();
NvsVideoResolution videoResolution = TimelineData.instance().getVideoResolution();
if (backGroundInfo != null && videoResolution != null) {
transX = backGroundInfo.getTransX() / videoResolution.imageWidth * mVideoFragment.getLiveWindow().getWidth();
transY = backGroundInfo.getTransY() / videoResolution.imageHeight * mVideoFragment.getLiveWindow().getHeight();
Log.d(TAG, "=-= setMaskCenter transX:" + backGroundInfo.getTransX() + "transY:" + backGroundInfo.getTransY());
scaleX = backGroundInfo.getScaleX();
rotation = backGroundInfo.getRotation();
mVideoFragment.getMaskZoomView().setBackgroundInfo(transX, transY, rotation, scaleX);
```

## `effects-transforms-113` `removeTimelineAnimal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:475`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoFx`, `NvsConstants`
Static/constants: `NvsConstants.ANIMATION_POST_PACKAGE_ID`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `getPropertyVideoFx()`, `setStringVal()`, `setBuiltinTransition()`, `setPackagedTransition()`

Simple sequence:

```java
private void removeTimelineAnimal(NvsTimeline timeline) {
if (timeline == null)
NvsVideoTrack mVideoTrack = timeline.getVideoTrackByIndex(0);
int clipCount = mVideoTrack.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = mVideoTrack.getClipByIndex(i);
if (videoClip != null) {
NvsVideoFx propertyVideoFx = videoClip.getPropertyVideoFx();
if (propertyVideoFx != null) {
propertyVideoFx.setStringVal(NvsConstants.ANIMATION_POST_PACKAGE_ID, "");
if (i < clipCount - 1) {
mVideoTrack.setBuiltinTransition(i, "");
mVideoTrack.setPackagedTransition(i, "");
```

## `effects-transforms-114` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:559`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `effects-transforms-115` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:564`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `effects-transforms-116` `playbackTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:569`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getMaskZoomView()`, `setMaskViewVisibility()`

Simple sequence:

```java
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
mVideoFragment.getMaskZoomView().setMaskViewVisibility(View.GONE);
mVideoFragment.getMaskZoomView().setMaskViewVisibility(View.VISIBLE);
```

## `effects-transforms-117` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:570`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getMaskZoomView()`, `setMaskViewVisibility()`

Simple sequence:

```java
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
mVideoFragment.getMaskZoomView().setMaskViewVisibility(View.GONE);
mVideoFragment.getMaskZoomView().setMaskViewVisibility(View.VISIBLE);
```

## `effects-transforms-118` `changeMaskByCrop`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:627`

API classes: `NvsLiveWindow`
Common calls: `calculateMaskByCrop()`, `getMaskZoomView()`, `updateMaskSize()`, `getMaskWidth()`, `getMaskHeight()`

Simple sequence:

```java
private void changeMaskByCrop(NvsLiveWindow liveWindow, ClipInfo clipInfo, MaskInfoData maskInfoData) {
if (!NvMaskHelper.calculateMaskByCrop(liveWindow, clipInfo, maskInfoData)) {
mVideoFragment.getMaskZoomView().updateMaskSize(maskInfoData.getMaskWidth(), maskInfoData.getMaskHeight());
```

## `effects-transforms-119` `buildCircleMaskRegionInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:555`

API classes: `NvsMaskRegionInfo`, `NvsPosition2D`
Static/constants: `NvsMaskRegionInfo.RegionInfo`, `NvsMaskRegionInfo.Transform2D`, `NvsMaskRegionInfo.MASK_REGION_TYPE_ELLIPSE2D`, `NvsMaskRegionInfo.Ellipse2D`
Common calls: `RegionInfo()`, `setEllipse2D()`, `Ellipse2D()`, `Transform2D()`, `setRotation()`, `setAnchor()`, `setTransform2D()`, `addRegionInfo()`

Simple sequence:

```java
center = mapViewToNormalized(center, liveWindow, size);
NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_ELLIPSE2D);
regionInfo.setEllipse2D(new NvsMaskRegionInfo.Ellipse2D(new NvsPosition2D(center.x, center.y), widthPercent, heightPercent, 0));
NvsMaskRegionInfo.Transform2D transform2D = new NvsMaskRegionInfo.Transform2D();
transform2D.setRotation(-angle);
transform2D.setAnchor(new NvsPosition2D(center.x, center.y));
regionInfo.setTransform2D(transform2D);
```

## `effects-transforms-120` `buildRectMaskRegionInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:598`

API classes: `NvsMaskRegionInfo`
Static/constants: `NvsMaskRegionInfo.RegionInfo`, `NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE`
Common calls: `d()`, `mapViewToNormalized()`, `RegionInfo()`, `addRegionInfo()`

Simple sequence:

```java
NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE);
getPointByAngle(nextPoint1, center, angle), getPointByAngle(prePoint1, center, angle), liveWindow, size);
getPointByAngle(nextPoint2, center, angle), getPointByAngle(prePoint2, center, angle), liveWindow, size);
getPointByAngle(nextPoint3, center, angle), getPointByAngle(prePoint3, center, angle), liveWindow, size);
getPointByAngle(nextPoint4, center, angle), getPointByAngle(prePoint4, center, angle), liveWindow, size);
getPointByAngle(nextPoint5, center, angle), getPointByAngle(prePoint5, center, angle), liveWindow, size);
getPointByAngle(nextPoint6, center, angle), getPointByAngle(prePoint6, center, angle), liveWindow, size);
getPointByAngle(nextPoint7, center, angle), getPointByAngle(prePoint7, center, angle), liveWindow, size);
getPointByAngle(nextPoint8, center, angle), getPointByAngle(prePoint8, center, angle), liveWindow, size);
```

## `effects-transforms-121` `maskRegionInfoAddPoints`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:782`

API classes: `NvsPosition2D`
Common calls: `e()`, `getPoints()`, `addAll()`

Simple sequence:

```java
List<NvsPosition2D> position2DList = buildNvsPositionListFromPointFList(pointArray, liveWindow, size);
info.getPoints().addAll(position2DList);
```

## `effects-transforms-122` `buildHeartMaskRegionInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:806`

API classes: `NvsMaskRegionInfo`, `NvsLiveWindow`, `NvsPosition2D`
Static/constants: `NvsMaskRegionInfo.RegionInfo`, `NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE`
Common calls: `RegionInfo()`, `setPoints()`, `addRegionInfo()`

Simple sequence:

```java
NvsLiveWindow liveWindow, PointF size) {
NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_CUBIC_CURVE);
List<NvsPosition2D> nvsPosition2DS = buildNvsPositionListFromPointFList(pointFS, liveWindow, size);
regionInfo.setPoints(nvsPosition2DS);
```

## `effects-transforms-123` `buildPolygonMaskRegionInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:843`

API classes: `NvsMaskRegionInfo`, `NvsLiveWindow`, `NvsPosition2D`
Static/constants: `NvsMaskRegionInfo.RegionInfo`, `NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON`
Common calls: `RegionInfo()`, `setPoints()`, `addRegionInfo()`

Simple sequence:

```java
public static NvsMaskRegionInfo buildPolygonMaskRegionInfo(PointF[] pointFList, NvsLiveWindow liveWindow, PointF size) {
List<NvsPosition2D> nvsPosition2DS = buildNvsPositionListFromPointFList(pointFList, liveWindow, size);
NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON);
regionInfo.setPoints(nvsPosition2DS);
```

## `effects-transforms-124` `buildStarMaskRegionInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:867`

API classes: `NvsMaskRegionInfo`, `NvsLiveWindow`, `NvsPosition2D`
Static/constants: `NvsMaskRegionInfo.RegionInfo`, `NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON`
Common calls: `sin()`, `cos()`, `RegionInfo()`, `setPoints()`, `addRegionInfo()`

Simple sequence:

```java
public static NvsMaskRegionInfo buildStarMaskRegionInfo(PointF center, int width, float rotation, NvsLiveWindow liveWindow, PointF size) {
NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON);
List<NvsPosition2D> position2DList = buildNvsPositionListFromPointFList(allPoints, liveWindow, size);
regionInfo.setPoints(position2DList);
```

## `effects-transforms-125` `mapViewToNormalized`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:922`

API classes: `NvsLiveWindow`
Common calls: `getWidth()`, `getHeight()`, `mapViewToNormalized()`

Simple sequence:

```java
private static PointF mapViewToNormalized(PointF pointF, NvsLiveWindow liveWindow, PointF size) {
livePoint.x = -(liveWindow.getWidth() / 2f - pointF.x) / size.x * 2f;
livePoint.y = (liveWindow.getHeight() / 2f - pointF.y) / size.y * 2f;
```

## `effects-transforms-126` `buildNvsPositionListFromPointFList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:942`

API classes: `NvsPosition2D`, `NvsLiveWindow`
Common calls: `add()`

Simple sequence:

```java
private static List<NvsPosition2D> buildNvsPositionListFromPointFList(PointF[] pointFList, NvsLiveWindow liveWindow, PointF size) {
List<NvsPosition2D> nvsPosition2DS = new ArrayList<>();
for (PointF pointF : pointFList) {
PointF result = mapViewToNormalized(pointF, liveWindow, size);
nvsPosition2DS.add(new NvsPosition2D(result.x, result.y));
```

## `effects-transforms-127` `buildNvsPositionListFromPointFList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:944`

API classes: `NvsPosition2D`
Common calls: `add()`

Simple sequence:

```java
for (PointF pointF : pointFList) {
PointF result = mapViewToNormalized(pointF, liveWindow, size);
nvsPosition2DS.add(new NvsPosition2D(result.x, result.y));
```

## `effects-transforms-128` `buildNvsPositionListFromPointFList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:945`

API classes: `NvsPosition2D`
Common calls: `add()`

Simple sequence:

```java
for (PointF pointF : pointFList) {
PointF result = mapViewToNormalized(pointF, liveWindow, size);
nvsPosition2DS.add(new NvsPosition2D(result.x, result.y));
```

## `effects-transforms-129` `buildRealMaskInfoData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:968`

API classes: `NvsMaskRegionInfo`
Common calls: `getMaskType()`, `e()`, `getTranslationX()`, `getTranslationY()`, `getRotation()`, `getScale()`, `getLiveWindowCenter()`, `transformData()`, `getMaskWidth()`, `getMaskHeight()`, `getRoundCornerWidthRate()`, `getMaskTextStoryboard()`

Simple sequence:

```java
NvsMaskRegionInfo nvsMaskRegionInfo = null;
PointF liveWindowCenter = maskData.getLiveWindowCenter();
PointF transform = NvMaskHelper.transformData(new PointF(maskData.getTranslationX(), maskData.getTranslationY())
int maskWidth = maskData.getMaskWidth();
int maskHeight = maskData.getMaskHeight();
float rotation = maskData.getRotation();
float cornerRadiusRate = maskData.getRoundCornerWidthRate();
if (maskData.getMaskType() == MaskInfoData.MaskType.NONE) {
} else if (maskData.getMaskType() == MaskInfoData.MaskType.LINE) {
} else if (maskData.getMaskType() == MaskInfoData.MaskType.MIRROR) {
} else if (maskData.getMaskType() == MaskInfoData.MaskType.CIRCLE) {
} else if (maskData.getMaskType() == MaskInfoData.MaskType.RECT) {
} else if (maskData.getMaskType() == MaskInfoData.MaskType.HEART) {
} else if (maskData.getMaskType() == MaskInfoData.MaskType.STAR) {
} else if (maskData.getMaskType() == MaskInfoData.MaskType.TEXT) {
String storyBoard = StoryboardUtil.getMaskTextStoryboard(liveWindowExt.getWidth(),
liveWindowExt.getHeight(), (int) maskData.getSingleTextHeight(), maskData.getText(), 100000,
maskData.getScale(), maskData.getScale(), maskData.getTranslationX() / fxScale,
-maskData.getTranslationY() / fxScale, -maskData.getRotation());
maskData.setTextStoryboard(storyBoard);
maskData.setMaskRegionInfo(nvsMaskRegionInfo);
```

## `effects-transforms-130` `assetSizeInBox`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1024`

API classes: `NvsLiveWindow`
Common calls: `getWidth()`, `getHeight()`

Simple sequence:

```java
public static PointF assetSizeInBox(NvsLiveWindow liveWindowExt, float assetAspectRatio) {
float liveWindowWidth = liveWindowExt.getWidth() * 1.0f;
float liveWindowHeight = liveWindowExt.getHeight() * 1.0f;
```

## `effects-transforms-131` `buildMaskRegionRect`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1109`

API classes: `NvsMaskRegionInfo`, `NvsPosition2D`
Static/constants: `NvsMaskRegionInfo.RegionInfo`, `NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON`
Common calls: `getRegionData()`, `add()`, `RegionInfo()`, `setPoints()`, `addRegionInfo()`

Simple sequence:

```java
public static NvsMaskRegionInfo buildMaskRegionRect(CropInfo cropInfo) {
float[] regionData = cropInfo.getRegionData();
NvsMaskRegionInfo nvsMaskRegionInfo = new NvsMaskRegionInfo();
List<NvsPosition2D> nvsPosition2DS = new ArrayList<>();
for (int i = 0; i < regionData.length; i++) {
nvsPosition2DS.add(new NvsPosition2D(regionData[i], regionData[++i]));
NvsMaskRegionInfo.RegionInfo regionInfo = new NvsMaskRegionInfo.RegionInfo(NvsMaskRegionInfo.MASK_REGION_TYPE_POLYGON);
regionInfo.setPoints(nvsPosition2DS);
```

## `effects-transforms-132` `calculateMaskByCrop`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/NvMaskHelper.java:1137`

API classes: `NvsLiveWindow`
Common calls: `getCropInfo()`, `setMaskWidth()`, `getMaskWidth()`, `setMaskHeight()`, `getMaskHeight()`

Simple sequence:

```java
public static boolean calculateMaskByCrop(NvsLiveWindow liveWindow, ClipInfo clipInfo, MaskInfoData maskInfoData) {
CutData cutData = clipInfo.getCropInfo();
float scale = calculateScaleInBox(liveWindow, clipInfo);
maskInfoData.setMaskWidth((int) (maskInfoData.getMaskWidth() * scale));
maskInfoData.setMaskHeight((int) (maskInfoData.getMaskHeight() * scale));
```

## `effects-transforms-133` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:305`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`

Simple sequence:

```java
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_play);
```

## `effects-transforms-134` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:306`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`

Simple sequence:

```java
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
m_playBtn.setBackgroundResource(R.mipmap.icon_edit_play);
```

## `effects-transforms-135` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:395`

API classes: `NvsVideoTransition`
Common calls: `getSelectPos()`, `setTransitionInterval()`, `putInt()`, `getInstance()`, `setVideoTransitionDuration()`, `parseFloat()`, `getVisibility()`, `setVisibility()`, `setClickable()`, `jumpActivityForResult()`, `currentActivity()`, `get()`

Simple sequence:

```java
if (id == R.id.download_more_btn) {
mMoreDownload.setClickable(false);
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(),
} else if (id == R.id.transition_change_interval_identify_iv) {/*                int transitionPos = mThumbAdapter.getSelectPos( );
NvsVideoTransition videoTransition = transitionInfo.getVideoTransition( );
int selectPos = mTimeChangeAdapter.getSelectPos( );
if (hasSelect) {
videoTransition.setVideoTransitionDuration(mIntervalArray[selectPos] * TIME_BASE);
transitionInfo.setTransitionInterval(mIntervalArray[selectPos] * TIME_BASE);
String inputValue = mIntervalChangeEdittext.getText( ).toString( ).trim( );
if (hasInput) {
videoTransition.setVideoTransitionDuration((long) (Float.parseFloat(inputValue) * TIME_BASE));
transitionInfo.setTransitionInterval((long) (Float.parseFloat(inputValue) * TIME_BASE));
if (mIntervalSettingLayout.getVisibility() == View.VISIBLE) {
mIntervalSettingLayout.setVisibility(View.GONE);
mTransitionInfo.setTransitionInterval((long) (mIntervalTime * 1000000));
mTransitionInfo.setChangeDuration(true);
TimelineUtil.setTransition(mTimeline, mTransitionInfo, mThumbAdapter.getSelectPos());
if (mIntervalSettingLayout.getVisibility() == View.VISIBLE) {
mIntervalSettingLayout.setVisibility(View.GONE);
```

## `effects-transforms-136` `removeTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:791`

API classes: `NvsVideoClip`
Common calls: `getClipByIndex()`, `getInPoint()`, `getOutPoint()`, `size()`, `get()`, `getTransitionInterval()`, `getClipCount()`, `playVideo()`

Simple sequence:

```java
if (transitionInfo != null) {
long transitionInterval = transitionInfo.getTransitionInterval();
int videoCount = mVideoTrack.getClipCount();
NvsVideoClip clip = mVideoTrack.getClipByIndex(index);
long inPointBefore = clip.getInPoint();
long outPointBefore = clip.getOutPoint();
NvsVideoClip nextClip = mVideoTrack.getClipByIndex(index + 1);
long inPointNext = nextClip.getInPoint();
long outPointNext = nextClip.getOutPoint();
```

## `effects-transforms-137` `onAssetHorizFlip`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:217`

API classes: `NvsTimeline`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setDrawRectVisible()`, `setVideoFragmentCallBack()`, `VideoFragmentListener()`

Simple sequence:

```java
videoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
if (waterMarkType == WaterMarkConstant.WATERMARKTYPE_DYNAMICS || waterMarkType == WATERMARKTYPE_EFFECK) {
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
videoFragment.setDrawRectVisible(View.GONE);
videoFragment.setDrawRectVisible(View.VISIBLE);
```

## `effects-transforms-138` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:225`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `effects-transforms-139` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:229`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `effects-transforms-140` `playbackTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:233`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setDrawRectVisible()`

Simple sequence:

```java
if (waterMarkType == WaterMarkConstant.WATERMARKTYPE_DYNAMICS || waterMarkType == WATERMARKTYPE_EFFECK) {
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
videoFragment.setDrawRectVisible(View.GONE);
videoFragment.setDrawRectVisible(View.VISIBLE);
```

## `effects-transforms-141` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:235`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setDrawRectVisible()`

Simple sequence:

```java
if (waterMarkType == WaterMarkConstant.WATERMARKTYPE_DYNAMICS || waterMarkType == WATERMARKTYPE_EFFECK) {
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
videoFragment.setDrawRectVisible(View.GONE);
videoFragment.setDrawRectVisible(View.VISIBLE);
```

## `effects-transforms-142` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:236`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setDrawRectVisible()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
videoFragment.setDrawRectVisible(View.GONE);
videoFragment.setDrawRectVisible(View.VISIBLE);
```

## `effects-transforms-143` `refreshLiveWindowFrame`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkActivity.java:527`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (playState != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
videoFragment.seekTimeline(nvsStreamingContext.getTimelineCurrentPosition(nvsTimeline), 0);
```

## `effects-transforms-144` `setDynamicWaterMark`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java:64`

API classes: `NvsTimelineVideoFx`
Common calls: `setFloatVal()`, `setStringVal()`, `addBuiltinTimelineVideoFx()`, `getDuration()`, `setBooleanVal()`

Simple sequence:

```java
NvsTimelineVideoFx story = nvsTimeline.addBuiltinTimelineVideoFx(0, nvsTimeline.getDuration(), WATERMARK_DYNAMICS_FXNAME);
story.setStringVal("Resource Dir", dir);
story.setStringVal("Description String", descString);
story.setBooleanVal("Is Animated Sticker", true);
story.setFloatVal("Sticker Scale", scale);
story.setFloatVal("Sticker TransX", transX);
story.setFloatVal("Sticker TransY", -transY);
```

## `effects-transforms-145` `onFragmentLoadFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectActivity.java:332`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `reset()`

Simple sequence:

```java
if (i != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
```

## `effects-transforms-146` `onStreamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:363`

API classes: `NvsTimeline`

Simple sequence:

```java
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
```

## `effects-transforms-147` `removeTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:196`

API classes: `NvsVideoClip`, `NvsVideoFx`
Static/constants: `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE`, `NvsVideoClip.VIDEO_CLIP_TYPE_AV`
Common calls: `instance()`, `getVideoType()`, `getClipInfoData()`, `size()`, `get()`, `createSingleClipTimeline()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `changeTrimOutPoint()`, `appendBuiltinFx()`, `e()`, `getVideoClipFxData()`

Simple sequence:

```java
ArrayList<ClipInfo> videoClipArray = TimelineData.instance().getClipInfoData();
mTimeline = TimelineUtil.createSingleClipTimeline(clipInfo, false);
if (mTimeline == null)
NvsVideoClip clip = mTimeline.getVideoTrackByIndex(0).getClipByIndex(0);
if (clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) { // 图片
clip.changeTrimOutPoint(10 * Constants.NS_TIME_BASE, true);
} else if (clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV) {// 视频
NvsVideoFx builtinFx = clip.appendBuiltinFx("Transform 2D");
mVideoClipFxInfo = TimelineData.instance().getVideoClipFxData();
```

## `effects-transforms-148` `updateFxIntensity`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverActivity.java:351`

API classes: `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoFx`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `equals()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `getRawFxCount()`, `getRawFxByIndex()`, `getBuiltinVideoFxName()`, `setFilterIntensity()`, `getCurrentEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mTimeline == null)
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
for (int i = 0; i < videoTrack.getClipCount(); i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
int fxCount = videoClip.getRawFxCount();
for (int j = 0; j < fxCount; j++) {
NvsVideoFx fx = videoClip.getRawFxByIndex(j);
String name = fx.getBuiltinVideoFxName();
fx.setFilterIntensity(value);
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `effects-transforms-149` `setSelectCoverListener`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:452`

API classes: `NvsVideoFx`, `NvsVideoTrack`, `NvsVideoClip`
Static/constants: `NvsVideoFx.VIDEOFX_TYPE_BUILTIN`
Common calls: `setFloatVal()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `getFxCount()`, `getFxByIndex()`, `getVideoFxType()`, `getBuiltinVideoFxName()`, `equals()`, `d()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
for (int clipIindex = 0; clipIindex < clipCount; ++clipIindex) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(clipIindex);
int fxCount = videoClip.getFxCount();
for (int fxIndex = 0; fxIndex < fxCount; ++fxIndex) {
NvsVideoFx videoFx = videoClip.getFxByIndex(fxIndex);
if (videoFx.getVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN
&& videoFx.getBuiltinVideoFxName().equals(videoFxName)) {
videoFx.setFloatVal("Scale X", scaleValue);
videoFx.setFloatVal("Scale Y", scaleValue);
videoFx.setFloatVal("Rotation", rotateAngle);
videoFx.setFloatVal("Trans X", transX);
videoFx.setFloatVal("Trans Y", transY);
```

## `effects-transforms-150` `updateTransform2DFx`

Source: `app/src/main/java/com/meishe/sdkdemo/makecover/MakeCoverFragment.java:455`

API classes: `NvsVideoFx`, `NvsVideoClip`
Static/constants: `NvsVideoFx.VIDEOFX_TYPE_BUILTIN`
Common calls: `setFloatVal()`, `getClipByIndex()`, `getFxCount()`, `getFxByIndex()`, `getVideoFxType()`, `getBuiltinVideoFxName()`, `equals()`, `d()`

Simple sequence:

```java
for (int clipIindex = 0; clipIindex < clipCount; ++clipIindex) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(clipIindex);
int fxCount = videoClip.getFxCount();
for (int fxIndex = 0; fxIndex < fxCount; ++fxIndex) {
NvsVideoFx videoFx = videoClip.getFxByIndex(fxIndex);
if (videoFx.getVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN
&& videoFx.getBuiltinVideoFxName().equals(videoFxName)) {
videoFx.setFloatVal("Scale X", scaleValue);
videoFx.setFloatVal("Scale Y", scaleValue);
videoFx.setFloatVal("Rotation", rotateAngle);
videoFx.setFloatVal("Trans X", transX);
videoFx.setFloatVal("Trans Y", transY);
```

## `effects-transforms-151` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleCaptureActivity.java:476`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING`
Common calls: `getParticleRecordPath()`, `setEnabled()`, `setBackgroundResource()`, `startRecording()`, `add()`

Simple sequence:

```java
if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
mCurRecordVideoPath = PathUtils.getParticleRecordPath();
mStartRecordingImage.setEnabled(false);
mStartRecordingImage.setBackgroundResource(R.mipmap.particle_capture_recording);
if (!mStreamingContext.startRecording(mCurRecordVideoPath)) {
```

## `effects-transforms-152` `setOnClickListener`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:348`

API classes: `NvsTimelineVideoFx`
Common calls: `getLastTimelineVideoFx()`, `getInPoint()`, `removeTimelineVideoFx()`, `updateIndicator()`, `deleteFxView()`

Simple sequence:

```java
if (mTimeline != null) {
NvsTimelineVideoFx lastVideoFx = mTimeline.getLastTimelineVideoFx();
if (lastVideoFx != null) {
long last_fx_in_point = lastVideoFx.getInPoint();
mTimeline.removeTimelineVideoFx(lastVideoFx);
```

## `effects-transforms-153` `getSqView`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleSqLayout.java:76`

API classes: `NvsMultiThumbnailSequenceView`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getSequenceWidth()`, `getRawX()`, `getWidth()`, `getPixelPerMicrosecond()`, `onDataChange()`, `initData()`, `addRule()`, `dip2px()`, `setBackgroundColor()`, `getColor()`, `setOnTouchListener()`, `getLayoutParams()`

Simple sequence:

```java
public void initData(long total_duration, ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> infoDescArray) {
LayoutParams fxAreaParams = new LayoutParams(m_sqView.getSequenceWidth(), m_sqHeight);
m_indicatorView.setBackgroundColor(ContextCompat.getColor(m_context, R.color.ff4a90e2));
m_indicatorView.setOnTouchListener(new OnTouchListener() {
LayoutParams indicatorParams = (RelativeLayout.LayoutParams) view.getLayoutParams();
switch (event.getAction()) {
m_lastX = (int) event.getRawX();
int curMoveX = (int)event.getRawX();
Object tag = view.getTag();
} else if(m_LeftMargin > m_sqView.getSequenceWidth() - m_indicatorView.getWidth()) {
m_LeftMargin = m_sqView.getSequenceWidth() - m_indicatorView.getWidth();
indicatorParams.setMargins(m_LeftMargin, 0, 0 , 0);
view.setLayoutParams(indicatorParams);
long curMoveTime = (long) (m_LeftMargin / m_sqView.getPixelPerMicrosecond());
long curUpTime = (long) (m_LeftMargin / m_sqView.getPixelPerMicrosecond());
m_indicatorView.setTag(m_LeftMargin);
```

## `effects-transforms-154` `onPlaybackTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/photoalbum/PhotoAlbumPreviewActivity.java:237`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.StreamingEngineCallback`, `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackground()`, `getDrawable()`, `StreamingEngineCallback()`, `setVisibility()`

Simple sequence:

```java
mStreamingEngineCallbackListener = new NvsStreamingContext.StreamingEngineCallback() {
if (i == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mPlayBtn.setBackground(ContextCompat.getDrawable(mContext, R.drawable.photo_ablum_preview_pause));
mPlayBtn.setVisibility(View.VISIBLE);
mPlayBtn.setBackground(ContextCompat.getDrawable(mContext, R.drawable.photo_ablum_preview_play));
public void onFirstVideoFramePresented(NvsTimeline nvsTimeline) {
```

## `effects-transforms-155` `addRemainVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:643`

API classes: `NvsVideoClip`, `NvsVideoFx`
Common calls: `getDuration()`, `getClipByIndex()`, `getFilePath()`, `abs()`, `min()`

Simple sequence:

```java
long firDuration = mVideoTrackFir.getDuration();
long secDuration = mVideoTrackSec.getDuration();
if (firDuration > secDuration) {
NvsVideoClip secondTrackClip = mVideoTrackSec.getClipByIndex(0);
String secondClipFilePath = secondTrackClip.getFilePath();
NvsVideoFx transformFx = getTransform2DFx(secondTrackClip);
NvsVideoClip firstTrackClip = mVideoTrackFir.getClipByIndex(0);
NvsVideoFx transformFx = getTransform2DFx(firstTrackClip);
String firstClipFilePath = firstTrackClip.getFilePath();
```

## `effects-transforms-156` `getTransform2DFx`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:713`

API classes: `NvsVideoFx`
Static/constants: `NvsVideoFx.VIDEOFX_TYPE_BUILTIN`
Common calls: `getFxByIndex()`, `getVideoFxType()`, `getBuiltinVideoFxName()`, `equals()`

Simple sequence:

```java
for (int fxIndex = 0; fxIndex < fxCount; ++fxIndex) {
NvsVideoFx videoFx = videoClip.getFxByIndex(fxIndex);
if (videoFx.getVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN
&& videoFx.getBuiltinVideoFxName().equals(videoFxName)) {
```

## `effects-transforms-157` `removeVideoFx`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:934`

API classes: `NvsVideoFx`
Common calls: `getFxByIndex()`, `getVideoFxType()`, `removeFx()`

Simple sequence:

```java
for (int index = 0; index < fxCount; ++index) {
NvsVideoFx videoFx = videoClip.getFxByIndex(index);
if (videoFx.getVideoFxType() == videoFxType) {
videoClip.removeFx(index);
```

## `effects-transforms-158` `updateSecTrackTransform2DFx`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:951`

API classes: `NvsVideoFx`, `NvsVideoTrack`, `NvsVideoClip`
Static/constants: `NvsVideoFx.VIDEOFX_TYPE_BUILTIN`
Common calls: `setFloatVal()`, `getClipCount()`, `getClipByIndex()`, `getFxCount()`, `getFxByIndex()`, `getVideoFxType()`, `getBuiltinVideoFxName()`, `equals()`, `e()`

Simple sequence:

```java
private void updateTransform2DFx(NvsVideoTrack videoTrack, double scaleValue, double rotateAngle, double transX, double transY) {
int clipCount = videoTrack.getClipCount();
for (int clipIindex = 0; clipIindex < clipCount; ++clipIindex) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(clipIindex);
int fxCount = videoClip.getFxCount();
for (int fxIndex = 0; fxIndex < fxCount; ++fxIndex) {
NvsVideoFx videoFx = videoClip.getFxByIndex(fxIndex);
if (videoFx.getVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN
&& videoFx.getBuiltinVideoFxName().equals(videoFxName)) {
videoFx.setFloatVal("Scale X", scaleValue);
videoFx.setFloatVal("Scale Y", scaleValue);
videoFx.setFloatVal("Rotation", rotateAngle);
videoFx.setFloatVal("Trans X", transX);
videoFx.setFloatVal("Trans Y", transY);
```

## `effects-transforms-159` `updateTransform2DFx`

Source: `app/src/main/java/com/meishe/sdkdemo/picinpic/PictureInPictureActivity.java:956`

API classes: `NvsVideoFx`
Static/constants: `NvsVideoFx.VIDEOFX_TYPE_BUILTIN`
Common calls: `setFloatVal()`, `getFxByIndex()`, `getVideoFxType()`, `getBuiltinVideoFxName()`, `equals()`, `e()`

Simple sequence:

```java
for (int fxIndex = 0; fxIndex < fxCount; ++fxIndex) {
NvsVideoFx videoFx = videoClip.getFxByIndex(fxIndex);
if (videoFx.getVideoFxType() == NvsVideoFx.VIDEOFX_TYPE_BUILTIN
&& videoFx.getBuiltinVideoFxName().equals(videoFxName)) {
videoFx.setFloatVal("Scale X", scaleValue);
videoFx.setFloatVal("Scale Y", scaleValue);
videoFx.setFloatVal("Rotation", rotateAngle);
videoFx.setFloatVal("Trans X", transX);
videoFx.setFloatVal("Trans Y", transY);
```

## `effects-transforms-160` `updateFilterVideoFx`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:731`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `appendPackagedCaptureVideoFx()`, `setFilterIntensity()`

Simple sequence:

```java
if (!TextUtils.isEmpty(filterPackageId)) {
NvsCaptureVideoFx curCaptureVideoFx = mStreamingContext.appendPackagedCaptureVideoFx(filterPackageId);
if (curCaptureVideoFx != null) {
curCaptureVideoFx.setFilterIntensity(1.0f);
```

## `effects-transforms-161` `updateFilterVideoFx`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:732`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `appendPackagedCaptureVideoFx()`, `setFilterIntensity()`

Simple sequence:

```java
if (!TextUtils.isEmpty(filterPackageId)) {
NvsCaptureVideoFx curCaptureVideoFx = mStreamingContext.appendPackagedCaptureVideoFx(filterPackageId);
if (curCaptureVideoFx != null) {
curCaptureVideoFx.setFilterIntensity(1.0f);
```

## `effects-transforms-162` `initTitle`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:143`

API classes: `NvsLiveWindow`
Static/constants: `NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT`
Common calls: `getVideoFx()`, `getExtras()`, `setLayoutManager()`, `addItemDecoration()`, `dip2px()`, `setAdapter()`, `setMax()`, `setOnSeekBarChangeListener()`, `OnSeekBarChangeListener()`, `setFilterIntensity()`, `getSerializable()`, `setFillMode()`

Simple sequence:

```java
filterSeekBar.setMax(100);
filterSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
if (currentPreviewBean != null && currentPreviewBean.getVideoFx() != null) {
currentPreviewBean.getVideoFx().setFilterIntensity(i / 100f);
if (getIntent() != null && getIntent().getExtras() != null) {
mThemeModel = (ThemeModel) getIntent().getExtras().getSerializable("ThemeModel");
mLiveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);
playView.setProgressMax((int) mTimeline.getDuration());
themeClipsRecycler.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false));
themeClipsRecycler.setAdapter(editAdapter);
editAdapter.setOnItemClickListener(new ThemePreviewAdapter.OnThemePreviewOnClickListener() {
compoundCaptionRecycler.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false));
compoundCaptionRecycler.setAdapter(captionAdapter);
mDownloadDialog.setOnDismissListener(new DialogInterface.OnDismissListener() {
mDownloadDialog.setProgress(0);
```

## `effects-transforms-163` `initFilterList`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:205`

API classes: `NvsTimelineVideoFx`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getFilterMode()`, `getFilterName()`, `setVideoFx()`, `get()`, `isEmpty()`, `getVideoFx()`, `setVisibility()`, `setEnabled()`, `getIsCartoon()`, `getStartDuration()`, `getDuration()`, `setBooleanVal()`

Simple sequence:

```java
mFilterDataArrayList = AssetFxUtil.getFilterData(this,
assetManager.getUsableAssets(NvAsset.ASSET_FILTER, NvAsset.AspectRatio_All, 0),
if (filterItem.getFilterMode() == FilterItem.FILTERMODE_PACKAGE) {
if (TextUtils.isEmpty(filterItem.getImageUrl()) || TextUtils.isEmpty(filterItem.getFilterName())) {
assetFilterAdapter.setFilterDataList(mFilterDataArrayList);
filterRecyclerView.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false));
filterRecyclerView.setAdapter(assetFilterAdapter);
assetFilterAdapter.setOnItemClickListener(new AssetFilterAdapter.OnItemClickListener() {
if (currentPreviewBean.getVideoFx() != null) {
mTimeline.removeTimelineVideoFx(currentPreviewBean.getVideoFx());
currentPreviewBean.setVideoFx(null);
if ("无".equals(filterItem.getFilterName())) {
filterSeekBar.setVisibility(View.INVISIBLE);
filterSeekBar.setEnabled(false);
filterSeekBar.setEnabled(true);
filterSeekBar.setProgress(80);
filterSeekBar.setVisibility(View.VISIBLE);
if (filterItem.getFilterMode() == FilterItem.FILTERMODE_BUILTIN) {
String buidId = filterItem.getIsCartoon() ? "Cartoon" : filterItem.getFilterName();
NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.addBuiltinTimelineVideoFx(currentPreviewBean.getStartDuration(),
currentPreviewBean.getDuration() * 1000, buidId);
if (filterItem.getIsCartoon() && nvsTimelineVideoFx != null) {
nvsTimelineVideoFx.setBooleanVal("Grayscale", filterItem.getGrayScale());
nvsTimelineVideoFx.setBooleanVal("Stroke Only", filterItem.getStrokenOnly());
// ... 8 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-164` `setTransCount`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:105`

API classes: `NvsTimelineVideoFx`

Simple sequence:

```java
public void setVideoFx(NvsTimelineVideoFx videoFx) {
```

## `effects-transforms-165` `addTimelineFilter`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:38`

API classes: `NvsTimeline`, `NvsTimelineVideoFx`
Common calls: `isEmpty()`, `addPackagedTimelineVideoFx()`, `getDuration()`, `setFilterIntensity()`

Simple sequence:

```java
public static void addTimelineFilter(NvsTimeline mTimeline, String filterPackageId) {
if (!TextUtils.isEmpty(filterPackageId)) {
NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.addPackagedTimelineVideoFx(0, mTimeline.getDuration(), filterPackageId);
if (nvsTimelineVideoFx != null) {
nvsTimelineVideoFx.setFilterIntensity(1.0f);
```

## `effects-transforms-166` `addTimelineFilter`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:39`

API classes: `NvsTimelineVideoFx`
Common calls: `isEmpty()`, `addPackagedTimelineVideoFx()`, `getDuration()`, `setFilterIntensity()`

Simple sequence:

```java
if (!TextUtils.isEmpty(filterPackageId)) {
NvsTimelineVideoFx nvsTimelineVideoFx = mTimeline.addPackagedTimelineVideoFx(0, mTimeline.getDuration(), filterPackageId);
if (nvsTimelineVideoFx != null) {
nvsTimelineVideoFx.setFilterIntensity(1.0f);
```

## `effects-transforms-167` `setVideoClipTrans`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/utlils/ThemeTimelineUtils.java:79`

API classes: `NvsVideoTransition`, `NvsVideoTrack`
Static/constants: `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH`
Common calls: `isEmpty()`, `setPackagedTransition()`, `getTransDuration()`, `e()`, `size()`, `get()`, `getSpeed()`, `getClipCountFromSpeed()`, `getDuration()`, `getTrans()`, `setVideoTransitionDuration()`, `setBuiltinTransition()`

Simple sequence:

```java
public static void setVideoClipTrans(NvsVideoTrack nvsVideoTrack, List<ThemeModel.ShotInfo> shotInfos) {
if (shotInfo != null) {
List<ThemeModel.ShotInfo.SpeedInfo> speed = shotInfo.getSpeed();
int clipCount = ThemeShootUtil.getClipCountFromSpeed(speed, shotInfo.getDuration());
for (int j = 0; j < clipCount -1; j++) {
nvsVideoTrack.setPackagedTransition(currentClip + addClip, null);
String trans = shotInfo.getTrans();
NvsVideoTransition nvsVideoTransition = nvsVideoTrack.setPackagedTransition(currentClip + addClip, trans);
if(shotInfo.getTransDuration() !=0){
nvsVideoTransition.setVideoTransitionDuration(shotInfo.getTransDuration()*1000, NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH);
nvsVideoTrack.setBuiltinTransition(currentClip + addClip, null);
int clipCount = nvsVideoTrack.getClipCount();
for (int index = 0;index < clipCount;index++){
NvsVideoTransition videoTransition = nvsVideoTrack.getTransitionBySourceClipIndex(index);
```

## `effects-transforms-168` `copyBuiltFx`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/CopyTimeLine.java:234`

API classes: `NvsFxDescription`
Static/constants: `NvsFxDescription.ParamInfoObject`
Common calls: `getString()`, `getIntVal()`, `getBooleanVal()`, `getStringVal()`, `getInteger()`, `setIntVal()`, `setFloatVal()`, `getFloatVal()`, `getBoolean()`, `setBooleanVal()`, `setMenuVal()`, `getMenuVal()`

Simple sequence:

```java
for (NvsFxDescription.ParamInfoObject param : paramInfo) {
String paramType = param.getString(PARAM_TYPE);
String paramName = param.getString(PARAM_NAME);
switch (paramType){
case NvsFxDescription.ParamInfoObject.PARAM_TYPE_INT:
if(param.getInteger(PARAM_INT_DEF_VAL) != oldBuiltFx.getIntVal(paramName))
newBuiltFx.setIntVal(paramName,oldBuiltFx.getIntVal(paramName));
case NvsFxDescription.ParamInfoObject.PARAM_TYPE_FLOAT:
newBuiltFx.setFloatVal(paramName,oldBuiltFx.getFloatVal(paramName));
case NvsFxDescription.ParamInfoObject.PARAM_TYPE_BOOL:
if(param.getBoolean(PARAM_BOOL_DEF_VAL) != oldBuiltFx.getBooleanVal(paramName))
newBuiltFx.setBooleanVal(paramName,oldBuiltFx.getBooleanVal(paramName));
case NvsFxDescription.ParamInfoObject.PARAM_TYPE_MENU:
newBuiltFx.setMenuVal(paramName,oldBuiltFx.getMenuVal(paramName));
case NvsFxDescription.ParamInfoObject.PARAM_TYPE_STRING:
if(param.getString(PARAM_STRING_DEF) != null && !param.getString(PARAM_STRING_DEF).equals(oldBuiltFx.getStringVal(paramName)))
newBuiltFx.setStringVal(paramName,oldBuiltFx.getStringVal(paramName));
case NvsFxDescription.ParamInfoObject.PARAM_TYPE_COLOR:
newBuiltFx.setColorVal(paramName,oldBuiltFx.getColorVal(paramName));
case NvsFxDescription.ParamInfoObject.PARAM_TYPE_POSITION2D:
newBuiltFx.setPosition2DVal(paramName,oldBuiltFx.getPosition2DVal(paramName));
case NvsFxDescription.ParamInfoObject.PARAM_TYPE_POSITION3D:
newBuiltFx.setPosition3DVal(paramName,oldBuiltFx.getPosition3DVal(paramName));
```

## `effects-transforms-169` `buildTimelineMaskClipInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:299`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `size()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `get()`, `getMaskInfoData()`

Simple sequence:

```java
public static void buildTimelineMaskClipInfo(NvsTimeline timeline, List<ClipInfo> clipInfoData) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip clip = videoTrack.getClipByIndex(i);
if ((clip != null) && (i < clipInfoData.size())) {
applyMask(clip, clipInfoData.get(i).getMaskInfoData());
```

## `effects-transforms-170` `buildFilterByTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:724`

API classes: `NvsTimeline`
Common calls: `instance()`, `getFilterFx()`

Simple sequence:

```java
public static void buildFilterByTimeline(NvsTimeline timeline) {
if (null == timeline) {
FilterItem filterItem = TimelineData.instance().getFilterFx();
applyFilterByTimeline(timeline, filterItem);
```

## `effects-transforms-171` `applyFilterByTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:739`

API classes: `NvsTimelineVideoFx`, `NvsTimeline`
Common calls: `getDuration()`, `setBooleanVal()`, `getFirstTimelineVideoFx()`, `removeTimelineVideoFx()`, `getFilterMode()`, `getIsCartoon()`, `addBuiltinTimelineVideoFx()`, `getStrokenOnly()`, `getGrayScale()`, `addPackagedTimelineVideoFx()`, `getPackageId()`, `setFilterIntensity()`

Simple sequence:

```java
public static void applyFilterByTimeline(NvsTimeline timeline, FilterItem filterItem) {
if ((null == timeline)) {
NvsTimelineVideoFx mCurrentFx = timeline.getFirstTimelineVideoFx();
if (null != mCurrentFx) {
timeline.removeTimelineVideoFx(mCurrentFx);
int mode = filterItem.getFilterMode();
NvsTimelineVideoFx videoFx = null;
if (mode == FilterItem.FILTERMODE_BUILTIN) {
if (filterItem.getIsCartoon()) {
videoFx = timeline.addBuiltinTimelineVideoFx(0, timeline.getDuration(), "Cartoon");
videoFx.setBooleanVal("Stroke Only", filterItem.getStrokenOnly());
videoFx.setBooleanVal("Grayscale", filterItem.getGrayScale());
videoFx = timeline.addPackagedTimelineVideoFx(0, timeline.getDuration(), filterItem.getPackageId());
videoFx.setFilterIntensity(filterItem.getIntensity());
```

## `effects-transforms-172` `applyExprVarByFilter`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:781`

API classes: `NvsColor`, `NvsFx`
Common calls: `isEmpty()`, `entrySet()`, `getKey()`, `getValue()`, `getFilterParam()`, `setExprVar()`, `getFilterColorParam()`, `setExprObjectVar()`

Simple sequence:

```java
public static void applyExprVarByFilter(NvsFx nvsFx, FilterItem filterItem) {
HashMap<String, Float> filterParam = filterItem.getFilterParam();
for (Map.Entry<String, Float> entry : entries) {
String key = entry.getKey();
Float value = entry.getValue();
nvsFx.setExprVar(key, value);
HashMap<String, NvsColor> filterColorParam = filterItem.getFilterColorParam();
if (!filterColorParam.isEmpty()) {
Set<Map.Entry<String, NvsColor>> entries = filterColorParam.entrySet();
for (Map.Entry<String, NvsColor> entry : entries) {
String key = entry.getKey();
NvsColor value = entry.getValue();
nvsFx.setExprObjectVar(key, value);
```

## `effects-transforms-173` `buildFilterByClip`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:814`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getFilePath()`, `getAbsPathByContentUri()`, `getContext()`, `equals()`, `clear()`, `getVideoTrackByIndex()`, `instance()`, `getClipInfoData()`, `getClipCount()`, `getClipByIndex()`, `size()`, `get()`

Simple sequence:

```java
public static boolean buildFilterByClip(NvsTimeline timeline, VideoClipFxInfo videoClipFxData) {
if (timeline == null) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
ArrayList<ClipInfo> clipInfos = TimelineData.instance().getClipInfoData();
int videoClipCount = videoTrack.getClipCount();
for (int i = 0; i < videoClipCount; i++) {
NvsVideoClip clip = videoTrack.getClipByIndex(i);
String clipFilPath = clip.getFilePath();
videoFilePath = clipInfoTemp.getFilePath();
videoFilePath = FileUtils.getAbsPathByContentUri(MSApplication.getContext(), videoFilePath);
if (TextUtils.equals(videoFilePath, clipFilPath)
&& (clip.getIndex() == clipInfoTemp.getTrackIndex())) {
if (MSApplication.CONTENT_FLAG) {
clipFilPath = FileUtils.getAbsPathByContentUri(MSApplication.getContext(), clipFilPath);
videoFilePath = FileUtils.getAbsPathByContentUri(MSApplication.getContext(), clipInfo.getFilePath());
clipFxData = clipInfo.getVideoClipFxInfo();
```

## `effects-transforms-174` `buildSingleClipFilter`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:896`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getFilePath()`, `getAbsPathByContentUri()`, `getContext()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `equals()`, `instance()`, `getVideoClipFxData()`

Simple sequence:

```java
public static boolean buildSingleClipFilter(NvsTimeline timeline, ClipInfo clipInfo, VideoClipFxInfo clipFxData) {
if (timeline == null || clipInfo == null) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
for (int i = 0; i < videoTrack.getClipCount(); i++) {
NvsVideoClip clip = videoTrack.getClipByIndex(i);
appendFilterFx(clip, TimelineData.instance().getVideoClipFxData());
```

## `effects-transforms-175` `appendFilterFx`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:942`

API classes: `NvsColor`, `NvsVideoFx`, `NvsVideoClip`
Common calls: `e()`, `entrySet()`, `getValue()`, `getKey()`, `isEmpty()`, `appendRawBuiltinFx()`, `setBooleanVal()`, `setFilterIntensity()`, `setFloatValAtTime()`, `getFxId()`, `getFxMode()`, `getFxIntensity()`

Simple sequence:

```java
private static void appendFilterFx(NvsVideoClip clip, VideoClipFxInfo videoClipFxData) {
String name = videoClipFxData.getFxId();
int mode = videoClipFxData.getFxMode();
float fxIntensity = videoClipFxData.getFxIntensity();
HashMap<Long, Double> keyFrameInfoMap = videoClipFxData.getKeyFrameInfoMap();
if (mode == FilterItem.FILTERMODE_BUILTIN) {
NvsVideoFx builtInFx;
if (videoClipFxData.getIsCartoon()) {
if (builtInFx != null) {
builtInFx.setBooleanVal("Stroke Only", videoClipFxData.getStrokenOnly());
builtInFx.setBooleanVal("Grayscale", videoClipFxData.getGrayScale());
if (builtInFx != null) {
builtInFx.setFilterIntensity(fxIntensity);
if (builtInFx != null) {
builtInFx.setFloatValAtTime("Filter Intensity", entry.getValue(), entry.getKey());
NvsVideoFx packagedFx = clip.appendRawPackagedFx(name);
if (packagedFx != null) {
packagedFx.setFilterIntensity(fxIntensity);
if (packagedFx != null) {
packagedFx.setFloatValAtTime("Filter Intensity", entry.getValue(), entry.getKey());
HashMap<String, Float> filterParam = videoClipFxData.getFilterParam();
for (Map.Entry<String, Float> entry : entries) {
String key = entry.getKey();
Float value = entry.getValue();
// ... 10 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-176` `setTransition`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1108`

API classes: `NvsVideoTransition`, `NvsTimeline`, `NvsVideoTrack`
Static/constants: `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE`, `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH`
Common calls: `getTransitionId()`, `setVideoTransitionDuration()`, `getTransitionInterval()`, `setPackagedTransition()`, `getVideoTrackByIndex()`, `getClipCount()`, `size()`, `get()`, `equals()`, `getTransitionMode()`, `setBuiltinTransition()`, `ismChangeTransitionDuration()`

Simple sequence:

```java
public static boolean setTransition(NvsTimeline timeline, ArrayList<TransitionInfo> transitionInfos) {
if (timeline == null) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
int videoClipCount = videoTrack.getClipCount();
NvsVideoTransition nvsVideoTransition = null;
if (TextUtils.equals(transitionInfo.getTransitionId(), "theme")) {
nvsVideoTransition = videoTrack.setPackagedTransition(i, transitionInfo.getTransitionId());
if (transitionInfo.getTransitionMode() == TransitionInfo.TRANSITIONMODE_BUILTIN) {
nvsVideoTransition = videoTrack.setBuiltinTransition(i, transitionInfo.getTransitionId());
nvsVideoTransition = videoTrack.setPackagedTransition(i, transitionInfo.getTransitionId());
if (transitionInfo.ismChangeTransitionDuration()) {
nvsVideoTransition.setVideoTransitionDuration(transitionInfo.getTransitionInterval(), NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH);
nvsVideoTransition.setVideoTransitionDuration(transitionInfo.getTransitionInterval(), NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE);
transitionInfo.setVideoTransition(nvsVideoTransition);
```

## `effects-transforms-177` `setTransition`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1166`

API classes: `NvsVideoTransition`, `NvsTimeline`, `NvsVideoTrack`
Static/constants: `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH`, `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE`
Common calls: `getTransitionId()`, `getVideoTransitionDuration()`, `setBuiltinTransition()`, `setPackagedTransition()`, `e()`, `getVideoTransitionDurationMatchMode()`, `setVideoTransitionDuration()`, `getTransitionInterval()`, `getVideoTrackByIndex()`, `getClipCount()`, `equals()`, `getTransitionMode()`

Simple sequence:

```java
public static boolean setTransition(NvsTimeline timeline, TransitionInfo transitionInfo, int index) {
if (timeline == null) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
int videoClipCount = videoTrack.getClipCount();
NvsVideoTransition nvsVideoTransition = null;
if (TextUtils.equals(transitionInfo.getTransitionId(), "theme")) {
videoTrack.setBuiltinTransition(index, "");
nvsVideoTransition = videoTrack.setPackagedTransition(index, transitionInfo.getTransitionId());
if (transitionInfo.getTransitionMode() == TransitionInfo.TRANSITIONMODE_BUILTIN) {
nvsVideoTransition = videoTrack.setBuiltinTransition(index, transitionInfo.getTransitionId());
nvsVideoTransition = videoTrack.setPackagedTransition(index, transitionInfo.getTransitionId());
if (nvsVideoTransition != null) {
Log.e("nvsVideoTransition", "pre duration=" + nvsVideoTransition.getVideoTransitionDuration() + " mode=" + nvsVideoTransition.getVideoTransitionDurationMatchMode());
transitionInfo.setVideoTransition(nvsVideoTransition);
nvsVideoTransition.setVideoTransitionDuration(transitionInfo.getTransitionInterval(), NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH);
nvsVideoTransition.setVideoTransitionDuration(transitionInfo.getTransitionInterval(), NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE);
Log.e("nvsVideoTransition", "duration=" + nvsVideoTransition.getVideoTransitionDuration() + " mode=" + nvsVideoTransition.getVideoTransitionDurationMatchMode());
```

## `effects-transforms-178` `applyAnimation`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1928`

API classes: `NvsConstants`, `NvsVideoFx`, `NvsVideoTransition`, `NvsVideoTrack`, `NvsVideoClip`
Static/constants: `NvsConstants.ANIMATION_PACKAGE_ID`, `NvsConstants.ANIMATION_POST_PACKAGE_ID`, `NvsConstants.ANIMATION_IS_POST_STORYBOARD_3D`, `NvsConstants.ANIMATION_ENABLE_MUTLISAMPLE`, `NvsConstants.ANIMATION_PACKAGE_EFFECT_IN`, `NvsConstants.ANIMATION_PACKAGE_EFFECT_OUT`
Common calls: `getVideoTransitionDuration()`, `setStringVal()`, `setBooleanVal()`, `setFloatVal()`, `getTransitionBySourceClipIndex()`, `getIndex()`, `getmPackageId()`, `enablePropertyVideoFx()`, `getPropertyVideoFx()`, `getmAnimationIn()`, `getmAnimationOut()`, `getmAssetType()`

Simple sequence:

```java
public static NvsVideoFx applyAnimation(NvsVideoTrack nvsVideoTrack, NvsVideoClip videoClip, AnimationInfo animationInfo) {
NvsVideoTransition preTrans = nvsVideoTrack.getTransitionBySourceClipIndex(videoClip.getIndex() - 1);
NvsVideoTransition transition = nvsVideoTrack.getTransitionBySourceClipIndex(videoClip.getIndex());
NvsVideoFx videoFx = videoClip.getPropertyVideoFx();
if (null != preTrans && null != transition) {
in += preTrans.getVideoTransitionDuration();
out += preTrans.getVideoTransitionDuration() + transition.getVideoTransitionDuration() * 0.5;
if (null != transition) {
out += 0.5 * transition.getVideoTransitionDuration();
videoFx.setStringVal(NvsConstants.ANIMATION_PACKAGE_ID, "");
videoFx.setStringVal(NvsConstants.ANIMATION_POST_PACKAGE_ID, "");
if (animationInfo.isPostPackage()) {
videoFx.setStringVal(NvsConstants.ANIMATION_POST_PACKAGE_ID, animationInfo.getmPackageId());
videoFx.setStringVal(NvsConstants.ANIMATION_PACKAGE_ID, animationInfo.getmPackageId());
videoFx.setBooleanVal(NvsConstants.ANIMATION_IS_POST_STORYBOARD_3D, false);
videoFx.setBooleanVal(NvsConstants.ANIMATION_ENABLE_MUTLISAMPLE, true);
mPositionerVideoFx.setBooleanVal("Enable Background Rotation", true);
mPositionerVideoFx.setMenuVal("Background Mode", "Blur");
mPositionerVideoFx.setFloatVal("Background Blur Radius", 40);*/
videoFx.setFloatVal(NvsConstants.ANIMATION_PACKAGE_EFFECT_IN, in);
videoFx.setFloatVal(NvsConstants.ANIMATION_PACKAGE_EFFECT_OUT, out);
videoFx.setExprVar("amplitude", amplitude);
```

## `effects-transforms-179` `buildColorAdjustInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1993`

API classes: `NvsVideoFx`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `setFloatVal()`, `equals()`, `appendBuiltinFx()`, `setAttachment()`, `size()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `get()`, `getCorrectionColorInfo()`, `getFxCount()`, `getFxByIndex()`, `getBuiltinVideoFxName()`

Simple sequence:

```java
mTimeline, ArrayList<ClipInfo> clipInfoArrayList) {
if (null == mTimeline || null == clipInfoArrayList || clipInfoArrayList.size() == 0) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
CorrectionColorInfo correctionColorInfo = clipInfo.getCorrectionColorInfo();
int fxCount = videoClip.getFxCount();
NvsVideoFx mColorVideoFx = null;
NvsVideoFx mVignetteVideoFx = null;
NvsVideoFx mSharpenVideoFx = null;
NvsVideoFx mTintVideoFx = null;
NvsVideoFx mDenoiseVideoFx = null;
for (int index = 0; index < fxCount; ++index) {
NvsVideoFx videoFx = videoClip.getFxByIndex(index);
String fxName = videoFx.getBuiltinVideoFxName();
mColorVideoFx.setAttachment(Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST, Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
mVignetteVideoFx.setAttachment(Constants.ADJUST_TYPE_VIGETTE, Constants.ADJUST_TYPE_VIGETTE);
mSharpenVideoFx.setAttachment(Constants.ADJUST_TYPE_SHARPEN, Constants.ADJUST_TYPE_SHARPEN);
mTintVideoFx.setAttachment(Constants.ADJUST_TYPE_TINT, Constants.ADJUST_TYPE_TINT);
mDenoiseVideoFx.setAttachment(Constants.ADJUST_TYPE_DENOISE, Constants.ADJUST_TYPE_DENOISE);
mColorVideoFx.setFloatVal(Constants.ADJUST_BRIGHTNESS, correctionColorInfo.getBrightnessVal());
mColorVideoFx.setFloatVal(Constants.ADJUST_CONTRAST, correctionColorInfo.getContrastVal());
mColorVideoFx.setFloatVal(Constants.ADJUST_SATURATION, correctionColorInfo.getSaturationVal());
mColorVideoFx.setFloatVal(Constants.ADJUST_HIGHTLIGHT, correctionColorInfo.getmHighLight());
mColorVideoFx.setFloatVal(Constants.ADJUST_SHADOW, correctionColorInfo.getmShadow());
// ... 7 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-180` `buildAdjustCutInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2237`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `size()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `get()`

Simple sequence:

```java
public static void buildAdjustCutInfo(NvsTimeline mTimeline, ArrayList<ClipInfo> clipInfoArrayList) {
if (null == mTimeline || null == clipInfoArrayList || clipInfoArrayList.size() == 0) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
for (int i = 0; i < clipInfoCount; i++) {
NvsVideoClip mVideoClip = videoTrack.getClipByIndex(i);
applyCropData(mTimeline, mVideoClip, clipInfo);
```

## `effects-transforms-181` `buildTimelineBackground`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2371`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `size()`, `get()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getBackGroundInfo()`

Simple sequence:

```java
public static void buildTimelineBackground(NvsTimeline mTimeline, ArrayList<ClipInfo> clipInfoData) {
if (null == clipInfoData || null == mTimeline) {
NvsVideoTrack videoTrackByIndex = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip clipByIndex = videoTrackByIndex.getClipByIndex(i);
applyBackground(clipByIndex, clipInfo.getBackGroundInfo());
```

## `effects-transforms-182` `buildTimelineBackground`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2376`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `get()`, `getVideoTrackByIndex()`, `getClipByIndex()`, `getBackGroundInfo()`

Simple sequence:

```java
NvsVideoTrack videoTrackByIndex = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip clipByIndex = videoTrackByIndex.getClipByIndex(i);
applyBackground(clipByIndex, clipInfo.getBackGroundInfo());
```

## `effects-transforms-183` `effect`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2397`

API classes: `NvsConstants`, `NvsVideoClip`, `NvsVideoFx`, `NvsColor`, `NvsVideoResolution`
Static/constants: `NvsConstants.PROPERTY_KEY_BACKGROUND_MODE`, `NvsConstants.PROPERTY_VALUE_BACKGROUND_COLOR_SOLID`, `NvsConstants.PROPERTY_KEY_BACKGROUND_IMAGE`, `NvsConstants.PROPERTY_KEY_BACKGROUND_COLOR`, `NvsConstants.PROPERTY_VALUE_BACKGROUND_IMAGE_FILE`, `NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR`, `NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR_NEW_MODE_ENABLE`, `NvsConstants.PROPERTY_KEY_BACKGROUND_BLUR_RADIUS`, `NvsConstants.PROPERTY_KEY_SCALE_X`, `NvsConstants.PROPERTY_KEY_SCALE_Y`, `NvsConstants.PROPERTY_KEY_TRANS_X`, `NvsConstants.PROPERTY_KEY_TRANS_Y`
Common calls: `setFloatVal()`, `setMenuVal()`, `getValue()`, `getInPoint()`, `getOutPoint()`, `setStringVal()`, `setColorVal()`, `getFilePath()`, `getType()`, `enablePropertyVideoFx()`, `getPropertyVideoFx()`, `colorStringtoNvsColor()`

Simple sequence:

```java
public static void applyBackground(NvsVideoClip videoClip, BackGroundInfo backGroundInfo) {
int type = backGroundInfo.getType();
NvsVideoFx bgFx = videoClip.getPropertyVideoFx();
if (type == BackGroundInfo.BackgroundType.BACKGROUND_COLOR) {
bgFx.setMenuVal(NvsConstants.PROPERTY_KEY_BACKGROUND_MODE, NvsConstants.PROPERTY_VALUE_BACKGROUND_COLOR_SOLID);
bgFx.setStringVal(NvsConstants.PROPERTY_KEY_BACKGROUND_IMAGE, "");
bgFx.setColorVal(NvsConstants.PROPERTY_KEY_BACKGROUND_COLOR, ColorUtil.colorStringtoNvsColor(backGroundInfo.getColorValue()));
if (!TextUtils.isEmpty(backGroundInfo.getFilePath())) {
bgFx.setMenuVal(NvsConstants.PROPERTY_KEY_BACKGROUND_MODE, NvsConstants.PROPERTY_VALUE_BACKGROUND_IMAGE_FILE);
bgFx.setStringVal(NvsConstants.PROPERTY_KEY_BACKGROUND_IMAGE, backGroundInfo.getFilePath());
bgFx.setMenuVal(NvsConstants.PROPERTY_KEY_BACKGROUND_MODE, NvsConstants.PROPERTY_VALUE_BACKGROUND_COLOR_SOLID);
bgFx.setColorVal(NvsConstants.PROPERTY_KEY_BACKGROUND_COLOR, new NvsColor(0, 0, 0, 0));
bgFx.setMenuVal(NvsConstants.PROPERTY_KEY_BACKGROUND_MODE, NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR);
bgFx.setBooleanVal(NvsConstants.PROPERTY_VALUE_BACKGROUND_BLUR_NEW_MODE_ENABLE, true);
Log.d(TAG, "backGroundInfo.getValue()=" + backGroundInfo.getValue());
bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_BACKGROUND_BLUR_RADIUS, backGroundInfo.getValue());
bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_SCALE_X, backGroundInfo.getScaleX());
bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_SCALE_Y, backGroundInfo.getScaleY());
bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_TRANS_X, backGroundInfo.getTransX());
bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_TRANS_Y, backGroundInfo.getTransY());
bgFx.setFloatVal(NvsConstants.PROPERTY_KEY_ROTATION, backGroundInfo.getRotation());
```

## `effects-transforms-184` `applyCropMaskData`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2613`

API classes: `NvsConstants`, `NvsVideoFx`, `NvsMaskRegionInfo`, `NvsPosition2D`, `NvsVideoClip`
Static/constants: `NvsConstants.KEY_MASK_GENERATOR_TYPE`, `NvsConstants.CUT_FX_TYPE_FOR_TRANSFORM`, `NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM`, `NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D`, `NvsMaskRegionInfo.RegionInfo`, `NvsConstants.CUT_KEY_MASK_GENERATOR`, `NvsConstants.CUT_KEY_IS_NORMALIZED_COORD`, `NvsConstants.KEY_CROPPER_TRANS_X`, `NvsConstants.KEY_CROPPER_TRANS_Y`, `NvsConstants.KEY_CROPPER_SCALE_X`, `NvsConstants.KEY_CROPPER_SCALE_Y`, `NvsConstants.KEY_CROPPER_ROTATION`
Common calls: `setFloatVal()`, `get()`, `getRawFxByIndex()`, `getAttachment()`, `appendRawBuiltinFx()`, `setAttachment()`, `equals()`, `setBooleanVal()`, `getCropInfo()`, `getRawFxCount()`, `getBuiltinVideoFxName()`, `getTransformData()`

Simple sequence:

```java
public static void applyCropMaskData(NvsVideoClip videoClip, ClipInfo clipInfo) {
CutData cropInfo = clipInfo.getCropInfo();
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
if (rawVideoFx != null && rawVideoFx.getAttachment(NvsConstants.CUT_FX_TYPE_FOR_TRANSFORM) != null) {
for (int i = 0; i < rawFxCount; i++) {
NvsVideoFx rawVideoFx = videoClip.getRawFxByIndex(i);
if (rawVideoFx != null && rawVideoFx.getAttachment(NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM) != null) {
if (extraTransformVideoFx == null) {
extraTransformVideoFx = videoClip.appendRawBuiltinFx(NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D);
if (transformVideoFx == null) {
transformVideoFx = videoClip.appendRawBuiltinFx(NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D);
Map<String, Float> transFromData = cropInfo.getTransformData();
if (extraTransformVideoFx != null) {
transformVideoFx.setAttachment(NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM, true);
// ... 29 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-185` `removeRawBuildInFx`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2718`

API classes: `NvsVideoClip`, `NvsVideoFx`
Common calls: `getRawFxCount()`, `getRawFxByIndex()`, `equals()`, `getBuiltinVideoFxName()`, `removeRawFx()`

Simple sequence:

```java
public static void removeRawBuildInFx(NvsVideoClip videoClip, String rawFxName) {
int rawFxCount = videoClip.getRawFxCount();
for (int i = 0; i < rawFxCount; i++) {
NvsVideoFx rawFx = videoClip.getRawFxByIndex(i);
if (rawFx != null && TextUtils.equals(rawFx.getBuiltinVideoFxName(), rawFxName)) {
videoClip.removeRawFx(i);
```

## `effects-transforms-186` `removeRawBuildInFx`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2723`

API classes: `NvsVideoFx`
Common calls: `getRawFxByIndex()`, `equals()`, `getBuiltinVideoFxName()`, `removeRawFx()`

Simple sequence:

```java
for (int i = 0; i < rawFxCount; i++) {
NvsVideoFx rawFx = videoClip.getRawFxByIndex(i);
if (rawFx != null && TextUtils.equals(rawFx.getBuiltinVideoFxName(), rawFxName)) {
videoClip.removeRawFx(i);
```

## `effects-transforms-187` `findOrCrateVideoFxFromVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2782`

API classes: `NvsVideoFx`
Common calls: `getRawFxByIndex()`, `getBuiltinVideoFxName()`, `equals()`, `removeRawFx()`

Simple sequence:

```java
for (int count = fxCount - 1; count >= 0; count--) {
NvsVideoFx fxByIndex = videoClip.getRawFxByIndex(count);
if (fxByIndex.getBuiltinVideoFxName().equals(Constants.AR_SCENE)) {
if (remove) {
videoClip.removeRawFx(count);
```

## `effects-transforms-188` `findOrCrateVideoFxFromVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2818`

API classes: `NvsVideoFx`, `NvsVideoClip`

Simple sequence:

```java
public static NvsVideoFx findOrCrateVideoFxFromVideoClip(NvsVideoClip clipByIndex) {
```

## `effects-transforms-189` `findVideoFxFromVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2829`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `getFxCount()`, `getFxByIndex()`, `getBuiltinVideoFxName()`, `equals()`

Simple sequence:

```java
public static NvsVideoFx findVideoFxFromVideoClip(NvsVideoClip clipByIndex) {
int fxCount = clipByIndex.getFxCount();
for (int i = 0; i < fxCount; i++) {
NvsVideoFx fxByIndex = clipByIndex.getFxByIndex(i);
if (fxByIndex.getBuiltinVideoFxName().equals(Constants.AR_SCENE)) {
```

## `effects-transforms-190` `findVideoFxFromVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2834`

API classes: `NvsVideoFx`
Common calls: `getFxByIndex()`, `getBuiltinVideoFxName()`, `equals()`

Simple sequence:

```java
for (int i = 0; i < fxCount; i++) {
NvsVideoFx fxByIndex = clipByIndex.getFxByIndex(i);
if (fxByIndex.getBuiltinVideoFxName().equals(Constants.AR_SCENE)) {
```

## `effects-transforms-191` `getFilterFxs`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2850`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoFx`
Common calls: `e()`, `getFxCount()`, `videoTrackCount()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `getRawFxCount()`, `getFxByIndex()`, `getBuiltinVideoFxName()`, `getVideoFxPackageId()`

Simple sequence:

```java
public static void logTimeline(NvsTimeline timeline) {
for (int i = 0; i < timeline.videoTrackCount(); i++) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(i);
for (int i1 = 0; i1 < videoTrack.getClipCount(); i1++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i1);
Log.e(TAG, "logTimeline videoClip.getFxCount: " + videoClip.getFxCount() + "  getRawFxCount: " + videoClip.getRawFxCount());
int fxCount = videoClip.getFxCount();
for (int i2 = 0; i2 < fxCount; i2++) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i2);
Log.e(TAG, "logTimeline getBuiltinVideoFxName: " + videoFx.getBuiltinVideoFxName()
+ "  " + videoFx.getVideoFxPackageId());
```

## `effects-transforms-192` `logTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2854`

API classes: `NvsVideoClip`, `NvsVideoFx`
Common calls: `e()`, `getFxCount()`, `getClipCount()`, `getClipByIndex()`, `getRawFxCount()`, `getFxByIndex()`, `getBuiltinVideoFxName()`, `getVideoFxPackageId()`

Simple sequence:

```java
for (int i1 = 0; i1 < videoTrack.getClipCount(); i1++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i1);
Log.e(TAG, "logTimeline videoClip.getFxCount: " + videoClip.getFxCount() + "  getRawFxCount: " + videoClip.getRawFxCount());
int fxCount = videoClip.getFxCount();
for (int i2 = 0; i2 < fxCount; i2++) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i2);
Log.e(TAG, "logTimeline getBuiltinVideoFxName: " + videoFx.getBuiltinVideoFxName()
+ "  " + videoFx.getVideoFxPackageId());
```

## `effects-transforms-193` `compileVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:48`

API classes: `NvsStreamingContext`, `NvsVideoResolution`
Static/constants: `NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME`, `NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER`, `NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_HARDWARE_ENCODER`, `NvsStreamingContext.COMPILE_BITRATE`, `NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT`, `NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM`, `NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE`
Common calls: `instance()`, `put()`, `d()`, `setCompileConfigurations()`, `isSupportHEVC()`, `getExportConfig()`, `compileTimeline()`, `isEmpty()`, `stop()`, `getCompileBitrate()`, `disableDeviceEncorder()`, `getBitDepth()`

Simple sequence:

```java
if (context == null || timeline == null || compileVideoPath.isEmpty()) {
context.stop();
context.setCompileConfigurations(null);
double bitrate = ParameterSettingValues.instance().getCompileBitrate();
if (ParameterSettingValues.instance().disableDeviceEncorder()) {
encoderFlag = NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_HARDWARE_ENCODER;
if (bitrate != 0) {
compileConfigurations.put(NvsStreamingContext.COMPILE_BITRATE, bitrate * 1000000);
if (settingValues.isSupportHEVC()) {
compileConfigurations.put(NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME, Constants.HDR_EXPORT_HEVC);
Log.d("ParameterSetting", "compile name:" + NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME + " value:" + Constants.HDR_EXPORT_HEVC);
if (settingValues.getBitDepth() != NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT) {
compileConfigurations.put(NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER, settingValues.getExportConfig());
Log.d("ParameterSetting", "compile name:" + NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER +
" value:" + settingValues.getExportConfig());
Hashtable<String, Object> compileConfigurations1 = VideoCompileUtil.getCompileConfigurations(compileConfigurations);
context.setCompileConfigurations(compileConfigurations1);
if (customHeight != -1) {
context.setCustomCompileVideoHeight(customHeight);
context.compileTimeline(timeline, startTime, endTime, compileVideoPath,
NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, encoderFlag
| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME
| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME
| NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE);
// ... 4 more SDK-related lines omitted in this compressed snippet ...
```

## `effects-transforms-194` `setClipTrans`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java:80`

API classes: `NvsVideoFx`
Common calls: `put()`, `getKey()`, `setStringVal()`

Simple sequence:

```java
mMeicamFxParam.put(param.getKey(), param);
```

## `effects-transforms-195` `getStoryboardFx`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/StoryboardInfo.java:140`

API classes: `NvsVideoFx`
Common calls: `getFxByIndex()`, `getAttachment()`, `equals()`

Simple sequence:

```java
for (int index = 0; index < fxCount; index++) {
NvsVideoFx clipFx = videoClip.getFxByIndex(index);
Object attachment = clipFx.getAttachment(ATTACHMENT_KEY_SUB_TYPE);
```

## `effects-transforms-196` `setTransitionInterval`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TransitionInfo.java:37`

API classes: `NvsVideoTransition`

Simple sequence:

```java
public NvsVideoTransition getVideoTransition() {
```

## `effects-transforms-197` `getVideoTransition`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TransitionInfo.java:41`

API classes: `NvsVideoTransition`

Simple sequence:

```java
public void setVideoTransition(NvsVideoTransition videoTransition) {
```

## `effects-transforms-198` `getFilterColorParam`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/VideoClipFxInfo.java:134`

API classes: `NvsColor`
Common calls: `put()`

Simple sequence:

```java
public void putFilterColorParam(String key, NvsColor value) {
```

## `effects-transforms-199` `setAdjustEffect`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:563`

API classes: `NvsVideoFx`, `NvsConstants`, `NvsVideoClip`
Static/constants: `NvsConstants.KEY_VIDEO_MODE`
Common calls: `setFloatVal()`, `setBooleanVal()`, `getFxCount()`, `getFxByIndex()`, `getAttachment()`, `equals()`, `appendBuiltinFx()`, `setAttachment()`

Simple sequence:

```java
private void setAdjustEffect(NvsVideoClip videoClip, float adjustData, String adjustKey, String attachmentKey) {
NvsVideoFx nvsVideoFx = null;
int fxCount = videoClip.getFxCount();
for (int i = 0; i < fxCount; i++) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
if (videoFx != null) {
Object attachment = videoFx.getAttachment(attachmentKey);
if (nvsVideoFx != null) {
nvsVideoFx.setFloatVal(adjustKey, adjustData);
nvsVideoFx.setBooleanVal(NvsConstants.KEY_VIDEO_MODE, true);
nvsVideoFx.setAttachment(attachmentKey, attachmentKey);
nvsVideoFx.setFloatVal(adjustKey, adjustData);
nvsVideoFx.setBooleanVal(NvsConstants.KEY_VIDEO_MODE, true);
```

## `effects-transforms-200` `setAdjustEffect`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:566`

API classes: `NvsVideoFx`
Common calls: `getFxByIndex()`, `getAttachment()`, `equals()`

Simple sequence:

```java
for (int i = 0; i < fxCount; i++) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
if (videoFx != null) {
Object attachment = videoFx.getAttachment(attachmentKey);
```

## `effects-transforms-201` `setTimelineAdjustEffect`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:592`

API classes: `NvsTimelineVideoFx`
Common calls: `size()`, `get()`, `getAttachment()`, `equals()`

Simple sequence:

```java
for (int i = 0; i < timelineVideoFxByTimelinePosition.size(); i++) {
NvsTimelineVideoFx nvsTimelineVideoFx = timelineVideoFxByTimelinePosition.get(i);
Object attachment = nvsTimelineVideoFx.getAttachment(attachmentKey);
```

## `effects-transforms-202` `setTimelineAdjustEffect`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:593`

API classes: `NvsTimelineVideoFx`
Common calls: `size()`, `get()`, `getAttachment()`, `equals()`

Simple sequence:

```java
for (int i = 0; i < timelineVideoFxByTimelinePosition.size(); i++) {
NvsTimelineVideoFx nvsTimelineVideoFx = timelineVideoFxByTimelinePosition.get(i);
Object attachment = nvsTimelineVideoFx.getAttachment(attachmentKey);
```

## `effects-transforms-203` `applyTransform`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1061`

API classes: `NvsVideoTransition`
Common calls: `addMainTransition()`, `getEffectMode()`, `getEffectId()`, `getCoverId()`, `getPackageId()`, `getCoverPath()`, `setDuration()`, `bindToTimeline()`, `getMainTrack()`, `getObject()`, `loadData()`

Simple sequence:

```java
if (baseInfo.getEffectMode() == BaseInfo.EFFECT_MODE_BUILTIN) {
desc = baseInfo.getEffectId();
meicamTransitionInfo = new MeicamTransition(targetTransitionIndex , TYPE_BUILD_IN, desc, baseInfo.getCoverId());
desc = baseInfo.getPackageId();
meicamTransitionInfo = new MeicamTransition(targetTransitionIndex , TYPE_PACKAGE, desc, baseInfo.getCoverPath());
meicamTransitionInfo.setDuration(duration);
NvsVideoTransition videoTransition = meicamTransitionInfo.bindToTimeline(TimelineDataUtil.getMainTrack().getObject());
```

## `effects-transforms-204` `applyEffect`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1123`

API classes: `NvsTimelineVideoFx`
Common calls: `isEmpty()`, `setDesc()`, `setClipType()`, `getInstance()`, `add()`, `getAssetPath()`, `getEffectMode()`, `getEffectId()`, `getPackageId()`, `setDisplayName()`, `getName()`, `getInPoint()`

Simple sequence:

```java
String packagePath = baseInfo.getAssetPath();
if (baseInfo.getEffectMode() == BaseInfo.EFFECT_MODE_BUILTIN) {
effect.setDesc(baseInfo.getEffectId());
effect.setClipType(EFFECT_BUILTIN);
effect.setDesc(baseInfo.getPackageId());
effect.setClipType(EFFECT_PACKAGE);
effect.setDisplayName(baseInfo.getName());
if (meicamTimelineVideoFxClip != null) {
inPoint = meicamTimelineVideoFxClip.getInPoint();
long titleThemeDuration = TimelineData.getInstance().getTitleThemeDuration();
effect.setInPoint(inPoint);
effect.setOutPoint(inPoint + effectDuration);
effect.setIntensity(1.0f);
NvsTimelineVideoFx timelineVideoFx = effect.bindToTimeline(mTimeline);
if (timelineVideoFx != null) {
List<MeicamTimelineVideoFxTrack> videoFxTrackList = TimelineData.getInstance().getMeicamTimelineVideoFxTrackList();
videoFxTrack.getClipInfoList().add(effect);
effect.setIndex(videoFxTrackList.size() - 1);
mOnTimelineChangeListener.onTimelineChanged(mTimeline, true);
```

## `effects-transforms-205` `getMaskTargetFx`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2965`

API classes: `NvsConstants`
Static/constants: `NvsConstants.KEY_MASK_GENERATOR`
Common calls: `equals()`, `size()`, `getSubType()`, `getDesc()`, `e()`, `getVideoFxs()`, `get()`, `isEmpty()`

Simple sequence:

```java
List<MeicamVideoFx> videoFxs = meicamVideoClip.getVideoFxs();
if (TextUtils.isEmpty(meicamVideoFx.getSubType())) {
if (meicamVideoFx.getDesc().equals(NvsConstants.KEY_MASK_GENERATOR)) {
if (SUB_TYPE_MASK.equals(meicamVideoFx.getSubType()) && meicamVideoFx.getDesc().equals(NvsConstants.KEY_MASK_GENERATOR)) {
```

## `effects-transforms-206` `setRevert`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamMaskRegionInfo.java:32`

API classes: `NvsMaskRegionInfo`

Simple sequence:

```java
public void setMaskRegionInfo(NvsMaskRegionInfo maskRegionInfo) {
```

## `effects-transforms-207` `setMaskRegionInfo`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamMaskRegionInfo.java:36`

API classes: `NvsMaskRegionInfo`

Simple sequence:

```java
public NvsMaskRegionInfo getMaskRegionInfo() {
```

## `effects-transforms-208` `setMeicamFxParamList`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java:151`

API classes: `NvsTimelineVideoFx`, `NvsTimeline`
Common calls: `addBuiltinTimelineVideoFx()`, `addPackagedTimelineVideoFx()`

Simple sequence:

```java
public NvsTimelineVideoFx bindToTimeline(NvsTimeline timeline) {
if (timeline == null) {
NvsTimelineVideoFx nvsTimelineVideoFx;
if (EFFECT_BUILTIN == clipType) {
nvsTimelineVideoFx = timeline.addBuiltinTimelineVideoFx(getInPoint(), getOutPoint() - getInPoint(), desc);
nvsTimelineVideoFx = timeline.addPackagedTimelineVideoFx(getInPoint(), getOutPoint() - getInPoint(), desc);
```

## `effects-transforms-209` `clone`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTimelineVideoFxClip.java:187`

API classes: `NvsLiveWindowExt`
Common calls: `add()`, `mapNormalizedToView()`, `size()`, `get()`, `equals()`, `getValue()`, `parseFloat()`, `toString()`, `clear()`

Simple sequence:

```java
public void setPointList(NvsLiveWindowExt mLiveWindow) {
if (meicamFxParam.type.equals("float[]") && meicamFxParam.key.equals("Unit Size")) {
Object value = meicamFxParam.getValue();
list.add(mLiveWindow.mapNormalizedToView(leftTop));
list.add(mLiveWindow.mapNormalizedToView(leftBottom));
list.add(mLiveWindow.mapNormalizedToView(rightBottom));
list.add(mLiveWindow.mapNormalizedToView(rightTop));
```

## `effects-transforms-210` `getDuration`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamTransition.java:155`

API classes: `NvsVideoTransition`
Static/constants: `NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE`
Common calls: `setVideoTransitionDuration()`

Simple sequence:

```java
NvsVideoTransition object = getObject();
if (object != null) {
object.setVideoTransitionDuration(duration, NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_NONE);
```

## `effects-transforms-211` `loadData`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:180`

API classes: `NvsVideoClip`
Common calls: `getFilePath()`, `getInPoint()`, `getOutPoint()`, `getPlayInReverse()`, `getTrimIn()`, `getTrimOut()`, `getSpeed()`, `getExtraVideoRotation()`, `getRoleInTheme()`, `getOpacity()`

Simple sequence:

```java
public void loadData(NvsVideoClip videoClip) {
setInPoint(videoClip.getInPoint());
setOutPoint(videoClip.getOutPoint());
isVideoReverse = videoClip.getPlayInReverse();
if (isVideoReverse) {
reverseFilePath = videoClip.getFilePath();
filePath = videoClip.getFilePath();
trimIn = videoClip.getTrimIn();
trimOut = videoClip.getTrimOut();
speed = videoClip.getSpeed();
extraRotation = videoClip.getExtraVideoRotation();
mRoleInTheme = videoClip.getRoleInTheme();
opacity = videoClip.getOpacity();
```

## `effects-transforms-212` `getResourceId`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:503`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `isEmpty()`, `get()`, `getObject()`, `removeFx()`, `getIndex()`, `remove()`

Simple sequence:

```java
NvsVideoFx nvsVideoFx = backgroundInfo.getObject();
NvsVideoClip object = getObject();
if (object != null) {
object.removeFx(nvsVideoFx.getIndex());
```

## `effects-transforms-213` `removeNvsVideoFx`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:660`

API classes: `NvsVideoFx`
Common calls: `getObject()`, `removeFx()`, `getIndex()`, `e()`, `fillInStackTrace()`

Simple sequence:

```java
if (filterFx != null) {
NvsVideoFx nvsVideoFx = filterFx.getObject();
if (nvsVideoFx != null) {
getObject().removeFx(nvsVideoFx.getIndex());
```

## `effects-transforms-214` `removeNvsVideoFx`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:661`

API classes: `NvsVideoFx`
Common calls: `getObject()`, `removeFx()`, `getIndex()`

Simple sequence:

```java
if (filterFx != null) {
NvsVideoFx nvsVideoFx = filterFx.getObject();
if (nvsVideoFx != null) {
getObject().removeFx(nvsVideoFx.getIndex());
```

## `effects-transforms-215` `setDefaultBackground`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:802`

API classes: `NvsConstants`
Static/constants: `NvsConstants.PROPERTY_FX`
Common calls: `setDesc()`, `setType()`, `add()`

Simple sequence:

```java
meicamVideoFx.setDesc(NvsConstants.PROPERTY_FX);
meicamVideoFx.setType(CommonData.TYPE_PROPERTY);
```

## `effects-transforms-216` `removeVideoFx`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1017`

API classes: `NvsConstants`
Static/constants: `NvsConstants.KEY_MASK_GENERATOR`
Common calls: `getObject()`, `getIndex()`, `equals()`, `removeRawFx()`, `removeFx()`, `remove()`

Simple sequence:

```java
if (filterFx != null) {
if (NvsConstants.KEY_MASK_GENERATOR.equals(type) && BaseConstants.EnableRawFilterMaskRender) {
getObject().removeRawFx(filterFx.getObject().getIndex());
getObject().removeFx(filterFx.getObject().getIndex());
```

## `effects-transforms-217` `removeVideoFx`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1018`

API classes: `NvsConstants`
Static/constants: `NvsConstants.KEY_MASK_GENERATOR`
Common calls: `getObject()`, `getIndex()`, `equals()`, `removeRawFx()`, `removeFx()`

Simple sequence:

```java
if (NvsConstants.KEY_MASK_GENERATOR.equals(type) && BaseConstants.EnableRawFilterMaskRender) {
getObject().removeRawFx(filterFx.getObject().getIndex());
getObject().removeFx(filterFx.getObject().getIndex());
```

## `effects-transforms-218` `setAdjustEffect`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1057`

API classes: `NvsVideoFx`
Common calls: `getFxByIndex()`, `getAttachment()`, `equals()`

Simple sequence:

```java
for (int i = 0; i < fxCount; i++) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
if (videoFx != null) {
Object attachment = videoFx.getAttachment(attachmentKey);
```

## `effects-transforms-219` `setMaskRegionInfoData`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:129`

API classes: `NvsVideoFx`
Common calls: `setFilterIntensity()`

Simple sequence:

```java
NvsVideoFx object = getObject();
if (object != null) {
object.setFilterIntensity(intensity);
```

## `effects-transforms-220` `setMeicamFxParam`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:145`

API classes: `NvsVideoFx`
Common calls: `containsKey()`, `remove()`, `put()`, `getKey()`, `setStringVal()`

Simple sequence:

```java
mMeicamFxParam.put(param.getKey(), param);
NvsVideoFx object = getObject();
if (object != null) {
object.setStringVal(key, value);
```

## `effects-transforms-221` `bindToTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:243`

API classes: `NvsConstants`, `NvsVideoFx`, `NvsVideoClip`
Static/constants: `NvsConstants.KEY_MASK_GENERATOR`, `NvsConstants.KEY_MASK_KEEP_RGB`, `NvsConstants.KEY_MASK_INVERSE_REGION`, `NvsConstants.KEY_MASK_REGION_INFO`, `NvsConstants.KEY_MASK_FEATHER_WIDTH`
Common calls: `equals()`, `appendRawBuiltinFx()`, `setBooleanVal()`, `appendBuiltinFx()`, `appendPackagedFx()`, `setFilterIntensity()`, `setAttachment()`, `isRevert()`, `setArbDataVal()`, `getMaskRegionInfo()`, `setFloatVal()`, `getFeatherWidth()`

Simple sequence:

```java
public NvsVideoFx bindToTimeline(NvsVideoClip videoClip) {
NvsVideoFx videoFx = null;
if (TYPE_BUILD_IN.equals(type)) {
if (NvsConstants.KEY_MASK_GENERATOR.equals(desc) && BaseConstants.EnableRawFilterMaskRender) {
videoFx.setFilterIntensity(getIntensity());
videoFx.setAttachment(ATTACHMENT_KEY_SUB_TYPE, getSubType());
if (null != meicamMaskRegionInfo) {
videoFx.setBooleanVal(NvsConstants.KEY_MASK_KEEP_RGB, true);
videoFx.setBooleanVal(NvsConstants.KEY_MASK_INVERSE_REGION, meicamMaskRegionInfo.isRevert());
videoFx.setArbDataVal(NvsConstants.KEY_MASK_REGION_INFO, meicamMaskRegionInfo.getMaskRegionInfo());
videoFx.setFloatVal(NvsConstants.KEY_MASK_FEATHER_WIDTH, meicamMaskRegionInfo.getFeatherWidth());
setDesc(videoFx.getBuiltinVideoFxName());
```

## `effects-transforms-222` `bindToTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:248`

API classes: `NvsConstants`
Static/constants: `NvsConstants.KEY_MASK_GENERATOR`
Common calls: `equals()`, `appendRawBuiltinFx()`, `appendBuiltinFx()`, `appendPackagedFx()`

Simple sequence:

```java
if (TYPE_BUILD_IN.equals(type)) {
if (NvsConstants.KEY_MASK_GENERATOR.equals(desc) && BaseConstants.EnableRawFilterMaskRender) {
```

## `effects-transforms-223` `setValue`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:278`

API classes: `NvsArbitraryData`, `NvsMaskRegionInfo`
Common calls: `getType()`, `equals()`, `getValue()`, `setFloatVal()`, `setArbDataVal()`, `get()`, `setStringVal()`, `setBooleanVal()`, `getGson()`, `toJson()`, `fromJson()`, `e()`

Simple sequence:

```java
if (TYPE_STRING.equals(meicamFxParam.getType())) {
videoFx.setStringVal(key, (String) meicamFxParam.getValue());
} else if (TYPE_BOOLEAN.equals(meicamFxParam.getType())) {
videoFx.setBooleanVal(key, (Boolean) meicamFxParam.getValue());
} else if (TYPE_FLOAT.equals(meicamFxParam.getType())) {
Object value = meicamFxParam.getValue();
videoFx.setFloatVal(key, floatValue);
videoFx.setFloatVal(key, (Double) value);
} else if (TYPE_OBJECT.equals(meicamFxParam.getType())) {
Object value = meicamFxParam.getValue();
if (value instanceof NvsArbitraryData) {
videoFx.setArbDataVal(key, (NvsArbitraryData) value);
try {
Gson gson = GsonUtils.getGson();
Type type = new TypeToken<NvsMaskRegionInfo>() {
}.getType();
NvsMaskRegionInfo result = gson.fromJson(json, type);
if (result != null) {
videoFx.setArbDataVal(key, result);
LogUtils.e("error:" + e.getMessage());
```

## `effects-transforms-224` `setValue`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoFx.java:280`

API classes: `NvsArbitraryData`, `NvsMaskRegionInfo`
Common calls: `getType()`, `equals()`, `getValue()`, `setFloatVal()`, `setArbDataVal()`, `setStringVal()`, `setBooleanVal()`, `getGson()`, `toJson()`, `fromJson()`, `e()`, `getMessage()`

Simple sequence:

```java
if (TYPE_STRING.equals(meicamFxParam.getType())) {
videoFx.setStringVal(key, (String) meicamFxParam.getValue());
} else if (TYPE_BOOLEAN.equals(meicamFxParam.getType())) {
videoFx.setBooleanVal(key, (Boolean) meicamFxParam.getValue());
} else if (TYPE_FLOAT.equals(meicamFxParam.getType())) {
Object value = meicamFxParam.getValue();
videoFx.setFloatVal(key, floatValue);
videoFx.setFloatVal(key, (Double) value);
} else if (TYPE_OBJECT.equals(meicamFxParam.getType())) {
Object value = meicamFxParam.getValue();
if (value instanceof NvsArbitraryData) {
videoFx.setArbDataVal(key, (NvsArbitraryData) value);
try {
Gson gson = GsonUtils.getGson();
Type type = new TypeToken<NvsMaskRegionInfo>() {
}.getType();
NvsMaskRegionInfo result = gson.fromJson(json, type);
if (result != null) {
videoFx.setArbDataVal(key, result);
LogUtils.e("error:" + e.getMessage());
```

## `effects-transforms-225` `setResourceId`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamWaterMark.java:98`

API classes: `NvsLiveWindowExt`, `NvsTimeline`, `NvsVideoResolution`
Common calls: `add()`, `mapCanonicalToView()`, `e()`, `clear()`, `getVideoRes()`

Simple sequence:

```java
public void setPointList(NvsLiveWindowExt mLiveWindow, NvsTimeline nvsTimeline) {
NvsVideoResolution resolution = nvsTimeline.getVideoRes();
list.add(mLiveWindow.mapCanonicalToView(leftTop));
list.add(mLiveWindow.mapCanonicalToView(leftBottom));
list.add(mLiveWindow.mapCanonicalToView(rightBottom));
list.add(mLiveWindow.mapCanonicalToView(rightTop));
```

## `effects-transforms-226` `verifyTransition`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1229`

API classes: `NvsVideoTrack`, `NvsVideoTransition`
Common calls: `getTransitionInfoList()`, `getObject()`, `getClipCount()`, `getTransitionBySourceClipIndex()`, `contains()`, `setBuiltinTransition()`

Simple sequence:

```java
List<MeicamTransition> transitionInfoList = meicamVideoTrack.getTransitionInfoList();
NvsVideoTrack videoTrack = meicamVideoTrack.getObject();
int clipCount = videoTrack.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoTransition nvsVideoTransition = videoTrack.getTransitionBySourceClipIndex(i);
if (!transitionInfoList.contains(meicamTransition)) {
videoTrack.setBuiltinTransition(i, "");
```

## `effects-transforms-227` `findPropertyFx`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1248`

API classes: `NvsConstants`
Static/constants: `NvsConstants.PROPERTY_FX`
Common calls: `getVideoFxs()`, `equals()`

Simple sequence:

```java
List<MeicamVideoFx> list = videoClip.getVideoFxs();
for (MeicamVideoFx fx : list) {
if (NvsConstants.PROPERTY_FX.equals(fx.desc)) {
```

## `effects-transforms-228` `findPropertyFx`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1253`

API classes: `NvsConstants`
Static/constants: `NvsConstants.PROPERTY_FX`
Common calls: `equals()`

Simple sequence:

```java
for (MeicamVideoFx fx : list) {
if (NvsConstants.PROPERTY_FX.equals(fx.desc)) {
```

## `effects-transforms-229` `resetPropertyAnimation`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1267`

API classes: `NvsConstants`
Static/constants: `NvsConstants.POST_PACKAGE_ID`, `NvsConstants.IS_POST_STORY_BOARD_3D`, `NvsConstants.PACKAGE_EFFECT_IN`, `NvsConstants.PACKAGE_EFFECT_OUT`
Common calls: `setFloatVal()`, `setStringVal()`, `setBooleanVal()`

Simple sequence:

```java
if (meicamVideoFx != null) {
meicamVideoFx.setStringVal(NvsConstants.POST_PACKAGE_ID, "");
meicamVideoFx.setBooleanVal(NvsConstants.IS_POST_STORY_BOARD_3D, false);
meicamVideoFx.setFloatVal(NvsConstants.PACKAGE_EFFECT_IN, 0);
meicamVideoFx.setFloatVal(NvsConstants.PACKAGE_EFFECT_OUT, 0);
```

## `effects-transforms-230` `resetPropertyAnimation`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1269`

API classes: `NvsConstants`
Static/constants: `NvsConstants.POST_PACKAGE_ID`, `NvsConstants.IS_POST_STORY_BOARD_3D`, `NvsConstants.PACKAGE_EFFECT_IN`, `NvsConstants.PACKAGE_EFFECT_OUT`
Common calls: `setFloatVal()`, `setStringVal()`, `setBooleanVal()`

Simple sequence:

```java
if (meicamVideoFx != null) {
meicamVideoFx.setStringVal(NvsConstants.POST_PACKAGE_ID, "");
meicamVideoFx.setBooleanVal(NvsConstants.IS_POST_STORY_BOARD_3D, false);
meicamVideoFx.setFloatVal(NvsConstants.PACKAGE_EFFECT_IN, 0);
meicamVideoFx.setFloatVal(NvsConstants.PACKAGE_EFFECT_OUT, 0);
```

## `effects-transforms-231` `LogMainTrack`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1298`

API classes: `NvsVideoClip`
Common calls: `e()`, `getInPoint()`, `getOutPoint()`, `getTrimIn()`, `getTrimOut()`, `getSpeed()`, `getObject()`

Simple sequence:

```java
Log.e(TAG, "LogMainTrack: getInPoint: " + videoClip.getInPoint() + "  getOutPoint: " + videoClip.getOutPoint() + "  getTrimIn: " + videoClip.getTrimIn()
+ "  getTrimOut: " + videoClip.getTrimOut() + "  getSpeed: " + videoClip.getSpeed());
NvsVideoClip videoClip1 = videoClip.getObject();
Log.e(TAG, "LogMainTrack: getInPoint: " + videoClip1.getInPoint() + "  getOutPoint: " + videoClip1.getOutPoint() + "  getTrimIn: " + videoClip1.getTrimIn()
+ "  getTrimOut: " + videoClip1.getTrimOut() + "  getSpeed: " + videoClip1.getSpeed());
```

## `effects-transforms-232` `setClipTrans`

Source: `libEngine/src/main/java/com/meishe/engine/bean/background/MeicamStoryboardInfo.java:74`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `equals()`, `getType()`, `getValue()`, `appendBuiltinFx()`, `e()`, `keySet()`, `get()`, `setStringVal()`, `setBooleanVal()`, `setAttachment()`, `getIndex()`

Simple sequence:

```java
public NvsVideoFx bindToTimelineByType(NvsVideoClip videoClip, String type) {
NvsVideoFx nvsVideoFx = getStoryboardFx(videoClip, type);
if (TYPE_STRING.equals(meicamFxParam.getType()) || TYPE_STRING_OLD.equals(meicamFxParam.getType())) {
nvsVideoFx.setStringVal(key, (String) meicamFxParam.getValue());
} else if (TYPE_BOOLEAN.equals(meicamFxParam.getType())) {
nvsVideoFx.setBooleanVal(key, (Boolean) meicamFxParam.getValue());
if (nvsVideoFx != null) {
nvsVideoFx.setAttachment(ATTACHMENT_KEY_SUB_TYPE, type);
setIndex(nvsVideoFx.getIndex());
```

## `effects-transforms-233` `setmRevert`

Source: `libEngine/src/main/java/com/meishe/engine/local/LMeicamMaskRegionInfo.java:30`

API classes: `NvsMaskRegionInfo`

Simple sequence:

```java
public void setMaskRegionInfo(NvsMaskRegionInfo maskRegionInfo) {
```

## `effects-transforms-234` `setMaskRegionInfo`

Source: `libEngine/src/main/java/com/meishe/engine/local/LMeicamMaskRegionInfo.java:34`

API classes: `NvsMaskRegionInfo`

Simple sequence:

```java
public NvsMaskRegionInfo getMaskRegionInfo() {
```

## `effects-transforms-235` `setAdjustEffect`

Source: `libEngine/src/main/java/com/meishe/engine/local/LMeicamVideoClip.java:436`

API classes: `NvsVideoFx`
Common calls: `getFxByIndex()`, `getAttachment()`, `equals()`

Simple sequence:

```java
for (int i = 0; i < fxCount; i++) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
if (videoFx != null) {
Object attachment = videoFx.getAttachment(attachmentKey);
```

## `effects-transforms-236` `colorToNvsColor`

Source: `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java:20`

API classes: `NvsColor`
Common calls: `isEmpty()`, `parseColor()`

Simple sequence:

```java
public static NvsColor colorToNvsColor(String colorString) {
NvsColor color = new NvsColor(1, 1, 1, 1);
```

## `effects-transforms-237` `colorFloatToNvsColor`

Source: `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java:57`

API classes: `NvsColor`

Simple sequence:

```java
public static NvsColor colorFloatToNvsColor(float[] colorString) {
return new NvsColor(colorString[0], colorString[1], colorString[2], colorString[3]);
```

## `effects-transforms-238` `getColorArray`

Source: `libEngine/src/main/java/com/meishe/engine/util/ColorUtil.java:72`

API classes: `NvsColor`

Simple sequence:

```java
public static float[] getColorArray(NvsColor nvsColor) {
```

## `effects-transforms-239` `setTimelineData`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:88`

API classes: `NvsTimeline`
Common calls: `getInstance()`, `getFilterFx()`

Simple sequence:

```java
public static void setTimelineData(NvsTimeline timeline) {
if (timeline == null) {
applyTheme(timeline);
removeAllTimelineEffect(timeline);
addTimeLineEffect(timeline);
buildTimelineMusic(timeline);
MeicamVideoFx filterFx = TimelineData.getInstance().getFilterFx();
if (filterFx != null) {
buildTimelineFilter(timeline, filterFx);
setAdjustEffects(timeline);
buildClipFilter(timeline);
removeAllSticker(timeline);
removeAllCaption(timeline);
removeAllCompoundCaption(timeline);
setSitckerCaptionObject(timeline);
buildTimelineRecordAudio(timeline);
buildTimelineWaterMark(timeline);
buildTimelineMasicEffect(timeline);
```

## `effects-transforms-240` `setAdjustEffects`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:158`

API classes: `NvsConstants`, `NvsTimeline`
Static/constants: `NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST`, `NvsConstants.ADJUST_TINT`, `NvsConstants.ADJUST_AMOUNT`, `NvsConstants.FX_SHARPEN`, `NvsConstants.ADJUST_DEGREE`, `NvsConstants.FX_VIGNETTE`, `NvsConstants.ADJUST_BLACKPOINT`, `NvsConstants.ADJUST_TEMPERATURE`, `NvsConstants.ADJUST_SHADOW`, `NvsConstants.ADJUST_HIGHTLIGHT`, `NvsConstants.ADJUST_SATURATION`, `NvsConstants.ADJUST_CONTRAST`
Common calls: `getInstance()`, `getMeicamAdjustData()`, `getAmount()`, `getDegree()`, `getBlackPoint()`, `getTint()`, `getTemperature()`, `getShadow()`, `getHighlight()`, `getSaturation()`, `getContrast()`, `getBrightness()`

Simple sequence:

```java
public static void setAdjustEffects(NvsTimeline timeline) {
if (timeline == null) {
MeicamAdjustData meicamAdjustData = TimelineData.getInstance().getMeicamAdjustData();
setTimelineAdjustEffect(timeline, meicamAdjustData.getAmount(), NvsConstants.ADJUST_AMOUNT, NvsConstants.FX_SHARPEN);
setTimelineAdjustEffect(timeline, meicamAdjustData.getDegree(), NvsConstants.ADJUST_DEGREE, NvsConstants.FX_VIGNETTE);
setTimelineAdjustEffect(timeline, meicamAdjustData.getBlackPoint(), NvsConstants.ADJUST_BLACKPOINT, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
setTimelineAdjustEffect(timeline, meicamAdjustData.getTint(), NvsConstants.ADJUST_TINT, NvsConstants.ADJUST_TINT);
setTimelineAdjustEffect(timeline, meicamAdjustData.getTemperature(), NvsConstants.ADJUST_TEMPERATURE, NvsConstants.ADJUST_TINT);
setTimelineAdjustEffect(timeline, meicamAdjustData.getShadow(), NvsConstants.ADJUST_SHADOW, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
setTimelineAdjustEffect(timeline, meicamAdjustData.getHighlight(), NvsConstants.ADJUST_HIGHTLIGHT, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
setTimelineAdjustEffect(timeline, meicamAdjustData.getSaturation(), NvsConstants.ADJUST_SATURATION, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
setTimelineAdjustEffect(timeline, meicamAdjustData.getContrast(), NvsConstants.ADJUST_CONTRAST, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
setTimelineAdjustEffect(timeline, meicamAdjustData.getBrightness(), NvsConstants.ADJUST_BRIGHTNESS, NvsConstants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
```

## `effects-transforms-241` `buildTimelineWaterMark`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:295`

API classes: `NvsTimeline`, `NvsTimelineWatermarkPosition_TopLeft`
Static/constants: `NvsTimeline.NvsTimelineWatermarkPosition_TopLeft`
Common calls: `getWatermarkPath()`, `getInstance()`, `getMeicamWaterMark()`, `deleteWatermark()`, `isEmpty()`, `addWatermark()`, `getWatermarkW()`, `getWatermarkH()`, `getWatermarkX()`, `getWatermarkY()`

Simple sequence:

```java
private static void buildTimelineWaterMark(NvsTimeline timeline) {
MeicamWaterMark waterMark = TimelineData.getInstance().getMeicamWaterMark();
timeline.deleteWatermark();
if (TextUtils.isEmpty(waterMark.getWatermarkPath())) {
timeline.addWatermark(waterMark.getWatermarkPath(), waterMark.getWatermarkW(), waterMark.getWatermarkH(), 1
, NvsTimeline.NvsTimelineWatermarkPosition_TopLeft, waterMark.getWatermarkX(), waterMark.getWatermarkY());
```

## `effects-transforms-242` `fillTrack`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:611`

API classes: `NvsTimeline`, `NvsVideoTrack`
Common calls: `e()`, `bindToTimeline()`, `getClipInfoList()`, `isEmpty()`, `size()`, `get()`, `addToTimeline()`, `getTransitionInfoList()`

Simple sequence:

```java
public static boolean fillTrack(NvsTimeline timeline, List<MeicamVideoTrack> videoTrackList) {
for (MeicamVideoTrack meicamVideoTrack : videoTrackList) {
NvsVideoTrack track = meicamVideoTrack.bindToTimeline(timeline);
List<ClipInfo<?>> clipInfoList = meicamVideoTrack.getClipInfoList();
setTransition(timeline, meicamVideoTrack.getTransitionInfoList());
```

## `effects-transforms-243` `fillTrack`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:612`

API classes: `NvsVideoTrack`
Common calls: `e()`, `bindToTimeline()`, `getClipInfoList()`, `isEmpty()`, `size()`, `get()`, `addToTimeline()`, `getTransitionInfoList()`

Simple sequence:

```java
for (MeicamVideoTrack meicamVideoTrack : videoTrackList) {
NvsVideoTrack track = meicamVideoTrack.bindToTimeline(timeline);
List<ClipInfo<?>> clipInfoList = meicamVideoTrack.getClipInfoList();
setTransition(timeline, meicamVideoTrack.getTransitionInfoList());
```

## `effects-transforms-244` `setTransition`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:642`

API classes: `NvsTimeline`, `NvsVideoTrack`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `bindToTimeline()`

Simple sequence:

```java
public static boolean setTransition(NvsTimeline timeline, List<MeicamTransition> meicamTransitions) {
if (timeline == null) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
int videoClipCount = videoTrack.getClipCount();
```

## `effects-transforms-245` `clearAllBuildInTransition`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:682`

API classes: `NvsTimeline`, `NvsVideoTrack`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `setBuiltinTransition()`

Simple sequence:

```java
public static boolean clearAllBuildInTransition(NvsTimeline timeline) {
if (timeline == null) {
NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(BaseConstants.TRACK_INDEX_MAIN);
int videoClipCount = videoTrack.getClipCount();
for (int i = 0; i < videoClipCount - 1; i++) {
videoTrack.setBuiltinTransition(i, "");
```

## `effects-transforms-246` `buildTimelineFilter`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:774`

API classes: `NvsTimeline`
Common calls: `get()`, `getInstance()`, `getMeicamVideoTrackList()`, `getClipInfoList()`, `size()`, `clone()`

Simple sequence:

```java
public static boolean buildTimelineFilter(NvsTimeline timeline, MeicamVideoFx videoClipFxData) {
if (timeline == null) {
MeicamVideoTrack meicamVideoTrack = TimelineData.getInstance().getMeicamVideoTrackList().get(BaseConstants.TRACK_INDEX_MAIN);
List<ClipInfo<?>> clipInfos = meicamVideoTrack.getClipInfoList();
```

## `effects-transforms-247` `buildClipFilter`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:800`

API classes: `NvsTimeline`
Common calls: `getInstance()`, `getMeicamVideoTrackList()`, `isEmpty()`, `getClipInfoList()`, `getVideoFx()`

Simple sequence:

```java
public static boolean buildClipFilter(NvsTimeline timeline) {
if (timeline == null) {
List<MeicamVideoTrack> meicamVideoTrackList = TimelineData.getInstance().getMeicamVideoTrackList();
for (MeicamVideoTrack meicamVideoTrack : meicamVideoTrackList) {
List<ClipInfo<?>> clipInfoList = meicamVideoTrack.getClipInfoList();
for (ClipInfo clipInfo : clipInfoList) {
appendFilterFx((MeicamVideoClip) clipInfo, ((MeicamVideoClip) clipInfo).getVideoFx(MeicamVideoFx.SUB_TYPE_CLIP_FILTER));
```

## `effects-transforms-248` `appendFilterFx`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:826`

API classes: `NvsVideoFx`
Common calls: `removeVideoFx()`, `getSubType()`, `bindToTimeline()`, `getObject()`, `setFilterMask()`, `getVideoFxs()`, `add()`

Simple sequence:

```java
clip.removeVideoFx(videoClipFxData.getSubType());
NvsVideoFx videoFx = videoClipFxData.bindToTimeline(clip.getObject());
if (videoFx != null) {
videoFx.setFilterMask(true);
clip.getVideoFxs().add(videoClipFxData);
```
