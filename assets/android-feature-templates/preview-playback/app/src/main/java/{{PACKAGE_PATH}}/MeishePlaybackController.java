package {{PACKAGE_NAME}};

import android.graphics.PointF;

import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsMultiThumbnailSequenceView;
import com.meicam.sdk.NvsRational;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;

import java.util.ArrayList;

public final class MeishePlaybackController {
    private final NvsStreamingContext streamingContext;

    public MeishePlaybackController(NvsStreamingContext streamingContext) {
        this.streamingContext = streamingContext;
    }

    public void connectTimeline(NvsTimeline timeline, NvsLiveWindow liveWindow) {
        MeisheThreading.requireMainThread("connectTimelineWithLiveWindow");
        if (streamingContext == null || timeline == null || liveWindow == null) {
            return;
        }
        streamingContext.connectTimelineWithLiveWindow(timeline, liveWindow);
    }

    public void play(NvsTimeline timeline, long startUs, long endUs, int flags) {
        MeisheThreading.requireMainThread("playbackTimeline");
        if (streamingContext == null || timeline == null) {
            return;
        }
        long safeStart = Math.max(0, startUs);
        long safeEnd = endUs > safeStart ? endUs : timeline.getDuration();
        streamingContext.playbackTimeline(
                timeline,
                safeStart,
                safeEnd,
                NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                true,
                flags);
    }

    public void seek(NvsTimeline timeline, long timestampUs, int flags) {
        MeisheThreading.requireMainThread("seekTimeline");
        if (streamingContext == null || timeline == null) {
            return;
        }
        long safeTimestamp = Math.max(0, Math.min(timestampUs, timeline.getDuration()));
        streamingContext.seekTimeline(
                timeline,
                safeTimestamp,
                NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                flags);
    }

    public void stop() {
        MeisheThreading.requireMainThread("stop");
        if (streamingContext != null) {
            streamingContext.stop();
        }
    }

    public long currentPosition(NvsTimeline timeline) {
        MeisheThreading.requireMainThread("getTimelineCurrentPosition");
        if (streamingContext == null || timeline == null) {
            return 0;
        }
        return streamingContext.getTimelineCurrentPosition(timeline);
    }

    public void configureLiveWindow(NvsLiveWindow liveWindow, int fillMode) {
        MeisheThreading.requireMainThread("NvsLiveWindow.setFillMode");
        if (liveWindow != null) {
            liveWindow.setFillMode(fillMode);
        }
    }

    public void registerCallbacks(
            NvsStreamingContext.PlaybackCallback playbackCallback,
            NvsStreamingContext.PlaybackCallback2 playbackPositionCallback,
            NvsStreamingContext.StreamingEngineCallback engineCallback) {
        MeisheThreading.requireMainThread("register streaming callbacks");
        if (streamingContext == null) {
            return;
        }
        streamingContext.setPlaybackCallback(playbackCallback);
        streamingContext.setPlaybackCallback2(playbackPositionCallback);
        streamingContext.setStreamingEngineCallback(engineCallback);
    }

