package {{PACKAGE_NAME}};

import android.graphics.RectF;
import android.util.Log;

import com.meicam.sdk.NvsCaptureVideoFx;
import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsStreamingContext;

import java.util.ArrayList;
import java.util.List;

public final class MeisheCaptureController {
    private static final String TAG = "MeisheCapture";

    private final NvsStreamingContext streamingContext;
    private final NvsLiveWindow liveWindow;

    public MeisheCaptureController(NvsStreamingContext streamingContext, NvsLiveWindow liveWindow) {
        this.streamingContext = streamingContext;
        this.liveWindow = liveWindow;
    }

    public boolean startPreview(int preferredDeviceIndex) {
        MeisheThreading.requireMainThread("startCapturePreview");
        if (streamingContext == null || liveWindow == null) {
            return false;
        }
        int deviceCount = streamingContext.getCaptureDeviceCount();
        if (deviceCount <= 0) {
            Log.e(TAG, "No camera device available");
            return false;
        }
        if (!streamingContext.connectCapturePreviewWithLiveWindow(liveWindow)) {
            Log.e(TAG, "Failed to connect capture preview");
            return false;
        }
        int deviceIndex = Math.min(
                Math.max(preferredDeviceIndex, 0),
                deviceCount - 1);
        int flags = NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER
                | NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME
                | NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_ENABLE_TAKE_PICTURE
                | NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE;
        return streamingContext.startCapturePreview(
                deviceIndex,
                NvsStreamingContext.VIDEO_CAPTURE_RESOLUTION_GRADE_HIGH,
                flags,
                null);
    }

    public int resolveDeviceIndex(int preferredDeviceIndex) {
        MeisheThreading.requireMainThread("resolve capture device index");
        if (streamingContext == null || streamingContext.getCaptureDeviceCount() <= 0) {
            return -1;
        }
        return Math.min(
                Math.max(preferredDeviceIndex, 0),
                streamingContext.getCaptureDeviceCount() - 1);
    }

    public int getDeviceCount() {
        MeisheThreading.requireMainThread("NvsStreamingContext.getCaptureDeviceCount");
        return streamingContext == null ? 0 : streamingContext.getCaptureDeviceCount();
    }

    public boolean isBackFacing(int deviceIndex) {
        MeisheThreading.requireMainThread("NvsStreamingContext.isCaptureDeviceBackFacing");
        return streamingContext != null
                && deviceIndex >= 0
                && deviceIndex < streamingContext.getCaptureDeviceCount()
                && streamingContext.isCaptureDeviceBackFacing(deviceIndex);
    }

    public boolean startRecording(String outputPath) {
        MeisheThreading.requireMainThread("startRecording");
        if (streamingContext == null || outputPath == null || outputPath.isEmpty()) {
            return false;
        }
        if (streamingContext.getStreamingEngineState()
                == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
            return true;
        }
        return streamingContext.startRecording(outputPath);
    }

    public void stopRecording() {
        MeisheThreading.requireMainThread("stopRecording");
        if (streamingContext != null && streamingContext.getStreamingEngineState()
                == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
            streamingContext.stopRecording();
        }
    }

    public boolean pauseRecording() {
        MeisheThreading.requireMainThread("NvsStreamingContext.pauseRecording");
        return streamingContext != null
                && streamingContext.getStreamingEngineState()
                        == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING
                && !streamingContext.isRecordingPaused()
                && streamingContext.pauseRecording();
    }

    public boolean resumeRecording() {
        MeisheThreading.requireMainThread("NvsStreamingContext.resumeRecording");
        return streamingContext != null
                && streamingContext.getStreamingEngineState()
                        == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING
                && streamingContext.isRecordingPaused()
                && streamingContext.resumeRecording();
    }

    public boolean isRecordingPaused() {
        MeisheThreading.requireMainThread("NvsStreamingContext.isRecordingPaused");
        return streamingContext != null
                && streamingContext.getStreamingEngineState()
                        == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING
                && streamingContext.isRecordingPaused();
    }

    public boolean stopRecordingSynchronously(boolean synchronous) {
        MeisheThreading.requireMainThread("NvsStreamingContext.stopRecording");
        if (streamingContext == null || streamingContext.getStreamingEngineState()
                != NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTURERECORDING) {
            return false;
        }
        streamingContext.stopRecording(synchronous);
        return true;
    }

    public void stop() {
        MeisheThreading.requireMainThread("NvsStreamingContext.stop");
        if (streamingContext != null) {
            streamingContext.stop();
        }
    }

