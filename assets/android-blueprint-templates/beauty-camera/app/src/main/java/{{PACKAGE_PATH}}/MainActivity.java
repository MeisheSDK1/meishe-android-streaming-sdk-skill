package {{PACKAGE_NAME}};

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.RectF;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.view.MotionEvent;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;
import android.view.ViewGroup;

import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsCaptureVideoFx;
import com.meicam.sdk.NvsColor;
import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsStreamingContext;

import java.io.File;
import java.io.IOException;
import java.util.Locale;
import java.util.Map;

public class MainActivity extends Activity {
    private static final int REQUEST_CAPTURE_PERMISSIONS = 41;
    private static final int REQUEST_MATERIAL = 42;
    private static final String[] CAPTURE_PERMISSIONS = {
            Manifest.permission.CAMERA,
            Manifest.permission.RECORD_AUDIO
    };

    private MeisheSdkManager sdkManager;
    private MeisheCaptureController captureController;
    private MeisheBeautyArController beautyController;
    private NvsLiveWindow liveWindow;
    private NvsCaptureVideoFx beautyFx;
    private NvsCaptureVideoFx sampleFilterFx;
    private NvsCaptureVideoFx downloadedPackageFx;
    private NvsCaptureVideoFx arSceneFx;
    private NvsCaptureVideoFx segmentationFx;
    private Map<String, String> packageIds;
    private TextView statusText;
    private Button recordButton;
    private Button pauseRecordingButton;
    private Button flashButton;
    private Button focusButton;
    private SeekBar zoomSeekBar;
    private SeekBar exposureSeekBar;
    private int requestedCameraDeviceIndex = 1;
    private int activeCameraDeviceIndex = -1;
    private int selectedExposure;
    private int selectedZoom;
    private boolean flashEnabled;
    private boolean recording;
    private boolean recordingPaused;
    private boolean recordingFirstFrameReached;
    private boolean isPreviewStarted;
    private boolean permissionRequestInFlight;
    private String pendingResumeStatus;
    private boolean humanModelsReady;
    private File recordingOutput;
    private String activeCaptureSceneId = "";
    private String activeArSceneId = "";
    private String activeFaceMeshId = "";
    private String activeMakeupId = "";
    private String pendingMaterialPackageId;
    private int pendingMaterialPackageType = -1;
    private String pendingMaterialApplicationKind;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        MeisheAppSupport.applySystemBarInsets(this);

        statusText = findViewById(R.id.cameraStatusText);
        recordButton = findViewById(R.id.recordButton);
        pauseRecordingButton = findViewById(R.id.pauseRecordingButton);
        flashButton = findViewById(R.id.flashButton);
        focusButton = findViewById(R.id.focusButton);
        zoomSeekBar = findViewById(R.id.zoomSeekBar);
        exposureSeekBar = findViewById(R.id.exposureSeekBar);
        FrameLayout liveWindowContainer = findViewById(R.id.liveWindow);

