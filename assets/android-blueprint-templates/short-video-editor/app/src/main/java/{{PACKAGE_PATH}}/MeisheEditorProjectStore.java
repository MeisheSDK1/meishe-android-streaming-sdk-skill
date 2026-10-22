package {{PACKAGE_NAME}};

import android.content.Context;
import android.graphics.PointF;

import com.meicam.sdk.NvsAudioClip;
import com.meicam.sdk.NvsAudioTrack;
import com.meicam.sdk.NvsCaption;
import com.meicam.sdk.NvsColor;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsTimelineAnimatedSticker;
import com.meicam.sdk.NvsTimelineCaption;
import com.meicam.sdk.NvsTimelineCompoundCaption;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoFx;
import com.meicam.sdk.NvsVideoTrack;
import com.meicam.sdk.NvsVideoTransition;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.UUID;

public final class MeisheEditorProjectStore {
    private static final int EDITOR_STATE_VERSION = 2;

    private MeisheEditorProjectStore() {
    }

    public static String emptyEditorState() {
        return editorObject().toString();
    }

    public static String extractEditorState(String serializedProjectState) {
        if (serializedProjectState == null || serializedProjectState.isEmpty()) {
            return "{\"version\":1}";
        }
        try {
            JSONObject editor = new JSONObject(serializedProjectState).optJSONObject("editor");
            return editor == null
                    ? "{\"version\":1}"
                    : editor.toString();
        } catch (JSONException exception) {
            return "{\"version\":1}";
        }
    }

    public static boolean saveEditorState(
            Context context,
            String projectId,
            String serializedEditorState) {
        if (context == null || projectId == null || projectId.isEmpty()
                || serializedEditorState == null || serializedEditorState.isEmpty()) {
            return false;
        }
        try {
            android.content.SharedPreferences preferences = context.getSharedPreferences(
                    "meishe_projects",
                    Context.MODE_PRIVATE);
            String current = preferences.getString(projectId, "");
            JSONObject project = current == null || current.isEmpty()
                    ? new JSONObject()
                    : new JSONObject(current);
            project.put("version", Math.max(2, project.optInt("version", 0)));
            project.put("editor", new JSONObject(serializedEditorState));
            return preferences.edit()
                    .putString(projectId, project.toString())
                    .putString("latest_project_id", projectId)
                    .commit();
        } catch (JSONException exception) {
            return false;
        }
    }

    public static int clearEditorFeatures(NvsTimeline timeline) {
        if (timeline == null) {
            return 0;
        }
        int cleared = 0;
        timeline.removeCurrentTheme();
        NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
        if (videoTrack != null) {
            for (int clipIndex = 0; clipIndex < videoTrack.getClipCount(); clipIndex++) {
                NvsVideoClip clip = videoTrack.getClipByIndex(clipIndex);
                if (clip != null) {
                    cleared += clip.getFxCount();
                    clip.removeAllFx();
                }
            }
            for (int sourceClipIndex = 0;
                    sourceClipIndex + 1 < videoTrack.getClipCount();
                    sourceClipIndex++) {
                if (videoTrack.getTransitionBySourceClipIndex(sourceClipIndex) != null) {
                    cleared++;
                }
                videoTrack.setBuiltinTransition(sourceClipIndex, "");
            }
        }
        List<NvsTimelineCaption> captions = new ArrayList<>();
        for (NvsTimelineCaption caption = timeline.getFirstCaption();
                caption != null;
                caption = timeline.getNextCaption(caption)) {
            captions.add(caption);
        }
        for (NvsTimelineCaption caption : captions) {
            timeline.removeCaption(caption);
            cleared++;
        }
        List<NvsTimelineAnimatedSticker> stickers = new ArrayList<>();
        for (NvsTimelineAnimatedSticker sticker = timeline.getFirstAnimatedSticker();
                sticker != null;
                sticker = timeline.getNextAnimatedSticker(sticker)) {
            stickers.add(sticker);
        }
        for (NvsTimelineAnimatedSticker sticker : stickers) {
            timeline.removeAnimatedSticker(sticker);
            cleared++;
        }
        List<NvsTimelineCompoundCaption> compoundCaptions = new ArrayList<>();
        for (NvsTimelineCompoundCaption caption = timeline.getFirstCompoundCaption();
                caption != null;
                caption = timeline.getNextCaption(caption)) {
            compoundCaptions.add(caption);
        }
        for (NvsTimelineCompoundCaption caption : compoundCaptions) {
            timeline.removeCompoundCaption(caption);
            cleared++;
        }
        for (int trackIndex = 0; trackIndex < timeline.audioTrackCount(); trackIndex++) {
            NvsAudioTrack audioTrack = timeline.getAudioTrackByIndex(trackIndex);
            if (audioTrack != null) {
                cleared += audioTrack.getClipCount();
                audioTrack.removeAllClips();
            }
        }
        return cleared;
    }

    public static int restoreEditorFeatures(NvsTimeline timeline, String serializedEditorState) {
        return restoreEditorFeaturesByClipIds(
                timeline,
                serializedEditorState,
                Collections.emptyList());
    }

