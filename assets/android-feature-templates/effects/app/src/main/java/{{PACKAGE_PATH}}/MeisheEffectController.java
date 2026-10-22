package {{PACKAGE_NAME}};

import android.graphics.RectF;

import com.meicam.sdk.NvsCaptureVideoFx;
import com.meicam.sdk.NvsColor;
import com.meicam.sdk.NvsFx;
import com.meicam.sdk.NvsMaskRegionInfo;
import com.meicam.sdk.NvsParticleSystemContext;
import com.meicam.sdk.NvsPosition2D;
import com.meicam.sdk.NvsPosition3D;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsTimelineVideoFx;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoFx;
import com.meicam.sdk.NvsVideoTrack;
import com.meicam.sdk.NvsVideoTransition;

import java.util.ArrayList;
import java.util.List;

public final class MeisheEffectController {
    public NvsTimelineVideoFx addBuiltinTimelineFx(
            NvsTimeline timeline,
            long inPointUs,
            long durationUs,
            String fxName) {
        MeisheThreading.requireMainThread("addBuiltinTimelineVideoFx");
        if (timeline == null || fxName == null || fxName.isEmpty() || durationUs <= 0) {
            return null;
        }
        return timeline.addBuiltinTimelineVideoFx(Math.max(0, inPointUs), durationUs, fxName);
    }

    public NvsTimelineVideoFx addPackagedTimelineFx(
            NvsTimeline timeline,
            long inPointUs,
            long durationUs,
            String packageId) {
        MeisheThreading.requireMainThread("addPackagedTimelineVideoFx");
        if (timeline == null || packageId == null || packageId.isEmpty() || durationUs <= 0) {
            return null;
        }
        return timeline.addPackagedTimelineVideoFx(Math.max(0, inPointUs), durationUs, packageId);
    }

    public NvsVideoFx appendBuiltinClipFx(NvsVideoClip clip, String fxName) {
        MeisheThreading.requireMainThread("appendBuiltinFx");
        if (clip == null || fxName == null || fxName.isEmpty()) {
            return null;
        }
        return clip.appendBuiltinFx(fxName);
    }

    public NvsVideoFx appendBuiltinClipFxInRange(
            NvsVideoClip clip,
            String fxName,
            long inPointUs,
            long durationUs) {
        MeisheThreading.requireMainThread("NvsVideoClip.appendBuiltinFx");
        if (clip == null || fxName == null || fxName.isEmpty() || inPointUs < 0
                || durationUs == 0 || durationUs < -1) {
            return null;
        }
        return clip.appendBuiltinFx(fxName, inPointUs, durationUs);
    }

    public NvsVideoFx appendPackagedClipFx(NvsVideoClip clip, String packageId) {
        MeisheThreading.requireMainThread("appendPackagedFx");
        if (clip == null || packageId == null || packageId.isEmpty()) {
            return null;
        }
        return clip.appendPackagedFx(packageId);
    }

    public NvsVideoFx appendPackagedClipFxInRange(
            NvsVideoClip clip,
            String packageId,
            long inPointUs,
            long durationUs) {
        MeisheThreading.requireMainThread("NvsVideoClip.appendPackagedFx");
        if (clip == null || packageId == null || packageId.isEmpty() || inPointUs < 0
                || durationUs == 0 || durationUs < -1) {
            return null;
        }
        return clip.appendPackagedFx(packageId, inPointUs, durationUs);
    }

    public void removeTimelineFx(NvsTimeline timeline, NvsTimelineVideoFx fx) {
        MeisheThreading.requireMainThread("removeTimelineVideoFx");
        if (timeline != null && fx != null) {
            timeline.removeTimelineVideoFx(fx);
        }
    }

    public void setFloat(NvsFx fx, String key, double value) {
        MeisheThreading.requireMainThread("NvsFx.setFloatVal");
        if (fx != null && key != null && !key.isEmpty()) {
            fx.setFloatVal(key, value);
        }
    }

    public void setString(NvsFx fx, String key, String value) {
        MeisheThreading.requireMainThread("NvsFx.setStringVal");
        if (fx != null && key != null && !key.isEmpty() && value != null) {
            fx.setStringVal(key, value);
        }
    }

    public void setBoolean(NvsFx fx, String key, boolean value) {
        MeisheThreading.requireMainThread("NvsFx.setBooleanVal");
        if (fx != null && key != null && !key.isEmpty()) {
            fx.setBooleanVal(key, value);
        }
    }

