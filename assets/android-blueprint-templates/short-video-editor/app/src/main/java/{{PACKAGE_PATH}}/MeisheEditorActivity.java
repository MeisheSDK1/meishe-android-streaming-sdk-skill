package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;

import java.util.ArrayList;
import java.util.UUID;

public class MeisheEditorActivity extends Activity {
    private static final String EXTRA_MEDIA_PATHS = "meishe.editorMediaPaths";
    private static final String EXTRA_WIDTH = "meishe.editorWidth";
    private static final String EXTRA_HEIGHT = "meishe.editorHeight";
    private static final String EXTRA_PROJECT_ID = "meishe.editorProjectId";
    private static final String EXTRA_RESUME = "meishe.editorResume";

    private MeisheEditorCoordinator coordinator;

    public static Intent createIntent(
            Context context,
            ArrayList<String> mediaPaths,
            int width,
            int height) {
        Intent intent = new Intent(context, MeisheEditorActivity.class);
        intent.putStringArrayListExtra(
                EXTRA_MEDIA_PATHS,
                mediaPaths == null ? new ArrayList<>() : new ArrayList<>(mediaPaths));
        intent.putExtra(EXTRA_WIDTH, width);
        intent.putExtra(EXTRA_HEIGHT, height);
        intent.putExtra(EXTRA_PROJECT_ID, UUID.randomUUID().toString());
        return intent;
    }

    public static Intent createResumeIntent(Context context) {
        MeisheEditorProjectRepository repository = new MeisheEditorProjectRepository(context);
        String latestProjectId = repository.latestProjectId();
        MeisheEditorProject project = repository.loadExistingOrMigrate(
                latestProjectId,
                720,
                1280);
        if (project == null) {
            return null;
        }
        Intent intent = new Intent(context, MeisheEditorActivity.class);
        intent.putExtra(EXTRA_PROJECT_ID, latestProjectId);
        intent.putExtra(EXTRA_RESUME, true);
        intent.putExtra(EXTRA_WIDTH, project.width());
        intent.putExtra(EXTRA_HEIGHT, project.height());
        return intent;
    }

    public static void attachInitialMaterial(
            Intent intent,
            String packageId,
            int packageType,
            String localAssetPath,
            String applicationKind,
            String materialLabel) {
        if (intent == null) {
            return;
        }
        intent.putExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_ID, packageId);
        intent.putExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_TYPE, packageType);
        intent.putExtra(MeisheAssetCenterConfig.EXTRA_LOCAL_ASSET_PATH, localAssetPath);
        intent.putExtra(MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND, applicationKind);
        intent.putExtra(MeisheAssetCenterConfig.EXTRA_MATERIAL_LABEL, materialLabel);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        String projectId = getIntent().getStringExtra(EXTRA_PROJECT_ID);
        if (projectId == null || projectId.isEmpty()) {
            projectId = UUID.randomUUID().toString();
        }
        coordinator = new MeisheEditorCoordinator(
                this,
                getIntent().getStringArrayListExtra(EXTRA_MEDIA_PATHS),
                getIntent().getIntExtra(EXTRA_WIDTH, 720),
                getIntent().getIntExtra(EXTRA_HEIGHT, 1280),
                projectId,
                getIntent().getBooleanExtra(EXTRA_RESUME, false));
        coordinator.onCreate(savedInstanceState);
        if (savedInstanceState == null) {
            coordinator.applyInitialMaterial(
                    getIntent().getStringExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_ID),
                    getIntent().getIntExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_TYPE, -1),
                    getIntent().getStringExtra(MeisheAssetCenterConfig.EXTRA_LOCAL_ASSET_PATH),
                    getIntent().getStringExtra(MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND),
                    getIntent().getStringExtra(MeisheAssetCenterConfig.EXTRA_MATERIAL_LABEL));
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (coordinator != null) {
            coordinator.onActivityResult(requestCode, resultCode, data);
        }
    }

    @Override
    public void onRequestPermissionsResult(
            int requestCode,
            String[] permissions,
            int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (coordinator != null) {
            coordinator.onRequestPermissionsResult(requestCode, grantResults);
        }
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        if (coordinator != null) {
            coordinator.onSaveInstanceState(outState);
        }
        super.onSaveInstanceState(outState);
    }

    @Override
    protected void onPause() {
        if (coordinator != null) {
            coordinator.onPause();
        }
        super.onPause();
    }

    @Override
    protected void onDestroy() {
        if (coordinator != null) {
            coordinator.onDestroy();
            coordinator = null;
        }
        super.onDestroy();
    }
}
