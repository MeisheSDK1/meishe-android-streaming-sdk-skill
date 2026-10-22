# Demo Simple Snippets - Rare And Structural

This reference completes method-level simple snippets with low-frequency, nested, field-level, callback, and structural SDK usages found in the demo.
Use it when a class/constant is missing from normal snippet groups or when working with rare APIs such as caption span subclasses, AR callbacks, watermark constants, `NvsTrackCaption`, `NvsPanAndScan`, or Effect SDK object types.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [Coverage Focus](#coverage-focus)
- [rare-structural-001 NvsAIContext](#rare-structural-001-nvsaicontext)
- [rare-structural-002 NvsARSceneManipulateCallback](#rare-structural-002-nvsarscenemanipulatecallback)
- [rare-structural-003 NvsCaptureAudioFx](#rare-structural-003-nvscaptureaudiofx)
- [rare-structural-004 NvsClipCompoundCaption](#rare-structural-004-nvsclipcompoundcaption)
- [rare-structural-005 NvsCompoundCaption](#rare-structural-005-nvscompoundcaption)
- [rare-structural-006 NvsEffect](#rare-structural-006-nvseffect)
- [rare-structural-007 NvsEffectRenderCore](#rare-structural-007-nvseffectrendercore)
- [rare-structural-008 NvsFaceBoundingRectInfo](#rare-structural-008-nvsfaceboundingrectinfo)
- [rare-structural-009 NvsFaceData](#rare-structural-009-nvsfacedata)
- [rare-structural-010 NvsFaceFeatureInfo](#rare-structural-010-nvsfacefeatureinfo)
- [rare-structural-011 NvsHandFeatureInfo](#rare-structural-011-nvshandfeatureinfo)
- [rare-structural-012 NvsItalicSpan](#rare-structural-012-nvsitalicspan)
- [rare-structural-013 NvsMakeupEffectInfo](#rare-structural-013-nvsmakeupeffectinfo)
- [rare-structural-014 NvsObject](#rare-structural-014-nvsobject)
- [rare-structural-015 NvsPanAndScan](#rare-structural-015-nvspanandscan)
- [rare-structural-016 NvsParticleSystemContext](#rare-structural-016-nvsparticlesystemcontext)
- [rare-structural-017 NvsPassthroughFileInfo](#rare-structural-017-nvspassthroughfileinfo)
- [rare-structural-018 NvsRendererIdSpan](#rare-structural-018-nvsrendereridspan)
- [rare-structural-019 NvsTemplateCompoundCaptionItemDesc](#rare-structural-019-nvstemplatecompoundcaptionitemdesc)
- [rare-structural-020 NvsTimelineWatermarkPosition_TopLeft](#rare-structural-020-nvstimelinewatermarkposition_topleft)
- [rare-structural-021 NvsTimelineWatermarkPosition_TopRight](#rare-structural-021-nvstimelinewatermarkposition_topright)
- [rare-structural-022 NvsTrackCaption](#rare-structural-022-nvstrackcaption)
- [rare-structural-023 NvsUnderlineSpan](#rare-structural-023-nvsunderlinespan)
- [rare-structural-024 NvsVideoEffect](#rare-structural-024-nvsvideoeffect)
- [rare-structural-025 NvsVideoEffectAnimatedSticker](#rare-structural-025-nvsvideoeffectanimatedsticker)
- [rare-structural-026 NvsVideoEffectCompoundCaption](#rare-structural-026-nvsvideoeffectcompoundcaption)
- [rare-structural-027 NvsVideoFrameInfo](#rare-structural-027-nvsvideoframeinfo)
- [rare-structural-028 NvsVolume](#rare-structural-028-nvsvolume)
- [rare-structural-029 NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO](#rare-structural-029-nvsstreamingcontextstreaming_engine_capture_flag_dont_capture_audio)
- [rare-structural-030 NvsAssetPackageManager template aspect ratio constants](#rare-structural-030-nvsassetpackagemanager-template-aspect-ratio-constants)
- [rare-structural-031 NvsAssetPackageManager template footage type constants](#rare-structural-031-nvsassetpackagemanager-template-footage-type-constants)
<!-- END GENERATED CONTENTS -->

## Coverage Focus

- Missing tokens from baseline simple snippets: 11
- Rare SDK tokens with three or fewer code-line occurrences: 24

| Token | Reason | Source examples |
| --- | --- | --- |
| `NvsAIContext` | rare | `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:166`<br>`app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:292`<br>`app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:295` |
| `NvsARSceneManipulateCallback` | missing from baseline snippets, rare | `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:108` |
| `NvsCaptureAudioFx` | missing from baseline snippets, rare | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:257` |
| `NvsClipCompoundCaption` | rare | `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1048`<br>`libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1108` |
| `NvsCompoundCaption` | rare | `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:33`<br>`libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:89`<br>`libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:93` |
| `NvsEffect` | rare | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3263`<br>`app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3429`<br>`app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3435` |
| `NvsEffectRenderCore` | rare | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:344`<br>`app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3427`<br>`app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3428` |
| `NvsFaceBoundingRectInfo` | missing from baseline snippets, rare | `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:110` |
| `NvsFaceData` | rare | `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1439`<br>`app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1443` |
| `NvsFaceFeatureInfo` | rare | `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:116`<br>`app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:121` |
| `NvsHandFeatureInfo` | rare | `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:160` |
| `NvsItalicSpan` | missing from baseline snippets | `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3665`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5051`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5052`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5134` |
| `NvsMakeupEffectInfo` | rare | `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:111`<br>`MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:146` |
| `NvsObject` | missing from baseline snippets | `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1208`<br>`libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1244`<br>`libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1440`<br>`libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1452` |
| `NvsPanAndScan` | missing from baseline snippets, rare | `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:250` |
| `NvsParticleSystemContext` | rare | `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:175`<br>`app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:532`<br>`app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:565` |
| `NvsPassthroughFileInfo` | rare | `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:102`<br>`app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:103` |
| `NvsRendererIdSpan` | missing from baseline snippets | `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2346`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2347`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5055`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5056` |
| `NvsTemplateCompoundCaptionItemDesc` | rare | `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:157`<br>`libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:316` |
| `NvsTimelineWatermarkPosition_TopLeft` | rare | `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:305` |
| `NvsTimelineWatermarkPosition_TopRight` | missing from baseline snippets, rare | `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java:34` |
| `NvsTrackCaption` | missing from baseline snippets, rare | `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1461` |
| `NvsUnderlineSpan` | missing from baseline snippets | `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3738`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5053`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5054`<br>`app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5136` |
| `NvsVideoEffect` | rare | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3270`<br>`app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3358` |
| `NvsVideoEffectAnimatedSticker` | missing from baseline snippets, rare | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3408` |
| `NvsVideoEffectCompoundCaption` | rare | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3369` |
| `NvsVideoFrameInfo` | rare | `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3248`<br>`app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3431` |
| `NvsVolume` | rare | `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:233` |

## `rare-structural-001` `NvsAIContext`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:166`

```java
164: private FloatBuffer mDrawTextureBuffer;
165: private FloatBuffer mDrawGLCubeBuffer;
166: private NvsAIContext mAISdkContext;
167: private NvsVideoResolution mCurrentVideoResolution;
168: private NvsFaceDetector mNvsFaceDetector;
169: private NvSuperZoom mNvSuperZoom;
```

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:292`

```java
290: @Override
291: protected void initViews() {
292: mAISdkContext = NvsAIContext.getInstance();
293: if (mAISdkContext == null) {
294: String licensePath = "assets:/meishesdk.lic";
295: mAISdkContext = NvsAIContext.init(getApplicationContext(), licensePath, 0);
```

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:295`

```java
293: if (mAISdkContext == null) {
294: String licensePath = "assets:/meishesdk.lic";
295: mAISdkContext = NvsAIContext.init(getApplicationContext(), licensePath, 0);
296: }
298: String className = "facemode/ms";
```


## `rare-structural-002` `NvsARSceneManipulateCallback`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:108`

```java
106: StringBuilder leftValue = new StringBuilder();
107: StringBuilder rightValue = new StringBuilder();
108: manipulate.setARSceneCallback(new NvsARSceneManipulate.NvsARSceneManipulateCallback() {
109: @Override
110: public void notifyFaceBoundingRect(List<NvsARSceneManipulate.NvsFaceBoundingRectInfo> list) {
```


## `rare-structural-003` `NvsCaptureAudioFx`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:257`

```java
255: private TopMoreDialog mMoreDialog;
257: private NvsCaptureAudioFx mNoiseAudioFx;
258: private AudioNoisePop mAudioNoisePop;
260: private VoicePop mVoicePop;
```


## `rare-structural-004` `NvsClipCompoundCaption`

Reason: rare SDK usage

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1048`

```java
1046: clipCaption = clipByIndex.getNextCaption(clipCaption);
1047: }
1048: NvsClipCompoundCaption clipCompoundCaption = clipByIndex.getFirstCompoundCaption();
1049: while (null != clipCompoundCaption) {
1050: int captionCount = clipCompoundCaption.getCaptionCount();
1051: for (int j = 0; j < captionCount; j++) {
```

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1108`

```java
1106: break;
1107: }
1108: NvsClipCompoundCaption clipCompoundCaption = clipByIndex.getFirstCompoundCaption();
1109: if (null != clipCompoundCaption) {
1110: hasClipCaption = true;
1111: break;
```


## `rare-structural-005` `NvsCompoundCaption`

Reason: rare SDK usage

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:33`

```java
31: */
32: private NvsCaption nvsCaption;
33: private NvsCompoundCaption nvsCompoundCaption;
34: private int captionType;
35: /**
36: * 如果是组合字幕，拆分成多个子字幕对象，保存子字幕的index
```

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:89`

```java
87: }
89: public void setNvsCompoundCaption(NvsCompoundCaption nvsCompoundCaption) {
90: this.nvsCompoundCaption = nvsCompoundCaption;
91: }
```

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:93`

```java
91: }
93: public NvsCompoundCaption getNvsCompoundCaption() {
94: return nvsCompoundCaption;
95: }
```


## `rare-structural-006` `NvsEffect`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3263`

```java
3261: int captureVideoFxCount = mStreamingContext.getCaptureVideoFxCount();
3263: List<NvsEffect> effects = new ArrayList<>();
3264: NvsRational nvsRational = new NvsRational(9, 16);
3266: for (int i = 0; i < captureVideoFxCount; i++) {
```

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3429`

```java
3427: mEffectRenderCore.initialize(NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K |
3428: NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED);
3429: ByteBuffer byteBufferResult = mEffectRenderCore.renderEffects(effects.toArray(new NvsEffect[effects.size()]),
3430: byteBuffer.array(), nvsVideoFrameInfo, 0,
3431: NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA, false,
3432: (System.currentTimeMillis() - mStartPreviewTime) * 1000, 0);
```

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3435`

```java
3434: for (int i = 0; i < effects.size(); i++) {
3435: NvsEffect nvsEffect = effects.get(i);
3436: mEffectRenderCore.clearEffectResources(nvsEffect);
3437: nvsEffect = null;
3438: }
```


## `rare-structural-007` `NvsEffectRenderCore`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:344`

```java
342: private TypeAndCategoryInfo mStickerTypeInfo;
344: private NvsEffectRenderCore mEffectRenderCore;
345: /**
346: * 开始预览时间
347: * Start preview time
```

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3427`

```java
3425: nvsVideoFrameInfo.frameHeight, Bitmap.Config.ARGB_8888);
3426: if (effects.size() > 0) {
3427: mEffectRenderCore.initialize(NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K |
3428: NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED);
3429: ByteBuffer byteBufferResult = mEffectRenderCore.renderEffects(effects.toArray(new NvsEffect[effects.size()]),
3430: byteBuffer.array(), nvsVideoFrameInfo, 0,
```

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3428`

```java
3426: if (effects.size() > 0) {
3427: mEffectRenderCore.initialize(NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_SUPPORT_8K |
3428: NvsEffectRenderCore.NV_EFFECT_CORE_FLAGS_CREATE_GLCONTEXT_IF_NEED);
3429: ByteBuffer byteBufferResult = mEffectRenderCore.renderEffects(effects.toArray(new NvsEffect[effects.size()]),
3430: byteBuffer.array(), nvsVideoFrameInfo, 0,
3431: NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA, false,
```


## `rare-structural-008` `NvsFaceBoundingRectInfo`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:110`

```java
108: manipulate.setARSceneCallback(new NvsARSceneManipulate.NvsARSceneManipulateCallback() {
109: @Override
110: public void notifyFaceBoundingRect(List<NvsARSceneManipulate.NvsFaceBoundingRectInfo> list) {
112: }
```


## `rare-structural-009` `NvsFaceData`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1439`

```java
1437: return;
1438: }
1439: List<NvsFaceDetector.NvsFaceData> faceDataList = mNvsFaceDetector.detectBuffer(
1440: data, width, height, NvsFaceDetector.AI_SDK_DETECTION_BUFFER_FORMAT_RGBA, mDetectOrientation, 0);
1441: mHumanInfos.clear();
1442: if (!CommonUtils.isEmpty(faceDataList)) {
```

Source: `app/src/main/java/com/meishe/sdkdemo/superzoom/SuperZoomActivity.java:1443`

```java
1441: mHumanInfos.clear();
1442: if (!CommonUtils.isEmpty(faceDataList)) {
1443: for (NvsFaceDetector.NvsFaceData faceData : faceDataList) {
1444: if (faceData == null) {
1445: continue;
1446: }
```


## `rare-structural-010` `NvsFaceFeatureInfo`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:116`

```java
114: @SuppressLint({"NotifyDataSetChanged", "DefaultLocale"})
115: @Override
116: public void notifyFaceFeatureInfos(List<NvsARSceneManipulate.NvsFaceFeatureInfo> list) {
117: textLeftValue.post(() -> {
118: if (list.isEmpty()) {
119: return;
```

Source: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:121`

```java
119: return;
120: }
121: NvsARSceneManipulate.NvsFaceFeatureInfo info = list.get(0);
122: if (null == info) {
123: return;
124: }
```


## `rare-structural-011` `NvsHandFeatureInfo`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/view/FaceAvatarView.java:160`

```java
159: @Override
160: public void notifyHandFeatureInfos(List<NvsARSceneManipulate.NvsHandFeatureInfo> list) {
162: }
163: });
```


## `rare-structural-012` `NvsItalicSpan`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3665`

```java
3663: if (checkPosition()) {
3664: List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
3665: NvsItalicSpan nvsItalicSpan = new NvsItalicSpan(mSelectionStart, mSelectionEnd);
3666: setSpanList(nvsItalicSpan, mIsItalic, textSpanList, captionInfo);
3667: } else {
3668: changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_ITALIC,
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5051`

```java
5049: } else if (nvsCaptionSpan instanceof NvsOpacitySpan) {
5050: ((NvsOpacitySpan) nvsCaptionSpan).setOpacity((Float) object);
5051: } else if (nvsCaptionSpan instanceof NvsItalicSpan) {
5052: ((NvsItalicSpan) nvsCaptionSpan).setItalic((Boolean) object);
5053: } else if (nvsCaptionSpan instanceof NvsUnderlineSpan) {
5054: ((NvsUnderlineSpan) nvsCaptionSpan).setUnderline((Boolean) object);
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5052`

```java
5050: ((NvsOpacitySpan) nvsCaptionSpan).setOpacity((Float) object);
5051: } else if (nvsCaptionSpan instanceof NvsItalicSpan) {
5052: ((NvsItalicSpan) nvsCaptionSpan).setItalic((Boolean) object);
5053: } else if (nvsCaptionSpan instanceof NvsUnderlineSpan) {
5054: ((NvsUnderlineSpan) nvsCaptionSpan).setUnderline((Boolean) object);
5055: } else if (nvsCaptionSpan instanceof NvsRendererIdSpan) {
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5134`

```java
5132: } else if (nvsCaptionSpan instanceof NvsOpacitySpan) {
5133: return ((NvsOpacitySpan) nvsCaptionSpan).getOpacity();
5134: } else if (nvsCaptionSpan instanceof NvsItalicSpan) {
5135: return ((NvsItalicSpan) nvsCaptionSpan).isItalic();
5136: } else if (nvsCaptionSpan instanceof NvsUnderlineSpan) {
5137: return ((NvsUnderlineSpan) nvsCaptionSpan).isUnderline();
```


## `rare-structural-013` `NvsMakeupEffectInfo`

Reason: rare SDK usage

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:111`

```java
109: // 是否设置单buffer模式 Whether to set single buffer mode
110: mArSceneFx.setBooleanVal(SINGLE_BUFFER_MODE, mIsSingleBufferMode);
111: enableCaptureMakeupFlag(NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
112: Utils.setAIFaceOcclusion(mArSceneFx);
113: }
114: }
```

Source: `MMakeup/src/main/java/com/meishe/makeup/MakeupHelper.java:146`

```java
144: videoFx.getARSceneManipulate().setDetectionMode(NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
145: }
146: enableMakeupFlag(videoFx, NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
147: Utils.setAIFaceOcclusion(videoFx);
148: }
149: }
```


## `rare-structural-014` `NvsObject`

Reason: missing from baseline snippets

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1208`

```java
1206: if (videoClip != null) {
1207: if (videoClip.getInternalTimeline() == null) {
1208: String bestSeekTime = videoClip.getTemplateAttachment(NvsObject.TEMPLATE_KEY_BEST_SEEK_TIME);
1209: if (TextUtils.isEmpty(bestSeekTime)) {
1210: bestSeekTime = "0";
1211: }
```

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1244`

```java
1242: private static NvsTimelineCaption loadTimelineCaptionToTemplate(NvsTimeline timeline, NvsTimelineCaption caption, String replaceId) {
1243: if (caption != null) {
1244: String id = caption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID);
1245: if (TextUtils.equals(id, replaceId)) {
1246: return caption;
1247: }
```

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1440`

```java
1438: NvsTimelineCaption meicamCaptionClip = loadTimelineCaptionToTemplate(meicamTimeline, firstCaption, templateCaptionDesc.replaceId);
1439: if (meicamCaptionClip != null) {
1440: long bestSeekTime = Long.parseLong(meicamCaptionClip.getTemplateAttachment(NvsObject.TEMPLATE_KEY_BEST_SEEK_TIME));
1441: if (bestSeekTime < 0) {
1442: templateCaptionDesc.setInPoint(clipInPoint + meicamCaptionClip.getInPoint() +
1443: (meicamCaptionClip.getOutPoint() - meicamCaptionClip.getInPoint()) / 2);
```

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1452`

```java
1450: }
1451: if (meicamCaptionClip != null) {
1452: String groupID = meicamCaptionClip.getTemplateAttachment(NvsObject.TEMPLATE_KEY_FX_GROUP);
1453: if (!TextUtils.isEmpty(groupID)) {
1454: templateCaptionDesc.setGroupID(groupID);
1455: }
```


## `rare-structural-015` `NvsPanAndScan`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/adjust/AdjustActivity.java:250`

```java
248: mVideoFragment.getRectViewSize(), transFromData);
250: NvsPanAndScan panAndScan = mVideoClip.getPanAndScan();
251: clipInfo.setPan(panAndScan.pan);
252: clipInfo.setScan(panAndScan.scan);
253: mCutData.setTransformData(transFromData);
```


## `rare-structural-016` `NvsParticleSystemContext`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:175`

```java
173: if (mCurrentEmitter >= mCurrentEmitterList.size())
174: mCurrentEmitter = 0;
175: NvsParticleSystemContext particleContext = mCurrentVideoFx.getParticleSystemContext();
176: PointF particlePointF = mCurrentVideoFx.mapPointFromCanonicalToParticleSystem(nowPointF);
177: for (int i = 0; i < mCurrentEmitterList.size(); ++i) {
178: String emitterName = mCurrentEmitterList.get(i);
```

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:532`

```java
530: Log.i(TAG, "particle x: " + particlePointF.x + " new y: " + particlePointF.y);
531: if (mCurrentEmitterList != null) {
532: NvsParticleSystemContext particleContext = mCurrentVideoFx.getParticleSystemContext();
533: for (int i = 0; i < mCurrentEmitterList.size(); i++) {
534: particleContext.appendPositionToEmitterPositionCurve(mCurrentEmitterList.get(i), 0, particlePointF.x, particlePointF.y);
535: particleContext.setEmitterRateGain(mCurrentEmitterList.get(i), mParticleRateValue);
```

Source: `app/src/main/java/com/meishe/sdkdemo/particle/ParticleEditActivity.java:565`

```java
563: if (mCurrentParticleFxId != null && !mCurrentParticleFxId.isEmpty() && mCurrentVideoFx != null && mCurrentEmitterList != null && mCurrentEmitterList.size() > 0) {
564: PointF particlePointF = mCurrentVideoFx.mapPointFromCanonicalToParticleSystem(nowPointF);
565: NvsParticleSystemContext particleContext = mCurrentVideoFx.getParticleSystemContext();
566: for (int i = 0; i < mCurrentEmitterList.size(); ++i) {
567: String emitterName = mCurrentEmitterList.get(i);
568: particleContext.appendPositionToEmitterPositionCurve(emitterName, (float) (cur_us_timeline + time_each_seek - mMoveBegin) / 1000000, particlePointF.x, particlePointF.y);
```


## `rare-structural-017` `NvsPassthroughFileInfo`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:102`

```java
100: mStreamingContext.stop();
101: NvsPassthroughConvertor nvsPassthroughConvertor = new NvsPassthroughConvertor();
102: List<NvsPassthroughConvertor.NvsPassthroughFileInfo> passthroughFileInfos = new ArrayList<>();
103: NvsPassthroughConvertor.NvsPassthroughFileInfo fileInfo = new NvsPassthroughConvertor.NvsPassthroughFileInfo();
104: fileInfo.filePath = mClipInfo.getFilePath();
105: fileInfo.trimIn = mClipInfo.getTrimIn();
```

Source: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:103`

```java
101: NvsPassthroughConvertor nvsPassthroughConvertor = new NvsPassthroughConvertor();
102: List<NvsPassthroughConvertor.NvsPassthroughFileInfo> passthroughFileInfos = new ArrayList<>();
103: NvsPassthroughConvertor.NvsPassthroughFileInfo fileInfo = new NvsPassthroughConvertor.NvsPassthroughFileInfo();
104: fileInfo.filePath = mClipInfo.getFilePath();
105: fileInfo.trimIn = mClipInfo.getTrimIn();
106: fileInfo.trimOut = mClipInfo.getTrimOut();
```


## `rare-structural-018` `NvsRendererIdSpan`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2346`

```java
2345: List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
2346: NvsRendererIdSpan nvsRendererIdSpan =
2347: new NvsRendererIdSpan(mSelectionStart, mSelectionEnd);
2348: setSpanList(nvsRendererIdSpan, mRichWordList.get(pos).getAsset().uuid, textSpanList,
2349: captionInfo);
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2347`

```java
2345: List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
2346: NvsRendererIdSpan nvsRendererIdSpan =
2347: new NvsRendererIdSpan(mSelectionStart, mSelectionEnd);
2348: setSpanList(nvsRendererIdSpan, mRichWordList.get(pos).getAsset().uuid, textSpanList,
2349: captionInfo);
2350: }
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5055`

```java
5053: } else if (nvsCaptionSpan instanceof NvsUnderlineSpan) {
5054: ((NvsUnderlineSpan) nvsCaptionSpan).setUnderline((Boolean) object);
5055: } else if (nvsCaptionSpan instanceof NvsRendererIdSpan) {
5056: ((NvsRendererIdSpan) nvsCaptionSpan).setRendererId((String) object);
5057: } else if (nvsCaptionSpan instanceof NvsOutlineColorSpan) {
5058: if (object == null) {
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5056`

```java
5054: ((NvsUnderlineSpan) nvsCaptionSpan).setUnderline((Boolean) object);
5055: } else if (nvsCaptionSpan instanceof NvsRendererIdSpan) {
5056: ((NvsRendererIdSpan) nvsCaptionSpan).setRendererId((String) object);
5057: } else if (nvsCaptionSpan instanceof NvsOutlineColorSpan) {
5058: if (object == null) {
5059: ((NvsOutlineColorSpan) nvsCaptionSpan).setOutlineColor(null);
```


## `rare-structural-019` `NvsTemplateCompoundCaptionItemDesc`

Reason: rare SDK usage

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:157`

```java
155: if (!CommonUtils.isEmpty(nvsTemplateCaptionDesc.itemList)) {
156: List<TemplateCaptionDesc.TemplateCompoundCaptionItemDesc> itemDescs = new ArrayList<>();
157: for (NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc nvsTemplateCompoundCaptionItemDesc
158: : nvsTemplateCaptionDesc.itemList) {
159: itemDescs.add(TemplateCaptionDesc.TemplateCompoundCaptionItemDesc.create(nvsTemplateCompoundCaptionItemDesc));
160: }
```

Source: `libEngine/src/main/java/com/meishe/engine/bean/template/TemplateCaptionDesc.java:316`

```java
314: }
316: public static TemplateCompoundCaptionItemDesc create(NvsAssetPackageManager.NvsTemplateCompoundCaptionItemDesc nvsTemplateCompoundCaptionItemDesc) {
317: return new TemplateCompoundCaptionItemDesc(nvsTemplateCompoundCaptionItemDesc.index, nvsTemplateCompoundCaptionItemDesc.text);
318: }
319: }
```


## `rare-structural-020` `NvsTimelineWatermarkPosition_TopLeft`

Reason: rare SDK usage

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:305`

```java
303: }
304: timeline.addWatermark(waterMark.getWatermarkPath(), waterMark.getWatermarkW(), waterMark.getWatermarkH(), 1
305: , NvsTimeline.NvsTimelineWatermarkPosition_TopLeft, waterMark.getWatermarkX(), waterMark.getWatermarkY());
306: }
308: private static void addTimeLineEffect(NvsTimeline timeline) {
```


## `rare-structural-021` `NvsTimelineWatermarkPosition_TopRight`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/WaterMarkUtil.java:34`

```java
32: int marginY = waterMarkData.getExcursionY();
33: if (type == WaterMarkConstant.WATERMARKTYPE_STATIC){
34: mTimeline.addWatermark(waterMarkPath, pictureW,pictureH,1, NvsTimeline.NvsTimelineWatermarkPosition_TopRight , marginX, marginY);
35: }else {
36: mTimeline.deleteWatermark();
37: TimelineUtil.checkAndDeleteExitFX(mTimeline);
```


## `rare-structural-022` `NvsTrackCaption`

Reason: missing from baseline snippets

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1461`

```java
1459: } else if (templateCaptionDesc.trackIndex >= 0 && templateCaptionDesc.clipIndex < 0) {
1460: NvsVideoTrack meicamVideoTrack = meicamTimeline.getVideoTrackByIndex(templateCaptionDesc.trackIndex);
1461: NvsTrackCaption firstCaption = meicamVideoTrack.getFirstCaption();
1462: while (null != firstCaption) {
1463: String id = firstCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID);
1464: if (TextUtils.equals(id, templateCaptionDesc.replaceId)) {
```


## `rare-structural-023` `NvsUnderlineSpan`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3738`

```java
3736: if (checkPosition()) {
3737: List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
3738: NvsUnderlineSpan nvsUnderlineSpan = new NvsUnderlineSpan(mSelectionStart, mSelectionEnd);
3739: setSpanList(nvsUnderlineSpan, underline, textSpanList, captionInfo);
3740: } else {
3741: changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_UNDERLINE,
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5053`

```java
5051: } else if (nvsCaptionSpan instanceof NvsItalicSpan) {
5052: ((NvsItalicSpan) nvsCaptionSpan).setItalic((Boolean) object);
5053: } else if (nvsCaptionSpan instanceof NvsUnderlineSpan) {
5054: ((NvsUnderlineSpan) nvsCaptionSpan).setUnderline((Boolean) object);
5055: } else if (nvsCaptionSpan instanceof NvsRendererIdSpan) {
5056: ((NvsRendererIdSpan) nvsCaptionSpan).setRendererId((String) object);
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5054`

```java
5052: ((NvsItalicSpan) nvsCaptionSpan).setItalic((Boolean) object);
5053: } else if (nvsCaptionSpan instanceof NvsUnderlineSpan) {
5054: ((NvsUnderlineSpan) nvsCaptionSpan).setUnderline((Boolean) object);
5055: } else if (nvsCaptionSpan instanceof NvsRendererIdSpan) {
5056: ((NvsRendererIdSpan) nvsCaptionSpan).setRendererId((String) object);
5057: } else if (nvsCaptionSpan instanceof NvsOutlineColorSpan) {
```

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5136`

```java
5134: } else if (nvsCaptionSpan instanceof NvsItalicSpan) {
5135: return ((NvsItalicSpan) nvsCaptionSpan).isItalic();
5136: } else if (nvsCaptionSpan instanceof NvsUnderlineSpan) {
5137: return ((NvsUnderlineSpan) nvsCaptionSpan).isUnderline();
5138: } else if (nvsCaptionSpan instanceof NvsRendererIdSpan) {
5139: return ((NvsRendererIdSpan) nvsCaptionSpan).getRendererId();
```


## `rare-structural-024` `NvsVideoEffect`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3270`

```java
3268: if (captureVideoFxByIndex.getBuiltinCaptureVideoFxName().equals(Constants.AR_SCENE)) {
3269: String stringVal = captureVideoFxByIndex.getStringVal(Constants.AR_SCENE_ID_KEY);
3270: NvsVideoEffect videoEffect = mNvsEffectSdkContext.createVideoEffect(Constants.AR_SCENE, nvsRational);
3272: if (videoEffect != null) {
3273: if (BuildConfig.FACE_MODEL == 240) {
```

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3358`

```java
3356: float filterIntensity = captureVideoFxByIndex.getFilterIntensity();
3357: if (!TextUtils.isEmpty(captureVideoFxPackageId)) {
3358: NvsVideoEffect videoEffect = mNvsEffectSdkContext.createVideoEffect(captureVideoFxPackageId, nvsRational);
3359: videoEffect.setFilterIntensity(filterIntensity);
3360: effects.add(videoEffect);
3361: }
```


## `rare-structural-025` `NvsVideoEffectAnimatedSticker`

Reason: missing from baseline snippets

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3408`

```java
3406: String animatedStickerPackageId = captureAnimatedStickerByIndex.getAnimatedStickerPackageId();
3407: if (!TextUtils.isEmpty(animatedStickerPackageId)) {
3408: NvsVideoEffectAnimatedSticker stickerFilter = mNvsEffectSdkContext.
3409: createAnimatedSticker(0, STICK_TIME_DURATION /*Long.MAX_VALUE*/, false,
3410: animatedStickerPackageId, nvsRational);
3411: stickerFilter.setScale(0.5f);
```


## `rare-structural-026` `NvsVideoEffectCompoundCaption`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3369`

```java
3367: NvsCaptureCompoundCaption captureCompoundCaption = mStreamingContext.getCaptureCompoundCaptionByIndex(i);
3369: NvsVideoEffectCompoundCaption compoundCaptionFilter = mNvsEffectSdkContext.
3370: createCompoundCaption(0, Long.MAX_VALUE, captureCompoundCaption.
3371: getCaptionStylePackageId(), nvsRational);
```


## `rare-structural-027` `NvsVideoFrameInfo`

Reason: rare SDK usage

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3248`

```java
3247: @Override
3248: public void onCapturedPictureArrived(final ByteBuffer byteBuffer, NvsVideoFrameInfo nvsVideoFrameInfo) {
3249: runOnUiThread(new Runnable() {
3250: @SuppressLint("CheckResult")
3251: @Override
```

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:3431`

```java
3429: ByteBuffer byteBufferResult = mEffectRenderCore.renderEffects(effects.toArray(new NvsEffect[effects.size()]),
3430: byteBuffer.array(), nvsVideoFrameInfo, 0,
3431: NvsVideoFrameInfo.VIDEO_FRAME_PIXEL_FROMAT_RGBA, false,
3432: (System.currentTimeMillis() - mStartPreviewTime) * 1000, 0);
3434: for (int i = 0; i < effects.size(); i++) {
```


## `rare-structural-028` `NvsVolume`

Reason: rare SDK usage

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamAudioClip.java:233`

```java
231: }
233: NvsVolume volumeGain = audioClip.getVolumeGain();
234: if (volumeGain != null) {
235: setVolume(volumeGain.leftVolume);
236: }
```

## `rare-structural-029` `NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO`

Reason: rare capture preview flag used by capture-only effect previews when audio is not needed.

Source: `app/src/main/java/com/meishe/sdkdemo/glitter/GlitterEffectFragment.java:31`

```java
import static com.meicam.sdk.NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO;

boolean started = streamingContext.startCapturePreview(
        currentDeviceIndex,
        captureResolutionGrade,
        NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME
                | NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER
                | STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO,
        null);
```

## `rare-structural-030` `NvsAssetPackageManager` template aspect ratio constants

Reason: template metadata maps SDK aspect-ratio constants to editable canvas ratios.

Source: `MCutSame/src/main/java/com/meishe/cutsame/bean/Template.java:8`

```java
import static com.meicam.sdk.NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_16v9;
import static com.meicam.sdk.NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_18v9;
import static com.meicam.sdk.NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_1v1;
import static com.meicam.sdk.NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_3v4;
import static com.meicam.sdk.NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_4v3;
import static com.meicam.sdk.NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_9v16;
import static com.meicam.sdk.NvsAssetPackageManager.ASSET_PACKAGE_ASPECT_RATIO_9v18;

if (defaultAspectRatio == ASSET_PACKAGE_ASPECT_RATIO_16v9) {
    ratio = 9 / 16f;
} else if (defaultAspectRatio == ASSET_PACKAGE_ASPECT_RATIO_1v1) {
    ratio = 1f;
} else if (defaultAspectRatio == ASSET_PACKAGE_ASPECT_RATIO_9v16) {
    ratio = 16 / 9f;
} else if (defaultAspectRatio == ASSET_PACKAGE_ASPECT_RATIO_4v3) {
    ratio = 3 / 4f;
} else if (defaultAspectRatio == ASSET_PACKAGE_ASPECT_RATIO_3v4) {
    ratio = 4 / 3f;
} else if (defaultAspectRatio == ASSET_PACKAGE_ASPECT_RATIO_18v9) {
    ratio = 9 / 18f;
} else if (defaultAspectRatio == ASSET_PACKAGE_ASPECT_RATIO_9v18) {
    ratio = 18 / 9f;
}
```

## `rare-structural-031` `NvsAssetPackageManager` template footage type constants

Reason: CutSame/template replacement validates selected media against SDK footage slot types.

Source: `MCutSame/src/main/java/com/meishe/cutsame/MaterialSelectActivity.java:46`

```java
import static com.meicam.sdk.NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_FREEZE_FRAME;
import static com.meicam.sdk.NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_IMAGE;
import static com.meicam.sdk.NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_VIDEO;
import static com.meicam.sdk.NvsAssetPackageManager.TEIMPLATE_FOOTAGE_TYPE_VIDEO_IMAGE;

if (clip.getType() == TEIMPLATE_FOOTAGE_TYPE_VIDEO
        || clip.getType() == TEIMPLATE_FOOTAGE_TYPE_FREEZE_FRAME) {
    return mediaData.getType() == MediaData.TYPE_VIDEO && clip.getDuration() <= duration;
}
if (clip.getType() == TEIMPLATE_FOOTAGE_TYPE_IMAGE) {
    return mediaData.getType() == MediaData.TYPE_PHOTO;
}
if (clip.getType() == TEIMPLATE_FOOTAGE_TYPE_VIDEO_IMAGE) {
    return mediaData.getType() == MediaData.TYPE_PHOTO
            || clip.getDuration() <= duration;
}
return false;
```
