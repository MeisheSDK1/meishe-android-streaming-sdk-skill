package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public final class MeisheEditorProject {
    public static final int VERSION = 3;
    private static final int DEFAULT_FPS_NUMERATOR = 25;
    private static final int DEFAULT_FPS_DENOMINATOR = 1;
    private static final int DEFAULT_AUDIO_SAMPLE_RATE = 44100;
    private static final int DEFAULT_AUDIO_CHANNEL_COUNT = 2;

    private final JSONObject root;

    private MeisheEditorProject(JSONObject root) {
        this.root = normalize(root);
    }

    public static MeisheEditorProject create(String projectId, int width, int height) {
        JSONObject root = new JSONObject();
        put(root, "version", VERSION);
        put(root, "projectId", projectId == null ? "" : projectId);
        put(root, "width", positive(width, 720));
        put(root, "height", positive(height, 1280));
        put(root, "clips", new JSONArray());
        put(root, "editor", parseObject(MeisheEditorProjectStore.emptyEditorState()));
        put(root, "extensions", new JSONObject());
        return new MeisheEditorProject(root);
    }

    public static MeisheEditorProject fromSerialized(
            String projectId,
            String serialized,
            int fallbackWidth,
            int fallbackHeight) {
        JSONObject parsed;
        try {
            parsed = serialized == null || serialized.isEmpty()
                    ? new JSONObject()
                    : new JSONObject(serialized);
        } catch (JSONException exception) {
            parsed = new JSONObject();
        }
        int width = parsed.optInt("width", fallbackWidth);
        int height = parsed.optInt("height", fallbackHeight);
        JSONObject canvas = parsed.optJSONObject("canvas");
        if (canvas != null) {
            width = canvas.optInt("width", width);
            height = canvas.optInt("height", height);
        }
        put(parsed, "projectId", parsed.optString("projectId", projectId));
        put(parsed, "width", positive(width, 720));
        put(parsed, "height", positive(height, 1280));
        return new MeisheEditorProject(parsed);
    }

    public String projectId() {
        return root.optString("projectId", "");
    }

    public int width() {
        return root.optJSONObject("canvas").optInt("width", 720);
    }

    public int height() {
        return root.optJSONObject("canvas").optInt("height", 1280);
    }

    public String serialize() {
        return root.toString();
    }

    public String editorState() {
        JSONObject editor = root.optJSONObject("editor");
        return editor == null
                ? MeisheEditorProjectStore.emptyEditorState()
                : editor.toString();
    }

    public void setEditorState(String serializedEditorState) {
        try {
            put(root, "editor", new JSONObject(serializedEditorState));
        } catch (JSONException exception) {
            put(root, "editor", parseObject(MeisheEditorProjectStore.emptyEditorState()));
        }
        migrateEditorRelations(root.optJSONObject("editor"), clipIds());
    }

    public String clipIdAt(int index) {
        JSONObject clip = clipAt(index);
        return clip == null ? "" : clip.optString("id", "");
    }

    public List<String> clipIds() {
        List<String> ids = new ArrayList<>();
        JSONArray clips = clips();
        for (int index = 0; index < clips.length(); index++) {
            JSONObject clip = clips.optJSONObject(index);
            ids.add(clip == null ? "" : clip.optString("id", ""));
        }
        return ids;
    }

    public String splitClip(int sourceIndex) {
        JSONArray current = clips();
        JSONObject source = current.optJSONObject(sourceIndex);
        if (source == null) {
            return "";
        }
        String newId = newStableId("clip");
        JSONArray replacement = new JSONArray();
        for (int index = 0; index < current.length(); index++) {
            JSONObject item = copy(current.optJSONObject(index));
            replacement.put(item);
            if (index == sourceIndex) {
                JSONObject right = copy(item);
                put(right, "id", newId);
                replacement.put(right);
            }
        }
        put(root, "clips", replacement);
        return newId;
    }

    public String removeClip(int removedIndex) {
        JSONArray current = clips();
        JSONObject removed = current.optJSONObject(removedIndex);
        if (removed == null) {
            return "";
        }
        JSONArray replacement = new JSONArray();
        for (int index = 0; index < current.length(); index++) {
            if (index != removedIndex) {
                replacement.put(current.opt(index));
            }
        }
        put(root, "clips", replacement);
        return removed.optString("id", "");
    }

    public boolean moveClip(int sourceIndex, int targetIndex) {
        JSONArray current = clips();
        if (sourceIndex < 0 || targetIndex < 0
                || sourceIndex >= current.length() || targetIndex >= current.length()
                || sourceIndex == targetIndex) {
            return false;
        }
        List<Object> values = new ArrayList<>();
        for (int index = 0; index < current.length(); index++) {
            values.add(current.opt(index));
        }
        Object moved = values.remove(sourceIndex);
        values.add(targetIndex, moved);
        JSONArray replacement = new JSONArray();
        for (Object value : values) {
            replacement.put(value);
        }
        put(root, "clips", replacement);
        return true;
    }

    public void synchronizeTimeline(NvsTimeline timeline) {
        NvsVideoTrack track = timeline == null ? null : timeline.getVideoTrackByIndex(0);
        if (track == null) {
            return;
        }
        JSONArray previous = clips();
        JSONArray synchronizedClips = new JSONArray();
        for (int index = 0; index < track.getClipCount(); index++) {
            NvsVideoClip clip = track.getClipByIndex(index);
            if (clip == null || clip.getFilePath() == null || clip.getFilePath().isEmpty()) {
                continue;
            }
            JSONObject item = copy(previous.optJSONObject(index));
            if (item.optString("id", "").isEmpty()) {
                put(item, "id", newStableId("clip"));
            }
            put(item, "path", clip.getFilePath());
            put(item, "trimInUs", clip.getTrimIn());
            put(item, "trimOutUs", clip.getTrimOut());
            put(item, "speed", clip.getSpeed());
            put(item, "keepAudioPitch", clip.isKeepAudioPitch());
            put(item, "videoType", clip.getVideoType());
            put(item, "imageMotion", clip.getImageMotionAnimationEnabled());
            synchronizedClips.put(item);
        }
        put(root, "clips", synchronizedClips);
        migrateEditorRelations(root.optJSONObject("editor"), clipIds());
    }

    public int restoreTimeline(NvsTimeline timeline, boolean clearExisting) {
        NvsVideoTrack track = timeline == null ? null : timeline.getVideoTrackByIndex(0);
        if (track == null && timeline != null) {
            track = timeline.appendVideoTrack();
        }
        if (track == null) {
            return 0;
        }
        if (clearExisting) {
            track.removeAllClips();
        } else if (track.getClipCount() > 0) {
            return track.getClipCount();
        }
        int restored = 0;
        JSONArray clips = clips();
        for (int index = 0; index < clips.length(); index++) {
            JSONObject item = clips.optJSONObject(index);
            if (item == null) {
                continue;
            }
            String path = item.optString("path", "");
            if (path.isEmpty() || (!path.startsWith("assets:/") && !new File(path).isFile())) {
                continue;
            }
            long trimInUs = Math.max(0, item.optLong("trimInUs", 0));
            long trimOutUs = item.optLong("trimOutUs", 0);
            NvsVideoClip clip = trimOutUs > trimInUs
                    ? track.appendClip(path, trimInUs, trimOutUs)
                    : track.appendClip(path);
            if (clip == null) {
                continue;
            }
            double speed = item.optDouble("speed", 1.0);
            if (!Double.isNaN(speed) && !Double.isInfinite(speed)
                    && speed > 0 && Math.abs(speed - 1.0) > 0.0001) {
                clip.changeSpeed(speed, item.optBoolean("keepAudioPitch", true));
            }
            if (clip.getVideoType() == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {
                clip.setImageMotionAnimationEnabled(item.optBoolean("imageMotion", false));
            }
            restored++;
        }
        return restored;
    }

    public <T> boolean putExtension(MeisheProjectExtensionCodec<T> codec, T value) {
        if (codec == null || codec.namespace() == null || codec.namespace().trim().isEmpty()) {
            return false;
        }
        try {
            JSONObject encoded = codec.encode(value);
            extensions().put(codec.namespace(), encoded == null ? new JSONObject() : encoded);
            return true;
        } catch (JSONException exception) {
            return false;
        }
    }

    public <T> T readExtension(MeisheProjectExtensionCodec<T> codec) {
        if (codec == null || codec.namespace() == null || codec.namespace().trim().isEmpty()) {
            return null;
        }
        try {
            JSONObject encoded = extensions().optJSONObject(codec.namespace());
            return encoded == null ? null : codec.decode(encoded);
        } catch (JSONException exception) {
            return null;
        }
    }

    private JSONObject clipAt(int index) {
        return index < 0 ? null : clips().optJSONObject(index);
    }

    private JSONArray clips() {
        JSONArray clips = root.optJSONArray("clips");
        if (clips == null) {
            clips = new JSONArray();
            put(root, "clips", clips);
        }
        return clips;
    }

    private JSONObject extensions() {
        JSONObject extensions = root.optJSONObject("extensions");
        if (extensions == null) {
            extensions = new JSONObject();
            put(root, "extensions", extensions);
        }
        return extensions;
    }

    private static JSONObject normalize(JSONObject value) {
        JSONObject root = value == null ? new JSONObject() : value;
        int width = positive(root.optInt("width", 720), 720);
        int height = positive(root.optInt("height", 1280), 1280);
        JSONObject canvas = root.optJSONObject("canvas");
        if (canvas == null) {
            canvas = new JSONObject();
        }
        put(canvas, "width", positive(canvas.optInt("width", width), width));
        put(canvas, "height", positive(canvas.optInt("height", height), height));
        JSONObject fps = canvas.optJSONObject("fps");
        if (fps == null) {
            fps = new JSONObject();
        }
        put(fps, "numerator", positive(fps.optInt("numerator", DEFAULT_FPS_NUMERATOR), DEFAULT_FPS_NUMERATOR));
        put(fps, "denominator", positive(fps.optInt("denominator", DEFAULT_FPS_DENOMINATOR), DEFAULT_FPS_DENOMINATOR));
        put(canvas, "fps", fps);
        put(root, "canvas", canvas);
        put(root, "width", canvas.optInt("width", width));
        put(root, "height", canvas.optInt("height", height));

        JSONObject audio = root.optJSONObject("audioResolution");
        if (audio == null) {
            audio = new JSONObject();
        }
        put(audio, "sampleRate", positive(audio.optInt("sampleRate", DEFAULT_AUDIO_SAMPLE_RATE), DEFAULT_AUDIO_SAMPLE_RATE));
        put(audio, "channelCount", positive(audio.optInt("channelCount", DEFAULT_AUDIO_CHANNEL_COUNT), DEFAULT_AUDIO_CHANNEL_COUNT));
        put(root, "audioResolution", audio);

        JSONArray clips = root.optJSONArray("clips");
        if (clips == null) {
            clips = new JSONArray();
            put(root, "clips", clips);
        }
        for (int index = 0; index < clips.length(); index++) {
            JSONObject clip = clips.optJSONObject(index);
            if (clip != null && clip.optString("id", "").isEmpty()) {
                put(clip, "id", newStableId("clip"));
            }
        }
        JSONObject editor = root.optJSONObject("editor");
        if (editor == null) {
            editor = parseObject(MeisheEditorProjectStore.emptyEditorState());
            put(root, "editor", editor);
        }
        migrateEditorRelations(editor, clipIds(clips));
        if (root.optJSONObject("extensions") == null) {
            put(root, "extensions", new JSONObject());
        }
        put(root, "version", VERSION);
        return root;
    }

    private static void migrateEditorRelations(JSONObject editor, List<String> clipIds) {
        if (editor == null) {
            return;
        }
        ensureArray(editor, "filters");
        ensureArray(editor, "captions");
        ensureArray(editor, "compoundCaptions");
        ensureArray(editor, "stickers");
        ensureArray(editor, "transitions");
        ensureArray(editor, "audio");
        ensureArray(editor, "backgrounds");
        ensureArray(editor, "watermarks");
        ensureObject(editor, "moduleData");
        ensureIds(editor.optJSONArray("filters"), "filter");
        ensureIds(editor.optJSONArray("captions"), "caption");
        ensureIds(editor.optJSONArray("compoundCaptions"), "compound-caption");
        ensureIds(editor.optJSONArray("stickers"), "sticker");
        ensureIds(editor.optJSONArray("audio"), "audio");
        ensureIds(editor.optJSONArray("backgrounds"), "background");
        ensureIds(editor.optJSONArray("watermarks"), "watermark");

        JSONArray filters = editor.optJSONArray("filters");
        for (int index = 0; filters != null && index < filters.length(); index++) {
            JSONObject item = filters.optJSONObject(index);
            if (item != null && item.optString("clipId", "").isEmpty()) {
                put(item, "clipId", idAt(clipIds, item.optInt("clipIndex", -1)));
            }
            if (item != null) {
                item.remove("clipIndex");
                ensureObject(item, "parameters");
            }
        }
        JSONArray transitions = editor.optJSONArray("transitions");
        for (int index = 0; transitions != null && index < transitions.length(); index++) {
            JSONObject item = transitions.optJSONObject(index);
            if (item == null) {
                continue;
            }
            int sourceIndex = item.optInt("sourceClipIndex", -1);
            if (item.optString("sourceClipId", "").isEmpty()) {
                put(item, "sourceClipId", idAt(clipIds, sourceIndex));
            }
            if (item.optString("targetClipId", "").isEmpty()) {
                put(item, "targetClipId", idAt(clipIds, sourceIndex + 1));
            }
            item.remove("sourceClipIndex");
        }
        put(editor, "version", 2);
    }

    private static List<String> clipIds(JSONArray clips) {
        List<String> ids = new ArrayList<>();
        for (int index = 0; index < clips.length(); index++) {
            JSONObject clip = clips.optJSONObject(index);
            ids.add(clip == null ? "" : clip.optString("id", ""));
        }
        return ids;
    }

    private static void ensureIds(JSONArray array, String prefix) {
        for (int index = 0; array != null && index < array.length(); index++) {
            JSONObject item = array.optJSONObject(index);
            if (item != null && item.optString("id", "").isEmpty()) {
                put(item, "id", newStableId(prefix));
            }
        }
    }

    private static void ensureArray(JSONObject parent, String key) {
        if (parent.optJSONArray(key) == null) {
            put(parent, key, new JSONArray());
        }
    }

    private static void ensureObject(JSONObject parent, String key) {
        if (parent.optJSONObject(key) == null) {
            put(parent, key, new JSONObject());
        }
    }

    private static String idAt(List<String> ids, int index) {
        return index < 0 || index >= ids.size() ? "" : ids.get(index);
    }

    private static int positive(int value, int fallback) {
        return value > 0 ? value : fallback;
    }

    private static String newStableId(String prefix) {
        return MeisheAppSupport.createStableObjectId(prefix);
    }

    private static JSONObject copy(JSONObject value) {
        if (value == null) {
            return new JSONObject();
        }
        try {
            return new JSONObject(value.toString());
        } catch (JSONException exception) {
            return new JSONObject();
        }
    }

    private static JSONObject parseObject(String value) {
        try {
            return new JSONObject(value == null ? "" : value);
        } catch (JSONException exception) {
            return new JSONObject();
        }
    }

    private static void put(JSONObject target, String key, Object value) {
        try {
            target.put(key, value);
        } catch (JSONException ignored) {
        }
    }
}
