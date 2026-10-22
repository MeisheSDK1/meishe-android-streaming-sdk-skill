package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsAudioResolution;
import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsClipCaption;
import com.meicam.sdk.NvsClipCompoundCaption;
import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsObject;
import com.meicam.sdk.NvsRational;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsTimelineCaption;
import com.meicam.sdk.NvsTimelineCompoundCaption;
import com.meicam.sdk.NvsTrackCaption;
import com.meicam.sdk.NvsTrackCompoundCaption;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;

import java.io.File;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.HashSet;
import java.util.IdentityHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Hashtable;

public final class MeisheTemplateWorkflowController {
    public List<NvsAssetPackageManager.NvsTemplateFootageDesc> getTemplateFootages(
            NvsStreamingContext streamingContext,
            String templateId) {
        MeisheThreading.requireMainThread("get template footages");
        if (streamingContext == null || templateId == null || templateId.isEmpty()) {
            return Collections.emptyList();
        }
        NvsAssetPackageManager packageManager = streamingContext.getAssetPackageManager();
        if (packageManager == null) {
            return Collections.emptyList();
        }
        List<NvsAssetPackageManager.NvsTemplateFootageDesc> footages =
                packageManager.getTemplateFootages(templateId);
        return footages == null ? Collections.emptyList() : new ArrayList<>(footages);
    }

    public List<NvsAssetPackageManager.NvsTemplateCaptionDesc> getTemplateCaptions(
            NvsStreamingContext streamingContext,
            String templateId) {
        MeisheThreading.requireMainThread("get template captions");
        if (streamingContext == null || templateId == null || templateId.isEmpty()) {
            return Collections.emptyList();
        }
        NvsAssetPackageManager packageManager = streamingContext.getAssetPackageManager();
        if (packageManager == null) {
            return Collections.emptyList();
        }
        List<NvsAssetPackageManager.NvsTemplateCaptionDesc> captions =
                packageManager.getTemplateCaptions(templateId);
        return captions == null ? Collections.emptyList() : new ArrayList<>(captions);
    }

    public List<NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc> getTemplateCompoundCaptions(
            NvsStreamingContext streamingContext,
            String templateId) {
        MeisheThreading.requireMainThread("get template compound captions");
        if (streamingContext == null || templateId == null || templateId.isEmpty()) {
            return Collections.emptyList();
        }
        NvsAssetPackageManager packageManager = streamingContext.getAssetPackageManager();
        if (packageManager == null) {
            return Collections.emptyList();
        }
        List<NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc> captions =
                packageManager.getTemplateCompoundCaptions(templateId);
        return captions == null ? Collections.emptyList() : new ArrayList<>(captions);
    }

    public List<String> listReplaceableFootageIds(
            List<NvsAssetPackageManager.NvsTemplateFootageDesc> descriptors) {
        if (descriptors == null || descriptors.isEmpty()) {
            return Collections.emptyList();
        }
        ArrayList<String> ids = new ArrayList<>();
        Set<String> seen = new HashSet<>();
        Deque<NvsAssetPackageManager.NvsTemplateFootageDesc> pending =
                new ArrayDeque<>(descriptors);
        while (!pending.isEmpty()) {
            NvsAssetPackageManager.NvsTemplateFootageDesc descriptor = pending.removeFirst();
            if (descriptor == null) {
                continue;
            }
            if (descriptor.timelineClipFootages != null) {
                pending.addAll(descriptor.timelineClipFootages);
            }
            if (descriptor.canReplace && descriptor.id != null && !descriptor.id.isEmpty()
                    && seen.add(descriptor.id)) {
                ids.add(descriptor.id);
            }
        }
        return ids;
    }

