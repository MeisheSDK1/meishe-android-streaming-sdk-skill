package {{PACKAGE_NAME}};

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;
import android.view.View;

import com.meicam.sdk.NvsAssetPackageManager;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class MeisheAssetCenterActivity extends Activity {
    private final List<MeisheLocalMaterialCatalog.Entry> visibleEntries = new ArrayList<>();

    private MeisheSdkManager sdkManager;
    private MeisheAssetInstaller assetInstaller;
    private ArrayAdapter<MeisheLocalMaterialCatalog.Entry> materialAdapter;
    private Spinner familySpinner;
    private TextView statusText;
    private Button installButton;
    private Button applyButton;
    private int selectedIndex = -1;
    private Intent pendingMaterialResult;
    private MeisheLocalMaterialCatalog.Entry installedEntry;
    private String requestedApplicationKind = "";

    public static Intent createIntent(Context context) {
        return new Intent(context, MeisheAssetCenterActivity.class);
    }

    public static Intent createPickerIntent(Context context) {
        return createIntent(context).putExtra(MeisheAssetCenterConfig.EXTRA_PICK_MODE, true);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_meishe_asset_center);
        MeisheAppSupport.applySystemBarInsets(this);

        familySpinner = findViewById(R.id.assetTypeSpinner);
        statusText = findViewById(R.id.assetStatusText);
        installButton = findViewById(R.id.installAssetButton);
        applyButton = findViewById(R.id.applyAssetButton);
        String requestedKind = getIntent().getStringExtra(
                MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND);
        requestedApplicationKind = requestedKind == null ? "" : requestedKind;
        bindFamilies();
        bindMaterials();

        sdkManager = new MeisheSdkManager(getApplicationContext());
        if (sdkManager.initialize()) {
            assetInstaller = new MeisheAssetInstaller(sdkManager.getStreamingContext());
            setStatus("Local materials are ready. Install or register one, then use it.");
        } else {
            installButton.setEnabled(false);
            setStatus("SDK initialization failed. Add the licensed SDK runtime before installing packages.");
        }

        findViewById(R.id.showAssetFamilyButton).setOnClickListener(view -> showSelectedFamily());
        installButton.setOnClickListener(view -> installSelectedMaterial());
        applyButton.setOnClickListener(view -> useInstalledMaterial());
        selectRequestedAssetType();
        showSelectedFamily();
    }

    private void bindFamilies() {
        familySpinner.setAdapter(new ArrayAdapter<>(
                this,
                android.R.layout.simple_spinner_dropdown_item,
                MeisheLocalMaterialCatalog.familyLabels()));
    }

    private void bindMaterials() {
        ListView materialList = findViewById(R.id.assetList);
        materialAdapter = new ArrayAdapter<>(
                this,
                android.R.layout.simple_list_item_activated_1,
                visibleEntries);
        materialList.setChoiceMode(ListView.CHOICE_MODE_SINGLE);
        materialList.setAdapter(materialAdapter);
        materialList.setOnItemClickListener((parent, view, position, id) -> {
            selectedIndex = position;
            pendingMaterialResult = null;
            installedEntry = null;
            applyButton.setVisibility(View.GONE);
            installButton.setEnabled(assetInstaller != null);
            MeisheLocalMaterialCatalog.Entry entry = visibleEntries.get(position);
            setStatus("Selected: " + entry.label
                    + "\n" + "Application requirement: " + entry.applicationRequirement
                    + "\n" + "Editable after applying: " + entry.editableProperties);
        });
    }

    private void selectRequestedAssetType() {
        int requestedType = getIntent().getIntExtra(MeisheAssetCenterConfig.EXTRA_ASSET_TYPE, -1);
        if (requestedType < 0) {
            return;
        }
        List<String> families = MeisheLocalMaterialCatalog.familiesForPackageType(requestedType);
        if (!families.isEmpty()) {
            int position = MeisheLocalMaterialCatalog.familyLabels().indexOf(families.get(0));
            familySpinner.setSelection(Math.max(position, 0));
        }
    }

    private void showSelectedFamily() {
        String family = String.valueOf(familySpinner.getSelectedItem());
        int requestedType = getIntent().getIntExtra(
                MeisheAssetCenterConfig.EXTRA_ASSET_TYPE,
                -1);
        visibleEntries.clear();
        for (MeisheLocalMaterialCatalog.Entry entry
                : MeisheLocalMaterialCatalog.entriesForFamily(family)) {
            boolean packageMatches = requestedType < 0 || requestedType == entry.packageType;
            boolean applicationMatches = requestedApplicationKind.isEmpty()
                    || requestedApplicationKind.equals(entry.applicationKind);
            if (packageMatches && applicationMatches) {
                visibleEntries.add(entry);
            }
        }
        selectedIndex = -1;
        installButton.setEnabled(false);
        pendingMaterialResult = null;
        installedEntry = null;
        applyButton.setVisibility(View.GONE);
        materialAdapter.notifyDataSetChanged();
        if (visibleEntries.isEmpty()
                && requestedType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP) {
            setStatus("No authorized Makeup package is available locally. Contact Meishe business to obtain material resources.");
        } else {
            setStatus("Local " + family + ": " + visibleEntries.size());
        }
    }

    private void installSelectedMaterial() {
        if (assetInstaller == null || selectedIndex < 0 || selectedIndex >= visibleEntries.size()) {
            return;
        }
        MeisheLocalMaterialCatalog.Entry entry = visibleEntries.get(selectedIndex);
        if (entry.isFont()) {
            registerFont(entry);
            return;
        }
        String packageId = MeisheLocalMaterialOperations.installBundledPackage(
                assetInstaller,
                entry.packagePath,
                entry.licensePath,
                entry.packageType);
        if (packageId == null || packageId.isEmpty()) {
            setStatus("Install failed. Verify SDK capability, local files, and package authorization.");
            return;
        }
        Intent result = new Intent();
        result.putExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_ID, packageId);
        result.putExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_TYPE, entry.packageType);
        result.putExtra(MeisheAssetCenterConfig.EXTRA_RESOURCE_KIND, entry.family);
        attachApplicationContract(result, entry);
        prepareMaterialUsage(entry, result, "Installed " + entry.label + "\nPackage id: " + packageId);
    }

    private void registerFont(MeisheLocalMaterialCatalog.Entry entry) {
        try {
            String assetPath = entry.packagePath.startsWith("assets:/")
                    ? entry.packagePath.substring("assets:/".length())
                    : entry.packagePath;
            String fileName = new File(assetPath).getName();
            String localPath = MeisheMediaFiles.copyAssetToProject(this, assetPath, fileName);
            String family = MeisheLocalMaterialOperations.registerBundledFont(
                    sdkManager.getStreamingContext(),
                    localPath);
            if (family.isEmpty()) {
                setStatus("Font registration failed.");
                return;
            }
            Intent result = new Intent();
            result.putExtra(MeisheAssetCenterConfig.EXTRA_LOCAL_ASSET_PATH, localPath);
            result.putExtra(MeisheAssetCenterConfig.EXTRA_RESOURCE_KIND, entry.family);
            result.putExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_ID, family);
            result.putExtra(MeisheAssetCenterConfig.EXTRA_PACKAGE_TYPE, entry.packageType);
            attachApplicationContract(result, entry);
            prepareMaterialUsage(entry, result, "Registered " + entry.label + "\nFont family: " + family);
        } catch (IOException exception) {
            setStatus("Font copy failed: " + exception.getMessage());
        }
    }

    private void setStatus(String message) {
        statusText.setText(message);
    }

    private void prepareMaterialUsage(
            MeisheLocalMaterialCatalog.Entry entry,
            Intent result,
            String message) {
        installedEntry = entry;
        pendingMaterialResult = result;
        applyButton.setEnabled(true);
        applyButton.setVisibility(View.VISIBLE);
        boolean pickerMode = getIntent().getBooleanExtra(
                MeisheAssetCenterConfig.EXTRA_PICK_MODE,
                false);
        applyButton.setText(pickerMode
                ? "Return selected material"
                : isCaptureMaterial(entry.packageType)
                        ? "Apply to camera preview"
                        : "Use in a sample editor project");
        setStatus(message
                + "\n" + "Application requirement: " + entry.applicationRequirement
                + "\n" + "Editable properties: " + entry.editableProperties
                + "\nNext: tap the button below to actually use this material.");
    }

    private void useInstalledMaterial() {
        if (pendingMaterialResult == null || installedEntry == null) {
            setStatus("Install or register a material first.");
            return;
        }
        if (getIntent().getBooleanExtra(MeisheAssetCenterConfig.EXTRA_PICK_MODE, false)) {
            setResult(RESULT_OK, pendingMaterialResult);
            finish();
            return;
        }
        if (!launchOptionalMaterialWorkflow()) {
            setStatus("The material is installed. Open this center from an editor or camera module to apply it.");
        }
    }

    private boolean launchOptionalMaterialWorkflow() {
        String packageId = pendingMaterialResult.getStringExtra(
                MeisheAssetCenterConfig.EXTRA_PACKAGE_ID);
        int packageType = pendingMaterialResult.getIntExtra(
                MeisheAssetCenterConfig.EXTRA_PACKAGE_TYPE,
                -1);
        try {
            if (isCaptureMaterial(packageType)) {
                Class<?> runtimeClass = Class.forName(getPackageName() + ".MeisheRuntimeDemoActivity");
                java.lang.reflect.Method factory = runtimeClass.getMethod(
                        "createCaptureIntentWithMaterial",
                        Context.class,
                        String.class,
                        int.class);
                startActivity((Intent) factory.invoke(null, this, packageId, packageType));
                return true;
            }
            ArrayList<String> mediaPaths = new ArrayList<>();
            mediaPaths.add(MeisheMediaFiles.copyAssetToProject(
                    this,
                    "sample/demo_base.jpg",
                    "material_demo_base.jpg"));
            mediaPaths.add(MeisheMediaFiles.copyAssetToProject(
                    this,
                    "sample/demo_overlay.jpg",
                    "material_demo_overlay.jpg"));
            Class<?> editorClass = Class.forName(getPackageName() + ".MeisheEditorActivity");
            java.lang.reflect.Method factory = editorClass.getMethod(
                    "createIntent",
                    Context.class,
                    ArrayList.class,
                    int.class,
                    int.class);
            Intent editorIntent = (Intent) factory.invoke(null, this, mediaPaths, 720, 1280);
            java.lang.reflect.Method attach = editorClass.getMethod(
                    "attachInitialMaterial",
                    Intent.class,
                    String.class,
                    int.class,
                    String.class,
                    String.class,
                    String.class);
            attach.invoke(
                    null,
                    editorIntent,
                    packageId,
                    packageType,
                    pendingMaterialResult.getStringExtra(
                            MeisheAssetCenterConfig.EXTRA_LOCAL_ASSET_PATH),
                    installedEntry.applicationKind,
                    installedEntry.label);
            startActivity(editorIntent);
            return true;
        } catch (Exception exception) {
            return false;
        }
    }

    private boolean isCaptureMaterial(int packageType) {
        return packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE
                || packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE
                || packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH
                || packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_MAKEUP;
    }

    private void attachApplicationContract(
            Intent result,
            MeisheLocalMaterialCatalog.Entry entry) {
        result.putExtra(MeisheAssetCenterConfig.EXTRA_MATERIAL_KEY, entry.materialKey);
        result.putExtra(MeisheAssetCenterConfig.EXTRA_MATERIAL_LABEL, entry.label);
        result.putExtra(MeisheAssetCenterConfig.EXTRA_APPLICATION_KIND, entry.applicationKind);
    }
}
