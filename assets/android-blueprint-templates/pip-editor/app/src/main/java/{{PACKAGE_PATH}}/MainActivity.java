package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.ClipData;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.TextView;

import java.io.IOException;
import java.util.ArrayList;

public class MainActivity extends Activity {
    private static final int REQUEST_PIP_MEDIA = 4101;
    private TextView statusText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        MeisheAppSupport.applySystemBarInsets(this);
        statusText = findViewById(R.id.statusText);
        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        boolean ready = sdkManager.initialize();
        statusText.setText(ready
                ? "SDK ready. Open the bundled two-track PIP or choose media."
                : "SDK initialization failed. Add license, jar, and native libraries.");
        findViewById(R.id.primaryButton).setEnabled(ready);
        findViewById(R.id.secondaryButton).setEnabled(ready);
        findViewById(R.id.primaryButton).setOnClickListener(v -> openPip(new ArrayList<>()));
        findViewById(R.id.secondaryButton).setOnClickListener(v -> selectPipMedia());
    }

    private void selectPipMedia() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.setType("*/*");
        intent.putExtra(Intent.EXTRA_MIME_TYPES, new String[]{"video/*", "image/*"});
        intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        startActivityForResult(intent, REQUEST_PIP_MEDIA);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode != REQUEST_PIP_MEDIA || resultCode != RESULT_OK || data == null) {
            return;
        }
        ArrayList<String> paths = new ArrayList<>();
        try {
            ClipData clipData = data.getClipData();
            if (clipData != null) {
                for (int index = 0; index < clipData.getItemCount() && paths.size() < 2; index++) {
                    paths.add(MeisheMediaFiles.copyContentUriToCache(
                            this,
                            clipData.getItemAt(index).getUri()));
                }
            } else {
                Uri uri = data.getData();
                if (uri != null) {
                    paths.add(MeisheSampleAssets.SAMPLE_IMAGE_PATH);
                    paths.add(MeisheMediaFiles.copyContentUriToCache(this, uri));
                }
            }
        } catch (IOException error) {
            statusText.setText("Selected media could not be copied: " + error.getMessage());
            return;
        }
        openPip(paths);
    }

    private void openPip(ArrayList<String> paths) {
        startActivity(MeisheRuntimeDemoActivity.createIntent(
                this,
                MeisheRuntimeDemoActivity.MODE_PIP,
                paths));
    }
}
