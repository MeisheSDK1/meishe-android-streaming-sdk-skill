package {{PACKAGE_NAME}};

import android.graphics.PointF;

import com.meicam.sdk.NvsAVFileInfo;
import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsAudioTrack;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimelineCaption;
import com.meicam.sdk.NvsTimelineAnimatedSticker;
import com.meicam.sdk.NvsTimelineCompoundCaption;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoTrack;

import java.util.Map;

public final class MeisheEditorOverlayController {
    public interface Listener {
        void onStatusChanged(String message);
    }

    private final MeisheEditorSessionController session;
    private final MeisheEditorProjectController project;
    private final MeisheEffectController effectController = new MeisheEffectController();
    private final MeisheCaptionStickerController captionController =
            new MeisheCaptionStickerController();
    private final MeisheAudioController audioController = new MeisheAudioController();
    private final Listener listener;
    private final Map<String, String> packageIds;
    private String captionStylePackageId;
    private String captionFontFilePath;

    public MeisheEditorOverlayController(
            MeisheEditorSessionController session,
            MeisheEditorProjectController project,
            Listener listener) {
        if (session == null || project == null || listener == null) {
            throw new IllegalArgumentException("session, project, and listener are required");
        }
        this.session = session;
        this.project = project;
        this.listener = listener;
        MeisheAssetInstaller installer = new MeisheAssetInstaller(session.streamingContext());
        packageIds = MeisheSampleAssets.installDefaultPackages(installer);
        String selectedStyle = project.selectedCaptionStylePackageId();
        captionStylePackageId = selectedStyle.isEmpty() ? null : selectedStyle;
    }

    public void applyDefaultFilter() {
        applyDefaultFilter(0);
    }

    public void applyDefaultFilter(int clipIndex) {
        applyPackagedClipEffect(
                packageIds.get("filter"),
                MeisheMaterialApplicationKind.FILTER,
                "Filter",
                clipIndex);
    }

    public void applyDefaultSticker() {
        applyAnimatedSticker(
                packageIds.get("animatedSticker"),
                MeisheSampleAssets.SAMPLE_STICKER_IMAGE_PATH,
                "Stickers");
    }

    public void applyDefaultTransition() {
        applyDefaultTransition(0);
    }

    public void applyDefaultTransition(int sourceClipIndex) {
        applyTransition(packageIds.get("transition"), "Transitions", sourceClipIndex);
    }

    public void applyPackagedFilter(String packageId) {
        applyPackagedClipEffect(
                packageId,
                MeisheMaterialApplicationKind.FILTER,
                "Filter",
                0);
    }