    public static int restoreEditorFeaturesByClipIds(
            NvsTimeline timeline,
            String serializedEditorState,
            List<String> clipIds) {
        if (timeline == null || serializedEditorState == null || serializedEditorState.isEmpty()) {
            return 0;
        }
        try {
            JSONObject editor = new JSONObject(serializedEditorState);
            NvsVideoTrack videoTrack = timeline.getVideoTrackByIndex(0);
            int restored = 0;
            JSONObject theme = editor.optJSONObject("theme");
            if (theme != null) {
                String themePackageId = theme.optString("packageId", "");
                if (!themePackageId.isEmpty() && timeline.applyTheme(themePackageId)) {
                    float themeMusicVolume = (float) theme.optDouble("volume", 1.0);
                    timeline.setThemeMusicVolumeGain(themeMusicVolume, themeMusicVolume);
                    restored++;
                }
            }
            JSONArray filters = editor.optJSONArray("filters");
            if (videoTrack != null && filters != null) {
                for (int index = 0; index < filters.length(); index++) {
                    JSONObject item = filters.optJSONObject(index);
                    if (item == null) {
                        continue;
                    }
                    int clipIndex = -1;
                    String clipId = item.optString("clipId", "");
                    if (!clipId.isEmpty() && clipIds != null) {
                        for (int clipIdIndex = 0; clipIdIndex < clipIds.size(); clipIdIndex++) {
                            if (clipId.equals(clipIds.get(clipIdIndex))) {
                                clipIndex = clipIdIndex;
                                break;
                            }
                        }
                    }
                    if (clipIndex < 0) {
                        clipIndex = item.optInt("clipIndex", -1);
                    }
                    String packageId = item.optString("packageId", "");
                    NvsVideoClip clip = clipIndex >= 0 && clipIndex < videoTrack.getClipCount()
                            ? videoTrack.getClipByIndex(clipIndex)
                            : null;
                    NvsVideoFx videoFx = clip == null || packageId.isEmpty()
                            ? null
                            : clip.appendPackagedFx(packageId);
                    if (videoFx != null) {
                        videoFx.setFilterIntensity((float) item.optDouble("intensity", 1.0));
                        restored++;
                    }
                }
            }
            JSONArray captions = editor.optJSONArray("captions");
            if (captions != null) {
                for (int index = 0; index < captions.length(); index++) {
                    JSONObject item = captions.optJSONObject(index);
                    if (item == null) {
                        continue;
                    }
                    String text = item.optString("text", "");
                    long inPointUs = Math.max(0, item.optLong("inPointUs", 0));
                    long durationUs = item.optLong("durationUs", 0);
                    String stylePackageId = item.optString("stylePackageId", "");
                    if (text.isEmpty() || durationUs <= 0) {
                        continue;
                    }
                    NvsTimelineCaption caption = timeline.addCaption(
                            text,
                            inPointUs,
                            durationUs,
                            stylePackageId.isEmpty() ? null : stylePackageId);
                    if (caption == null) {
                        continue;
                    }
                    if (item.optBoolean("readableDefault", stylePackageId.isEmpty())) {
                        caption.setTextAlignment(NvsCaption.TEXT_ALIGNMENT_CENTER);
                        caption.setTextColor(new NvsColor(1.0f, 1.0f, 1.0f, 1.0f));
                        caption.setFontSize(48.0f);
                        caption.setDrawOutline(true);
                        caption.setOutlineColor(new NvsColor(0.0f, 0.0f, 0.0f, 1.0f));
                        caption.setOutlineWidth(4.0f);
                    }
                    String fontFilePath = item.optString("fontFilePath", "");
                    if (!fontFilePath.isEmpty()) {
                        caption.setFontByFilePath(fontFilePath);
                    }
                    String contextPackageId = item.optString("contextPackageId", "");
                    if (!contextPackageId.isEmpty()) {
                        caption.applyModularCaptionContext(contextPackageId);
                    }
                    String rendererPackageId = item.optString("rendererPackageId", "");
                    if (!rendererPackageId.isEmpty()) {
                        caption.applyModularCaptionRenderer(rendererPackageId);
                    }
                    String animationPackageId = item.optString("animationPackageId", "");
                    if (!animationPackageId.isEmpty()) {
                        caption.applyModularCaptionAnimation(animationPackageId);
                    }
                    caption.setFontSize((float) item.optDouble("fontSize", 48.0));
                    caption.setOpacity((float) item.optDouble("opacity", 1.0));
                    caption.setCaptionTranslation(new PointF(
                            (float) item.optDouble("translationX", 0.0),
                            (float) item.optDouble("translationY", 0.0)));
                    float captionScale = (float) item.optDouble("scale", 1.0);
                    caption.setScaleX(captionScale);
                    caption.setScaleY(captionScale);
                    caption.setRotationZ((float) item.optDouble("rotation", 0.0));
                    restored++;
                }
            }
            JSONArray compoundCaptions = editor.optJSONArray("compoundCaptions");
            if (compoundCaptions != null) {
                for (int index = 0; index < compoundCaptions.length(); index++) {
                    JSONObject item = compoundCaptions.optJSONObject(index);
                    if (item == null) {
                        continue;
                    }
                    long inPointUs = Math.max(0, item.optLong("inPointUs", 0));
                    long durationUs = item.optLong("durationUs", 0);
                    String packageId = item.optString("packageId", "");
                    if (durationUs <= 0 || packageId.isEmpty()) {
                        continue;
                    }
                    NvsTimelineCompoundCaption compoundCaption = timeline.addCompoundCaption(
                            inPointUs,
                            durationUs,
                            packageId);
                    if (compoundCaption == null) {
                        continue;
                    }
                    JSONArray texts = item.optJSONArray("texts");
                    int captionCount = compoundCaption.getCaptionCount();
                    for (int textIndex = 0;
                            texts != null && textIndex < texts.length() && textIndex < captionCount;
                            textIndex++) {
                        compoundCaption.setText(textIndex, texts.optString(textIndex, ""));
                    }
                    compoundCaption.setOpacity((float) item.optDouble("opacity", 1.0));
                    float compoundScale = (float) item.optDouble("scale", 1.0);
                    compoundCaption.setScaleX(compoundScale);
                    compoundCaption.setScaleY(compoundScale);
                    compoundCaption.setRotationZ((float) item.optDouble("rotation", 0.0));
                    restored++;
                }
            }
            JSONArray stickers = editor.optJSONArray("stickers");
            if (stickers != null) {
                for (int index = 0; index < stickers.length(); index++) {
                    JSONObject item = stickers.optJSONObject(index);
                    if (item == null) {
                        continue;
                    }
                    long inPointUs = Math.max(0, item.optLong("inPointUs", 0));
                    long durationUs = item.optLong("durationUs", 0);
                    String packageId = item.optString("packageId", "");
                    String customImagePath = item.optString("customImagePath", "");
                    if (durationUs <= 0 || packageId.isEmpty()) {
                        continue;
                    }
                    NvsTimelineAnimatedSticker sticker = customImagePath.isEmpty()
                            ? timeline.addAnimatedSticker(inPointUs, durationUs, packageId)
                            : timeline.addCustomAnimatedSticker(
                                    inPointUs,
                                    durationUs,
                                    packageId,
                                    customImagePath);
                    if (sticker != null) {
                        sticker.setTranslation(new PointF(
                                (float) item.optDouble("translationX", 0.0),
                                (float) item.optDouble("translationY", 0.0)));
                        sticker.setScale((float) item.optDouble("scale", 0.78));
                        sticker.setRotationZ((float) item.optDouble("rotation", 0.0));
                        sticker.setOpacity((float) item.optDouble("opacity", 1.0));
                        float stickerVolume = (float) item.optDouble("volume", 1.0);
                        sticker.setVolumeGain(stickerVolume, stickerVolume);
                        String inAnimationPackageId = item.optString(
                                "inAnimationPackageId",
                                "");
                        if (!inAnimationPackageId.isEmpty()) {
                            sticker.applyAnimatedStickerInAnimation(inAnimationPackageId);
                        }
                        sticker.setZValue(20.0f);
                        restored++;
                    }
                }
            }
            JSONArray transitions = editor.optJSONArray("transitions");
            if (videoTrack != null && transitions != null) {
                for (int index = 0; index < transitions.length(); index++) {
                    JSONObject item = transitions.optJSONObject(index);
                    if (item == null) {
                        continue;
                    }
                    int sourceClipIndex = -1;
                    String sourceClipId = item.optString("sourceClipId", "");
                    if (!sourceClipId.isEmpty() && clipIds != null) {
                        for (int clipIdIndex = 0; clipIdIndex < clipIds.size(); clipIdIndex++) {
                            if (sourceClipId.equals(clipIds.get(clipIdIndex))) {
                                sourceClipIndex = clipIdIndex;
                                break;
                            }
                        }
                    }
                    if (sourceClipIndex < 0) {
                        sourceClipIndex = item.optInt("sourceClipIndex", -1);
                    }
                    String targetClipId = item.optString("targetClipId", "");
                    boolean targetMatches = targetClipId.isEmpty()
                            || (clipIds != null
                            && sourceClipIndex + 1 >= 0
                            && sourceClipIndex + 1 < clipIds.size()
                            && targetClipId.equals(clipIds.get(sourceClipIndex + 1)));
                    String packageId = item.optString("packageId", "");
                    if (sourceClipIndex >= 0
                            && sourceClipIndex + 1 < videoTrack.getClipCount()
                            && targetMatches
                            && !packageId.isEmpty()) {
                        NvsVideoTransition transition = videoTrack.setPackagedTransition(
                                sourceClipIndex,
                                packageId);
                        if (transition == null) {
                            continue;
                        }
                        long transitionDurationUs = item.optLong("durationUs", 500_000L);
                        transition.setVideoTransitionDuration(
                                Math.max(100_000L, transitionDurationUs),
                                NvsVideoTransition.VIDEO_TRANSITION_DURATION_MATCH_MODE_STRETCH);
                        restored++;
                    }
                }
            }
            JSONArray audio = editor.optJSONArray("audio");
            if (audio != null) {
                for (int index = 0; index < audio.length(); index++) {
                    JSONObject item = audio.optJSONObject(index);
                    if (item == null) {
                        continue;
                    }
                    int trackIndex = item.optInt("trackIndex", -1);
                    String path = item.optString("path", "");
                    long inPointUs = Math.max(0, item.optLong("inPointUs", 0));
                    long trimInUs = Math.max(0, item.optLong("trimInUs", 0));
                    long trimOutUs = item.optLong("trimOutUs", 0);
                    if (trackIndex < 0 || path.isEmpty() || trimOutUs <= trimInUs
                            || (!path.startsWith("assets:/") && !new File(path).isFile())) {
                        continue;
                    }
                    while (timeline.audioTrackCount() <= trackIndex) {
                        if (timeline.appendAudioTrack() == null) {
                            break;
                        }
                    }
                    NvsAudioTrack audioTrack = timeline.getAudioTrackByIndex(trackIndex);
                    NvsAudioClip clip = audioTrack == null
                            ? null
                            : audioTrack.addClip(path, inPointUs, trimInUs, trimOutUs);
                    if (clip == null) {
                        continue;
                    }
                    float volume = (float) item.optDouble("volume", 1.0);
                    clip.setVolumeGain(volume, volume);
                    clip.setFadeInDuration(Math.max(0, item.optLong("fadeInUs", 0)));
                    clip.setFadeOutDuration(Math.max(0, item.optLong("fadeOutUs", 0)));
                    restored++;
                }
            }
            return restored;
        } catch (JSONException exception) {
            return 0;
        }
    }

