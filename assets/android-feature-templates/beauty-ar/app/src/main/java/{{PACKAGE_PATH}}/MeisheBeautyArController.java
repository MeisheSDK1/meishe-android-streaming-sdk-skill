package {{PACKAGE_NAME}};

import android.content.Context;

import com.meicam.effect.sdk.NvsEffectSdkContext;
import com.meicam.sdk.NvsARSceneManipulate;
import com.meicam.sdk.NvsAudioResolution;
import com.meicam.sdk.NvsCaptureVideoFx;
import com.meicam.sdk.NvsColor;
import com.meicam.sdk.NvsFx;
import com.meicam.sdk.NvsMakeupEffectInfo;
import com.meicam.sdk.NvsRational;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoFx;
import com.meicam.sdk.NvsVideoResolution;
import com.meicam.sdk.NvsVideoTrack;

import java.util.Hashtable;

public final class MeisheBeautyArController {
    private static final String AR_SCENE = "AR Scene";
    private static final String AR_SCENE_ID = "Scene Id";
    private static final String AI_FACE_OCCLUSION_ENABLED = "AI Face Occlusion Enabled";
    private static final String MAX_FACES_RESPECT_MIN = "Max Faces Respect Min";
    private static final String SINGLE_BUFFER_MODE = "Single Buffer Mode";
    private static final String BEAUTY_SHAPE = "Beauty Shape";
    private static final String FACE_MESH_INTERNAL_ENABLED = "Face Mesh Internal Enabled";
    private static final String EYEBROW_ANGLE_PACKAGE_ID =
            "Face Mesh Eyebrow Angle Custom Package Id";
    private static final String EYEBROW_ANGLE_DEGREE = "Face Mesh Eyebrow Angle Degree";
    private static final String FACE_106_MODEL = "ms_face106_v4.0.3.next.model";
    private static final String FACE_240_MODEL = "ms_face240_v4.0.3.next.model";
    private static final String FACE_COMMON_DAT = "facecommon_v1.0.1.dat";
    private static final String ADVANCED_BEAUTY_DAT = "advancedbeauty_v1.0.1.dat";
    private static final String FAKE_FACE_DAT = "fakeface_v1.0.1.dat";
    private static final String HUMAN_SEGMENT_SMALL_MODEL = "ms_humansegment_small_v2.0.0.next.model";
    private static final String HUMAN_SEGMENT_MEDIUM_MODEL = "ms_humansegment_medium_v2.0.0.next.model";
    private static final String HAND_MODEL = "ms_hand_common_v2.0.0.next.model";
    private static final String EYE_CONTOUR_MODEL = "ms_eyecontour_v2.0.0.next.model";
    private static final String AVATAR_MODEL = "ms_avatar_v2.0.0.next.model";
    private static final String SKY_SEGMENT_MODEL = "ms_skysegment_v1.0.5.next.model";

    private final NvsStreamingContext streamingContext;

    public MeisheBeautyArController(NvsStreamingContext streamingContext) {
        this.streamingContext = streamingContext;
    }

    public boolean initializeEffectSdkIfNeeded(Context context) {
        MeisheThreading.requireMainThread("NvsEffectSdkContext.init");
        if (context == null) {
            return false;
        }
        if (NvsEffectSdkContext.getInstance() != null) {
            return true;
        }
        return NvsEffectSdkContext.init(
                context.getApplicationContext(),
                "assets:/meishesdk.lic",
                NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_VIDEO_MODE
                        | NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_IMAGE_MODE) != null;
    }

    public boolean initializeEffectSdkForActivity(android.app.Activity activity) {
        MeisheThreading.requireMainThread("NvsEffectSdkContext.init");
        if (activity == null) {
            return false;
        }
        if (NvsEffectSdkContext.getInstance() != null) {
            return true;
        }
        return NvsEffectSdkContext.init(activity, "assets:/meishesdk.lic") != null;
    }

