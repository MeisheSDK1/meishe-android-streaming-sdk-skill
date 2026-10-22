package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        MeisheAppSupport.applySystemBarInsets(this);
        TextView statusText = findViewById(R.id.statusText);
        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        boolean ready = sdkManager.initialize();
        statusText.setText(ready
                ? "SDK ready. Choose capture or timeline editing."
                : "SDK initialization failed. Add license, jar, and native libraries.");
        findViewById(R.id.primaryButton).setEnabled(ready);
        findViewById(R.id.secondaryButton).setEnabled(ready);
        findViewById(R.id.primaryButton).setOnClickListener(v -> startActivity(
                MeisheRuntimeDemoActivity.createIntent(this, MeisheRuntimeDemoActivity.MODE_CAPTURE)));
        findViewById(R.id.secondaryButton).setOnClickListener(v -> startActivity(
                MeisheRuntimeDemoActivity.createIntent(this, MeisheRuntimeDemoActivity.MODE_EDITOR)));
    }
}
