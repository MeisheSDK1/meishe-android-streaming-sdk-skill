package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsRational;

import java.util.Hashtable;

public final class MeisheExportController {
    private final NvsStreamingContext streamingContext;

    public MeisheExportController(NvsStreamingContext streamingContext) {
        this.streamingContext = streamingContext;
    }

    public boolean export(NvsTimeline timeline, String outputPath) {
        MeisheThreading.requireMainThread("compileTimeline");
        if (timeline == null || outputPath == null || outputPath.isEmpty()) {
            return false;
        }
        streamingContext.stop();
        streamingContext.setCompileConfigurations(new Hashtable<String, Object>());
        return streamingContext.compileTimeline(
                timeline,
                0,
                timeline.getDuration(),
                outputPath,
                NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM,
                NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH,
                NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_HOST_VIDEO_FRAME
                        | NvsStreamingContext.STREAMING_ENGINE_COMPILE_FLAG_BUDDY_ORIGIN_VIDEO_FRAME);
    }

    public boolean exportWithConfigurations(
            NvsTimeline timeline,
            long startTime,
            long endTime,
            String outputPath,
            int videoResolutionGrade,
            int videoBitrateGrade,
            Hashtable<String, Object> compileConfigurations,
            int flags) {
        MeisheThreading.requireMainThread("NvsStreamingContext.compileTimeline");
        if (streamingContext == null || timeline == null || outputPath == null
                || outputPath.isEmpty() || startTime < 0 || endTime <= startTime
                || endTime > timeline.getDuration()) {
            return false;
        }
        streamingContext.stop();
        Hashtable<String, Object> safeConfigurations = compileConfigurations == null
                ? new Hashtable<String, Object>()
                : compileConfigurations;
        return streamingContext.compileTimeline(
                timeline,
                startTime,
                endTime,
                outputPath,
                videoResolutionGrade,
                videoBitrateGrade,
                safeConfigurations,
                flags);
    }

    public Hashtable<String, Object> configureCompile(
            int bitrateMbps,
            int fps,
            boolean useOperatingRate,
            String videoEncoderName,
            Integer hdrColorTransfer) {
        MeisheThreading.requireMainThread("NvsStreamingContext.setCompileConfigurations");
        Hashtable<String, Object> configurations = new Hashtable<>();
        if (bitrateMbps > 0) {
            configurations.put(
                    NvsStreamingContext.COMPILE_BITRATE,
                    bitrateMbps * 1_000_000);
        }
        if (fps > 0) {
            configurations.put(
                    NvsStreamingContext.COMPILE_FPS,
                    new NvsRational(fps, 1));
        }
        configurations.put(
                NvsStreamingContext.COMPILE_USE_OPERATING_RATE,
                useOperatingRate);
        if (videoEncoderName != null && !videoEncoderName.isEmpty()) {
            configurations.put(
                    NvsStreamingContext.COMPILE_VIDEO_ENCODER_NAME,
                    videoEncoderName);
        }
        if (hdrColorTransfer != null) {
            configurations.put(
                    NvsStreamingContext.COMPILE_VIDEO_HDR_COLOR_TRANSFER,
                    hdrColorTransfer);
        }
        streamingContext.setCompileConfigurations(configurations);
        return configurations;
    }

    public int resolutionGradeForHeight(int outputHeight) {
        if (outputHeight <= 360) {
            return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_360;
        }
        if (outputHeight <= 480) {
            return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_480;
        }
        if (outputHeight <= 720) {
            return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_720;
        }
        if (outputHeight <= 1080) {
            return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_1080;
        }
        if (outputHeight <= 2160) {
            return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_2160;
        }
        return NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM;
    }

    public int bitrateGrade(boolean preferHighQuality) {
        return preferHighQuality
                ? NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH
                : NvsStreamingContext.COMPILE_BITRATE_GRADE_MEDIUM;
    }

    public void registerCompileCallbacks(
            NvsStreamingContext.CompileCallback compileCallback,
            NvsStreamingContext.CompileCallback2 compileProgressCallback) {
        MeisheThreading.requireMainThread("register compile callbacks");
        if (streamingContext == null) {
            return;
        }
        streamingContext.setCompileCallback(compileCallback);
        streamingContext.setCompileCallback2(compileProgressCallback);
    }

    public void registerCompileCallback3(NvsStreamingContext.CompileCallback3 callback) {
        MeisheThreading.requireMainThread("NvsStreamingContext.setCompileCallback3");
        if (streamingContext != null) {
            streamingContext.setCompileCallback3(callback);
        }
    }
}