    public boolean initializeEffectSdkForActivityWithFlags(
            android.app.Activity activity,
            int flags) {
        MeisheThreading.requireMainThread("NvsEffectSdkContext.init");
        if (activity == null) {
            return false;
        }
        if (NvsEffectSdkContext.getInstance() != null) {
            return true;
        }
        return NvsEffectSdkContext.init(activity, "assets:/meishesdk.lic", flags) != null;
    }

    public boolean initializeMsHumanDetectionModels(
            Context context,
            boolean useFace240Model,
            boolean initializeOptionalModels) {
        MeisheThreading.requireMainThread("initHumanDetection");
        if (context == null || streamingContext == null || NvsStreamingContext.hasARModule() != 1) {
            return false;
        }
        Context appContext = context.getApplicationContext();
        String faceModelPath = "assets:/facemode/ms/" + (useFace240Model ? FACE_240_MODEL : FACE_106_MODEL);
        int faceFlags = NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_LANDMARK
                | NvsStreamingContext.HUMAN_DETECTION_FEATURE_FACE_ACTION
                | NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE;
        boolean faceInitialized = NvsStreamingContext.initHumanDetection(appContext, faceModelPath, "", faceFlags);
        if (NvsEffectSdkContext.getInstance() != null) {
            NvsEffectSdkContext.initHumanDetection(appContext, faceModelPath, "", faceFlags);
        }
        if (initializeOptionalModels) {
            initializeOptionalHumanDetectionModels(appContext);
        }
        return faceInitialized;
    }