    public int buildSeekFlags(
            boolean showCaptionPoster,
            boolean showStickerPoster,
            boolean allowFastScrubbing) {
        int flags = 0;
        if (showCaptionPoster) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER;
        }
        if (showStickerPoster) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER;
        }
        if (allowFastScrubbing) {
            flags |= NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING;
        }
        return flags;
    }

    public void setSeekTimelineScale(NvsTimeline timeline, double scale) {
        MeisheThreading.requireMainThread("NvsStreamingContext.setTimelineScaleForSeek");
        if (streamingContext != null && timeline != null && scale > 0) {
            streamingContext.setTimelineScaleForSeek(timeline, scale);
        }
    }

    public long mapThumbnailXToTimelinePosition(
            NvsMultiThumbnailSequenceView thumbnailView,
            int x) {
        if (thumbnailView == null) {
            return 0;
        }
        return thumbnailView.mapTimelinePosFromX(Math.max(0, x));
    }

    public String streamingEngineStateName() {
        MeisheThreading.requireMainThread("NvsStreamingContext.getStreamingEngineState");
        if (streamingContext == null) {
            return "unavailable";
        }
        int state = streamingContext.getStreamingEngineState();
        if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_STOPPED) {
            return "stopped";
        }
        if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_CAPTUREPREVIEW) {
            return "capture-preview";
        }
        if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_SEEKING) {
            return "seeking";
        }
        if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_COMPILE) {
            return "compile";
        }
        return "active";
    }

    public void playWithPreviewFps(
            NvsTimeline timeline,
            long startUs,
            long endUs,
            NvsRational previewFps,
            int flags) {
        MeisheThreading.requireMainThread("NvsStreamingContext.playbackTimeline");
        if (streamingContext == null || timeline == null || previewFps == null) {
            return;
        }
        long safeStart = Math.max(0, startUs);
        long safeEnd = endUs > safeStart ? endUs : timeline.getDuration();
        streamingContext.playbackTimeline(
                timeline,
                safeStart,
                safeEnd,
                previewFps,
                true,
                flags);
    }

    public void seekWithPreviewFps(
            NvsTimeline timeline,
            long timestampUs,
            NvsRational previewFps,
            int flags) {
        MeisheThreading.requireMainThread("NvsStreamingContext.seekTimeline");
        if (streamingContext == null || timeline == null || previewFps == null) {
            return;
        }
        streamingContext.seekTimeline(
                timeline,
                Math.max(0, Math.min(timestampUs, timeline.getDuration())),
                previewFps,
                flags);
    }

    public boolean grabImageAsynchronously(
            NvsTimeline timeline,
            long timestampUs,
            NvsRational outputAspectRatio,
            int flags,
            NvsStreamingContext.ImageGrabberCallback callback) {
        MeisheThreading.requireMainThread("grab timeline image asynchronously");
        if (streamingContext == null || timeline == null || outputAspectRatio == null
                || callback == null || timestampUs < 0 || timestampUs > timeline.getDuration()) {
            return false;
        }
        streamingContext.setImageGrabberCallback(callback);
        return streamingContext.grabImageFromTimelineAsync(
                timeline,
                timestampUs,
                outputAspectRatio,
                flags);
    }

    public PointF mapLiveWindowPoint(
            NvsLiveWindow liveWindow,
            PointF point,
            int mappingMode) {
        MeisheThreading.requireMainThread("map LiveWindow point");
        if (liveWindow == null || point == null) {
            return null;
        }
        switch (mappingMode) {
            case 0:
                return liveWindow.mapViewToCanonical(point);
            case 1:
                return liveWindow.mapCanonicalToView(point);
            case 2:
                return liveWindow.mapViewToNormalized(point);
            case 3:
                return liveWindow.mapNormalizedToView(point);
            default:
                return null;
        }
    }

    public boolean configureThumbnailSequence(
            NvsMultiThumbnailSequenceView thumbnailView,
            ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> descriptions,
            double pixelsPerMicrosecond,
            int startPadding,
            int endPadding,
            int scaleAnchor,
            NvsMultiThumbnailSequenceView.OnScrollChangeListener listener) {
        MeisheThreading.requireMainThread("configure thumbnail sequence");
        if (thumbnailView == null || descriptions == null || descriptions.isEmpty()
                || pixelsPerMicrosecond <= 0) {
            return false;
        }
        thumbnailView.setStartPadding(Math.max(0, startPadding));
        thumbnailView.setEndPadding(Math.max(0, endPadding));
        thumbnailView.setPixelPerMicrosecond(pixelsPerMicrosecond);
        thumbnailView.setThumbnailSequenceDescArray(descriptions);
        thumbnailView.setOnScrollChangeListenser(listener);
        thumbnailView.scaleWithAnchor(1.0, scaleAnchor);
        return thumbnailView.getPixelPerMicrosecond() > 0;
    }
}