    public static String selectedCaptionStylePackageId(String serializedEditorState) {
        return parseEditor(serializedEditorState).optString("selectedCaptionStylePackageId", "");
    }

    public static String setSelectedCaptionStylePackageId(
            String serializedEditorState,
            String packageId) {
        JSONObject editor = parseEditor(serializedEditorState);
        try {
            editor.put("selectedCaptionStylePackageId", packageId == null ? "" : packageId);
        } catch (JSONException ignored) {
        }
        return editor.toString();
    }

    public static String recordPackagedFilter(
            String serializedEditorState,
            int clipIndex,
            String packageId) {
        if (clipIndex < 0 || packageId == null || packageId.isEmpty()) {
            return normalized(serializedEditorState);
        }
        JSONObject item = new JSONObject();
        try {
            item.put("clipIndex", clipIndex);
            item.put("packageId", packageId);
        } catch (JSONException ignored) {
        }
        return append(serializedEditorState, "filters", item);
    }

    public static String recordPackagedFilterByClipId(
            String serializedEditorState,
            String clipId,
            String packageId) {
        return recordPackagedFilterByClipId(
                serializedEditorState,
                clipId,
                packageId,
                MeisheMaterialApplicationKind.FILTER,
                "Filter");
    }

    public static String recordPackagedFilterByClipId(
            String serializedEditorState,
            String clipId,
            String packageId,
            String applicationKind,
            String materialLabel) {
        if (clipId == null || clipId.isEmpty() || packageId == null || packageId.isEmpty()) {
            return normalized(serializedEditorState);
        }
        JSONObject item = new JSONObject();
        put(item, "id", stableId("filter"));
        put(item, "clipId", clipId);
        put(item, "packageId", packageId);
        put(item, "applicationKind", applicationKind);
        put(item, "materialLabel", materialLabel);
        put(item, "intensity", 1.0);
        put(item, "parameters", new JSONObject());
        return append(serializedEditorState, "filters", item);
    }

