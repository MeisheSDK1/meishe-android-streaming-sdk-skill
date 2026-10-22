package {{PACKAGE_NAME}};

import android.graphics.Bitmap;
import android.os.Handler;

import com.meicam.sdk.NvsAVFileInfo;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;
import com.meicam.sdk.NvsRational;
import com.meicam.sdk.NvsPassthroughConvertor;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.List;
import java.util.Hashtable;

public final class MeisheMediaWorkflowController {
    public NvsAVFileInfo probeUrlMedia(String mediaUrlOrPath, int probeFlags) {
        MeisheThreading.requireMainThread("probe URL media");
        if (mediaUrlOrPath == null || mediaUrlOrPath.trim().isEmpty()) {
            return null;
        }
        return NvsStreamingContext.getAVInfoFromFile(mediaUrlOrPath.trim(), probeFlags);
    }

    public int appendPhotoAlbum(NvsTimeline timeline, List<String> imagePaths) {
        MeisheThreading.requireMainThread("append photo album media");
        if (timeline == null || imagePaths == null || imagePaths.isEmpty()) {
            return 0;
        }
        NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null) {
            track = timeline.appendVideoTrack();
        }
        if (track == null) {
            return 0;
        }
        int appended = 0;
        for (String imagePath : imagePaths) {
            if (imagePath == null || imagePath.isEmpty()) {
                continue;
            }
            NvsVideoClip clip = track.appendClip(imagePath);
            if (clip != null) {
                clip.setImageMotionAnimationEnabled(false);
                appended++;
            }
        }
        return appended;
    }

    public int appendThemeShots(
            NvsTimeline timeline,
            List<String> shotPaths,
            List<Long> trimInPointsUs,
            List<Long> trimOutPointsUs,
            List<Double> speeds) {
        MeisheThreading.requireMainThread("append theme-shoot clips");
        if (timeline == null || shotPaths == null || trimInPointsUs == null
                || trimOutPointsUs == null || speeds == null) {
            return 0;
        }
        NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null) {
            track = timeline.appendVideoTrack();
        }
        if (track == null) {
            return 0;
        }
        int count = Math.min(
                Math.min(shotPaths.size(), trimInPointsUs.size()),
                Math.min(trimOutPointsUs.size(), speeds.size()));
        int appended = 0;
        for (int index = 0; index < count; index++) {
            String path = shotPaths.get(index);
            Long trimIn = trimInPointsUs.get(index);
            Long trimOut = trimOutPointsUs.get(index);
            Double speed = speeds.get(index);
            if (path == null || path.isEmpty() || trimIn == null || trimOut == null
                    || speed == null || trimIn < 0 || trimOut <= trimIn || speed <= 0) {
                continue;
            }
            NvsVideoClip clip = track.appendClip(path, trimIn, trimOut);
            if (clip != null) {
                clip.changeSpeed(speed);
                appended++;
            }
        }
        return appended;
    }

    public int appendRecordedClips(NvsTimeline timeline, List<String> recordedPaths) {
        MeisheThreading.requireMainThread("append recorded clips for editing");
        if (timeline == null || recordedPaths == null || recordedPaths.isEmpty()) {
            return 0;
        }
        NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null) {
            track = timeline.appendVideoTrack();
        }
        if (track == null) {
            return 0;
        }
        int appended = 0;
        for (String path : recordedPaths) {
            if (path != null && !path.isEmpty() && track.appendClip(path) != null) {
                appended++;
            }
        }
        return appended;
    }

    public boolean appendBoomerangClips(
            NvsTimeline timeline,
            String forwardMediaPath,
            String reverseMediaPath) {
        MeisheThreading.requireMainThread("append boomerang forward and reverse clips");
        if (timeline == null || forwardMediaPath == null || forwardMediaPath.isEmpty()
                || reverseMediaPath == null || reverseMediaPath.isEmpty()) {
            return false;
        }
        NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null) {
            track = timeline.appendVideoTrack();
        }
        if (track == null || track.appendClip(forwardMediaPath) == null) {
            return false;
        }
        return track.appendClip(reverseMediaPath) != null;
    }

    public Bitmap grabCoverFrame(
            NvsStreamingContext streamingContext,
            NvsTimeline timeline,
            long timelinePositionUs) {
        MeisheThreading.requireMainThread("grab cover frame");
        if (streamingContext == null || timeline == null || timelinePositionUs < 0) {
            return null;
        }
        return streamingContext.grabImageFromTimeline(
                timeline,
                Math.min(timelinePositionUs, timeline.getDuration()),
                new NvsRational(1, 1));
    }

    public NvsVideoClip appendNestedTimeline(
            NvsTimeline parentTimeline,
            NvsTimeline childTimeline,
            boolean insertAtHead) {
        MeisheThreading.requireMainThread("append nested timeline clip");
        if (parentTimeline == null || childTimeline == null || parentTimeline == childTimeline) {
            return null;
        }
        NvsVideoTrack track = parentTimeline.getVideoTrackByIndex(0);
        if (track == null) {
            track = parentTimeline.appendVideoTrack();
        }
        if (track == null) {
            return null;
        }
        return insertAtHead
                ? track.insertTimelineClip(childTimeline, 0)
                : track.appendTimelineClip(childTimeline);
    }

    public boolean makeLivePhoto(
            NvsStreamingContext streamingContext,
            String compiledVideoPath,
            long coverPositionUs,
            String outputPath) {
        MeisheThreading.requireMainThread("make live photo from compiled video");
        if (streamingContext == null || compiledVideoPath == null || compiledVideoPath.isEmpty()
                || coverPositionUs < 0 || outputPath == null || outputPath.isEmpty()) {
            return false;
        }
        return streamingContext.makeLivePhotoFromVideoFile(
                compiledVideoPath,
                coverPositionUs,
                outputPath);
    }

    public boolean exportTimelineFrame(
            NvsStreamingContext streamingContext,
            NvsTimeline timeline,
            long timelinePositionUs,
            File outputFile,
            int jpegQuality) {
        MeisheThreading.requireMainThread("export timeline frame");
        if (streamingContext == null || timeline == null || timelinePositionUs < 0
                || outputFile == null || jpegQuality < 0 || jpegQuality > 100) {
            return false;
        }
        Bitmap bitmap = streamingContext.grabImageFromTimeline(
                timeline,
                Math.min(timelinePositionUs, timeline.getDuration()),
                new NvsRational(1, 1));
        if (bitmap == null) {
            return false;
        }
        File parent = outputFile.getParentFile();
        if (parent != null && !parent.exists() && !parent.mkdirs()) {
            return false;
        }
        try (FileOutputStream output = new FileOutputStream(outputFile)) {
            return bitmap.compress(Bitmap.CompressFormat.JPEG, jpegQuality, output);
        } catch (IOException exception) {
            return false;
        }
    }

    public long convertMediaFilesWithoutReencoding(
            NvsPassthroughConvertor convertor,
            List<NvsPassthroughConvertor.NvsPassthroughFileInfo> inputFiles,
            String outputPath,
            Hashtable<String, Object> configurations,
            int flags,
            NvsPassthroughConvertor.PassthroughConvertorCallback callback,
            Handler callbackHandler) {
        MeisheThreading.requireMainThread("NvsPassthroughConvertor.convertMediaFile");
        if (convertor == null || inputFiles == null || inputFiles.isEmpty()
                || outputPath == null || outputPath.isEmpty() || callback == null) {
            return -1;
        }
        convertor.setPassthroughConvertorCallback(callback, callbackHandler);
        return convertor.convertMediaFile(
                inputFiles,
                outputPath,
                configurations == null ? new Hashtable<String, Object>() : configurations,
                flags);
    }
}
