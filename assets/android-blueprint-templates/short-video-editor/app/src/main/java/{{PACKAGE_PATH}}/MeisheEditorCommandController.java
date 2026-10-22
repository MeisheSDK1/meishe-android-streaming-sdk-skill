package {{PACKAGE_NAME}};

import android.os.Bundle;

import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;

public final class MeisheEditorCommandController {
    public interface Listener {
        void onStatusChanged(String message);
    }

    private static final String STATE_SELECTED_CLIP = "meishe.selectedClip";
    private static final String STATE_SELECTED_TRACK = "meishe.selectedTrack";
    private static final String STATE_POSITION_US = "meishe.positionUs";

    private final MeisheEditorSessionController session;
    private final MeisheEditorProjectController project;
    private final MeisheClipEditController clipController;
    private final Listener listener;
    private MeisheTrackSelection selectedClip;

    public MeisheEditorCommandController(
            MeisheEditorSessionController session,
            MeisheEditorProjectController project,
            Listener listener) {
        if (session == null || project == null || listener == null) {
            throw new IllegalArgumentException("session, project, and listener are required");
        }
        this.session = session;
        this.project = project;
        this.listener = listener;
        clipController = new MeisheClipEditController(session.timeline());
    }

    public void splitAtPlayhead() {
        if (!requireStructuralMutationPermission()) {
            return;
        }
        NvsVideoTrack track = session.videoTrack();
        long positionUs = session.currentPosition();
        if (track == null) {
            listener.onStatusChanged("No video track is available.");
            return;
        }
        for (int index = 0; index < track.getClipCount(); index++) {
            NvsVideoClip clip = track.getClipByIndex(index);
            if (clip == null
                    || positionUs <= clip.getInPoint() + 100_000
                    || positionUs >= clip.getOutPoint() - 100_000) {
                continue;
            }
            boolean split = MeisheClipEditController.splitAt(track, index, positionUs);
            if (split) {
                project.onClipSplit(index);
                project.reapplyEditorState();
                project.captureAndPersist();
            }
            selectedClip = clipController.selectAt(positionUs);
            session.refreshPreview(positionUs);
            listener.onStatusChanged(split
                    ? "Clip split at the playhead."
                    : "The SDK rejected this split point.");
            return;
        }
        listener.onStatusChanged("Move the playhead inside a clip before splitting.");
    }

    public void selectAtPlayhead() {
        selectedClip = clipController.selectAt(session.currentPosition());
        if (selectedClip.isValid()) {
            listener.onStatusChanged(
                    "Selected clip " + (selectedClip.clipIndex + 1)
                            + " on track " + (selectedClip.trackIndex + 1) + ".");
        } else {
            listener.onStatusChanged("No clip at the current playhead.");
        }
    }

    public void selectClip(int clipIndex) {
        NvsVideoTrack track = session.videoTrack();
        if (track == null || clipIndex < 0 || clipIndex >= track.getClipCount()) {
            selectedClip = null;
            listener.onStatusChanged("The selected timeline clip is unavailable.");
            return;
        }
        NvsVideoClip clip = track.getClipByIndex(clipIndex);
        if (clip == null) {
            selectedClip = null;
            listener.onStatusChanged("The selected timeline clip is unavailable.");
            return;
        }
        selectedClip = new MeisheTrackSelection(
                0,
                clipIndex,
                clip.getInPoint(),
                clip.getOutPoint());
        session.refreshPreview(clip.getInPoint());
        listener.onStatusChanged(
                "Selected clip " + (clipIndex + 1) + ", starting at "
                        + String.format(java.util.Locale.US, "%.1f seconds", clip.getInPoint() / 1_000_000.0)
                        + ".");
    }

    public int selectedClipIndex() {
        return selectedClip == null || !selectedClip.isValid() ? -1 : selectedClip.clipIndex;
    }

    public void trimSelectedToPlayhead() {
        if (!requireStructuralMutationPermission()) {
            return;
        }
        ensureSelection();
        long positionUs = session.currentPosition();
        if (!clipController.trimOut(selectedClip, positionUs)) {
            listener.onStatusChanged(
                    "Select a clip and move the playhead inside it before trimming.");
            return;
        }
        project.captureAndPersist();
        selectedClip = clipController.selectAt(Math.max(0, positionUs - 1));
        session.refreshPreview(Math.max(0, positionUs - 1));
        listener.onStatusChanged("Selected clip trimmed to the playhead.");
    }

