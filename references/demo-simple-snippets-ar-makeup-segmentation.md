# Demo Simple Snippets - AR Makeup Segmentation

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: AR scene, human detection, beauty, makeup, face mesh, warp, segmentation, mask generator, master keyer, and virtual background style flows.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [ar-makeup-segmentation-001 getBuffingSkin](#ar-makeup-segmentation-001-getbuffingskin)
- [ar-makeup-segmentation-002 checkBuildCaptureBeautyFx](#ar-makeup-segmentation-002-checkbuildcapturebeautyfx)
- [ar-makeup-segmentation-003 checkBuildCaptureBeautyFx](#ar-makeup-segmentation-003-checkbuildcapturebeautyfx)
- [ar-makeup-segmentation-004 checkBuildCaptureBeautyFx](#ar-makeup-segmentation-004-checkbuildcapturebeautyfx)
- [ar-makeup-segmentation-005 getCaptureVideoFx](#ar-makeup-segmentation-005-getcapturevideofx)
- [ar-makeup-segmentation-006 getCaptureVideoFx](#ar-makeup-segmentation-006-getcapturevideofx)
- [ar-makeup-segmentation-007 getCaptureBeautyFx](#ar-makeup-segmentation-007-getcapturebeautyfx)
- [ar-makeup-segmentation-008 getBeautyFx](#ar-makeup-segmentation-008-getbeautyfx)
- [ar-makeup-segmentation-009 checkBuildClipArSceneFx](#ar-makeup-segmentation-009-checkbuildcliparscenefx)
- [ar-makeup-segmentation-010 checkBuildClipArSceneFx](#ar-makeup-segmentation-010-checkbuildcliparscenefx)
- [ar-makeup-segmentation-011 checkBuildClipArSceneFx](#ar-makeup-segmentation-011-checkbuildcliparscenefx)
- [ar-makeup-segmentation-012 getVideoFx](#ar-makeup-segmentation-012-getvideofx)
- [ar-makeup-segmentation-013 getVideoFx](#ar-makeup-segmentation-013-getvideofx)
- [ar-makeup-segmentation-014 deleteBeauty](#ar-makeup-segmentation-014-deletebeauty)
- [ar-makeup-segmentation-015 deleteBeauty](#ar-makeup-segmentation-015-deletebeauty)
- [ar-makeup-segmentation-016 checkBuildCaptureSharpenFx](#ar-makeup-segmentation-016-checkbuildcapturesharpenfx)
- [ar-makeup-segmentation-017 checkBuildClipSharpenFx](#ar-makeup-segmentation-017-checkbuildclipsharpenfx)
- [ar-makeup-segmentation-018 checkBuildCaptureDefinitionFx](#ar-makeup-segmentation-018-checkbuildcapturedefinitionfx)
- [ar-makeup-segmentation-019 checkBuildClipDefinitionFx](#ar-makeup-segmentation-019-checkbuildclipdefinitionfx)
- [ar-makeup-segmentation-020 getCapturePackageFx](#ar-makeup-segmentation-020-getcapturepackagefx)
- [ar-makeup-segmentation-021 getCapturePackageFx](#ar-makeup-segmentation-021-getcapturepackagefx)
- [ar-makeup-segmentation-022 removeCapturePackageFx](#ar-makeup-segmentation-022-removecapturepackagefx)
- [ar-makeup-segmentation-023 getVideoPackageFx](#ar-makeup-segmentation-023-getvideopackagefx)
- [ar-makeup-segmentation-024 getVideoPackageFx](#ar-makeup-segmentation-024-getvideopackagefx)
- [ar-makeup-segmentation-025 setVideoPackageFx](#ar-makeup-segmentation-025-setvideopackagefx)
- [ar-makeup-segmentation-026 enableBeauty](#ar-makeup-segmentation-026-enablebeauty)
- [ar-makeup-segmentation-027 enableBeauty](#ar-makeup-segmentation-027-enablebeauty)
- [ar-makeup-segmentation-028 enableAdvancedBeauty](#ar-makeup-segmentation-028-enableadvancedbeauty)
- [ar-makeup-segmentation-029 enableAdvancedBeauty](#ar-makeup-segmentation-029-enableadvancedbeauty)
- [ar-makeup-segmentation-030 enableShape](#ar-makeup-segmentation-030-enableshape)
- [ar-makeup-segmentation-031 enableShape](#ar-makeup-segmentation-031-enableshape)
- [ar-makeup-segmentation-032 applyBeautyFx](#ar-makeup-segmentation-032-applybeautyfx)
- [ar-makeup-segmentation-033 applyBeautyFx](#ar-makeup-segmentation-033-applybeautyfx)
- [ar-makeup-segmentation-034 applyBeautyFx](#ar-makeup-segmentation-034-applybeautyfx)
- [ar-makeup-segmentation-035 getFxDesc](#ar-makeup-segmentation-035-getfxdesc)
- [ar-makeup-segmentation-036 applySharpenFx](#ar-makeup-segmentation-036-applysharpenfx)
- [ar-makeup-segmentation-037 applyDefinitionFx](#ar-makeup-segmentation-037-applydefinitionfx)
- [ar-makeup-segmentation-038 getPackageType](#ar-makeup-segmentation-038-getpackagetype)
- [ar-makeup-segmentation-039 getPackageType](#ar-makeup-segmentation-039-getpackagetype)
- [ar-makeup-segmentation-040 getLocalMakeupList](#ar-makeup-segmentation-040-getlocalmakeuplist)
- [ar-makeup-segmentation-041 getPackageType](#ar-makeup-segmentation-041-getpackagetype)
- [ar-makeup-segmentation-042 getPackageType](#ar-makeup-segmentation-042-getpackagetype)
- [ar-makeup-segmentation-043 checkBuildCaptureArSceneFx](#ar-makeup-segmentation-043-checkbuildcapturearscenefx)
- [ar-makeup-segmentation-044 checkBuildCaptureArSceneFx](#ar-makeup-segmentation-044-checkbuildcapturearscenefx)
- [ar-makeup-segmentation-045 checkBuildCaptureArSceneFx](#ar-makeup-segmentation-045-checkbuildcapturearscenefx)
- [ar-makeup-segmentation-046 checkBuildClipArSceneFx](#ar-makeup-segmentation-046-checkbuildcliparscenefx)
- [ar-makeup-segmentation-047 checkBuildClipArSceneFx](#ar-makeup-segmentation-047-checkbuildcliparscenefx)
- [ar-makeup-segmentation-048 checkBuildClipArSceneFx](#ar-makeup-segmentation-048-checkbuildcliparscenefx)
- [ar-makeup-segmentation-049 getVideoFx](#ar-makeup-segmentation-049-getvideofx)
- [ar-makeup-segmentation-050 getVideoFx](#ar-makeup-segmentation-050-getvideofx)
- [ar-makeup-segmentation-051 getCaptureVideoFx](#ar-makeup-segmentation-051-getcapturevideofx)
- [ar-makeup-segmentation-052 getCaptureVideoFx](#ar-makeup-segmentation-052-getcapturevideofx)
- [ar-makeup-segmentation-053 enableMakeupFlag](#ar-makeup-segmentation-053-enablemakeupflag)
- [ar-makeup-segmentation-054 enableMakeupFlag](#ar-makeup-segmentation-054-enablemakeupflag)
- [ar-makeup-segmentation-055 setCaptureMakeupColor](#ar-makeup-segmentation-055-setcapturemakeupcolor)
- [ar-makeup-segmentation-056 setMakeupColor](#ar-makeup-segmentation-056-setmakeupcolor)
- [ar-makeup-segmentation-057 setMakeupColor](#ar-makeup-segmentation-057-setmakeupcolor)
- [ar-makeup-segmentation-058 setMakeupIntensity](#ar-makeup-segmentation-058-setmakeupintensity)
- [ar-makeup-segmentation-059 setMakeupIntensity](#ar-makeup-segmentation-059-setmakeupintensity)
- [ar-makeup-segmentation-060 setMakeupFilterIntensity](#ar-makeup-segmentation-060-setmakeupfilterintensity)
- [ar-makeup-segmentation-061 setMakeupFilterIntensity](#ar-makeup-segmentation-061-setmakeupfilterintensity)
- [ar-makeup-segmentation-062 setMakeupPackageId](#ar-makeup-segmentation-062-setmakeuppackageid)
- [ar-makeup-segmentation-063 setMakeupPackageId](#ar-makeup-segmentation-063-setmakeuppackageid)
- [ar-makeup-segmentation-064 applyMakeupFx](#ar-makeup-segmentation-064-applymakeupfx)
- [ar-makeup-segmentation-065 applyMakeupFx](#ar-makeup-segmentation-065-applymakeupfx)
- [ar-makeup-segmentation-066 applyMakeupFx](#ar-makeup-segmentation-066-applymakeupfx)
- [ar-makeup-segmentation-067 resetMakeupFx](#ar-makeup-segmentation-067-resetmakeupfx)
- [ar-makeup-segmentation-068 resetMakeupFilter](#ar-makeup-segmentation-068-resetmakeupfilter)
- [ar-makeup-segmentation-069 applyMakeupFx](#ar-makeup-segmentation-069-applymakeupfx)
- [ar-makeup-segmentation-070 applyMakeupFx](#ar-makeup-segmentation-070-applymakeupfx)
- [ar-makeup-segmentation-071 applyBeautyFx](#ar-makeup-segmentation-071-applybeautyfx)
- [ar-makeup-segmentation-072 applyParam](#ar-makeup-segmentation-072-applyparam)
- [ar-makeup-segmentation-073 applyFilter](#ar-makeup-segmentation-073-applyfilter)
- [ar-makeup-segmentation-074 applyFilter](#ar-makeup-segmentation-074-applyfilter)
- [ar-makeup-segmentation-075 applyFilter](#ar-makeup-segmentation-075-applyfilter)
- [ar-makeup-segmentation-076 applyFilter](#ar-makeup-segmentation-076-applyfilter)
- [ar-makeup-segmentation-077 getPackageType](#ar-makeup-segmentation-077-getpackagetype)
- [ar-makeup-segmentation-078 getPackageType](#ar-makeup-segmentation-078-getpackagetype)
- [ar-makeup-segmentation-079 packageBeauty](#ar-makeup-segmentation-079-packagebeauty)
- [ar-makeup-segmentation-080 initArSceneEffect](#ar-makeup-segmentation-080-initarsceneeffect)
- [ar-makeup-segmentation-081 onEndLoop](#ar-makeup-segmentation-081-onendloop)
- [ar-makeup-segmentation-082 initBeautyFx](#ar-makeup-segmentation-082-initbeautyfx)
- [ar-makeup-segmentation-083 resetCustomMakeup](#ar-makeup-segmentation-083-resetcustommakeup)
- [ar-makeup-segmentation-084 onCaptureRecordingStarted](#ar-makeup-segmentation-084-oncapturerecordingstarted)
- [ar-makeup-segmentation-085 onCapturedPictureArrived](#ar-makeup-segmentation-085-oncapturedpicturearrived)
- [ar-makeup-segmentation-086 onCapturedPictureArrived](#ar-makeup-segmentation-086-oncapturedpicturearrived)
- [ar-makeup-segmentation-087 initRootView](#ar-makeup-segmentation-087-initrootview)
- [ar-makeup-segmentation-088 initArguments](#ar-makeup-segmentation-088-initarguments)
- [ar-makeup-segmentation-089 removeAllSkinColour](#ar-makeup-segmentation-089-removeallskincolour)
- [ar-makeup-segmentation-090 applyBeauty](#ar-makeup-segmentation-090-applybeauty)
- [ar-makeup-segmentation-091 getBuffingSkinData](#ar-makeup-segmentation-091-getbuffingskindata)
- [ar-makeup-segmentation-092 getWhiteningSkinData](#ar-makeup-segmentation-092-getwhiteningskindata)
- [ar-makeup-segmentation-093 applyShape](#ar-makeup-segmentation-093-applyshape)
- [ar-makeup-segmentation-094 applyMicroShape](#ar-makeup-segmentation-094-applymicroshape)
- [ar-makeup-segmentation-095 applyMakeup](#ar-makeup-segmentation-095-applymakeup)
- [ar-makeup-segmentation-096 initBeautifyParam](#ar-makeup-segmentation-096-initbeautifyparam)
- [ar-makeup-segmentation-097 initBeautifyParam](#ar-makeup-segmentation-097-initbeautifyparam)
- [ar-makeup-segmentation-098 setMakeupEffect](#ar-makeup-segmentation-098-setmakeupeffect)
- [ar-makeup-segmentation-099 setMakeupEffect](#ar-makeup-segmentation-099-setmakeupeffect)
- [ar-makeup-segmentation-100 initListener](#ar-makeup-segmentation-100-initlistener)
- [ar-makeup-segmentation-101 initListener](#ar-makeup-segmentation-101-initlistener)
- [ar-makeup-segmentation-102 makeupIntensityChanged](#ar-makeup-segmentation-102-makeupintensitychanged)
- [ar-makeup-segmentation-103 makeupColorChanged](#ar-makeup-segmentation-103-makeupcolorchanged)
- [ar-makeup-segmentation-104 clearShape](#ar-makeup-segmentation-104-clearshape)
- [ar-makeup-segmentation-105 clearAllCustomMakeup](#ar-makeup-segmentation-105-clearallcustommakeup)
- [ar-makeup-segmentation-106 postSeekAction](#ar-makeup-segmentation-106-postseekaction)
- [ar-makeup-segmentation-107 setMakeupCategoryList](#ar-makeup-segmentation-107-setmakeupcategorylist)
- [ar-makeup-segmentation-108 onColorChanged](#ar-makeup-segmentation-108-oncolorchanged)
- [ar-makeup-segmentation-109 onSubViewSelect](#ar-makeup-segmentation-109-onsubviewselect)
- [ar-makeup-segmentation-110 onDonwloadAssetFailed](#ar-makeup-segmentation-110-ondonwloadassetfailed)
- [ar-makeup-segmentation-111 setSkinApply](#ar-makeup-segmentation-111-setskinapply)
- [ar-makeup-segmentation-112 setSharpenApply](#ar-makeup-segmentation-112-setsharpenapply)
- [ar-makeup-segmentation-113 isSupportMatte](#ar-makeup-segmentation-113-issupportmatte)
- [ar-makeup-segmentation-114 setFaceApply](#ar-makeup-segmentation-114-setfaceapply)
- [ar-makeup-segmentation-115 setSmallApply](#ar-makeup-segmentation-115-setsmallapply)
- [ar-makeup-segmentation-116 applyBeautyFx](#ar-makeup-segmentation-116-applybeautyfx)
- [ar-makeup-segmentation-117 setCancelDefaultFxValue](#ar-makeup-segmentation-117-setcanceldefaultfxvalue)
- [ar-makeup-segmentation-118 initRootView](#ar-makeup-segmentation-118-initrootview)
- [ar-makeup-segmentation-119 detectFace](#ar-makeup-segmentation-119-detectface)
- [ar-makeup-segmentation-120 buildTimelineMakeup](#ar-makeup-segmentation-120-buildtimelinemakeup)
- [ar-makeup-segmentation-121 applyMakeupFx](#ar-makeup-segmentation-121-applymakeupfx)
- [ar-makeup-segmentation-122 buildTimelineBeauty](#ar-makeup-segmentation-122-buildtimelinebeauty)
- [ar-makeup-segmentation-123 applyBeautyFx](#ar-makeup-segmentation-123-applybeautyfx)
- [ar-makeup-segmentation-124 getPackageType](#ar-makeup-segmentation-124-getpackagetype)
- [ar-makeup-segmentation-125 getPackageType](#ar-makeup-segmentation-125-getpackagetype)
- [ar-makeup-segmentation-126 onDestroy](#ar-makeup-segmentation-126-ondestroy)
- [ar-makeup-segmentation-127 setSelectedMakeupMap](#ar-makeup-segmentation-127-setselectedmakeupmap)
- [ar-makeup-segmentation-128 notifyFaceFeatureInfos](#ar-makeup-segmentation-128-notifyfacefeatureinfos)
- [ar-makeup-segmentation-129 notifyFaceFeatureInfos](#ar-makeup-segmentation-129-notifyfacefeatureinfos)
- [ar-makeup-segmentation-130 notifyTotalTimeCost](#ar-makeup-segmentation-130-notifytotaltimecost)
- [ar-makeup-segmentation-131 onTabReselected](#ar-makeup-segmentation-131-ontabreselected)
- [ar-makeup-segmentation-132 onDonwloadAssetFailed](#ar-makeup-segmentation-132-ondonwloadassetfailed)
- [ar-makeup-segmentation-133 onTabReselected](#ar-makeup-segmentation-133-ontabreselected)
- [ar-makeup-segmentation-134 onDonwloadAssetFailed](#ar-makeup-segmentation-134-ondonwloadassetfailed)
- [ar-makeup-segmentation-135 setAIFaceOcclusion](#ar-makeup-segmentation-135-setaifaceocclusion)
- [ar-makeup-segmentation-136 setAIFaceOcclusion](#ar-makeup-segmentation-136-setaifaceocclusion)
- [ar-makeup-segmentation-137 getPackageType](#ar-makeup-segmentation-137-getpackagetype)
- [ar-makeup-segmentation-138 getPackageType](#ar-makeup-segmentation-138-getpackagetype)
- [ar-makeup-segmentation-139 installAssetPackageSynchronous](#ar-makeup-segmentation-139-installassetpackagesynchronous)
- [ar-makeup-segmentation-140 showPropsToast](#ar-makeup-segmentation-140-showpropstoast)
- [ar-makeup-segmentation-141 applyBeautyFaceEffect](#ar-makeup-segmentation-141-applybeautyfaceeffect)
- [ar-makeup-segmentation-142 applyBeautyShapeFaceEffect](#ar-makeup-segmentation-142-applybeautyshapefaceeffect)
- [ar-makeup-segmentation-143 resetBeautyShape](#ar-makeup-segmentation-143-resetbeautyshape)
- [ar-makeup-segmentation-144 resetBeauty](#ar-makeup-segmentation-144-resetbeauty)
- [ar-makeup-segmentation-145 openBeautyFx](#ar-makeup-segmentation-145-openbeautyfx)
- [ar-makeup-segmentation-146 playNow](#ar-makeup-segmentation-146-playnow)
- [ar-makeup-segmentation-147 grabBitmapFromAuxiliaryTimelineAsync](#ar-makeup-segmentation-147-grabbitmapfromauxiliarytimelineasync)
- [ar-makeup-segmentation-148 grabBitmapFromAuxiliaryTimelineAsync](#ar-makeup-segmentation-148-grabbitmapfromauxiliarytimelineasync)
- [ar-makeup-segmentation-149 grabBitmapFromTimeline](#ar-makeup-segmentation-149-grabbitmapfromtimeline)
- [ar-makeup-segmentation-150 grabBitmapFromTimeline](#ar-makeup-segmentation-150-grabbitmapfromtimeline)
<!-- END GENERATED CONTENTS -->

## `ar-makeup-segmentation-001` `getBuffingSkin`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyDataManager.java:176`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`, `NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH`
Common calls: `addParam()`, `add()`, `create()`, `setType()`, `setName()`, `getResources()`, `getString()`, `setResourceId()`, `setFxName()`, `getInstance()`, `getDeviceCpuLevel()`

Simple sequence:

```java
.setType(FxParams.SKINNING)
.setName(context.getResources().getString(R.string.strength_1))
.setResourceId(R.drawable.beauty_strength_selector)
.setFxName(BEAUTY_STRENGTH));
.setType(FxParams.SKINNING)
.setName(context.getResources().getString(R.string.advanced_strength_1))
.setResourceId(R.drawable.beauty_strength_selector)
.setFxName(ADVANCED_BEAUTY_INTENSITY));
.setType(FxParams.SKINNING)
.setName(context.getResources().getString(R.string.advanced_strength_2))
.setResourceId(R.drawable.beauty_strength_selector)
.setFxName(ADVANCED_BEAUTY_INTENSITY));
.setType(FxParams.SKINNING)
.setName(context.getResources().getString(R.string.advanced_strength_3))
.setResourceId(R.drawable.beauty_strength_selector)
.setFxName(ADVANCED_BEAUTY_INTENSITY));
if (null != NvsStreamingContext.getInstance()) {
int level = NvsStreamingContext.getInstance().getDeviceCpuLevel();
if (level == NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH) {
.setType(FxParams.SKINNING)
.setName(context.getResources().getString(R.string.advanced_strength_4))
.setResourceId(R.drawable.beauty_strength_selector)
.setFxName(ADVANCED_BEAUTY_INTENSITY));
```

## `ar-makeup-segmentation-002` `checkBuildCaptureBeautyFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:70`

API classes: `NvsCaptureVideoFx`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.hasARModule`
Common calls: `setBooleanVal()`, `hasARModule()`, `appendBuiltinCaptureVideoFx()`, `isAndroidCameraPreferDualBufferAR()`, `setAIFaceOcclusion()`, `appendBeautyCaptureVideoFx()`

Simple sequence:

```java
public NvsCaptureVideoFx checkBuildCaptureBeautyFx() {
if (mBeautyFx == null) {
if (NvsStreamingContext.hasARModule() == 1) {
if (mBeautyFx == null) {
mBeautyFx = mStreamingContext.appendBuiltinCaptureVideoFx(AR_SCENE);
mBeautyFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
if (mStreamingContext.isAndroidCameraPreferDualBufferAR()) {
mBeautyFx.setBooleanVal(SINGLE_BUFFER_MODE, false);
mBeautyFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
Utils.setAIFaceOcclusion(mBeautyFx);
if (mBeautyFx == null) {
mBeautyFx = mStreamingContext.appendBeautyCaptureVideoFx();
```

## `ar-makeup-segmentation-003` `checkBuildCaptureBeautyFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:71`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.hasARModule`
Common calls: `setBooleanVal()`, `hasARModule()`, `appendBuiltinCaptureVideoFx()`, `isAndroidCameraPreferDualBufferAR()`, `setAIFaceOcclusion()`, `appendBeautyCaptureVideoFx()`

Simple sequence:

```java
if (mBeautyFx == null) {
if (NvsStreamingContext.hasARModule() == 1) {
if (mBeautyFx == null) {
mBeautyFx = mStreamingContext.appendBuiltinCaptureVideoFx(AR_SCENE);
mBeautyFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
if (mStreamingContext.isAndroidCameraPreferDualBufferAR()) {
mBeautyFx.setBooleanVal(SINGLE_BUFFER_MODE, false);
mBeautyFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
Utils.setAIFaceOcclusion(mBeautyFx);
if (mBeautyFx == null) {
mBeautyFx = mStreamingContext.appendBeautyCaptureVideoFx();
```

## `ar-makeup-segmentation-004` `checkBuildCaptureBeautyFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:72`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.hasARModule`
Common calls: `setBooleanVal()`, `hasARModule()`, `appendBuiltinCaptureVideoFx()`, `isAndroidCameraPreferDualBufferAR()`, `setAIFaceOcclusion()`, `appendBeautyCaptureVideoFx()`

Simple sequence:

```java
if (NvsStreamingContext.hasARModule() == 1) {
if (mBeautyFx == null) {
mBeautyFx = mStreamingContext.appendBuiltinCaptureVideoFx(AR_SCENE);
mBeautyFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
if (mStreamingContext.isAndroidCameraPreferDualBufferAR()) {
mBeautyFx.setBooleanVal(SINGLE_BUFFER_MODE, false);
mBeautyFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
Utils.setAIFaceOcclusion(mBeautyFx);
if (mBeautyFx == null) {
mBeautyFx = mStreamingContext.appendBeautyCaptureVideoFx();
```

## `ar-makeup-segmentation-005` `getCaptureVideoFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:105`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `equals()`, `getBuiltinCaptureVideoFxName()`

Simple sequence:

```java
private NvsCaptureVideoFx getCaptureVideoFx(String buildInName) {
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx videoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getBuiltinCaptureVideoFxName(), buildInName)) {
```

## `ar-makeup-segmentation-006` `getCaptureVideoFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:106`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `equals()`, `getBuiltinCaptureVideoFxName()`

Simple sequence:

```java
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx videoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getBuiltinCaptureVideoFxName(), buildInName)) {
```

## `ar-makeup-segmentation-007` `getCaptureBeautyFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:119`

API classes: `NvsFx`

Simple sequence:

```java
public NvsFx getCaptureBeautyFx() {
```

## `ar-makeup-segmentation-008` `getBeautyFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:127`

API classes: `NvsVideoFx`, `NvsVideoClip`

Simple sequence:

```java
public NvsVideoFx getBeautyFx(NvsVideoClip videoClip) {
NvsVideoFx videoFx = getVideoFx(videoClip, AR_SCENE);
```

## `ar-makeup-segmentation-009` `checkBuildClipArSceneFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:139`

API classes: `NvsVideoFx`, `NvsStreamingContext`, `NvsVideoClip`
Static/constants: `NvsStreamingContext.hasARModule`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`
Common calls: `setBooleanVal()`, `getARSceneManipulate()`, `hasARModule()`, `insertRawBuiltinFx()`, `setDetectionMode()`, `setAIFaceOcclusion()`, `e()`, `insertBeautyFx()`

Simple sequence:

```java
public NvsVideoFx checkBuildClipArSceneFx(NvsVideoClip videoClip) {
NvsVideoFx videoFx;
if (NvsStreamingContext.hasARModule() == 1) {
videoFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
videoFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
if (videoFx.getARSceneManipulate() != null) {
videoFx.getARSceneManipulate().setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
Utils.setAIFaceOcclusion(videoFx);
```

## `ar-makeup-segmentation-010` `checkBuildClipArSceneFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:141`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.hasARModule`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`
Common calls: `setBooleanVal()`, `getARSceneManipulate()`, `hasARModule()`, `insertRawBuiltinFx()`, `setDetectionMode()`, `setAIFaceOcclusion()`, `e()`, `insertBeautyFx()`

Simple sequence:

```java
if (NvsStreamingContext.hasARModule() == 1) {
videoFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
videoFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
if (videoFx.getARSceneManipulate() != null) {
videoFx.getARSceneManipulate().setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
Utils.setAIFaceOcclusion(videoFx);
```

## `ar-makeup-segmentation-011` `checkBuildClipArSceneFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:144`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`
Common calls: `setBooleanVal()`, `getARSceneManipulate()`, `insertRawBuiltinFx()`, `setDetectionMode()`, `setAIFaceOcclusion()`

Simple sequence:

```java
videoFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
videoFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
if (videoFx.getARSceneManipulate() != null) {
videoFx.getARSceneManipulate().setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
Utils.setAIFaceOcclusion(videoFx);
```

## `ar-makeup-segmentation-012` `getVideoFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:176`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `getRawFxCount()`, `getRawFxByIndex()`, `equals()`, `getBuiltinVideoFxName()`

Simple sequence:

```java
private NvsVideoFx getVideoFx(NvsVideoClip nvsVideoClip, String buildInName) {
for (int i = 0; i < nvsVideoClip.getRawFxCount(); i++) {
NvsVideoFx videoFx = nvsVideoClip.getRawFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getBuiltinVideoFxName(), buildInName)) {
```

## `ar-makeup-segmentation-013` `getVideoFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:177`

API classes: `NvsVideoFx`
Common calls: `getRawFxCount()`, `getRawFxByIndex()`, `equals()`, `getBuiltinVideoFxName()`

Simple sequence:

```java
for (int i = 0; i < nvsVideoClip.getRawFxCount(); i++) {
NvsVideoFx videoFx = nvsVideoClip.getRawFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getBuiltinVideoFxName(), buildInName)) {
```

## `ar-makeup-segmentation-014` `deleteBeauty`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:201`

API classes: `NvsVideoClip`, `NvsVideoFx`
Common calls: `removeFx()`, `getIndex()`

Simple sequence:

```java
public void deleteBeauty(NvsVideoClip videoClip) {
if (videoClip != null) {
NvsVideoFx videoFx = getVideoFx(videoClip, AR_SCENE);
if (videoFx != null) {
videoClip.removeFx(videoFx.getIndex());
```

## `ar-makeup-segmentation-015` `deleteBeauty`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:202`

API classes: `NvsVideoFx`
Common calls: `removeFx()`, `getIndex()`

Simple sequence:

```java
if (videoClip != null) {
NvsVideoFx videoFx = getVideoFx(videoClip, AR_SCENE);
if (videoFx != null) {
videoClip.removeFx(videoFx.getIndex());
```

## `ar-makeup-segmentation-016` `checkBuildCaptureSharpenFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:214`

API classes: `NvsCaptureVideoFx`
Common calls: `appendBuiltinCaptureVideoFx()`

Simple sequence:

```java
public NvsCaptureVideoFx checkBuildCaptureSharpenFx() {
if (mSharpenFx == null) {
mSharpenFx = mStreamingContext.appendBuiltinCaptureVideoFx(SHARPEN);
```

## `ar-makeup-segmentation-017` `checkBuildClipSharpenFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:228`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `appendBuiltinFx()`

Simple sequence:

```java
public NvsVideoFx checkBuildClipSharpenFx(NvsVideoClip videoClip) {
NvsVideoFx videoFx = getVideoFx(videoClip, SHARPEN);
```

## `ar-makeup-segmentation-018` `checkBuildCaptureDefinitionFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:251`

API classes: `NvsCaptureVideoFx`
Common calls: `appendBuiltinCaptureVideoFx()`, `setBooleanVal()`

Simple sequence:

```java
public NvsCaptureVideoFx checkBuildCaptureDefinitionFx() {
if (mDefinitionFx == null) {
mDefinitionFx = mStreamingContext.appendBuiltinCaptureVideoFx(DEFINITION);
if (null != mDefinitionFx) {
mDefinitionFx.setBooleanVal("Fast Mode", true);
```

## `ar-makeup-segmentation-019` `checkBuildClipDefinitionFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:268`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `appendBuiltinFx()`, `setBooleanVal()`

Simple sequence:

```java
public NvsVideoFx checkBuildClipDefinitionFx(NvsVideoClip videoClip) {
NvsVideoFx videoFx = getVideoFx(videoClip, DEFINITION);
if (null != videoFx) {
videoFx.setBooleanVal("Fast Mode", true);
```

## `ar-makeup-segmentation-020` `getCapturePackageFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:296`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `equals()`, `getCaptureVideoFxPackageId()`, `appendPackagedCaptureVideoFx()`

Simple sequence:

```java
public NvsCaptureVideoFx getCapturePackageFx(String packageId) {
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx videoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getCaptureVideoFxPackageId(), packageId)) {
return mStreamingContext.appendPackagedCaptureVideoFx(packageId);
```

## `ar-makeup-segmentation-021` `getCapturePackageFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:297`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `equals()`, `getCaptureVideoFxPackageId()`

Simple sequence:

```java
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx videoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getCaptureVideoFxPackageId(), packageId)) {
```

## `ar-makeup-segmentation-022` `removeCapturePackageFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:310`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `equals()`, `getCaptureVideoFxPackageId()`, `removeCaptureVideoFx()`

Simple sequence:

```java
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx videoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getCaptureVideoFxPackageId(), packageId)) {
mStreamingContext.removeCaptureVideoFx(i);
```

## `ar-makeup-segmentation-023` `getVideoPackageFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:325`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `getFxCount()`, `getFxByIndex()`, `equals()`, `getVideoFxPackageId()`

Simple sequence:

```java
private NvsVideoFx getVideoPackageFx(NvsVideoClip nvsVideoClip, String packedId) {
for (int i = 0; i < nvsVideoClip.getFxCount(); i++) {
NvsVideoFx videoFx = nvsVideoClip.getFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getVideoFxPackageId(), packedId)) {
```

## `ar-makeup-segmentation-024` `getVideoPackageFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:326`

API classes: `NvsVideoFx`
Common calls: `getFxCount()`, `getFxByIndex()`, `equals()`, `getVideoFxPackageId()`

Simple sequence:

```java
for (int i = 0; i < nvsVideoClip.getFxCount(); i++) {
NvsVideoFx videoFx = nvsVideoClip.getFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getVideoFxPackageId(), packedId)) {
```

## `ar-makeup-segmentation-025` `setVideoPackageFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:342`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `isEmpty()`, `appendPackagedFx()`

Simple sequence:

```java
private NvsVideoFx setVideoPackageFx(NvsVideoClip nvsVideoClip, String packedId) {
```

## `ar-makeup-segmentation-026` `enableBeauty`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:365`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void enableBeauty(NvsVideoClip videoClip, boolean enable) {
```

## `ar-makeup-segmentation-027` `enableBeauty`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:375`

API classes: `NvsFx`
Common calls: `setBooleanVal()`

Simple sequence:

```java
public void enableBeauty(NvsFx arSceneFx, boolean enable) {
if (arSceneFx != null) {
arSceneFx.setBooleanVal(ENABLE_BEAUTY, enable);
```

## `ar-makeup-segmentation-028` `enableAdvancedBeauty`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:396`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void enableAdvancedBeauty(NvsVideoClip videoClip, boolean enable) {
```

## `ar-makeup-segmentation-029` `enableAdvancedBeauty`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:406`

API classes: `NvsFx`
Common calls: `setBooleanVal()`

Simple sequence:

```java
public void enableAdvancedBeauty(NvsFx arSceneFx, boolean enable) {
if (arSceneFx != null) {
arSceneFx.setBooleanVal(ENABLE_ADVANCED_BEAUTY, enable);
```

## `ar-makeup-segmentation-030` `enableShape`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:427`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void enableShape(NvsVideoClip videoClip, boolean enable) {
```

## `ar-makeup-segmentation-031` `enableShape`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:437`

API classes: `NvsFx`
Common calls: `setBooleanVal()`

Simple sequence:

```java
public void enableShape(NvsFx arSceneFx, boolean enable) {
if (arSceneFx != null) {
arSceneFx.setBooleanVal(ENABLE_BEAUTY_SHAPE, enable);
```

## `ar-makeup-segmentation-032` `applyBeautyFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:491`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void applyBeautyFx(NvsVideoClip videoClip, IFxInfo fxInfo) {
```

## `ar-makeup-segmentation-033` `applyBeautyFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:503`

API classes: `NvsVideoClip`, `NvsFx`, `NvsAssetPackageManager`, `NvsVideoFx`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`
Common calls: `getPackageId()`, `getStrength()`, `get()`, `equals()`, `addBuildInParam()`, `getFxName()`, `isEmpty()`, `setFloatVal()`, `setIntVal()`, `d()`, `e()`, `setFilterIntensity()`

Simple sequence:

```java
public void applyBeautyFx(NvsVideoClip videoClip, NvsFx arSceneFx, IFxInfo fxInfo) {
String assetPackagePath = fxInfo.getAssetPackagePath();
int packageType = getPackageType(FileUtils.getFileExtension(assetPackagePath));
if (!TextUtils.isEmpty(assetPackagePath) && !TextUtils.equals(mLastInstallPackageId, fxInfo.getPackageId())) {
fxInfo.setPackageId(mLastInstallPackageId = installFxPackage(assetPackagePath, packageType));
List<FxParams> paramList = compoundFx.getParamList();
if (param.value instanceof Float) {
arSceneFx.setFloatVal(param.key, (Float) param.value);
arSceneFx.setFloatVal(param.key, (Double) param.value);
arSceneFx.setStringVal(param.key, (String) param.value);
arSceneFx.setBooleanVal(param.key, (Boolean) param.value);
arSceneFx.setIntVal(param.key, (Integer) param.value);
if (TextUtils.isEmpty(fxInfo.getFxName())) {
if (!TextUtils.isEmpty(fxInfo.getPackageId()) && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX) {
if (videoClip == null) {
if (mLastFx == null || !TextUtils.equals(mLastFx.getCaptureVideoFxPackageId(), fxInfo.getPackageId())) {
mLastFx = getCapturePackageFx(fxInfo.getPackageId());
if (mLastFx != null) {
Log.e("applyParam", "package id= " + fxInfo.getPackageId() + " value =" + fxInfo.getStrength());
mLastFx.setFilterIntensity((float) fxInfo.getStrength());
CustomBeautyHelper.get().addPackageParam(fxInfo.getPackageId(), new FxParams(FILTER_INTENSITY, fxInfo.getStrength()));
NvsVideoFx videoFx = getVideoPackageFx(videoClip, fxInfo.getPackageId());
if (null == videoFx) {
videoFx = setVideoPackageFx(videoClip, fxInfo.getPackageId());
// ... 9 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-034` `applyBeautyFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:504`

API classes: `NvsAssetPackageManager`, `NvsVideoFx`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`
Common calls: `getPackageId()`, `getStrength()`, `get()`, `equals()`, `addBuildInParam()`, `getFxName()`, `isEmpty()`, `setFloatVal()`, `setIntVal()`, `d()`, `e()`, `setFilterIntensity()`

Simple sequence:

```java
String assetPackagePath = fxInfo.getAssetPackagePath();
int packageType = getPackageType(FileUtils.getFileExtension(assetPackagePath));
if (!TextUtils.isEmpty(assetPackagePath) && !TextUtils.equals(mLastInstallPackageId, fxInfo.getPackageId())) {
fxInfo.setPackageId(mLastInstallPackageId = installFxPackage(assetPackagePath, packageType));
List<FxParams> paramList = compoundFx.getParamList();
if (param.value instanceof Float) {
arSceneFx.setFloatVal(param.key, (Float) param.value);
arSceneFx.setFloatVal(param.key, (Double) param.value);
arSceneFx.setStringVal(param.key, (String) param.value);
arSceneFx.setBooleanVal(param.key, (Boolean) param.value);
arSceneFx.setIntVal(param.key, (Integer) param.value);
if (TextUtils.isEmpty(fxInfo.getFxName())) {
if (!TextUtils.isEmpty(fxInfo.getPackageId()) && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX) {
if (videoClip == null) {
if (mLastFx == null || !TextUtils.equals(mLastFx.getCaptureVideoFxPackageId(), fxInfo.getPackageId())) {
mLastFx = getCapturePackageFx(fxInfo.getPackageId());
if (mLastFx != null) {
Log.e("applyParam", "package id= " + fxInfo.getPackageId() + " value =" + fxInfo.getStrength());
mLastFx.setFilterIntensity((float) fxInfo.getStrength());
CustomBeautyHelper.get().addPackageParam(fxInfo.getPackageId(), new FxParams(FILTER_INTENSITY, fxInfo.getStrength()));
NvsVideoFx videoFx = getVideoPackageFx(videoClip, fxInfo.getPackageId());
if (null == videoFx) {
videoFx = setVideoPackageFx(videoClip, fxInfo.getPackageId());
if (null != videoFx) {
// ... 8 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-035` `getFxDesc`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:580`

API classes: `NvsCaptureVideoFx`
Common calls: `getBuiltinCaptureVideoFxName()`

Simple sequence:

```java
if (videoFx instanceof NvsCaptureVideoFx) {
NvsCaptureVideoFx captureVideoFx = (NvsCaptureVideoFx) videoFx;
return captureVideoFx.getBuiltinCaptureVideoFxName();
```

## `ar-makeup-segmentation-036` `applySharpenFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:605`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void applySharpenFx(NvsVideoClip videoClip, IFxInfo fxInfo) {
```

## `ar-makeup-segmentation-037` `applyDefinitionFx`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:626`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void applyDefinitionFx(NvsVideoClip videoClip, IFxInfo fxInfo) {
```

## `ar-makeup-segmentation-038` `getPackageType`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:648`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`
Common calls: `isEmpty()`

Simple sequence:

```java
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
```

## `ar-makeup-segmentation-039` `getPackageType`

Source: `MArScene/src/main/java/com/meishe/arscene/BeautyHelper.java:652`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`

Simple sequence:

```java
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
```

## `ar-makeup-segmentation-040` `getLocalMakeupList`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java:158`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP`
Common calls: `add()`, `getAbsolutePath()`, `setType()`, `listFiles()`, `getName()`, `Param()`, `setKey()`, `getType()`, `setValue()`, `isEmpty()`, `exists()`, `isFile()`

Simple sequence:

```java
for (File fileItem : list) {
if (fileItem.isFile() && fileItem.getName().endsWith("makeup")) {
String packageId = installFxPackage(fileItem.getAbsolutePath(), "", NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP);
makeup.setAssetsDirectory(fileItem.getParent());
makeup.setUuid(packageId);
makeup.setEffectContent(makeupParamContent);
makeupParamContent.setMakeupParams(makeupParams);
File parentFile = fileItem.getParentFile();
makeupParam.setType(parentFile.getName());
param.setKey("Makeup " + makeupParam.getType() + " Package Id");
param.setValue(packageId);
param.setType("string");
paramValue.setKey("Makeup " + makeupParam.getType() + " Intensity");
paramValue.setValue(0.6f);
paramValue.setType("float");
makeupParam.setParams(paramList);
makeupParam.setPackageId(packageId);
if (fileItem.isDirectory()) {
Makeup makeup = getMakeup(context, fileItem.getAbsolutePath(), false);
for (File fxItem : files) {
int packageType = getPackageType(FileUtils.getFileExtension(fileItem));
if (packageType >= 0) {
installFxPackage(fxItem.getAbsolutePath(), "", packageType);
```

## `ar-makeup-segmentation-041` `getPackageType`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java:306`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP`
Common calls: `isEmpty()`

Simple sequence:

```java
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
```

## `ar-makeup-segmentation-042` `getPackageType`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupDataManager.java:310`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP`

Simple sequence:

```java
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
```

## `ar-makeup-segmentation-043` `checkBuildCaptureArSceneFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:98`

API classes: `NvsCaptureVideoFx`, `NvsStreamingContext`, `NvsMakeupEffectInfo`
Static/constants: `NvsStreamingContext.hasARModule`, `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL`
Common calls: `setBooleanVal()`, `hasARModule()`, `appendBuiltinCaptureVideoFx()`, `setAIFaceOcclusion()`

Simple sequence:

```java
public NvsCaptureVideoFx checkBuildCaptureArSceneFx() {
if (mStreamingContext != null && NvsStreamingContext.hasARModule() == 1) {
if (mArSceneFx == null) {
mArSceneFx = mStreamingContext.appendBuiltinCaptureVideoFx(AR_SCENE);
mArSceneFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
mArSceneFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
enableCaptureMakeupFlag(NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
Utils.setAIFaceOcclusion(mArSceneFx);
```

## `ar-makeup-segmentation-044` `checkBuildCaptureArSceneFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:99`

API classes: `NvsStreamingContext`, `NvsMakeupEffectInfo`
Static/constants: `NvsStreamingContext.hasARModule`, `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL`
Common calls: `setBooleanVal()`, `hasARModule()`, `appendBuiltinCaptureVideoFx()`, `setAIFaceOcclusion()`

Simple sequence:

```java
if (mStreamingContext != null && NvsStreamingContext.hasARModule() == 1) {
if (mArSceneFx == null) {
mArSceneFx = mStreamingContext.appendBuiltinCaptureVideoFx(AR_SCENE);
mArSceneFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
mArSceneFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
enableCaptureMakeupFlag(NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
Utils.setAIFaceOcclusion(mArSceneFx);
```

## `ar-makeup-segmentation-045` `checkBuildCaptureArSceneFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:101`

API classes: `NvsMakeupEffectInfo`
Static/constants: `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL`
Common calls: `setBooleanVal()`, `appendBuiltinCaptureVideoFx()`, `setAIFaceOcclusion()`

Simple sequence:

```java
if (mArSceneFx == null) {
mArSceneFx = mStreamingContext.appendBuiltinCaptureVideoFx(AR_SCENE);
mArSceneFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
mArSceneFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
enableCaptureMakeupFlag(NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
Utils.setAIFaceOcclusion(mArSceneFx);
```

## `ar-makeup-segmentation-046` `checkBuildClipArSceneFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:127`

API classes: `NvsVideoFx`, `NvsStreamingContext`, `NvsVideoClip`, `NvsMakeupEffectInfo`
Static/constants: `NvsStreamingContext.hasARModule`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`, `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL`
Common calls: `setBooleanVal()`, `getARSceneManipulate()`, `hasARModule()`, `insertRawBuiltinFx()`, `setDetectionMode()`, `setAIFaceOcclusion()`, `e()`

Simple sequence:

```java
public NvsVideoFx checkBuildClipArSceneFx(NvsVideoClip videoClip) {
if (NvsStreamingContext.hasARModule() == 1) {
NvsVideoFx videoFx = getVideoFx(videoClip, AR_SCENE);
videoFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
videoFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
if (videoFx.getARSceneManipulate() != null) {
videoFx.getARSceneManipulate().setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
enableMakeupFlag(videoFx, NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
Utils.setAIFaceOcclusion(videoFx);
```

## `ar-makeup-segmentation-047` `checkBuildClipArSceneFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:128`

API classes: `NvsStreamingContext`, `NvsVideoFx`, `NvsMakeupEffectInfo`
Static/constants: `NvsStreamingContext.hasARModule`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`, `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL`
Common calls: `setBooleanVal()`, `getARSceneManipulate()`, `hasARModule()`, `insertRawBuiltinFx()`, `setDetectionMode()`, `setAIFaceOcclusion()`

Simple sequence:

```java
if (NvsStreamingContext.hasARModule() == 1) {
NvsVideoFx videoFx = getVideoFx(videoClip, AR_SCENE);
videoFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
videoFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
if (videoFx.getARSceneManipulate() != null) {
videoFx.getARSceneManipulate().setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
enableMakeupFlag(videoFx, NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
Utils.setAIFaceOcclusion(videoFx);
```

## `ar-makeup-segmentation-048` `checkBuildClipArSceneFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:131`

API classes: `NvsStreamingContext`, `NvsMakeupEffectInfo`
Static/constants: `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`, `NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL`
Common calls: `setBooleanVal()`, `getARSceneManipulate()`, `insertRawBuiltinFx()`, `setDetectionMode()`, `setAIFaceOcclusion()`

Simple sequence:

```java
videoFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
videoFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
if (videoFx.getARSceneManipulate() != null) {
videoFx.getARSceneManipulate().setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
enableMakeupFlag(videoFx, NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
Utils.setAIFaceOcclusion(videoFx);
```

## `ar-makeup-segmentation-049` `getVideoFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:163`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `getRawFxCount()`, `getRawFxByIndex()`, `equals()`, `getBuiltinVideoFxName()`

Simple sequence:

```java
private NvsVideoFx getVideoFx(NvsVideoClip nvsVideoClip, String buildInName) {
for (int i = 0; i < nvsVideoClip.getRawFxCount(); i++) {
NvsVideoFx videoFx = nvsVideoClip.getRawFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getBuiltinVideoFxName(), buildInName)) {
```

## `ar-makeup-segmentation-050` `getVideoFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:164`

API classes: `NvsVideoFx`
Common calls: `getRawFxCount()`, `getRawFxByIndex()`, `equals()`, `getBuiltinVideoFxName()`

Simple sequence:

```java
for (int i = 0; i < nvsVideoClip.getRawFxCount(); i++) {
NvsVideoFx videoFx = nvsVideoClip.getRawFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getBuiltinVideoFxName(), buildInName)) {
```

## `ar-makeup-segmentation-051` `getCaptureVideoFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:179`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `equals()`, `getBuiltinCaptureVideoFxName()`

Simple sequence:

```java
private NvsCaptureVideoFx getCaptureVideoFx(String buildInName) {
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx videoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getBuiltinCaptureVideoFxName(), buildInName)) {
```

## `ar-makeup-segmentation-052` `getCaptureVideoFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:180`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `equals()`, `getBuiltinCaptureVideoFxName()`

Simple sequence:

```java
for (int i = 0; i < mStreamingContext.getCaptureVideoFxCount(); i++) {
NvsCaptureVideoFx videoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (videoFx != null && TextUtils.equals(videoFx.getBuiltinCaptureVideoFxName(), buildInName)) {
```

## `ar-makeup-segmentation-053` `enableMakeupFlag`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:206`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void enableMakeupFlag(NvsVideoClip videoClip, int flag) {
```

## `ar-makeup-segmentation-054` `enableMakeupFlag`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:217`

API classes: `NvsFx`
Common calls: `setIntVal()`

Simple sequence:

```java
public void enableMakeupFlag(NvsFx arSceneFx, int flag) {
if (arSceneFx != null) {
arSceneFx.setIntVal(MAKEUP_CUSTOM_ENABLE_FLAG, flag);
```

## `ar-makeup-segmentation-055` `setCaptureMakeupColor`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:230`

API classes: `NvsColor`

Simple sequence:

```java
public void setCaptureMakeupColor(String makeupTypeId, NvsColor nvsColor) {
```

## `ar-makeup-segmentation-056` `setMakeupColor`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:242`

API classes: `NvsVideoClip`, `NvsColor`

Simple sequence:

```java
public void setMakeupColor(NvsVideoClip videoClip, String makeupTypeId, NvsColor nvsColor) {
```

## `ar-makeup-segmentation-057` `setMakeupColor`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:254`

API classes: `NvsFx`, `NvsColor`
Common calls: `isEmpty()`, `setColorVal()`

Simple sequence:

```java
public void setMakeupColor(NvsFx arSceneFx, String makeupTypeId, NvsColor nvsColor) {
if (arSceneFx != null && !TextUtils.isEmpty(makeupTypeId)) {
arSceneFx.setColorVal(getMakeupColorKey(makeupTypeId), nvsColor);
```

## `ar-makeup-segmentation-058` `setMakeupIntensity`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:290`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void setMakeupIntensity(NvsVideoClip videoClip, String makeupTypeId, float intensity) {
```

## `ar-makeup-segmentation-059` `setMakeupIntensity`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:302`

API classes: `NvsFx`
Common calls: `isEmpty()`, `setFloatVal()`

Simple sequence:

```java
public void setMakeupIntensity(NvsFx arSceneFx, String makeupTypeId, float intensity) {
if (arSceneFx != null && !TextUtils.isEmpty(makeupTypeId)) {
arSceneFx.setFloatVal(getMakeupIntensityKey(makeupTypeId), intensity);
```

## `ar-makeup-segmentation-060` `setMakeupFilterIntensity`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:316`

API classes: `NvsVideoClip`, `NvsCaptureVideoFx`, `NvsVideoFx`
Common calls: `equals()`, `setFilterIntensity()`, `isEmpty()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getCaptureVideoFxPackageId()`, `getFxCount()`, `getFxByIndex()`, `getVideoFxPackageId()`

Simple sequence:

```java
public void setMakeupFilterIntensity(NvsVideoClip videoClip, String videoFxName, float intensity) {
if (null == videoClip) {
int count = mStreamingContext.getCaptureVideoFxCount();
for (int i = count - 1; i >= 0; i--) {
NvsCaptureVideoFx captureVideoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (TextUtils.equals(captureVideoFx.getCaptureVideoFxPackageId(), videoFxName)) {
captureVideoFx.setFilterIntensity(intensity);
int count = videoClip.getFxCount();
for (int i = count - 1; i >= 0; i--) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
if (TextUtils.equals(videoFx.getVideoFxPackageId(), videoFxName)) {
videoFx.setFilterIntensity(intensity);
```

## `ar-makeup-segmentation-061` `setMakeupFilterIntensity`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:320`

API classes: `NvsCaptureVideoFx`
Common calls: `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `equals()`, `getCaptureVideoFxPackageId()`, `setFilterIntensity()`

Simple sequence:

```java
if (null == videoClip) {
int count = mStreamingContext.getCaptureVideoFxCount();
for (int i = count - 1; i >= 0; i--) {
NvsCaptureVideoFx captureVideoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
if (TextUtils.equals(captureVideoFx.getCaptureVideoFxPackageId(), videoFxName)) {
captureVideoFx.setFilterIntensity(intensity);
```

## `ar-makeup-segmentation-062` `setMakeupPackageId`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:358`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void setMakeupPackageId(NvsVideoClip videoClip, String makeupTypeId, String packageId) {
```

## `ar-makeup-segmentation-063` `setMakeupPackageId`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:370`

API classes: `NvsFx`
Common calls: `isEmpty()`, `setStringVal()`

Simple sequence:

```java
public void setMakeupPackageId(NvsFx arSceneFx, String makeupTypeId, String packageId) {
if (arSceneFx != null && !TextUtils.isEmpty(makeupTypeId)) {
arSceneFx.setStringVal(getMakeupPackageKey(makeupTypeId), packageId);
```

## `ar-makeup-segmentation-064` `applyMakeupFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:393`

API classes: `NvsVideoClip`

Simple sequence:

```java
public Makeup applyMakeupFx(File makeupFileDir, NvsVideoClip videoClip) {
```

## `ar-makeup-segmentation-065` `applyMakeupFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:405`

API classes: `NvsVideoClip`, `NvsFx`
Common calls: `getAbsolutePath()`, `getName()`, `equals()`, `isEmpty()`, `endsWith()`, `exists()`, `listFiles()`, `isDirectory()`, `getFileNameNoExtension()`, `split()`, `getFileExtension()`, `readSdCardJsonFile()`

Simple sequence:

```java
private Makeup applyMakeupFx(File makeupFileDir, NvsVideoClip videoClip, NvsFx arSceneFx) {
for (File itemFile : fileList) {
if (isInvalidFolder(itemFile.getName())) {
for (File itemFile : fileList) {
if (isInvalidFolder(itemFile.getName())) {
String name = itemFile.getName();
jsonPath = itemFile.getAbsolutePath();
if (TextUtils.equals(MakeupDataManager.INFO_NEW_JSON, name)) {
jsonPath = itemFile.getAbsolutePath();
String fileName = FileUtils.getFileNameNoExtension(itemFile);
String licPath = makeupFileDir.getAbsolutePath() + File.separator + split[0] + ".lic";
String packagePath = itemFile.getAbsolutePath();
int packageType = getPackageType(FileUtils.getFileExtension(itemFile));
if (jsonPath.endsWith(MakeupDataManager.INFO_JSON)) {
makeupInfo = DataConvertUtils.convertMakeup(infoJsonStr, makeupFileDir.getAbsolutePath());
if (null != makeupInfo) {
makeupInfo.setAssetsDirectory(makeupFileDir.getAbsolutePath());
```

## `ar-makeup-segmentation-066` `applyMakeupFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:491`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void applyMakeupFx(Makeup makeup, NvsVideoClip videoClip) {
```

## `ar-makeup-segmentation-067` `resetMakeupFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:512`

API classes: `NvsVideoClip`

Simple sequence:

```java
public void resetMakeupFx(Makeup makeup, NvsVideoClip videoClip) {
```

## `ar-makeup-segmentation-068` `resetMakeupFilter`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:523`

API classes: `NvsVideoClip`
Common calls: `getEffectContent()`, `getFilterParams()`, `isEmpty()`

Simple sequence:

```java
public void resetMakeupFilter(Makeup makeup, NvsVideoClip videoClip) {
if (makeup != null) {
MakeupParamContent effectContent = makeup.getEffectContent();
if (effectContent != null) {
List<FilterParam> filterParams = effectContent.getFilterParams();
```

## `ar-makeup-segmentation-069` `applyMakeupFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:544`

API classes: `NvsVideoClip`, `NvsFx`

Simple sequence:

```java
private void applyMakeupFx(Makeup makeup, NvsVideoClip videoClip, NvsFx arSceneFx) {
```

## `ar-makeup-segmentation-070` `applyMakeupFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:557`

API classes: `NvsVideoClip`, `NvsFx`
Common calls: `getBeautyParams()`, `getAssetsDirectory()`, `getFilterParams()`, `size()`, `d()`, `getUuid()`, `getName()`, `getEffectContent()`, `getShapeParams()`, `getMicroShapeParams()`, `addAll()`, `equals()`

Simple sequence:

```java
private void applyMakeupFx(Makeup makeup, NvsVideoClip videoClip, NvsFx arSceneFx, boolean reset) {
LogUtils.d("makeupId=" + makeup.getUuid() + ",name=" + makeup.getName());
MakeupParamContent effectContent = makeup.getEffectContent();
applyBeautyFx(arSceneFx, effectContent.getBeautyParams(), reset, makeup.getAssetsDirectory());
applyBeautyFx(arSceneFx, effectContent.getShapeParams(), reset, makeup.getAssetsDirectory());
applyBeautyFx(arSceneFx, effectContent.getMicroShapeParams(), reset, makeup.getAssetsDirectory());
if (null != effectContent.getFilterParams() && effectContent.getFilterParams().size() > 0) {
filterParams.addAll(effectContent.getFilterParams());
if (null != effectContent.getBeautyParams() && effectContent.getBeautyParams().size() > 0) {
for (BeautyParam beautyParam : effectContent.getBeautyParams()) {
if (null != beautyParam && TextUtils.equals("ColorCorrect", beautyParam.getType())) {
List<MakeupParam> makeupParamList = effectContent.getMakeupParams();
applyMakeupContentFx(makeupParamList, arSceneFx, reset, makeup.getAssetsDirectory());
```

## `ar-makeup-segmentation-071` `applyBeautyFx`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:624`

API classes: `NvsFx`
Common calls: `getType()`, `getParams()`, `d()`, `isEmpty()`, `equals()`

Simple sequence:

```java
private void applyBeautyFx(NvsFx arSceneFx, List<? extends BaseParam> paramList, boolean reset, String assetsDirectory) {
if (baseParam instanceof BeautyParam) {
if (TextUtils.isEmpty(baseParam.getType())) {
applyParam(arSceneFx, baseParam.getParams(), assetsDirectory, reset);
} else if (TextUtils.equals(baseParam.getType(), "ColorCorrect")) {
applyParam(arSceneFx, baseParam.getParams(), assetsDirectory, reset);
```

## `ar-makeup-segmentation-072` `applyParam`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:645`

API classes: `NvsFx`
Common calls: `getKey()`, `getValue()`, `equals()`, `e()`, `setStringVal()`, `setFloatVal()`, `getType()`, `isEmpty()`, `parseFloat()`, `toString()`, `round()`, `parseDouble()`

Simple sequence:

```java
private void applyParam(NvsFx arSceneFx, List<BaseParam.Param> params, String assetsDirectory, boolean reset) {
String paramsType = param.getType();
if (TextUtils.equals(paramsType, "path") && param.getValue() instanceof String) {
Log.e("applyParam ", "key = " + param.getKey() + " value =" + assetsDirectory + File.separator + param.getValue());
arSceneFx.setStringVal(param.getKey(), reset ? "" : ((TextUtils.isEmpty(assetsDirectory) ? "" : assetsDirectory) + File.separator + param.getValue()));
float value = Float.parseFloat(param.getValue().toString());
Log.e("applyParam ", "key = " + param.getKey() + " value =" + value);
arSceneFx.setFloatVal(param.getKey(), reset ? 0 : value);
Log.e("applyParam ", "key = " + param.getKey() + " value =" + (double) param.getValue());
arSceneFx.setFloatVal(param.getKey(), reset ? 0 : (double) param.getValue());
int value = (int) Math.round(Double.parseDouble(String.valueOf(param.getValue())));
Log.e("applyParam ", "key = " + param.getKey() + " value =" + value);
arSceneFx.setIntVal(param.getKey(), reset ? 0 : value);
Log.e("applyParam ", "key = " + param.getKey() + " value =" + param.getValue());
arSceneFx.setBooleanVal(param.getKey(), (boolean) param.getValue());
Log.e("applyParam ", "key = " + param.getKey() + " value =" + (String) param.getValue());
arSceneFx.setStringVal(param.getKey(), reset ? "" : (String) param.getValue());
```

## `ar-makeup-segmentation-073` `applyFilter`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:686`

API classes: `NvsVideoClip`, `NvsCaptureVideoFx`, `NvsVideoFx`, `NvsFx`
Common calls: `equals()`, `getPackageId()`, `isEmpty()`, `getValue()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getCaptureVideoFxPackageId()`, `getBuiltinCaptureVideoFxName()`, `removeCaptureVideoFx()`, `d()`, `getFxCount()`, `getFxByIndex()`

Simple sequence:

```java
private void applyFilter(NvsVideoClip videoClip, List<BaseParam> filterParamList, boolean reset) {
int count = mStreamingContext.getCaptureVideoFxCount();
for (int i = count - 1; i >= 0; i--) {
NvsCaptureVideoFx captureVideoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
for (String videoFxName : mWhiteListFx) {
if (TextUtils.equals(captureVideoFx.getCaptureVideoFxPackageId(), videoFxName)
|| TextUtils.equals(captureVideoFx.getBuiltinCaptureVideoFxName(), videoFxName)) {
if (delete) {
mStreamingContext.removeCaptureVideoFx(i);
for (BaseParam filterParam : filterParamList) {
int fxCount = videoClip.getFxCount();
for (int i = fxCount - 1; i >= 0; i--) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
if (TextUtils.equals(filterParam.getPackageId(), videoFx.getBuiltinVideoFxName()) ||
TextUtils.equals(filterParam.getPackageId(), videoFx.getVideoFxPackageId())) {
videoClip.removeFx(i);
for (BaseParam filterParam : filterParamList) {
String packageId = filterParam.getPackageId();
NvsFx nvsFx;
if (videoClip == null) {
nvsFx = mStreamingContext.appendBuiltinCaptureVideoFx(packageId);
if (videoClip == null) {
nvsFx = mStreamingContext.appendPackagedCaptureVideoFx(packageId);
if (filterParam instanceof FilterParam) {
// ... 3 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-074` `applyFilter`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:687`

API classes: `NvsCaptureVideoFx`, `NvsVideoFx`, `NvsFx`
Common calls: `equals()`, `getPackageId()`, `isEmpty()`, `getValue()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getCaptureVideoFxPackageId()`, `getBuiltinCaptureVideoFxName()`, `removeCaptureVideoFx()`, `d()`, `getFxCount()`, `getFxByIndex()`

Simple sequence:

```java
int count = mStreamingContext.getCaptureVideoFxCount();
for (int i = count - 1; i >= 0; i--) {
NvsCaptureVideoFx captureVideoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
for (String videoFxName : mWhiteListFx) {
if (TextUtils.equals(captureVideoFx.getCaptureVideoFxPackageId(), videoFxName)
|| TextUtils.equals(captureVideoFx.getBuiltinCaptureVideoFxName(), videoFxName)) {
if (delete) {
mStreamingContext.removeCaptureVideoFx(i);
for (BaseParam filterParam : filterParamList) {
int fxCount = videoClip.getFxCount();
for (int i = fxCount - 1; i >= 0; i--) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
if (TextUtils.equals(filterParam.getPackageId(), videoFx.getBuiltinVideoFxName()) ||
TextUtils.equals(filterParam.getPackageId(), videoFx.getVideoFxPackageId())) {
videoClip.removeFx(i);
for (BaseParam filterParam : filterParamList) {
String packageId = filterParam.getPackageId();
NvsFx nvsFx;
if (videoClip == null) {
nvsFx = mStreamingContext.appendBuiltinCaptureVideoFx(packageId);
if (videoClip == null) {
nvsFx = mStreamingContext.appendPackagedCaptureVideoFx(packageId);
if (filterParam instanceof FilterParam) {
value = ((FilterParam) filterParam).getValue();
// ... 2 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-075` `applyFilter`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:688`

API classes: `NvsCaptureVideoFx`
Common calls: `isEmpty()`, `equals()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getCaptureVideoFxPackageId()`, `getBuiltinCaptureVideoFxName()`, `removeCaptureVideoFx()`, `d()`

Simple sequence:

```java
int count = mStreamingContext.getCaptureVideoFxCount();
for (int i = count - 1; i >= 0; i--) {
NvsCaptureVideoFx captureVideoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
for (String videoFxName : mWhiteListFx) {
if (TextUtils.equals(captureVideoFx.getCaptureVideoFxPackageId(), videoFxName)
|| TextUtils.equals(captureVideoFx.getBuiltinCaptureVideoFxName(), videoFxName)) {
if (delete) {
mStreamingContext.removeCaptureVideoFx(i);
```

## `ar-makeup-segmentation-076` `applyFilter`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:689`

API classes: `NvsCaptureVideoFx`
Common calls: `equals()`, `getCaptureVideoFxCount()`, `getCaptureVideoFxByIndex()`, `getCaptureVideoFxPackageId()`, `getBuiltinCaptureVideoFxName()`, `removeCaptureVideoFx()`, `d()`

Simple sequence:

```java
int count = mStreamingContext.getCaptureVideoFxCount();
for (int i = count - 1; i >= 0; i--) {
NvsCaptureVideoFx captureVideoFx = mStreamingContext.getCaptureVideoFxByIndex(i);
for (String videoFxName : mWhiteListFx) {
if (TextUtils.equals(captureVideoFx.getCaptureVideoFxPackageId(), videoFxName)
|| TextUtils.equals(captureVideoFx.getBuiltinCaptureVideoFxName(), videoFxName)) {
if (delete) {
mStreamingContext.removeCaptureVideoFx(i);
```

## `ar-makeup-segmentation-077` `getPackageType`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:821`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP`
Common calls: `isEmpty()`

Simple sequence:

```java
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
```

## `ar-makeup-segmentation-078` `getPackageType`

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:825`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP`

Simple sequence:

```java
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
```

## `ar-makeup-segmentation-079` `packageBeauty`

Source: `MMakeup/src/main/java/com/meishe/makeup/utils/DataConvertUtils.java:125`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`
Common calls: `add()`, `getValue()`, `isEmpty()`, `equals()`, `setParams()`, `getBeautyParams()`, `setCanReplace()`, `canReplace()`, `advancedBeautyEnable()`, `getAdvancedBeautyType()`, `whiteningLutEnabled()`, `exists()`

Simple sequence:

```java
List<BeautyOldParam> beautyOldParams = oldParamContent.getBeautyParams();
beautyParam.setCanReplace(oldParam.canReplace() ? 1 : 0);
if (advancedBeautyEnable) {
enableAdvancedBeauty(beautyParam, oldParam.getAdvancedBeautyType(), oldParam.getValue());
if (!file.exists()) {
copyAssetFile(BaseApp.getContext(), WHITEB_NAME, "capture", directory);
enableWhiteningLut(beautyParam, oldParam.getValue());
String paramKey = oldParam.getParamKey();
if (TextUtils.equals(paramKey, "Beauty Reddening")) {
beautyParam.setParams(packageCommonParams(paramKey, oldParam.getValue()));
if (TextUtils.equals(paramKey, "Default Beauty Enabled")) {
PackageManagerUtil.installAssetPackage(ADJUST_COLOR_PATH, ADJUST_COLOR_LIC_PATH, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
beautyParam.setParams(enables);
paramContent.setBeautyParams(beautyParams);
```

## `ar-makeup-segmentation-080` `initArSceneEffect`

Source: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:95`

API classes: `NvsStreamingContext`, `NvsEffectSdkContext`
Static/constants: `NvsStreamingContext.initHumanDetectionExt`, `NvsEffectSdkContext.initHumanDetectionExt`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE`, `NvsStreamingContext.setupHumanDetectionData`, `NvsEffectSdkContext.setupHumanDetectionData`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION`, `NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE`, `NvsStreamingContext.getInstance`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK`, `NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION`
Common calls: `append()`, `getContext()`, `initHumanDetectionExt()`, `setupHumanDetectionData()`, `initHumanDetection()`, `getInstance()`, `e()`, `getDeviceCpuLevel()`, `toString()`

Simple sequence:

```java
boolean initSuccess = NvsStreamingContext.initHumanDetection(MSApplication.getContext(),
NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK |
NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION |
NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
NvsEffectSdkContext.initHumanDetection(MSApplication.getContext(),
NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK |
NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION |
NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
boolean faceCommonSuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON, faceCommonPath);
NvsEffectSdkContext.setupHumanDetectionData(NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON, faceCommonPath);
boolean advancedBeautySuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY, advancedBeautyPath);
NvsEffectSdkContext.setupHumanDetectionData(NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY, advancedBeautyPath);
boolean fakefaceSuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE, fakeFacePath);
NvsEffectSdkContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE, fakeFacePath);
if (null != NvsStreamingContext.getInstance()) {
int level = NvsStreamingContext.getInstance().getDeviceCpuLevel();
if (level == NvsStreamingContext.DEVICE_POWER_LEVEL_LOW) {
boolean segSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),
segPath, null, NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND);
NvsEffectSdkContext.initHumanDetectionExt(MSApplication.getContext(),
segPath, null, NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND);
boolean handSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(), handPath, null,
NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK
| NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION);
// ... 13 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-081` `onEndLoop`

Source: `app/src/main/java/com/meishe/sdkdemo/activity/MainActivity.java:617`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.hasARModule`, `NvsStreamingContext.closeHumanDetection`
Common calls: `instance()`, `clear()`, `onDestroy()`, `clearRecordAudioData()`, `getInstance()`, `destory()`, `hasARModule()`, `closeHumanDetection()`

Simple sequence:

```java
MeicamContextWrap.getInstance().destory();
if (NvsStreamingContext.hasARModule() == HUMAN_AI_TYPE_MS) {
NvsStreamingContext.closeHumanDetection();
```

## `ar-makeup-segmentation-082` `initBeautyFx`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1774`

API classes: `NvsARSceneManipulate`
Static/constants: `NvsARSceneManipulate.CheckedFunctionType_Matte`
Common calls: `getDimensionPixelSize()`, `isSingleBufferMode()`, `checkBuildCaptureBeautyFx()`, `getARSceneManipulate()`, `isFunctionAvailable()`, `checkBuildCaptureArSceneFx()`, `enableCaptureBeauty()`, `enableCaptureAdvancedBeauty()`, `enableCaptureShape()`, `enableCaptureShapeNew()`, `setFloatVal()`, `LayoutParams()`

Simple sequence:

```java
mBeautyHelper = new BeautyHelper(mStreamingContext, BuildConfig.FACE_MODEL == 240, parameterValues.isSingleBufferMode());
if (mArSceneFaceEffect != null) {
NvsARSceneManipulate arSceneManipulate = mArSceneFaceEffect.getARSceneManipulate();
if (arSceneManipulate != null) {
mIsSupportMatte = arSceneManipulate.isFunctionAvailable(NvsARSceneManipulate.CheckedFunctionType_Matte);
mMakeupHelper = new MakeupHelper(mStreamingContext, BuildConfig.FACE_MODEL == 240, parameterValues.isSingleBufferMode());
if (null != mArSceneFaceEffect) {
mArSceneFaceEffect.setFloatVal(FxParams.ADVANCED_BEAUTY_INTENSITY, 0);
layoutParams.topMargin = getResources().getDimensionPixelSize(com.meishe.base.R.dimen.dp_px_150);
layoutParams.leftMargin = getResources().getDimensionPixelSize(R.dimen.dp_px_30);
layoutParams.rightMargin = getResources().getDimensionPixelSize(R.dimen.dp_px_30);
faceAvatarView.setLayoutParams(layoutParams);
faceAvatarView.setArSceneEffect(mArSceneFaceEffect);
```

## `ar-makeup-segmentation-083` `resetCustomMakeup`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2709`

API classes: `NvsColor`
Common calls: `setCaptureMakeupIntensity()`, `setCaptureMakeupColor()`, `setCaptureMakeupPackageId()`

Simple sequence:

```java
mMakeupHelper.setCaptureMakeupIntensity(makeupType, MakeUpSingleView.DEFAULT_MAKEUP_INTENSITY);
mMakeupHelper.setCaptureMakeupColor(makeupType, new NvsColor(0, 0, 0, 0));
mMakeupHelper.setCaptureMakeupPackageId(makeupType, "");
```

## `ar-makeup-segmentation-084` `onCaptureRecordingStarted`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3248`

API classes: `NvsVideoResolution`, `NvsRational`, `NvsEffect`, `NvsVideoFrameInfo`, `NvsVideoEffect`, `NvsEffectRenderCore`, `NvsCaptureVideoFx`, `NvsARSceneManipulate`, `NvsStreamingContext`, `NvsCaptureCompoundCaption`, `NvsVideoEffectCompoundCaption`, `NvsColor`
Static/constants: `NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE`, `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K`, `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED`, `NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA`
Common calls: `getFloatVal()`, `setFloatVal()`, `setBooleanVal()`, `isEmpty()`, `size()`, `getFxName()`, `add()`, `clear()`, `copyPixelsFromBuffer()`, `createVideoEffect()`, `observeOn()`, `getVideoEditResolution()`

Simple sequence:

```java
public void onCapturedPictureArrived(final ByteBuffer byteBuffer, NvsVideoFrameInfo nvsVideoFrameInfo) {
NvsVideoResolution mCurrentVideoResolution = new NvsVideoResolution();
mCurrentVideoResolution.imagePAR = new NvsRational(1, 1);
NvsVideoResolution videoEditResolution = Util.getVideoEditResolution(makeRatio);
int captureVideoFxCount = mStreamingContext.getCaptureVideoFxCount();
List<NvsEffect> effects = new ArrayList<>();
NvsRational nvsRational = new NvsRational(9, 16);
for (int i = 0; i < captureVideoFxCount; i++) {
NvsCaptureVideoFx captureVideoFxByIndex = mStreamingContext.getCaptureVideoFxByIndex(i);
if (captureVideoFxByIndex.getBuiltinCaptureVideoFxName().equals(Constants.AR_SCENE)) {
String stringVal = captureVideoFxByIndex.getStringVal(Constants.AR_SCENE_ID_KEY);
NvsVideoEffect videoEffect = mNvsEffectSdkContext.createVideoEffect(Constants.AR_SCENE, nvsRational);
if (BuildConfig.FACE_MODEL == 240) {
videoEffect.setBooleanVal("Use Face Extra Info", true);
NvsARSceneManipulate arSceneManipulate = videoEffect.getARSceneManipulate();
videoEffect.setBooleanVal(Constants.MAX_FACES_RESPECT_MIN, true);
videoEffect.setBooleanVal("Beauty Effect", true);
videoEffect.setBooleanVal("Beauty Shape", true);
videoEffect.setBooleanVal("Face Mesh Internal Enabled", true);
videoEffect.setBooleanVal("Advanced Beauty Enable", true);
if (arSceneManipulate != null) {
arSceneManipulate.setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE);
arSceneManipulate.setDetectionAutoProbe(true);
if (!TextUtils.isEmpty(stringVal)) {
// ... 65 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-085` `onCapturedPictureArrived`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3249`

API classes: `NvsVideoResolution`, `NvsRational`, `NvsEffect`, `NvsVideoEffect`, `NvsEffectRenderCore`, `NvsCaptureVideoFx`, `NvsARSceneManipulate`, `NvsStreamingContext`, `NvsCaptureCompoundCaption`, `NvsVideoEffectCompoundCaption`, `NvsColor`, `NvsCaptureAnimatedSticker`
Static/constants: `NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE`, `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K`, `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED`, `NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA`
Common calls: `getFloatVal()`, `setFloatVal()`, `setBooleanVal()`, `isEmpty()`, `size()`, `getFxName()`, `add()`, `clear()`, `copyPixelsFromBuffer()`, `createVideoEffect()`, `observeOn()`, `getVideoEditResolution()`

Simple sequence:

```java
NvsVideoResolution mCurrentVideoResolution = new NvsVideoResolution();
mCurrentVideoResolution.imagePAR = new NvsRational(1, 1);
NvsVideoResolution videoEditResolution = Util.getVideoEditResolution(makeRatio);
int captureVideoFxCount = mStreamingContext.getCaptureVideoFxCount();
List<NvsEffect> effects = new ArrayList<>();
NvsRational nvsRational = new NvsRational(9, 16);
for (int i = 0; i < captureVideoFxCount; i++) {
NvsCaptureVideoFx captureVideoFxByIndex = mStreamingContext.getCaptureVideoFxByIndex(i);
if (captureVideoFxByIndex.getBuiltinCaptureVideoFxName().equals(Constants.AR_SCENE)) {
String stringVal = captureVideoFxByIndex.getStringVal(Constants.AR_SCENE_ID_KEY);
NvsVideoEffect videoEffect = mNvsEffectSdkContext.createVideoEffect(Constants.AR_SCENE, nvsRational);
if (BuildConfig.FACE_MODEL == 240) {
videoEffect.setBooleanVal("Use Face Extra Info", true);
NvsARSceneManipulate arSceneManipulate = videoEffect.getARSceneManipulate();
videoEffect.setBooleanVal(Constants.MAX_FACES_RESPECT_MIN, true);
videoEffect.setBooleanVal("Beauty Effect", true);
videoEffect.setBooleanVal("Beauty Shape", true);
videoEffect.setBooleanVal("Face Mesh Internal Enabled", true);
videoEffect.setBooleanVal("Advanced Beauty Enable", true);
if (arSceneManipulate != null) {
arSceneManipulate.setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE);
arSceneManipulate.setDetectionAutoProbe(true);
if (!TextUtils.isEmpty(stringVal)) {
videoEffect.setStringVal(Constants.AR_SCENE_ID_KEY, stringVal);
// ... 64 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-086` `onCapturedPictureArrived`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3252`

API classes: `NvsVideoResolution`, `NvsRational`, `NvsEffect`, `NvsVideoEffect`, `NvsEffectRenderCore`, `NvsCaptureVideoFx`, `NvsARSceneManipulate`, `NvsStreamingContext`, `NvsCaptureCompoundCaption`, `NvsVideoEffectCompoundCaption`, `NvsColor`, `NvsCaptureAnimatedSticker`
Static/constants: `NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE`, `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K`, `NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED`, `NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA`
Common calls: `getFloatVal()`, `setFloatVal()`, `setBooleanVal()`, `isEmpty()`, `size()`, `getFxName()`, `add()`, `clear()`, `copyPixelsFromBuffer()`, `createVideoEffect()`, `observeOn()`, `getVideoEditResolution()`

Simple sequence:

```java
NvsVideoResolution mCurrentVideoResolution = new NvsVideoResolution();
mCurrentVideoResolution.imagePAR = new NvsRational(1, 1);
NvsVideoResolution videoEditResolution = Util.getVideoEditResolution(makeRatio);
int captureVideoFxCount = mStreamingContext.getCaptureVideoFxCount();
List<NvsEffect> effects = new ArrayList<>();
NvsRational nvsRational = new NvsRational(9, 16);
for (int i = 0; i < captureVideoFxCount; i++) {
NvsCaptureVideoFx captureVideoFxByIndex = mStreamingContext.getCaptureVideoFxByIndex(i);
if (captureVideoFxByIndex.getBuiltinCaptureVideoFxName().equals(Constants.AR_SCENE)) {
String stringVal = captureVideoFxByIndex.getStringVal(Constants.AR_SCENE_ID_KEY);
NvsVideoEffect videoEffect = mNvsEffectSdkContext.createVideoEffect(Constants.AR_SCENE, nvsRational);
if (BuildConfig.FACE_MODEL == 240) {
videoEffect.setBooleanVal("Use Face Extra Info", true);
NvsARSceneManipulate arSceneManipulate = videoEffect.getARSceneManipulate();
videoEffect.setBooleanVal(Constants.MAX_FACES_RESPECT_MIN, true);
videoEffect.setBooleanVal("Beauty Effect", true);
videoEffect.setBooleanVal("Beauty Shape", true);
videoEffect.setBooleanVal("Face Mesh Internal Enabled", true);
videoEffect.setBooleanVal("Advanced Beauty Enable", true);
if (arSceneManipulate != null) {
arSceneManipulate.setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE);
arSceneManipulate.setDetectionAutoProbe(true);
if (!TextUtils.isEmpty(stringVal)) {
videoEffect.setStringVal(Constants.AR_SCENE_ID_KEY, stringVal);
// ... 64 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-087` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java:53`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`
Common calls: `equals()`, `getSerializable()`

Simple sequence:

```java
if (arguments != null) {
mTag = (String) arguments.getSerializable(ARG_PARAM1);
mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
```

## `ar-makeup-segmentation-088` `initArguments`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java:57`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`
Common calls: `equals()`

Simple sequence:

```java
mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
mInstallType = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
```

## `ar-makeup-segmentation-089` `removeAllSkinColour`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCaptureFragment.java:220`

API classes: `NvsFx`
Common calls: `setFloatVal()`, `getCaptureBeautyFx()`

Simple sequence:

```java
if (null != mBeautyHelper) {
NvsFx nvsFx = mBeautyHelper.getCaptureBeautyFx();
nvsFx.setFloatVal(FxParams.BEAUTY_STRENGTH, 0);
nvsFx.setFloatVal(FxParams.ADVANCED_BEAUTY_INTENSITY, 0);
```

## `ar-makeup-segmentation-090` `applyBeauty`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:307`

API classes: `NvsFx`
Common calls: `equals()`, `getResources()`, `getString()`, `isEmpty()`, `getFloatVal()`, `add()`, `setFxNodes()`, `setAttachment()`, `getFxName()`, `setStrength()`, `setDefaultStrength()`, `setName()`

Simple sequence:

```java
NvsFx mArScene = mBeautyHelper.getCaptureBeautyFx();
List<IFxInfo> mSkins = BeautyDataManager.getBeautyList(mContext, true);
for (IFxInfo info : mSkins) {
String name = info.getName();
if (TextUtils.equals(name, mContext.getResources().getString(R.string.correctionColor))
|| TextUtils.equals(name, mContext.getResources().getString(R.string.sharpness))
|| TextUtils.equals(name, mContext.getResources().getString(R.string.whitening_B))) {
if (TextUtils.equals(info.getFxName(), FxParams.ADVANCED_BEAUTY_MATTE_INTENSITY)) {
double strength = mArScene.getFloatVal(FxParams.ADVANCED_BEAUTY_MATTE_INTENSITY);
info.setStrength(strength);
info.setDefaultStrength(strength);
double matteRadius = mArScene.getFloatVal(FxParams.ADVANCED_BEAUTY_MATTE_FILL_RADIUS);
if (null != fxParams) {
fxParams.setValue(matteRadius);
fxParams.setDefaultValue(matteRadius);
if (TextUtils.equals(info.getFxName(), FxParams.WHITENING_REDDENING)) {
double strength = mArScene.getFloatVal(FxParams.WHITENING_REDDENING);
info.setStrength(strength);
info.setDefaultStrength(strength);
if (null != mBuffingSkinData) {
mBuffingSkinData.setFxNodes(getBuffingSkinData(mArScene, mContext, beautyParams));
beautySkin.setName(mContext.getResources().getString(com.meishe.arscene.R.string.skin));
beautySkin.setResourceId(com.meishe.arscene.R.mipmap.icon_beauty_skin);
beautySkin.setFxNodes(getSkinData(mContext, isCustomTemplate, mBeautyHelper, assetsDirectory, beautyParams));
// ... 7 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-091` `getBuffingSkinData`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:390`

API classes: `NvsFx`
Common calls: `findParam()`, `getValue()`, `setSelected()`, `setDefaultFx()`, `setStrength()`, `setDefaultStrength()`, `getBuffingSkin()`, `remove()`, `size()`, `getParams()`, `isEmpty()`, `equals()`

Simple sequence:

```java
public List<IFxInfo> getBuffingSkinData(NvsFx mArScene, Context mContext, List<BeautyParam> beautyParams) {
List<IFxInfo> data = BeautyDataManager.getBuffingSkin(mContext);
List<BaseParam.Param> paramList = beautyParam.getParams();
if (null != typeParam) {
type = (double) typeParam.getValue();
if (null != strengthParam) {
beautyStrengthValue = (double) strengthParam.getValue();
if (null != intensityParam) {
intensityValue = (double) intensityParam.getValue();
for (IFxInfo info : data) {
if (TextUtils.equals(info.getFxName(), FxParams.BEAUTY_STRENGTH)) {
if ((beautyStrengthValue > 0) && (type == 0)) {
info.setSelected(true);
info.setDefaultFx(true);
info.setStrength(beautyStrengthValue);
info.setDefaultStrength(beautyStrengthValue);
int value = fxParams.getIntValue();
if (type == value) {
info.setSelected(true);
info.setDefaultFx(true);
info.setStrength(intensityValue);
info.setDefaultStrength(intensityValue);
```

## `ar-makeup-segmentation-092` `getWhiteningSkinData`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:459`

API classes: `NvsFx`
Common calls: `findParam()`, `getValue()`, `get()`, `setStrength()`, `setDefaultStrength()`, `setSelected()`, `getWhiteningSkin()`, `getParams()`, `isEmpty()`, `getParamList()`, `equals()`

Simple sequence:

```java
public List<IFxInfo> getWhiteningSkinData(NvsFx mArScene, Context mContext, List<BeautyParam> beautyParams) {
List<IFxInfo> data = BeautyDataManager.getWhiteningSkin(mContext);
List<BaseParam.Param> paramList = beautyParam.getParams();
Object value = typeParam.getValue();
List<FxParams> whitenParamList = iFxInfo.getParamList();
if (FxParams.WHITENING_LUT_FILE.equals(fxParams.key)) {
fxParams.value = param.getValue();
if (intensityParam != null) {
double strength = (double) intensityParam.getValue();
iFxInfo.setStrength(strength);
iFxInfo.setDefaultStrength(strength);
iFxInfo.setSelected(true);
if (intensityParam != null) {
double strength = (double) intensityParam.getValue();
iFxInfo.setStrength(strength);
iFxInfo.setDefaultStrength(strength);
iFxInfo.setSelected(true);
```

## `ar-makeup-segmentation-093` `applyShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:594`

API classes: `NvsFx`
Common calls: `isEmpty()`, `getBeautyShapeList()`, `getCaptureBeautyFx()`, `getFxName()`, `getFloatVal()`, `setStrength()`, `setDefaultStrength()`, `getParamList()`, `getStringVal()`, `equals()`, `getStringValue()`, `setValue()`

Simple sequence:

```java
List<IFxInfo> shapeList = BeautyDataManager.getBeautyShapeList(context);
NvsFx mArScene = mBeautyHelper.getCaptureBeautyFx();
for (IFxInfo info : shapeList) {
String fxName = info.getFxName();
double degree = mArScene.getFloatVal(fxName);
info.setStrength(degree);
info.setDefaultStrength(degree);
List<FxParams> fxParams = fxInfo.getParamList();
String uuid = mArScene.getStringVal(key);
if (TextUtils.equals(uuid, params.getStringValue())) {
if (!TextUtils.isEmpty(newPackageId)) {
params.setValue(newPackageId);
if (!TextUtils.isEmpty(newPackageId)) {
info.setPackageId(newPackageId);
info.setAssetPackagePath(getPackagePath(assetsDirectory, newPackageId));
```

## `ar-makeup-segmentation-094` `applyMicroShape`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:646`

API classes: `NvsFx`
Common calls: `isEmpty()`, `getMicroPlasticList()`, `getCaptureBeautyFx()`, `getFxName()`, `getFloatVal()`, `setStrength()`, `setDefaultStrength()`, `getParamList()`, `getStringVal()`, `equals()`, `getStringValue()`, `setValue()`

Simple sequence:

```java
List<IFxInfo> microShapeList = BeautyDataManager.getMicroPlasticList(context);
NvsFx mArScene = mBeautyHelper.getCaptureBeautyFx();
for (IFxInfo info : microShapeList) {
String fxName = info.getFxName();
double degree = mArScene.getFloatVal(fxName);
info.setStrength(degree);
info.setDefaultStrength(degree);
List<FxParams> fxParams = fxInfo.getParamList();
String uuid = mArScene.getStringVal(key);
if (TextUtils.equals(uuid, params.getStringValue())) {
if (!TextUtils.isEmpty(newPackageId)) {
params.setValue(newPackageId);
if (!TextUtils.isEmpty(newPackageId)) {
info.setPackageId(newPackageId);
info.setAssetPackagePath(getPackagePath(assetsDirectory, newPackageId));
```

## `ar-makeup-segmentation-095` `applyMakeup`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/beauty/BeautyCapturePresenter.java:755`

API classes: `NvsFx`
Common calls: `isEmpty()`, `getType()`, `getCaptureVideoFx()`, `getMakeupCategory()`, `equals()`, `isZh()`, `getDisplayNameZhCn()`, `getDisplayName()`, `getCover()`, `create()`, `setType()`, `setName()`

Simple sequence:

```java
NvsFx mArScene = mMakeupHelper.getCaptureVideoFx();
List<MakeupCategory> makeupCategories = MakeupDataManager.getMakeupCategory(context);
for (MakeupParam makeupParam : makeupParams) {
String type = makeupParam.getType();
for (MakeupCategory category : makeupCategories) {
if (TextUtils.equals(category.getType(), type)) {
name = Utils.isZh() ? category.getDisplayNameZhCn() : category.getDisplayName();
icon = category.getCover();
.setType(FxParams.CONTOURING)
.setName(name)
.setResourceId(icon)
.setFxName(type);
String packageId = mArScene.getStringVal(mMakeupHelper.getMakeupPackageKey(type));
compoundFxInfo.setPackageId(packageId);
compoundFxInfo.setAssetPackagePath(getPackagePath(assetsDirectory, packageId));
double degree = mArScene.getFloatVal(mMakeupHelper.getMakeupIntensityKey(type));
compoundFxInfo.setStrength(degree);
compoundFxInfo.setDefaultStrength(degree);
```

## `ar-makeup-segmentation-096` `initBeautifyParam`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1007`

API classes: `NvsFxDescription`
Static/constants: `NvsFxDescription.ParamInfoObject`
Common calls: `setMax()`, `getFloatVal()`, `setBooleanVal()`, `getFloat()`, `setEnabled()`, `setClickable()`, `appendBuiltinCaptureVideoFx()`, `setAIFaceOcclusion()`, `appendBeautyCaptureVideoFx()`, `getVideoFxDescription()`, `getAllParamsInfo()`, `getString()`

Simple sequence:

```java
if (mCanUseARFaceType == HUMAN_AI_TYPE_MS && mInitArScene) {
mARFaceU = mStreamingContext.appendBuiltinCaptureVideoFx(arSceneFxName);
if (mARFaceU != null) {
Utils.setAIFaceOcclusion(mARFaceU);
mARFaceU.setBooleanVal(arSceneBeauty, true);
mARFaceU.setBooleanVal(arSceneBeautyShape, true);
mCheekThinningSeekBar.setMax(SEEKBAR_BEAUTYSHAPE_MAXVALUE);
if (mIntentCheekThinning == -1) {
int cheekThinning = getCheekThinProgressVal(mARFaceU.getFloatVal(BEAUTIFY_SHAPE_EYE_ENLARGING));
mEyeEnlargingSeekBar.setMax(SEEKBAR_BEAUTYSHAPE_MAXVALUE);
if (mIntentEyeEnlarging == -1) {
int eyeEnlarge = getEyeEnlargeProgressVal(mARFaceU.getFloatVal(BEAUTIFY_SHAPE_EYE_ENLARGING));
if (mIntentStrength == -1) {
int stength = (int) (mARFaceU.getFloatVal(BEAUTIFY_ARSCENE_STRENGTH) * 100);
mBeautyVideoFx = mStreamingContext.appendBeautyCaptureVideoFx();
NvsFxDescription fxDescription = mStreamingContext.getVideoFxDescription(beautyFxName);
List<NvsFxDescription.ParamInfoObject> paramInfo = fxDescription.getAllParamsInfo();
for (NvsFxDescription.ParamInfoObject param : paramInfo) {
String paramName = param.getString("paramName");
double maxValue = param.getFloat("floatMaxVal");
double defVal = param.getFloat("floatDefVal");
mStrengthSeekBar.setMax((int) (maxValue * 100));
mCheekThinningSeekBar.setEnabled(false);
mCheekThinningSeekBar.setClickable(false);
// ... 2 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-097` `initBeautifyParam`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoCaptureActivity.java:1010`

API classes: `NvsFxDescription`
Static/constants: `NvsFxDescription.ParamInfoObject`
Common calls: `setMax()`, `getFloatVal()`, `setBooleanVal()`, `getFloat()`, `setEnabled()`, `setClickable()`, `appendBuiltinCaptureVideoFx()`, `setAIFaceOcclusion()`, `appendBeautyCaptureVideoFx()`, `getVideoFxDescription()`, `getAllParamsInfo()`, `getString()`

Simple sequence:

```java
if (mCanUseARFaceType == HUMAN_AI_TYPE_MS && mInitArScene) {
mARFaceU = mStreamingContext.appendBuiltinCaptureVideoFx(arSceneFxName);
if (mARFaceU != null) {
Utils.setAIFaceOcclusion(mARFaceU);
mARFaceU.setBooleanVal(arSceneBeauty, true);
mARFaceU.setBooleanVal(arSceneBeautyShape, true);
mCheekThinningSeekBar.setMax(SEEKBAR_BEAUTYSHAPE_MAXVALUE);
if (mIntentCheekThinning == -1) {
int cheekThinning = getCheekThinProgressVal(mARFaceU.getFloatVal(BEAUTIFY_SHAPE_EYE_ENLARGING));
mEyeEnlargingSeekBar.setMax(SEEKBAR_BEAUTYSHAPE_MAXVALUE);
if (mIntentEyeEnlarging == -1) {
int eyeEnlarge = getEyeEnlargeProgressVal(mARFaceU.getFloatVal(BEAUTIFY_SHAPE_EYE_ENLARGING));
if (mIntentStrength == -1) {
int stength = (int) (mARFaceU.getFloatVal(BEAUTIFY_ARSCENE_STRENGTH) * 100);
mBeautyVideoFx = mStreamingContext.appendBeautyCaptureVideoFx();
NvsFxDescription fxDescription = mStreamingContext.getVideoFxDescription(beautyFxName);
List<NvsFxDescription.ParamInfoObject> paramInfo = fxDescription.getAllParamsInfo();
for (NvsFxDescription.ParamInfoObject param : paramInfo) {
String paramName = param.getString("paramName");
double maxValue = param.getFloat("floatMaxVal");
double defVal = param.getFloat("floatDefVal");
mStrengthSeekBar.setMax((int) (maxValue * 100));
mCheekThinningSeekBar.setEnabled(false);
mCheekThinningSeekBar.setClickable(false);
// ... 2 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-098` `setMakeupEffect`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:116`

API classes: `NvsVideoClip`
Common calls: `getClipByIndex()`, `entrySet()`, `getValue()`, `applyMakeupFx()`

Simple sequence:

```java
for (int i = 0; i < clips; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
for (Map.Entry<String, Makeup> entry : mSelectedMakeupMap.entrySet()) {
Makeup value = entry.getValue();
mMakeupHelper.applyMakeupFx(value, videoClip);
```

## `ar-makeup-segmentation-099` `setMakeupEffect`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:117`

API classes: `NvsVideoClip`
Common calls: `getClipByIndex()`, `entrySet()`, `getValue()`, `applyMakeupFx()`

Simple sequence:

```java
for (int i = 0; i < clips; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
for (Map.Entry<String, Makeup> entry : mSelectedMakeupMap.entrySet()) {
Makeup value = entry.getValue();
mMakeupHelper.applyMakeupFx(value, videoClip);
```

## `ar-makeup-segmentation-100` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:132`

API classes: `NvsColor`
Common calls: `setOnClickListener()`, `setOnMakeUpEventListener()`, `MakeUpEventListener()`

Simple sequence:

```java
mMakeupFinish.setOnClickListener(this);
mMakeUpView.setOnMakeUpEventListener(new EditMakeUpView.MakeUpEventListener() {
public void onMakeupColorChanged(String makeupId, NvsColor color) {
```

## `ar-makeup-segmentation-101` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:135`

API classes: `NvsColor`
Common calls: `setOnMakeUpEventListener()`, `MakeUpEventListener()`

Simple sequence:

```java
mMakeUpView.setOnMakeUpEventListener(new EditMakeUpView.MakeUpEventListener() {
public void onMakeupColorChanged(String makeupId, NvsColor color) {
```

## `ar-makeup-segmentation-102` `makeupIntensityChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:173`

API classes: `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `setMakeupIntensity()`

Simple sequence:

```java
if (mTimeline == null) {
NvsVideoTrack videoTrackByIndex = mTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrackByIndex.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrackByIndex.getClipByIndex(i);
mMakeupHelper.setMakeupIntensity(videoClip, makeupId, intensity);
```

## `ar-makeup-segmentation-103` `makeupColorChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:197`

API classes: `NvsColor`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `setMakeupColor()`

Simple sequence:

```java
private void makeupColorChanged(String makeupId, NvsColor color) {
if (mTimeline == null) {
NvsVideoTrack videoTrackByIndex = mTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrackByIndex.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip videoClip = videoTrackByIndex.getClipByIndex(i);
mMakeupHelper.setMakeupColor(videoClip, makeupId, color);
```

## `ar-makeup-segmentation-104` `clearShape`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:289`

API classes: `NvsVideoFx`
Common calls: `isEmpty()`, `instance()`, `getClipInfoData()`, `size()`, `get()`, `getBeautyFxInfo()`, `getBeautys()`, `getPackageId()`, `getFxName()`, `setFloatVal()`

Simple sequence:

```java
private void clearShape(int i, NvsVideoFx nvsVideoFx) {
ArrayList<ClipInfo> clipInfos = TimelineData.instance().getClipInfoData();
BeautyFxInfo beautyFxInfo = clipInfo.getBeautyFxInfo();
HashSet<IFxInfo> infos = beautyFxInfo.getBeautys();
for (IFxInfo info : infos) {
if (info instanceof CompoundFxInfo && !TextUtils.isEmpty(info.getPackageId())) {
String fxName = compoundFxInfo.getFxName();
if (!TextUtils.isEmpty(fxName)) {
nvsVideoFx.setFloatVal(fxName, 0);
```

## `ar-makeup-segmentation-105` `clearAllCustomMakeup`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:322`

API classes: `NvsVideoFx`
Common calls: `getMakeupCategoryList()`, `getMaterialType()`, `getCategoryContent()`, `setSelectedPosition()`, `upperCaseName()`, `getDisplayName()`

Simple sequence:

```java
private void clearAllCustomMakeup(NvsVideoFx videoFx) {
List<MakeupCategory> makeupCategoryList = mMakeUpView.getMakeupCategoryList();
for (MakeupCategory categoryInfo : makeupCategoryList) {
if (categoryInfo.getMaterialType() == 21) {
categoryInfo.getCategoryContent().setSelectedPosition(0);
resetCustomMakeup(videoFx, Util.upperCaseName(categoryInfo.getDisplayName()));
```

## `ar-makeup-segmentation-106` `postSeekAction`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/makeup/BeautyMakeupActivity.java:360`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME`
Common calls: `putInt()`, `getLayoutParams()`, `beginTransaction()`, `setTimeline()`, `setPlayFlag()`, `instance()`, `getMakeRatio()`, `putBoolean()`, `setArguments()`, `add()`, `commit()`, `show()`

Simple sequence:

```java
mVideoFragment.setTimeline(mTimeline);
mVideoFragment.setPlayFlag(NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
bundle.putInt("titleHeight", mTitleBar.getLayoutParams().height);
bundle.putInt("bottomHeight", mBottomLayout.getLayoutParams().height);
bundle.putInt("ratio", TimelineData.instance().getMakeRatio());
mVideoFragment.setArguments(bundle);
```

## `ar-makeup-segmentation-107` `setMakeupCategoryList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java:117`

API classes: `NvsColor`
Common calls: `findViewById()`, `setVisibility()`, `setBitmap()`, `setColor()`, `setText()`, `getEffectContent()`, `decodeResource()`, `setSelected()`, `getId()`, `from()`, `inflate()`, `setMax()`

Simple sequence:

```java
mMakeupSeekBar.setMax(100);
mMakeupSeekBar.setPointEnable(false);
mMakeupSeekBar.setBreakProgress(0);
mMakeupRecyclerView.setLayoutManager(layoutManager);
mMakeupRecyclerView.setAdapter(mMakeupAdapter);
mMakeupAdapter.setEnable(true);
mColorSeekView.setOnColorChangedListener(new ColorSeekBar.OnColorChangedListener() {
mCustomButtonView.setColor(co);
mTvColor.setVisibility(View.VISIBLE);
mTvColor.setText(String.format(getResources().getString(R.string.make_up_tone), ColorUtil.intColorToHexString(color).toUpperCase()));
NvsColor nvsColor = new NvsColor(red, green, blue, alphaF);
if (selectItem != null) {
MakeupParamContent effectContent = selectItem.getEffectContent();
if (effectContent != null) {
MakeupParam makeupParam = effectContent.getMakeupParam(0);
if (makeupParam != null) {
makeupParam.setColorData(colorData);
mCustomButtonView.setBitmap(BitmapFactory.decodeResource(getResources(), R.mipmap.icon_no_color_selected, null));
mCustomButtonView.setOnClickListener(new OnClickListener() {
if (mColorSeekView.getVisibility() == View.VISIBLE) {
mColorSeekView.setVisibility(INVISIBLE);
mCustomButtonView.setSelected(false);
mCustomButtonView.setText("");
mCustomButtonView.setBitmap(BitmapFactory.decodeResource(getResources(), R.mipmap.icon_no_color_selected, null));
// ... 11 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-108` `onColorChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java:145`

API classes: `NvsColor`
Common calls: `setColor()`, `setVisibility()`, `setText()`, `format()`, `getString()`, `intColorToHexString()`, `toUpperCase()`, `alpha()`, `red()`, `green()`, `blue()`, `getEffectContent()`

Simple sequence:

```java
mCustomButtonView.setColor(co);
mTvColor.setVisibility(View.VISIBLE);
mTvColor.setText(String.format(getResources().getString(R.string.make_up_tone), ColorUtil.intColorToHexString(color).toUpperCase()));
NvsColor nvsColor = new NvsColor(red, green, blue, alphaF);
if (selectItem != null) {
MakeupParamContent effectContent = selectItem.getEffectContent();
if (effectContent != null) {
MakeupParam makeupParam = effectContent.getMakeupParam(0);
if (makeupParam != null) {
makeupParam.setColorData(colorData);
```

## `ar-makeup-segmentation-109` `onSubViewSelect`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java:426`

API classes: `NvsColor`
Common calls: `setVisibility()`, `size()`, `getValue()`, `setText()`, `getEffectContent()`, `get()`, `setValue()`, `setProgress()`, `format()`, `getString()`, `getMakeupParams()`, `getParams()`

Simple sequence:

```java
if (selectItem.getEffectContent() == null) {
List<MakeupParam> makeupParams = selectItem.getEffectContent().getMakeupParams();
List<BaseParam.Param> params = makeupParam.getParams();
for (BaseParam.Param param : params) {
if (param.getValue() instanceof Float) {
intensity = (float) param.getValue();
if (intensity == Float.MIN_VALUE) {
param.setValue(intensity = DEFAULT_MAKEUP_INTENSITY);
mMakeupSeekBar.setVisibility(VISIBLE);
mMakeupSeekBar.setProgress((int) (intensity * 100));
List<RecommendColor> recommendColors = makeupParam.getMakeupRecommendColors();
for (int index = 0; index < recommendColors.size(); index++) {
colors[index] = splitColor(recommendColors.get(index).getMakeupColor());
ColorData colorData = makeupParam.getColorData();
String progress = String.format(getResources().getString(R.string.make_up_transparency), (int) (intensity * 100)) + "%";
mTvAlpha.setText(progress);
mTvColor.setVisibility((color == -1) ? INVISIBLE : VISIBLE);
if (color >= 0) {
mTvColor.setText(String.format(getResources().getString(R.string.make_up_tone), ColorUtil.intColorToHexString(color).toUpperCase()));
mCustomButtonView.setVisibility(VISIBLE);
mMakeupColorHinLayout.setVisibility(VISIBLE);
mMakeupSeekBar.setVisibility(VISIBLE);
mMakeupSeekBar.setProgress((int) (intensity * 100));
mCustomButtonView.setColor(color);
// ... 6 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-110` `onDonwloadAssetFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/view/EditMakeUpView.java:565`

API classes: `NvsColor`

Simple sequence:

```java
void onMakeupColorChanged(String makeupId, NvsColor color);
```

## `ar-makeup-segmentation-111` `setSkinApply`

Source: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:37`

API classes: `NvsTimeline`

Simple sequence:

```java
public void setSkinApply(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {
applyBeautyFx(FxParams.BEAUTY_SKIN, mTimeline, mBeautyHelper, info);
```

## `ar-makeup-segmentation-112` `setSharpenApply`

Source: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:49`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoFx`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `enableBeauty()`, `getBeautyFx()`, `setBooleanVal()`, `onSeekTimeline()`

Simple sequence:

```java
public void setSharpenApply(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, boolean isSharpenOpen) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int count = videoTrack.getClipCount();
for (int i = 0; i < count; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
NvsVideoFx nvsVideoFx = mBeautyHelper.getBeautyFx(videoClip);
nvsVideoFx.setBooleanVal(FxParams.DEFAULT_SHARPEN_ENABLE, isSharpenOpen);
```

## `ar-makeup-segmentation-113` `isSupportMatte`

Source: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:78`

API classes: `NvsARSceneManipulate`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`, `NvsVideoFx`
Static/constants: `NvsARSceneManipulate.CheckedFunctionType_Matte`
Common calls: `isSupportMatte()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `insertBuiltinFx()`, `getARSceneManipulate()`, `removeFx()`, `isFunctionAvailable()`

Simple sequence:

```java
public boolean isSupportMatte(NvsTimeline mTimeline, BeautyFxInfo mBeautyParams) {
if ((null == mTimeline) || (null == mBeautyParams)) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int count = videoTrack.getClipCount();
for (int i = 0; i < count; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
NvsVideoFx videoFx = videoClip.insertBuiltinFx(Constants.AR_SCENE, 0);
NvsARSceneManipulate arSceneManipulate = videoFx.getARSceneManipulate();
videoClip.removeFx(0);
return arSceneManipulate.isFunctionAvailable(NvsARSceneManipulate.CheckedFunctionType_Matte);
```

## `ar-makeup-segmentation-114` `setFaceApply`

Source: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:117`

API classes: `NvsTimeline`

Simple sequence:

```java
public void setFaceApply(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {
applyBeautyFx(FxParams.BEAUTY_FACE, mTimeline, mBeautyHelper, info);
```

## `ar-makeup-segmentation-115` `setSmallApply`

Source: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:129`

API classes: `NvsTimeline`

Simple sequence:

```java
public void setSmallApply(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {
applyBeautyFx(FxParams.BEAUTY_SMALL, mTimeline, mBeautyHelper, info);
```

## `ar-makeup-segmentation-116` `applyBeautyFx`

Source: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:142`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `enableAdvancedBeauty()`, `enableShape()`, `enableShapeNew()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `enableBeauty()`, `equals()`, `getFxName()`, `applyBeautyFx()`, `onSeekTimeline()`

Simple sequence:

```java
public void applyBeautyFx(int type, NvsTimeline mTimeline, BeautyHelper mBeautyHelper, IFxInfo info) {
if (!checkIsNull(mTimeline, mBeautyHelper, info)) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int count = videoTrack.getClipCount();
for (int i = 0; i < count; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
if (TextUtils.equals(info.getFxName(), FxParams.ADVANCED_BEAUTY_MATTE_INTENSITY)) {
mBeautyHelper.applyBeautyFx(videoClip, info);
```

## `ar-makeup-segmentation-117` `setCancelDefaultFxValue`

Source: `app/src/main/java/com/meishe/sdkdemo/presenter/BeautyPresenter.java:196`

API classes: `NvsVideoClip`, `NvsTimeline`, `NvsVideoTrack`, `NvsVideoFx`
Common calls: `getClipByIndex()`, `getVideoTrackByIndex()`, `getClipCount()`, `getBeautys()`, `enableAdvancedBeauty()`, `equals()`, `getFxName()`, `getBeautyFx()`, `setFloatVal()`

Simple sequence:

```java
public void setCancelDefaultFxValue(NvsTimeline mTimeline, BeautyHelper mBeautyHelper, BeautyFxInfo mBeautyParams) {
if ((null == mTimeline) || (null == mBeautyParams) || (null == mBeautyHelper)) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int count = videoTrack.getClipCount();
HashSet<IFxInfo> data = mBeautyParams.getBeautys();
for (int i = 0; i < count; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
if (TextUtils.equals(info.getFxName(), FxParams.ADVANCED_BEAUTY_INTENSITY)) {
for (int i = 0; i < count; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
NvsVideoFx videoFx = mBeautyHelper.getBeautyFx(videoClip);
if (!isAddAdvancedBuffing) {
videoFx.setFloatVal(FxParams.ADVANCED_BEAUTY_INTENSITY, 0);
```

## `ar-makeup-segmentation-118` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:291`

API classes: `NvsAIContext`, `NvsFaceDetector`
Static/constants: `NvsAIContext.getInstance`, `NvsAIContext.init`, `NvsFaceDetector.createNvsFaceDetector`, `NvsFaceDetector.AI_SDK_DETECTION_FRAME_VIDEO_MODE`
Common calls: `getInstance()`, `init()`, `getExternalFilesDir()`, `getFilesDir()`, `copyFileIfNeed()`, `createNvsFaceDetector()`

Simple sequence:

```java
mAISdkContext = NvsAIContext.getInstance();
mAISdkContext = NvsAIContext.init(getApplicationContext(), licensePath, 0);
File rootDir = getApplicationContext().getExternalFilesDir("");
if (AndroidOS.USE_SCOPED_STORAGE) {
rootDir = getApplicationContext().getFilesDir();
if (copySuccess) {
mNvsFaceDetector = NvsFaceDetector.createNvsFaceDetector(destModelPath, NvsFaceDetector.AI_SDK_DETECTION_FRAME_VIDEO_MODE);
```

## `ar-makeup-segmentation-119` `detectFace`

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1431`

API classes: `NvsFaceDetector`, `NvsFaceData`
Static/constants: `NvsFaceDetector.NvsFaceData`, `NvsFaceDetector.AI_SDK_DETECTION_BUFFER_FORMAT_RGBA`
Common calls: `setHumanInfoList()`, `clear()`, `add()`, `detectBuffer()`, `isEmpty()`, `getFaceRect()`, `d()`, `getPointFList()`, `getPitch()`, `getYaw()`, `getRoll()`

Simple sequence:

```java
mFacePointView.setHumanInfoList(mHumanInfos, width, height);
List<NvsFaceDetector.NvsFaceData> faceDataList = mNvsFaceDetector.detectBuffer(
data, width, height, NvsFaceDetector.AI_SDK_DETECTION_BUFFER_FORMAT_RGBA, mDetectOrientation, 0);
if (!CommonUtils.isEmpty(faceDataList)) {
for (NvsFaceDetector.NvsFaceData faceData : faceDataList) {
Rect srcRect = faceData.getFaceRect();
if (isShowFaceFrame) {
List<PointF> position2Ds = faceData.getPointFList();
HumanInfo humanInfo = new HumanInfo(faceRect, pointList, faceData.getPitch(),
faceData.getYaw(), faceData.getRoll());
mFacePointView.setHumanInfoList(mHumanInfos, width, height);
if (isShowFaceFrame) {
mFacePointView.setHumanInfoList(mHumanInfos, width, height);
```

## `ar-makeup-segmentation-120` `buildTimelineMakeup`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2098`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`

Simple sequence:

```java
public static void buildTimelineMakeup(NvsTimeline mTimeline, MakeupHelper makeupHelper) {
if ((null == mTimeline) || (null == makeupHelper)) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int count = videoTrack.getClipCount();
for (int i = 0; i < count; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
```

## `ar-makeup-segmentation-121` `applyMakeupFx`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2123`

API classes: `NvsVideoClip`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `applyMakeupFx()`, `instance()`, `getSelectedMakeupMap()`, `isEmpty()`, `getInstance()`, `get()`, `entrySet()`, `equals()`, `getKey()`, `getValue()`

Simple sequence:

```java
public static void applyMakeupFx(NvsVideoClip videoClip, MakeupHelper makeupHelper) {
HashMap<String, Makeup> makeupHashMap = TimelineData.instance().getSelectedMakeupMap();
if (makeupHelper == null) {
makeupHelper = new MakeupHelper(NvsStreamingContext.getInstance(), BuildConfig.FACE_MODEL == 240, false);
makeupHelper.applyMakeupFx(makeup, videoClip);
for (Map.Entry<String, Makeup> entry : makeupHashMap.entrySet()) {
if (!MakeupDataManager.COMBINED_MAKEUP_TYPE.equals(entry.getKey())) {
makeupHelper.applyMakeupFx(entry.getValue(), videoClip);
```

## `ar-makeup-segmentation-122` `buildTimelineBeauty`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2155`

API classes: `NvsTimeline`, `NvsVideoTrack`, `NvsVideoClip`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `get()`

Simple sequence:

```java
public static void buildTimelineBeauty(NvsTimeline mTimeline, ArrayList<ClipInfo> clipInfoData, BeautyHelper beautyHelper) {
if ((null == clipInfoData) || (null == mTimeline) || (null == beautyHelper)) {
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int count = videoTrack.getClipCount();
for (int i = 0; i < count; i++) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(i);
```

## `ar-makeup-segmentation-123` `applyBeautyFx`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2184`

API classes: `NvsVideoClip`, `NvsStreamingContext`, `NvsVideoFx`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `isOpenSmall()`, `isOpenFace()`, `isOpenSkin()`, `getBeautyFxInfo()`, `getInstance()`, `instance()`, `isSingleBufferMode()`, `enableBeauty()`, `enableShape()`, `enableShapeNew()`, `enableAdvancedBeauty()`, `getBeautys()`

Simple sequence:

```java
public static void applyBeautyFx(NvsVideoClip videoClip, ClipInfo clipInfo, BeautyHelper beautyHelper) {
BeautyFxInfo beautyFxInfo = clipInfo.getBeautyFxInfo();
if (null == beautyHelper) {
beautyHelper = new BeautyHelper(NvsStreamingContext.getInstance()
HashSet<IFxInfo> fxData = beautyFxInfo.getBeautys();
String fxName = info.getFxName();
beautyHelper.applyBeautyFx(videoClip, info);
NvsVideoFx videoFx = beautyHelper.getBeautyFx(videoClip);
if (!isAddAdvancedBuffing) {
videoFx.setFloatVal(FxParams.ADVANCED_BEAUTY_INTENSITY, 0);
```

## `ar-makeup-segmentation-124` `getPackageType`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:250`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER`

Simple sequence:

```java
if (assetType == NvAsset.ASSET_THEME) {
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_CONTEXT;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_IN_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_OUT_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
// ... 2 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-125` `getPackageType`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAsset.java:251`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER`

Simple sequence:

```java
if (assetType == NvAsset.ASSET_THEME) {
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_CONTEXT;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_IN_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_OUT_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
// ... 2 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-126` `onDestroy`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:226`

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

## `ar-makeup-segmentation-127` `setSelectedMakeupMap`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/TimelineData.java:160`

API classes: `NvsVideoResolution`

Simple sequence:

```java
public void setVideoResolution(NvsVideoResolution resolution) {
```

## `ar-makeup-segmentation-128` `notifyFaceFeatureInfos`

Source: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:116`

API classes: `NvsARSceneManipulate`, `NvsFaceFeatureInfo`
Static/constants: `NvsARSceneManipulate.NvsFaceFeatureInfo`
Common calls: `append()`, `isEmpty()`, `get()`, `delete()`, `length()`, `format()`, `setText()`, `toString()`, `post()`, `getAvatarExpressions()`, `size()`

Simple sequence:

```java
public void notifyFaceFeatureInfos(List<NvsARSceneManipulate.NvsFaceFeatureInfo> list) {
NvsARSceneManipulate.NvsFaceFeatureInfo info = list.get(0);
List<Float> avatarExpressions = info.getAvatarExpressions();
textLeftValue.setText(leftValue.toString());
textRightValue.setText(rightValue.toString());
```

## `ar-makeup-segmentation-129` `notifyFaceFeatureInfos`

Source: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:117`

API classes: `NvsARSceneManipulate`, `NvsFaceFeatureInfo`
Static/constants: `NvsARSceneManipulate.NvsFaceFeatureInfo`
Common calls: `append()`, `isEmpty()`, `get()`, `delete()`, `length()`, `format()`, `setText()`, `toString()`, `post()`, `getAvatarExpressions()`, `size()`

Simple sequence:

```java
NvsARSceneManipulate.NvsFaceFeatureInfo info = list.get(0);
List<Float> avatarExpressions = info.getAvatarExpressions();
textLeftValue.setText(leftValue.toString());
textRightValue.setText(rightValue.toString());
```

## `ar-makeup-segmentation-130` `notifyTotalTimeCost`

Source: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:160`

API classes: `NvsARSceneManipulate`, `NvsHandFeatureInfo`
Static/constants: `NvsARSceneManipulate.NvsHandFeatureInfo`

Simple sequence:

```java
public void notifyHandFeatureInfos(List<NvsARSceneManipulate.NvsHandFeatureInfo> list) {
```

## `ar-makeup-segmentation-131` `onTabReselected`

Source: `app/src/main/java/com/meishe/sdkdemo/view/MakeUpSingleView.java:259`

API classes: `NvsColor`
Common calls: `setOnColorChangedListener()`, `OnColorChangedListener()`, `setVisibility()`, `setText()`, `format()`, `getString()`, `intColorToHexString()`, `toUpperCase()`, `alpha()`, `red()`, `green()`, `blue()`

Simple sequence:

```java
mColorPickerView.setOnColorChangedListener(new ColorPickerView.OnColorChangedListener() {
mTvColor.setVisibility(View.VISIBLE);
mTvColor.setText(String.format(getResources().getString(R.string.make_up_tone), ColorUtil.intColorToHexString(color).toUpperCase()));
NvsColor nvsColor = new NvsColor(red, green, blue, alphaF);
if (selectItem != null) {
MakeupParamContent effectContent = selectItem.getEffectContent();
if (effectContent != null) {
MakeupParam makeupParam = effectContent.getMakeupParam(0);
if (makeupParam != null) {
makeupParam.setColorData(colorData);
```

## `ar-makeup-segmentation-132` `onDonwloadAssetFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/view/MakeUpSingleView.java:773`

API classes: `NvsColor`

Simple sequence:

```java
void onMakeupColorChanged(String makeupId, NvsColor color);
```

## `ar-makeup-segmentation-133` `onTabReselected`

Source: `app/src/main/java/com/meishe/sdkdemo/view/MakeUpView.java:134`

API classes: `NvsColor`
Common calls: `getInstacne()`, `setOnColorChangedListener()`, `OnColorChangedListener()`, `setVisibility()`, `setText()`, `format()`, `getString()`, `intColorToHexString()`, `toUpperCase()`, `getMakeupEffect()`, `setColorData()`, `addMakeupEffect()`

Simple sequence:

```java
mColorPickerView.setOnColorChangedListener(new ColorPickerView.OnColorChangedListener() {
mTvColor.setVisibility(View.VISIBLE);
mTvColor.setText(String.format(getResources().getString(R.string.make_up_tone), ColorUtil.intColorToHexString(color).toUpperCase()));
MakeupData makeupData = MakeupManager.getInstacne().getMakeupEffect(mCurrentEffectId);
makeupData.setColorData(colorData);
MakeupManager.getInstacne().addMakeupEffect(mCurrentEffectId, makeupData);
NvsColor nvsColor = new NvsColor(red, green, blue, alphaF);
```

## `ar-makeup-segmentation-134` `onDonwloadAssetFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/view/MakeUpView.java:531`

API classes: `NvsColor`

Simple sequence:

```java
void onMakeupColorChanged(String makeupId, NvsColor color);
```

## `ar-makeup-segmentation-135` `setAIFaceOcclusion`

Source: `libBase/src/main/java/com/meishe/base/utils/Utils.java:660`

API classes: `NvsStreamingContext`, `NvsFx`
Static/constants: `NvsStreamingContext.getInstance`, `NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH`
Common calls: `getInstance()`, `getDeviceCpuLevel()`, `setBooleanVal()`

Simple sequence:

```java
public static void setAIFaceOcclusion(NvsFx arSceneFx) {
if (null == NvsStreamingContext.getInstance()) {
int level = NvsStreamingContext.getInstance().getDeviceCpuLevel();
if (level == NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH) {
arSceneFx.setBooleanVal("AI Face Occlusion Enabled", true);
```

## `ar-makeup-segmentation-136` `setAIFaceOcclusion`

Source: `libBase/src/main/java/com/meishe/base/utils/Utils.java:664`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
if (null == NvsStreamingContext.getInstance()) {
```

## `ar-makeup-segmentation-137` `getPackageType`

Source: `libBase/src/main/java/com/meishe/utils/NvAsset.java:239`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER`

Simple sequence:

```java
if (assetType == NvAsset.ASSET_THEME) {
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_CONTEXT;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_IN_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_OUT_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
// ... 1 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-138` `getPackageType`

Source: `libBase/src/main/java/com/meishe/utils/NvAsset.java:240`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER`

Simple sequence:

```java
if (assetType == NvAsset.ASSET_THEME) {
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_OUT_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_CONTEXT;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_IN_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_OUT_ANIMATION;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH;
return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_WARP;
// ... 1 more SDK-related lines omitted in this compressed snippet ...
```

## `ar-makeup-segmentation-139` `installAssetPackageSynchronous`

Source: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:181`

API classes: `NvsAssetPackageManager`, `NvsStreamingContext`
Static/constants: `NvsAssetPackageManager.AssetPackageManagerCallback`, `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `getAssetPackageManager()`, `setCallbackInterface()`

Simple sequence:

```java
public static void installAssetPackageAsynchronous(String packagePath, String licPath, int packageType, StringBuilder stringBuilder, NvsAssetPackageManager.AssetPackageManagerCallback callback) {
NvsStreamingContext.getInstance().getAssetPackageManager().setCallbackInterface(callback);
```

## `ar-makeup-segmentation-140` `showPropsToast`

Source: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:222`

API classes: `NvsAssetPackageManager`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `getAssetPackageManager()`, `getARSceneAssetPackagePrompt()`, `isEmpty()`, `showToastCenter()`

Simple sequence:

```java
NvsAssetPackageManager manager = NvsStreamingContext.getInstance().getAssetPackageManager();
String packagePrompt = manager.getARSceneAssetPackagePrompt(sceneId);
```

## `ar-makeup-segmentation-141` `applyBeautyFaceEffect`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1170`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `get()`, `setFloatVal()`, `getFxCount()`, `getFxByIndex()`, `getAttachment()`, `appendBuiltinFx()`, `e()`, `setAttachment()`

Simple sequence:

```java
NvsVideoClip videoClip = getObject();
int fxCount = videoClip.getFxCount();
NvsVideoFx arSceneFx = null;
for (int i = 0; i < fxCount; i++) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
Object attachment = videoFx.getAttachment(ATTACHMENT_KEY_VIDEO_CLIP_AR_SCENE);
arSceneFx.setAttachment(ATTACHMENT_KEY_VIDEO_CLIP_AR_SCENE, VIDEO_FX_AR_SCENE);
arSceneFx.setFloatVal(VIDEO_FX_BEAUTY_STRENGTH, strength == null ? 50 / 100f : strength);
arSceneFx.setFloatVal(VIDEO_FX_BEAUTY_WHITENING, whitening == null ? 0 : whitening);
arSceneFx.setFloatVal(VIDEO_FX_BEAUTY_REDDENING, ruddy == null ? 0 : ruddy);
```

## `ar-makeup-segmentation-142` `applyBeautyShapeFaceEffect`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1216`

API classes: `NvsVideoFx`, `NvsVideoClip`
Common calls: `getFxCount()`, `getFxByIndex()`, `getAttachment()`, `appendBuiltinFx()`, `e()`, `setAttachment()`, `keySet()`, `setFloatVal()`, `get()`

Simple sequence:

```java
NvsVideoClip videoClip = getObject();
int fxCount = videoClip.getFxCount();
NvsVideoFx arSceneFx = null;
for (int i = 0; i < fxCount; i++) {
NvsVideoFx videoFx = videoClip.getFxByIndex(i);
Object attachment = videoFx.getAttachment(ATTACHMENT_KEY_VIDEO_CLIP_AR_SCENE);
arSceneFx.setAttachment(ATTACHMENT_KEY_VIDEO_CLIP_AR_SCENE, VIDEO_FX_AR_SCENE);
if (!isBeautyEffectKey(key)) {
arSceneFx.setFloatVal(key, mFaceEffectParameter.get(key));
```

## `ar-makeup-segmentation-143` `resetBeautyShape`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1271`

API classes: `NvsVideoFx`
Common calls: `keySet()`, `setFloatVal()`

Simple sequence:

```java
public void resetBeautyShape(NvsVideoFx nvsVideoFx) {
if (!isBeautyEffectKey(key)) {
nvsVideoFx.setFloatVal(key, 0);
```

## `ar-makeup-segmentation-144` `resetBeauty`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1286`

API classes: `NvsVideoFx`
Common calls: `setFloatVal()`, `put()`

Simple sequence:

```java
public void resetBeauty(NvsVideoFx nvsVideoFx) {
nvsVideoFx.setFloatVal(VIDEO_FX_BEAUTY_STRENGTH, 50 / 100f);
nvsVideoFx.setFloatVal(VIDEO_FX_BEAUTY_WHITENING, 0f);
nvsVideoFx.setFloatVal(VIDEO_FX_BEAUTY_REDDENING, 0f);
```

## `ar-makeup-segmentation-145` `openBeautyFx`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamVideoClip.java:1306`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE`
Common calls: `setDetectionMode()`

Simple sequence:

```java
if (arSceneManipulate != null) {
arSceneManipulate.setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE);
```

## `ar-makeup-segmentation-146` `playNow`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:245`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME`, `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`
Common calls: `e()`, `getDuration()`, `getInstance()`, `isUseFaceShape()`, `playbackTimeline()`

Simple sequence:

```java
if ((mStreamingContext == null) || (mNvsTimeline == null)) {
Log.e(TAG, "playNow: mStreamingContext or mNvsTimeline is null!");
if (end == -1) {
end = mNvsTimeline.getDuration();
if (EditorEngine.getInstance().isUseFaceShape()) {
flag = NvsStreamingContext.STREAMING_ENGINE_PLAYBACK_FLAG_BUDDY_HOST_VIDEO_FRAME;
mStreamingContext.playbackTimeline(mNvsTimeline, start, end, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, true, flag);
```

## `ar-makeup-segmentation-147` `grabBitmapFromAuxiliaryTimelineAsync`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:526`

API classes: `NvsStreamingContext`, `NvsRational`
Static/constants: `NvsStreamingContext.ImageGrabberCallback`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getInstance()`, `isUseFaceShape()`, `setImageGrabberCallback()`, `grabImageFromTimelineAsync()`, `e()`, `getDuration()`

Simple sequence:

```java
public void grabBitmapFromAuxiliaryTimelineAsync(long timestamp, NvsStreamingContext.ImageGrabberCallback callback) {
if (EditorEngine.getInstance().isUseFaceShape()) {
flag |= NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME;
mAuxiliaryStreamingContext.setImageGrabberCallback(callback);
boolean b = mAuxiliaryStreamingContext.grabImageFromTimelineAsync(mAuxiliaryTimeline, timestamp, new NvsRational(1, 1), flag);
Log.e("grabImageFrom", "grabImageFrom = " + b + " duration=" + mAuxiliaryTimeline.getDuration() + "  time =" + timestamp);
```

## `ar-makeup-segmentation-148` `grabBitmapFromAuxiliaryTimelineAsync`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:531`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getInstance()`, `isUseFaceShape()`

Simple sequence:

```java
if (EditorEngine.getInstance().isUseFaceShape()) {
flag |= NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME;
```

## `ar-makeup-segmentation-149` `grabBitmapFromTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:548`

API classes: `NvsRational`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getInstance()`, `isUseFaceShape()`, `grabImageFromTimeline()`

Simple sequence:

```java
public Bitmap grabBitmapFromTimeline(long timestamp, NvsRational proxyScale) {
if (EditorEngine.getInstance().isUseFaceShape()) {
flag = NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME;
return mStreamingContext.grabImageFromTimeline(mNvsTimeline, timestamp, proxyScale, flag);
```

## `ar-makeup-segmentation-150` `grabBitmapFromTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:550`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getInstance()`, `isUseFaceShape()`

Simple sequence:

```java
if (EditorEngine.getInstance().isUseFaceShape()) {
flag = NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME;
```
