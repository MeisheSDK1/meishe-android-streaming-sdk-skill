package {{PACKAGE_NAME}};

import android.app.Activity;
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

        TextView statusText = findViewById(R.id.homeStatusText);
        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        if (!sdkManager.initialize()) {
            statusText.setText("SDK initialization failed. Check license, JAR/AAR, and native libraries.");
            setEntriesEnabled(false);
            return;
        }

        MeisheAssetInstaller installer = new MeisheAssetInstaller(sdkManager.getStreamingContext());
        Map<String, String> packageIds = MeisheSampleAssets.installDefaultPackages(installer);
        sdkReady = true;
        statusText.setText("SDK ready. Local sample packages installed: " + packageIds.size());

        findViewById(R.id.createProjectButton).setOnClickListener(v ->
                startActivity(new Intent(this, MediaPickerActivity.class)));
        Intent resumeIntent = MeisheEditorActivity.createResumeIntent(this);
        findViewById(R.id.resumeProjectButton).setEnabled(resumeIntent != null);
        findViewById(R.id.resumeProjectButton).setOnClickListener(v -> {
            Intent latest = MeisheEditorActivity.createResumeIntent(this);
            if (latest != null) {
                startActivity(latest);
            } else {
                statusText.setText("No saved project is available.");
            }
        });
        findViewById(R.id.sampleProjectButton).setOnClickListener(v -> openSampleProject());
        findViewById(R.id.materialCenterButton).setOnClickListener(v ->
                startActivity(MeisheAssetCenterActivity.createIntent(this)));
    }

    private void openSampleProject() {
        try {
            String samplePath = MeisheMediaFiles.copyAssetToProject(
                    this,
                    "sample/demo_base.jpg",
                    "demo_base.jpg");
            ArrayList<String> paths = new ArrayList<>();
            paths.add(samplePath);
            Intent intent = MeisheEditorActivity.createIntent(this, paths, 720, 1280);
            startActivity(intent);
        } catch (IOException exception) {
            TextView statusText = findViewById(R.id.homeStatusText);
            statusText.setText("Local sample media is unavailable: " + exception.getMessage());
        }
    }

    private void setEntriesEnabled(boolean enabled) {
        findViewById(R.id.createProjectButton).setEnabled(enabled);
        findViewById(R.id.resumeProjectButton).setEnabled(enabled
                && MeisheEditorActivity.createResumeIntent(this) != null);
        findViewById(R.id.sampleProjectButton).setEnabled(enabled);
        findViewById(R.id.materialCenterButton).setEnabled(enabled);
    }

    @Override
    protected void onResume() {
        super.onResume();
        findViewById(R.id.resumeProjectButton).setEnabled(
                sdkReady && MeisheEditorActivity.createResumeIntent(this) != null);
    }
}