    public int buildCapturePreviewFlags(
            boolean captureAudio,
            boolean grabCapturedFrames,
            boolean enableTakePicture,
            boolean strictPreviewSize,
            boolean buddyHostFrames) {
        int flags = NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_USE_SYSTEM_RECORDER;
        if (!captureAudio) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_DONT_CAPTURE_AUDIO;
        }
        if (grabCapturedFrames) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_GRAB_CAPTURED_VIDEO_FRAME;
        }
        if (enableTakePicture) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_ENABLE_TAKE_PICTURE;
        }
        if (strictPreviewSize) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_STRICT_PREVIEW_VIDEO_SIZE;
        }
        if (buddyHostFrames) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_CAPTURE_FLAG_CAPTURE_BUDDY_HOST_VIDEO_FRAME;
        }
        return flags;
    }

    public boolean startRecordingWithFlags(
            String outputPath,
            boolean ignoreVideoRotation,
            boolean fastStop) {
        MeisheThreading.requireMainThread("NvsStreamingContext.startRecording");
        if (streamingContext == null || outputPath == null || outputPath.isEmpty()) {
            return false;
        }
        int flags = 0;
        if (ignoreVideoRotation) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_RECORDING_FLAG_IGNORE_VIDEO_ROTATION;
        }
        if (fastStop) {
            flags |= NvsStreamingContext
                    .STREAMING_ENGINE_RECORDING_FLAG_SOFTWARE_VIDEO_INTRA_FRAME_ONLY_FAST_STOP;
        }
        return streamingContext.startRecording(outputPath, flags);
    }

    public NvsStreamingContext.CaptureDeviceCapability getDeviceCapability(int deviceIndex) {
        MeisheThreading.requireMainThread("NvsStreamingContext.getCaptureDeviceCapability");
        if (streamingContext == null || deviceIndex < 0
                || deviceIndex >= streamingContext.getCaptureDeviceCount()) {
            return null;
        }
        return streamingContext.getCaptureDeviceCapability(deviceIndex);
    }

    public int getExposureCompensation() {
        MeisheThreading.requireMainThread("NvsStreamingContext.getExposureCompensation");
        return streamingContext == null ? 0 : streamingContext.getExposureCompensation();
    }

    public int getZoom() {
        MeisheThreading.requireMainThread("NvsStreamingContext.getZoom");
        return streamingContext == null ? 0 : streamingContext.getZoom();
    }

    public boolean setExposureCompensation(int deviceIndex, int exposureCompensation) {
        MeisheThreading.requireMainThread("NvsStreamingContext.setExposureCompensation");
        NvsStreamingContext.CaptureDeviceCapability capability = getDeviceCapability(deviceIndex);
        if (capability == null || !capability.supportExposureCompensation) {
            return false;
        }
        int clampedExposure = Math.max(
                capability.minExposureCompensation,
                Math.min(exposureCompensation, capability.maxExposureCompensation));
        streamingContext.setExposureCompensation(clampedExposure);
        return streamingContext.getExposureCompensation() == clampedExposure;
    }

    public boolean setZoom(int deviceIndex, int zoom) {
        MeisheThreading.requireMainThread("NvsStreamingContext.setZoom");
        NvsStreamingContext.CaptureDeviceCapability capability = getDeviceCapability(deviceIndex);
        if (capability == null || !capability.supportZoom) {
            return false;
        }
        int clampedZoom = Math.max(0, Math.min(zoom, capability.maxZoom));
        streamingContext.setZoom(clampedZoom);
        return streamingContext.getZoom() == clampedZoom;
    }

    public boolean focusAndMeter(int deviceIndex, RectF focusRect) {
        MeisheThreading.requireMainThread("configure autofocus and auto exposure");
        NvsStreamingContext.CaptureDeviceCapability capability = getDeviceCapability(deviceIndex);
        if (capability == null || focusRect == null || focusRect.isEmpty()) {
            return false;
        }
        boolean requested = false;
        if (capability.supportAutoExposure) {
            streamingContext.setAutoExposureRect(focusRect);
            requested = true;
        }
        if (capability.supportAutoFocus) {
            streamingContext.startAutoFocus(focusRect);
            requested = true;
        }
        return requested;
    }

    public boolean setFlashEnabled(int deviceIndex, boolean enabled) {
        MeisheThreading.requireMainThread("NvsStreamingContext.toggleFlash");
        NvsStreamingContext.CaptureDeviceCapability capability = getDeviceCapability(deviceIndex);
        if (capability == null || !capability.supportFlash || !isBackFacing(deviceIndex)) {
            if (streamingContext != null && streamingContext.isFlashOn()) {
                streamingContext.toggleFlash(false);
            }
            return !enabled;
        }
        streamingContext.toggleFlash(enabled);
        return streamingContext.isFlashOn() == enabled;
    }

    public boolean isFlashEnabled() {
        MeisheThreading.requireMainThread("NvsStreamingContext.isFlashOn");
        return streamingContext != null && streamingContext.isFlashOn();
    }

    public boolean configureDeviceControls(
            int deviceIndex,
            int exposureCompensation,
            int zoom,
            RectF focusRect,
            boolean flashEnabled) {
        MeisheThreading.requireMainThread("configure capture device controls");
        if (streamingContext == null || deviceIndex < 0
                || deviceIndex >= streamingContext.getCaptureDeviceCount()) {
            return false;
        }
        NvsStreamingContext.CaptureDeviceCapability capability =
                streamingContext.getCaptureDeviceCapability(deviceIndex);
        if (capability == null) {
            return false;
        }
        boolean exposureConfigured = true;
        if (capability.supportExposureCompensation) {
            int clampedExposure = Math.max(
                    capability.minExposureCompensation,
                    Math.min(
                            exposureCompensation,
                            capability.maxExposureCompensation));
            streamingContext.setExposureCompensation(clampedExposure);
            exposureConfigured =
                    streamingContext.getExposureCompensation() == clampedExposure;
        }

        boolean zoomConfigured = true;
        if (capability.supportZoom) {
            int clampedZoom = Math.max(0, Math.min(zoom, capability.maxZoom));
            streamingContext.setZoom(clampedZoom);
            zoomConfigured = streamingContext.getZoom() == clampedZoom;
        }

        boolean focusConfigured = true;
        if (focusRect != null && !focusRect.isEmpty()) {
            focusConfigured = false;
            if (capability.supportAutoExposure) {
                streamingContext.setAutoExposureRect(focusRect);
                focusConfigured = true;
            }
            if (capability.supportAutoFocus) {
                streamingContext.startAutoFocus(focusRect);
                focusConfigured = true;
            }
        }

        boolean flashConfigured = true;
        boolean canUseFlash = capability.supportFlash
                && streamingContext.isCaptureDeviceBackFacing(deviceIndex);
        if (canUseFlash) {
            streamingContext.toggleFlash(flashEnabled);
            flashConfigured = streamingContext.isFlashOn() == flashEnabled;
        } else if (streamingContext.isFlashOn()) {
            streamingContext.toggleFlash(false);
            flashConfigured = !flashEnabled && !streamingContext.isFlashOn();
        } else {
            flashConfigured = !flashEnabled;
        }
        return exposureConfigured && zoomConfigured && focusConfigured && flashConfigured;
    }

    public void registerCallbacks(
            NvsStreamingContext.CaptureDeviceCallback deviceCallback,
            NvsStreamingContext.CaptureRecordingStartedCallback recordingStartedCallback,
            NvsStreamingContext.CaptureRecordingDurationCallback recordingDurationCallback,
            NvsStreamingContext.CaptureRecordingFrameReachedCallback recordingFrameReachedCallback) {
        MeisheThreading.requireMainThread("register capture callbacks");
        if (streamingContext == null) {
            return;
        }
        streamingContext.setCaptureDeviceCallback(deviceCallback);
        streamingContext.setCaptureRecordingStartedCallback(recordingStartedCallback);
        streamingContext.setCaptureRecordingDurationCallback(recordingDurationCallback);
        streamingContext.setCaptureRecordingFrameReachedCallback(recordingFrameReachedCallback);
    }

    public void registerCallbacks(
            NvsStreamingContext.CaptureDeviceCallback deviceCallback,
            NvsStreamingContext.CaptureRecordingStartedCallback recordingStartedCallback,
            NvsStreamingContext.CaptureRecordingDurationCallback recordingDurationCallback) {
        registerCallbacks(
                deviceCallback,
                recordingStartedCallback,
                recordingDurationCallback,
                null);
    }

    public List<NvsCaptureVideoFx> listCaptureEffects() {
        MeisheThreading.requireMainThread("inspect capture video FX");
        List<NvsCaptureVideoFx> effects = new ArrayList<>();
        if (streamingContext == null) {
            return effects;
        }
        for (int index = 0; index < streamingContext.getCaptureVideoFxCount(); index++) {
            NvsCaptureVideoFx fx = streamingContext.getCaptureVideoFxByIndex(index);
            if (fx != null) {
                effects.add(fx);
            }
        }
        return effects;
    }

    public boolean removeCaptureEffect(int effectIndex) {
        MeisheThreading.requireMainThread("NvsStreamingContext.removeCaptureVideoFx");
        return streamingContext != null
                && effectIndex >= 0
                && effectIndex < streamingContext.getCaptureVideoFxCount()
                && streamingContext.removeCaptureVideoFx(effectIndex);
    }

    public void clearCaptureEffects() {
        MeisheThreading.requireMainThread("NvsStreamingContext.removeAllCaptureVideoFx");
        if (streamingContext != null) {
            streamingContext.removeAllCaptureVideoFx();
            streamingContext.removeCurrentCaptureScene();
        }
    }

    public boolean startRecordingWithConfigurations(
            String outputPath,
            int flags,
            java.util.Hashtable<String, Object> configurations) {
        MeisheThreading.requireMainThread("NvsStreamingContext.startRecording");
        if (streamingContext == null || outputPath == null || outputPath.isEmpty()) {
            return false;
        }
        return streamingContext.startRecording(
                outputPath,
                flags,
                configurations == null
                        ? new java.util.Hashtable<String, Object>()
                        : configurations);
    }
}