    public static String recordCaption(
            String serializedEditorState,
            String text,
            long inPointUs,
            long durationUs,
            String stylePackageId,
            boolean readableDefault) {
        return recordCaptionWithMaterial(
                serializedEditorState,
                text,
                inPointUs,
                durationUs,
                stylePackageId,
                readableDefault,
                "",
                "",
                "",
                "",
                stylePackageId == null || stylePackageId.isEmpty() ? "Captions" : "Caption style");
    }

    public static String recordCaptionWithMaterial(
            String serializedEditorState,
            String text,
            long inPointUs,
            long durationUs,
            String stylePackageId,
            boolean readableDefault,
            String fontFilePath,
            String contextPackageId,
            String rendererPackageId,
            String animationPackageId,
            String materialLabel) {
        if (text == null || text.isEmpty() || durationUs <= 0) {
            return normalized(serializedEditorState);
        }
        JSONObject item = new JSONObject();
        try {
            item.put("id", stableId("caption"));
            item.put("text", text);
            item.put("inPointUs", Math.max(0, inPointUs));
            item.put("durationUs", durationUs);
            item.put("stylePackageId", stylePackageId == null ? "" : stylePackageId);
            item.put("fontFilePath", fontFilePath == null ? "" : fontFilePath);
            item.put("contextPackageId", contextPackageId == null ? "" : contextPackageId);
            item.put("rendererPackageId", rendererPackageId == null ? "" : rendererPackageId);
            item.put("animationPackageId", animationPackageId == null ? "" : animationPackageId);
            item.put("materialLabel", materialLabel == null ? "Captions" : materialLabel);
            item.put("readableDefault", readableDefault);
            item.put("translationX", 0.0);
            item.put("translationY", 0.0);
            item.put("scale", 1.0);
            item.put("rotation", 0.0);
            item.put("opacity", 1.0);
            item.put("fontSize", 48.0);
        } catch (JSONException ignored) {
        }
        return append(serializedEditorState, "captions", item);
    }

    public static String recordSticker(
            String serializedEditorState,
            long inPointUs,
            long durationUs,
            String packageId) {
        return recordSticker(serializedEditorState, inPointUs, durationUs, packageId, null);
    }

    public static String recordSticker(
            String serializedEditorState,
            long inPointUs,
            long durationUs,
            String packageId,
            String customImagePath) {
        return recordSticker(
                serializedEditorState,
                inPointUs,
                durationUs,
                packageId,
                customImagePath,
                "Stickers");
    }

    public static String recordSticker(
            String serializedEditorState,
            long inPointUs,
            long durationUs,
            String packageId,
            String customImagePath,
            String materialLabel) {
        if (durationUs <= 0 || packageId == null || packageId.isEmpty()) {
            return normalized(serializedEditorState);
        }
        JSONObject item = new JSONObject();
        try {
            item.put("id", stableId("sticker"));
            item.put("inPointUs", Math.max(0, inPointUs));
            item.put("durationUs", durationUs);
            item.put("packageId", packageId);
            item.put("materialLabel", materialLabel == null ? "Stickers" : materialLabel);
            if (customImagePath != null && !customImagePath.isEmpty()) {
                item.put("customImagePath", customImagePath);
            }
            item.put("translationX", 0.0);
            item.put("translationY", 0.0);
            item.put("scale", 0.78);
            item.put("rotation", 0.0);
            item.put("opacity", 1.0);
            item.put("volume", 1.0);
        } catch (JSONException ignored) {
        }
        return append(serializedEditorState, "stickers", item);
    }

    public static String recordCompoundCaption(
            String serializedEditorState,
            String text,
            long inPointUs,
            long durationUs,
            String packageId,
            String materialLabel) {
        if (text == null || text.trim().isEmpty() || durationUs <= 0
                || packageId == null || packageId.isEmpty()) {
            return normalized(serializedEditorState);
        }
        JSONObject item = new JSONObject();
        JSONArray texts = new JSONArray();
        for (String slot : text.split("\\r?\\n", -1)) {
            texts.put(slot);
        }
        put(item, "id", stableId("compound-caption"));
        put(item, "texts", texts);
        put(item, "inPointUs", Math.max(0, inPointUs));
        put(item, "durationUs", durationUs);
        put(item, "packageId", packageId);
        put(item, "materialLabel", materialLabel == null ? "Compound caption" : materialLabel);
        put(item, "opacity", 1.0);
        put(item, "scale", 1.0);
        put(item, "rotation", 0.0);
        return append(serializedEditorState, "compoundCaptions", item);
    }

    public static String attachStickerInAnimation(
            String serializedEditorState,
            String animationPackageId,
            String materialLabel) {
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray stickers = editor.optJSONArray("stickers");
        JSONObject latest = stickers == null || stickers.length() == 0
                ? null
                : stickers.optJSONObject(stickers.length() - 1);
        if (latest != null && animationPackageId != null && !animationPackageId.isEmpty()) {
            put(latest, "inAnimationPackageId", animationPackageId);
            put(latest, "animationLabel", materialLabel == null ? "Sticker in animation" : materialLabel);
        }
        return editor.toString();
    }

    public static String recordTheme(
            String serializedEditorState,
            String packageId,
            String materialLabel) {
        JSONObject editor = parseEditor(serializedEditorState);
        if (packageId == null || packageId.isEmpty()) {
            put(editor, "theme", JSONObject.NULL);
            return editor.toString();
        }
        JSONObject theme = new JSONObject();
        put(theme, "id", "timeline-theme");
        put(theme, "packageId", packageId);
        put(theme, "materialLabel", materialLabel == null ? "Themes" : materialLabel);
        put(theme, "volume", 1.0);
        put(editor, "theme", theme);
        return editor.toString();
    }

