package {{PACKAGE_NAME}};

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;

public final class MeisheAppSupport {
    private MeisheAppSupport() {
    }

    public static void applySystemBarInsets(android.app.Activity activity) {
        if (activity == null || android.os.Build.VERSION.SDK_INT < 20) {
            return;
        }
        android.view.View content = activity.findViewById(android.R.id.content);
        if (content == null) {
            return;
        }
        int initialLeft = content.getPaddingLeft();
        int initialTop = content.getPaddingTop();
        int initialRight = content.getPaddingRight();
        int initialBottom = content.getPaddingBottom();
        content.setOnApplyWindowInsetsListener((view, insets) -> {
            view.setPadding(
                    initialLeft + insets.getSystemWindowInsetLeft(),
                    initialTop + insets.getSystemWindowInsetTop(),
                    initialRight + insets.getSystemWindowInsetRight(),
                    initialBottom + insets.getSystemWindowInsetBottom());
            return insets;
        });
        content.requestApplyInsets();
    }

    public static boolean requestPermissions(
            android.app.Activity activity,
            String[] permissions,
            int requestCode) {
        if (activity == null || permissions == null || permissions.length == 0) {
            return true;
        }
        if (android.os.Build.VERSION.SDK_INT < android.os.Build.VERSION_CODES.M) {
            return true;
        }
        ArrayList<String> missing = new ArrayList<>();
        for (String permission : permissions) {
            if (permission != null
                    && activity.checkSelfPermission(permission)
                    != android.content.pm.PackageManager.PERMISSION_GRANTED) {
                missing.add(permission);
            }
        }
        if (missing.isEmpty()) {
            return true;
        }
        activity.requestPermissions(missing.toArray(new String[0]), requestCode);
        return false;
    }

    public static boolean openFeature(
            android.content.Context context,
            Class<?> activityClass) {
        if (context == null || activityClass == null) {
            return false;
        }
        android.content.Intent intent = new android.content.Intent(context, activityClass);
        if (!(context instanceof android.app.Activity)) {
            intent.addFlags(android.content.Intent.FLAG_ACTIVITY_NEW_TASK);
        }
        context.startActivity(intent);
        return true;
    }

    public static android.app.AlertDialog showEditorMessage(
            android.content.Context context,
            String title,
            String message) {
        if (context == null) {
            return null;
        }
        return new android.app.AlertDialog.Builder(context)
                .setTitle(title == null ? "" : title)
                .setMessage(message == null ? "" : message)
                .setPositiveButton(android.R.string.ok, null)
                .show();
    }

    public static boolean saveProjectState(
            android.content.Context context,
            String projectId,
            String serializedState) {
        if (context == null || projectId == null || projectId.isEmpty() || serializedState == null) {
            return false;
        }
        return context.getSharedPreferences("meishe_projects", android.content.Context.MODE_PRIVATE)
                .edit()
                .putString(projectId, serializedState)
                .commit();
    }

    public static String createStableObjectId(String prefix) {
        String normalized = prefix == null || prefix.trim().isEmpty()
                ? "object"
                : prefix.trim();
        return normalized + "-" + java.util.UUID.randomUUID();
    }

    public static boolean saveAtomicProjectState(
            android.content.Context context,
            String projectId,
            String serializedState) {
        if (context == null || projectId == null || projectId.isEmpty()
                || serializedState == null || serializedState.isEmpty()) {
            return false;
        }
        String safeId = projectId.replaceAll("[^A-Za-z0-9._-]", "_");
        java.io.File projectDir = new java.io.File(
                new java.io.File(context.getFilesDir(), "meishe-projects"),
                safeId);
        if (!projectDir.isDirectory() && !projectDir.mkdirs()) {
            return false;
        }
        android.util.AtomicFile atomicFile = new android.util.AtomicFile(
                new java.io.File(projectDir, "project.json"));
        java.io.FileOutputStream output = null;
        try {
            output = atomicFile.startWrite();
            output.write(serializedState.getBytes(java.nio.charset.StandardCharsets.UTF_8));
            output.flush();
            output.getFD().sync();
            atomicFile.finishWrite(output);
            return true;
        } catch (java.io.IOException exception) {
            if (output != null) {
                atomicFile.failWrite(output);
            }
            return false;
        }
    }

    public static String loadAtomicProjectState(
            android.content.Context context,
            String projectId) {
        if (context == null || projectId == null || projectId.isEmpty()) {
            return "";
        }
        String safeId = projectId.replaceAll("[^A-Za-z0-9._-]", "_");
        java.io.File projectFile = new java.io.File(
                new java.io.File(
                        new java.io.File(context.getFilesDir(), "meishe-projects"),
                        safeId),
                "project.json");
        android.util.AtomicFile atomicFile = new android.util.AtomicFile(projectFile);
        if (!atomicFile.getBaseFile().isFile()) {
            return "";
        }
        try (java.io.FileInputStream input = atomicFile.openRead();
                java.io.ByteArrayOutputStream output = new java.io.ByteArrayOutputStream()) {
            byte[] buffer = new byte[8192];
            int count;
            while ((count = input.read(buffer)) >= 0) {
                output.write(buffer, 0, count);
            }
            return output.toString(java.nio.charset.StandardCharsets.UTF_8.name());
        } catch (java.io.IOException exception) {
            return "";
        }
    }

