# Demo Simple Snippets - Asset Packages

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: NvsAssetPackageManager install/query/update flows, package type constants, theme/transition/caption/sticker/filter package IDs, and package callbacks.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [assets-packages-001 installEffect](#assets-packages-001-installeffect)
- [assets-packages-002 setCaptureFilterByPath](#assets-packages-002-setcapturefilterbypath)
- [assets-packages-003 initData](#assets-packages-003-initdata)
- [assets-packages-004 setCaptureFilterByPath](#assets-packages-004-setcapturefilterbypath)
- [assets-packages-005 initData](#assets-packages-005-initdata)
- [assets-packages-006 setCaptureFilterByPath](#assets-packages-006-setcapturefilterbypath)
- [assets-packages-007 installEffect](#assets-packages-007-installeffect)
- [assets-packages-008 initData](#assets-packages-008-initdata)
- [assets-packages-009 load](#assets-packages-009-load)
- [assets-packages-010 onSuccess](#assets-packages-010-onsuccess)
- [assets-packages-011 onFinishAssetPackageInstallation](#assets-packages-011-onfinishassetpackageinstallation)
- [assets-packages-012 onImageResourceItemClick](#assets-packages-012-onimageresourceitemclick)
- [assets-packages-013 installAssetPackage](#assets-packages-013-installassetpackage)
- [assets-packages-014 getAdjustFilter](#assets-packages-014-getadjustfilter)
- [assets-packages-015 applyFilter](#assets-packages-015-applyfilter)
- [assets-packages-016 onTouch](#assets-packages-016-ontouch)
- [assets-packages-017 getFilterData](#assets-packages-017-getfilterdata)
- [assets-packages-018 onSuccess](#assets-packages-018-onsuccess)
- [assets-packages-019 installAssetPackage](#assets-packages-019-installassetpackage)
- [assets-packages-020 installAssetPackage](#assets-packages-020-installassetpackage)
- [assets-packages-021 installAssetPackagedNoSynchronous](#assets-packages-021-installassetpackagednosynchronous)
<!-- END GENERATED CONTENTS -->

## `assets-packages-001` `installEffect`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/CaptureEffectTabFragment.java:271`

API classes: `NvsAssetPackageManager`
Common calls: `installAssetPackage()`, `sharedInstance()`, `getAssetPackageManager()`, `get()`, `putString()`, `toString()`

Simple sequence:

```java
NvAsset asset = NvAssetManager.sharedInstance().installAssetPackage(
```

## `assets-packages-002` `setCaptureFilterByPath`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/LocalEffectFragment.java:136`

API classes: `NvsAssetPackageManager`
Common calls: `installAssetPackage()`, `sharedInstance()`, `getAssetPackageManager()`

Simple sequence:

```java
NvAsset asset = NvAssetManager.sharedInstance().installAssetPackage(
```

## `assets-packages-003` `initData`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:155`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED`
Common calls: `isEmpty()`, `getInstance()`, `setSelect()`, `equals()`, `toString()`, `setVisibility()`, `post()`, `get()`, `getString()`, `getId()`, `setDownload()`, `split()`

Simple sequence:

```java
mCommonRecyclerViewAdapter.setOnItemClickListener(new CommonRecyclerViewAdapter.
for (EffectInfo info : mData) {
info.setSelect(false);
filterInfo.setSelect(true);
mPackageUrl = filterInfo.getZipUrl();
setCaptureFilterByPath(filterInfo.getId(), effectPath);
mEtSearch.setOnEditorActionListener(new TextView.OnEditorActionListener() {
KeyBoardUtil.hideSoftKeyBroad(mEtSearch, mEtSearch.getContext());
String searchContent = mEtSearch.getText().toString().trim();
mEtSearch.setOnFocusChangeListener(new View.OnFocusChangeListener() {
if (hasFocus) {
mTvCancel.setVisibility(View.VISIBLE);
mTvCancel.setVisibility(View.GONE);
if (TextUtils.isEmpty(searchContent)) {
mEtSearch.setCompoundDrawables(null, null, null, null);
if (searchContentEmpty) {
Drawable drawable = getResources().getDrawable(
drawable.setBounds(0, 0, drawable.getMinimumWidth(),
drawable.getMinimumHeight());
mEtSearch.setCompoundDrawables(null, null, drawable, null);
mTvCancel.setVisibility(View.VISIBLE);
mEtSearch.setOnTouchListener(new View.OnTouchListener() {
mEtSearch.setCursorVisible(true);
Drawable drawable = mEtSearch.getCompoundDrawables()[2];
// ... 33 more SDK-related lines omitted in this compressed snippet ...
```

## `assets-packages-004` `setCaptureFilterByPath`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/SearchEffectTabFragment.java:343`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED`

Simple sequence:

```java
if (packageStatus == NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED) {
```

## `assets-packages-005` `initData`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:130`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED`
Common calls: `getId()`, `getPackageUrl()`, `post()`, `equals()`, `get()`, `isEmpty()`, `setSelect()`, `size()`, `getInstance()`, `valueOf()`, `getAssetPackageManager()`, `installAssetPackage()`

Simple sequence:

```java
mCommonRecyclerViewAdapter.setOnLoadMoreListener(new BaseQuickAdapter.RequestLoadMoreListener() {
mKindInfo.setPageNumber(mKindInfo.getPageNumber() + 1);
mCommonRecyclerViewAdapter.setOnItemClickListener(new CommonLoadMoreAndRefreshAdapter.OnItemClickListener<EffectInfo>() {
for (EffectInfo info : mData) {
info.setSelect(false);
filterInfo.setSelect(true);
String effectPath = NvHttpFilePathUtil.getFilterPathOutOfPathSuffix(filterInfo, NvAsset.ASSET_FILTER);
mKindInfo.setPageNumber(1);
mFilterViewModel.getFilterLiveData().observeForever(new Observer<BaseBean<EffectInfo>>() {
mBinding.setVariable(BR.isLoading, false);
updateFilterInfo(filterInfos.getElements());
String id = effectInfo.getId();
if (!effectInfo1.getId().equals(id)) {
boolean isLoadMore = mKindInfo.getPageNumber() > 1;
for (EffectInfo mDatum : mData) {
mDatum.setSelect(TextUtils.equals(mSelectPackageUrl, mDatum.getPackageUrl()));
mCommonRecyclerViewAdapter.setNewData(new ArrayList<>(mData));
for (EffectInfo effectInfo : dataOrigin) {
if (TextUtils.isEmpty(effectInfo.getPackageUrl())) {
if (effectInfo.getPackageUrl().equals(datum.getPackageUrl())) {
String packageUrl = filterInfo.getZipUrl();
String effectPathDir = PathUtils.getCaptureSDCardPathByType(NvAsset.ASSET_FILTER);
filterInfo.setProgress((int) (progress.fraction * 360));
filterInfo.setDownload(true);
// ... 23 more SDK-related lines omitted in this compressed snippet ...
```

## `assets-packages-006` `setCaptureFilterByPath`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:332`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED`

Simple sequence:

```java
if (packageStatus == NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED) {
```

## `assets-packages-007` `installEffect`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/CaptureFilterTabFragment.java:359`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`
Common calls: `installAssetPackage()`, `getAssetPackageManager()`, `d()`, `get()`, `putString()`, `toString()`

Simple sequence:

```java
String packageId = PackageManagerUtil.installAssetPackage(effectPackageFilePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
```

## `assets-packages-008` `initData`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/fragment/filter/SearchFragment.java:123`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_STATUS_NOTINSTALLED`
Common calls: `getInstance()`, `isEmpty()`, `installAssetPackage()`, `post()`, `setSelect()`, `get()`, `getId()`, `toString()`, `setVisibility()`, `setDownload()`, `getString()`, `getPackageUrl()`

Simple sequence:

```java
mCommonRecyclerViewAdapter.setOnItemClickListener(new CommonRecyclerViewAdapter.
for (EffectInfo info : mData) {
info.setSelect(false);
filterInfo.setSelect(true);
mPackageUrl = filterInfo.getPackageUrl();
mEtSearch.setOnEditorActionListener(new TextView.OnEditorActionListener() {
KeyBoardUtil.hideSoftKeyBroad(mEtSearch, mEtSearch.getContext());
String searchContent = mEtSearch.getText().toString().trim();
mEtSearch.setOnFocusChangeListener(new View.OnFocusChangeListener() {
if (hasFocus) {
mTvCancel.setVisibility(View.VISIBLE);
mTvCancel.setVisibility(View.GONE);
if (TextUtils.isEmpty(searchContent)) {
mEtSearch.setCompoundDrawables(null, null, null, null);
if (searchContentEmpty) {
Drawable drawable = getResources().getDrawable(
drawable.setBounds(0, 0, drawable.getMinimumWidth(),
drawable.getMinimumHeight());
mEtSearch.setCompoundDrawables(null, null, drawable, null);
mTvCancel.setVisibility(View.VISIBLE);
mEtSearch.setOnTouchListener(new View.OnTouchListener() {
mEtSearch.setCursorVisible(true);
Drawable drawable = mEtSearch.getCompoundDrawables()[2];
if (event.getAction() != MotionEvent.ACTION_UP) {
// ... 31 more SDK-related lines omitted in this compressed snippet ...
```

## `assets-packages-009` `load`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/viewmodel/CaptureEffectTabViewModel.java:42`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getAssetType()`, `getAssetPackageManager()`, `getCode()`, `getData()`, `getElements()`, `size()`, `setName()`, `getDisplayName()`, `getFilterPathOutOfPathSuffix()`, `exists()`, `getInstance()`, `getFilterPath()`

Simple sequence:

```java
if (response.getCode() == 1) {
BaseBean<EffectInfo> data = response.getData();
List<EffectInfo> elements = data.getElements();
for (EffectInfo filterInfo : elements) {
filterInfo.setName(filterInfo.getDisplayName());
String effectPath = NvHttpFilePathUtil.getFilterPathOutOfPathSuffix(filterInfo, mCategoryInfo.getAssetType());
if (new File(effectPath).exists()) {
NvsStreamingContext streamingContext = NvsStreamingContext.getInstance();
if ((null != streamingContext) && (null != streamingContext.getAssetPackageManager())) {
String fxPath = NvHttpFilePathUtil.getFilterPath(filterInfo, mCategoryInfo.getAssetType());
int localVersion = streamingContext.getAssetPackageManager().getAssetPackageVersionFromAssetPackageFilePath(fxPath);
int netVersion = filterInfo.getVersion();
filterInfo.setDownload(isDownload);
loadFail(response.getMessage());
```

## `assets-packages-010` `onSuccess`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/viewmodel/CaptureEffectTabViewModel.java:49`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getAssetType()`, `getAssetPackageManager()`, `size()`, `setName()`, `getDisplayName()`, `getFilterPathOutOfPathSuffix()`, `exists()`, `getInstance()`, `getFilterPath()`, `getAssetPackageVersionFromAssetPackageFilePath()`, `getVersion()`, `get()`

Simple sequence:

```java
for (EffectInfo filterInfo : elements) {
filterInfo.setName(filterInfo.getDisplayName());
String effectPath = NvHttpFilePathUtil.getFilterPathOutOfPathSuffix(filterInfo, mCategoryInfo.getAssetType());
if (new File(effectPath).exists()) {
NvsStreamingContext streamingContext = NvsStreamingContext.getInstance();
if ((null != streamingContext) && (null != streamingContext.getAssetPackageManager())) {
String fxPath = NvHttpFilePathUtil.getFilterPath(filterInfo, mCategoryInfo.getAssetType());
int localVersion = streamingContext.getAssetPackageManager().getAssetPackageVersionFromAssetPackageFilePath(fxPath);
int netVersion = filterInfo.getVersion();
filterInfo.setDownload(isDownload);
```

## `assets-packages-011` `onFinishAssetPackageInstallation`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:457`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR`
Common calls: `applyCaptureScene()`

Simple sequence:

```java
if (error == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR) {
mStreamingContext.applyCaptureScene(assetPackageId);
```

## `assets-packages-012` `onImageResourceItemClick`

Source: `app/src/main/java/com/meishe/sdkdemo/capturescene/CaptureSceneActivity.java:469`

API classes: `NvsCaptureSceneInfo`
Static/constants: `NvsCaptureSceneInfo.ClipData`, `NvsCaptureSceneInfo.CAPTURESCENE_INFO_IMAGE_FILLMODE_CROP`
Common calls: `isEmpty()`, `installAssetPackage()`, `ClipData()`, `add()`, `applyCaptureScene()`

Simple sequence:

```java
NvAsset asset = mAssetManager.installAssetPackage(Constants.BG_SEGMENT_CAPTURE_SCENE_PATH, NvAsset.ASSET_CAPTURE_SCENE, false);
NvsCaptureSceneInfo sceneInfo = new NvsCaptureSceneInfo();
List<NvsCaptureSceneInfo.ClipData> clipDataList = new ArrayList<>();
NvsCaptureSceneInfo.ClipData clipData = new NvsCaptureSceneInfo.ClipData();
clipData.imageFillMode = NvsCaptureSceneInfo.CAPTURESCENE_INFO_IMAGE_FILLMODE_CROP;
mStreamingContext.applyCaptureScene(mBgSegPackageId, sceneInfo);
```

## `assets-packages-013` `installAssetPackage`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:920`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`
Common calls: `installAssetPackage()`

Simple sequence:

```java
return PackageManagerUtil.installAssetPackage(filterPackageFilePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
```

## `assets-packages-014` `getAdjustFilter`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/BaseFilterActivity.java:487`

API classes: `NvsExpressionParam`, `NvsAssetPackageManager`, `NvsColor`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsExpressionParam.TYPE_COLOR`, `NvsExpressionParam.TYPE_FLOAT`, `NvsExpressionParam.FloatParam`, `NvsExpressionParam.TYPE_INT`, `NvsExpressionParam.IntParam`, `NvsExpressionParam.TYPE_BOOLEAN`
Common calls: `getDefVal()`, `isEmpty()`, `getAssetPackageManager()`, `setDefVal()`, `setMaxVal()`, `getMaxVal()`, `setMinVal()`, `getMinVal()`, `setStrength()`, `putFilterParam()`, `getKey()`, `getStrength()`

Simple sequence:

```java
List<NvsExpressionParam> expValueList = mStreamingContext.getAssetPackageManager().getExpValueList(packageId,
NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
Hashtable<String, String> hashtable = mStreamingContext.getAssetPackageManager().getTranslationMap(packageId,
NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
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
case NvsExpressionParam.TYPE_FLOAT:
NvsExpressionParam.FloatParam floatParam = nvsExpressionParam.getFloatParam();
if (null != floatParam) {
adjustSpecialEffectsInfo.setDefVal(floatParam.getDefVal());
adjustSpecialEffectsInfo.setMaxVal(floatParam.getMaxVal());
adjustSpecialEffectsInfo.setMinVal(floatParam.getMinVal());
adjustSpecialEffectsInfo.setStrength(floatParam.getDefVal());
if (mVideoClipFxInfo != null) {
// ... 15 more SDK-related lines omitted in this compressed snippet ...
```

## `assets-packages-015` `applyFilter`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterActivity.java:246`

API classes: `NvsAssetPackageManager`, `NvsStreamingContext`, `NvsExpressionParam`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `isEmpty()`, `setVisibility()`, `setIntensityLayoutVisible()`, `setIntensitySeekBarVisibility()`, `setIntensitySeekBarProgress()`, `getAssetPackageManager()`, `get()`, `applyFilterByTimeline()`, `getStreamingEngineState()`, `playVideoButtonClick()`, `getPackageId()`, `getExpValueList()`

Simple sequence:

```java
TimelineUtil.applyFilterByTimeline(mTimeline, mFilterItem);
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
String packageId = mFilterItem.getPackageId();
if (TextUtils.isEmpty(packageId)) {
mAdjustView.setVisibility(View.GONE);
mFilterView.setIntensityLayoutVisible(View.VISIBLE);
mFilterView.setIntensitySeekBarVisibility(View.VISIBLE);
mFilterView.setIntensitySeekBarProgress(100);
List<NvsExpressionParam> expValueList = mStreamingContext.getAssetPackageManager().getExpValueList(packageId,
NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
Hashtable<String, String> hashtable = mStreamingContext.getAssetPackageManager().getTranslationMap(packageId,
NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
if ((null == expValueList) || (null == hashtable) || expValueList.isEmpty() || hashtable.isEmpty()) {
mAdjustView.setVisibility(View.GONE);
mFilterView.setIntensityLayoutVisible(View.VISIBLE);
mFilterView.setIntensitySeekBarVisibility(View.VISIBLE);
mFilterView.setIntensitySeekBarProgress(100);
mAdjustView.setVisibility(View.VISIBLE);
mFilterView.setIntensityLayoutVisible(View.INVISIBLE);
mAdjustView.setData(mPresenter.setAdjustFilter(packageId, expValueList, hashtable, mFilterItem));
```

## `assets-packages-016` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:496`

API classes: `NvsAssetPackageParticleDescParser`, `NvsParticleSystemContext`
Common calls: `get()`, `getTimelineCurrentPosition()`, `i()`, `isEmpty()`, `getCurrentTimeMS()`, `size()`, `mapViewToCanonical()`, `mapPointFromCanonicalToParticleSystem()`, `getParticleSystemContext()`, `appendPositionToEmitterPositionCurve()`, `getAction()`, `addPackagedTimelineVideoFx()`

Simple sequence:

```java
switch (motionEvent.getAction()) {
mSeekBegin = mStreamingContext.getTimelineCurrentPosition(mTimeline);
if (mCurrentParticleFxId != null && !mCurrentParticleFxId.isEmpty() && mStreamingContext != null) {
mMoveSystemBegin = TimeFormatUtil.getCurrentTimeMS();
mMoveBegin = mStreamingContext.getTimelineCurrentPosition(mTimeline);
mCurrentVideoFx = mTimeline.addPackagedTimelineVideoFx(mMoveBegin, mTimeline.getDuration(), mCurrentParticleFxId);
if (null != mCurrentVideoFx) {
mCurrentVideoFx.setFloatVal("Tail Fading Duration", 0.5); // 拖尾效果的时长（s） Length of trailing effect (s)
String assetDescription = mParticleFxList.get(mCurrentParticlePos).getAsset().assetDescription;
NvsAssetPackageParticleDescParser parser = new NvsAssetPackageParticleDescParser(assetDescription);
PointF nowPointF = mLiveWindow.mapViewToCanonical(new PointF(mCurrentX, mCurrentY));
if (mCurrentEmitterList != null) {
NvsParticleSystemContext particleContext = mCurrentVideoFx.getParticleSystemContext();
particleContext.setEmitterRateGain(mCurrentEmitterList.get(i), mParticleRateValue);
particleContext.setEmitterParticleSizeGain(mCurrentEmitterList.get(i), mParticleSizeValue);
long cur_ms_system = TimeFormatUtil.getCurrentTimeMS();
long cur_us_timeline = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long cur_ms_system = TimeFormatUtil.getCurrentTimeMS();
PointF nowPointF = mLiveWindow.mapViewToCanonical(new PointF(mCurrentX, mCurrentY));
NvsParticleSystemContext particleContext = mCurrentVideoFx.getParticleSystemContext();
if (mCurrentParticleFxId != null && !mCurrentParticleFxId.isEmpty() && mCurrentVideoFx != null) {
mCurrentVideoFx.changeOutPoint(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `assets-packages-017` `getFilterData`

Source: `app/src/main/java/com/meishe/sdkdemo/repository/AppRepository.java:60`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `setValue()`, `valueOf()`, `getMaterialType()`, `getData()`, `setDefaultStrength()`, `getAssetPackageManager()`, `get()`, `getCategory()`, `getId()`, `getMaterialList()`, `getSdkVersion()`, `getPageNumber()`

Simple sequence:

```java
if (filterInfos != null) {
liveData.setValue(filterInfos);
final int category = kindInfo.getCategory();
final int kindInfoId = kindInfo.getId();
HttpManager.getMaterialList(null, String.valueOf(kindInfo.getMaterialType()),
String.valueOf(kindInfoId), "", MSApplication.getSdkVersion(),
kindInfo.getPageNumber(), Constants.PAGE_SIZE, new RequestCallback<BaseBean<EffectInfo>>() {
if (response.getCode() == 1) {
List<EffectInfo> elements = response.getData().getElements();
for (EffectInfo filterInfo : elements) {
filterInfo.setName(filterInfo.getDisplayName());
filterInfo.setDefaultStrength(1);
filterInfo.setDefaultStrength(0.8F);
String effectPath = HttpFilePathUtil.getFilterPathOutOfPathSuffix(filterInfo, kindInfo.getMaterialType());
if (new File(effectPath).exists()) {
NvsStreamingContext streamingContext = NvsStreamingContext.getInstance();
if ((null != streamingContext) && (null != streamingContext.getAssetPackageManager())) {
String fxPath = HttpFilePathUtil.getFilterPath(filterInfo, kindInfo.getMaterialType());
int localVersion = streamingContext.getAssetPackageManager().getAssetPackageVersionFromAssetPackageFilePath(fxPath);
int netVersion = filterInfo.getVersion();
filterInfo.setDownload(isDownload);
cacheMap.put(cacheKey, response.getData());
liveData.setValue(response.getData());
liveData.setValue(null);
```

## `assets-packages-018` `onSuccess`

Source: `app/src/main/java/com/meishe/sdkdemo/repository/AppRepository.java:83`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `setDefaultStrength()`, `getMaterialType()`, `getAssetPackageManager()`, `setName()`, `getDisplayName()`, `getFilterPathOutOfPathSuffix()`, `exists()`, `getInstance()`, `getFilterPath()`, `getAssetPackageVersionFromAssetPackageFilePath()`, `getVersion()`, `setDownload()`

Simple sequence:

```java
for (EffectInfo filterInfo : elements) {
filterInfo.setName(filterInfo.getDisplayName());
filterInfo.setDefaultStrength(1);
filterInfo.setDefaultStrength(0.8F);
String effectPath = HttpFilePathUtil.getFilterPathOutOfPathSuffix(filterInfo, kindInfo.getMaterialType());
if (new File(effectPath).exists()) {
NvsStreamingContext streamingContext = NvsStreamingContext.getInstance();
if ((null != streamingContext) && (null != streamingContext.getAssetPackageManager())) {
String fxPath = HttpFilePathUtil.getFilterPath(filterInfo, kindInfo.getMaterialType());
int localVersion = streamingContext.getAssetPackageManager().getAssetPackageVersionFromAssetPackageFilePath(fxPath);
int netVersion = filterInfo.getVersion();
filterInfo.setDownload(isDownload);
```

## `assets-packages-019` `installAssetPackage`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:816`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`
Common calls: `endsWith()`

Simple sequence:

```java
if (filterPackageFilePath.endsWith(".videofx")) {
type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
```

## `assets-packages-020` `installAssetPackage`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/asset/NvAssetManager.java:933`

API classes: `NvsAssetPackageManager`
Common calls: `isEmpty()`, `getPackageType()`, `getSDCardPathByType()`, `isZipFile()`, `unZipFile()`, `getAssetVersionWithPath()`, `substring()`, `lastIndexOf()`, `split()`, `getAssetPackageManager()`, `installAssetPackage()`, `getAssetPackageVersion()`

Simple sequence:

```java
NvsAssetPackageManager manager = streamingContext.getAssetPackageManager();
if (assetType == NvAsset.ASSET_FACE1_STICKER) {
String destPath = PathUtils.getSDCardPathByType(NvAsset.ASSET_FACE1_STICKER);
asset.version = PathUtils.getAssetVersionWithPath(filePath);
String destPath = PathUtils.getSDCardPathByType(NvAsset.ASSET_SUPER_ZOOM);
asset.version = PathUtils.getAssetVersionWithPath(filePath);
String packageId = PackageManagerUtil.installAssetPackage(filePath, null, asset.getPackageType());
asset.version = manager.getAssetPackageVersion(asset.uuid, asset.getPackageType());
asset.aspectRatio = manager.getAssetPackageSupportedAspectRatio(asset.uuid, asset.getPackageType());
if (asset.assetType == NvAsset.ASSET_PARTICLE) {
asset.assetDescription = manager.getVideoFxAssetPackageDescription(packageId);
```

## `assets-packages-021` `installAssetPackagedNoSynchronous`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:636`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.AssetPackageManagerCallback`, `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR`, `NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED`
Common calls: `e()`, `getAssetPackageManager()`, `installAssetPackageAsynchronous()`, `getAssetPackageStatus()`, `installAssetPackage()`, `onFinishAssetPackageInstallation()`, `toString()`

Simple sequence:

```java
public void installAssetPackagedNoSynchronous(String path, int type, StringBuilder stringBuilder, NvsAssetPackageManager.AssetPackageManagerCallback callback) {
if (mStreamingContext == null) {
Log.e(TAG, "installAssetPackaged: mStreamingContext is null!");
```