    public NvsVideoFx appendRawBuiltinClipFx(NvsVideoClip clip, String fxName) {
        MeisheThreading.requireMainThread("NvsVideoClip.appendRawBuiltinFx");
        if (clip == null || fxName == null || fxName.isEmpty()) {
            return null;
        }
        return clip.appendRawBuiltinFx(fxName);
    }

    public NvsVideoFx appendRawBuiltinClipFxInRange(
            NvsVideoClip clip,
            String fxName,
            long inPointUs,
            long durationUs) {
        MeisheThreading.requireMainThread("NvsVideoClip.appendRawBuiltinFx");
        if (clip == null || fxName == null || fxName.isEmpty() || inPointUs < 0
                || durationUs == 0 || durationUs < -1) {
            return null;
        }
        return clip.appendRawBuiltinFx(fxName, inPointUs, durationUs);
    }

    public List<String> listBuiltinClipFxNames(NvsVideoClip clip) {
        MeisheThreading.requireMainThread("inspect NvsVideoClip FX");
        List<String> names = new ArrayList<>();
        if (clip == null) {
            return names;
        }
        for (int index = 0; index < clip.getFxCount(); index++) {
            NvsVideoFx fx = clip.getFxByIndex(index);
            if (fx != null && fx.getBuiltinVideoFxName() != null) {
                names.add(fx.getBuiltinVideoFxName());
            }
        }
        for (int index = 0; index < clip.getRawFxCount(); index++) {
            NvsVideoFx fx = clip.getRawFxByIndex(index);
            if (fx != null && fx.getBuiltinVideoFxName() != null) {
                names.add(fx.getBuiltinVideoFxName());
            }
        }
        return names;
    }

    public NvsTimelineVideoFx getFirstTimelineFx(NvsTimeline timeline) {
        MeisheThreading.requireMainThread("NvsTimeline.getFirstTimelineVideoFx");
        return timeline == null ? null : timeline.getFirstTimelineVideoFx();
    }

    public NvsVideoTransition setBuiltinTransition(
            NvsVideoTrack track,
            int sourceClipIndex,
            String transitionName) {
        MeisheThreading.requireMainThread("NvsVideoTrack.setBuiltinTransition");
        if (track == null || sourceClipIndex < 0 || transitionName == null) {
            return null;
        }
        return track.setBuiltinTransition(sourceClipIndex, transitionName);
    }

    public NvsVideoTransition setPackagedTransition(
            NvsVideoTrack track,
            int sourceClipIndex,
            String packageId) {
        MeisheThreading.requireMainThread("NvsVideoTrack.setPackagedTransition");
        if (track == null || sourceClipIndex < 0 || packageId == null || packageId.isEmpty()) {
            return null;
        }
        return track.setPackagedTransition(sourceClipIndex, packageId);
    }

    public NvsVideoTransition getTransition(NvsVideoTrack track, int sourceClipIndex) {
        MeisheThreading.requireMainThread("NvsVideoTrack.getTransitionBySourceClipIndex");
        if (track == null || sourceClipIndex < 0) {
            return null;
        }
        return track.getTransitionBySourceClipIndex(sourceClipIndex);
    }

    public void configureImageMotion(
            NvsVideoClip clip,
            int motionMode,
            float pan,
            float scan,
            boolean animationEnabled) {
        MeisheThreading.requireMainThread("configure image motion");
        if (clip == null) {
            return;
        }
        clip.setImageMotionMode(motionMode);
        clip.setPanAndScan(pan, scan);
        clip.setImageMotionAnimationEnabled(animationEnabled);
    }

    public boolean isAudioVideoClip(NvsVideoClip clip) {
        MeisheThreading.requireMainThread("NvsVideoClip.getVideoType");
        return clip != null && clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_AV;
    }

    public NvsVideoFx applyMaskRegion(
            NvsVideoClip clip,
            NvsMaskRegionInfo regionInfo,
            double featherWidth,
            boolean inverseRegion) {
        MeisheThreading.requireMainThread("apply Mask Generator region");
        if (clip == null || regionInfo == null) {
            return null;
        }
        NvsVideoFx maskFx = null;
        for (int index = 0; index < clip.getRawFxCount(); index++) {
            NvsVideoFx candidate = clip.getRawFxByIndex(index);
            if (candidate != null && "Mask Generator".equals(candidate.getBuiltinVideoFxName())
                    && "mask".equals(candidate.getAttachment("Meishe Mask Role"))) {
                maskFx = candidate;
                break;
            }
        }
        if (maskFx == null) {
            maskFx = clip.appendRawBuiltinFx("Mask Generator");
            if (maskFx == null) {
                return null;
            }
            maskFx.setAttachment("Meishe Mask Role", "mask");
        }
        maskFx.setFloatVal("Feather Width", Math.max(0.0, featherWidth));
        maskFx.setBooleanVal("Inverse Region", inverseRegion);
        maskFx.setBooleanVal("Keep RGB", true);
        maskFx.setStringVal("Description String", "");
        maskFx.setArbDataVal("Region Info", regionInfo);
        return maskFx;
    }

