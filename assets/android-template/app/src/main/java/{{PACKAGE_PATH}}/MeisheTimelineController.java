package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsAudioResolution;
import com.meicam.sdk.NvsClip;
import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsRational;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsTrack;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoResolution;
import com.meicam.sdk.NvsVideoTrack;

import java.util.List;

public final class MeisheTimelineController {
    private final NvsStreamingContext streamingContext;
    private NvsTimeline timeline;

    public MeisheTimelineController(NvsStreamingContext streamingContext) {
        this.streamingContext = streamingContext;
    }

    public NvsTimeline createTimeline(int width, int height) {
        MeisheThreading.requireMainThread("createTimeline");
        NvsVideoResolution videoRes = new NvsVideoResolution();
        videoRes.imageWidth = width;
        videoRes.imageHeight = height;
        videoRes.imagePAR = new NvsRational(1, 1);
        NvsAudioResolution audioRes = new NvsAudioResolution();
        audioRes.sampleRate = 44100;
        audioRes.channelCount = 2;
        timeline = streamingContext.createTimeline(videoRes, new NvsRational(30, 1), audioRes);
        if (timeline != null) {
            timeline.appendVideoTrack();
            timeline.appendAudioTrack();
        }
        return timeline;
    }

    public NvsVideoClip appendClip(String filePath) {
        MeisheThreading.requireMainThread("appendClip");
        if (timeline == null || filePath == null || filePath.isEmpty()) {
            throw new IllegalStateException("Create a timeline before adding clips");
        }
        NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
        if (videoTrack == null) {
            videoTrack = timeline.appendVideoTrack();
        }
        NvsVideoClip clip = videoTrack == null ? null : videoTrack.appendClip(filePath);
        if (clip != null && clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {
            clip.setImageMotionAnimationEnabled(false);
        }
        return clip;
    }

    public int appendMediaList(List<String> mediaPaths) {
        MeisheThreading.requireMainThread("appendMediaList");
        if (timeline == null || mediaPaths == null || mediaPaths.isEmpty()) {
            return 0;
        }
        NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
        if (videoTrack == null) {
            videoTrack = timeline.appendVideoTrack();
        }
        if (videoTrack == null) {
            return 0;
        }
        int appended = 0;
        for (String filePath : mediaPaths) {
            if (filePath == null || filePath.isEmpty() || !new java.io.File(filePath).isFile()) {
                continue;
            }
            NvsVideoClip clip = videoTrack.appendClip(filePath);
            if (clip == null) {
                continue;
            }
            if (clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {
                clip.setImageMotionAnimationEnabled(false);
            }
            appended++;
        }
        return appended;
    }

    public void connectPreview(NvsLiveWindow liveWindow) {
        MeisheThreading.requireMainThread("connectTimelineWithLiveWindow");
        streamingContext.connectTimelineWithLiveWindow(timeline, liveWindow);
    }

    public NvsTimeline getTimeline() {
        return timeline;
    }

    public NvsTimeline createTimelineWithFlags(int width, int height, int flags) {
        MeisheThreading.requireMainThread("NvsStreamingContext.createTimeline");
        if (streamingContext == null || width <= 0 || height <= 0) {
            return null;
        }
        NvsVideoResolution videoRes = new NvsVideoResolution();
        videoRes.imageWidth = width;
        videoRes.imageHeight = height;
        videoRes.imagePAR = new NvsRational(1, 1);
        NvsAudioResolution audioRes = new NvsAudioResolution();
        audioRes.sampleRate = 44100;
        audioRes.channelCount = 2;
        timeline = streamingContext.createTimeline(
                videoRes,
                new NvsRational(30, 1),
                audioRes,
                flags);
        return timeline;
    }

    public NvsVideoClip getVideoClip(int clipIndex) {
        MeisheThreading.requireMainThread("NvsVideoTrack.getClipByIndex");
        if (timeline == null || clipIndex < 0) {
            return null;
        }
        NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null || clipIndex >= track.getClipCount()) {
            return null;
        }
        return track.getClipByIndex(clipIndex);
    }

    public NvsVideoResolution getVideoResolution() {
        MeisheThreading.requireMainThread("NvsTimeline.getVideoRes");
        return timeline == null ? null : timeline.getVideoRes();
    }

    public void setThemeMusicVolume(float volume) {
        MeisheThreading.requireMainThread("NvsTimeline.setThemeMusicVolumeGain");
        if (timeline != null) {
            float safeVolume = Math.max(0f, volume);
            timeline.setThemeMusicVolumeGain(safeVolume, safeVolume);
        }
    }

    public boolean removeTimeline() {
        MeisheThreading.requireMainThread("NvsStreamingContext.removeTimeline");
        if (timeline == null) {
            return true;
        }
        streamingContext.stop();
        if (!streamingContext.removeTimeline(timeline)) {
            return false;
        }
        timeline = null;
        return true;
    }

    public NvsTimeline createTemplateTimeline(
            String templateId,
            java.util.List<NvsStreamingContext.templateFootageInfo> footage) {
        MeisheThreading.requireMainThread("NvsStreamingContext.createTimeline");
        if (templateId == null || templateId.isEmpty() || footage == null || footage.isEmpty()) {
            return null;
        }
        timeline = streamingContext.createTimeline(templateId, footage);
        return timeline;
    }

    public NvsTimeline createTemplateTimelineWithFlags(
            String templateId,
            java.util.List<NvsStreamingContext.templateFootageInfo> footage,
            int flags) {
        MeisheThreading.requireMainThread("NvsStreamingContext.createTimeline");
        if (templateId == null || templateId.isEmpty() || footage == null || footage.isEmpty()) {
            return null;
        }
        timeline = streamingContext.createTimeline(templateId, footage, flags);
        return timeline;
    }

    public NvsTimeline createTemplateTimelineConfigured(
            String templateId,
            List<NvsStreamingContext.templateFootageInfo> footage,
            int flags,
            NvsRational videoFps,
            NvsAudioResolution audioResolution) {
        MeisheThreading.requireMainThread("NvsStreamingContext.createTimeline");
        if (streamingContext == null || templateId == null || templateId.isEmpty()
                || footage == null || footage.isEmpty()
                || videoFps == null || audioResolution == null) {
            return null;
        }
        timeline = streamingContext.createTimeline(
                templateId,
                footage,
                flags,
                videoFps,
                audioResolution);
        return timeline;
    }

    public NvsVideoClip appendTrimmedClip(
            String filePath,
            long trimInUs,
            long trimOutUs) {
        MeisheThreading.requireMainThread("NvsVideoTrack.appendClip");
        if (timeline == null || filePath == null || filePath.isEmpty() || trimOutUs <= trimInUs) {
            return null;
        }
        NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null) {
            track = timeline.appendVideoTrack();
        }
        return track.appendClip(filePath, Math.max(0, trimInUs), trimOutUs);
    }