    public static String recordTransition(
            String serializedEditorState,
            int sourceClipIndex,
            String packageId) {
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray current = editor.optJSONArray("transitions");
        JSONArray replacement = new JSONArray();
        if (current != null) {
            for (int index = 0; index < current.length(); index++) {
                JSONObject item = current.optJSONObject(index);
                if (item != null && item.optInt("sourceClipIndex", -1) != sourceClipIndex) {
                    replacement.put(item);
                }
            }
        }
        if (sourceClipIndex >= 0 && packageId != null && !packageId.isEmpty()) {
            JSONObject item = new JSONObject();
            try {
                item.put("sourceClipIndex", sourceClipIndex);
                item.put("packageId", packageId);
            } catch (JSONException ignored) {
            }
            replacement.put(item);
        }
        put(editor, "transitions", replacement);
        return editor.toString();
    }

    public static String recordTransitionByClipIds(
            String serializedEditorState,
            String sourceClipId,
            String targetClipId,
            String packageId) {
        return recordTransitionByClipIds(
                serializedEditorState,
                sourceClipId,
                targetClipId,
                packageId,
                "Transitions");
    }

    public static String recordTransitionByClipIds(
            String serializedEditorState,
            String sourceClipId,
            String targetClipId,
            String packageId,
            String materialLabel) {
        if (sourceClipId == null) {
            sourceClipId = "";
        }
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray current = editor.optJSONArray("transitions");
        JSONArray replacement = new JSONArray();
        for (int index = 0; current != null && index < current.length(); index++) {
            JSONObject item = current.optJSONObject(index);
            if (item != null
                    && !sourceClipId.equals(item.optString("sourceClipId", ""))) {
                replacement.put(item);
            }
        }
        if (sourceClipId != null && !sourceClipId.isEmpty()
                && targetClipId != null && !targetClipId.isEmpty()
                && packageId != null && !packageId.isEmpty()) {
            JSONObject item = new JSONObject();
            put(item, "id", stableId("transition"));
            put(item, "sourceClipId", sourceClipId);
            put(item, "targetClipId", targetClipId);
            put(item, "packageId", packageId);
            put(item, "materialLabel", materialLabel == null ? "Transitions" : materialLabel);
            put(item, "durationUs", 500_000L);
            replacement.put(item);
        }
        put(editor, "transitions", replacement);
        return editor.toString();
    }

    public static String replaceAudioTrackWithClip(
            String serializedEditorState,
            int trackIndex,
            String path,
            long inPointUs,
            long trimInUs,
            long trimOutUs) {
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray current = editor.optJSONArray("audio");
        JSONArray replacement = new JSONArray();
        if (current != null) {
            for (int index = 0; index < current.length(); index++) {
                JSONObject item = current.optJSONObject(index);
                if (item != null && item.optInt("trackIndex", -1) != trackIndex) {
                    replacement.put(item);
                }
            }
        }
        put(editor, "audio", replacement);
        return appendAudio(editor, trackIndex, path, inPointUs, trimInUs, trimOutUs);
    }

    public static String appendAudioClip(
            String serializedEditorState,
            int trackIndex,
            String path,
            long inPointUs,
            long trimInUs,
            long trimOutUs) {
        return appendAudio(
                parseEditor(serializedEditorState),
                trackIndex,
                path,
                inPointUs,
                trimInUs,
                trimOutUs);
    }

    public static String removeLastAudioClip(String serializedEditorState, int trackIndex) {
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray audio = editor.optJSONArray("audio");
        int removeIndex = -1;
        for (int index = audio == null ? -1 : audio.length() - 1; index >= 0; index--) {
            JSONObject item = audio.optJSONObject(index);
            if (item != null && item.optInt("trackIndex", -1) == trackIndex) {
                removeIndex = index;
                break;
            }
        }
        if (removeIndex < 0) {
            return editor.toString();
        }
        JSONArray replacement = new JSONArray();
        for (int index = 0; index < audio.length(); index++) {
            if (index != removeIndex) {
                replacement.put(audio.opt(index));
            }
        }
        put(editor, "audio", replacement);
        return editor.toString();
    }

    public static List<MeisheAppliedMaterial> listAppliedMaterials(
            String serializedEditorState) {
        JSONObject editor = parseEditor(serializedEditorState);
        List<MeisheAppliedMaterial> materials = new ArrayList<>();
        appendAppliedMaterials(materials, editor.optJSONArray("filters"),
                MeisheAppliedMaterial.TYPE_CLIP_EFFECT);
        appendAppliedMaterials(materials, editor.optJSONArray("captions"),
                MeisheAppliedMaterial.TYPE_CAPTION);
        appendAppliedMaterials(materials, editor.optJSONArray("compoundCaptions"),
                MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION);
        appendAppliedMaterials(materials, editor.optJSONArray("stickers"),
                MeisheAppliedMaterial.TYPE_STICKER);
        appendAppliedMaterials(materials, editor.optJSONArray("transitions"),
                MeisheAppliedMaterial.TYPE_TRANSITION);
        appendAppliedMaterials(materials, editor.optJSONArray("audio"),
                MeisheAppliedMaterial.TYPE_AUDIO);
        JSONObject theme = editor.optJSONObject("theme");
        if (theme != null) {
            materials.add(appliedMaterial(theme, MeisheAppliedMaterial.TYPE_THEME));
        }
        return materials;
    }

