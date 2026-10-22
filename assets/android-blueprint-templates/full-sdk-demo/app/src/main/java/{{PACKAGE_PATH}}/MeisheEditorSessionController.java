package {{PACKAGE_NAME}};

import android.app.Activity;
import android.widget.FrameLayout;
import android.view.ViewGroup;
import android.view.ViewParent;

import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsAudioClip;
import com.meicam.sdk.NvsAudioTrack;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public final class MeisheEditorSessionController {
    public interface Listener {
        void onPlaybackStateChanged(boolean playing);

        void onTimelinePositionChanged(long positionUs, long durationUs);

        void onStatusChanged(String message);
    }

    private static final int SEEK_FLAGS =
            NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
                    | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER;

    private final Activity activity;
    private final Listener listener;
    private final MeisheEditorHostContract hostContract;
    private final MeisheTimelineOwnership timelineOwnership;
    private NvsStreamingContext streamingContext;
    private NvsTimeline timeline;
    private MeishePlaybackController playbackController;
    private MeisheExportController exportController;
    private boolean playing;
    private boolean seeking;

    public MeisheEditorSessionController(Activity activity, Listener listener) {
        this(activity, listener, null);
    }

    public MeisheEditorSessionController(
            Activity activity,
            Listener listener,
            MeisheEditorHostContract hostContract) {
        if (activity == null || listener == null) {
            throw new IllegalArgumentException("activity and listener are required");
        }
        this.activity = activity;
        this.listener = listener;
        this.hostContract = hostContract;
        MeisheTimelineOwnership requestedOwnership = hostContract == null
                ? null
                : hostContract.timelineOwnership();
        timelineOwnership = requestedOwnership == null
                ? MeisheTimelineOwnership.EDITOR_OWNED
                : requestedOwnership;
    }

    public boolean open(
            FrameLayout liveWindowContainer,
            List<String> mediaPaths,
            int width,
            int height,
            String serializedProjectState,
            boolean restoreProject) {
        MeisheSdkManager sdkManager = new MeisheSdkManager(activity.getApplicationContext());
        if (!sdkManager.initialize()) {
            listener.onStatusChanged("SDK initialization failed.");
            return false;
        }
        streamingContext = sdkManager.getStreamingContext();
        playbackController = new MeishePlaybackController(streamingContext);
        exportController = new MeisheExportController(streamingContext);

        NvsLiveWindow liveWindow = hostContract == null
                ? null
                : hostContract.acquireLiveWindow(activity);
        if (liveWindow == null) {
            liveWindow = new NvsLiveWindow(activity);
        }
        ViewParent liveWindowParent = liveWindow.getParent();
        if (liveWindowParent == null) {
            liveWindowContainer.addView(
                    liveWindow,
                    new FrameLayout.LayoutParams(
                            ViewGroup.LayoutParams.MATCH_PARENT,
                            ViewGroup.LayoutParams.MATCH_PARENT));
        } else if (liveWindowParent != liveWindowContainer) {
            listener.onStatusChanged("Host LiveWindow is already attached to another parent.");
            return false;
        }
        playbackController.configureLiveWindow(
                liveWindow,
                NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);

        MeisheTimelineController timelineController = new MeisheTimelineController(streamingContext);
        timeline = hostContract == null
                ? null
                : hostContract.acquireTimeline(streamingContext, width, height);
        if (timeline == null && timelineOwnership == MeisheTimelineOwnership.EDITOR_OWNED) {
            timeline = timelineController.createTimeline(width, height);
        }
        if (timeline == null) {
            listener.onStatusChanged(timelineOwnership == MeisheTimelineOwnership.HOST_OWNED
                    ? "Host-owned Timeline was not provided."
                    : "Timeline creation failed.");
            return false;
        }

        int appended = 0;
        if (timelineOwnership == MeisheTimelineOwnership.HOST_OWNED) {
            NvsVideoTrack hostTrack = timeline.getVideoTrackByIndex(0);
            appended = hostTrack == null ? 0 : hostTrack.getClipCount();
            if (appended == 0 && canMutateStructure()
                    && mediaPaths != null && !mediaPaths.isEmpty()) {
                appended = timelineController.appendMediaList(mediaPaths);
            }
        } else {
            MeisheEditorProject project = restoreProject
                    ? MeisheEditorProject.fromSerialized(
                            "session-restore",
                            serializedProjectState,
                            width,
                            height)
                    : null;
            appended = project == null ? 0 : project.restoreTimeline(timeline, false);
            if (appended == 0 && mediaPaths != null && !mediaPaths.isEmpty()) {
                appended = timelineController.appendMediaList(mediaPaths);
            }
        }
        boolean restoringEmptyProject = restoreProject
                && serializedProjectState != null
                && !serializedProjectState.isEmpty()
                && timelineOwnership == MeisheTimelineOwnership.EDITOR_OWNED;
        if (appended == 0 && !restoringEmptyProject) {
            if (timelineOwnership == MeisheTimelineOwnership.EDITOR_OWNED) {
                streamingContext.removeTimeline(timeline);
            }
            timeline = null;
            listener.onStatusChanged("No selected media could be added to the timeline.");
            return false;
        }

        playbackController.connectTimeline(timeline, liveWindow);
        bindCallbacks();
        if (hostContract != null) {
            hostContract.onTimelineReady(timeline);
        }
        return true;
    }

    private void bindCallbacks() {
        streamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
            @Override
            public void onPlaybackPreloadingCompletion(NvsTimeline callbackTimeline) {
            }

            @Override
            public void onPlaybackStopped(NvsTimeline callbackTimeline) {
                activity.runOnUiThread(() -> setPlaying(false));
            }

            @Override
            public void onPlaybackEOF(NvsTimeline callbackTimeline) {
                activity.runOnUiThread(() -> {
                    setPlaying(false);
                    refreshPreview(0);
                });
            }
        });
        streamingContext.setPlaybackCallback2((callbackTimeline, positionUs) ->
                activity.runOnUiThread(() -> notifyPosition(positionUs)));
        streamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {
            @Override
            public void onCompileProgress(NvsTimeline callbackTimeline, int progress) {
                activity.runOnUiThread(() ->
                        listener.onStatusChanged("Exporting: " + progress + "%"));
            }

            @Override
            public void onCompileFinished(NvsTimeline callbackTimeline) {
                activity.runOnUiThread(() -> listener.onStatusChanged(
                        "Export finished in the app Movies directory."));
            }

            @Override
            public void onCompileFailed(NvsTimeline callbackTimeline) {
                activity.runOnUiThread(() -> listener.onStatusChanged(
                        "Export failed. Check output access, license, and codec support."));
            }
        });
        streamingContext.setCompileCallback2((callbackTimeline, isCanceled) -> {
            if (isCanceled) {
                activity.runOnUiThread(() -> listener.onStatusChanged("Export canceled."));
            }
        });
    }

    public void togglePlayback() {
        if (timeline == null || timeline.getDuration() <= 0) {
            return;
        }
        if (playing) {
            stopPlayback();
            return;
        }
        long startUs = currentPosition();
        playbackController.play(timeline, startUs, timeline.getDuration(), 0);
        setPlaying(true);
    }

    public void seekToProgress(int progress, int max) {
        if (timeline == null || max <= 0) {
            return;
        }
        long positionUs = timeline.getDuration() * Math.max(0, progress) / max;
        playbackController.seek(timeline, positionUs, SEEK_FLAGS);
    }

    public void beginSeeking() {
        seeking = true;
        stopPlayback();
    }

    public void endSeeking() {
        seeking = false;
    }

    public void refreshPreview(long positionUs) {
        if (timeline == null) {
            return;
        }
        stopPlayback();
        if (timeline.getDuration() <= 0) {
            return;
        }
        playbackController.seek(timeline, positionUs, SEEK_FLAGS);
        notifyPosition(positionUs);
    }

    public void playRange(long inPointUs, long outPointUs) {
        if (timeline == null || outPointUs <= inPointUs || timeline.getDuration() <= 0) {
            return;
        }
        stopPlayback();
        playbackController.play(
                timeline,
                Math.max(0, inPointUs),
                Math.min(timeline.getDuration(), outPointUs),
                0);
        setPlaying(true);
    }

    public void stopPlayback() {
        if (playbackController != null) {
            playbackController.stop();
        }
        setPlaying(false);
    }

    public boolean exportTo(File outputFile) {
        if (timeline == null || timeline.getDuration() <= 0 || outputFile == null) {
            return false;
        }
        stopPlayback();
        return exportController.export(timeline, outputFile.getAbsolutePath());
    }

    public long currentPosition() {
        return timeline == null || playbackController == null
                ? 0
                : playbackController.currentPosition(timeline);
    }

    public long duration() {
        return timeline == null ? 0 : timeline.getDuration();
    }

    public long overlayInPoint() {
        long positionUs = currentPosition();
        return positionUs >= duration() ? 0 : positionUs;
    }

    public long overlayDuration(long inPointUs) {
        return Math.max(100_000, Math.min(3_000_000, duration() - inPointUs));
    }

    public NvsVideoTrack videoTrack() {
        return timeline == null ? null : timeline.getVideoTrackByIndex(0);
    }

    public NvsVideoClip firstClip() {
        NvsVideoTrack track = videoTrack();
        return track == null || track.getClipCount() == 0 ? null : track.getClipByIndex(0);
    }

    public NvsAudioTrack audioTrack(int trackIndex) {
        return timeline == null || trackIndex < 0 || trackIndex >= timeline.audioTrackCount()
                ? null
                : timeline.getAudioTrackByIndex(trackIndex);
    }

    public List<MeisheEditorClipUiModel> audioClipUiModels(int trackIndex) {
        List<MeisheEditorClipUiModel> clips = new ArrayList<>();
        NvsAudioTrack track = audioTrack(trackIndex);
        if (track == null) {
            return clips;
        }
        for (int index = 0; index < track.getClipCount(); index++) {
            NvsAudioClip clip = track.getClipByIndex(index);
            if (clip == null) {
                continue;
            }
            String filePath = clip.getFilePath();
            clips.add(new MeisheEditorClipUiModel(
                    index,
                    filePath == null || filePath.isEmpty()
                            ? "Voiceover " + (index + 1)
                            : new File(filePath).getName(),
                    clip.getInPoint(),
                    clip.getOutPoint()));
        }
        return clips;
    }

    public List<MeisheEditorClipUiModel> clipUiModels() {
        List<MeisheEditorClipUiModel> clips = new ArrayList<>();
        NvsVideoTrack track = videoTrack();
        if (track == null) {
            return clips;
        }
        for (int index = 0; index < track.getClipCount(); index++) {
            NvsVideoClip clip = track.getClipByIndex(index);
            if (clip == null) {
                continue;
            }
            String filePath = clip.getFilePath();
            String displayName = filePath == null || filePath.isEmpty()
                    ? "Clip " + (index + 1)
                    : new File(filePath).getName();
            clips.add(new MeisheEditorClipUiModel(
                    index,
                    displayName,
                    clip.getInPoint(),
                    clip.getOutPoint()));
        }
        return clips;
    }

    public int clipIndexAt(long positionUs) {
        NvsVideoTrack track = videoTrack();
        if (track == null) {
            return -1;
        }
        long boundedPositionUs = Math.max(0, positionUs);
        for (int index = 0; index < track.getClipCount(); index++) {
            NvsVideoClip clip = track.getClipByIndex(index);
            if (clip != null
                    && boundedPositionUs >= clip.getInPoint()
                    && boundedPositionUs < clip.getOutPoint()) {
                return index;
            }
        }
        return track.getClipCount() > 0 && boundedPositionUs >= duration()
                ? track.getClipCount() - 1
                : -1;
    }

    public NvsTimeline timeline() {
        return timeline;
    }

    public NvsStreamingContext streamingContext() {
        return streamingContext;
    }

    public MeisheTimelineOwnership timelineOwnership() {
        return timelineOwnership;
    }

    public boolean canMutateStructure() {
        return hostContract == null || hostContract.allowStructuralMutations();
    }

    public boolean canRebuildEditorFeatures() {
        return hostContract == null || hostContract.allowEditorFeatureRebuild();
    }

    public MeisheEditorHostContract hostContract() {
        return hostContract;
    }

    public void close() {
        if (streamingContext == null) {
            return;
        }
        streamingContext.setPlaybackCallback(null);
        streamingContext.setPlaybackCallback2(null);
        streamingContext.setCompileCallback(null);
        streamingContext.setCompileCallback2(null);
        NvsTimeline closingTimeline = timeline;
        if (closingTimeline != null) {
            streamingContext.stop();
            if (timelineOwnership == MeisheTimelineOwnership.EDITOR_OWNED) {
                streamingContext.removeTimeline(closingTimeline);
            }
            timeline = null;
        }
        if (hostContract != null) {
            hostContract.onEditorClosed(closingTimeline);
        }
    }

    private void notifyPosition(long positionUs) {
        if (!seeking && timeline != null && timeline.getDuration() > 0) {
            listener.onTimelinePositionChanged(positionUs, timeline.getDuration());
        }
    }

    private void setPlaying(boolean value) {
        playing = value;
        listener.onPlaybackStateChanged(value);
    }
}
