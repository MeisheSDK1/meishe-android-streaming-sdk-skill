package {{PACKAGE_NAME}};

import android.Manifest;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.view.Gravity;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoTrack;
import java.io.IOException;
import java.io.File;
import java.util.ArrayList;
import java.util.Map;

public class MeisheRuntimeDemoActivity extends Activity {
    public static final String MODE_EDITOR = "editor";
    public static final String MODE_CAPTURE = "capture";
    public static final String MODE_PIP = "pip";
    public static final String MODE_QUICK_SPLICE = "quick-splice";

    private static final String EXTRA_MODE = "meishe.runtime.mode";
    private static final String EXTRA_MEDIA_PATHS = "meishe.runtime.media-paths";
    private static final String EXTRA_PROJECT_WIDTH = "meishe.runtime.projectWidth";
    private static final String EXTRA_PROJECT_HEIGHT = "meishe.runtime.projectHeight";
    private static final String EXTRA_MATERIAL_PACKAGE_ID = "meishe.installedPackageId";
    private static final String EXTRA_MATERIAL_PACKAGE_TYPE = "meishe.installedPackageType";
    private static final int REQUEST_CAPTURE_PERMISSIONS = 7001;

    private String mode;
    private TextView statusText;
    private FrameLayout liveWindowContainer;
    private Button primaryButton;
    private Button secondaryButton;
    private Button tertiaryButton;
    private NvsStreamingContext streamingContext;
    private NvsLiveWindow liveWindow;
    private NvsTimeline timeline;
    private MeisheTimelineController timelineController;
    private MeisheCaptureController captureController;
    private boolean playing;
    private boolean recording;
    private boolean capturePreviewStarted;
    private boolean permissionRequestInFlight;
    private int captureDeviceIndex;
    private int projectWidth;
    private int projectHeight;
    private ArrayList<String> quickSplicePaths = new ArrayList<>();
    private boolean quickSpliceTransitionEnabled = true;
    private File activeCaptureFile;
    private File lastCapturedFile;
    private boolean pendingCaptureMaterialApplied;

    public static Intent createIntent(Context context, String mode) {
        return new Intent(context, MeisheRuntimeDemoActivity.class).putExtra(EXTRA_MODE, mode);
    }

    public static Intent createIntent(Context context, String mode, ArrayList<String> mediaPaths) {
        return createIntent(context, mode).putStringArrayListExtra(EXTRA_MEDIA_PATHS, mediaPaths);
    }

    public static Intent createIntent(
            Context context,
            String mode,
            ArrayList<String> mediaPaths,
            int width,
            int height) {
        return createIntent(context, mode, mediaPaths)
                .putExtra(EXTRA_PROJECT_WIDTH, width)
                .putExtra(EXTRA_PROJECT_HEIGHT, height);
    }