        sdkManager = new MeisheSdkManager(getApplicationContext());
        if (!sdkManager.initialize()) {
            setStatus("SDK initialization failed. Check license and native libraries.");
            setControlsEnabled(false);
            return;
        }
        liveWindow = new NvsLiveWindow(this);
        liveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);
        liveWindowContainer.addView(
                liveWindow,
                new FrameLayout.LayoutParams(
                        ViewGroup.LayoutParams.MATCH_PARENT,
                        ViewGroup.LayoutParams.MATCH_PARENT));

        MeisheAssetInstaller assetInstaller = new MeisheAssetInstaller(sdkManager.getStreamingContext());
        packageIds = MeisheSampleAssets.installDefaultPackages(assetInstaller);
        captureController = new MeisheCaptureController(sdkManager.getStreamingContext(), liveWindow);
        beautyController = new MeisheBeautyArController(sdkManager.getStreamingContext());
        initializeOptionalFaceModels();
        bindBeautyControls();
        bindDeviceControls();
        bindActions();
        registerCaptureCallbacks();
        bindTouchFocus();
        setControlsEnabled(true);
        updateDeviceCapabilityUi();

        if (requestCapturePermissionsIfNeeded()) {
            startPreview();
        }
    }

    private void initializeOptionalFaceModels() {
        beautyController.initializeEffectSdkIfNeeded(this);
        try {
            String[] models = getAssets().list("facemode/ms");
            if (models != null && models.length > 0) {
                humanModelsReady = beautyController.initializeMsHumanDetectionModels(this, false, true);
            }
        } catch (IOException ignored) {
            humanModelsReady = false;
        }
    }

    private void bindBeautyControls() {
        SeekBar smoothSeekBar = findViewById(R.id.smoothSeekBar);
        SeekBar whiteningSeekBar = findViewById(R.id.whiteningSeekBar);
        SeekBar.OnSeekBarChangeListener listener = new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (!fromUser) {
                    return;
                }
                ensureBeautyFx();
                if (seekBar.getId() == R.id.smoothSeekBar) {
                    beautyController.setFloat(beautyFx, "Strength", progress / 100.0);
                } else {
                    beautyController.setFloat(beautyFx, "Whitening", progress / 100.0);
                }
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
            }
        };
        smoothSeekBar.setOnSeekBarChangeListener(listener);
        whiteningSeekBar.setOnSeekBarChangeListener(listener);
        ensureBeautyFx();
        beautyController.setFloat(beautyFx, "Strength", smoothSeekBar.getProgress() / 100.0);
        beautyController.setFloat(beautyFx, "Whitening", whiteningSeekBar.getProgress() / 100.0);
    }

    private void bindDeviceControls() {
        zoomSeekBar.setEnabled(false);
        exposureSeekBar.setEnabled(false);
        zoomSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (!fromUser) {
                    return;
                }
                selectedZoom = progress;
                applyDeviceControls(null, "Zoom");
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
            }
        });
        exposureSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (!fromUser || captureController == null) {
                    return;
                }
                int deviceIndex = currentDeviceIndex();
                NvsStreamingContext.CaptureDeviceCapability capability =
                        captureController.getDeviceCapability(deviceIndex);
                if (capability == null) {
                    return;
                }
                selectedExposure = capability.minExposureCompensation + progress;
                applyDeviceControls(null, "Exposure");
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
            }
        });
    }

    private void bindActions() {
        findViewById(R.id.switchCameraButton).setOnClickListener(v -> switchCamera());
        findViewById(R.id.filterButton).setOnClickListener(v -> toggleSampleFilter());
        findViewById(R.id.materialsButton).setOnClickListener(v -> {
            if (downloadedPackageFx != null) {
                removeDownloadedPackageFx();
                setStatus("Downloaded filter removed.");
                return;
            }
            openMaterialPicker(
                    NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX,
                    MeisheMaterialApplicationKind.FILTER);
        });
        findViewById(R.id.captureSceneButton).setOnClickListener(v -> {
            if (!activeCaptureSceneId.isEmpty()) {
                beautyController.removeCaptureScene();
                activeCaptureSceneId = "";
                setStatus("Capture Scene removed.");
                return;
            }
            openMaterialPicker(
                    NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE,
                    MeisheMaterialApplicationKind.CAPTURE_SCENE);
        });
        findViewById(R.id.arSceneButton).setOnClickListener(v -> {
            if (!activeArSceneId.isEmpty()) {
                beautyController.applyArScenePackage(arSceneFx, "");
                activeArSceneId = "";
                setStatus("AR Scene package removed.");
                return;
            }
            openMaterialPicker(
                    NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE,
                    MeisheMaterialApplicationKind.AR_SCENE);
        });
        findViewById(R.id.faceMeshButton).setOnClickListener(v -> {
            if (!activeFaceMeshId.isEmpty()) {
                beautyController.clearFaceMeshPackage(arSceneFx);
                activeFaceMeshId = "";
                setStatus("Face Mesh removed.");
                return;
            }
            openMaterialPicker(
                    NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH,
                    MeisheMaterialApplicationKind.FACE_MESH);
        });
        findViewById(R.id.makeupButton).setOnClickListener(v -> {
            if (!activeMakeupId.isEmpty()) {
                beautyController.clearMakeupPart(arSceneFx, "Lip");
                activeMakeupId = "";
                setStatus("Makeup removed.");
                return;
            }
            setStatus("Choose an authorized Makeup package. If none is listed, Contact Meishe business to obtain material resources.");
            openMaterialPicker(
                    NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP,
                    MeisheMaterialApplicationKind.MAKEUP);
        });
        findViewById(R.id.builtinArButton).setOnClickListener(v -> toggleArScene());
        findViewById(R.id.segmentationButton).setOnClickListener(v -> toggleSegmentation());
        focusButton.setOnClickListener(v -> focusAtCenter());
        flashButton.setOnClickListener(v -> toggleFlash());
        recordButton.setOnClickListener(v -> toggleRecording());
        pauseRecordingButton.setOnClickListener(v -> toggleRecordingPause());
    }

    private void openMaterialPicker(int packageType, String applicationKind) {
        if (recording) {
            setStatus("Stop recording before opening the material center.");
            return;
        }
        Intent intent = MeisheAssetCenterActivity.createPickerIntent(this);
        intent.putExtra(MeisheAssetCenterConfig.EXTRA_ASSET_TYPE, packageType);
        intent.putExtra(
                MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND,
                applicationKind);
        startActivityForResult(intent, REQUEST_MATERIAL);
    }

    private void ensureBeautyFx() {
        if (beautyFx == null) {
            beautyFx = beautyController.appendBeautyCaptureFx();
            if (beautyFx == null) {
                setStatus("This device or SDK build did not create the beauty effect.");
            }
        }
    }

    private NvsCaptureVideoFx ensureArSceneFx() {
        if (!humanModelsReady) {
            setStatus("AR Scene, Face Mesh, and Makeup require human models supplied with --human-models-dir.");
            return null;
        }
        if (arSceneFx == null) {
            arSceneFx = beautyController.appendArSceneCaptureFx(false);
            if (arSceneFx != null) {
                beautyController.configureArBeauty(arSceneFx, 0.5, 0.2);
            }
        }
        return arSceneFx;
    }

    private void toggleArScene() {
        if (arSceneFx != null) {
            if (!activeArSceneId.isEmpty()
                    || !activeFaceMeshId.isEmpty()
                    || !activeMakeupId.isEmpty()) {
                setStatus("Remove the active AR, Face Mesh, and Makeup materials before removing the shared AR Scene effect.");
                return;
            }
            removeCaptureFx(arSceneFx);
            arSceneFx = null;
            setStatus("AR Scene removed.");
            return;
        }
        if (!humanModelsReady) {
            setStatus("AR Scene requires human models supplied with --human-models-dir.");
            return;
        }
        setStatus(ensureArSceneFx() != null
                ? "AR Scene and model-backed beauty applied."
                : "AR Scene could not be created. Check AR module and model initialization.");
    }

    private void toggleSegmentation() {
        if (segmentationFx != null) {
            removeCaptureFx(segmentationFx);
            segmentationFx = null;
            setStatus("Background segmentation removed.");
            return;
        }
        if (!humanModelsReady) {
            setStatus("Background segmentation requires human models supplied with --human-models-dir.");
            return;
        }
        segmentationFx = beautyController.appendSegmentationBackgroundFx(
                new NvsColor(0.0f, 1.0f, 0.0f, 1.0f));
        setStatus(segmentationFx == null
                ? "Background segmentation could not be created."
                : "Background segmentation applied with a green background.");
    }

    private boolean removeCaptureFx(NvsCaptureVideoFx effect) {
        if (effect == null) {
            return false;
        }
        int count = sdkManager.getStreamingContext().getCaptureVideoFxCount();
        for (int index = count - 1; index >= 0; index--) {
            if (sdkManager.getStreamingContext().getCaptureVideoFxByIndex(index) == effect) {
                return sdkManager.getStreamingContext().removeCaptureVideoFx(index);
            }
        }
        return false;
    }

    private void bindTouchFocus() {
        liveWindow.setOnTouchListener((view, event) -> {
            if (event.getAction() != MotionEvent.ACTION_UP
                    || !focusButton.isEnabled()) {
                return true;
            }
            float radius = Math.max(
                    36.0f,
                    Math.min(view.getWidth(), view.getHeight()) * 0.08f);
            RectF focusRect = new RectF(
                    Math.max(0.0f, event.getX() - radius),
                    Math.max(0.0f, event.getY() - radius),
                    Math.min(view.getWidth(), event.getX() + radius),
                    Math.min(view.getHeight(), event.getY() + radius));
            applyDeviceControls(focusRect, "Touch focus");
            return true;
        });
    }

    private void registerCaptureCallbacks() {
        captureController.registerCallbacks(
                new NvsStreamingContext.CaptureDeviceCallback() {
                    @Override
                    public void onCaptureDeviceCapsReady(int deviceIndex) {
                        runOnUiThread(() -> {
                            activeCameraDeviceIndex = deviceIndex;
                            updateDeviceCapabilityUi();
                            setStatus(cameraLabel(deviceIndex) + " capabilities are ready.");
                        });
                    }

                    @Override
                    public void onCaptureDevicePreviewResolutionReady(int deviceIndex) {
                    }

                    @Override
                    public void onCaptureDevicePreviewStarted(int deviceIndex) {
                        runOnUiThread(() -> {
                            activeCameraDeviceIndex = deviceIndex;
                            isPreviewStarted = true;
                            updateDeviceCapabilityUi();
                            setStatus(cameraLabel(deviceIndex)
                                    + " preview started. Human models: "
                                    + (humanModelsReady ? "ready" : "not provided"));
                            applyPendingMaterialResult();
                        });
                    }

                    @Override
                    public void onCaptureDeviceError(int deviceIndex, int errorCode) {
                        runOnUiThread(() -> {
                            isPreviewStarted = false;
                            setStatus("Camera " + deviceIndex + " error: " + errorCode);
                        });
                    }

                    @Override
                    public void onCaptureDeviceStopped(int deviceIndex) {
                        runOnUiThread(() -> {
                            if (deviceIndex == activeCameraDeviceIndex) {
                                isPreviewStarted = false;
                            }
                        });
                    }

                    @Override
                    public void onCaptureDeviceAutoFocusComplete(
                            int deviceIndex,
                            boolean succeeded) {
                        runOnUiThread(() -> setStatus(succeeded
                                ? "Focus completed on " + cameraLabel(deviceIndex) + "."
                                : "Focus failed on " + cameraLabel(deviceIndex) + "."));
                    }

                    @Override
                    public void onCaptureRecordingFinished(int errorCode) {
                        runOnUiThread(() -> finishRecording(errorCode == 0, errorCode));
                    }

                    @Override
                    public void onCaptureRecordingError(int errorCode) {
                        runOnUiThread(() -> finishRecording(false, errorCode));
                    }
                },
                new NvsStreamingContext.CaptureRecordingStartedCallback() {
                    @Override
                    public void onCaptureRecordingStarted(int errorCode) {
                        runOnUiThread(() -> {
                            if (errorCode != 0) {
                                finishRecording(false, errorCode);
                                return;
                            }
                            recording = true;
                            recordingPaused = false;
                            updateRecordingControls();
                            setStatus("Recording started. Waiting for the first video frame.");
                        });
                    }
                },
                new NvsStreamingContext.CaptureRecordingDurationCallback() {
                    @Override
                    public void onCaptureRecordingDuration(int errorCode, long duration) {
                        runOnUiThread(() -> {
                            if (!recording || errorCode != 0) {
                                return;
                            }
                            setStatus(String.format(
                                    Locale.US,
                                    recordingPaused
                                            ? "Recording paused at %.1fs."
                                            : "Recording %.1fs%s",
                                    duration / 1_000_000.0,
                                    recordingFirstFrameReached
                                            ? ""
                                            : " · waiting for first frame"));
                        });
                    }
                },
                new NvsStreamingContext.CaptureRecordingFrameReachedCallback() {
                    @Override
                    public void onRecordingFirstVideoFrameReached(
                            int errorCode,
                            long timestamp) {
                        runOnUiThread(() -> {
                            if (errorCode == 0) {
                                recordingFirstFrameReached = true;
                                setStatus("The first video frame reached the recording file.");
                            }
                        });
                    }
                });
    }

    private void toggleSampleFilter() {
        if (sampleFilterFx != null) {
            removeCaptureFx(sampleFilterFx);
            sampleFilterFx = null;
            setStatus("Sample filter removed.");
            return;
        }
        String packageId = packageIds.get("filter");
        sampleFilterFx = beautyController.appendCapturePackagedFx(packageId);
        setStatus(sampleFilterFx == null
                ? "Sample filter could not be applied. Check package license."
                : "Sample packaged filter applied.");
    }

    private void switchCamera() {
        int deviceCount = captureController == null ? 0 : captureController.getDeviceCount();
        if (deviceCount <= 1) {
            setStatus("No second camera device is available.");
            return;
        }
        captureController.setFlashEnabled(currentDeviceIndex(), false);
        flashEnabled = false;
        requestedCameraDeviceIndex = (currentDeviceIndex() + 1) % deviceCount;
        captureController.stop();
        isPreviewStarted = false;
        startPreview();
    }

    private void startPreview() {
        if (!hasCapturePermissions() || captureController == null) {
            return;
        }
        requestedCameraDeviceIndex =
                captureController.resolveDeviceIndex(requestedCameraDeviceIndex);
        boolean requestAccepted = requestedCameraDeviceIndex >= 0
                && captureController.startPreview(requestedCameraDeviceIndex);
        isPreviewStarted = false;
        setStatus(requestAccepted
                ? "Starting camera " + requestedCameraDeviceIndex
                        + ". Installed sample packages: " + packageIds.size() + "."
                : "Camera preview failed.");
    }

    private int currentDeviceIndex() {
        return activeCameraDeviceIndex >= 0
                ? activeCameraDeviceIndex
                : requestedCameraDeviceIndex;
    }

    private String cameraLabel(int deviceIndex) {
        return (captureController != null && captureController.isBackFacing(deviceIndex)
                ? "Back camera "
                : "Front camera ") + deviceIndex;
    }

    private void updateDeviceCapabilityUi() {
        if (captureController == null) {
            return;
        }
        int deviceIndex = currentDeviceIndex();
        NvsStreamingContext.CaptureDeviceCapability capability =
                captureController.getDeviceCapability(deviceIndex);
        if (capability == null) {
            focusButton.setEnabled(false);
            flashButton.setEnabled(false);
            zoomSeekBar.setEnabled(false);
            exposureSeekBar.setEnabled(false);
            return;
        }

        focusButton.setEnabled(
                capability.supportAutoFocus || capability.supportAutoExposure);
        boolean canUseFlash = capability.supportFlash
                && captureController.isBackFacing(deviceIndex);
        flashButton.setEnabled(canUseFlash);
        if (!canUseFlash) {
            flashEnabled = false;
            flashButton.setText("Flash");
        }

        zoomSeekBar.setEnabled(capability.supportZoom);
        zoomSeekBar.setMax(Math.max(0, capability.maxZoom));
        selectedZoom = Math.max(
                0,
                Math.min(captureController.getZoom(), capability.maxZoom));
        zoomSeekBar.setProgress(selectedZoom);

        exposureSeekBar.setEnabled(capability.supportExposureCompensation);
        exposureSeekBar.setMax(Math.max(
                0,
                capability.maxExposureCompensation
                        - capability.minExposureCompensation));
        selectedExposure = Math.max(
                capability.minExposureCompensation,
                Math.min(
                        captureController.getExposureCompensation(),
                        capability.maxExposureCompensation));
        exposureSeekBar.setProgress(
                selectedExposure - capability.minExposureCompensation);
    }

    private void applyDeviceControls(RectF focusRect, String controlName) {
        if (!isPreviewStarted || captureController == null) {
            setStatus("Start camera preview before changing " + controlName + ".");
            return;
        }
        boolean applied = captureController.configureDeviceControls(
                currentDeviceIndex(),
                selectedExposure,
                selectedZoom,
                focusRect,
                flashEnabled);
        setStatus(applied
                ? controlName + " applied on "
                        + cameraLabel(currentDeviceIndex()) + "."
                : controlName + " is not supported by the active camera.");
    }

    private void focusAtCenter() {
        if (liveWindow == null
                || liveWindow.getWidth() <= 0
                || liveWindow.getHeight() <= 0) {
            setStatus("Live camera bounds are not ready for focus.");
            return;
        }
        applyDeviceControls(
                new RectF(
                        liveWindow.getWidth() * 0.4f,
                        liveWindow.getHeight() * 0.4f,
                        liveWindow.getWidth() * 0.6f,
                        liveWindow.getHeight() * 0.6f),
                "Center focus");
    }

    private void toggleFlash() {
        boolean requestedFlash = !flashEnabled;
        boolean applied = captureController.setFlashEnabled(
                currentDeviceIndex(),
                requestedFlash);
        flashEnabled = captureController.isFlashEnabled();
        flashButton.setText(flashEnabled ? "Flash off" : "Flash");
        setStatus(applied
                ? (flashEnabled ? "Flash enabled." : "Flash disabled.")
                : "Flash is not supported by the active camera.");
    }

    private void toggleRecording() {
        if (!hasCapturePermissions()) {
            requestCapturePermissionsIfNeeded();
            return;
        }
        if (!isPreviewStarted) {
            startPreview();
            return;
        }
        if (recording) {
            recordButton.setEnabled(false);
            pauseRecordingButton.setEnabled(false);
            if (!captureController.stopRecordingSynchronously(true)) {
                recordButton.setEnabled(true);
                pauseRecordingButton.setEnabled(true);
                setStatus("Recording could not be stopped.");
            } else {
                setStatus("Finalizing the recording file...");
            }
            return;
        }
        File outDir = getExternalFilesDir(Environment.DIRECTORY_MOVIES);
        if (outDir == null) {
            setStatus("Movie output directory is unavailable.");
            return;
        }
        recordingOutput =
                new File(outDir, "beauty_camera_" + System.currentTimeMillis() + ".mp4");
        recordingFirstFrameReached = false;
        recordingPaused = false;
        recording = captureController.startRecording(recordingOutput.getAbsolutePath());
        updateRecordingControls();
        setStatus(recording
                ? "Recording requested: " + recordingOutput.getName()
                : "Failed to start recording.");
    }

    private void toggleRecordingPause() {
        if (!recording || captureController == null) {
            return;
        }
        boolean changed = recordingPaused
                ? captureController.resumeRecording()
                : captureController.pauseRecording();
        if (changed) {
            recordingPaused = captureController.isRecordingPaused();
            setStatus(recordingPaused ? "Recording paused." : "Recording resumed.");
        } else {
            setStatus(recordingPaused
                    ? "Recording could not resume."
                    : "Recording could not pause.");
        }
        updateRecordingControls();
    }

    private void updateRecordingControls() {
        recordButton.setText(recording ? "Stop" : "Record");
        recordButton.setEnabled(true);
        pauseRecordingButton.setEnabled(recording);
        pauseRecordingButton.setText(recordingPaused ? "Resume" : "Pause");
    }

    private void finishRecording(boolean succeeded, int errorCode) {
        recording = false;
        recordingPaused = false;
        updateRecordingControls();
        boolean outputReady = recordingOutput != null
                && recordingOutput.isFile()
                && recordingOutput.length() > 0;
        setStatus(succeeded && outputReady
                ? "Recording saved: " + recordingOutput.getName()
                        + " (" + recordingOutput.length() + " bytes)."
                : "Recording failed or produced no file. Error: " + errorCode);
    }

    private boolean hasCapturePermissions() {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M) {
            return true;
        }
        for (String permission : CAPTURE_PERMISSIONS) {
            if (checkSelfPermission(permission) != PackageManager.PERMISSION_GRANTED) {
                return false;
            }
        }
        return true;
    }

    private boolean requestCapturePermissionsIfNeeded() {
        if (hasCapturePermissions()) {
            return true;
        }
        if (!permissionRequestInFlight) {
            permissionRequestInFlight = true;
            requestPermissions(CAPTURE_PERMISSIONS, REQUEST_CAPTURE_PERMISSIONS);
        }
        return false;
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode != REQUEST_CAPTURE_PERMISSIONS) {
            return;
        }
        permissionRequestInFlight = false;
        for (int result : grantResults) {
            if (result != PackageManager.PERMISSION_GRANTED) {
                Toast.makeText(this, "Camera and microphone permissions are required.", Toast.LENGTH_LONG).show();
                return;
            }
        }
        getWindow().getDecorView().post(this::startPreview);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode != REQUEST_MATERIAL || resultCode != RESULT_OK || data == null) {
            return;
        }
        String packageId = data.getStringExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_ID);
        int packageType = data.getIntExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_TYPE, -1);
        String applicationKind = data.getStringExtra(
                MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND);
        if (packageId == null || packageId.isEmpty() || applicationKind == null) {
            setStatus("The material center returned an incomplete material contract.");
            return;
        }
        if (!isSupportedMaterialContract(applicationKind, packageType)) {
            setStatus("Material application kind and package type do not match. Nothing was changed.");
            return;
        }
        pendingMaterialPackageId = packageId;
        pendingMaterialPackageType = packageType;
        pendingMaterialApplicationKind = applicationKind;
        if (isPreviewStarted) {
            applyPendingMaterialResult();
        } else {
            pendingResumeStatus = "Restarting camera preview before applying the selected material.";
        }
    }

    private boolean isSupportedMaterialContract(String applicationKind, int packageType) {
        return (MeisheMaterialApplicationKind.FILTER.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX)
                || (MeisheMaterialApplicationKind.CAPTURE_SCENE.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE)
                || (MeisheMaterialApplicationKind.AR_SCENE.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE)
                || (MeisheMaterialApplicationKind.FACE_MESH.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH)
                || (MeisheMaterialApplicationKind.MAKEUP.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP);
    }

    private void applyPendingMaterialResult() {
        if (!isPreviewStarted
                || pendingMaterialPackageId == null
                || pendingMaterialApplicationKind == null) {
            return;
        }
        String packageId = pendingMaterialPackageId;
        int packageType = pendingMaterialPackageType;
        String applicationKind = pendingMaterialApplicationKind;
        pendingMaterialPackageId = null;
        pendingMaterialPackageType = -1;
        pendingMaterialApplicationKind = null;

        if (MeisheMaterialApplicationKind.FILTER.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX) {
            removeDownloadedPackageFx();
            downloadedPackageFx = beautyController.appendCapturePackagedFx(packageId);
            pendingResumeStatus = downloadedPackageFx == null
                    ? "Package installed but could not be added to the capture effect chain."
                    : "Downloaded filter applied to the live camera.";
            setStatus(pendingResumeStatus);
            return;
        }
        if (MeisheMaterialApplicationKind.CAPTURE_SCENE.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE) {
            boolean applied = beautyController.applyCaptureScene(
                    sdkManager.getStreamingContext(),
                    packageId);
            if (applied) {
                activeCaptureSceneId = packageId;
            }
            setStatus(applied
                    ? "Capture Scene applied to the live camera."
                    : "Capture Scene installation succeeded, but applyCaptureScene failed.");
            return;
        }
        if (MeisheMaterialApplicationKind.AR_SCENE.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE) {
            boolean applied = beautyController.applyArScenePackage(
                    ensureArSceneFx(),
                    packageId);
            if (applied) {
                activeArSceneId = packageId;
            }
            String prompt = beautyController.getArScenePackagePrompt(packageId);
            setStatus(applied
                    ? "AR Scene package applied."
                            + (prompt.isEmpty() ? "" : "\n" + prompt)
                    : "AR Scene package installed, but Scene Id could not be bound.");
            return;
        }
        if (MeisheMaterialApplicationKind.FACE_MESH.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH) {
            boolean applied = beautyController.applyEyebrowAngleFaceMeshPackage(
                    ensureArSceneFx(),
                    packageId,
                    0.65);
            if (applied) {
                activeFaceMeshId = packageId;
            }
            setStatus(applied
                    ? "Eyebrow-angle Face Mesh applied at 65%."
                    : "Face Mesh package installed, but AR Scene binding failed.");
            return;
        }
        if (MeisheMaterialApplicationKind.MAKEUP.equals(applicationKind)
                && packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP) {
            if (ensureArSceneFx() == null) {
                return;
            }
            boolean applied = beautyController.configureMakeupPart(
                    arSceneFx, "Lip", packageId, 0.6);
            if (applied) {
                activeMakeupId = packageId;
            }
            setStatus(applied
                    ? "Lip Makeup package applied at 60%."
                    : "Makeup package installed, but AR Scene binding failed.");
            return;
        }
    }

    private void removeDownloadedPackageFx() {
        if (downloadedPackageFx == null) {
            return;
        }
        int count = sdkManager.getStreamingContext().getCaptureVideoFxCount();
        for (int index = count - 1; index >= 0; index--) {
            if (sdkManager.getStreamingContext().getCaptureVideoFxByIndex(index) == downloadedPackageFx) {
                sdkManager.getStreamingContext().removeCaptureVideoFx(index);
                break;
            }
        }
        downloadedPackageFx = null;
    }

    private void setControlsEnabled(boolean enabled) {
        findViewById(R.id.switchCameraButton).setEnabled(enabled);
        findViewById(R.id.filterButton).setEnabled(enabled);
        findViewById(R.id.materialsButton).setEnabled(enabled);
        findViewById(R.id.arSceneButton).setEnabled(enabled);
        findViewById(R.id.builtinArButton).setEnabled(enabled);
        findViewById(R.id.captureSceneButton).setEnabled(enabled);
        findViewById(R.id.makeupButton).setEnabled(enabled);
        findViewById(R.id.faceMeshButton).setEnabled(enabled);
        findViewById(R.id.segmentationButton).setEnabled(enabled);
        recordButton.setEnabled(enabled);
        pauseRecordingButton.setEnabled(enabled && recording);
        focusButton.setEnabled(enabled);
        flashButton.setEnabled(enabled);
        findViewById(R.id.smoothSeekBar).setEnabled(enabled);
        findViewById(R.id.whiteningSeekBar).setEnabled(enabled);
        zoomSeekBar.setEnabled(enabled);
        exposureSeekBar.setEnabled(enabled);
    }

    private void setStatus(String message) {
        statusText.setText(message);
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (captureController != null && hasCapturePermissions() && !isPreviewStarted) {
            startPreview();
        }
        if (pendingResumeStatus != null) {
            setStatus(pendingResumeStatus);
            pendingResumeStatus = null;
        }
    }

    @Override
    protected void onPause() {
        if (captureController != null) {
            if (recording) {
                captureController.stopRecordingSynchronously(true);
            }
            captureController.stop();
            isPreviewStarted = false;
        }
        super.onPause();
    }

    @Override
    protected void onDestroy() {
        if (captureController != null) {
            captureController.registerCallbacks(null, null, null, null);
        }
        if (beautyController != null && humanModelsReady) {
            beautyController.releaseHumanDetection();
        }
        super.onDestroy();
    }
}
