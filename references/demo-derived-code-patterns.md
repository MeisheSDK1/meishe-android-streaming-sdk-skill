# Demo-Derived Code Patterns

These snippets were extracted from the Android demo and embedded here so the skill can be used without the original demo folder. Treat them as implementation patterns; adapt names and app architecture to the target project.

Use `demo-simple-snippets-index.md` and the relevant `demo-simple-snippets-*.md` reference first when you need feature/API-level examples. Use this file for curated broader lifecycle patterns and controller-level call order.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [streaming-context-init: Initialize Streaming SDK And Effect SDK](#streaming-context-init-initialize-streaming-sdk-and-effect-sdk)
- [timeline-create-main: Create Main Edit Timeline](#timeline-create-main-create-main-edit-timeline)
- [single-clip-timeline: Create A Single-Clip Timeline](#single-clip-timeline-create-a-single-clip-timeline)
- [append-clip-and-adjust: Append A Clip And Add Built-In Adjust Effects](#append-clip-and-adjust-append-a-clip-and-add-built-in-adjust-effects)
- [capture-preview: Connect Capture Preview And Start Camera](#capture-preview-connect-capture-preview-and-start-camera)
- [capture-recording-toggle: Start And Stop Capture Recording](#capture-recording-toggle-start-and-stop-capture-recording)
- [capture-filters: Add Built-In Or Packaged Capture Filters](#capture-filters-add-built-in-or-packaged-capture-filters)
- [ar-scene-prop: Apply AR Scene Package To Capture Effect](#ar-scene-prop-apply-ar-scene-package-to-capture-effect)
- [asset-package-install: Install Or Upgrade Asset Package](#asset-package-install-install-or-upgrade-asset-package)
- [timeline-stickers: Add Timeline Stickers With Transform And Animation](#timeline-stickers-add-timeline-stickers-with-transform-and-animation)
- [timeline-captions: Add Captions And Compound Captions](#timeline-captions-add-captions-and-compound-captions)
- [compile-video: Compile Timeline To Video](#compile-video-compile-timeline-to-video)
- [compile-callbacks: Register Compile Callbacks](#compile-callbacks-register-compile-callbacks)
- [human-detection-models: Initialize Human Detection Models](#human-detection-models-initialize-human-detection-models)
- [human-detection-data: Set Up Face, Beauty, Segmentation, Hand, Eyeball, Avatar, Sky Models](#human-detection-data-set-up-face-beauty-segmentation-hand-eyeball-avatar-sky-models)
<!-- END GENERATED CONTENTS -->

## streaming-context-init: Initialize Streaming SDK And Effect SDK

Use this as the canonical app-level initialization shape. Keep the license path as an assets URI and select flags based on the requested app.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:116-132`

```java
    /**
     * 统一管理初始化，便于统一添加flag
     * Unified management initialization facilitates unified flag addition
     */
    public static NvsStreamingContext initStreamingContext(Context mContext, String licensePath) {
        return NvsStreamingContext.init(mContext, licensePath, NvsStreamingContext.STREAMING_CONTEXT_FLAG_SUPPORT_4K_EDIT
                | NvsStreamingContext.STREAMING_CONTEXT_FLAG_ENABLE_HDR_DISPLAY_WHEN_SUPPORTED
                | NvsStreamingContext.STREAMING_CONTEXT_FLAG_NEED_GIF_MOTION
                | NvsStreamingContext.STREAMING_CONTEXT_FLAG_INTERRUPT_STOP_FOR_INTERNAL_STOP);
    }

    public static NvsEffectSdkContext initEffectSdkContext(Context mContext, String licensePath) {
        // 初始化 effect sdk ，用到的时候在初始化，没用到没有必要初始化.
        //sdk, when used in the initialization, no need to initialize.
        return NvsEffectSdkContext.init(mContext, licensePath, NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE
                | NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE);
    }
```

## timeline-create-main: Create Main Edit Timeline

Create a timeline, append video/audio tracks, then populate it from app state.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:146-172`

```java
    public static NvsTimeline createTimeline(int width, int height) {
        NvsVideoResolution videoResolution = TimelineData.instance().getVideoResolution();
        if (width > 0 && height > 0) {
            videoResolution.imageWidth = width;
            videoResolution.imageHeight = height;
        }
        NvsTimeline timeline = newTimeline(videoResolution);
        if (timeline == null) {
            Log.e(TAG, "failed to create timeline");
            return null;
        }
        if (!buildVideoTrack(timeline)) {
            return timeline;
        }
        // 音乐轨道 Music track
        timeline.appendAudioTrack();
        // 录音轨道 Recording track
        timeline.appendAudioTrack();

//        //用于贝塞尔曲线的音频轨道
//        NvsAudioTrack audioTrack = timeline.appendAudioTrack();
//        if (audioTrack != null) {
//            audioTrack.setAttachment(Constants.ATTACHMENT_AUDIO_CURVE, true);
//        }
        setTimelineData(timeline);
        return timeline;
    }
```

## single-clip-timeline: Create A Single-Clip Timeline

Use this pattern for trim, clip-edit, or quick preview workflows.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:178-214`

```java
    public static NvsTimeline createSingleClipTimeline(ClipInfo clipInfo, boolean isTrimClip) {
        NvsTimeline timeline = newTimeline(TimelineData.instance().getVideoResolution());
        if (timeline == null) {
            Log.e(TAG, "failed to create timeline");
            return null;
        }
        buildSingleClipVideoTrack(timeline, clipInfo, isTrimClip);
        return timeline;
    }

    /**
     * 片段编辑页面时间线扩展API
     * Clip Edit Page Timeline Extension API
     */
    public static NvsTimeline createSingleClipTimelineExt(NvsVideoResolution videoEditRes, String filePath) {
        NvsTimeline timeline = newTimeline(videoEditRes);
        if (timeline == null) {
            Log.e(TAG, "failed to create timeline");
            return null;
        }
        buildSingleClipVideoTrackExt(timeline, filePath);
        return timeline;
    }

    public static boolean buildSingleClipVideoTrack(NvsTimeline timeline, ClipInfo clipInfo, boolean isTrimClip) {
        if (timeline == null || clipInfo == null) {
            return false;
        }
        NvsVideoTrack videoTrack = timeline.appendVideoTrack();
        if (videoTrack == null) {
            Log.e(TAG, "failed to append video track");
            return false;
        }
        NvsVideoResolution videoRes = timeline.getVideoRes();
        addVideoClip(videoTrack, clipInfo, isTrimClip, videoRes);
        return true;
    }
```

## append-clip-and-adjust: Append A Clip And Add Built-In Adjust Effects

Shows content path resolution, appendClip, null handling, background mode, and parameterized built-in effects.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:396-465`

```java
    private static void addVideoClip(NvsVideoTrack videoTrack, ClipInfo clipInfo, boolean isTrimClip, NvsVideoResolution videoRes) {
        if (videoTrack == null || clipInfo == null) {
            return;
        }
        String filePath = FileUtils.getAbsPathByContentUri(MSApplication.getContext(),
                MSApplication.CONTENT_FLAG, clipInfo.getFilePath());
        NvsVideoClip videoClip = null;
        LivePhotoInfo livePhotoInfo = clipInfo.getLivePhotoInfo();
        if (null != livePhotoInfo) {
            String url = livePhotoInfo.getLivePhotoUrl();
            videoClip = videoTrack.appendClip(url);
        } else {
            videoClip = videoTrack.appendClip(filePath);
        }
        if (videoClip == null) {
            Log.e(TAG, "failed to append video clip");
            return;
        }
        boolean blurFlag = ParameterSettingValues.instance().isUseBackgroudBlur();
        if (blurFlag) {
            videoClip.setSourceBackgroundMode(NvsVideoClip.ClIP_BACKGROUNDMODE_BLUR);
        }
        //获取亮度 对比度 饱和度 高光 阴影 褪色 Get brightness contrast saturation highlight shadow fade
        CorrectionColorInfo correctionColorInfo = clipInfo.getCorrectionColorInfo();
        if (correctionColorInfo != null) {
            float brightVal = correctionColorInfo.getBrightnessVal();
            float contrastVal = correctionColorInfo.getContrastVal();
            float saturationVal = correctionColorInfo.getSaturationVal();
            float highLight = correctionColorInfo.getmHighLight();
            float shadow = correctionColorInfo.getmShadow();
            float fade = correctionColorInfo.getFade();
            //暗角 Dark Angle
            float vignette = correctionColorInfo.getVignetteVal();
            //获取锐度 Gain sharpness
            float sharpen = correctionColorInfo.getSharpenVal();
            //获取色温 色调 Get the color temperature hue
            float temperature = correctionColorInfo.getTemperature();
            float tint = correctionColorInfo.getTint();
            //噪点 Noise point
            float density = correctionColorInfo.getDensity();
            float denoiseDensity = correctionColorInfo.getDenoiseDensity();
            NvsVideoFx mColorVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
            mColorVideoFx.setAttachment(Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST, Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
            mColorVideoFx.setFloatVal(Constants.ADJUST_BRIGHTNESS, brightVal);
            mColorVideoFx.setFloatVal(Constants.ADJUST_CONTRAST, contrastVal);
            mColorVideoFx.setFloatVal(Constants.ADJUST_SATURATION, saturationVal);
            mColorVideoFx.setFloatVal(Constants.ADJUST_HIGHTLIGHT, highLight);
            mColorVideoFx.setFloatVal(Constants.ADJUST_SHADOW, shadow);
            mColorVideoFx.setFloatVal(Constants.ADJUST_FADE, fade);

            NvsVideoFx mVignetteVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_VIGETTE);
            mVignetteVideoFx.setAttachment(Constants.ADJUST_TYPE_VIGETTE, Constants.ADJUST_TYPE_VIGETTE);
            mVignetteVideoFx.setFloatVal(Constants.ADJUST_DEGREE, vignette);

            NvsVideoFx mSharpenVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_SHARPEN);
            mSharpenVideoFx.setAttachment(Constants.ADJUST_TYPE_SHARPEN, Constants.ADJUST_TYPE_SHARPEN);
            mSharpenVideoFx.setFloatVal(Constants.ADJUST_AMOUNT, sharpen);

            NvsVideoFx mTintVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_TINT);
            mTintVideoFx.setAttachment(Constants.ADJUST_TYPE_TINT, Constants.ADJUST_TYPE_TINT);
            mTintVideoFx.setFloatVal(Constants.ADJUST_TEMPERATURE, temperature);
            mTintVideoFx.setFloatVal(Constants.ADJUST_TINT, tint);


            NvsVideoFx mDenoiseVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_DENOISE);
            mDenoiseVideoFx.setAttachment(Constants.ADJUST_TYPE_DENOISE, Constants.ADJUST_TYPE_DENOISE);
            mDenoiseVideoFx.setFloatVal(Constants.ADJUST_DENOISE, density);
            mDenoiseVideoFx.setFloatVal(Constants.ADJUST_DENOISE_DENSITY, denoiseDensity);
            mDenoiseVideoFx.setBooleanVal(Constants.ADJUST_DENOISE_COLOR_MODE, correctionColorInfo.isNoiseGrayscale());
        }
```

## capture-preview: Connect Capture Preview And Start Camera

Use for live camera preview. Runtime permissions must be handled before startCapturePreview on modern Android.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2955-3029`

```java
        int captureDeviceCount = mStreamingContext.getCaptureDeviceCount();
        if (captureDeviceCount == 0) {
            return;
        }

        /*
         * 将采集预览输出连接到LiveWindow控件
         * Connect the capture preview output to the LiveWindow control
         * */
        if (mLiveWindow instanceof MSLiveWindow) {
            if (!mStreamingContext.connectCapturePreviewWithLiveWindow((MSLiveWindow) mLiveWindow)) {
                Log.e(TAG, "Failed to connect capture preview with livewindow!");
                return;
            }

        } else if (mLiveWindow instanceof MSLiveWindowExt) {
            if (!mStreamingContext.connectCapturePreviewWithLiveWindowExt((MSLiveWindowExt) mLiveWindow)) {
                Log.e(TAG, "Failed to connect capture preview with livewindow!");
                return;
            }
        } else {
            return;
        }

        /*
         * 采集设备数量判定
         * Judging the count of collection equipment
         * */
        if (captureDeviceCount > 1) {
            mCurrentDeviceIndex = 1;
            mIvChangeCamera.setEnabled(true);
        } else {
            mCurrentDeviceIndex = 0;
            mIvChangeCamera.setEnabled(false);
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            checkPermissions();
        } else {
            try {
                startCapturePreview(false);
            } catch (Exception e) {
                e.printStackTrace();
                Log.e(TAG, "startCapturePreviewException: initCapture failed,under 6.0 device may has no access to camera");
                PermissionDialog.noPermissionDialog(CaptureActivity.this);
            }
        }
        if (getIntent() != null) {
            Bundle bundle = getIntent().getExtras();
            if (bundle != null) {
                initArScene = bundle.getBoolean("initArScene");
            }
        }
    }

    private boolean startCapturePreview(boolean deviceChanged) {
        mStartPreviewTime = System.currentTimeMillis();
        /*
         * 判断当前引擎状态是否为采集预览状态
         * Determine if the current engine status is the collection preview status
         * */
        int captureResolutionGrade = ParameterSettingValues.instance().getCaptureResolutionGrade();
        if (deviceChanged || getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW) {
            m_supportAutoFocus = false;
            if (!mStreamingContext.startCapturePreview(mCurrentDeviceIndex, captureResolutionGrade,
                    NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER |
                            NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME |
                            NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_ENABLE_TAKE_PICTURE |
                            NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE, null)) {
                Log.e(TAG, "Failed to start capture preview!");
                return false;
            }
        }
        checkFlashState(mCurrentDeviceIndex != 1);
        return true;
    }
```

## capture-recording-toggle: Start And Stop Capture Recording

Check engine state, generate an output path, then call startRecording/stopRecording.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:2100-2149`

```java

        /*
         * 开始录制
         *Start recording
         */
        mFlStartRecord.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean startNativeCamera = parameterValues.isStartNativeCamera();
                if (startNativeCamera) {
                    if (mRecordType == Constants.RECORD_TYPE_PICTURE) {
                        takePhoto();
                        changeRecordDisplay(RECORD_DEFAULT, true);
                        return;
                    }
                }

                /*
                 * 当前在录制状态，可停止视频录制
                 * Currently in recording state, you can stop video recording
                 */
                if (getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
                    stopRecording();
                } else {
                    mCurRecordVideoPath = PathUtils.getRecordVideoPath();
                    if (mCurRecordVideoPath == null) {
                        return;
                    }
                    mFlStartRecord.setEnabled(false);
                    if (mRecordType == Constants.RECORD_TYPE_VIDEO) {
                        mEachRecodingVideoTime = 0;
                        /*
                         * 当前未在视频录制状态，则启动视频录制。此处使用带特效的录制方式
                         * If video recording is not currently in progress, start video recording. Use the recording method with special effects here
                         */
                        if (!mStreamingContext.startRecording(mCurRecordVideoPath)) {
                            return;
                        }
                        if (mSelectMusicInfo != null) {
                            if (mAllRecordingTime == 0) {
                                AudioPlayer.getInstance(mContext).setCurrentMusic(mSelectMusicInfo, true);
                            } else {
                                AudioPlayer.getInstance(mContext).seekPosition(mAllRecordingTime + mSelectMusicInfo.getTrimIn());
                            }
                            AudioPlayer.getInstance(mContext).startPlay();
                        }
                        changeSelectMusicState(false);
                        changeRecordDisplay(RECORDING, false);
                        mRecordFileList.add(mCurRecordVideoPath);
                    } else if (mRecordType == Constants.RECORD_TYPE_PICTURE) {
```

## capture-filters: Add Built-In Or Packaged Capture Filters

Use appendBuiltinCaptureVideoFx for built-ins and appendPackagedCaptureVideoFx for installed packages.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1544-1561`

```java
                int filterMode = filterItem.getFilterMode();
                if (filterMode == FilterItem.FILTERMODE_BUILTIN) {
                    String filterName = filterItem.getFilterName();
                    if (!TextUtils.isEmpty(filterName) && filterItem.getIsCartoon()) {
                        mCurCaptureVideoFx = mStreamingContext.appendBuiltinCaptureVideoFx("Cartoon");
                        mCurCaptureVideoFx.setBooleanVal("Stroke Only", filterItem.getStrokenOnly());
                        mCurCaptureVideoFx.setBooleanVal("Grayscale", filterItem.getGrayScale());
                    } else if (!TextUtils.isEmpty(filterName)) {
                        mCurCaptureVideoFx = mStreamingContext.appendBuiltinCaptureVideoFx(filterName);
                    }
                    mVideoClipFxInfo.setFxMode(VideoClipFxInfo.FXMODE_BUILTIN);
                    mVideoClipFxInfo.setFxId(filterName);
                } else {
                    String filterPackageId = filterItem.getPackageId();
                    if (!TextUtils.isEmpty(filterPackageId)) {
                        mCurCaptureVideoFx = mStreamingContext.appendPackagedCaptureVideoFx(filterPackageId);
                    }
                    mVideoClipFxInfo.setFxMode(VideoClipFxInfo.FXMODE_PACKAGE);
```

## ar-scene-prop: Apply AR Scene Package To Capture Effect

Use the AR scene id string parameter on the AR scene capture effect.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1608-1630`

```java
            isPropContainShape = true;
        } else {
            isPropContainShape = false;
        }
        String sceneId = packageId;
        showPropsToast(sceneId);
        //重置默认值
        mArSceneFaceEffect.setFloatVal(Constants.AR_SCENE_FACE_CAMERA_FOVY_ID_KEY, 45);
        NvsAssetPackageManager.ARSceneCameraPreset cameraPreset = mAssetPackageManager.getARSceneAssetPackageCameraPreset(packageId);
        if (null != cameraPreset) {
            float fovy = cameraPreset.fovy;
            mArSceneFaceEffect.setFloatVal(Constants.AR_SCENE_FACE_CAMERA_FOVY_ID_KEY, fovy);
        }
        mArSceneFaceEffect.setStringVal(Constants.AR_SCENE_ID_KEY, sceneId);
    }

    @MSSubscribe(Constants.SubscribeType.SUB_UN_USE_PROP_TYPE)
    private void removeAllProp() {
        if (mArSceneFaceEffect == null) {
            return;
        }
        mArSceneFaceEffect.setStringVal("Scene Id", "");
        isPropContainShape = false;
```

## asset-package-install: Install Or Upgrade Asset Package

Treat already-installed packages as success and upgrade when the package file version is newer.

Provenance label: `libBase/src/main/java/com/meishe/utils/PackageManagerUtil.java:90-134`

```java
                String parentPath = PathNameUtil.getOutOfPathSuffixWithOutPoint(packagePath);
                licPath = parentPath + ".lic";
                if (!new File(licPath).exists()) {
                    Log.e(TAG, "installAssetPackage local licPath: " + licPath
                            + "  is not exists");
                    licPath = "";
                }
            }
        }
//        if (!noLic && (licPath == null || licPath.isEmpty())) {
//            Log.e(TAG, "installAssetPackage licPath is null! packagePath: " + packagePath
//                    + " licPath: " + licPath, new Exception(""));
//        }
        if (noLic){
            licPath = "";
        }
        NvsAssetPackageManager packageManager = NvsStreamingContext.getInstance().getAssetPackageManager();
        int code;
        StringBuilder stringBuilder = new StringBuilder();
        if (synchronous) {
            code = packageManager.installAssetPackage(packagePath, licPath, packageType, true, stringBuilder);
        } else {
            code = packageManager.installAssetPackage(packagePath, licPath, packageType, false, asynchronousStringBuilder);
        }
//        Log.d("====","====installAssetPackage=="+code+"=="+packageType+"=="+packagePath);
        if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR || code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
            if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
                int version = packageManager.getAssetPackageVersion(FileUtils.getFileName(packagePath), packageType);
                int newVersion = packageManager.getAssetPackageVersionFromAssetPackageFilePath(packagePath);
                if (newVersion > version) {
                    packageManager.upgradeAssetPackage(packagePath, licPath, packageType, true, new StringBuilder());
                }
            }
            return stringBuilder.toString();
        } else {
            if (synchronous) {
                Log.e(TAG, "error synchronous installAssetPackage packagePath: " + packagePath + " packageType: " + packageType + " errorCode: " + code);
            } else {
                if (code != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_WORKING_INPROGRESS) {
                    Log.e(TAG, "error asynchronous installAssetPackage packagePath: " + packagePath + " packageType: " + packageType + " errorCode: " + code);
                }
            }
            return "";
        }
    }
```

## timeline-stickers: Add Timeline Stickers With Transform And Animation

Use for timeline animated sticker generation, keyframes, transforms, in/out animation, period animation, and audio gain.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1320-1390`

```java
        if (timeline == null) {
            return false;
        }
        NvsTimelineAnimatedSticker deleteSticker = timeline.getFirstAnimatedSticker();
        while (deleteSticker != null) {
            deleteSticker = timeline.removeAnimatedSticker(deleteSticker);
        }

        for (StickerInfo sticker : stickerArray) {
            long duration = sticker.getOutPoint() - sticker.getInPoint();
            boolean isCutsomSticker = sticker.isCustomSticker();
            NvsTimelineAnimatedSticker timelineSticker = isCutsomSticker ?
                    timeline.addCustomAnimatedSticker(sticker.getInPoint(), duration, sticker.getId(), sticker.getCustomImagePath())
                    : timeline.addAnimatedSticker(sticker.getInPoint(), duration, sticker.getId());
            if (timelineSticker == null) {
                continue;
            }
            applyAnimatedStickerAnimation(timelineSticker, sticker);
            // 判断是否应用关键帧信息
            //Determine whether to apply key frame information
            Map<Long, KeyFrameInfo> keyFrameInfoHashMap = sticker.getKeyFrameInfoHashMap();
            if (keyFrameInfoHashMap.isEmpty()) {
                PointF translation = sticker.getTranslation();
                float scaleFactor = sticker.getScaleFactor();
                float rotation = sticker.getRotation();
                timelineSticker.setScale(scaleFactor);
                timelineSticker.setRotationZ(rotation);
                timelineSticker.setTranslation(translation);
            } else {
                Set<Map.Entry<Long, KeyFrameInfo>> entries = keyFrameInfoHashMap.entrySet();
                for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
                    timelineSticker.setCurrentKeyFrameTime(entry.getKey() - timelineSticker.getInPoint());
                    KeyFrameInfo keyFrameInfo = entry.getValue();
                    timelineSticker.setRotationZ(keyFrameInfo.getRotationZ());
                    timelineSticker.setScale(keyFrameInfo.getScaleX());
                    timelineSticker.setTranslation(keyFrameInfo.getTranslation());
                }
            }
            float volumeGain = sticker.getVolumeGain();
            timelineSticker.setVolumeGain(volumeGain, volumeGain);
        }
        return true;
    }

    /**
     * 贴纸动画生效
     * AnimatedStickerAnimation effect
     *
     * @param animatedSticker sticker
     * @param stickerInfo     sticker info
     */
    public static void applyAnimatedStickerAnimation(NvsAnimatedSticker animatedSticker, StickerInfo stickerInfo) {
        if (animatedSticker == null || stickerInfo == null) {
            return;
        }
        animatedSticker.setZValue(stickerInfo.getAnimateStickerZVal());
        animatedSticker.setHorizontalFlip(stickerInfo.isHorizFlip());
        //动画 1判断组合 2 判断进出 Animation 1 Judge combination 2 Judge in and out
        if (!TextUtils.isEmpty(stickerInfo.getPeriodAnimationId())) {
            animatedSticker.applyAnimatedStickerPeriodAnimation(stickerInfo.getPeriodAnimationId());
            animatedSticker.setAnimatedStickerAnimationPeriod((int) stickerInfo.getPeriodAnimationDuration());
        } else {
            //进动画 Advance animation
            animatedSticker.applyAnimatedStickerInAnimation(stickerInfo.getInAnimationId());
            animatedSticker.setAnimatedStickerInAnimationDuration((int) stickerInfo.getInAnimationDuration());
            //出动画 animation
            animatedSticker.applyAnimatedStickerOutAnimation(stickerInfo.getOutAnimationId());
            animatedSticker.setAnimatedStickerOutAnimationDuration((int) stickerInfo.getOutAnimationDuration());
        }

    }
```

## timeline-captions: Add Captions And Compound Captions

Use addCaption/addModularCaption/addCompoundCaption and then apply attributes.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1392-1458`

```java
    public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray) {
        return setCaption(timeline, captionArray, 0, false);
    }

    public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray, long themeDuration) {
        return setCaption(timeline, captionArray, themeDuration, false);
    }

    public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray, long themeDuration, boolean userRecordingFlag) {
        if (timeline == null) {
            return false;
        }
        NvsTimelineCaption deleteCaption = timeline.getFirstCaption();
        while (deleteCaption != null) {
            int capCategory = deleteCaption.getCategory();
            Logger.e(TAG, "capCategory = " + capCategory);
            int roleTheme = deleteCaption.getRoleInTheme();
            //主题字幕不作删除 Subject captions will not be deleted
            if (capCategory == NvsTimelineCaption.THEME_CATEGORY
                    && roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {
                deleteCaption = timeline.getNextCaption(deleteCaption);
            } else {
                deleteCaption = timeline.removeCaption(deleteCaption);
            }
        }

        NvsTimelineCaption newCaption;
        for (CaptionInfo caption : captionArray) {
            long duration = caption.getOutPoint() - caption.getInPoint();
            if (caption.isTraditionCaption()) {
                //传统字幕 Traditional subtitles
                newCaption = timeline.addCaption(caption.getText(), caption.getInPoint() + themeDuration,
                        duration, null);
            } else {
                //拼装字幕 Assembled subtitles
                newCaption = timeline.addModularCaption(caption.getText(), caption.getInPoint() + themeDuration,
                        duration);
            }
            updateCaptionAttribute(newCaption, caption, userRecordingFlag);
        }
        return true;
    }

    /**
     * 添加组合字幕
     * add compound caption
     *
     * @param timeline     timeline
     * @param captionArray array
     * @return boolean
     */
    public static boolean setCompoundCaption(NvsTimeline timeline, ArrayList<CompoundCaptionInfo> captionArray) {
        if (timeline == null) {
            return false;
        }

        NvsTimelineCompoundCaption deleteCaption = timeline.getFirstCompoundCaption();
        while (deleteCaption != null) {
            deleteCaption = timeline.removeCompoundCaption(deleteCaption);
        }

        for (CompoundCaptionInfo caption : captionArray) {
            long duration = caption.getOutPoint() - caption.getInPoint();
            NvsTimelineCompoundCaption newCaption = timeline.addCompoundCaption(caption.getInPoint(),
                    duration, caption.getCaptionStyleUuid());
            updateCompoundCaptionAttribute(newCaption, caption);
        }
```

## compile-video: Compile Timeline To Video

Stop the engine, clear configurations, set bitrate/HDR/HEVC options, then compileTimeline.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/utils/VideoCompileUtil.java:44-104`

```java
    public static void compileVideo(NvsStreamingContext context,
                                    NvsTimeline timeline,
                                    String compileVideoPath,
                                    long startTime,
                                    long endTime, int videoResolutionGrade, int customHeight) {
        if (context == null || timeline == null || compileVideoPath.isEmpty()) {
            return;
        }
        context.stop();
        /*
         * 之前配置清空
         * Clear before configuration
         * */
        context.setCompileConfigurations(null);
        double bitrate = ParameterSettingValues.instance().getCompileBitrate();
        Hashtable<String, Object> compileConfigurations = new Hashtable<>();
        int encoderFlag = 0;
        if (ParameterSettingValues.instance().disableDeviceEncorder()) {
            encoderFlag = NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_DISABLE_HARDWARE_ENCODER;
        }
        if (bitrate != 0) {
            compileConfigurations.put(NvsStreamingContext.COMPILE_BITRATE, bitrate * 1000000);
        }
        ParameterSettingValues settingValues = ParameterSettingValues.instance();
        Log.d("ParameterSetting", "compile supportHEVC:" + settingValues.isSupportHEVC());
        if (settingValues.isSupportHEVC()) {
            compileConfigurations.put(NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME, Constants.HDR_EXPORT_HEVC);
            Log.d("ParameterSetting", "compile name:" + NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME + " value:" + Constants.HDR_EXPORT_HEVC);
            if (settingValues.getBitDepth() != NvsVideoResolution.VIDEO_RESOLUTION_BIT_DEPTH_8_BIT) {
                compileConfigurations.put(NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER, settingValues.getExportConfig());
                Log.d("ParameterSetting", "compile name:" + NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER +
                        " value:" + settingValues.getExportConfig());
            }
        }
        Hashtable<String, Object> compileConfigurations1 = VideoCompileUtil.getCompileConfigurations(compileConfigurations);
        context.setCompileConfigurations(compileConfigurations1);
        if (customHeight != -1) {
            context.setCustomCompileVideoHeight(customHeight);
            context.compileTimeline(timeline, startTime, endTime, compileVideoPath,
                    NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, encoderFlag
                            | NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME
                            | NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME
                            | NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_IGNORE_TIMELINE_VIDEO_SIZE);
        } else {
            context.compileTimeline(timeline, startTime, endTime, compileVideoPath,
                    videoResolutionGrade, NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH, encoderFlag
                            | NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME
                            | NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME
            );
        }
    }

    public static void compileVideo(NvsStreamingContext context,
                                    NvsTimeline timeline,
                                    String compileVideoPath,
                                    long startTime,
                                    long endTime) {
        NvsVideoResolution videoRes = timeline.getVideoRes();
        int resultHeight = Util.getCustomHeight(videoRes.imageWidth, videoRes.imageHeight);
        compileVideo(context, timeline, compileVideoPath, startTime, endTime, NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM, resultHeight);
    }
```

## compile-callbacks: Register Compile Callbacks

Use callbacks to drive progress UI, success/failure handling, media scanning, and cleanup.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/edit/CompileVideoFragment.java:205-264`

```java
    public void initCompileCallBack() {
        mStreamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {
            @Override
            public void onCompileProgress(NvsTimeline nvsTimeline, int i) {
                setCenterProgress(i);
            }

            @Override
            public void onCompileFinished(NvsTimeline nvsTimeline) {
//                Toast.makeText(getActivity().getApplicationContext(),
//                        "生成耗时： " + (System.currentTimeMillis() - costTime), Toast.LENGTH_LONG).show();
                Log.e(TAG, "onCompileFinished: 生成耗时： " + (System.currentTimeMillis() - costTime));
                mStreamingContext.setCompileConfigurations(null);
                /*
                 * 加入到媒体库
                 * Add to media library
                 * */
                MediaScannerUtil.scanFile(mCompileVideoPath, "video/mp4");
                if (mCompileVideoListener != null)
                    mCompileVideoListener.compileFinished(nvsTimeline);
            }

            @Override
            public void onCompileFailed(NvsTimeline nvsTimeline) {
                onCompileFiled();
                String[] tipsName = getResources().getStringArray(R.array.compile_video_failed_tips);
                Util.showDialog(getActivity(), tipsName[0], tipsName[1]);
                if (mCompileVideoListener != null)
                    mCompileVideoListener.compileFailed(nvsTimeline);
                removeLogoSticker();
            }
        });
        mStreamingContext.setCompileCallback2(new NvsStreamingContext.CompileCallback2() {
            @Override
            public void onCompileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
                if (!isCanceled) {
                    mStreamingContext.setCompileConfigurations(null);
                    mCompileVideoRect.setVisibility(View.GONE);
                    mCompileVideoFinished.setVisibility(View.VISIBLE);

                    /*
                     * 加入到媒体库
                     * Add to media library
                     * */
                    MediaScannerUtil.scanFile(mCompileVideoPath, "video/mp4");

                    String[] tipsName = getResources().getStringArray(R.array.compile_video_success_tips);
                    StringBuilder successTips = new StringBuilder();
                    successTips.append(tipsName[0]);
                    successTips.append("\n");
                    successTips.append(mCompileVideoPath);
                    Logger.e(TAG, "successTips" + successTips.toString());
                    ToastUtil.showToastCenter(getActivity(), successTips.toString());
                }
                removeLogoSticker();
                if (mCompileVideoListener != null)
                    mCompileVideoListener.compileCompleted(nvsTimeline, isCanceled);

            }
        });
```

## human-detection-models: Initialize Human Detection Models

Check AR module availability before model setup.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:68-85`

```java
    public void initMeicamModel(Context context, boolean arSceneFinished
            , OnInitModelListener onInitModelListener) {
        //检测SDK包是否有人脸模块 Detects if the SDK package has a face module
        int mCanUseArFaceType = NvsStreamingContext.hasARModule();
        Logger.e(TAG, "mCanUseArFaceType:" + mCanUseArFaceType);
        // 初始化AR Scene，全局只需一次 Initialize the AR Scene, global only once
        if (mCanUseArFaceType == HUMAN_AI_TYPE_MS && !arSceneFinished) {
            boolean initSuccess = initArSceneEffect(context);
            if (null != onInitModelListener) {
                onInitModelListener.onInitModel(initSuccess);
            }
        } else {
            if (null != onInitModelListener) {
                onInitModelListener.onInitModel(false);
            }
            Logger.e(TAG, "initARScene false no face model");
        }
```

## human-detection-data: Set Up Face, Beauty, Segmentation, Hand, Eyeball, Avatar, Sky Models

Only initialize the model families needed by the generated app; choose lighter segmentation models on low-end devices.

Provenance label: `app/src/main/java/com/meishe/sdkdemo/MeicamContextWrap.java:118-235`

```java
        /*
         * 人脸通用模型初始化
         *The face common model is initialized
         */
        String faceCommonPath = "assets:/facemode/common/" + FACE_COMMON_DAT;
        boolean faceCommonSuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON, faceCommonPath);
        /*
         * 对应的effect sdk的部分（如果没用到可以不填加）
         * The part of the corresponding effect sdk (if not used, you can leave it blank)
         */
        NvsEffectSdkContext.setupHumanDetectionData(NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON, faceCommonPath);
//--------------------------------------------------------------------------------------------------

        /*
         * 美颜，美妆模型初始化
         *The advanced beauty model is initialized
         */
        String advancedBeautyPath = "assets:/facemode/common/" + ADVANCED_BEAUTY_DAT;
        boolean advancedBeautySuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY, advancedBeautyPath);

        /*
         * 对应的effect sdk的部分（如果没用到可以不填加）
         * The part of the corresponding effect sdk (if not used, you can leave it blank)
         */
        NvsEffectSdkContext.setupHumanDetectionData(NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY, advancedBeautyPath);
//--------------------------------------------------------------------------------------------------

        /*
         * 假脸模型初始化，类似面具效果等，特效只跟随脸部动
         * Fake face model initialization, similar to mask effects, etc., the special effects only follow the movement of the face
         */
        String fakeFacePath = "assets:/facemode/common/" + FAKE_FACE_DAT;
        boolean fakefaceSuccess = NvsStreamingContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE, fakeFacePath);

        /*
         * 对应的effect sdk的部分（如果没用到可以不填加）
         * The part of the corresponding effect sdk (if not used, you can leave it blank)
         */
        NvsEffectSdkContext.setupHumanDetectionData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE, fakeFacePath);
//--------------------------------------------------------------------------------------------------
        /*
         * 人像背景分割模型
         * Portrait Background Segmentation Model
         */
        String segPath = "assets:/facemode/common/" + HUMAN_SEG_MODEL;
        if (null != NvsStreamingContext.getInstance()) {
            int level = NvsStreamingContext.getInstance().getDeviceCpuLevel();
            Log.e(TAG, "MS CPU level:-->" + level);
            if (level == NvsStreamingContext.DEVICE_POWER_LEVEL_LOW) {
                segPath = "assets:/facemode/common/" + HUMAN_SEG_LEVEL_LOW_MODEL;
            }
        }
        boolean segSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),
                segPath, null, NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND);

        /*
         * 对应的effect sdk的部分（如果没用到可以不填加）
         * The part of the corresponding effect sdk (if not used, you can leave it blank)
         */
        NvsEffectSdkContext.initHumanDetectionExt(MSApplication.getContext(),
                segPath, null, NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND);
//--------------------------------------------------------------------------------------------------

        /*
         * 手势点位模型，比心等效果会使用到这个模型
         * Gesture point model, heart and other effects will use this model
         */
        String handPath = "assets:/facemode/common/" + HAND_MODEL;
        boolean handSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(), handPath, null,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK
                        | NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION);

        /*
         * 对应的effect sdk的部分（如果没用到可以不填加）
         * The part of the corresponding effect sdk (if not used, you can leave it blank)
         */
        NvsEffectSdkContext.initHumanDetectionExt(MSApplication.getContext(), handPath, null,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK
                        | NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION);
//--------------------------------------------------------------------------------------------------
        /*
         * 眼球模型初始化 , 作用在美妆的 美瞳选项 ,不用美妆美瞳 可以不做初始化
         */
        String eyeBallModelPath = "assets:/facemode/common/" + EYE_CONTOUR_MODEL;
        boolean eyeBallSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(), eyeBallModelPath, null
                , NvsStreamingContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK | NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE);
        /*
         * 对应的effect sdk的部分（如果没用到可以不填加）
         * The part of the corresponding effect sdk (if not used, you can leave it blank)
         */
        NvsEffectSdkContext.initHumanDetectionExt(MSApplication.getContext(),
                eyeBallModelPath, null, NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK);
//--------------------------------------------------------------------------------------------------
        /*
         * avatar模型初始化，小狐狸效果等，根据表情动的特效果类别会使用这个模型
         * avatar model initialization, little fox effect, etc.,
         * this model will be used according to the special effect category of facial expressions
         */
        modelPath = "assets:/facemode/common/" + AVATAR_MODEL;
        boolean avatarSuccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),
                modelPath,
                null,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_AVATAR_EXPRESSION);
        /*
         * 对应的effect sdk的部分（如果没用到可以不填加）
         * The part of the corresponding effect sdk (if not used, you can leave it blank)
         */
        NvsEffectSdkContext.initHumanDetectionExt(MSApplication.getContext(),
                modelPath,
                null,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_AVATAR_EXPRESSION);
//--------------------------------------------------------------------------------------------------
        modelPath = "assets:/facemode/common/" + SKY_SEG_MODEL;
        boolean skySeguccess = NvsStreamingContext.initHumanDetectionExt(MSApplication.getContext(),
                modelPath,
                null,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_SKY);
        StringBuilder sb = new StringBuilder();
```