    private void initializeOptionalHumanDetectionModels(Context appContext) {
        setupHumanData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON,
                NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_FACE_COMMON,
                "assets:/facemode/common/" + FACE_COMMON_DAT);
        setupHumanData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY,
                NvsEffectSdkContext.HUMAN_DETECTION_DATA_TYPE_ADVANCED_BEAUTY,
                "assets:/facemode/common/" + ADVANCED_BEAUTY_DAT);
        setupHumanData(NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE,
                NvsStreamingContext.HUMAN_DETECTION_DATA_TYPE_FAKE_FACE,
                "assets:/facemode/common/" + FAKE_FACE_DAT);

        String segmentationModel = streamingContext.getDeviceCpuLevel() == NvsStreamingContext.DEVICE_POWER_LEVEL_LOW
                ? HUMAN_SEGMENT_SMALL_MODEL
                : HUMAN_SEGMENT_MEDIUM_MODEL;
        initHumanDetectionExt(appContext,
                "assets:/facemode/common/" + segmentationModel,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_BACKGROUND);
        initHumanDetectionExt(appContext,
                "assets:/facemode/common/" + HAND_MODEL,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_LANDMARK
                        | NvsStreamingContext.HUMAN_DETECTION_FEATURE_HAND_ACTION);
        initHumanDetectionExt(appContext,
                "assets:/facemode/common/" + EYE_CONTOUR_MODEL,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK
                        | NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEMI_IMAGE_MODE,
                NvsEffectSdkContext.HUMAN_DETECTION_FEATURE_EYEBALL_LANDMARK);
        initHumanDetectionExt(appContext,
                "assets:/facemode/common/" + AVATAR_MODEL,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_AVATAR_EXPRESSION);
        NvsStreamingContext.initHumanDetectionExt(appContext,
                "assets:/facemode/common/" + SKY_SEGMENT_MODEL,
                null,
                NvsStreamingContext.HUMAN_DETECTION_FEATURE_SEGMENTATION_SKY);
    }

    private void setupHumanData(int streamingDataType, int effectDataType, String assetPath) {
        NvsStreamingContext.setupHumanDetectionData(streamingDataType, assetPath);
        if (NvsEffectSdkContext.getInstance() != null) {
            NvsEffectSdkContext.setupHumanDetectionData(effectDataType, assetPath);
        }
    }

    private void initHumanDetectionExt(Context appContext, String modelPath, int featureFlags) {
        initHumanDetectionExt(appContext, modelPath, featureFlags, featureFlags);
    }

    private void initHumanDetectionExt(
            Context appContext,
            String modelPath,
            int streamingFeatureFlags,
            int effectFeatureFlags) {
        NvsStreamingContext.initHumanDetectionExt(appContext, modelPath, null, streamingFeatureFlags);
        if (NvsEffectSdkContext.getInstance() != null) {
            NvsEffectSdkContext.initHumanDetectionExt(appContext, modelPath, null, effectFeatureFlags);
        }
    }

    public NvsCaptureVideoFx appendBeautyCaptureFx() {
        MeisheThreading.requireMainThread("appendBeautyCaptureVideoFx");
        if (streamingContext == null) {
            return null;
        }
        return streamingContext.appendBeautyCaptureVideoFx();
    }

    public NvsCaptureVideoFx appendCaptureBuiltinFx(String fxName) {
        MeisheThreading.requireMainThread("appendBuiltinCaptureVideoFx");
        if (streamingContext == null || fxName == null || fxName.isEmpty()) {
            return null;
        }
        return streamingContext.appendBuiltinCaptureVideoFx(fxName);
    }

    public NvsCaptureVideoFx appendCapturePackagedFx(String packageId) {
        MeisheThreading.requireMainThread("appendPackagedCaptureVideoFx");
        if (streamingContext == null || packageId == null || packageId.isEmpty()) {
            return null;
        }
        return streamingContext.appendPackagedCaptureVideoFx(packageId);
    }

    public NvsCaptureVideoFx appendArSceneCaptureFx(boolean singleBufferMode) {
        MeisheThreading.requireMainThread("appendBuiltinCaptureVideoFx");
        if (streamingContext == null || NvsStreamingContext.hasARModule() != 1) {
            return null;
        }
        NvsCaptureVideoFx arSceneFx = streamingContext.appendBuiltinCaptureVideoFx(AR_SCENE);
        if (arSceneFx != null) {
            arSceneFx.setBooleanVal(MAX_FACES_RESPECT_MIN, true);
            if (streamingContext.isAndroidCameraPreferDualBufferAR()) {
                arSceneFx.setBooleanVal(SINGLE_BUFFER_MODE, false);
            } else {
                arSceneFx.setBooleanVal(SINGLE_BUFFER_MODE, singleBufferMode);
            }
            enableAIFaceOcclusionIfHighPower(arSceneFx);
        }
        return arSceneFx;
    }

    public boolean configureArBeauty(NvsCaptureVideoFx arSceneFx, double strength, double whitening) {
        MeisheThreading.requireMainThread("configure AR Scene beauty");
        if (arSceneFx == null) {
            return false;
        }
        arSceneFx.setBooleanVal("Beauty Effect", true);
        arSceneFx.setFloatVal("Beauty Strength", Math.max(0.0, Math.min(1.0, strength)));
        arSceneFx.setFloatVal("Beauty Whitening", Math.max(0.0, Math.min(1.0, whitening)));
        return true;
    }

    public boolean applyArScenePackage(NvsCaptureVideoFx arSceneFx, String packageId) {
        MeisheThreading.requireMainThread("apply AR Scene package");
        if (arSceneFx == null || packageId == null) {
            return false;
        }
        arSceneFx.setStringVal("Scene Id", packageId);
        return packageId.equals(arSceneFx.getStringVal("Scene Id"));
    }

    public String getArScenePackagePrompt(String packageId) {
        MeisheThreading.requireMainThread("NvsAssetPackageManager.getARSceneAssetPackagePrompt");
        if (streamingContext == null || packageId == null || packageId.isEmpty()
                || streamingContext.getAssetPackageManager() == null) {
            return "";
        }
        String prompt = streamingContext.getAssetPackageManager()
                .getARSceneAssetPackagePrompt(packageId);
        return prompt == null ? "" : prompt;
    }

    public boolean applyEyebrowAngleFaceMeshPackage(
            NvsCaptureVideoFx arSceneFx,
            String packageId,
            double degree) {
        MeisheThreading.requireMainThread("apply face mesh package");
        if (arSceneFx == null || packageId == null || packageId.isEmpty()) {
            return false;
        }
        arSceneFx.setBooleanVal("Beauty Shape", true);
        arSceneFx.setBooleanVal("Face Mesh Internal Enabled", true);
        arSceneFx.setStringVal(
                "Face Mesh Eyebrow Angle Custom Package Id",
                packageId);
        arSceneFx.setFloatVal(
                "Face Mesh Eyebrow Angle Degree",
                Math.max(-1.0, Math.min(1.0, degree)));
        return packageId.equals(arSceneFx.getStringVal(
                "Face Mesh Eyebrow Angle Custom Package Id"));
    }

    public void clearFaceMeshPackage(NvsCaptureVideoFx arSceneFx) {
        MeisheThreading.requireMainThread("clear face mesh package");
        if (arSceneFx == null) {
            return;
        }
        arSceneFx.setStringVal(EYEBROW_ANGLE_PACKAGE_ID, "");
        arSceneFx.setFloatVal(EYEBROW_ANGLE_DEGREE, 0.0);
    }

    public NvsCaptureVideoFx appendSegmentationBackgroundFx(NvsColor backgroundColor) {
        MeisheThreading.requireMainThread("append segmentation background capture FX");
        if (streamingContext == null || NvsStreamingContext.hasARModule() != 1) {
            return null;
        }
        NvsCaptureVideoFx segmentationFx = streamingContext.appendBuiltinCaptureVideoFx(
                "Segmentation Background Fill");
        if (segmentationFx == null) {
            return null;
        }
        segmentationFx.setMenuVal("Segment Type", "Background");
        segmentationFx.setIntVal("Stretch Mode", 1);
        if (backgroundColor != null) {
            segmentationFx.setColorVal("Background Color", backgroundColor);
        }
        return segmentationFx;
    }

    public void enableAIFaceOcclusionIfHighPower(NvsFx arSceneFx) {
        MeisheThreading.requireMainThread("AI Face Occlusion Enabled");
        if (streamingContext == null || arSceneFx == null) {
            return;
        }
        if (streamingContext.getDeviceCpuLevel() == NvsStreamingContext.DEVICE_POWER_LEVEL_HIGH) {
            arSceneFx.setBooleanVal(AI_FACE_OCCLUSION_ENABLED, true);
        }
    }

    public void setFloat(NvsFx fx, String key, double value) {
        MeisheThreading.requireMainThread("NvsFx.setFloatVal");
        if (fx != null && key != null && !key.isEmpty()) {
            fx.setFloatVal(key, value);
        }
    }

    public void setBoolean(NvsFx fx, String key, boolean value) {
        MeisheThreading.requireMainThread("NvsFx.setBooleanVal");
        if (fx != null && key != null && !key.isEmpty()) {
            fx.setBooleanVal(key, value);
        }
    }

    public boolean initializeHumanDetection(
            Context context,
            String mainModelPath,
            String extensionModelPath,
            String dataPath,
            int featureFlags,
            int dataType) {
        MeisheThreading.requireMainThread("initialize human detection");
        if (context == null || mainModelPath == null || mainModelPath.isEmpty()) {
            return false;
        }
        Context appContext = context.getApplicationContext();
        if (!NvsStreamingContext.initHumanDetection(
                appContext,
                mainModelPath,
                "",
                featureFlags)) {
            return false;
        }
        if (extensionModelPath != null && !extensionModelPath.isEmpty()
                && !NvsStreamingContext.initHumanDetectionExt(
                appContext,
                extensionModelPath,
                null,
                featureFlags)) {
            return false;
        }
        return dataPath == null || dataPath.isEmpty()
                || NvsStreamingContext.setupHumanDetectionData(dataType, dataPath);
    }

    public boolean initializeStreamingHumanDetectionWithOptions(
            Context context,
            String modelFilePath,
            String licenseFilePath,
            int features,
            Hashtable<String, Object> options) {
        MeisheThreading.requireMainThread("NvsStreamingContext.initHumanDetection");
        if (context == null || modelFilePath == null || modelFilePath.isEmpty()) {
            return false;
        }
        return NvsStreamingContext.initHumanDetection(
                context.getApplicationContext(),
                modelFilePath,
                licenseFilePath,
                features,
                options == null ? new Hashtable<String, Object>() : options);
    }

    public boolean initializeStreamingHumanDetectionExtWithOptions(
            Context context,
            String modelFilePath,
            String licenseFilePath,
            int features,
            Hashtable<String, Object> options) {
        MeisheThreading.requireMainThread("NvsStreamingContext.initHumanDetectionExt");
        if (context == null || modelFilePath == null || modelFilePath.isEmpty()) {
            return false;
        }
        return NvsStreamingContext.initHumanDetectionExt(
                context.getApplicationContext(),
                modelFilePath,
                licenseFilePath,
                features,
                options == null ? new Hashtable<String, Object>() : options);
    }

    public boolean initializeEffectHumanDetectionExtWithOptions(
            Context context,
            String modelFilePath,
            String licenseFilePath,
            int features,
            Hashtable<String, Object> options) {
        MeisheThreading.requireMainThread("NvsEffectSdkContext.initHumanDetectionExt");
        if (context == null || modelFilePath == null || modelFilePath.isEmpty()
                || NvsEffectSdkContext.getInstance() == null) {
            return false;
        }
        return NvsEffectSdkContext.initHumanDetectionExt(
                context.getApplicationContext(),
                modelFilePath,
                licenseFilePath,
                features,
                options == null ? new Hashtable<String, Object>() : options);
    }

    public void releaseHumanDetection() {
        MeisheThreading.requireMainThread("NvsStreamingContext.closeHumanDetection");
        NvsStreamingContext.closeHumanDetection();
    }

    public NvsVideoFx applyCompoundMakeup(NvsVideoClip clip, String makeupPackageId) {
        MeisheThreading.requireMainThread("apply compound makeup to clip AR Scene");
        if (clip == null || makeupPackageId == null || makeupPackageId.isEmpty()) {
            return null;
        }
        NvsVideoFx arSceneFx = null;
        for (int index = 0; index < clip.getFxCount(); index++) {
            NvsVideoFx candidate = clip.getFxByIndex(index);
            if (candidate != null && "AR Scene".equals(candidate.getBuiltinVideoFxName())) {
                arSceneFx = candidate;
                break;
            }
        }
        if (arSceneFx == null) {
            arSceneFx = clip.appendBuiltinFx("AR Scene");
        }
        if (arSceneFx != null) {
            arSceneFx.setStringVal("Makeup Compound Package Id", makeupPackageId);
        }
        return arSceneFx;
    }

    public boolean configureMakeupPart(
            NvsFx arSceneFx,
            String makeupType,
            String packageId,
            double intensity) {
        MeisheThreading.requireMainThread("configure single makeup package");
        if (arSceneFx == null || makeupType == null || makeupType.trim().isEmpty()
                || packageId == null) {
            return false;
        }
        String normalizedType = makeupType.trim();
        arSceneFx.setBooleanVal("Makeup Enabled", true);
        arSceneFx.setIntVal(
                "Makeup Custom Enabled Flag",
                NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_ALL);
        arSceneFx.setStringVal("Makeup " + normalizedType + " Package Id", packageId);
        arSceneFx.setFloatVal(
                "Makeup " + normalizedType + " Intensity",
                Math.max(0.0, Math.min(1.0, intensity)));
        return true;
    }

    public void clearMakeupPart(NvsFx arSceneFx, String makeupType) {
        MeisheThreading.requireMainThread("clear single makeup package");
        if (arSceneFx == null || makeupType == null || makeupType.trim().isEmpty()) {
            return;
        }
        String normalizedType = makeupType.trim();
        arSceneFx.setStringVal("Makeup " + normalizedType + " Package Id", "");
        arSceneFx.setFloatVal("Makeup " + normalizedType + " Intensity", 0.0);
        arSceneFx.setBooleanVal("Makeup Enabled", false);
        arSceneFx.setIntVal(
                "Makeup Custom Enabled Flag",
                NvsMakeupEffectInfo.MAKEUP_EFFECT_CUSTOM_ENABLED_FLAG_NONE);
    }

    public NvsCaptureVideoFx appendCaptureSceneKeyer(NvsStreamingContext streamingContext) {
        MeisheThreading.requireMainThread("append Master Keyer capture FX");
        if (streamingContext == null) {
            return null;
        }
        NvsCaptureVideoFx keyerFx = streamingContext.appendBuiltinCaptureVideoFx("Master Keyer");
        if (keyerFx != null) {
            keyerFx.setBooleanVal("Spill Removal", true);
            keyerFx.setFloatVal("Spill Removal Intensity", 0.0);
            keyerFx.setFloatVal("Shrink Intensity", 0.4);
        }
        return keyerFx;
    }

    public boolean applyCaptureScene(
            NvsStreamingContext streamingContext,
            String installedCaptureSceneId) {
        MeisheThreading.requireMainThread("apply capture scene package");
        if (streamingContext == null || installedCaptureSceneId == null
                || installedCaptureSceneId.isEmpty()) {
            return false;
        }
        return streamingContext.applyCaptureScene(installedCaptureSceneId);
    }

    public void removeCaptureScene() {
        MeisheThreading.requireMainThread("NvsStreamingContext.removeCurrentCaptureScene");
        if (streamingContext != null) {
            streamingContext.removeCurrentCaptureScene();
        }
    }

    public NvsTimeline createSuperZoomPreviewTimeline(
            NvsStreamingContext streamingContext,
            String renderedVideoPath,
            NvsVideoResolution videoResolution,
            NvsRational videoFps,
            NvsAudioResolution audioResolution) {
        MeisheThreading.requireMainThread("create SuperZoom output timeline");
        if (streamingContext == null || renderedVideoPath == null || renderedVideoPath.isEmpty()
                || videoResolution == null || videoFps == null || audioResolution == null) {
            return null;
        }
        NvsTimeline outputTimeline = streamingContext.createTimeline(
                videoResolution,
                videoFps,
                audioResolution);
        if (outputTimeline == null) {
            return null;
        }
        NvsVideoTrack videoTrack = outputTimeline.appendVideoTrack();
        if (videoTrack == null || videoTrack.appendClip(renderedVideoPath) == null) {
            streamingContext.removeTimeline(outputTimeline);
            return null;
        }
        return outputTimeline;
    }

    public NvsCaptureVideoFx appendBeautyCaptureFx(NvsStreamingContext streamingContext) {
        MeisheThreading.requireMainThread("NvsStreamingContext.appendBeautyCaptureVideoFx");
        return streamingContext == null ? null : streamingContext.appendBeautyCaptureVideoFx();
    }

    public boolean configureArSceneManipulation(
            NvsFx arSceneFx,
            int detectionMode,
            boolean automaticProbe,
            NvsARSceneManipulate.NvsARSceneManipulateCallback callback) {
        MeisheThreading.requireMainThread("configure AR scene manipulation");
        if (arSceneFx == null || callback == null) {
            return false;
        }
        NvsARSceneManipulate manipulate = arSceneFx.getARSceneManipulate();
        if (manipulate == null) {
            return false;
        }
        manipulate.setARSceneCallback(callback);
        manipulate.setDetectionMode(detectionMode);
        manipulate.setDetectionAutoProbe(automaticProbe);
        return manipulate.isFunctionAvailable(NvsARSceneManipulate.CheckedFunctionType_Matte);
    }
}