    public boolean changeClipSpeed(NvsClip clip, double newSpeed) {
        MeisheThreading.requireMainThread("NvsClip.changeSpeed");
        if (clip == null || Double.isNaN(newSpeed) || Double.isInfinite(newSpeed)
                || newSpeed <= 0.0) {
            return false;
        }
        clip.changeSpeed(newSpeed);
        return true;
    }

    public long changeClipTrimIn(NvsClip clip, long newTrimInPoint, boolean affectSibling) {
        MeisheThreading.requireMainThread("NvsClip.changeTrimInPoint");
        if (clip == null || newTrimInPoint < 0) {
            return -1;
        }
        return clip.changeTrimInPoint(newTrimInPoint, affectSibling);
    }

    public boolean moveClipToTimelinePosition(
            NvsTrack track,
            int clipIndex,
            long targetTimelinePos,
            boolean isInsertTarget,
            boolean keepSpace) {
        MeisheThreading.requireMainThread("NvsTrack.moveClip");
        return track != null
                && clipIndex >= 0
                && clipIndex < track.getClipCount()
                && targetTimelinePos >= 0
                && track.moveClip(clipIndex, targetTimelinePos, isInsertTarget, keepSpace);
    }

    public NvsVideoClip addClipAtTimelinePosition(
            NvsVideoTrack track,
            String filePath,
            long timelinePositionUs,
            long trimInUs,
            long trimOutUs) {
        MeisheThreading.requireMainThread("NvsVideoTrack.addClip");
        if (track == null || filePath == null || filePath.isEmpty()
                || timelinePositionUs < 0 || trimInUs < 0 || trimOutUs <= trimInUs) {
            return null;
        }
        NvsVideoClip clip = track.addClip(filePath, timelinePositionUs, trimInUs, trimOutUs);
        return clip == null ? null : track.getClipByTimelinePosition(timelinePositionUs);
    }

    public NvsVideoClip insertClipAtIndex(
            NvsVideoTrack track,
            String filePath,
            long trimInUs,
            long trimOutUs,
            int clipIndex) {
        MeisheThreading.requireMainThread("NvsVideoTrack.insertClip");
        if (track == null || filePath == null || filePath.isEmpty()
                || trimInUs < 0 || trimOutUs <= trimInUs
                || clipIndex < 0 || clipIndex > track.getClipCount()) {
            return null;
        }
        return track.insertClip(filePath, trimInUs, trimOutUs, clipIndex);
    }

    public boolean configureTimelineStructure(
            NvsTimeline targetTimeline,
            int width,
            int height,
            long audioFadeOutDurationUs,
            boolean removeLastVideoTrack,
            boolean removeLastAudioTrack) {
        MeisheThreading.requireMainThread("configure timeline structure");
        if (streamingContext == null || targetTimeline == null
                || width <= 0 || height <= 0 || audioFadeOutDurationUs < 0) {
            return false;
        }
        streamingContext.stop();
        if (!targetTimeline.changeVideoSize(width, height)) {
            return false;
        }
        targetTimeline.setAudioFadeOutDuration(audioFadeOutDurationUs);
        if (removeLastVideoTrack && targetTimeline.videoTrackCount() > 1
                && !targetTimeline.removeVideoTrack(targetTimeline.videoTrackCount() - 1)) {
            return false;
        }
        if (removeLastAudioTrack && targetTimeline.audioTrackCount() > 1
                && !targetTimeline.removeAudioTrack(targetTimeline.audioTrackCount() - 1)) {
            return false;
        }
        return targetTimeline.getAudioFadeOutDuration() == audioFadeOutDurationUs;
    }
}