    public static Intent createCaptureIntentWithMaterial(
            Context context,
            String packageId,
            int packageType) {
        return createIntent(context, MODE_CAPTURE)
                .putExtra(EXTRA_MATERIAL_PACKAGE_ID, packageId)
                .putExtra(EXTRA_MATERIAL_PACKAGE_TYPE, packageType);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mode = getIntent().getStringExtra(EXTRA_MODE);
        if (mode == null || mode.isEmpty()) {
            mode = MODE_EDITOR;
        }
        projectWidth = getIntent().getIntExtra(EXTRA_PROJECT_WIDTH, 720);
        projectHeight = getIntent().getIntExtra(EXTRA_PROJECT_HEIGHT, 1280);
        buildScreen();
        MeisheAppSupport.applySystemBarInsets(this);

        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        if (!sdkManager.initialize()) {
            setStatus("SDK initialization failed. Check license, JAR, and native libraries.");
            setControlsEnabled(false);
            return;
        }
        streamingContext = sdkManager.getStreamingContext();
        liveWindow = new NvsLiveWindow(this);
        liveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);
        liveWindowContainer.addView(liveWindow, new FrameLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.MATCH_PARENT));

        if (MODE_CAPTURE.equals(mode)) {
            bindCaptureControls();
            requestCapturePermissionsIfNeeded();
        } else {
            bindTimelineCallbacks();
            buildTimelineDemo();
        }
    }

    private void buildScreen() {
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setPadding(dp(16), dp(12), dp(16), dp(12));
        root.setBackgroundResource(R.drawable.bg_screen_gradient);

        statusText = new TextView(this);
        statusText.setTextColor(getResources().getColor(R.color.text_secondary));
        statusText.setTextSize(15);
        statusText.setText("Initializing SDK...");
        statusText.setGravity(Gravity.CENTER_VERTICAL);
        statusText.setMinHeight(dp(58));
        statusText.setBackgroundResource(R.drawable.bg_surface_card);
        root.addView(statusText, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT));

        liveWindowContainer = new FrameLayout(this);
        liveWindowContainer.setBackgroundResource(R.drawable.bg_preview_stage);
        LinearLayout.LayoutParams previewParams = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                0,
                1f);
        previewParams.topMargin = dp(12);
        root.addView(liveWindowContainer, previewParams);

        LinearLayout controls = new LinearLayout(this);
        controls.setOrientation(LinearLayout.HORIZONTAL);
        controls.setGravity(Gravity.CENTER);
        primaryButton = addControl(controls);
        secondaryButton = addControl(controls);
        tertiaryButton = addControl(controls);
        LinearLayout.LayoutParams controlParams = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT);
        controlParams.topMargin = dp(12);
        root.addView(controls, controlParams);
        setContentView(root);
    }

    private Button addControl(LinearLayout parent) {
        Button button = new Button(this);
        button.setAllCaps(false);
        button.setTextColor(getResources().getColor(R.color.text_primary));
        button.setBackgroundResource(R.drawable.bg_button_secondary);
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(0, dp(52), 1f);
        params.setMarginStart(dp(4));
        params.setMarginEnd(dp(4));
        parent.addView(button, params);
        return button;
    }

    private void buildTimelineDemo() {
        timelineController = new MeisheTimelineController(streamingContext);
        timeline = timelineController.createTimeline(projectWidth, projectHeight);
        if (timeline == null) {
            setStatus("Timeline creation failed.");
            setControlsEnabled(false);
            return;
        }

        ArrayList<String> selectedPaths = getIntent().getStringArrayListExtra(EXTRA_MEDIA_PATHS);
        boolean built;
        if (MODE_PIP.equals(mode)) {
            built = buildPipTimeline(selectedPaths);
        } else if (MODE_QUICK_SPLICE.equals(mode)) {
            built = buildQuickSpliceTimeline(selectedPaths);
        } else {
            String path = firstPathOrSample(selectedPaths);
            built = timelineController.appendClip(path) != null;
        }
        if (!built || !streamingContext.connectTimelineWithLiveWindow(timeline, liveWindow)) {
            setStatus("Timeline media could not be connected to LiveWindow.");
            setControlsEnabled(false);
            return;
        }
        streamingContext.seekTimeline(
                timeline,
                0,
                NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
                        | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
        bindTimelineControls();
        if (MODE_PIP.equals(mode)) {
            setStatus("PIP ready: two tracks with Transform 2D overlay.");
        } else if (MODE_QUICK_SPLICE.equals(mode)) {
            updateQuickSpliceStatus();
        } else {
            setStatus("Sample editor timeline is connected to LiveWindow.");
        }
    }

    private boolean buildPipTimeline(ArrayList<String> paths) {
        String basePath = paths != null && !paths.isEmpty()
                ? paths.get(0)
                : MeisheSampleAssets.SAMPLE_IMAGE_PATH;
        String overlayPath = paths != null && paths.size() > 1
                ? paths.get(1)
                : MeisheSampleAssets.SAMPLE_OVERLAY_IMAGE_PATH;
        return MeisheCompositionController.buildPictureInPicture(
                timeline,
                basePath,
                overlayPath);
    }

    private boolean buildQuickSpliceTimeline(ArrayList<String> paths) {
        quickSplicePaths.clear();
        if (paths != null) {
            for (String path : paths) {
                if (path != null && !path.isEmpty()) {
                    quickSplicePaths.add(path);
                }
            }
        }
        if (quickSplicePaths.isEmpty()) {
            try {
                quickSplicePaths.add(MeisheMediaFiles.copyAssetToProject(
                        this,
                        "sample/demo_base.jpg",
                        "quick_splice_base.jpg"));
                quickSplicePaths.add(MeisheMediaFiles.copyAssetToProject(
                        this,
                        "sample/demo_overlay.jpg",
                        "quick_splice_overlay.jpg"));
            } catch (IOException exception) {
                return false;
            }
        }
        MeisheAssetInstaller installer = new MeisheAssetInstaller(streamingContext);
        Map<String, String> packageIds = MeisheSampleAssets.installDefaultPackages(installer);
        String transitionId = packageIds.get("transition");
        return MeisheCompositionController.buildQuickSplice(
                timeline,
                quickSplicePaths,
                transitionId) >= 2;
    }

    private String firstPathOrSample(ArrayList<String> paths) {
        return paths != null && !paths.isEmpty() && paths.get(0) != null
                ? paths.get(0)
                : MeisheSampleAssets.SAMPLE_IMAGE_PATH;
    }

    private void bindTimelineControls() {
        if (MODE_QUICK_SPLICE.equals(mode)) {
            bindQuickSpliceControls();
            return;
        }
        primaryButton.setText("Play");
        secondaryButton.setText("Export");
        tertiaryButton.setText("Stop");
        primaryButton.setOnClickListener(v -> {
            if (timeline == null) {
                return;
            }
            if (playing) {
                streamingContext.stop();
                setPlaying(false);
                return;
            }
            long start = Math.max(0, streamingContext.getTimelineCurrentPosition(timeline));
            if (start >= timeline.getDuration()) {
                start = 0;
            }
            boolean started = streamingContext.playbackTimeline(
                    timeline,
                    start,
                    timeline.getDuration(),
                    NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                    true,
                    0);
            setPlaying(started);
            setStatus(started ? "Timeline playback started." : "Timeline playback could not start.");
        });
        secondaryButton.setOnClickListener(v -> exportTimeline());
        tertiaryButton.setOnClickListener(v -> {
            streamingContext.stop();
            setPlaying(false);
            setStatus("Streaming engine stopped.");
        });
    }

    private void bindQuickSpliceControls() {
        primaryButton.setText("Play");
        secondaryButton.setText("Disable transition");
        tertiaryButton.setText("Open full editor");
        primaryButton.setOnClickListener(v -> toggleTimelinePlayback());
        secondaryButton.setOnClickListener(v -> toggleQuickSpliceTransition());
        tertiaryButton.setOnClickListener(v ->
                openEditorWithMedia(quickSplicePaths, projectWidth, projectHeight));
    }

    private void toggleTimelinePlayback() {
        if (timeline == null) {
            return;
        }
        if (playing) {
            streamingContext.stop();
            setPlaying(false);
            return;
        }
        long startUs = Math.max(0, streamingContext.getTimelineCurrentPosition(timeline));
        if (startUs >= timeline.getDuration()) {
            startUs = 0;
        }
        boolean started = streamingContext.playbackTimeline(
                timeline,
                startUs,
                timeline.getDuration(),
                NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                true,
                0);
        setPlaying(started);
        setStatus(started
                ? "Previewing the splice in the selected order."
                : "Splice preview could not start.");
    }

    private void toggleQuickSpliceTransition() {
        NvsVideoTrack track = timeline == null ? null : timeline.getVideoTrackByIndex(0);
        if (track == null || track.getClipCount() < 2) {
            setStatus("At least two clips are required to toggle transitions.");
            return;
        }
        quickSpliceTransitionEnabled = !quickSpliceTransitionEnabled;
        for (int index = 0; index + 1 < track.getClipCount(); index++) {
            track.setBuiltinTransition(index, quickSpliceTransitionEnabled ? "Fade" : "");
        }
        secondaryButton.setText(quickSpliceTransitionEnabled
                ? "Disable transition"
                : "Enable transition");
        streamingContext.seekTimeline(
                timeline,
                Math.max(0, streamingContext.getTimelineCurrentPosition(timeline)),
                NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                0);
        updateQuickSpliceStatus();
    }

    private void updateQuickSpliceStatus() {
        double durationSeconds = timeline == null ? 0 : timeline.getDuration() / 1_000_000.0;
        setStatus("Quick splice: " + quickSplicePaths.size()
                + " clips in the selected order; "
                + (quickSpliceTransitionEnabled ? "transition enabled" : "no transition")
                + "; total " + String.format(java.util.Locale.US, "%.1f seconds.", durationSeconds));
    }

    private void bindTimelineCallbacks() {
        streamingContext.setPlaybackCallback(new NvsStreamingContext.PlaybackCallback() {
            @Override
            public void onPlaybackPreloadingCompletion(NvsTimeline callbackTimeline) {
            }

            @Override
            public void onPlaybackStopped(NvsTimeline callbackTimeline) {
                runOnUiThread(() -> setPlaying(false));
            }

            @Override
            public void onPlaybackEOF(NvsTimeline callbackTimeline) {
                runOnUiThread(() -> {
                    setPlaying(false);
                    streamingContext.seekTimeline(
                            timeline,
                            0,
                            NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                            0);
                    setStatus("Playback finished.");
                });
            }
        });
        streamingContext.setCompileCallback(new NvsStreamingContext.CompileCallback() {
            @Override
            public void onCompileProgress(NvsTimeline callbackTimeline, int progress) {
                runOnUiThread(() -> setStatus("Exporting: " + progress + "%"));
            }

            @Override
            public void onCompileFinished(NvsTimeline callbackTimeline) {
                runOnUiThread(() -> setStatus("Export finished in the app Movies directory."));
            }

            @Override
            public void onCompileFailed(NvsTimeline callbackTimeline) {
                runOnUiThread(() -> setStatus("Export failed. Check license and codec support."));
            }
        });
    }

    private void exportTimeline() {
        File movies = getExternalFilesDir(Environment.DIRECTORY_MOVIES);
        if (movies == null) {
            setStatus("External Movies directory is unavailable.");
            return;
        }
        File output = new File(movies, mode + "-" + System.currentTimeMillis() + ".mp4");
        boolean started = new MeisheExportController(streamingContext).export(
                timeline,
                output.getAbsolutePath());
        setStatus(started ? "Export started: " + output.getName() : "Export could not start.");
    }

    private void bindCaptureControls() {
        primaryButton.setText("Record");
        secondaryButton.setText("Switch");
        tertiaryButton.setText("Edit recording");
        tertiaryButton.setEnabled(false);
        primaryButton.setOnClickListener(v -> toggleRecording());
        secondaryButton.setOnClickListener(v -> switchCamera());
        tertiaryButton.setOnClickListener(v -> openCapturedResult());
    }

    private void requestCapturePermissionsIfNeeded() {
        if (hasCapturePermissions()) {
            startCapturePreview();
            return;
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && !permissionRequestInFlight) {
            permissionRequestInFlight = true;
            requestPermissions(
                    new String[]{Manifest.permission.CAMERA, Manifest.permission.RECORD_AUDIO},
                    REQUEST_CAPTURE_PERMISSIONS);
        }
    }

    private boolean hasCapturePermissions() {
        return Build.VERSION.SDK_INT < Build.VERSION_CODES.M
                || (checkSelfPermission(Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED
                && checkSelfPermission(Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode != REQUEST_CAPTURE_PERMISSIONS) {
            return;
        }
        permissionRequestInFlight = false;
        if (hasCapturePermissions()) {
            statusText.post(this::startCapturePreview);
        } else {
            setStatus("Camera and microphone permissions are required.");
        }
    }

    private void startCapturePreview() {
        if (!hasCapturePermissions() || capturePreviewStarted || streamingContext == null) {
            return;
        }
        captureController = new MeisheCaptureController(streamingContext, liveWindow);
        capturePreviewStarted = captureController.startPreview(captureDeviceIndex);
        if (capturePreviewStarted) {
            applyPendingCaptureMaterial();
            setStatus(lastCapturedFile == null
                    ? "Camera preview is ready. A completed recording can open in the timeline editor."
                    : "Camera preview resumed. Record again or edit the previous result.");
        } else {
            setStatus("Camera preview failed to start.");
        }
    }

    private void switchCamera() {
        if (streamingContext == null || streamingContext.getCaptureDeviceCount() < 2) {
            setStatus("A second camera is not available.");
            return;
        }
        if (recording) {
            setStatus("Stop recording before switching cameras.");
            return;
        }
        streamingContext.stop();
        capturePreviewStarted = false;
        captureDeviceIndex = (captureDeviceIndex + 1) % streamingContext.getCaptureDeviceCount();
        startCapturePreview();
    }

    private void toggleRecording() {
        if (captureController == null || !capturePreviewStarted) {
            setStatus("Start camera preview before recording.");
            return;
        }
        if (recording) {
            finishCurrentRecording();
            return;
        }
        File movies = getExternalFilesDir(Environment.DIRECTORY_MOVIES);
        if (movies == null) {
            setStatus("External Movies directory is unavailable.");
            return;
        }
        activeCaptureFile = new File(movies, "capture-" + System.currentTimeMillis() + ".mp4");
        recording = captureController.startRecording(activeCaptureFile.getAbsolutePath());
        primaryButton.setText(recording ? "Stop rec" : "Record");
        tertiaryButton.setEnabled(false);
        setStatus(recording ? "Recording started: " + activeCaptureFile.getName() : "Recording could not start.");
    }

    private void finishCurrentRecording() {
        if (captureController == null || !recording) {
            return;
        }
        captureController.stopRecordingSynchronously(true);
        recording = false;
        primaryButton.setText("Record");
        if (activeCaptureFile != null && activeCaptureFile.isFile()
                && activeCaptureFile.length() > 0) {
            lastCapturedFile = activeCaptureFile;
            tertiaryButton.setEnabled(true);
            setStatus("Recording is ready for editing: " + lastCapturedFile.getName()
                    + ". Record again or open the full editor.");
        } else {
            setStatus("The recording result is unavailable. Record again.");
        }
        activeCaptureFile = null;
    }

    private void openCapturedResult() {
        if (recording) {
            finishCurrentRecording();
        }
        if (lastCapturedFile == null || !lastCapturedFile.isFile()) {
            setStatus("Complete a valid recording first.");
            return;
        }
        ArrayList<String> mediaPaths = new ArrayList<>();
        mediaPaths.add(lastCapturedFile.getAbsolutePath());
        openEditorWithMedia(mediaPaths, 720, 1280);
    }

    private void openEditorWithMedia(ArrayList<String> mediaPaths, int width, int height) {
        try {
            Class<?> editorClass = Class.forName(getPackageName() + ".MeisheEditorActivity");
            java.lang.reflect.Method factory = editorClass.getMethod(
                    "createIntent",
                    Context.class,
                    ArrayList.class,
                    int.class,
                    int.class);
            startActivity((Intent) factory.invoke(null, this, mediaPaths, width, height));
        } catch (Exception exception) {
            setStatus("The recording or splice is ready. Add the editor-shell module to continue editing it.");
        }
    }

    private void applyPendingCaptureMaterial() {
        if (pendingCaptureMaterialApplied) {
            return;
        }
        String packageId = getIntent().getStringExtra(EXTRA_MATERIAL_PACKAGE_ID);
        int packageType = getIntent().getIntExtra(
                EXTRA_MATERIAL_PACKAGE_TYPE,
                -1);
        if (packageId == null || packageId.isEmpty()) {
            return;
        }
        pendingCaptureMaterialApplied = true;
        boolean applied = packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE
                ? streamingContext.applyCaptureScene(packageId)
                : streamingContext.appendPackagedCaptureVideoFx(packageId) != null;
        setStatus(applied
                ? "Applied the selected material to the live camera preview."
                : "The material is installed, but this camera cannot apply its package type.");
    }

    private void stopCapture() {
        if (captureController != null) {
            if (recording) {
                finishCurrentRecording();
            }
            captureController.stop();
        }
        recording = false;
        capturePreviewStarted = false;
        primaryButton.setText("Record");
        if (!isFinishing()) {
            setStatus(lastCapturedFile == null
                    ? "Capture engine stopped."
                    : "Capture stopped. The recording can still be opened in the editor.");
        }
    }

    private void setPlaying(boolean value) {
        playing = value;
        primaryButton.setText(value ? "Pause" : "Play");
    }

    private void setControlsEnabled(boolean enabled) {
        primaryButton.setEnabled(enabled);
        secondaryButton.setEnabled(enabled);
        tertiaryButton.setEnabled(enabled);
    }

    private void setStatus(String message) {
        statusText.setText(message);
    }

    private int dp(int value) {
        return Math.round(value * getResources().getDisplayMetrics().density);
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (MODE_CAPTURE.equals(mode) && hasCapturePermissions()) {
            startCapturePreview();
        }
    }

    @Override
    protected void onPause() {
        if (MODE_CAPTURE.equals(mode)) {
            stopCapture();
        } else if (streamingContext != null) {
            streamingContext.stop();
        }
        super.onPause();
    }

    @Override
    protected void onDestroy() {
        if (streamingContext != null) {
            streamingContext.setPlaybackCallback(null);
            streamingContext.setCompileCallback(null);
            streamingContext.stop();
        }
        if (timelineController != null) {
            timelineController.removeTimeline();
        }
        super.onDestroy();
    }
}
