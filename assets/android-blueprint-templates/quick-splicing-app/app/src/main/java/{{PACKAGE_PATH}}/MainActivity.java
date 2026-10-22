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
    private static final int REQUEST_SPLICE_MEDIA = 4201;
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
                ? "SDK ready. Build a sample splice or select two or more clips."
                : "SDK initialization failed. Add license, jar, and native libraries.");
        findViewById(R.id.primaryButton).setEnabled(ready);
        findViewById(R.id.secondaryButton).setEnabled(ready);
        findViewById(R.id.primaryButton).setOnClickListener(v -> selectClips());
        findViewById(R.id.secondaryButton).setOnClickListener(v -> openSplice(new ArrayList<>()));
    }

    private void selectClips() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.setType("*/*");
        intent.putExtra(Intent.EXTRA_MIME_TYPES, new String[]{"video/*", "image/*"});
        intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        startActivityForResult(intent, REQUEST_SPLICE_MEDIA);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode != REQUEST_SPLICE_MEDIA || resultCode != RESULT_OK || data == null) {
            return;
        }
        ArrayList<String> paths = new ArrayList<>();
        try {
            ClipData clipData = data.getClipData();
            if (clipData != null) {
                for (int index = 0; index < clipData.getItemCount(); index++) {
                    paths.add(MeisheMediaFiles.copyContentUriToCache(
                            this,
                            clipData.getItemAt(index).getUri()));
                }
            } else {
                Uri uri = data.getData();
                if (uri != null) {
                    paths.add(MeisheMediaFiles.copyContentUriToCache(this, uri));
                }
            }
        } catch (IOException error) {
            statusText.setText("Selected media could not be copied: " + error.getMessage());
            return;
        }
        if (paths.size() < 2) {
            statusText.setText("Select at least two clips, or use the bundled sample splice.");
            return;
        }
        openSplice(paths);
    }

    private void openSplice(ArrayList<String> paths) {
        startActivity(MeisheRuntimeDemoActivity.createIntent(
                this,
                MeisheRuntimeDemoActivity.MODE_QUICK_SPLICE,
                paths));
    }
}
