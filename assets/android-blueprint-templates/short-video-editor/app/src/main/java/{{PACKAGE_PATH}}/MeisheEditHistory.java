package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public final class MeisheEditHistory {
    private static final int MAX_SNAPSHOTS = 50;

    private final Deque<HistorySnapshot> undoStack = new ArrayDeque<>();
    private final Deque<HistorySnapshot> redoStack = new ArrayDeque<>();
    private final Deque<String> projectUndoStack = new ArrayDeque<>();
    private final Deque<String> projectRedoStack = new ArrayDeque<>();

    public void capture(NvsTimeline timeline, String editorStateJson) {
        undoStack.push(new HistorySnapshot(snapshot(timeline), editorStateJson));
        while (undoStack.size() > MAX_SNAPSHOTS) {
            undoStack.removeLast();
        }
        redoStack.clear();
    }

    public void captureProject(String serializedProject) {
        if (serializedProject == null || serializedProject.isEmpty()
                || (!projectUndoStack.isEmpty()
                && serializedProject.equals(projectUndoStack.peek()))) {
            return;
        }
        projectUndoStack.push(serializedProject);
        while (projectUndoStack.size() > MAX_SNAPSHOTS) {
            projectUndoStack.removeLast();
        }
        projectRedoStack.clear();
    }

    public String undoProject() {
        if (projectUndoStack.size() <= 1) {
            return null;
        }
        projectRedoStack.push(projectUndoStack.pop());
        return projectUndoStack.peek();
    }

    public String redoProject() {
        if (projectRedoStack.isEmpty()) {
            return null;
        }
        String next = projectRedoStack.pop();
        projectUndoStack.push(next);
        return next;
    }

    public String undo(NvsTimeline timeline) {
        if (undoStack.size() <= 1) {
            return null;
        }
        redoStack.push(undoStack.pop());
        HistorySnapshot previous = undoStack.peek();
        return previous != null && restore(timeline, previous.clips)
                ? previous.editorStateJson
                : null;
    }

    public String redo(NvsTimeline timeline) {
        if (redoStack.isEmpty()) {
            return null;
        }
        HistorySnapshot next = redoStack.pop();
        undoStack.push(next);
        return restore(timeline, next.clips) ? next.editorStateJson : null;
    }

    private static List<ClipSnapshot> snapshot(NvsTimeline timeline) {
        List<ClipSnapshot> clips = new ArrayList<>();
        NvsVideoTrack track = timeline == null ? null : timeline.getVideoTrackByIndex(0);
        if (track == null) {
            return clips;
        }
        for (int index = 0; index < track.getClipCount(); index++) {
            NvsVideoClip clip = track.getClipByIndex(index);
            if (clip != null) {
                clips.add(new ClipSnapshot(
                        clip.getFilePath(),
                        clip.getTrimIn(),
                        clip.getTrimOut(),
                        clip.getSpeed(),
                        clip.isKeepAudioPitch(),
                        clip.getVideoType(),
                        clip.getImageMotionAnimationEnabled()));
            }
        }
        return clips;
    }

    private static boolean restore(NvsTimeline timeline, List<ClipSnapshot> clips) {
        NvsVideoTrack track = timeline == null ? null : timeline.getVideoTrackByIndex(0);
        if (track == null || clips == null) {
            return false;
        }
        track.removeAllClips();
        for (ClipSnapshot clip : clips) {
            if (clip.filePath != null && !clip.filePath.isEmpty()) {
                NvsVideoClip restored = track.appendClip(clip.filePath, clip.trimInUs, clip.trimOutUs);
                if (restored == null) {
                    continue;
                }
                if (!Double.isNaN(clip.speed)
                        && !Double.isInfinite(clip.speed)
                        && clip.speed > 0
                        && Math.abs(clip.speed - 1.0) > 0.0001) {
                    restored.changeSpeed(clip.speed, clip.keepAudioPitch);
                }
                if (restored.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {
                    restored.setImageMotionAnimationEnabled(clip.imageMotionEnabled);
                }
            }
        }
        return true;
    }

    private static final class ClipSnapshot {
        final String filePath;
        final long trimInUs;
        final long trimOutUs;
        final double speed;
        final boolean keepAudioPitch;
        final int videoType;
        final boolean imageMotionEnabled;

        ClipSnapshot(
                String filePath,
                long trimInUs,
                long trimOutUs,
                double speed,
                boolean keepAudioPitch,
                int videoType,
                boolean imageMotionEnabled) {
            this.filePath = filePath;
            this.trimInUs = trimInUs;
            this.trimOutUs = trimOutUs;
            this.speed = speed;
            this.keepAudioPitch = keepAudioPitch;
            this.videoType = videoType;
            this.imageMotionEnabled = imageMotionEnabled;
        }
    }

    private static final class HistorySnapshot {
        final List<ClipSnapshot> clips;
        final String editorStateJson;

        HistorySnapshot(List<ClipSnapshot> clips, String editorStateJson) {
            this.clips = clips;
            this.editorStateJson = editorStateJson == null ? "" : editorStateJson;
        }
    }
}
