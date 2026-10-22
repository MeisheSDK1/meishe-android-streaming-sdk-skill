package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.TextView;

import java.io.IOException;

public class MainActivity extends Activity {
    private static final int REQUEST_TEMPLATE = 4301;
    private static final int REQUEST_FOOTAGE = 4302;
    private TextView statusText;
    private String templatePath;
    private String footagePath;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        MeisheAppSupport.applySystemBarInsets(this);
        statusText = findViewById(R.id.statusText);
        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        boolean ready = sdkManager.initialize();
        statusText.setText(ready
                ? "SDK ready. Select a template package and replacement footage, or open the material center."
                : "SDK initialization failed. Add license, jar, and native libraries.");
        findViewById(R.id.primaryButton).setEnabled(ready);
        findViewById(R.id.secondaryButton).setEnabled(ready);
        findViewById(R.id.materialButton).setEnabled(ready);
        findViewById(R.id.primaryButton).setOnClickListener(v -> selectFile(REQUEST_TEMPLATE, "*/*", false));
        findViewById(R.id.secondaryButton).setOnClickListener(v -> selectFile(REQUEST_FOOTAGE, "*/*", true));
        findViewById(R.id.materialButton).setOnClickListener(v ->
                startActivity(MeisheAssetCenterActivity.createIntent(this)));
    }

    private void selectFile(int requestCode, String type, boolean mediaOnly) {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.setType(type);
        if (mediaOnly) {
            intent.putExtra(Intent.EXTRA_MIME_TYPES, new String[]{"video/*", "image/*"});
        }
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        startActivityForResult(intent, requestCode);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (resultCode != RESULT_OK || data == null || data.getData() == null) {
            return;
        }
        Uri uri = data.getData();
        try {
            String path = MeisheMediaFiles.copyContentUriToCache(this, uri);
            if (requestCode == REQUEST_TEMPLATE) {
                templatePath = path;
            } else if (requestCode == REQUEST_FOOTAGE) {
                footagePath = path;
            } else {
                return;
            }
        } catch (IOException error) {
            statusText.setText("Selected resource could not be copied: " + error.getMessage());
            return;
        }
        if (templatePath != null && footagePath != null) {
            statusText.setText("Template and footage are staged. A matching template descriptor/package ID is still required before createTimeline(templateId, footage).");
        } else if (templatePath != null) {
            statusText.setText("Template staged. Select replacement footage next.");
        } else {
            statusText.setText("Footage staged. Select a matching template package next.");
        }
    }
}