    public void trimSelectedToPercent(int retainedPercent) {
        if (!requireStructuralMutationPermission()) {
            return;
        }
        ensureSelection();
        NvsVideoTrack track = session.videoTrack();
        if (track == null || selectedClip == null || !selectedClip.isValid()
                || selectedClip.clipIndex >= track.getClipCount()) {
            listener.onStatusChanged("Select a timeline clip first.");
            return;
        }
        NvsVideoClip clip = track.getClipByIndex(selectedClip.clipIndex);
        if (clip == null) {
            listener.onStatusChanged("The selected timeline clip is unavailable.");
            return;
        }
        int boundedPercent = Math.max(10, Math.min(95, retainedPercent));
        long originalDurationUs = clip.getOutPoint() - clip.getInPoint();
        long targetTimelinePositionUs = clip.getInPoint()
                + originalDurationUs * boundedPercent / 100;
        session.stopPlayback();
        if (!clipController.trimOut(selectedClip, targetTimelinePositionUs)) {
            listener.onStatusChanged("Trim failed. Select a valid clip and retain enough duration.");
            return;
        }
        project.captureAndPersist();
        selectedClip = new MeisheTrackSelection(
                0,
                selectedClip.clipIndex,
                clip.getInPoint(),
                clip.getOutPoint());
        session.refreshPreview(clip.getInPoint());
        listener.onStatusChanged(String.format(
                java.util.Locale.CHINA,
                "Trim complete: %.1fs shortened to %.1fs.",
                originalDurationUs / 1_000_000.0,
                (clip.getOutPoint() - clip.getInPoint()) / 1_000_000.0));
    }

    public void deleteSelected() {
        if (!requireStructuralMutationPermission()) {
            return;
        }
        ensureSelection();
        int removedIndex = selectedClip == null ? -1 : selectedClip.clipIndex;
        if (!clipController.delete(selectedClip)) {
            listener.onStatusChanged("No selected clip could be deleted.");
            return;
        }
        project.onClipRemoved(removedIndex);
        project.reapplyEditorState();
        project.captureAndPersist();
        selectedClip = null;
        session.refreshPreview(0);
        listener.onStatusChanged(session.videoTrack() == null
                || session.videoTrack().getClipCount() == 0
                ? "The last clip was deleted. LiveWindow now shows an empty timeline; use Previous step to restore it."
                : "Selected clip deleted.");
    }

    public void moveSelectedRight() {
        if (!requireStructuralMutationPermission()) {
            return;
        }
        ensureSelection();
        NvsVideoTrack track = session.videoTrack();
        if (track == null || selectedClip == null || !selectedClip.isValid()) {
            listener.onStatusChanged("Select a clip before moving it.");
            return;
        }
        int targetIndex = Math.min(track.getClipCount() - 1, selectedClip.clipIndex + 1);
        if (targetIndex < 0 || !clipController.move(selectedClip, targetIndex)) {
            listener.onStatusChanged("Selected clip is already at the end or cannot be moved.");
            return;
        }
        int sourceIndex = selectedClip.clipIndex;
        project.onClipMoved(sourceIndex, targetIndex);
        project.reapplyEditorState();
        project.captureAndPersist();
        selectedClip = new MeisheTrackSelection(
                0,
                targetIndex,
                selectedClip.inPointUs,
                selectedClip.outPointUs);
        session.refreshPreview(session.currentPosition());
        listener.onStatusChanged("Selected clip moved one slot to the right.");
    }

    public void undo() {
        if (!project.undo()) {
            listener.onStatusChanged("There is no previous step.");
            return;
        }
        selectedClip = null;
        session.refreshPreview(0);
        listener.onStatusChanged("Returned to the previous editing step.");
    }

    public void redo() {
        if (!project.redo()) {
            listener.onStatusChanged("There is no next step.");
            return;
        }
        selectedClip = null;
        session.refreshPreview(0);
        listener.onStatusChanged("Advanced to the next editing step.");
    }

    public void restoreInstanceState(Bundle state) {
        if (state == null) {
            selectedClip = clipController.selectAt(0);
            return;
        }
        int trackIndex = state.getInt(STATE_SELECTED_TRACK, -1);
        int clipIndex = state.getInt(STATE_SELECTED_CLIP, -1);
        NvsVideoTrack track = trackIndex == 0 ? session.videoTrack() : null;
        if (track != null && clipIndex >= 0 && clipIndex < track.getClipCount()) {
            NvsVideoClip clip = track.getClipByIndex(clipIndex);
            selectedClip = new MeisheTrackSelection(
                    trackIndex,
                    clipIndex,
                    clip.getInPoint(),
                    clip.getOutPoint());
            return;
        }
        selectedClip = clipController.selectAt(state.getLong(STATE_POSITION_US, 0));
    }

    public void saveInstanceState(Bundle state) {
        if (state == null) {
            return;
        }
        if (selectedClip != null && selectedClip.isValid()) {
            state.putInt(STATE_SELECTED_TRACK, selectedClip.trackIndex);
            state.putInt(STATE_SELECTED_CLIP, selectedClip.clipIndex);
        }
        state.putLong(STATE_POSITION_US, session.currentPosition());
    }

    private void ensureSelection() {
        if (selectedClip == null || !selectedClip.isValid()) {
            selectedClip = clipController.selectAt(session.currentPosition());
        }
    }

    private boolean requireStructuralMutationPermission() {
        if (session.canMutateStructure()) {
            return true;
        }
        listener.onStatusChanged(
                "The host owns this Timeline. Enable structural mutations in the host contract first.");
        return false;
    }
}
