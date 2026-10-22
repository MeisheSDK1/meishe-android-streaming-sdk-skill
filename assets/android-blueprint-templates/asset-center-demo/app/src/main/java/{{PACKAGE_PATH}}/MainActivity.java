package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.os.Bundle;
import android.view.Gravity;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.SeekBar;
import android.widget.TextView;

import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsLiveWindow;
import com.meicam.sdk.NvsStreamingContext;
import com.meicam.sdk.NvsTimeline;
import com.meicam.sdk.NvsVideoClip;
import com.meicam.sdk.NvsVideoFx;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class MainActivity extends Activity {
    private static final int REQUEST_FILTER_MATERIAL = 4101;
    private static final int PROJECT_WIDTH = 720;
    private static final int PROJECT_HEIGHT = 1280;

    private TextView statusText;
    private TextView intensityText;
    private Button openMaterialCenterButton;
    private Button removeFilterButton;
    private SeekBar intensitySeekBar;
    private NvsStreamingContext streamingContext;
    private NvsTimeline timeline;
    private NvsVideoClip previewClip;
    private NvsVideoFx appliedFilter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_asset_center_demo);
        MeisheAppSupport.applySystemBarInsets(this);

        statusText = findViewById(R.id.materialPreviewStatusText);
        intensityText = findViewById(R.id.materialIntensityText);
        openMaterialCenterButton = findViewById(R.id.openMaterialCenterButton);
        removeFilterButton = findViewById(R.id.removeFilterButton);
        intensitySeekBar = findViewById(R.id.materialIntensitySeekBar);
        openMaterialCenterButton.setOnClickListener(view -> openFilterPicker());
        removeFilterButton.setOnClickListener(view -> removeAppliedFilter());
        intensitySeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                intensityText.setText("Filter intensity: " + progress + "%");
                if (fromUser && appliedFilter != null) {
                    appliedFilter.setFilterIntensity(progress / 100f);
                    refreshPreview();
                }
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
            }
        });
        initializePreviewHost();
    }

    private void initializePreviewHost() {
        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        if (!sdkManager.initialize()) {
            showUnavailablePreview("SDK initialization failed. Add the licensed SDK runtime.");
            return;
        }
        streamingContext = sdkManager.getStreamingContext();
        NvsLiveWindow liveWindow = new NvsLiveWindow(this);
        liveWindow.setFillMode(NvsLiveWindow.FILLMODE_PRESERVEASPECTFIT);
        FrameLayout previewStage = findViewById(R.id.materialPreviewStage);
        FrameLayout liveWindowContainer = findViewById(R.id.materialPreviewLiveWindowContainer);
        previewStage.addOnLayoutChangeListener(
                (view, left, top, right, bottom, oldLeft, oldTop, oldRight, oldBottom) ->
                        updatePreviewBounds(previewStage, liveWindowContainer));
        liveWindowContainer.addView(
                liveWindow,
                new FrameLayout.LayoutParams(
                        ViewGroup.LayoutParams.MATCH_PARENT,
                        ViewGroup.LayoutParams.MATCH_PARENT));

        MeisheTimelineController timelineController =
                new MeisheTimelineController(streamingContext);
        timeline = timelineController.createTimeline(PROJECT_WIDTH, PROJECT_HEIGHT);
        if (timeline == null) {
            showUnavailablePreview("Timeline creation failed.");
            return;
        }
        try {
            previewClip = timelineController.appendClip(resolvePreviewImage());
        } catch (IOException exception) {
            showUnavailablePreview("Preview image creation failed.");
            return;
        }
        if (previewClip == null
                || !streamingContext.connectTimelineWithLiveWindow(timeline, liveWindow)) {
            showUnavailablePreview("Timeline media could not be connected to LiveWindow.");
            return;
        }
        openMaterialCenterButton.setEnabled(true);
        refreshPreview();
        statusText.setText(
                "Preview ready. Open the material center, install a filter, and return it here.");
    }

    private void updatePreviewBounds(FrameLayout stage, FrameLayout previewContainer) {
        int availableWidth = stage.getWidth();
        int availableHeight = stage.getHeight();
        if (availableWidth <= 0 || availableHeight <= 0) {
            return;
        }
        int previewWidth = availableWidth;
        int previewHeight = Math.round(
                previewWidth * (PROJECT_HEIGHT / (float) PROJECT_WIDTH));
        if (previewHeight > availableHeight) {
            previewHeight = availableHeight;
            previewWidth = Math.round(
                    previewHeight * (PROJECT_WIDTH / (float) PROJECT_HEIGHT));
        }
        FrameLayout.LayoutParams layoutParams = new FrameLayout.LayoutParams(
                previewWidth,
                previewHeight,
                Gravity.CENTER);
        previewContainer.setLayoutParams(layoutParams);
    }

    private String resolvePreviewImage() throws IOException {
        try {
            return MeisheMediaFiles.copyAssetToProject(
                    this,
                    "sample/demo_base.jpg",
                    "asset_center_preview.jpg");
        } catch (IOException unavailableExternalSample) {
            return createGeneratedPreviewImage();
        }
    }

    private String createGeneratedPreviewImage() throws IOException {
        File directory = new File(getFilesDir(), "sample-media");
        if (!directory.isDirectory() && !directory.mkdirs()) {
            throw new IOException("Cannot create preview directory");
        }
        File output = new File(directory, "asset_center_generated_preview.png");
        if (output.isFile() && output.length() > 0) {
            return output.getAbsolutePath();
        }

        Bitmap bitmap = Bitmap.createBitmap(
                PROJECT_WIDTH,
                PROJECT_HEIGHT,
                Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(bitmap);
        Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        canvas.drawColor(Color.rgb(23, 28, 47));
        paint.setColor(Color.rgb(124, 92, 255));
        canvas.drawCircle(180f, 310f, 145f, paint);
        paint.setColor(Color.rgb(45, 212, 191));
        canvas.drawRect(330f, 180f, 650f, 610f, paint);
        paint.setColor(Color.rgb(255, 178, 92));
        canvas.drawCircle(360f, 940f, 230f, paint);
        try (FileOutputStream stream = new FileOutputStream(output)) {
            if (!bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream)) {
                throw new IOException("Cannot encode preview image");
            }
        } finally {
            bitmap.recycle();
        }
        if (!output.isFile() || output.length() == 0) {
            throw new IOException("Generated preview image is empty");
        }
        return output.getAbsolutePath();
    }

    private void openFilterPicker() {
        Intent intent = MeisheAssetCenterActivity.createPickerIntent(this);
        intent.putExtra(
                MeisheAssetCenterConfig.EXTRA_ASSET_TYPE,
                NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
        intent.putExtra(
                MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND,
                MeisheMaterialApplicationKind.FILTER);
        startActivityForResult(intent, REQUEST_FILTER_MATERIAL);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode != REQUEST_FILTER_MATERIAL
                || resultCode != RESULT_OK
                || data == null) {
            return;
        }
        String packageId = data.getStringExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_ID);
        String applicationKind = data.getStringExtra(
                MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND);
        String materialLabel = data.getStringExtra(
                MeisheAssetCenterConfig.EXTRA_MATERIAL_LABEL);
        if (packageId == null
                || packageId.isEmpty()
                || !MeisheMaterialApplicationKind.FILTER.equals(applicationKind)) {
            statusText.setText("No installed filter was returned.");
            return;
        }
        applyInstalledFilter(packageId, materialLabel);
    }

    private void applyInstalledFilter(String packageId, String materialLabel) {
        if (previewClip == null || streamingContext == null) {
            showUnavailablePreview("The Timeline preview is unavailable.");
            return;
        }
        if (appliedFilter != null && !previewClip.removeFx(appliedFilter.getIndex())) {
            statusText.setText("The previous filter could not be removed.");
            return;
        }
        appliedFilter = previewClip.appendPackagedFx(packageId);
        if (appliedFilter == null) {
            statusText.setText("The installed filter could not be applied to the Timeline clip.");
            intensitySeekBar.setEnabled(false);
            removeFilterButton.setEnabled(false);
            return;
        }
        appliedFilter.setFilterIntensity(intensitySeekBar.getProgress() / 100f);
        intensitySeekBar.setEnabled(true);
        removeFilterButton.setEnabled(true);
        refreshPreview();
        String label = materialLabel == null || materialLabel.isEmpty()
                ? packageId
                : materialLabel;
        statusText.setText("Applied filter to the sample Timeline clip: " + label);
    }

    private void removeAppliedFilter() {
        if (previewClip == null || appliedFilter == null) {
            return;
        }
        if (!previewClip.removeFx(appliedFilter.getIndex())) {
            statusText.setText("The applied filter could not be removed.");
            return;
        }
        appliedFilter = null;
        intensitySeekBar.setEnabled(false);
        removeFilterButton.setEnabled(false);
        refreshPreview();
        statusText.setText("Filter removed from the sample Timeline clip.");
    }

    private void refreshPreview() {
        if (streamingContext == null || timeline == null) {
            return;
        }
        streamingContext.stop();
        streamingContext.seekTimeline(
                timeline,
                0,
                NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE,
                0);
    }

    private void showUnavailablePreview(String message) {
        statusText.setText(message);
        openMaterialCenterButton.setEnabled(false);
        intensitySeekBar.setEnabled(false);
        removeFilterButton.setEnabled(false);
    }

    @Override
    protected void onPause() {
        if (streamingContext != null) {
            streamingContext.stop();
        }
        super.onPause();
    }

    @Override
    protected void onDestroy() {
        if (streamingContext != null && timeline != null) {
            streamingContext.stop();
            streamingContext.removeTimeline(timeline);
        }
        timeline = null;
        previewClip = null;
        appliedFilter = null;
        super.onDestroy();
    }
}
