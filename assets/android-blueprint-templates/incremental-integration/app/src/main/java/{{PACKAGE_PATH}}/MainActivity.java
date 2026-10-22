package {{PACKAGE_NAME}};

import android.app.Activity;
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
        statusText.setText(sdkManager.initialize()
                ? "SDK runtime initialized. Use --mode incremental to stage controllers and patch-manifest.json without replacing the host UI."
                : "SDK initialization failed. The host patch still requires license, jar, and native libraries.");
    }
}
