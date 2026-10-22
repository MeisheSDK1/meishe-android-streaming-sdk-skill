package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;

public final class MeisheClipEditController {
    private final NvsTimeline timeline;

    public MeisheClipEditController(NvsTimeline timeline) {
        this.timeline = timeline;
    }

    public MeisheTrackSelection selectAt(long timelinePositionUs) {
        NvsVideoTrack track = videoTrack();
        if (track == null) {
            return new MeisheTrackSelection(-1, -1, 0, 0);
        }
        for (int index = 0; index < track.getClipCount(); index++) {
            NvsVideoClip clip = track.getClipByIndex(index);
            if (clip != null
                    && timelinePositionUs >= clip.getInPoint()
                    && timelinePositionUs < clip.getOutPoint()) {
                return new MeisheTrackSelection(0, index, clip.getInPoint(), clip.getOutPoint());
            }
        }
        return new MeisheTrackSelection(-1, -1, 0, 0);
    }

    public boolean trimOut(MeisheTrackSelection selection, long timelinePositionUs) {
        NvsVideoClip clip = selectedClip(selection);
        return trimOutAtTimelinePosition(clip, timelinePositionUs);
    }

    public static boolean trimOutAtTimelinePosition(
            NvsVideoClip clip,
            long timelinePositionUs) {
        if (clip == null
                || timelinePositionUs <= clip.getInPoint() + 100_000
                || timelinePositionUs >= clip.getOutPoint()) {
            return false;
        }
        double speed = clip.getSpeed();
        if (Double.isNaN(speed) || Double.isInfinite(speed) || speed <= 0) {
            speed = 1.0;
        }
        long oldTrimOutUs = clip.getTrimOut();
        long sourceOffsetUs = Math.round((timelinePositionUs - clip.getInPoint()) * speed);
        long requestedTrimOutUs = clip.getTrimIn() + sourceOffsetUs;
        if (requestedTrimOutUs <= clip.getTrimIn() || requestedTrimOutUs >= oldTrimOutUs) {
            return false;
        }
        clip.changeTrimOutPoint(requestedTrimOutUs, true);
        long actualTrimOutUs = clip.getTrimOut();
        return actualTrimOutUs > clip.getTrimIn() && actualTrimOutUs < oldTrimOutUs;
    }

    public boolean delete(MeisheTrackSelection selection) {
        NvsVideoTrack track = videoTrack();
        return selection != null && selection.isValid() && removeAt(track, selection.clipIndex);
    }

    public static boolean removeAt(NvsVideoTrack track, int clipIndex) {
        return track != null
                && clipIndex >= 0
                && clipIndex < track.getClipCount()
                && track.removeClip(clipIndex, false);
    }

    public boolean move(MeisheTrackSelection selection, int targetIndex) {
        NvsVideoTrack track = videoTrack();
        if (selection == null || !selection.isValid() || track == null) {
            return false;
        }
        return moveAt(track, selection.clipIndex, targetIndex);
    }

    public static boolean moveAt(NvsVideoTrack track, int clipIndex, int targetIndex) {
        if (track == null || clipIndex < 0 || clipIndex >= track.getClipCount()) {
            return false;
        }
        int boundedIndex = Math.max(0, Math.min(targetIndex, track.getClipCount() - 1));
        return boundedIndex != clipIndex && track.moveClip(clipIndex, boundedIndex);
    }

    public static boolean splitAt(NvsVideoTrack track, int clipIndex, long timelinePositionUs) {
        if (track == null || clipIndex < 0 || clipIndex >= track.getClipCount()) {
            return false;
        }
        NvsVideoClip clip = track.getClipByIndex(clipIndex);
        return clip != null
                && timelinePositionUs > clip.getInPoint() + 100_000
                && timelinePositionUs < clip.getOutPoint() - 100_000
                && track.splitClip(clipIndex, timelinePositionUs);
    }

    private NvsVideoClip selectedClip(MeisheTrackSelection selection) {
        NvsVideoTrack track = videoTrack();
        if (selection == null || !selection.isValid() || track == null) {
            return null;
        }
        if (selection.clipIndex >= track.getClipCount()) {
            return null;
        }
        return track.getClipByIndex(selection.clipIndex);
    }

    private NvsVideoTrack videoTrack() {
        return timeline == null ? null : timeline.getVideoTrackByIndex(0);
    }
}
