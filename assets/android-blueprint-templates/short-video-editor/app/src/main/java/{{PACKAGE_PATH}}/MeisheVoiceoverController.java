package {{PACKAGE_NAME}};

import android.Manifest;
import android.app.Activity;
import android.content.pm.PackageManager;
import android.media.MediaRecorder;
import android.os.Build;
import android.os.Environment;

import com.meicam.sdk.NvsAVFileInfo;
import com.meicam.sdk.NvsAudioTrack;
import com.meicam.sdk.NvsAudioClip;
import com.meicam.sdk.NvsStreamingContext;

import java.io.File;

public final class MeisheVoiceoverController {
    public interface Listener {
        void onRecordingStateChanged(boolean recording);

        void onStatusChanged(String message);
    }

    private final Activity activity;
    private final int permissionRequestCode;
    private final MeisheEditorSessionController session;
    private final MeisheEditorProjectController project;
    private final MeisheAudioController audioController;
    private final Listener listener;
    private MediaRecorder recorder;
    private File outputFile;
    private long inPointUs;

    public MeisheVoiceoverController(
            Activity activity,
            int permissionRequestCode,
            MeisheEditorSessionController session,
            MeisheEditorProjectController project,
            MeisheAudioController audioController,
            Listener listener) {
        if (activity == null || session == null || project == null
                || audioController == null || listener == null) {
            throw new IllegalArgumentException("voiceover dependencies are required");
        }
        this.activity = activity;
        this.permissionRequestCode = permissionRequestCode;
        this.session = session;
        this.project = project;
        this.audioController = audioController;
        this.listener = listener;
    }

    public void toggle() {
        if (!session.canRebuildEditorFeatures()) {
            listener.onStatusChanged(
                    "The host owns this Timeline. Enable editor feature mutations first.");
            return;
        }
        if (recorder != null) {
            stop();
            return;
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M
                && activity.checkSelfPermission(Manifest.permission.RECORD_AUDIO)
                != PackageManager.PERMISSION_GRANTED) {
            activity.requestPermissions(
                    new String[]{Manifest.permission.RECORD_AUDIO},
                    permissionRequestCode);
            return;
        }
        start();
    }

    public void onPermissionResult(int requestCode, int[] grantResults) {
        if (requestCode == permissionRequestCode
                && session.canRebuildEditorFeatures()
                && grantResults != null
                && grantResults.length > 0
                && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            start();
        }
    }

    public void onPause() {
        if (recorder != null) {
            stop();
        }
    }

    public void release() {
        releaseRecorder();
    }

    private void start() {
        File outputDir = activity.getExternalFilesDir(Environment.DIRECTORY_MUSIC);
        if (outputDir == null) {
            listener.onStatusChanged("Voiceover output directory is unavailable.");
            return;
        }
        session.stopPlayback();
        inPointUs = session.currentPosition();
        outputFile = new File(outputDir, "voiceover_" + System.currentTimeMillis() + ".m4a");
        recorder = new MediaRecorder();
        try {
            recorder.setAudioSource(MediaRecorder.AudioSource.MIC);
            recorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4);
            recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AAC);
            recorder.setAudioEncodingBitRate(128_000);
            recorder.setAudioSamplingRate(44_100);
            recorder.setOutputFile(outputFile.getAbsolutePath());
            recorder.prepare();
            recorder.start();
            listener.onRecordingStateChanged(true);
            listener.onStatusChanged("Recording voiceover at the current playhead.");
        } catch (Exception exception) {
            releaseRecorder();
            listener.onStatusChanged("Voiceover failed to start: " + exception.getMessage());
        }
    }

    private void stop() {
        try {
            recorder.stop();
        } catch (RuntimeException exception) {
            if (outputFile != null) {
                outputFile.delete();
            }
            listener.onStatusChanged("Voiceover was too short and was discarded.");
            releaseRecorder();
            return;
        }
        releaseRecorder();
        if (outputFile == null) {
            return;
        }
        NvsAVFileInfo audioInfo = NvsStreamingContext.getAVInfoFromFile(
                outputFile.getAbsolutePath(),
                0);
        if (audioInfo == null || audioInfo.getDuration() <= 0) {
            listener.onStatusChanged("Recorded voiceover could not be read.");
            return;
        }
        long maxDurationUs = Math.max(0, session.duration() - inPointUs);
        long durationUs = Math.min(audioInfo.getDuration(), maxDurationUs);
        NvsAudioTrack track = audioController.ensureAudioTrack(session.timeline(), 1);
        if (durationUs <= 0 || audioController.addClip(
                track,
                outputFile.getAbsolutePath(),
                inPointUs,
                0,
                durationUs) == null) {
            listener.onStatusChanged("Voiceover could not be inserted at this playhead.");
            return;
        }
        project.replaceEditorState(MeisheEditorProjectStore.appendAudioClip(
                project.editorState(),
                1,
                outputFile.getAbsolutePath(),
                inPointUs,
                0,
                durationUs));
        project.captureAndPersist();
        session.refreshPreview(inPointUs);
        listener.onStatusChanged("Voiceover applied to its audio track. Preview the latest take or play the full timeline.");
    }

    public void previewLatest() {
        NvsAudioTrack track = session.audioTrack(1);
        NvsAudioClip clip = track == null || track.getClipCount() == 0
                ? null
                : track.getClipByIndex(track.getClipCount() - 1);
        if (clip == null) {
            listener.onStatusChanged("There is no recorded voiceover to preview.");
            return;
        }
        session.playRange(clip.getInPoint(), clip.getOutPoint());
        listener.onStatusChanged("Previewing the latest voiceover with synchronized timeline video.");
    }

    public void deleteLatest() {
        if (!session.canRebuildEditorFeatures()) {
            listener.onStatusChanged("The host owns this Timeline, so the voiceover cannot be deleted.");
            return;
        }
        NvsAudioTrack track = session.audioTrack(1);
        int clipIndex = track == null ? -1 : track.getClipCount() - 1;
        if (clipIndex < 0 || !track.removeClip(clipIndex, false)) {
            listener.onStatusChanged("There is no recorded voiceover to delete.");
            return;
        }
        project.replaceEditorState(MeisheEditorProjectStore.removeLastAudioClip(
                project.editorState(),
                1));
        project.captureAndPersist();
        session.refreshPreview(session.currentPosition());
        listener.onStatusChanged("Deleted the latest recording from the voiceover track.");
    }

    private void releaseRecorder() {
        if (recorder != null) {
            try {
                recorder.reset();
            } catch (RuntimeException ignored) {
            }
            recorder.release();
            recorder = null;
        }
        listener.onRecordingStateChanged(false);
    }
}
