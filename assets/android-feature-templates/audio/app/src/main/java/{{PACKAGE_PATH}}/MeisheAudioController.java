package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsAudioClip;
import com.meicam.sdk.NvsAudioFx;
import com.meicam.sdk.NvsAudioTrack;
import com.meicam.sdk.NvsAudioTransition;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsTrack;
import com.meicam.sdk.NvsVideoClip;

public final class MeisheAudioController {
    public NvsAudioTrack ensureAudioTrack(NvsTimeline timeline, int index) {
        MeisheThreading.requireMainThread("getAudioTrackByIndex");
        if (timeline == null || index < 0) {
            return null;
        }
        while (timeline.audioTrackCount() <= index) {
            if (timeline.appendAudioTrack() == null) {
                return null;
            }
        }
        return timeline.getAudioTrackByIndex(index);
    }

    public NvsAudioClip addClip(
            NvsAudioTrack track,
            String filePath,
            long inPointUs,
            long trimInUs,
            long trimOutUs) {
        MeisheThreading.requireMainThread("NvsAudioTrack.addClip");
        if (track == null || filePath == null || filePath.isEmpty() || trimOutUs <= trimInUs) {
            return null;
        }
        return track.addClip(filePath, Math.max(0, inPointUs), Math.max(0, trimInUs), trimOutUs);
    }

    public NvsAudioClip appendClip(NvsAudioTrack track, String filePath, long trimInUs, long trimOutUs) {
        MeisheThreading.requireMainThread("NvsAudioTrack.appendClip");
        if (track == null || filePath == null || filePath.isEmpty() || trimOutUs <= trimInUs) {
            return null;
        }
        return track.appendClip(filePath, Math.max(0, trimInUs), trimOutUs);
    }

    public NvsAudioClip appendClipDefault(NvsAudioTrack track, String filePath) {
        MeisheThreading.requireMainThread("NvsAudioTrack.appendClip");
        if (track == null || filePath == null || filePath.isEmpty()) {
            return null;
        }
        return track.appendClip(filePath);
    }

    public void clearTrack(NvsAudioTrack track) {
        MeisheThreading.requireMainThread("NvsAudioTrack.removeAllClips");
        if (track != null) {
            track.removeAllClips();
        }
    }

    public void setClipVolume(NvsAudioClip clip, float volume) {
        MeisheThreading.requireMainThread("NvsAudioClip.setVolumeGain");
        if (clip != null) {
            clip.setVolumeGain(volume, volume);
        }
    }

    public void setTrackVolume(NvsAudioTrack track, float volume) {
        MeisheThreading.requireMainThread("NvsAudioTrack.setVolumeGain");
        if (track != null) {
            track.setVolumeGain(volume, volume);
        }
    }

    public void setTrackStereoVolume(NvsTrack track, float leftVolume, float rightVolume) {
        MeisheThreading.requireMainThread("NvsTrack.setVolumeGain");
        if (track != null) {
            track.setVolumeGain(Math.max(0f, leftVolume), Math.max(0f, rightVolume));
        }
    }

    public NvsAudioFx appendFx(NvsAudioClip clip, String fxName) {
        MeisheThreading.requireMainThread("NvsAudioClip.appendFx");
        if (clip == null || fxName == null || fxName.isEmpty()) {
            return null;
        }
        return clip.appendFx(fxName);
    }

    public NvsAudioClip getClip(NvsAudioTrack track, int clipIndex) {
        MeisheThreading.requireMainThread("NvsAudioTrack.getClipByIndex");
        if (track == null || clipIndex < 0 || clipIndex >= track.getClipCount()) {
            return null;
        }
        return track.getClipByIndex(clipIndex);
    }

    public void setFadeDurations(
            NvsAudioClip clip,
            long fadeInDurationUs,
            long fadeOutDurationUs) {
        MeisheThreading.requireMainThread("configure audio fades");
        if (clip == null) {
            return;
        }
        clip.setFadeInDuration(Math.max(0, fadeInDurationUs));
        clip.setFadeOutDuration(Math.max(0, fadeOutDurationUs));
    }

    public NvsAudioClip addClipAt(
            NvsAudioTrack track,
            String filePath,
            long inPointUs) {
        MeisheThreading.requireMainThread("NvsAudioTrack.addClip");
        if (track == null || filePath == null || filePath.isEmpty()) {
            return null;
        }
        return track.addClip(filePath, Math.max(0, inPointUs));
    }

    public NvsAudioClip addVoiceoverClip(
            NvsAudioTrack track,
            String recordedFilePath,
            long timelineInPointUs,
            long trimInUs,
            long trimOutUs) {
        MeisheThreading.requireMainThread("add recorded voiceover clip");
        if (track == null || recordedFilePath == null || recordedFilePath.isEmpty()
                || timelineInPointUs < 0 || trimInUs < 0 || trimOutUs <= trimInUs) {
            return null;
        }
        return track.addClip(recordedFilePath, timelineInPointUs, trimInUs, trimOutUs);
    }

    public NvsAudioFx applyVideoClipEqualizer(
            NvsVideoClip clip,
            String bandKey,
            double gain) {
        MeisheThreading.requireMainThread("configure Audio EQ");
        if (clip == null || bandKey == null || bandKey.isEmpty()) {
            return null;
        }
        NvsAudioFx equalizer = null;
        for (int index = 0; index < clip.getAudioFxCount(); index++) {
            NvsAudioFx candidate = clip.getAudioFxByIndex(index);
            if (candidate != null && "Audio EQ".equals(candidate.getBuiltinAudioFxName())) {
                equalizer = candidate;
                break;
            }
        }
        if (equalizer == null) {
            equalizer = clip.appendAudioFx("Audio EQ");
        }
        if (equalizer != null) {
            equalizer.setFloatVal(bandKey, gain);
        }
        return equalizer;
    }

    public NvsAudioFx appendAudioClipFx(NvsAudioClip clip, String builtinFxName) {
        MeisheThreading.requireMainThread("NvsAudioClip.appendFx");
        if (clip == null || builtinFxName == null || builtinFxName.isEmpty()) {
            return null;
        }
        NvsAudioFx fx = clip.appendFx(builtinFxName);
        return fx != null && builtinFxName.equals(fx.getBuiltinAudioFxName()) ? fx : null;
    }

    public NvsAudioFx replaceAudioClipFx(
            NvsAudioClip clip,
            int fxIndex,
            String builtinFxName) {
        MeisheThreading.requireMainThread("replace audio clip FX");
        if (clip == null || fxIndex < 0 || builtinFxName == null || builtinFxName.isEmpty()) {
            return null;
        }
        if (clip.getFxByIndex(fxIndex) != null && !clip.removeFx(fxIndex)) {
            return null;
        }
        NvsAudioFx inserted = clip.insertFx(builtinFxName, fxIndex);
        return inserted == null ? null : clip.getFxByIndex(fxIndex);
    }

    public NvsAudioTransition configureAudioTransition(
            NvsAudioTrack track,
            int sourceClipIndex,
            String builtinTransitionName) {
        MeisheThreading.requireMainThread("configure audio transition");
        if (track == null || sourceClipIndex < 0
                || builtinTransitionName == null || builtinTransitionName.isEmpty()) {
            return null;
        }
        NvsAudioTransition transition = track.setBuiltinTransition(
                sourceClipIndex,
                builtinTransitionName);
        return transition == null
                ? null
                : track.getTransitionWithSourceClipIndex(sourceClipIndex);
    }
}