    public NvsVideoFx applySolidBackground(
            NvsVideoClip clip,
            NvsColor color,
            double scaleX,
            double scaleY,
            double translationX,
            double translationY,
            double rotation) {
        MeisheThreading.requireMainThread("configure clip property background");
        if (clip == null || color == null || scaleX <= 0 || scaleY <= 0) {
            return null;
        }
        clip.enablePropertyVideoFx(true);
        NvsVideoFx backgroundFx = clip.getPropertyVideoFx();
        if (backgroundFx == null) {
            return null;
        }
        backgroundFx.setMenuVal("Background Mode", "Color Solid");
        backgroundFx.setStringVal("Background Image", "");
        backgroundFx.setColorVal("Background Color", color);
        backgroundFx.setFloatVal("Scale X", scaleX);
        backgroundFx.setFloatVal("Scale Y", scaleY);
        backgroundFx.setFloatVal("Trans X", translationX);
        backgroundFx.setFloatVal("Trans Y", translationY);
        backgroundFx.setFloatVal("Rotation", rotation);
        return backgroundFx;
    }

    public boolean addTimelineWatermark(
            NvsTimeline timeline,
            String imagePath,
            int imageWidth,
            int imageHeight,
            float opacity,
            int position,
            int marginX,
            int marginY) {
        MeisheThreading.requireMainThread("NvsTimeline.addWatermark");
        if (timeline == null || imagePath == null || imagePath.isEmpty()
                || imageWidth <= 0 || imageHeight <= 0 || opacity < 0f || opacity > 1f
                || marginX < 0 || marginY < 0) {
            return false;
        }
        timeline.deleteWatermark();
        return timeline.addWatermark(
                imagePath,
                imageWidth,
                imageHeight,
                opacity,
                position,
                marginX,
                marginY);
    }

    public NvsTimelineVideoFx addParticleFx(
            NvsTimeline timeline,
            long inPointUs,
            long durationUs,
            String packageId,
            double tailFadingSeconds) {
        MeisheThreading.requireMainThread("add packaged particle timeline FX");
        if (timeline == null || packageId == null || packageId.isEmpty()
                || inPointUs < 0 || durationUs <= 0 || tailFadingSeconds < 0) {
            return null;
        }
        NvsTimelineVideoFx particleFx = timeline.addPackagedTimelineVideoFx(
                inPointUs,
                durationUs,
                packageId);
        if (particleFx != null) {
            particleFx.setFloatVal("Tail Fading Duration", tailFadingSeconds);
        }
        return particleFx;
    }

    public NvsCaptureVideoFx appendGlitterCaptureFx(
            NvsStreamingContext streamingContext,
            String sourcePath,
            double quantity) {
        MeisheThreading.requireMainThread("append Glitter capture FX");
        if (streamingContext == null || sourcePath == null || sourcePath.isEmpty()) {
            return null;
        }
        NvsCaptureVideoFx glitterFx = streamingContext.appendBuiltinCaptureVideoFx("Glitter");
        if (glitterFx != null) {
            glitterFx.setStringVal("Source Path", sourcePath);
            glitterFx.setFloatVal("Quantity", Math.max(0.0, Math.min(1.0, quantity)));
        }
        return glitterFx;
    }

    public boolean configureAdvancedClipPlayback(
            NvsVideoClip clip,
            double startSpeed,
            double endSpeed,
            boolean keepAudioPitch,
            int extraRotation,
            boolean playInReverse,
            boolean softwareDecoding,
            boolean disableAmbiguousCrop,
            boolean rawSourceMode,
            int wrapMode,
            int backgroundMode) {
        MeisheThreading.requireMainThread("configure advanced clip playback");
        if (clip == null || startSpeed <= 0 || endSpeed <= 0) {
            return false;
        }
        clip.changeVariableSpeed(startSpeed, endSpeed, keepAudioPitch);
        clip.setExtraVideoRotation(extraRotation);
        clip.setPlayInReverse(playInReverse);
        clip.setSoftWareDecoding(softwareDecoding);
        clip.disableAmbiguousCrop(disableAmbiguousCrop);
        clip.enableRawSourceMode(rawSourceMode);
        clip.setClipWrapMode(wrapMode);
        clip.setSourceBackgroundMode(backgroundMode);
        return clip.getExtraVideoRotation() == extraRotation
                && clip.getPlayInReverse() == playInReverse
                && clip.isAmbiguousCropDisabled() == disableAmbiguousCrop
                && clip.getClipWrapMode() == wrapMode
                && clip.getSourceBackgroundMode() == backgroundMode;
    }

