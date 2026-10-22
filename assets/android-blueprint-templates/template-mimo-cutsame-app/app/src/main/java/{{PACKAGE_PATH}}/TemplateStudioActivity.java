package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.ClipData;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.os.Looper;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.RadioGroup;
import android.widget.TextView;

import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsAudioResolution;
import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsMediaFileConvertor;
import com.meicam.sdk.NvsRational;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoResolution;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TemplateStudioActivity extends Activity {
    private static final int REQUEST_TEMPLATE = 4301;
    private static final int REQUEST_TEMPLATE_LICENSE = 4302;
    private static final int REQUEST_FOOTAGE = 4303;

    private final ArrayList<String> footagePaths = new ArrayList<>();
    private final ArrayList<String> pendingReverseIds = new ArrayList<>();
    private final Map<String, String> mediaByFootageId = new HashMap<>();
    private final Map<String, String> reverseMediaByFootageId = new HashMap<>();
    private final MeisheTemplateWorkflowController templateController =
            new MeisheTemplateWorkflowController();
    private MeisheTemplateReverseController reverseController;
    private final MeisheMimoWorkflowController mimoController =
            new MeisheMimoWorkflowController();

    private TextView statusText;
    private EditText captionText;
    private RadioGroup workflowMode;
    private NvsLiveWindow liveWindow;
    private NvsStreamingContext streamingContext;
    private List<NvsAssetPackageManager.NvsTemplateFootageDesc> footageDescriptors =
            Collections.emptyList();
    private String templatePath;
    private String templateLicensePath;
    private String templateId;
    private boolean templateInstallPending;
    private MeisheMimoWorkflowController.ExtractedMimoPackage extractedMimoPackage;
    private MeisheMimoWorkflowController.MimoSpec mimoSpec;
    private String currentReverseId;
    private long reverseTaskId = -1;
    private NvsTimeline timeline;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_template_studio);
        MeisheAppSupport.applySystemBarInsets(this);
        statusText = findViewById(R.id.statusText);
        captionText = findViewById(R.id.captionText);
        workflowMode = findViewById(R.id.workflowMode);
        FrameLayout liveWindowContainer = findViewById(R.id.liveWindowContainer);

        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        if (!sdkManager.initialize()) {
            statusText.setText("SDK initialization failed");
            setWorkflowEnabled(false);
            return;
        }
        streamingContext = NvsStreamingContext.getInstance();
        reverseController = new MeisheTemplateReverseController();
        liveWindow = new NvsLiveWindow(this);
        liveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);
        liveWindowContainer.addView(
                liveWindow,
                new FrameLayout.LayoutParams(
                        FrameLayout.LayoutParams.MATCH_PARENT,
                        FrameLayout.LayoutParams.MATCH_PARENT));
        registerCompileCallbacks();
        reverseController.registerCallback(createReverseCallback(), new Handler(Looper.getMainLooper()));
        setWorkflowEnabled(true);
        statusText.setText("SDK ready");

        findViewById(R.id.templateButton).setOnClickListener(
                view -> selectFiles(REQUEST_TEMPLATE, "*/*", false));
        findViewById(R.id.licenseButton).setOnClickListener(
                view -> selectFiles(REQUEST_TEMPLATE_LICENSE, "*/*", false));
        findViewById(R.id.footageButton).setOnClickListener(
                view -> selectFiles(REQUEST_FOOTAGE, "*/*", true));
        findViewById(R.id.buildButton).setOnClickListener(view -> prepareTemplateTimeline());
        findViewById(R.id.playButton).setOnClickListener(view -> playTemplate());
        findViewById(R.id.captionButton).setOnClickListener(view -> replaceFirstTemplateCaption());
        findViewById(R.id.exportButton).setOnClickListener(view -> exportTemplate());
        findViewById(R.id.materialButton).setOnClickListener(view ->
                startActivity(MeisheAssetCenterActivity.createIntent(this)));
        workflowMode.setOnCheckedChangeListener((group, checkedId) -> {
            boolean mimoMode = checkedId == R.id.modeMimo;
            findViewById(R.id.licenseButton).setEnabled(!mimoMode);
            statusText.setText(mimoMode
                    ? "Select a Mimo ZIP and at least one footage file"
                    : "Select an SDK .template package and its footage");
        });
    }

    private void setWorkflowEnabled(boolean enabled) {
        int[] ids = {
                R.id.templateButton,
                R.id.licenseButton,
                R.id.footageButton,
                R.id.buildButton,
                R.id.playButton,
                R.id.captionButton,
                R.id.exportButton,
                R.id.materialButton
        };
        for (int id : ids) {
            findViewById(id).setEnabled(enabled);
        }
    }

    private void selectFiles(int requestCode, String type, boolean allowMultiple) {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.setType(type);
        if (allowMultiple) {
            intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
            intent.putExtra(Intent.EXTRA_MIME_TYPES, new String[]{"video/*", "image/*", "audio/*"});
        }
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        startActivityForResult(intent, requestCode);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode != RESULT_OK || data == null) {
            return;
        }
        ArrayList<Uri> uris = selectedUris(data);
        if (uris.isEmpty()) {
            return;
        }
        try {
            if (requestCode == REQUEST_TEMPLATE) {
                templatePath = MeisheMediaFiles.copyContentUriToCache(this, uris.get(0));
                templateId = null;
                if (isMimoMode()) {
                    prepareMimoArchive();
                } else {
                    beginTemplatePackageInstall();
                }
            } else if (requestCode == REQUEST_TEMPLATE_LICENSE) {
                templateLicensePath = MeisheMediaFiles.copyContentUriToCache(this, uris.get(0));
                templateId = null;
                beginTemplatePackageInstall();
            } else if (requestCode == REQUEST_FOOTAGE) {
                footagePaths.clear();
                for (Uri uri : uris) {
                    footagePaths.add(MeisheMediaFiles.copyContentUriToCache(this, uri));
                }
                statusText.setText("Selected footage: " + footagePaths.size());
            }
        } catch (IOException error) {
            statusText.setText("Resource copy failed: " + error.getMessage());
        }
    }

    private ArrayList<Uri> selectedUris(Intent data) {
        ArrayList<Uri> uris = new ArrayList<>();
        ClipData clipData = data.getClipData();
        if (clipData != null) {
            for (int index = 0; index < clipData.getItemCount(); index++) {
                Uri uri = clipData.getItemAt(index).getUri();
                if (uri != null) {
                    uris.add(uri);
                }
            }
        } else if (data.getData() != null) {
            uris.add(data.getData());
        }
        return uris;
    }

    private boolean beginTemplatePackageInstall() {
        if (streamingContext == null || templatePath == null) {
            return false;
        }
        if (templateInstallPending) {
            statusText.setText("Template installation is still running");
            return false;
        }
        templateInstallPending = true;
        MeisheAssetInstaller installer = new MeisheAssetInstaller(streamingContext);
        int code = installer.installAsynchronously(
                templatePath,
                templateLicensePath,
                NvsAssetPackageManager.ASSET_PACKAGE_TYPE_TEMPLATE,
                result -> runOnUiThread(() -> finishTemplatePackageInstall(result)));
        if (code != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
                && code != NvsAssetPackageManager
                .ASSET_PACKAGE_MANAGER_ERROR_WORKING_INPROGRESS
                && code != NvsAssetPackageManager
                .ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
            templateInstallPending = false;
            statusText.setText("Template install could not start: " + code);
            return false;
        }
        if (templateInstallPending) {
            statusText.setText("Template installation started: " + code);
        }
        return true;
    }

    private void finishTemplatePackageInstall(MeisheAssetInstaller.InstallResult result) {
        templateInstallPending = false;
        if (result == null || !result.isSuccess()
                || result.packageId == null || result.packageId.isEmpty()) {
            templateId = null;
            statusText.setText("Template install failed; error="
                    + (result == null ? "missing callback" : result.errorCode));
            return;
        }
        templateId = result.packageId;
        footageDescriptors = templateController.getTemplateFootages(streamingContext, templateId);
        int requiredCount = templateController.listReplaceableFootageIds(footageDescriptors).size();
        statusText.setText("Template ready. Required footage: " + requiredCount);
    }

    private void prepareMimoArchive() {
        extractedMimoPackage = null;
        mimoSpec = null;
        File extractionDirectory = new File(
                getCacheDir(),
                "mimo-" + System.currentTimeMillis());
        try (FileInputStream input = new FileInputStream(templatePath)) {
            extractedMimoPackage = mimoController.extractArchive(input, extractionDirectory);
            try (FileInputStream infoInput = new FileInputStream(extractedMimoPackage.infoFile)) {
                mimoSpec = mimoController.parse(infoInput);
            }
            MeisheMimoWorkflowController.AssetInstallResult installResult =
                    mimoController.installExtractedChildPackages(
                            streamingContext,
                            extractedMimoPackage.rootDirectory);
            if (!installResult.failures.isEmpty()) {
                statusText.setText("Mimo child package install failed: "
                        + installResult.failures.get(0));
                return;
            }
            statusText.setText("Mimo ready. Shots: " + mimoSpec.shots.size()
                    + ", child packages: " + installResult.installed);
        } catch (Exception error) {
            extractedMimoPackage = null;
            mimoSpec = null;
            statusText.setText("Mimo archive preparation failed: " + error.getMessage());
        }
    }

    private void prepareTemplateTimeline() {
        if (isMimoMode()) {
            createMimoTimeline();
            return;
        }
        if (templateId == null || templateId.isEmpty()) {
            beginTemplatePackageInstall();
            return;
        }
        List<String> footageIds = templateController.listReplaceableFootageIds(footageDescriptors);
        if (footageIds.isEmpty()) {
            statusText.setText("Template has no replaceable footage descriptors");
            return;
        }
        if (footagePaths.isEmpty()) {
            statusText.setText("Select at least one footage file");
            return;
        }
        mediaByFootageId.clear();
        reverseMediaByFootageId.clear();
        for (int index = 0; index < footageIds.size(); index++) {
            mediaByFootageId.put(
                    footageIds.get(index),
                    footagePaths.get(index % footagePaths.size()));
        }
        pendingReverseIds.clear();
        pendingReverseIds.addAll(templateController.listReverseFootageIds(footageDescriptors));
        if (pendingReverseIds.isEmpty()) {
            createTemplateTimeline();
        } else {
            statusText.setText("Generating reverse footage: " + pendingReverseIds.size());
            generateNextReverse();
        }
    }

    private void generateNextReverse() {
        if (pendingReverseIds.isEmpty()) {
            currentReverseId = null;
            reverseTaskId = -1;
            createTemplateTimeline();
            return;
        }
        currentReverseId = pendingReverseIds.get(0);
        String sourcePath = mediaByFootageId.get(currentReverseId);
        MeisheMediaProbeController.MediaProbe probe =
                new MeisheMediaProbeController(streamingContext).probe(sourcePath);
        if (probe == null || probe.durationUs <= 0) {
            statusText.setText("Cannot read reverse footage: " + currentReverseId);
            return;
        }
        File outputDirectory = new File(getCacheDir(), "template-reverse");
        File outputFile = new File(
                outputDirectory,
                currentReverseId.replaceAll("[^A-Za-z0-9._-]", "_") + ".mp4");
        reverseTaskId = reverseController.generateReverseMedia(
                sourcePath,
                outputFile.getAbsolutePath(),
                0,
                probe.durationUs,
                1080);
        if (reverseTaskId < 0) {
            statusText.setText("Reverse conversion could not start: " + currentReverseId);
        }
    }

    private NvsMediaFileConvertor.MeidaFileConvertorCallback createReverseCallback() {
        return new NvsMediaFileConvertor.MeidaFileConvertorCallback() {
            @Override
            public void onProgress(long taskId, float progress) {
                if (taskId == reverseTaskId) {
                    statusText.setText("Reverse footage: " + Math.round(progress * 100f) + "%");
                }
            }

            @Override
            public void onFinish(long taskId, String sourcePath, String outputPath, int errorCode) {
                if (taskId != reverseTaskId || currentReverseId == null) {
                    return;
                }
                if (errorCode != NvsMediaFileConvertor.CONVERTOR_ERROR_CODE_NO_ERROR
                        || outputPath == null || !new File(outputPath).isFile()) {
                    statusText.setText("Reverse conversion failed: " + errorCode);
                    return;
                }
                reverseMediaByFootageId.put(currentReverseId, outputPath);
                pendingReverseIds.remove(0);
                generateNextReverse();
            }

            @Override
            public void notifyAudioMuteRage(long taskId, long startTime, long endTime) {
            }
        };
    }

    private void createTemplateTimeline() {
        List<String> failures = templateController.validateFootageSelections(
                footageDescriptors,
                mediaByFootageId,
                reverseMediaByFootageId);
        if (!failures.isEmpty()) {
            statusText.setText(failures.get(0));
            return;
        }
        List<NvsStreamingContext.templateFootageInfo> footage =
                templateController.buildTemplateFootage(
                        footageDescriptors,
                        mediaByFootageId,
                        reverseMediaByFootageId);
        if (footage.isEmpty()) {
            statusText.setText("Template footage mapping failed");
            return;
        }
        NvsTimeline createdTimeline;
        int checkedMode = workflowMode.getCheckedRadioButtonId();
        if (checkedMode == R.id.modeCutSame) {
            createdTimeline = templateController.createCutSameTimeline(
                    streamingContext, templateId, footage, 0);
        } else {
            createdTimeline = templateController.createTemplateEditorTimeline(
                    streamingContext, templateId, footage);
        }
        if (createdTimeline == null) {
            statusText.setText("Template timeline creation failed");
            return;
        }
        if (timeline != null) {
            streamingContext.stop();
            streamingContext.removeTimeline(timeline);
        }
        timeline = createdTimeline;
        boolean connected = templateController.reconnectTemplatePreview(
                streamingContext, timeline, liveWindow, 0, 0);
        statusText.setText(connected
                ? "Template ready: " + timeline.getDuration() / 1_000_000f + "s"
                : "Timeline created, preview connection failed");
    }

    private void createMimoTimeline() {
        if (mimoSpec == null || extractedMimoPackage == null) {
            statusText.setText("Select and prepare a Mimo ZIP first");
            return;
        }
        if (footagePaths.isEmpty()) {
            statusText.setText("Select at least one Mimo footage file");
            return;
        }
        NvsVideoResolution videoResolution = new NvsVideoResolution();
        boolean portrait = mimoSpec.supportedAspectRatio.toLowerCase().contains("9v16");
        videoResolution.imageWidth = portrait ? 720 : 1280;
        videoResolution.imageHeight = portrait ? 1280 : 720;
        videoResolution.imagePAR = new NvsRational(1, 1);
        NvsAudioResolution audioResolution = new NvsAudioResolution();
        audioResolution.sampleRate = 44100;
        audioResolution.channelCount = 2;
        File musicFile = mimoController.findExtractedFile(
                extractedMimoPackage.rootDirectory,
                mimoSpec.musicFileName);
        MeisheMimoWorkflowController.BuildResult result = mimoController.buildTimeline(
                streamingContext,
                mimoSpec,
                footagePaths,
                musicFile == null ? null : musicFile.getAbsolutePath(),
                videoResolution,
                new NvsRational(30, 1),
                audioResolution);
        if (result.timeline == null) {
            statusText.setText(result.failures.isEmpty()
                    ? "Mimo timeline creation failed"
                    : result.failures.get(0));
            return;
        }
        replaceTimeline(result.timeline);
        boolean connected = mimoController.reconnectPreview(
                streamingContext,
                timeline,
                liveWindow,
                0,
                0);
        statusText.setText(connected
                ? "Mimo ready: " + result.clipCount + " clips, "
                + result.appliedEffectCount + " effects, "
                + result.compoundCaptionCount + " captions"
                : "Mimo Timeline created, preview connection failed");
    }

    private void replaceTimeline(NvsTimeline replacement) {
        if (timeline != null) {
            streamingContext.stop();
            streamingContext.removeTimeline(timeline);
        }
        timeline = replacement;
    }

    private boolean isMimoMode() {
        return workflowMode.getCheckedRadioButtonId() == R.id.modeMimo;
    }

    private void playTemplate() {
        if (timeline == null) {
            statusText.setText("Create a template timeline first");
            return;
        }
        if (!templateController.playTemplate(
                streamingContext, timeline, 0, timeline.getDuration(), 0)) {
            statusText.setText("Template playback failed to start");
        }
    }

    private void replaceFirstTemplateCaption() {
        if (isMimoMode()) {
            statusText.setText("Mimo caption content is defined by its info.json workflow");
            return;
        }
        if (timeline == null || templateId == null) {
            statusText.setText("Create a template timeline first");
            return;
        }
        String replacement = captionText.getText().toString();
        if (replacement.isEmpty()) {
            return;
        }
        String replaceId = firstCaptionReplaceId(
                templateController.getTemplateCaptions(streamingContext, templateId));
        int replaced;
        if (replaceId != null) {
            Map<String, String> replacements = new HashMap<>();
            replacements.put(replaceId, replacement);
            replaced = templateController.replaceTemplateCaptionTexts(timeline, replacements);
        } else {
            String compoundReplaceId = firstCompoundCaptionReplaceId(
                    templateController.getTemplateCompoundCaptions(
                            streamingContext,
                            templateId));
            if (compoundReplaceId == null) {
                statusText.setText("Template has no replaceable caption");
                return;
            }
            Map<String, List<String>> replacements = new HashMap<>();
            replacements.put(compoundReplaceId, Collections.singletonList(replacement));
            replaced = templateController.replaceTemplateCompoundCaptionTexts(
                    timeline,
                    replacements);
        }
        long position = templateController.currentTemplatePosition(streamingContext, timeline);
        templateController.reconnectTemplatePreview(
                streamingContext, timeline, liveWindow, position, 0);
        statusText.setText("Caption replacements: " + replaced);
    }

    private String firstCaptionReplaceId(
            List<NvsAssetPackageManager.NvsTemplateCaptionDesc> descriptors) {
        ArrayDeque<NvsAssetPackageManager.NvsTemplateCaptionDesc> pending =
                new ArrayDeque<>(descriptors == null ? Collections.emptyList() : descriptors);
        while (!pending.isEmpty()) {
            NvsAssetPackageManager.NvsTemplateCaptionDesc descriptor = pending.removeFirst();
            if (descriptor == null) {
                continue;
            }
            if (descriptor.subCaptions != null) {
                pending.addAll(descriptor.subCaptions);
            }
            if (descriptor.replaceId != null && !descriptor.replaceId.isEmpty()) {
                return descriptor.replaceId;
            }
        }
        return null;
    }

    private String firstCompoundCaptionReplaceId(
            List<NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc> descriptors) {
        ArrayDeque<NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc> pending =
                new ArrayDeque<>(descriptors == null ? Collections.emptyList() : descriptors);
        while (!pending.isEmpty()) {
            NvsAssetPackageManager.NvsTemplateCompoundCaptionDesc descriptor =
                    pending.removeFirst();
            if (descriptor == null) {
                continue;
            }
            if (descriptor.subCaptions != null) {
                pending.addAll(descriptor.subCaptions);
            }
            if (descriptor.replaceId != null && !descriptor.replaceId.isEmpty()) {
                return descriptor.replaceId;
            }
        }
        return null;
    }

    private void exportTemplate() {
        if (timeline == null) {
            statusText.setText("Create a template timeline first");
            return;
        }
        File directory = getExternalFilesDir(Environment.DIRECTORY_MOVIES);
        if (directory == null) {
            directory = getFilesDir();
        }
        File output = new File(directory, "template-output-" + System.currentTimeMillis() + ".mp4");
        boolean started = templateController.exportTemplate(
                streamingContext,
                timeline,
                0,
                timeline.getDuration(),
                output.getAbsolutePath(),
                NvsStreamingContext.COMPILE_VIDEO_RESOLUTION_GRADE_CUSTOM,
                NvsStreamingContext.COMPILE_BITRATE_GRADE_HIGH,
                null,
                0);
        statusText.setText(started ? "Export started: " + output.getName() : "Export failed to start");
    }

    private void registerCompileCallbacks() {
        templateController.registerTemplateCompileCallbacks(
                streamingContext,
                new NvsStreamingContext.CompileCallback() {
                    @Override
                    public void onCompileProgress(NvsTimeline compileTimeline, int progress) {
                        if (compileTimeline == timeline) {
                            statusText.setText("Export progress: " + progress + "%");
                        }
                    }

                    @Override
                    public void onCompileFinished(NvsTimeline compileTimeline) {
                        if (compileTimeline == timeline) {
                            statusText.setText("Export finished");
                        }
                    }

                    @Override
                    public void onCompileFailed(NvsTimeline compileTimeline) {
                        if (compileTimeline == timeline) {
                            statusText.setText("Export failed");
                        }
                    }
                },
                new NvsStreamingContext.CompileCallback2() {
                    @Override
                    public void onCompileCompleted(
                            NvsTimeline compileTimeline,
                            boolean isCanceled) {
                        if (compileTimeline == timeline && isCanceled) {
                            statusText.setText("Export canceled");
                        }
                    }
                });
    }

    @Override
    protected void onDestroy() {
        if (reverseController != null && reverseTaskId >= 0) {
            reverseController.cancel(reverseTaskId);
        }
        if (reverseController != null) {
            reverseController.release();
        }
        if (streamingContext != null) {
            streamingContext.stop();
            if (timeline != null) {
                streamingContext.removeTimeline(timeline);
            }
        }
        super.onDestroy();
    }
}