    public void applyPackagedClipEffect(
            String packageId,
            String applicationKind,
            String materialLabel,
            int clipIndex) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        NvsVideoTrack videoTrack = session.videoTrack();
        int targetClipIndex = clipIndex >= 0 ? clipIndex : 0;
        NvsVideoClip targetClip = videoTrack != null && targetClipIndex < videoTrack.getClipCount()
                ? videoTrack.getClipByIndex(targetClipIndex)
                : null;
        if (effectController.appendPackagedClipFx(targetClip, packageId) == null) {
            listener.onStatusChanged(
                    "Filter could not be applied. Check package installation and license.");
            return;
        }
        project.replaceEditorState(MeisheEditorProjectStore.recordPackagedFilterByClipId(
                project.editorState(),
                project.clipIdAt(targetClipIndex),
                packageId,
                applicationKind,
                materialLabel));
        project.captureAndPersist();
        session.refreshPreview(session.currentPosition());
        listener.onStatusChanged("Applied “" + materialLabel + "” to clip "
                + (targetClipIndex + 1) + ".");
    }

    public void addCaption(String text) {
        addCaptionWithMaterial(
                text,
                captionStylePackageId,
                captionFontFilePath,
                "",
                "",
                "",
                captionStylePackageId == null ? "Captions" : "Caption style");
    }

    public void addCaptionWithMaterial(
            String text,
            String stylePackageId,
            String fontFilePath,
            String contextPackageId,
            String rendererPackageId,
            String animationPackageId,
            String materialLabel) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        String captionText = text == null ? "" : text.trim();
        if (captionText.isEmpty()) {
            listener.onStatusChanged("Caption text cannot be empty.");
            return;
        }
        long inPointUs = session.overlayInPoint();
        long durationUs = session.overlayDuration(inPointUs);
        NvsTimelineCaption caption = captionController.addCaption(
                session.timeline(),
                captionText,
                inPointUs,
                durationUs,
                emptyToNull(stylePackageId));
        if (caption == null) {
            listener.onStatusChanged("Caption could not be added.");
            return;
        }
        if (stylePackageId == null || stylePackageId.isEmpty()) {
            captionController.applyReadableDefaultStyle(caption);
        }
        if (fontFilePath != null && !fontFilePath.isEmpty()) {
            caption.setFontByFilePath(fontFilePath);
        }
        if (!captionController.applyModularCaptionAssets(
                caption,
                null,
                emptyToNull(contextPackageId),
                emptyToNull(rendererPackageId),
                emptyToNull(animationPackageId),
                null,
                null,
                900,
                0,
                0)) {
            session.timeline().removeCaption(caption);
            listener.onStatusChanged("This caption material could not be applied. Check its type and license.");
            return;
        }
        project.replaceEditorState(MeisheEditorProjectStore.recordCaptionWithMaterial(
                project.editorState(),
                captionText,
                inPointUs,
                durationUs,
                stylePackageId,
                stylePackageId == null || stylePackageId.isEmpty(),
                fontFilePath,
                contextPackageId,
                rendererPackageId,
                animationPackageId,
                materialLabel));
        project.captureAndPersist();
        session.refreshPreview(inPointUs);
        listener.onStatusChanged("Added “" + materialLabel + "” with the entered text to the caption track.");
    }

    public void applyAnimatedSticker(String packageId) {
        applyAnimatedSticker(packageId, null, "Stickers");
    }

    public void applyCustomAnimatedSticker(
            String packageId,
            String customImagePath,
            String materialLabel) {
        applyAnimatedSticker(packageId, customImagePath, materialLabel);
    }

    private void applyAnimatedSticker(
            String packageId,
            String customImagePath,
            String materialLabel) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        long inPointUs = session.overlayInPoint();
        long durationUs = session.overlayDuration(inPointUs);
        NvsTimelineAnimatedSticker sticker = customImagePath == null
                ? captionController.addAnimatedSticker(
                        session.timeline(),
                        inPointUs,
                        durationUs,
                        packageId)
                : captionController.addCustomAnimatedSticker(
                        session.timeline(),
                        inPointUs,
                        durationUs,
                        packageId,
                        customImagePath);
        if (sticker == null) {
            listener.onStatusChanged(
                    "Sticker could not be added. Check its package, ratio support, and license.");
            return;
        }
        captionController.configureAnimatedSticker(
                sticker,
                new PointF(0.0f, 0.0f),
                new PointF(0.0f, 0.0f),
                0.78f,
                0.0f,
                false,
                20.0f,
                1.0f,
                1.0f,
                null,
                null,
                null,
                0,
                0,
                0);
        project.replaceEditorState(MeisheEditorProjectStore.recordSticker(
                project.editorState(),
                inPointUs,
                durationUs,
                packageId,
                customImagePath,
                materialLabel));
        project.captureAndPersist();
        session.refreshPreview(inPointUs);
        listener.onStatusChanged("Added “" + materialLabel + "” to the sticker track and refreshed the preview.");
    }

    public void addCompoundCaption(
            String packageId,
            String materialLabel,
            String text) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        String captionText = text == null ? "" : text.trim();
        if (captionText.isEmpty()) {
            listener.onStatusChanged("A compound caption requires text.");
            return;
        }
        long inPointUs = session.overlayInPoint();
        long durationUs = session.overlayDuration(inPointUs);
        NvsTimelineCompoundCaption caption = captionController.addCompoundCaption(
                session.timeline(),
                inPointUs,
                durationUs,
                packageId);
        if (caption == null) {
            listener.onStatusChanged("The compound caption could not be added. Check its package and license.");
            return;
        }
        String[] textSlots = captionText.split("\\r?\\n", -1);
        for (int index = 0;
                index < textSlots.length && index < caption.getCaptionCount();
                index++) {
            caption.setText(index, textSlots[index]);
        }
        project.replaceEditorState(MeisheEditorProjectStore.recordCompoundCaption(
                project.editorState(),
                captionText,
                inPointUs,
                durationUs,
                packageId,
                materialLabel));
        project.captureAndPersist();
        session.refreshPreview(inPointUs);
        listener.onStatusChanged("Added “" + materialLabel + "” with the entered text to the compound-caption track.");
    }

    public void applyStickerInAnimation(String packageId, String materialLabel) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        java.util.List<NvsTimelineAnimatedSticker> stickers =
                captionController.listAnimatedStickers(session.timeline());
        if (stickers.isEmpty()) {
            listener.onStatusChanged("A sticker in-animation requires an existing sticker. Add a sticker first.");
            return;
        }
        NvsTimelineAnimatedSticker sticker = stickers.get(stickers.size() - 1);
        if (!sticker.applyAnimatedStickerInAnimation(packageId)) {
            listener.onStatusChanged("The sticker in-animation could not be applied.");
            return;
        }
        sticker.setAnimatedStickerInAnimationDuration(500);
        project.replaceEditorState(MeisheEditorProjectStore.attachStickerInAnimation(
                project.editorState(),
                packageId,
                materialLabel));
        project.captureAndPersist();
        session.refreshPreview(session.currentPosition());
        listener.onStatusChanged("Applied “" + materialLabel + "” to the most recently added sticker.");
    }

    public void applyTransition(String packageId) {
        applyTransition(packageId, "Transitions", 0);
    }

    public void applyTransition(String packageId, String materialLabel, int sourceClipIndex) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        NvsVideoTrack track = session.videoTrack();
        if (track == null || track.getClipCount() < 2) {
            listener.onStatusChanged("A transition requires at least two clips.");
            return;
        }
        int boundaryIndex = Math.max(0, Math.min(sourceClipIndex, track.getClipCount() - 2));
        if (track.setPackagedTransition(boundaryIndex, packageId) == null) {
            listener.onStatusChanged("Transition could not be applied.");
            return;
        }
        project.replaceEditorState(MeisheEditorProjectStore.recordTransitionByClipIds(
                project.editorState(),
                project.clipIdAt(boundaryIndex),
                project.clipIdAt(boundaryIndex + 1),
                packageId,
                materialLabel));
        project.captureAndPersist();
        session.refreshPreview(session.currentPosition());
        listener.onStatusChanged("Applied “" + materialLabel + "” between clips "
                + (boundaryIndex + 1) + " and " + (boundaryIndex + 2) + ".");
    }

    public void applyBundledMusic() {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        NvsAVFileInfo audioInfo = NvsStreamingContext.getAVInfoFromFile(
                MeisheSampleAssets.SAMPLE_AUDIO_PATH,
                0);
        if (audioInfo == null || audioInfo.getDuration() <= 0) {
            listener.onStatusChanged("The local sample music could not be read.");
            return;
        }
        NvsAudioTrack track = audioController.ensureAudioTrack(session.timeline(), 0);
        audioController.clearTrack(track);
        long durationUs = Math.min(audioInfo.getDuration(), session.duration());
        if (audioController.addClip(
                track,
                MeisheSampleAssets.SAMPLE_AUDIO_PATH,
                0,
                0,
                durationUs) == null) {
            listener.onStatusChanged("The local sample music could not be added.");
            return;
        }
        project.replaceEditorState(MeisheEditorProjectStore.replaceAudioTrackWithClip(
                project.editorState(),
                0,
                MeisheSampleAssets.SAMPLE_AUDIO_PATH,
                0,
                0,
                durationUs));
        project.captureAndPersist();
        session.refreshPreview(session.currentPosition());
        listener.onStatusChanged("Added the local sample music to the timeline.");
    }

    public void applyDownloadedPackage(String packageId, int packageType) {
        applyInstalledMaterial(
                packageId,
                packageType,
                null,
                inferApplicationKind(packageType),
                "Materials",
                null,
                null,
                0);
    }

    public void applyDownloadedPackage(
            String packageId,
            int packageType,
            String localAssetPath) {
        applyInstalledMaterial(
                packageId,
                packageType,
                localAssetPath,
                inferApplicationKind(packageType),
                "Materials",
                null,
                null,
                0);
    }

    public void applyInstalledMaterial(
            String packageId,
            int packageType,
            String localAssetPath,
            String applicationKind,
            String materialLabel,
            String userText,
            String customImagePath,
            int selectedClipIndex) {
        String label = materialLabel == null || materialLabel.isEmpty() ? "Materials" : materialLabel;
        if (MeisheMaterialApplicationKind.FILTER.equals(applicationKind)
                || MeisheMaterialApplicationKind.CLIP_EFFECT.equals(applicationKind)) {
            applyPackagedClipEffect(packageId, applicationKind, label, selectedClipIndex);
        } else if (MeisheMaterialApplicationKind.TRANSITION.equals(applicationKind)) {
            applyTransition(packageId, label, selectedClipIndex);
        } else if (MeisheMaterialApplicationKind.CAPTION_STYLE.equals(applicationKind)) {
            captionStylePackageId = packageId;
            project.selectCaptionStyle(packageId);
            addCaptionWithMaterial(userText, packageId, "", "", "", "", label);
        } else if (MeisheMaterialApplicationKind.COMPOUND_CAPTION.equals(applicationKind)) {
            addCompoundCaption(packageId, label, userText);
        } else if (MeisheMaterialApplicationKind.CAPTION_CONTEXT.equals(applicationKind)) {
            addCaptionWithMaterial(userText, "", "", packageId, "", "", label);
        } else if (MeisheMaterialApplicationKind.CAPTION_RENDERER.equals(applicationKind)) {
            addCaptionWithMaterial(userText, "", "", "", packageId, "", label);
        } else if (MeisheMaterialApplicationKind.CAPTION_ANIMATION.equals(applicationKind)) {
            addCaptionWithMaterial(userText, "", "", "", "", packageId, label);
        } else if (MeisheMaterialApplicationKind.FONT.equals(applicationKind)) {
            captionFontFilePath = localAssetPath;
            addCaptionWithMaterial(userText, "", localAssetPath, "", "", "", label);
        } else if (MeisheMaterialApplicationKind.CUSTOM_STICKER.equals(applicationKind)) {
            applyCustomAnimatedSticker(packageId, customImagePath, label);
        } else if (MeisheMaterialApplicationKind.STICKER_IN_ANIMATION.equals(applicationKind)) {
            applyStickerInAnimation(packageId, label);
        } else if (MeisheMaterialApplicationKind.THEME.equals(applicationKind)) {
            applyTheme(packageId, label);
        } else if (MeisheMaterialApplicationKind.isCaptureOnly(applicationKind)) {
            listener.onStatusChanged("“" + label
                    + "” is capture-preview only and is not added to the editing timeline.");
        } else {
            listener.onStatusChanged("The package is installed, but its application type is unknown: " + packageType);
        }
    }

    public void updateAppliedMaterial(
            MeisheAppliedMaterial material,
            MeisheAppliedMaterial.Edits edits) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        project.replaceEditorState(MeisheEditorProjectStore.updateAppliedMaterial(
                project.editorState(),
                material,
                edits));
        project.reapplyEditorState();
        project.captureAndPersist();
        session.refreshPreview(session.currentPosition());
        listener.onStatusChanged("Updated “" + material.title + "” and refreshed the preview.");
    }

    public void deleteAppliedMaterial(MeisheAppliedMaterial material) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        project.replaceEditorState(MeisheEditorProjectStore.deleteAppliedMaterial(
                project.editorState(),
                material));
        project.reapplyEditorState();
        project.captureAndPersist();
        session.refreshPreview(Math.min(session.currentPosition(), session.duration()));
        listener.onStatusChanged("Removed “" + material.title + "” from the timeline.");
    }

    private void applyTheme(String packageId, String materialLabel) {
        if (!requireFeatureMutationPermission()) {
            return;
        }
        boolean applied = session.timeline() != null && session.timeline().applyTheme(packageId);
        if (applied) {
            project.replaceEditorState(MeisheEditorProjectStore.recordTheme(
                    project.editorState(),
                    packageId,
                    materialLabel));
            project.captureAndPersist();
        }
        session.refreshPreview(0);
        listener.onStatusChanged(applied
                ? "Applied “" + materialLabel + "” to the whole timeline."
                : "Theme application failed. Check its license and timeline content.");
    }

    public MeisheAudioController audioController() {
        return audioController;
    }

    private boolean requireFeatureMutationPermission() {
        if (session.canRebuildEditorFeatures()) {
            return true;
        }
        listener.onStatusChanged(
                "The host owns this timeline. Enable editor feature mutations in the host contract first.");
        return false;
    }

    private String inferApplicationKind(int packageType) {
        if (packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX) {
            return MeisheMaterialApplicationKind.FILTER;
        }
        if (packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE) {
            return MeisheMaterialApplicationKind.CAPTION_STYLE;
        }
        if (packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER) {
            return MeisheMaterialApplicationKind.CUSTOM_STICKER;
        }
        if (packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION) {
            return MeisheMaterialApplicationKind.TRANSITION;
        }
        if (packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME) {
            return MeisheMaterialApplicationKind.THEME;
        }
        if (packageType == MeisheLocalMaterialCatalog.RESOURCE_TYPE_FONT) {
            return MeisheMaterialApplicationKind.FONT;
        }
        return "";
    }

    private String emptyToNull(String value) {
        return value == null || value.isEmpty() ? null : value;
    }
}