    public boolean configureClipImageRegions(
            NvsVideoClip clip,
            RectF startRoi,
            RectF endRoi,
            RectF maskRoi) {
        MeisheThreading.requireMainThread("configure clip image regions");
        if (clip == null || startRoi == null || endRoi == null || maskRoi == null
                || startRoi.isEmpty() || endRoi.isEmpty() || maskRoi.isEmpty()) {
            return false;
        }
        clip.setImageMotionROI(startRoi, endRoi);
        clip.setImageMaskROI(maskRoi);
        return clip.getStartROI() != null
                && clip.getEndROI() != null
                && clip.getImageMaskROI() != null;
    }

    public boolean setFloatKeyframe(
            NvsFx fx,
            String parameterKey,
            double value,
            long keyframeTimeUs) {
        MeisheThreading.requireMainThread("configure FX keyframe");
        if (fx == null || parameterKey == null || parameterKey.isEmpty()
                || !Double.isFinite(value) || keyframeTimeUs < 0) {
            return false;
        }
        fx.setFloatValAtTime(parameterKey, value, keyframeTimeUs);
        return fx.hasKeyframeList(parameterKey)
                && Double.isFinite(fx.getFloatValAtTime(parameterKey, keyframeTimeUs));
    }

    public boolean removeNearestKeyframe(
            NvsFx fx,
            String parameterKey,
            long inputTimeUs,
            int findMode) {
        MeisheThreading.requireMainThread("remove FX keyframe");
        if (fx == null || parameterKey == null || parameterKey.isEmpty() || inputTimeUs < 0) {
            return false;
        }
        long keyframeTimeUs = fx.findKeyframeTime(parameterKey, inputTimeUs, findMode);
        return keyframeTimeUs >= 0 && fx.removeKeyframeAtTime(parameterKey, keyframeTimeUs);
    }

    public boolean setPositionParameters(
            NvsFx fx,
            String position2DKey,
            NvsPosition2D position2D,
            String position3DKey,
            NvsPosition3D position3D) {
        MeisheThreading.requireMainThread("configure FX positions");
        if (fx == null || position2DKey == null || position2DKey.isEmpty()
                || position2D == null || position3DKey == null || position3DKey.isEmpty()
                || position3D == null) {
            return false;
        }
        fx.setPosition2DVal(position2DKey, position2D);
        fx.setPosition3DVal(position3DKey, position3D);
        return fx.getPosition2DVal(position2DKey) != null
                && fx.getPosition3DVal(position3DKey) != null;
    }

    public boolean configureTransitionTiming(
            NvsVideoTransition transition,
            long durationUs,
            int durationMatchMode,
            float durationScale,
            boolean enabled) {
        MeisheThreading.requireMainThread("configure video transition timing");
        if (transition == null || durationUs <= 0 || durationScale <= 0) {
            return false;
        }
        transition.enableTimelineTransition(enabled);
        transition.setVideoTransitionDuration(durationUs, durationMatchMode);
        transition.setVideoTransitionDurationScaleFactor(durationScale);
        return transition.getVideoTransitionDuration() > 0
                && transition.getVideoTransitionDurationMatchMode() == durationMatchMode;
    }

    public boolean configureParticleEmitter(
            NvsParticleSystemContext particleContext,
            String emitterName,
            float rateGain,
            float sizeGain,
            float x,
            float y,
            float z) {
        MeisheThreading.requireMainThread("configure particle emitter");
        if (particleContext == null || emitterName == null || emitterName.isEmpty()
                || rateGain < 0 || sizeGain < 0) {
            return false;
        }
        particleContext.setEmitterRateGain(emitterName, rateGain);
        particleContext.setEmitterParticleSizeGain(emitterName, sizeGain);
        particleContext.appendPositionToEmitterPositionCurve(emitterName, x, y, z);
        return true;
    }
}
