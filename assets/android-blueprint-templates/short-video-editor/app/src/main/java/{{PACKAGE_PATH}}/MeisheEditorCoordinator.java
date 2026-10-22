package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public final class MeisheEditorCoordinator implements
        MeisheEditorSessionController.Listener,
        MeisheEditorCommandController.Listener,
        MeisheEditorOverlayController.Listener,
        MeisheVoiceoverController.Listener,
        MeisheEditorMediaController.Listener,
        MeisheEditorUiBindings.Listener {
    public static final int REQUEST_MATERIAL = 61;
    public static final int REQUEST_RECORD_AUDIO = 62;
    public static final int REQUEST_ADD_MEDIA = 63;
    public static final int REQUEST_STICKER_IMAGE = 64;

    private static final String STATE_POSITION_US = "meishe.positionUs";

    private final Activity activity;
    private final ArrayList<String> mediaPaths;
    private final int projectWidth;
    private final int projectHeight;
    private final String projectId;
    private final boolean resumeProject;
    private final MeisheEditorHostContract hostContract;
    private MeisheEditorUiBindings ui;
    private MeisheEditorSessionController session;
    private MeisheEditorProjectController project;
    private MeisheEditorCommandController commands;
    private MeisheEditorOverlayController overlays;
    private MeisheVoiceoverController voiceover;
    private MeisheEditorMediaController mediaController;
    private boolean initialized;
    private PendingMaterial pendingMaterial;

    public MeisheEditorCoordinator(
            Activity activity,
            ArrayList<String> mediaPaths,
            int projectWidth,
            int projectHeight,
            String projectId,
            boolean resumeProject) {
        this(
                activity,
                mediaPaths,
                projectWidth,
                projectHeight,
                projectId,
                resumeProject,
                null);
    }

    public MeisheEditorCoordinator(
            Activity activity,
            ArrayList<String> mediaPaths,
            int projectWidth,
            int projectHeight,
            String projectId,
            boolean resumeProject,
            MeisheEditorHostContract hostContract) {
        if (activity == null || projectId == null || projectId.isEmpty()) {
            throw new IllegalArgumentException("activity and project id are required");
        }
        this.activity = activity;
        this.mediaPaths = mediaPaths == null ? new ArrayList<>() : new ArrayList<>(mediaPaths);
        this.projectWidth = projectWidth;
        this.projectHeight = projectHeight;
        this.projectId = projectId;
        this.resumeProject = resumeProject;
        this.hostContract = hostContract;
    }

    public void onCreate(Bundle savedInstanceState) {
        activity.setContentView(R.layout.activity_meishe_editor);
        MeisheAppSupport.applySystemBarInsets(activity);
        ui = new MeisheEditorUiBindings(activity, this);
        ui.bind();
        ui.configurePreviewAspectRatio(projectWidth, projectHeight);
        session = new MeisheEditorSessionController(activity, this, hostContract);
        project = new MeisheEditorProjectController(
                activity,
                projectId,
                projectWidth,
                projectHeight,
                session);

        boolean restoreProject = resumeProject || savedInstanceState != null;
        String serializedProject = project.loadSerializedProject(restoreProject);
        if (!session.open(
                ui.liveWindowContainer(),
                mediaPaths,
                projectWidth,
                projectHeight,
                serializedProject,
                restoreProject)) {
            ui.setControlsEnabled(false);
            return;
        }

        int restoredFeatureCount = project.restoreEditorFeatures(restoreProject);
        overlays = new MeisheEditorOverlayController(session, project, this);
        commands = new MeisheEditorCommandController(session, project, this);
        voiceover = new MeisheVoiceoverController(
                activity,
                REQUEST_RECORD_AUDIO,
                session,
                project,
                overlays.audioController(),
                this);
        mediaController = new MeisheEditorMediaController(
                activity,
                session,
                project,
                this);
        commands.restoreInstanceState(savedInstanceState);
        long positionUs = savedInstanceState == null
                ? 0
                : savedInstanceState.getLong(STATE_POSITION_US, 0);
        session.refreshPreview(positionUs);
        project.persist();
        initialized = true;
        refreshTimelineUi();
        ui.updateTimelinePosition(positionUs, session.duration());
        ui.setStatus(
                "Timeline ready: " + session.videoTrack().getClipCount()
                        + " clips, " + restoredFeatureCount
                        + " editor items restored. Every edit refreshes the preview.");
    }

    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (!initialized) {
            return;
        }
        if (requestCode == REQUEST_STICKER_IMAGE) {
            if (resultCode != Activity.RESULT_OK || data == null || data.getData() == null) {
                pendingMaterial = null;
                ui.setStatus("No sticker image was selected. The material was not added.");
                return;
            }
            applySelectedStickerImage(data.getData());
            return;
        }
        if (resultCode != Activity.RESULT_OK || data == null) {
            return;
        }
        if (requestCode == REQUEST_MATERIAL) {
            handleMaterialResult(data);
        } else if (requestCode == REQUEST_ADD_MEDIA) {
            mediaController.importResult(data);
        }
    }

    public void onRequestPermissionsResult(int requestCode, int[] grantResults) {
        if (voiceover != null) {
            voiceover.onPermissionResult(requestCode, grantResults);
        }
    }

    public void onSaveInstanceState(Bundle outState) {
        if (!initialized) {
            return;
        }
        project.persist();
        commands.saveInstanceState(outState);
    }

    public void onPause() {
        if (!initialized) {
            return;
        }
        voiceover.onPause();
        session.stopPlayback();
        project.persist();
    }

    public void onDestroy() {
        if (voiceover != null) {
            voiceover.release();
        }
        if (mediaController != null) {
            mediaController.release();
        }
        if (project != null && session != null && session.timeline() != null) {
            project.persist();
        }
        if (session != null) {
            session.close();
        }
        initialized = false;
    }

    @Override
    public void onPlaybackStateChanged(boolean playing) {
        if (ui != null) {
            ui.setPlaying(playing);
        }
    }

    @Override
    public void onTimelinePositionChanged(long positionUs, long durationUs) {
        if (ui != null) {
            ui.updateTimelinePosition(positionUs, durationUs);
            ui.setSelectedTimelineClip(session.clipIndexAt(positionUs));
        }
    }

    @Override
    public void onRecordingStateChanged(boolean recording) {
        if (ui != null) {
            ui.setRecording(recording);
        }
    }

    @Override
    public void onStatusChanged(String message) {
        if (ui != null) {
            ui.setStatus(message);
            refreshTimelineUi();
        }
    }

    @Override
    public void onTogglePlayback() {
        if (initialized) {
            session.togglePlayback();
        }
    }

    @Override
    public void onSeekProgress(int progress, int max) {
        if (initialized) {
            session.seekToProgress(progress, max);
        }
    }

    @Override
    public void onSeekStarted() {
        if (initialized) {
            session.beginSeeking();
        }
    }

    @Override
    public void onSeekFinished() {
        if (initialized) {
            session.endSeeking();
        }
    }

    @Override
    public void onSplitClip() {
        commands.splitAtPlayhead();
        refreshTimelineUi();
    }

    @Override
    public void onSelectClip() {
        commands.selectAtPlayhead();
        refreshTimelineUi();
    }

    @Override
    public void onTrimClip(int retainedPercent) {
        commands.trimSelectedToPercent(retainedPercent);
        refreshTimelineUi();
    }

    @Override
    public void onDeleteClip() {
        commands.deleteSelected();
        refreshTimelineUi();
    }

    @Override
    public void onMoveClip() {
        commands.moveSelectedRight();
        refreshTimelineUi();
    }

    @Override
    public void onUndo() {
        commands.undo();
        refreshTimelineUi();
    }

    @Override
    public void onRedo() {
        commands.redo();
        refreshTimelineUi();
    }

    public void applyInitialMaterial(
            String packageId,
            int packageType,
            String localAssetPath,
            String applicationKind,
            String materialLabel) {
        if (initialized && packageId != null && !packageId.isEmpty()) {
            pendingMaterial = new PendingMaterial(
                    packageId,
                    packageType,
                    localAssetPath,
                    applicationKind,
                    materialLabel);
            continuePendingMaterial();
        }
    }

    @Override
    public void onAddMedia() {
        if (initialized) {
            activity.startActivityForResult(
                    mediaController.createPickerIntent(),
                    REQUEST_ADD_MEDIA);
        }
    }

    @Override
    public void onSelectClipIndex(int clipIndex) {
        if (!initialized) {
            return;
        }
        commands.selectClip(clipIndex);
        refreshTimelineUi();
    }

    @Override
    public void onApplyFilter() {
        overlays.applyDefaultFilter(Math.max(0, commands.selectedClipIndex()));
    }

    @Override
    public void onAddCaption(String text) {
        overlays.addCaption(text);
    }

    @Override
    public void onApplySticker() {
        overlays.applyDefaultSticker();
    }

    @Override
    public void onApplyTransition() {
        overlays.applyDefaultTransition(Math.max(0, commands.selectedClipIndex()));
    }

    @Override
    public void onApplyMusic() {
        overlays.applyBundledMusic();
    }

    @Override
    public void onToggleVoiceover() {
        voiceover.toggle();
    }

    @Override
    public void onPreviewVoiceover() {
        voiceover.previewLatest();
    }

    @Override
    public void onDeleteVoiceover() {
        voiceover.deleteLatest();
    }

    @Override
    public void onOpenMaterialCenter(int packageType) {
        Intent intent = MeisheAssetCenterActivity.createPickerIntent(activity);
        if (packageType >= 0) {
            intent.putExtra(MeisheAssetCenterConfig.EXTRA_ASSET_TYPE, packageType);
        }
        activity.startActivityForResult(intent, REQUEST_MATERIAL);
    }

    @Override
    public void onMaterialTextProvided(String text) {
        if (pendingMaterial == null) {
            return;
        }
        if (text == null || text.trim().isEmpty()) {
            ui.setStatus("Caption text cannot be empty. The material was not added.");
            return;
        }
        applyPendingMaterial(text, null);
    }

    @Override
    public void onUseSampleStickerImage() {
        if (pendingMaterial != null) {
            applyPendingMaterial(null, MeisheSampleAssets.SAMPLE_STICKER_IMAGE_PATH);
        }
    }

    @Override
    public void onChooseStickerImage() {
        if (pendingMaterial == null) {
            return;
        }
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("image/*");
        activity.startActivityForResult(intent, REQUEST_STICKER_IMAGE);
    }

    @Override
    public void onUpdateAppliedMaterial(
            MeisheAppliedMaterial material,
            MeisheAppliedMaterial.Edits edits) {
        overlays.updateAppliedMaterial(material, edits);
    }

    @Override
    public void onDeleteAppliedMaterial(MeisheAppliedMaterial material) {
        overlays.deleteAppliedMaterial(material);
    }

    @Override
    public void onExport() {
        File outputDir = activity.getExternalFilesDir(Environment.DIRECTORY_MOVIES);
        if (outputDir == null) {
            ui.setStatus("Movie output directory is unavailable.");
            return;
        }
        File output = new File(
                outputDir,
                "meishe_export_" + System.currentTimeMillis() + ".mp4");
        boolean started = session.exportTo(output);
        ui.setStatus(started
                ? "Export started: " + output.getName()
                : "Export could not start.");
    }

    @Override
    public void onMediaImportStarted(int mediaCount) {
        ui.setStatus("Importing " + mediaCount + " media items into the current timeline...");
        ui.setControlsEnabled(false);
    }

    @Override
    public void onMediaImportFinished(int appendedCount, int rejectedCount) {
        ui.setControlsEnabled(true);
        refreshTimelineUi();
        ui.setStatus(
                "Added " + appendedCount + " media items to the video track; "
                        + rejectedCount + " failed validation.");
    }

    private void refreshTimelineUi() {
        if (ui == null || session == null || session.timeline() == null) {
            return;
        }
        int selectedClipIndex = commands == null
                ? session.clipIndexAt(session.currentPosition())
                : commands.selectedClipIndex();
        if (selectedClipIndex < 0) {
            selectedClipIndex = session.clipIndexAt(session.currentPosition());
        }
        ArrayList<MeisheEditorClipUiModel> videoClips = new ArrayList<>(session.clipUiModels());
        ui.renderTimeline(videoClips, selectedClipIndex);
        ui.setTimelineEmpty(videoClips.isEmpty());
        ui.renderVoiceoverTrack(session.audioClipUiModels(1));
        ui.renderAppliedMaterials(MeisheEditorProjectStore.listAppliedMaterials(
                project == null ? null : project.editorState()));
        ui.updateTimelinePosition(session.currentPosition(), session.duration());
    }

    private void handleMaterialResult(Intent data) {
        pendingMaterial = new PendingMaterial(
                data.getStringExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_ID),
                data.getIntExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_TYPE, -1),
                data.getStringExtra(MeisheAssetCenterConfig.EXTRA_LOCAL_ASSET_PATH),
                data.getStringExtra(MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND),
                data.getStringExtra(MeisheAssetCenterConfig.EXTRA_MATERIAL_LABEL));
        continuePendingMaterial();
    }

    private void continuePendingMaterial() {
        if (pendingMaterial == null || pendingMaterial.packageId == null
                || pendingMaterial.packageId.isEmpty()) {
            pendingMaterial = null;
            ui.setStatus("The material installation result is incomplete and cannot be added.");
            return;
        }
        if (MeisheMaterialApplicationKind.requiresCaptionText(
                pendingMaterial.applicationKind)) {
            ui.requestMaterialText(
                    pendingMaterial.materialLabel,
                    MeisheMaterialApplicationKind.COMPOUND_CAPTION.equals(
                            pendingMaterial.applicationKind));
        } else if (MeisheMaterialApplicationKind.requiresCustomImage(
                pendingMaterial.applicationKind)) {
            ui.requestCustomStickerImage(pendingMaterial.materialLabel);
        } else {
            applyPendingMaterial(null, null);
        }
    }

    private void applySelectedStickerImage(Uri imageUri) {
        try {
            String imagePath = MeisheMediaFiles.copyContentUriToCache(activity, imageUri);
            applyPendingMaterial(null, imagePath);
        } catch (IOException exception) {
            pendingMaterial = null;
            ui.setStatus("The selected sticker image could not be read: " + exception.getMessage());
        }
    }

    private void applyPendingMaterial(String userText, String customImagePath) {
        PendingMaterial material = pendingMaterial;
        pendingMaterial = null;
        if (material == null) {
            return;
        }
        int selectedClipIndex = commands == null ? 0 : commands.selectedClipIndex();
        overlays.applyInstalledMaterial(
                material.packageId,
                material.packageType,
                material.localAssetPath,
                material.applicationKind,
                material.materialLabel,
                userText,
                customImagePath,
                Math.max(0, selectedClipIndex));
    }

    private static final class PendingMaterial {
        final String packageId;
        final int packageType;
        final String localAssetPath;
        final String applicationKind;
        final String materialLabel;

        PendingMaterial(
                String packageId,
                int packageType,
                String localAssetPath,
                String applicationKind,
                String materialLabel) {
            this.packageId = packageId;
            this.packageType = packageType;
            this.localAssetPath = localAssetPath;
            this.applicationKind = applicationKind == null ? "" : applicationKind;
            this.materialLabel = materialLabel == null || materialLabel.isEmpty()
                    ? "Materials"
                    : materialLabel;
        }
    }
}
