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
        if (!sdkManager.initialize()) {
            statusText.setText("SDK initialization failed. Check license, JAR/AAR, and native libraries.");
            return;
        }
        statusText.setText("SDK ready. Select a blueprint or modules to generate a product workflow.");
    }
}
