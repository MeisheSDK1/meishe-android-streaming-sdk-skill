package {{PACKAGE_NAME}};

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.ClipData;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.view.View;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MediaPickerActivity extends Activity {
    private static final int REQUEST_MEDIA = 51;
    private static final String EXTRA_QUICK_SPLICE = "meishe.quickSplice";
    private static final String[] RATIO_LABELS = {"16:9 landscape", "9:16 portrait", "1:1 square"};
    private static final int[][] RATIO_SIZES = {{1280, 720}, {720, 1280}, {720, 720}};

    private final ExecutorService importExecutor = Executors.newSingleThreadExecutor();
    private final ArrayList<String> selectedPaths = new ArrayList<>();
    private final List<String> selectedNames = new ArrayList<>();

    private ArrayAdapter<String> mediaAdapter;
    private MeisheMediaProbeController mediaProbeController;
    private TextView statusText;
    private Button selectButton;
    private Button continueButton;
    private Button moveEarlierButton;
    private Button moveLaterButton;
    private boolean quickSpliceMode;
    private int selectedMediaIndex = -1;

    public static Intent createQuickSpliceIntent(Context context) {
        return new Intent(context, MediaPickerActivity.class)
                .putExtra(EXTRA_QUICK_SPLICE, true);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_media_picker);
        MeisheAppSupport.applySystemBarInsets(this);

        statusText = findViewById(R.id.mediaPickerStatusText);
        selectButton = findViewById(R.id.selectMediaButton);
        continueButton = findViewById(R.id.continueToEditorButton);
        moveEarlierButton = findViewById(R.id.moveMediaEarlierButton);
        moveLaterButton = findViewById(R.id.moveMediaLaterButton);
        quickSpliceMode = getIntent().getBooleanExtra(EXTRA_QUICK_SPLICE, false);
        if (quickSpliceMode) {
            ((TextView) findViewById(R.id.mediaPickerTitle)).setText("Create a quick splice");
            ((TextView) findViewById(R.id.mediaPickerSubtitle)).setText(
                    "Choose at least two items, select a row, then adjust the splice order.");
            continueButton.setText("Choose ratio and preview splice");
            moveEarlierButton.setVisibility(View.VISIBLE);
            moveLaterButton.setVisibility(View.VISIBLE);
        }
        ListView selectedMediaList = findViewById(R.id.selectedMediaList);
        mediaAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, selectedNames);
        selectedMediaList.setAdapter(mediaAdapter);
        selectedMediaList.setChoiceMode(ListView.CHOICE_MODE_SINGLE);
        selectedMediaList.setOnItemClickListener((parent, view, position, id) -> {
            selectedMediaIndex = position;
            updateReorderControls();
            if (quickSpliceMode) {
                statusText.setText("Selected clip " + (position + 1)
                        + ". Use the buttons below to adjust the splice order.");
            }
        });
        selectedMediaList.setOnItemLongClickListener((parent, view, position, id) -> {
            if (position < 0 || position >= selectedPaths.size()) {
                return false;
            }
            File removed = new File(selectedPaths.remove(position));
            selectedNames.remove(position);
            selectedMediaIndex = -1;
            mediaAdapter.notifyDataSetChanged();
            updateContinueButton();
            updateReorderControls();
            if (removed.isFile()) {
                removed.delete();
            }
            statusText.setText("Removed " + removed.getName() + ". "
                    + selectedPaths.size() + " items remain.");
            return true;
        });

        MeisheSdkManager sdkManager = new MeisheSdkManager(getApplicationContext());
        if (!sdkManager.initialize()) {
            setBusy(true, "SDK initialization failed.");
            return;
        }
        mediaProbeController = new MeisheMediaProbeController(sdkManager.getStreamingContext());
        selectButton.setOnClickListener(v -> launchMediaPicker());
        continueButton.setOnClickListener(v -> chooseRatio());
        moveEarlierButton.setOnClickListener(v -> moveSelectedMedia(-1));
        moveLaterButton.setOnClickListener(v -> moveSelectedMedia(1));
        updateReorderControls();
    }

    private void launchMediaPicker() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("*/*");
        intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
        intent.putExtra(Intent.EXTRA_MIME_TYPES, new String[]{"video/*", "image/*"});
        startActivityForResult(intent, REQUEST_MEDIA);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode != REQUEST_MEDIA || resultCode != RESULT_OK || data == null) {
            return;
        }
        List<Uri> uris = collectUris(data);
        if (uris.isEmpty()) {
            statusText.setText("No media was selected.");
            return;
        }
        setBusy(true, "Importing " + uris.size() + " selected items...");
        importExecutor.execute(() -> importUris(uris));
    }

    private List<Uri> collectUris(Intent data) {
        List<Uri> uris = new ArrayList<>();
        ClipData clipData = data.getClipData();
        if (clipData != null) {
            for (int index = 0; index < clipData.getItemCount(); index++) {
                Uri uri = clipData.getItemAt(index).getUri();
                if (uri != null) {
                    uris.add(uri);
                }
            }
        } else if (data.getData() != null) {
            uris.add(data.getData());
        }
        return uris;
    }

    private void importUris(List<Uri> uris) {
        List<File> imported = new ArrayList<>();
        List<String> failures = new ArrayList<>();
        for (Uri uri : uris) {
            try {
                imported.add(MeisheMediaImporter.copyToProjectFile(this, uri));
            } catch (Exception exception) {
                failures.add(exception.getMessage() == null
                        ? uri.toString()
                        : exception.getMessage());
            }
        }
        runOnUiThread(() -> {
            for (File file : imported) {
                selectedPaths.add(file.getAbsolutePath());
                selectedNames.add(file.getName());
            }
            mediaAdapter.notifyDataSetChanged();
            updateContinueButton();
            String message = "Imported " + imported.size() + " items; "
                    + selectedPaths.size() + " total selected.";
            if (!failures.isEmpty()) {
                message += " " + failures.size() + " items failed.";
            }
            setBusy(false, message);
        });
    }

    private void chooseRatio() {
        if (!validateMedia()) {
            return;
        }
        new AlertDialog.Builder(this)
                .setTitle("Project ratio")
                .setItems(RATIO_LABELS, (dialog, which) -> {
                    int[] size = RATIO_SIZES[which];
                    if (quickSpliceMode) {
                        startActivity(MeisheRuntimeDemoActivity.createIntent(
                                this,
                                MeisheRuntimeDemoActivity.MODE_QUICK_SPLICE,
                                selectedPaths,
                                size[0],
                                size[1]));
                    } else {
                        startActivity(MeisheEditorActivity.createIntent(
                                this,
                                selectedPaths,
                                size[0],
                                size[1]));
                    }
                })
                .show();
    }

    private boolean validateMedia() {
        int removed = 0;
        for (int index = selectedPaths.size() - 1; index >= 0; index--) {
            String path = selectedPaths.get(index);
            if (mediaProbeController == null || mediaProbeController.probe(path) == null) {
                File unsupported = new File(path);
                selectedPaths.remove(index);
                selectedNames.remove(index);
                if (unsupported.isFile()) {
                    unsupported.delete();
                }
                removed++;
            }
        }
        if (removed > 0) {
            mediaAdapter.notifyDataSetChanged();
            updateContinueButton();
            statusText.setText("Removed " + removed + " unsupported items; "
                    + selectedPaths.size() + " valid items remain.");
        }
        if (quickSpliceMode && selectedPaths.size() < 2) {
            statusText.setText("Quick splice requires at least two valid media items.");
            return false;
        }
        return !selectedPaths.isEmpty();
    }

    private void setBusy(boolean busy, String message) {
        selectButton.setEnabled(!busy);
        continueButton.setEnabled(!busy && hasEnoughMedia());
        statusText.setText(message);
    }

    private void moveSelectedMedia(int direction) {
        int targetIndex = selectedMediaIndex + direction;
        if (!quickSpliceMode
                || selectedMediaIndex < 0
                || targetIndex < 0
                || targetIndex >= selectedPaths.size()) {
            return;
        }
        java.util.Collections.swap(selectedPaths, selectedMediaIndex, targetIndex);
        java.util.Collections.swap(selectedNames, selectedMediaIndex, targetIndex);
        selectedMediaIndex = targetIndex;
        mediaAdapter.notifyDataSetChanged();
        ((ListView) findViewById(R.id.selectedMediaList)).setItemChecked(targetIndex, true);
        updateReorderControls();
        statusText.setText("Splice order updated. The selected clip is now item "
                + (targetIndex + 1) + ".");
    }

    private void updateContinueButton() {
        continueButton.setEnabled(hasEnoughMedia());
    }

    private boolean hasEnoughMedia() {
        return quickSpliceMode ? selectedPaths.size() >= 2 : !selectedPaths.isEmpty();
    }

    private void updateReorderControls() {
        moveEarlierButton.setEnabled(quickSpliceMode && selectedMediaIndex > 0);
        moveLaterButton.setEnabled(
                quickSpliceMode
                        && selectedMediaIndex >= 0
                        && selectedMediaIndex + 1 < selectedPaths.size());
    }

    @Override
    protected void onDestroy() {
        importExecutor.shutdownNow();
        super.onDestroy();
    }
}
