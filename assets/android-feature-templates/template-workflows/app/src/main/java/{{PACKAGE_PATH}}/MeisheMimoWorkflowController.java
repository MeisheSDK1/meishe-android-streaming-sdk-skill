package {{PACKAGE_NAME}};

import android.content.Context;

import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsAudioResolution;
import com.meicam.sdk.NvsAudioTrack;
import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsRational;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsTimelineCompoundCaption;
import com.meicam.sdk.NvsTimelineVideoFx;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoFx;
import com.meicam.sdk.NvsVideoResolution;
import com.meicam.sdk.NvsVideoTrack;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Hashtable;
import java.util.List;
import java.util.Locale;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public final class MeisheMimoWorkflowController {
    private static final long US_PER_MS = 1000L;
    private static final int MAX_ARCHIVE_ENTRIES = 2048;
    private static final long MAX_EXTRACTED_BYTES = 256L * 1024L * 1024L;

    public ExtractedMimoPackage extractArchive(
            InputStream archiveInput,
            File outputDirectory) throws IOException {
        if (archiveInput == null) {
            throw new IOException("Mimo archive input is missing");
        }
        if (outputDirectory == null) {
            throw new IOException("Mimo extraction directory is missing");
        }
        if (!outputDirectory.exists() && !outputDirectory.mkdirs()) {
            throw new IOException("Cannot create Mimo extraction directory");
        }
        String extractionRoot = outputDirectory.getCanonicalPath() + File.separator;
        File infoFile = null;
        long extractedBytes = 0L;
        int entryCount = 0;
        byte[] buffer = new byte[32 * 1024];
        try (ZipInputStream zipInput = new ZipInputStream(archiveInput)) {
            ZipEntry entry;
            while ((entry = zipInput.getNextEntry()) != null) {
                entryCount++;
                if (entryCount > MAX_ARCHIVE_ENTRIES) {
                    throw new IOException("Mimo archive contains too many entries");
                }
                File outputFile = new File(outputDirectory, entry.getName());
                String outputPath = outputFile.getCanonicalPath();
                if (!outputPath.startsWith(extractionRoot)) {
                    throw new IOException("Unsafe Mimo archive entry: " + entry.getName());
                }
                if (entry.isDirectory()) {
                    if (!outputFile.exists() && !outputFile.mkdirs()) {
                        throw new IOException("Cannot create Mimo archive directory");
                    }
                    continue;
                }
                File parent = outputFile.getParentFile();
                if (parent != null && !parent.exists() && !parent.mkdirs()) {
                    throw new IOException("Cannot create Mimo archive parent directory");
                }
                try (FileOutputStream output = new FileOutputStream(outputFile)) {
                    int read;
                    while ((read = zipInput.read(buffer)) != -1) {
                        extractedBytes += read;
                        if (extractedBytes > MAX_EXTRACTED_BYTES) {
                            throw new IOException("Mimo archive exceeds extraction limit");
                        }
                        output.write(buffer, 0, read);
                    }
                }
                if ("info.json".equalsIgnoreCase(outputFile.getName()) && infoFile == null) {
                    infoFile = outputFile;
                }
            }
        }
        if (infoFile == null || !infoFile.isFile()) {
            throw new IOException("Mimo archive does not contain info.json");
        }
        return new ExtractedMimoPackage(infoFile.getParentFile(), infoFile);
    }

    public MimoSpec parse(InputStream input) throws IOException, JSONException {
        if (input == null) {
            throw new IOException("Mimo info.json input is missing");
        }
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        byte[] buffer = new byte[8 * 1024];
        int count;
        while ((count = input.read(buffer)) != -1) {
            output.write(buffer, 0, count);
        }
        JSONObject root = new JSONObject(new String(
                output.toByteArray(),
                StandardCharsets.UTF_8));
        JSONArray shotArray = root.optJSONArray("shotInfos");
        if (shotArray == null || shotArray.length() == 0) {
            throw new JSONException("Mimo template has no shotInfos");
        }
        ArrayList<ShotSpec> shots = new ArrayList<>();
        for (int index = 0; index < shotArray.length(); index++) {
            JSONObject shot = shotArray.optJSONObject(index);
            if (shot == null) {
                continue;
            }
            long durationMs = Math.max(1L, Math.round(shot.optDouble("duration", 0d)));
            shots.add(new ShotSpec(
                    shot.optInt("shot", index),
                    durationMs * US_PER_MS,
                    shot.optString("source", ""),
                    shot.optString("filter", ""),
                    shot.optString("trans", ""),
                    shot.optString("compoundCaption", "")));
        }
        if (shots.isEmpty()) {
            throw new JSONException("Mimo template has no valid shots");
        }
        return new MimoSpec(
                root.optString("id", ""),
                root.optString("supportedAspectRatio", "16v9"),
                root.optString("music", ""),
                Math.max(0L, root.optLong("musicDuration", 0L)) * US_PER_MS,
                root.optString("timelineFilter", ""),
                root.optString("endingFilter", ""),
                Math.max(0L, root.optLong("endingFilterLen", 0L)) * US_PER_MS,
                shots);
    }

    public AssetInstallResult installChildPackages(
            Context context,
            NvsStreamingContext streamingContext,
            String assetRoot) throws IOException {
        MeisheThreading.requireMainThread("install Mimo child packages");
        if (context == null || streamingContext == null || assetRoot == null
                || assetRoot.isEmpty()) {
            return new AssetInstallResult(0, 0,
                    Collections.singletonList("Mimo asset root is unavailable"));
        }
        String[] names = context.getAssets().list(assetRoot);
        if (names == null || names.length == 0) {
            return new AssetInstallResult(0, 0,
                    Collections.singletonList("Mimo asset root is empty"));
        }
        NvsAssetPackageManager packageManager = streamingContext.getAssetPackageManager();
        int attempted = 0;
        int installed = 0;
        ArrayList<String> failures = new ArrayList<>();
        for (String name : names) {
            int packageType = packageTypeForName(name);
            if (packageType < 0) {
                continue;
            }
            attempted++;
            String packagePath = "assets:/" + assetRoot + "/" + name;
            StringBuilder packageId = new StringBuilder();
            int code = packageManager.installAssetPackage(
                    packagePath,
                    null,
                    packageType,
                    true,
                    packageId);
            if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
                    || code == NvsAssetPackageManager
                    .ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
                installed++;
            } else {
                failures.add(name + ": install error=" + code);
            }
        }
        return new AssetInstallResult(attempted, installed, failures);
    }

    public AssetInstallResult installExtractedChildPackages(
            NvsStreamingContext streamingContext,
            File assetRoot) {
        MeisheThreading.requireMainThread("install extracted Mimo child packages");
        if (streamingContext == null || assetRoot == null || !assetRoot.isDirectory()) {
            return new AssetInstallResult(0, 0,
                    Collections.singletonList("Extracted Mimo asset root is unavailable"));
        }
        ArrayList<File> pending = new ArrayList<>();
        pending.add(assetRoot);
        NvsAssetPackageManager packageManager = streamingContext.getAssetPackageManager();
        int attempted = 0;
        int installed = 0;
        ArrayList<String> failures = new ArrayList<>();
        while (!pending.isEmpty()) {
            File current = pending.remove(pending.size() - 1);
            File[] children = current.listFiles();
            if (children == null) {
                continue;
            }
            for (File child : children) {
                if (child.isDirectory()) {
                    pending.add(child);
                    continue;
                }
                int packageType = packageTypeForName(child.getName());
                if (packageType < 0) {
                    continue;
                }
                attempted++;
                StringBuilder packageId = new StringBuilder();
                int code = packageManager.installAssetPackage(
                        child.getAbsolutePath(),
                        null,
                        packageType,
                        true,
                        packageId);
                if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
                        || code == NvsAssetPackageManager
                        .ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
                    installed++;
                } else {
                    failures.add(child.getName() + ": install error=" + code);
                }
            }
        }
        return new AssetInstallResult(attempted, installed, failures);
    }

    public File findExtractedFile(File root, String relativeName) {
        if (root == null || !root.isDirectory() || relativeName == null
                || relativeName.isEmpty()) {
            return null;
        }
        File direct = new File(root, relativeName);
        if (direct.isFile()) {
            return direct;
        }
        String expectedName = new File(relativeName).getName();
        ArrayList<File> pending = new ArrayList<>();
        pending.add(root);
        while (!pending.isEmpty()) {
            File current = pending.remove(pending.size() - 1);
            File[] children = current.listFiles();
            if (children == null) {
                continue;
            }
            for (File child : children) {
                if (child.isDirectory()) {
                    pending.add(child);
                } else if (expectedName.equals(child.getName())) {
                    return child;
                }
            }
        }
        return null;
    }

    public BuildResult buildTimeline(
            NvsStreamingContext streamingContext,
            MimoSpec spec,
            List<String> mediaPaths,
            String musicPath,
            NvsVideoResolution videoResolution,
            NvsRational videoFps,
            NvsAudioResolution audioResolution) {
        MeisheThreading.requireMainThread("build Mimo timeline");
        ArrayList<String> failures = new ArrayList<>();
        if (streamingContext == null || spec == null || spec.shots.isEmpty()
                || mediaPaths == null || mediaPaths.isEmpty() || videoResolution == null
                || videoFps == null || audioResolution == null) {
            failures.add("Mimo timeline inputs are incomplete");
            return new BuildResult(null, 0, 0, 0, failures);
        }
        NvsTimeline timeline = streamingContext.createTimeline(
                videoResolution,
                videoFps,
                audioResolution);
        if (timeline == null) {
            failures.add("SDK did not create a Mimo Timeline");
            return new BuildResult(null, 0, 0, 0, failures);
        }
        NvsVideoTrack track = timeline.appendVideoTrack();
        if (track == null) {
            failures.add("SDK did not create a Mimo video track");
            return new BuildResult(timeline, 0, 0, 0, failures);
        }
        track.setVolumeGain(0f, 0f);
        int clipCount = 0;
        int effectCount = 0;
        int captionCount = 0;
        ArrayList<String> transitions = new ArrayList<>();
        for (int index = 0; index < spec.shots.size(); index++) {
            ShotSpec shot = spec.shots.get(index);
            String mediaPath = mediaPaths.get(Math.min(index, mediaPaths.size() - 1));
            if (mediaPath == null || mediaPath.isEmpty()) {
                failures.add("shot " + shot.index + ": media path is missing");
                continue;
            }
            long inPoint = track.getDuration();
            NvsVideoClip clip = track.appendClip(mediaPath, 0, shot.durationUs);
            if (clip == null) {
                clip = track.appendClip(mediaPath);
            }
            if (clip == null) {
                failures.add("shot " + shot.index + ": SDK rejected media");
                continue;
            }
            clipCount++;
            clip.setPanAndScan(0f, 1f);
            if (!shot.filterId.isEmpty()) {
                NvsVideoFx filter = clip.appendPackagedFx(shot.filterId);
                if (filter != null) {
                    effectCount++;
                } else {
                    failures.add("shot " + shot.index + ": filter was not applied");
                }
            }
            if (!shot.compoundCaptionId.isEmpty()) {
                NvsTimelineCompoundCaption caption = timeline.addCompoundCaption(
                        inPoint,
                        Math.min(shot.durationUs, clip.getOutPoint() - inPoint),
                        shot.compoundCaptionId);
                if (caption != null) {
                    captionCount++;
                    for (int captionIndex = 0;
                         captionIndex < caption.getCaptionCount();
                         captionIndex++) {
                        caption.setText(captionIndex, "Mimo " + (index + 1));
                    }
                } else {
                    failures.add("shot " + shot.index + ": compound caption was not applied");
                }
            }
            transitions.add(shot.transitionId);
        }
        for (int index = 0; index + 1 < track.getClipCount()
                && index < transitions.size(); index++) {
            String transition = transitions.get(index);
            if (!transition.isEmpty()) {
                track.setPackagedTransition(index, transition);
            }
        }
        if (!spec.timelineFilterId.isEmpty() && timeline.getDuration() > 0) {
            NvsTimelineVideoFx timelineFilter = timeline.addPackagedTimelineVideoFx(
                    0,
                    timeline.getDuration(),
                    spec.timelineFilterId);
            if (timelineFilter != null) {
                effectCount++;
            } else {
                failures.add("Mimo timeline filter was not applied");
            }
        }
        if (!spec.endingFilterId.isEmpty() && spec.endingFilterDurationUs > 0
                && timeline.getDuration() > 0) {
            long durationUs = Math.min(spec.endingFilterDurationUs, timeline.getDuration());
            NvsTimelineVideoFx endingFilter = timeline.addPackagedTimelineVideoFx(
                    timeline.getDuration() - durationUs,
                    durationUs,
                    spec.endingFilterId);
            if (endingFilter != null) {
                effectCount++;
            }
        }
        if (musicPath != null && !musicPath.isEmpty() && timeline.getDuration() > 0) {
            NvsAudioTrack audioTrack = timeline.appendAudioTrack();
            long audioDurationUs = spec.musicDurationUs > 0
                    ? Math.min(spec.musicDurationUs, timeline.getDuration())
                    : timeline.getDuration();
            if (audioTrack == null || audioTrack.appendClip(
                    musicPath,
                    0,
                    audioDurationUs) == null) {
                failures.add("Mimo music was not appended");
            }
        }
        return new BuildResult(timeline, clipCount, effectCount, captionCount, failures);
    }

    public boolean reconnectPreview(
            NvsStreamingContext streamingContext,
            NvsTimeline timeline,
            NvsLiveWindow liveWindow,
            long positionUs,
            int seekFlags) {
        MeisheThreading.requireMainThread("connect Mimo preview");
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

    public boolean export(
            NvsStreamingContext streamingContext,
            NvsTimeline timeline,
            String outputPath,
            int resolutionGrade,
            int bitrateGrade,
            Hashtable<String, Object> compileConfigurations,
            int compileFlags) {
        MeisheThreading.requireMainThread("export Mimo timeline");
        if (streamingContext == null || timeline == null || timeline.getDuration() <= 0
                || outputPath == null || outputPath.isEmpty()) {
            return false;
        }
        streamingContext.stop();
        Hashtable<String, Object> safeConfigurations = compileConfigurations == null
                ? new Hashtable<String, Object>()
                : compileConfigurations;
        return streamingContext.compileTimeline(
                timeline,
                0,
                timeline.getDuration(),
                outputPath,
                resolutionGrade,
                bitrateGrade,
                safeConfigurations,
                compileFlags);
    }

    private int packageTypeForName(String name) {
        if (name == null) {
            return -1;
        }
        String normalized = name.toLowerCase(Locale.US);
        if (normalized.endsWith(".videofx")) {
            return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
        }
        if (normalized.endsWith(".videotransition")) {
            return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;
        }
        if (normalized.endsWith(".compoundcaption")) {
            return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
        }
        if (normalized.endsWith(".animatedsticker")) {
            return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
        }
        return -1;
    }

    public static final class MimoSpec {
        public final String id;
        public final String supportedAspectRatio;
        public final String musicFileName;
        public final long musicDurationUs;
        public final String timelineFilterId;
        public final String endingFilterId;
        public final long endingFilterDurationUs;
        public final List<ShotSpec> shots;

        MimoSpec(
                String id,
                String supportedAspectRatio,
                String musicFileName,
                long musicDurationUs,
                String timelineFilterId,
                String endingFilterId,
                long endingFilterDurationUs,
                List<ShotSpec> shots) {
            this.id = id;
            this.supportedAspectRatio = supportedAspectRatio;
            this.musicFileName = musicFileName;
            this.musicDurationUs = musicDurationUs;
            this.timelineFilterId = timelineFilterId;
            this.endingFilterId = endingFilterId;
            this.endingFilterDurationUs = endingFilterDurationUs;
            this.shots = Collections.unmodifiableList(new ArrayList<>(shots));
        }
    }

    public static final class ExtractedMimoPackage {
        public final File rootDirectory;
        public final File infoFile;

        ExtractedMimoPackage(File rootDirectory, File infoFile) {
            this.rootDirectory = rootDirectory;
            this.infoFile = infoFile;
        }
    }

    public static final class ShotSpec {
        public final int index;
        public final long durationUs;
        public final String bundledSource;
        public final String filterId;
        public final String transitionId;
        public final String compoundCaptionId;

        ShotSpec(
                int index,
                long durationUs,
                String bundledSource,
                String filterId,
                String transitionId,
                String compoundCaptionId) {
            this.index = index;
            this.durationUs = durationUs;
            this.bundledSource = bundledSource;
            this.filterId = filterId;
            this.transitionId = transitionId;
            this.compoundCaptionId = compoundCaptionId;
        }
    }

    public static final class AssetInstallResult {
        public final int attempted;
        public final int installed;
        public final List<String> failures;

        AssetInstallResult(int attempted, int installed, List<String> failures) {
            this.attempted = attempted;
            this.installed = installed;
            this.failures = Collections.unmodifiableList(new ArrayList<>(failures));
        }
    }

    public static final class BuildResult {
        public final NvsTimeline timeline;
        public final int clipCount;
        public final int appliedEffectCount;
        public final int compoundCaptionCount;
        public final List<String> failures;

        BuildResult(
                NvsTimeline timeline,
                int clipCount,
                int appliedEffectCount,
                int compoundCaptionCount,
                List<String> failures) {
            this.timeline = timeline;
            this.clipCount = clipCount;
            this.appliedEffectCount = appliedEffectCount;
            this.compoundCaptionCount = compoundCaptionCount;
            this.failures = Collections.unmodifiableList(new ArrayList<>(failures));
        }
    }
}