    public static String updateAppliedMaterial(
            String serializedEditorState,
            MeisheAppliedMaterial material,
            MeisheAppliedMaterial.Edits edits) {
        if (material == null || edits == null || material.id.isEmpty()) {
            return normalized(serializedEditorState);
        }
        JSONObject editor = parseEditor(serializedEditorState);
        JSONObject descriptor = findMaterialDescriptor(editor, material);
        if (descriptor == null) {
            return editor.toString();
        }
        if (MeisheAppliedMaterial.TYPE_CAPTION.equals(material.type)) {
            put(descriptor, "text", nonEmpty(edits.text, material.text));
            put(descriptor, "durationUs", Math.max(100_000L, edits.durationUs));
            put(descriptor, "fontSize", clamp(edits.fontSize, 8.0f, 200.0f));
            put(descriptor, "opacity", clamp(edits.opacity, 0.0f, 1.0f));
            put(descriptor, "scale", clamp(edits.scale, 0.1f, 5.0f));
            put(descriptor, "rotation", edits.rotation);
        } else if (MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(material.type)) {
            JSONArray texts = new JSONArray();
            for (String slot : nonEmpty(edits.text, material.text).split("\\r?\\n", -1)) {
                texts.put(slot);
            }
            put(descriptor, "texts", texts);
            put(descriptor, "durationUs", Math.max(100_000L, edits.durationUs));
            put(descriptor, "opacity", clamp(edits.opacity, 0.0f, 1.0f));
            put(descriptor, "scale", clamp(edits.scale, 0.1f, 5.0f));
            put(descriptor, "rotation", edits.rotation);
        } else if (MeisheAppliedMaterial.TYPE_CLIP_EFFECT.equals(material.type)) {
            put(descriptor, "intensity", clamp(edits.intensity, 0.0f, 1.0f));
        } else if (MeisheAppliedMaterial.TYPE_STICKER.equals(material.type)) {
            put(descriptor, "durationUs", Math.max(100_000L, edits.durationUs));
            put(descriptor, "opacity", clamp(edits.opacity, 0.0f, 1.0f));
            put(descriptor, "scale", clamp(edits.scale, 0.1f, 5.0f));
            put(descriptor, "rotation", edits.rotation);
            put(descriptor, "volume", clamp(edits.volume, 0.0f, 2.0f));
        } else if (MeisheAppliedMaterial.TYPE_TRANSITION.equals(material.type)) {
            put(descriptor, "durationUs", Math.max(100_000L, edits.durationUs));
        } else if (MeisheAppliedMaterial.TYPE_AUDIO.equals(material.type)) {
            put(descriptor, "volume", clamp(edits.volume, 0.0f, 2.0f));
            put(descriptor, "fadeInUs", Math.max(0, edits.fadeInUs));
            put(descriptor, "fadeOutUs", Math.max(0, edits.fadeOutUs));
        } else if (MeisheAppliedMaterial.TYPE_THEME.equals(material.type)) {
            put(descriptor, "volume", clamp(edits.volume, 0.0f, 2.0f));
        }
        return editor.toString();
    }

    public static String deleteAppliedMaterial(
            String serializedEditorState,
            MeisheAppliedMaterial material) {
        if (material == null || material.id.isEmpty()) {
            return normalized(serializedEditorState);
        }
        JSONObject editor = parseEditor(serializedEditorState);
        if (MeisheAppliedMaterial.TYPE_THEME.equals(material.type)) {
            put(editor, "theme", JSONObject.NULL);
            return editor.toString();
        }
        String arrayKey = arrayKeyForType(material.type);
        JSONArray current = editor.optJSONArray(arrayKey);
        JSONArray replacement = new JSONArray();
        for (int index = 0; current != null && index < current.length(); index++) {
            JSONObject item = current.optJSONObject(index);
            if (item != null && !material.id.equals(item.optString("id", ""))) {
                replacement.put(item);
            }
        }
        put(editor, arrayKey, replacement);
        return editor.toString();
    }

    public static String onClipRemoved(String serializedEditorState, int removedIndex) {
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray filters = editor.optJSONArray("filters");
        JSONArray replacement = new JSONArray();
        if (filters != null) {
            for (int index = 0; index < filters.length(); index++) {
                JSONObject item = filters.optJSONObject(index);
                if (item == null) {
                    continue;
                }
                int clipIndex = item.optInt("clipIndex", -1);
                if (clipIndex == removedIndex) {
                    continue;
                }
                setInt(item, "clipIndex", clipIndex > removedIndex ? clipIndex - 1 : clipIndex);
                replacement.put(item);
            }
        }
        put(editor, "filters", replacement);
        put(editor, "transitions", new JSONArray());
        return editor.toString();
    }

    public static String onClipMoved(
            String serializedEditorState,
            int sourceIndex,
            int targetIndex) {
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray filters = editor.optJSONArray("filters");
        if (filters != null) {
            for (int index = 0; index < filters.length(); index++) {
                JSONObject item = filters.optJSONObject(index);
                if (item == null) {
                    continue;
                }
                int clipIndex = item.optInt("clipIndex", -1);
                int mapped = clipIndex;
                if (clipIndex == sourceIndex) {
                    mapped = targetIndex;
                } else if (sourceIndex < targetIndex && clipIndex > sourceIndex && clipIndex <= targetIndex) {
                    mapped = clipIndex - 1;
                } else if (targetIndex < sourceIndex && clipIndex >= targetIndex && clipIndex < sourceIndex) {
                    mapped = clipIndex + 1;
                }
                setInt(item, "clipIndex", mapped);
            }
        }
        put(editor, "transitions", new JSONArray());
        return editor.toString();
    }

    public static String onClipSplit(String serializedEditorState, int sourceIndex) {
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray filters = editor.optJSONArray("filters");
        JSONArray replacement = new JSONArray();
        if (filters != null) {
            for (int index = 0; index < filters.length(); index++) {
                JSONObject item = filters.optJSONObject(index);
                if (item == null) {
                    continue;
                }
                int clipIndex = item.optInt("clipIndex", -1);
                if (clipIndex > sourceIndex) {
                    setInt(item, "clipIndex", clipIndex + 1);
                    replacement.put(item);
                } else {
                    replacement.put(item);
                    if (clipIndex == sourceIndex) {
                        JSONObject duplicate = copy(item);
                        setInt(duplicate, "clipIndex", sourceIndex + 1);
                        replacement.put(duplicate);
                    }
                }
            }
        }
        put(editor, "filters", replacement);
        put(editor, "transitions", new JSONArray());
        return editor.toString();
    }

