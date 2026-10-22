package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.ClipData;
import android.content.Intent;
import android.net.Uri;

import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public final class MeisheEditorMediaController {
    public interface Listener {
        void onMediaImportStarted(int mediaCount);

        void onMediaImportFinished(int appendedCount, int rejectedCount);
    }

    private final Activity activity;
    private final MeisheEditorSessionController session;
    private final MeisheEditorProjectController project;
    private final Listener listener;
    private final ExecutorService importExecutor = Executors.newSingleThreadExecutor();

    public MeisheEditorMediaController(
            Activity activity,
            MeisheEditorSessionController session,
            MeisheEditorProjectController project,
            Listener listener) {
        if (activity == null || session == null || project == null || listener == null) {
            throw new IllegalArgumentException(
                    "activity, session, project, and listener are required");
        }
        this.activity = activity;
        this.session = session;
        this.project = project;
        this.listener = listener;
    }

    public Intent createPickerIntent() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("*/*");
        intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
        intent.putExtra(Intent.EXTRA_MIME_TYPES, new String[]{"video/*", "image/*"});
        return intent;
    }

    public void importResult(Intent data) {
        List<Uri> uris = collectUris(data);
        if (uris.isEmpty()) {
            listener.onMediaImportFinished(0, 0);
            return;
        }
        listener.onMediaImportStarted(uris.size());
        importExecutor.execute(() -> copySelectedMedia(uris));
    }

    public void release() {
        importExecutor.shutdownNow();
    }

    private void copySelectedMedia(List<Uri> uris) {
        List<File> copiedFiles = new ArrayList<>();
        int copyFailures = 0;
        for (Uri uri : uris) {
            try {
                copiedFiles.add(MeisheMediaImporter.copyToProjectFile(activity, uri));
            } catch (Exception exception) {
                copyFailures++;
            }
        }
        int finalCopyFailures = copyFailures;
        activity.runOnUiThread(() -> appendCopiedMedia(copiedFiles, finalCopyFailures));
    }

    private void appendCopiedMedia(List<File> copiedFiles, int copyFailures) {
        NvsVideoTrack videoTrack = session.videoTrack();
        if (videoTrack == null) {
            listener.onMediaImportFinished(0, copiedFiles.size() + copyFailures);
            return;
        }
        session.stopPlayback();
        int appendedCount = 0;
        int rejectedCount = copyFailures;
        for (File file : copiedFiles) {
            NvsVideoClip clip = videoTrack.appendClip(file.getAbsolutePath());
            if (clip == null) {
                rejectedCount++;
                if (file.isFile()) {
                    file.delete();
                }
                continue;
            }
            if (clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {
                clip.setImageMotionAnimationEnabled(false);
            }
            appendedCount++;
        }
        if (appendedCount > 0) {
            project.captureAndPersist();
            session.refreshPreview(session.currentPosition());
        }
        listener.onMediaImportFinished(appendedCount, rejectedCount);
    }

    private static List<Uri> collectUris(Intent data) {
        List<Uri> uris = new ArrayList<>();
        if (data == null) {
            return uris;
        }
        ClipData clipData = data.getClipData();
        if (clipData != null) {
            for (int index = 0; index < clipData.getItemCount(); index++) {
                Uri uri = clipData.getItemAt(index).getUri();
                if (uri != null) {
                    uris.add(uri);
                }
            }
        } else if (data.getData() != null) {
            uris.add(data.getData());
        }
        return uris;
    }
}