    public List<String> listReverseFootageIds(
            List<NvsAssetPackageManager.NvsTemplateFootageDesc> descriptors) {
        if (descriptors == null || descriptors.isEmpty()) {
            return Collections.emptyList();
        }
        ArrayList<String> ids = new ArrayList<>();
        Set<String> seen = new HashSet<>();
        Deque<NvsAssetPackageManager.NvsTemplateFootageDesc> pending =
                new ArrayDeque<>(descriptors);
        while (!pending.isEmpty()) {
            NvsAssetPackageManager.NvsTemplateFootageDesc descriptor = pending.removeFirst();
            if (descriptor == null) {
                continue;
            }
            if (descriptor.timelineClipFootages != null) {
                pending.addAll(descriptor.timelineClipFootages);
            }
            boolean needsReverse = false;
            if (descriptor.correspondingClipInfos != null) {
                for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo
                        : descriptor.correspondingClipInfos) {
                    needsReverse |= clipInfo != null && clipInfo.needReverse;
                }
            }
            if (descriptor.canReplace && needsReverse && descriptor.id != null
                    && !descriptor.id.isEmpty() && seen.add(descriptor.id)) {
                ids.add(descriptor.id);
            }
        }
        return ids;
    }

    public List<String> validateFootageSelections(
            List<NvsAssetPackageManager.NvsTemplateFootageDesc> descriptors,
            Map<String, String> mediaByFootageId,
            Map<String, String> reverseMediaByFootageId) {
        ArrayList<String> failures = new ArrayList<>();
        if (descriptors == null || descriptors.isEmpty()) {
            failures.add("template has no footage descriptors");
            return failures;
        }
        Map<String, String> media = mediaByFootageId == null
                ? Collections.emptyMap() : mediaByFootageId;
        Map<String, String> reverseMedia = reverseMediaByFootageId == null
                ? Collections.emptyMap() : reverseMediaByFootageId;
        Set<String> checked = new HashSet<>();
        Deque<NvsAssetPackageManager.NvsTemplateFootageDesc> pending =
                new ArrayDeque<>(descriptors);
        while (!pending.isEmpty()) {
            NvsAssetPackageManager.NvsTemplateFootageDesc descriptor = pending.removeFirst();
            if (descriptor == null) {
                continue;
            }
            if (descriptor.timelineClipFootages != null) {
                pending.addAll(descriptor.timelineClipFootages);
            }
            if (!descriptor.canReplace || descriptor.id == null || descriptor.id.isEmpty()
                    || !checked.add(descriptor.id)) {
                continue;
            }
            String mediaPath = media.get(descriptor.id);
            if (mediaPath == null || mediaPath.isEmpty() || !new File(mediaPath).isFile()) {
                failures.add(descriptor.id + ": replacement media is missing");
                continue;
            }
            boolean needsReverse = false;
            if (descriptor.correspondingClipInfos != null) {
                for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo
                        : descriptor.correspondingClipInfos) {
                    needsReverse |= clipInfo != null && clipInfo.needReverse;
                }
            }
            String reversePath = reverseMedia.get(descriptor.id);
            if (needsReverse && (reversePath == null || reversePath.isEmpty()
                    || !new File(reversePath).isFile())) {
                failures.add(descriptor.id + ": reverse media is missing");
            }
        }
        return failures;
    }

    public List<NvsStreamingContext.templateFootageInfo> buildTemplateFootage(
            List<NvsAssetPackageManager.NvsTemplateFootageDesc> descriptors,
            Map<String, String> mediaByFootageId,
            Map<String, String> reverseMediaByFootageId) {
        if (descriptors == null || descriptors.isEmpty() || mediaByFootageId == null) {
            return Collections.emptyList();
        }
        Map<String, String> reverseMedia = reverseMediaByFootageId == null
                ? Collections.emptyMap() : reverseMediaByFootageId;
        ArrayList<NvsStreamingContext.templateFootageInfo> result = new ArrayList<>();
        Set<String> mapped = new HashSet<>();
        Deque<NvsAssetPackageManager.NvsTemplateFootageDesc> pending =
                new ArrayDeque<>(descriptors);
        while (!pending.isEmpty()) {
            NvsAssetPackageManager.NvsTemplateFootageDesc descriptor = pending.removeFirst();
            if (descriptor == null) {
                continue;
            }
            if (descriptor.timelineClipFootages != null) {
                pending.addAll(descriptor.timelineClipFootages);
            }
            if (!descriptor.canReplace || descriptor.id == null || descriptor.id.isEmpty()
                    || !mapped.add(descriptor.id)) {
                continue;
            }
            String mediaPath = mediaByFootageId.get(descriptor.id);
            if (mediaPath == null || mediaPath.isEmpty() || !new File(mediaPath).isFile()) {
                return Collections.emptyList();
            }
            boolean needsReverse = false;
            if (descriptor.correspondingClipInfos != null) {
                for (NvsAssetPackageManager.NvsTemplateFootageCorrespondingClipInfo clipInfo
                        : descriptor.correspondingClipInfos) {
                    needsReverse |= clipInfo != null && clipInfo.needReverse;
                }
            }
            String reversePath = reverseMedia.get(descriptor.id);
            if (needsReverse && (reversePath == null || reversePath.isEmpty()
                    || !new File(reversePath).isFile())) {
                return Collections.emptyList();
            }
            NvsStreamingContext.templateFootageInfo footageInfo =
                    new NvsStreamingContext.templateFootageInfo();
            footageInfo.footageId = descriptor.id;
            footageInfo.filePath = mediaPath;
            footageInfo.reverseFilePath = reversePath == null ? "" : reversePath;
            result.add(footageInfo);
        }
        return result;
    }

    public NvsTimeline createTemplateEditorTimeline(
            NvsStreamingContext streamingContext,
            String templateId,
            List<NvsStreamingContext.templateFootageInfo> footage) {
        MeisheThreading.requireMainThread("create template editor timeline");
        if (streamingContext == null || templateId == null || templateId.isEmpty()
                || footage == null || footage.isEmpty()) {
            return null;
        }
        return streamingContext.createTimeline(templateId, footage);
    }

    public NvsTimeline createCutSameTimeline(
            NvsStreamingContext streamingContext,
            String templateId,
            List<NvsStreamingContext.templateFootageInfo> footage,
            int timelineFlags) {
        MeisheThreading.requireMainThread("create CutSame timeline");
        if (streamingContext == null || templateId == null || templateId.isEmpty()
                || footage == null || footage.isEmpty()) {
            return null;
        }
        return streamingContext.createTimeline(templateId, footage, timelineFlags);
    }

    public NvsTimeline createConfiguredTemplateTimeline(
            NvsStreamingContext streamingContext,
            String templateId,
            List<NvsStreamingContext.templateFootageInfo> footage,
            int timelineFlags,
            NvsRational videoFps,
            NvsAudioResolution audioResolution) {
        MeisheThreading.requireMainThread("create configured template timeline");
        if (streamingContext == null || templateId == null || templateId.isEmpty()
                || footage == null || footage.isEmpty() || videoFps == null
                || audioResolution == null) {
            return null;
        }
        return streamingContext.createTimeline(
                templateId,
                footage,
                timelineFlags,
                videoFps,
                audioResolution);
    }

    /**
     * @deprecated Demo Mimo archives are JSON workflows, not SDK template packages. Use
     * {@link MeisheMimoWorkflowController} for Mimo, or
     * {@link #createConfiguredTemplateTimeline} for the SDK template overload.
     */
    @Deprecated
    public NvsTimeline createMimoTimeline(
            NvsStreamingContext streamingContext,
            String templateId,
            List<NvsStreamingContext.templateFootageInfo> footage,
            int timelineFlags,
            NvsRational videoFps,
            NvsAudioResolution audioResolution) {
        return createConfiguredTemplateTimeline(
                streamingContext,
                templateId,
                footage,
                timelineFlags,
                videoFps,
                audioResolution);
    }

    public int replaceTemplateCaptionTexts(
            NvsTimeline timeline,
            Map<String, String> textByReplaceId) {
        MeisheThreading.requireMainThread("replace template captions");
        if (timeline == null || textByReplaceId == null || textByReplaceId.isEmpty()) {
            return 0;
        }
        int replaced = 0;
        Deque<NvsTimeline> pending = new ArrayDeque<>();
        Set<NvsTimeline> visited = Collections.newSetFromMap(
                new IdentityHashMap<NvsTimeline, Boolean>());
        pending.add(timeline);
        while (!pending.isEmpty()) {
            NvsTimeline current = pending.removeFirst();
            if (current == null || !visited.add(current)) {
                continue;
            }
            NvsTimelineCaption timelineCaption = current.getFirstCaption();
            while (timelineCaption != null) {
                String replacement = textByReplaceId.get(
                        timelineCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID));
                if (replacement != null) {
                    timelineCaption.setText(replacement);
                    replaced++;
                }
                timelineCaption = current.getNextCaption(timelineCaption);
            }
            for (int trackIndex = 0; trackIndex < current.videoTrackCount(); trackIndex++) {
                NvsVideoTrack track = current.getVideoTrackByIndex(trackIndex);
                if (track == null) {
                    continue;
                }
                NvsTrackCaption trackCaption = track.getFirstCaption();
                while (trackCaption != null) {
                    String replacement = textByReplaceId.get(
                            trackCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID));
                    if (replacement != null) {
                        trackCaption.setText(replacement);
                        replaced++;
                    }
                    trackCaption = track.getNextCaption(trackCaption);
                }
                for (int clipIndex = 0; clipIndex < track.getClipCount(); clipIndex++) {
                    NvsVideoClip clip = track.getClipByIndex(clipIndex);
                    if (clip == null) {
                        continue;
                    }
                    NvsClipCaption clipCaption = clip.getFirstCaption();
                    while (clipCaption != null) {
                        String replacement = textByReplaceId.get(
                                clipCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID));
                        if (replacement != null) {
                            clipCaption.setText(replacement);
                            replaced++;
                        }
                        clipCaption = clip.getNextCaption(clipCaption);
                    }
                    NvsTimeline internalTimeline = clip.getInternalTimeline();
                    if (internalTimeline != null) {
                        pending.addLast(internalTimeline);
                    }
                }
            }
        }
        return replaced;
    }

    public int replaceTemplateCompoundCaptionTexts(
            NvsTimeline timeline,
            Map<String, List<String>> textByReplaceId) {
        MeisheThreading.requireMainThread("replace template compound captions");
        if (timeline == null || textByReplaceId == null || textByReplaceId.isEmpty()) {
            return 0;
        }
        int replaced = 0;
        Deque<NvsTimeline> pending = new ArrayDeque<>();
        Set<NvsTimeline> visited = Collections.newSetFromMap(
                new IdentityHashMap<NvsTimeline, Boolean>());
        pending.add(timeline);
        while (!pending.isEmpty()) {
            NvsTimeline current = pending.removeFirst();
            if (current == null || !visited.add(current)) {
                continue;
            }
            NvsTimelineCompoundCaption timelineCaption = current.getFirstCompoundCaption();
            while (timelineCaption != null) {
                List<String> replacements = textByReplaceId.get(
                        timelineCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID));
                if (replacements != null) {
                    int count = Math.min(timelineCaption.getCaptionCount(), replacements.size());
                    for (int index = 0; index < count; index++) {
                        if (replacements.get(index) != null) {
                            timelineCaption.setText(index, replacements.get(index));
                            replaced++;
                        }
                    }
                }
                timelineCaption = current.getNextCaption(timelineCaption);
            }
            for (int trackIndex = 0; trackIndex < current.videoTrackCount(); trackIndex++) {
                NvsVideoTrack track = current.getVideoTrackByIndex(trackIndex);
                if (track == null) {
                    continue;
                }
                NvsTrackCompoundCaption trackCaption = track.getFirstCompoundCaption();
                while (trackCaption != null) {
                    List<String> replacements = textByReplaceId.get(
                            trackCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID));
                    if (replacements != null) {
                        int count = Math.min(trackCaption.getCaptionCount(), replacements.size());
                        for (int index = 0; index < count; index++) {
                            if (replacements.get(index) != null) {
                                trackCaption.setText(index, replacements.get(index));
                                replaced++;
                            }
                        }
                    }
                    trackCaption = track.getNextCaption(trackCaption);
                }
                for (int clipIndex = 0; clipIndex < track.getClipCount(); clipIndex++) {
                    NvsVideoClip clip = track.getClipByIndex(clipIndex);
                    if (clip == null) {
                        continue;
                    }
                    NvsClipCompoundCaption clipCaption = clip.getFirstCompoundCaption();
                    while (clipCaption != null) {
                        List<String> replacements = textByReplaceId.get(
                                clipCaption.getTemplateAttachment(NvsObject.TEMPLATE_KEY_REPLACE_ID));
                        if (replacements != null) {
                            int count = Math.min(clipCaption.getCaptionCount(), replacements.size());
                            for (int index = 0; index < count; index++) {
                                if (replacements.get(index) != null) {
                                    clipCaption.setText(index, replacements.get(index));
                                    replaced++;
                                }
                            }
                        }
                        clipCaption = clip.getNextCaption(clipCaption);
                    }
                    NvsTimeline internalTimeline = clip.getInternalTimeline();
                    if (internalTimeline != null) {
                        pending.addLast(internalTimeline);
                    }
                }
            }
        }
        return replaced;
    }

    public boolean reconnectTemplatePreview(
            NvsStreamingContext streamingContext,
            NvsTimeline timeline,
            NvsLiveWindow liveWindow,
            long positionUs,
            int seekFlags) {
        MeisheThreading.requireMainThread("refresh template preview");
        if (streamingContext == null || timeline == null || liveWindow == null) {
            return false;
        }
        streamingContext.stop();
        if (!streamingContext.connectTimelineWithLiveWindow(timeline, liveWindow)) {
            return false;
        }
        long safePosition = Math.max(0, Math.min(positionUs, timeline.getDuration()));
        return streamingContext.seekTimeline(
                timeline,
                safePosition,
                NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                seekFlags);
    }

    public boolean playTemplate(
            NvsStreamingContext streamingContext,
            NvsTimeline timeline,
            long startUs,
            long endUs,
            int playbackFlags) {
        MeisheThreading.requireMainThread("play template timeline");
        if (streamingContext == null || timeline == null || timeline.getDuration() <= 0) {
            return false;
        }
        long safeStart = Math.max(0, Math.min(startUs, timeline.getDuration()));
        long safeEnd = endUs > safeStart
                ? Math.min(endUs, timeline.getDuration())
                : timeline.getDuration();
        if (safeEnd <= safeStart) {
            return false;
        }
        return streamingContext.playbackTimeline(
                timeline,
                safeStart,
                safeEnd,
                NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                true,
                playbackFlags);
    }

    public long currentTemplatePosition(
            NvsStreamingContext streamingContext,
            NvsTimeline timeline) {
        MeisheThreading.requireMainThread("read template timeline position");
        if (streamingContext == null || timeline == null) {
            return 0;
        }
        return Math.max(
                0,
                Math.min(
                        streamingContext.getTimelineCurrentPosition(timeline),
                        timeline.getDuration()));
    }

    public boolean registerTemplateCompileCallbacks(
            NvsStreamingContext streamingContext,
            NvsStreamingContext.CompileCallback compileCallback,
            NvsStreamingContext.CompileCallback2 completionCallback) {
        MeisheThreading.requireMainThread("register template compile callbacks");
        if (streamingContext == null || compileCallback == null || completionCallback == null) {
            return false;
        }
        streamingContext.setCompileCallback(compileCallback);
        streamingContext.setCompileCallback2(completionCallback);
        return true;
    }

    public boolean exportTemplate(
            NvsStreamingContext streamingContext,
            NvsTimeline timeline,
            long startUs,
            long endUs,
            String outputPath,
            int resolutionGrade,
            int bitrateGrade,
            Hashtable<String, Object> compileConfigurations,
            int compileFlags) {
        MeisheThreading.requireMainThread("export template timeline");
        if (streamingContext == null || timeline == null || outputPath == null
                || outputPath.isEmpty() || startUs < 0 || endUs <= startUs
                || endUs > timeline.getDuration()) {
            return false;
        }
        streamingContext.stop();
        Hashtable<String, Object> safeConfigurations = compileConfigurations == null
                ? new Hashtable<String, Object>()
                : compileConfigurations;
        return streamingContext.compileTimeline(
                timeline,
                startUs,
                endUs,
                outputPath,
                resolutionGrade,
                bitrateGrade,
                safeConfigurations,
                compileFlags);
    }

    public boolean applyTheme(
            NvsTimeline timeline,
            String themePackageId,
            String title,
            String trailer,
            float musicVolume) {
        MeisheThreading.requireMainThread("apply timeline theme");
        if (timeline == null || themePackageId == null || themePackageId.isEmpty()) {
            return false;
        }
        timeline.removeCurrentTheme();
        if (title != null) {
            timeline.setThemeTitleCaptionText(title);
        }
        if (trailer != null) {
            timeline.setThemeTrailerCaptionText(trailer);
        }
        if (!timeline.applyTheme(themePackageId)) {
            return false;
        }
        float safeVolume = Math.max(0f, musicVolume);
        timeline.setThemeMusicVolumeGain(safeVolume, safeVolume);
        return true;
    }
}