    public static String onClipRemovedById(
            String serializedEditorState,
            String removedClipId) {
        if (removedClipId == null || removedClipId.isEmpty()) {
            return normalized(serializedEditorState);
        }
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray filters = editor.optJSONArray("filters");
        JSONArray replacement = new JSONArray();
        for (int index = 0; filters != null && index < filters.length(); index++) {
            JSONObject item = filters.optJSONObject(index);
            if (item != null
                    && !removedClipId.equals(item.optString("clipId", ""))) {
                replacement.put(item);
            }
        }
        put(editor, "filters", replacement);
        put(editor, "transitions", new JSONArray());
        return editor.toString();
    }

    public static String onClipSplitById(
            String serializedEditorState,
            String sourceClipId,
            String newClipId) {
        if (sourceClipId == null || sourceClipId.isEmpty()
                || newClipId == null || newClipId.isEmpty()) {
            return normalized(serializedEditorState);
        }
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray filters = editor.optJSONArray("filters");
        JSONArray replacement = new JSONArray();
        for (int index = 0; filters != null && index < filters.length(); index++) {
            JSONObject item = filters.optJSONObject(index);
            if (item == null) {
                continue;
            }
            replacement.put(item);
            if (sourceClipId.equals(item.optString("clipId", ""))) {
                JSONObject duplicate = copy(item);
                put(duplicate, "id", stableId("filter"));
                put(duplicate, "clipId", newClipId);
                replacement.put(duplicate);
            }
        }
        put(editor, "filters", replacement);
        put(editor, "transitions", new JSONArray());
        return editor.toString();
    }

    public static String onClipMovedById(String serializedEditorState) {
        JSONObject editor = parseEditor(serializedEditorState);
        put(editor, "transitions", new JSONArray());
        return editor.toString();
    }

    private static void appendAppliedMaterials(
            List<MeisheAppliedMaterial> output,
            JSONArray descriptors,
            String type) {
        for (int index = 0; descriptors != null && index < descriptors.length(); index++) {
            JSONObject descriptor = descriptors.optJSONObject(index);
            if (descriptor != null) {
                output.add(appliedMaterial(descriptor, type));
            }
        }
    }

    private static MeisheAppliedMaterial appliedMaterial(JSONObject descriptor, String type) {
        String title = descriptor.optString("materialLabel", defaultMaterialTitle(type));
        String text = descriptor.optString("text", "");
        if (MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(type)) {
            JSONArray texts = descriptor.optJSONArray("texts");
            StringBuilder joined = new StringBuilder();
            for (int index = 0; texts != null && index < texts.length(); index++) {
                if (index > 0) {
                    joined.append('\n');
                }
                joined.append(texts.optString(index, ""));
            }
            text = joined.toString();
        }
        long durationUs = descriptor.optLong("durationUs",
                descriptor.optLong("trimOutUs", 0) - descriptor.optLong("trimInUs", 0));
        float intensity = (float) descriptor.optDouble("intensity", 1.0);
        float fontSize = (float) descriptor.optDouble("fontSize", 48.0);
        float opacity = (float) descriptor.optDouble("opacity", 1.0);
        float scale = (float) descriptor.optDouble("scale", 1.0);
        float rotation = (float) descriptor.optDouble("rotation", 0.0);
        float volume = (float) descriptor.optDouble("volume", 1.0);
        String summary;
        if (MeisheAppliedMaterial.TYPE_CLIP_EFFECT.equals(type)) {
            summary = "Clip effect · intensity " + Math.round(intensity * 100) + "%";
        } else if (MeisheAppliedMaterial.TYPE_CAPTION.equals(type)
                || MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(type)) {
            summary = abbreviate(text, 12) + " · " + formatSeconds(durationUs);
        } else if (MeisheAppliedMaterial.TYPE_STICKER.equals(type)) {
            String animationLabel = descriptor.optString("animationLabel", "");
            summary = formatSeconds(durationUs)
                    + (animationLabel.isEmpty() ? "" : " · " + animationLabel);
        } else if (MeisheAppliedMaterial.TYPE_TRANSITION.equals(type)) {
            summary = "Clip boundary · " + formatSeconds(durationUs);
        } else if (MeisheAppliedMaterial.TYPE_AUDIO.equals(type)) {
            String path = descriptor.optString("path", "Audio");
            summary = new File(path).getName() + " · volume " + Math.round(volume * 100) + "%";
            if (title.equals(defaultMaterialTitle(type))) {
                title = descriptor.optInt("trackIndex", 0) == 1 ? "Voiceover" : "Music";
            }
        } else if (MeisheAppliedMaterial.TYPE_THEME.equals(type)) {
            summary = "Whole timeline · music " + Math.round(volume * 100) + "%";
        } else {
            summary = formatSeconds(durationUs);
        }
        return new MeisheAppliedMaterial(
                descriptor.optString("id", ""),
                type,
                title,
                summary,
                text,
                durationUs,
                intensity,
                fontSize,
                opacity,
                scale,
                rotation,
                volume,
                descriptor.optLong("fadeInUs", 0),
                descriptor.optLong("fadeOutUs", 0));
    }

    private static JSONObject findMaterialDescriptor(
            JSONObject editor,
            MeisheAppliedMaterial material) {
        if (MeisheAppliedMaterial.TYPE_THEME.equals(material.type)) {
            return editor.optJSONObject("theme");
        }
        JSONArray values = editor.optJSONArray(arrayKeyForType(material.type));
        for (int index = 0; values != null && index < values.length(); index++) {
            JSONObject descriptor = values.optJSONObject(index);
            if (descriptor != null && material.id.equals(descriptor.optString("id", ""))) {
                return descriptor;
            }
        }
        return null;
    }