    public static boolean saveTimelineStructure(
            android.content.Context context,
            String projectId,
            com.meicam.sdk.NvsTimeline timeline,
            int width,
            int height) {
        if (context == null || projectId == null || projectId.isEmpty() || timeline == null) {
            return false;
        }
        com.meicam.sdk.NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null) {
            return false;
        }
        try {
            android.content.SharedPreferences preferences = context.getSharedPreferences(
                    "meishe_projects",
                    android.content.Context.MODE_PRIVATE);
            String current = preferences.getString(projectId, "");
            org.json.JSONObject existing = current == null || current.isEmpty()
                    ? new org.json.JSONObject()
                    : new org.json.JSONObject(current);
            org.json.JSONObject root = new org.json.JSONObject();
            root.put("version", 2);
            root.put("width", width);
            root.put("height", height);
            org.json.JSONArray clips = new org.json.JSONArray();
            for (int index = 0; index < track.getClipCount(); index++) {
                com.meicam.sdk.NvsVideoClip clip = track.getClipByIndex(index);
                if (clip == null || clip.getFilePath() == null || clip.getFilePath().isEmpty()) {
                    continue;
                }
                org.json.JSONObject item = new org.json.JSONObject();
                item.put("path", clip.getFilePath());
                item.put("trimInUs", clip.getTrimIn());
                item.put("trimOutUs", clip.getTrimOut());
                item.put("speed", clip.getSpeed());
                item.put("keepAudioPitch", clip.isKeepAudioPitch());
                item.put("videoType", clip.getVideoType());
                item.put("imageMotion", clip.getImageMotionAnimationEnabled());
                clips.put(item);
            }
            if (clips.length() == 0) {
                return false;
            }
            root.put("clips", clips);
            org.json.JSONObject editor = existing.optJSONObject("editor");
            if (editor != null) {
                root.put("editor", editor);
            }
            return preferences.edit()
                    .putString(projectId, root.toString())
                    .putString("latest_project_id", projectId)
                    .commit();
        } catch (org.json.JSONException exception) {
            return false;
        }
    }

    public static String loadProjectState(android.content.Context context, String projectId) {
        if (context == null || projectId == null || projectId.isEmpty()) {
            return "";
        }
        return context.getSharedPreferences("meishe_projects", android.content.Context.MODE_PRIVATE)
                .getString(projectId, "");
    }

    public static String latestProjectId(android.content.Context context) {
        if (context == null) {
            return "";
        }
        return context.getSharedPreferences("meishe_projects", android.content.Context.MODE_PRIVATE)
                .getString("latest_project_id", "");
    }

    public static int readProjectDimension(String serializedState, String key, int fallback) {
        if (serializedState == null || serializedState.isEmpty() || key == null || key.isEmpty()) {
            return fallback;
        }
        try {
            return new org.json.JSONObject(serializedState).optInt(key, fallback);
        } catch (org.json.JSONException exception) {
            return fallback;
        }
    }

    public static int restoreTimelineStructure(
            com.meicam.sdk.NvsTimeline timeline,
            String serializedState) {
        if (timeline == null || serializedState == null || serializedState.isEmpty()) {
            return 0;
        }
        com.meicam.sdk.NvsVideoTrack track = timeline.getVideoTrackByIndex(0);
        if (track == null) {
            track = timeline.appendVideoTrack();
        }
        if (track == null) {
            return 0;
        }
        try {
            org.json.JSONArray clips = new org.json.JSONObject(serializedState).optJSONArray("clips");
            if (clips == null || clips.length() == 0) {
                return 0;
            }
            track.removeAllClips();
            int restored = 0;
            for (int index = 0; index < clips.length(); index++) {
                org.json.JSONObject item = clips.optJSONObject(index);
                if (item == null) {
                    continue;
                }
                String path = item.optString("path", "");
                if (path.isEmpty() || !new java.io.File(path).isFile()) {
                    continue;
                }
                long trimInUs = Math.max(0, item.optLong("trimInUs", 0));
                long trimOutUs = item.optLong("trimOutUs", 0);
                com.meicam.sdk.NvsVideoClip clip = trimOutUs > trimInUs
                        ? track.appendClip(path, trimInUs, trimOutUs)
                        : track.appendClip(path);
                if (clip == null) {
                    continue;
                }
                double speed = item.optDouble("speed", 1.0);
                if (!Double.isNaN(speed)
                        && !Double.isInfinite(speed)
                        && speed > 0
                        && Math.abs(speed - 1.0) > 0.0001) {
                    clip.changeSpeed(speed, item.optBoolean("keepAudioPitch", true));
                }
                if (clip.getVideoType() == com.meicam.sdk.NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {
                    clip.setImageMotionAnimationEnabled(item.optBoolean("imageMotion", false));
                }
                restored++;
            }
            return restored;
        } catch (org.json.JSONException exception) {
            return 0;
        }
    }

    public static Map<String, Object> buildEffectParameter(
            String key,
            String type,
            Object value) {
        if (key == null || key.isEmpty() || type == null || type.isEmpty()) {
            return java.util.Collections.emptyMap();
        }
        Map<String, Object> parameter = new LinkedHashMap<>();
        parameter.put("key", key);
        parameter.put("type", type);
        parameter.put("value", value);
        return java.util.Collections.unmodifiableMap(parameter);
    }

    public static android.content.Intent createFeedbackIntent(
            String email,
            String subject,
            String body) {
        android.content.Intent intent = new android.content.Intent(
                android.content.Intent.ACTION_SENDTO);
        String address = email == null ? "" : email.trim();
        intent.setData(android.net.Uri.parse("mailto:" + android.net.Uri.encode(address)));
        intent.putExtra(android.content.Intent.EXTRA_SUBJECT, subject == null ? "" : subject);
        intent.putExtra(android.content.Intent.EXTRA_TEXT, body == null ? "" : body);
        return intent;
    }
}
