package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoFx;
import com.meicam.sdk.NvsVideoTrack;

import java.util.List;

public final class MeisheCompositionController {
    private MeisheCompositionController() {
    }

    public static boolean buildPictureInPicture(
            NvsTimeline timeline,
            String basePath,
            String overlayPath) {
        if (timeline == null || basePath == null || basePath.isEmpty()
                || overlayPath == null || overlayPath.isEmpty()) {
            return false;
        }
        NvsVideoTrack baseTrack = timeline.getVideoTrackByIndex(0);
        NvsVideoTrack overlayTrack = timeline.appendVideoTrack();
        if (baseTrack == null || overlayTrack == null) {
            return false;
        }
        NvsVideoClip baseClip = baseTrack.appendClip(basePath);
        NvsVideoClip overlayClip = overlayTrack.appendClip(overlayPath);
        if (baseClip == null || overlayClip == null) {
            return false;
        }
        baseClip.setImageMotionAnimationEnabled(false);
        overlayClip.setImageMotionAnimationEnabled(false);
        NvsVideoFx transform = overlayClip.appendBuiltinFx("Transform 2D");
        if (transform == null) {
            return false;
        }
        transform.setFloatVal("Scale X", 0.42);
        transform.setFloatVal("Scale Y", 0.42);
        transform.setFloatVal("Trans X", 160.0);
        transform.setFloatVal("Trans Y", -300.0);
        return true;
    }

    public static int buildQuickSplice(
            NvsTimeline timeline,
            List<String> mediaPaths,
            String transitionPackageId) {
        if (timeline == null || mediaPaths == null || mediaPaths.size() < 2) {
            return 0;
        }
        NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null) {
            return 0;
        }
        int appended = 0;
        for (String path : mediaPaths) {
            if (path == null || path.isEmpty()) {
                continue;
            }
            NvsVideoClip clip = track.appendClip(path);
            if (clip != null) {
                clip.setImageMotionAnimationEnabled(false);
                appended++;
            }
        }
        if (appended < 2) {
            return appended;
        }
        for (int index = 0; index < appended - 1; index++) {
            if (transitionPackageId != null && !transitionPackageId.isEmpty()) {
                track.setPackagedTransition(index, transitionPackageId);
            } else {
                track.setBuiltinTransition(index, "Fade");
            }
        }
        return appended;
    }
}