    private static String arrayKeyForType(String type) {
        if (MeisheAppliedMaterial.TYPE_CLIP_EFFECT.equals(type)) {
            return "filters";
        }
        if (MeisheAppliedMaterial.TYPE_CAPTION.equals(type)) {
            return "captions";
        }
        if (MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(type)) {
            return "compoundCaptions";
        }
        if (MeisheAppliedMaterial.TYPE_STICKER.equals(type)) {
            return "stickers";
        }
        if (MeisheAppliedMaterial.TYPE_TRANSITION.equals(type)) {
            return "transitions";
        }
        if (MeisheAppliedMaterial.TYPE_AUDIO.equals(type)) {
            return "audio";
        }
        return "";
    }

    private static String defaultMaterialTitle(String type) {
        if (MeisheAppliedMaterial.TYPE_CLIP_EFFECT.equals(type)) {
            return "Clip effect";
        }
        if (MeisheAppliedMaterial.TYPE_CAPTION.equals(type)) {
            return "Captions";
        }
        if (MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(type)) {
            return "Compound caption";
        }
        if (MeisheAppliedMaterial.TYPE_STICKER.equals(type)) {
            return "Stickers";
        }
        if (MeisheAppliedMaterial.TYPE_TRANSITION.equals(type)) {
            return "Transitions";
        }
        if (MeisheAppliedMaterial.TYPE_AUDIO.equals(type)) {
            return "Audio";
        }
        if (MeisheAppliedMaterial.TYPE_THEME.equals(type)) {
            return "Themes";
        }
        return "Materials";
    }

    private static String abbreviate(String value, int maxLength) {
        String safe = value == null ? "" : value.replace('\n', ' ');
        return safe.length() <= maxLength ? safe : safe.substring(0, maxLength) + "…";
    }

    private static String formatSeconds(long durationUs) {
        return String.format(java.util.Locale.US, "%.1f", Math.max(0, durationUs) / 1_000_000.0)
                + " seconds";
    }

    private static String nonEmpty(String candidate, String fallback) {
        return candidate == null || candidate.trim().isEmpty() ? fallback : candidate.trim();
    }

    private static float clamp(float value, float minimum, float maximum) {
        return Math.max(minimum, Math.min(maximum, value));
    }

    private static String appendAudio(
            JSONObject editor,
            int trackIndex,
            String path,
            long inPointUs,
            long trimInUs,
            long trimOutUs) {
        if (trackIndex < 0 || path == null || path.isEmpty() || trimOutUs <= trimInUs) {
            return editor.toString();
        }
        JSONObject item = new JSONObject();
        try {
            item.put("id", stableId("audio"));
            item.put("trackIndex", trackIndex);
            item.put("path", path);
            item.put("inPointUs", Math.max(0, inPointUs));
            item.put("trimInUs", Math.max(0, trimInUs));
            item.put("trimOutUs", trimOutUs);
            item.put("volume", 1.0);
            item.put("fadeInUs", 0);
            item.put("fadeOutUs", 0);
        } catch (JSONException ignored) {
        }
        JSONArray audio = editor.optJSONArray("audio");
        if (audio == null) {
            audio = new JSONArray();
            put(editor, "audio", audio);
        }
        audio.put(item);
        return editor.toString();
    }

    private static String append(String serializedEditorState, String key, JSONObject item) {
        JSONObject editor = parseEditor(serializedEditorState);
        JSONArray array = editor.optJSONArray(key);
        if (array == null) {
            array = new JSONArray();
            put(editor, key, array);
        }
        array.put(item);
        return editor.toString();
    }

    private static String normalized(String serializedEditorState) {
        return parseEditor(serializedEditorState).toString();
    }

    private static JSONObject parseEditor(String serializedEditorState) {
        if (serializedEditorState == null || serializedEditorState.isEmpty()) {
            return editorObject();
        }
        try {
            JSONObject editor = new JSONObject(serializedEditorState);
            ensureArrays(editor);
            return editor;
        } catch (JSONException exception) {
            return editorObject();
        }
    }

    private static JSONObject editorObject() {
        JSONObject editor = new JSONObject();
        try {
            editor.put("version", EDITOR_STATE_VERSION);
            editor.put("selectedCaptionStylePackageId", "");
            ensureArrays(editor);
        } catch (JSONException ignored) {
        }
        return editor;
    }

    private static void ensureArrays(JSONObject editor) {
        for (String key : new String[]{
                "filters",
                "captions",
                "compoundCaptions",
                "stickers",
                "transitions",
                "audio",
                "backgrounds",
                "watermarks"}) {
            if (editor.optJSONArray(key) == null) {
                put(editor, key, new JSONArray());
            }
        }
        if (editor.optJSONObject("moduleData") == null) {
            put(editor, "moduleData", new JSONObject());
        }
        ensureDescriptorIds(editor);
    }

    private static void ensureDescriptorIds(JSONObject editor) {
        for (String key : new String[]{
                "filters",
                "captions",
                "compoundCaptions",
                "stickers",
                "transitions",
                "audio",
                "backgrounds",
                "watermarks"}) {
            JSONArray values = editor.optJSONArray(key);
            for (int index = 0; values != null && index < values.length(); index++) {
                JSONObject item = values.optJSONObject(index);
                if (item != null && item.optString("id", "").isEmpty()) {
                    put(item, "id", stableId(key));
                }
            }
        }
    }

    private static int indexOfClipId(List<String> clipIds, String clipId) {
        if (clipIds == null || clipId == null || clipId.isEmpty()) {
            return -1;
        }
        return clipIds.indexOf(clipId);
    }

    private static String idAt(List<String> clipIds, int index) {
        return clipIds == null || index < 0 || index >= clipIds.size()
                ? ""
                : clipIds.get(index);
    }

    private static String stableId(String prefix) {
        return prefix + "-" + UUID.randomUUID();
    }

    private static JSONObject copy(JSONObject value) {
        try {
            return new JSONObject(value.toString());
        } catch (JSONException exception) {
            return new JSONObject();
        }
    }

    private static void setInt(JSONObject target, String key, int value) {
        try {
            target.put(key, value);
        } catch (JSONException ignored) {
        }
    }

    private static void put(JSONObject target, String key, Object value) {
        try {
            target.put(key, value);
        } catch (JSONException ignored) {
        }
    }
}
