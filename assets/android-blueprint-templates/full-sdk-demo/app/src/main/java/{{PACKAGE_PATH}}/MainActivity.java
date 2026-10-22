package {{PACKAGE_NAME}};

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;

public class MainActivity extends Activity {
    private boolean sdkReady;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        MeisheAppSupport.applySystemBarInsets(this);
        TextView statusText = findViewById(R.id.statusText);
        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        sdkReady = sdkManager.initialize();
        if (sdkReady) {
            MeisheAssetInstaller installer = new MeisheAssetInstaller(
                    sdkManager.getStreamingContext());
            Map<String, String> packageIds = MeisheSampleAssets.installDefaultPackages(installer);
            statusText.setText(
                    "SDK ready. Timeline editing and LiveWindow preview are available. Installed "
                            + packageIds.size() + " local sample packages.");
        } else {
            statusText.setText("SDK initialization failed. Check license, JAR, and native libraries.");
        }
        setEntriesEnabled(sdkReady);
        findViewById(R.id.editorButton).setOnClickListener(v ->
                startActivity(new Intent(this, MediaPickerActivity.class)));
        findViewById(R.id.sampleEditorButton).setOnClickListener(v -> openSampleEditor());
        findViewById(R.id.resumeEditorButton).setOnClickListener(v -> resumeLatestEditorProject());
        findViewById(R.id.captureButton).setOnClickListener(v ->
                openMode(MeisheRuntimeDemoActivity.MODE_CAPTURE));
        findViewById(R.id.pipButton).setOnClickListener(v ->
                openMode(MeisheRuntimeDemoActivity.MODE_PIP));
        findViewById(R.id.spliceButton).setOnClickListener(v ->
                startActivity(MediaPickerActivity.createQuickSpliceIntent(this)));
        findViewById(R.id.materialButton).setOnClickListener(v ->
                startActivity(MeisheAssetCenterActivity.createIntent(this)));
        findViewById(R.id.resourceButton).setOnClickListener(v -> showAdvancedResourceGuide());
    }

    private void openSampleEditor() {
        TextView statusText = findViewById(R.id.statusText);
        try {
            ArrayList<String> mediaPaths = new ArrayList<>();
            mediaPaths.add(MeisheMediaFiles.copyAssetToProject(
                    this,
                    "sample/demo_base.jpg",
                    "demo_base.jpg"));
            mediaPaths.add(MeisheMediaFiles.copyAssetToProject(
                    this,
                    "sample/demo_overlay.jpg",
                    "demo_overlay.jpg"));
            startActivity(MeisheEditorActivity.createIntent(this, mediaPaths, 720, 1280));
        } catch (IOException exception) {
            statusText.setText("Local sample media is unavailable: " + exception.getMessage());
        }
    }

    private void resumeLatestEditorProject() {
        Intent resumeIntent = MeisheEditorActivity.createResumeIntent(this);
        if (resumeIntent != null) {
            startActivity(resumeIntent);
            return;
        }
        ((TextView) findViewById(R.id.statusText)).setText("No saved project is available.");
    }

    private void openMode(String mode) {
        startActivity(MeisheRuntimeDemoActivity.createIntent(this, mode));
    }

    private void showAdvancedResourceGuide() {
        new AlertDialog.Builder(this)
                .setTitle("Advanced resources and usage")
                .setMessage(
                        "R8 Template / Mimo / CutSame resources power template-based creation.\n\n"
                                + "R9 AR / makeup / segmentation resources power live camera preview.\n\n"
                                + "R10-R12 album / theme / extension packages must be applied from their matching editor or capture module after installation.\n\n"
                                + "These resources are not bundled in the Skill. Contact Meishe sales for SDK artifacts, licenses, models, and packages matched to your authorization.")
                .setPositiveButton("Open material center", (dialog, which) ->
                        startActivity(MeisheAssetCenterActivity.createIntent(this)))
                .setNegativeButton("Close", null)
                .show();
    }

    private void setEntriesEnabled(boolean enabled) {
        int[] ids = {
                R.id.editorButton,
                R.id.sampleEditorButton,
                R.id.resumeEditorButton,
                R.id.captureButton,
                R.id.pipButton,
                R.id.spliceButton,
                R.id.materialButton,
                R.id.resourceButton
        };
        for (int id : ids) {
            findViewById(id).setEnabled(enabled);
        }
        findViewById(R.id.resumeEditorButton).setEnabled(
                enabled && MeisheEditorActivity.createResumeIntent(this) != null);
    }

    @Override
    protected void onResume() {
        super.onResume();
        findViewById(R.id.resumeEditorButton).setEnabled(
                sdkReady && MeisheEditorActivity.createResumeIntent(this) != null);
    }
}
