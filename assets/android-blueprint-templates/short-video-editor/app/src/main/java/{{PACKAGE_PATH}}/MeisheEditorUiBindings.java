package {{PACKAGE_NAME}};

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.drawable.GradientDrawable;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.HorizontalScrollView;
import android.widget.LinearLayout;
import android.widget.SeekBar;
import android.widget.TextView;

import com.meicam.sdk.NvsAssetPackageManager;

import java.util.List;
import java.util.Locale;

public final class MeisheEditorUiBindings {
    public interface Listener {
        void onTogglePlayback();

        void onSeekProgress(int progress, int max);

        void onSeekStarted();

        void onSeekFinished();

        void onAddMedia();

        void onSelectClipIndex(int clipIndex);

        void onSplitClip();

        void onSelectClip();

        void onTrimClip(int retainedPercent);

        void onDeleteClip();

        void onMoveClip();

        void onUndo();

        void onRedo();

        void onApplyFilter();

        void onAddCaption(String text);

        void onApplySticker();

        void onApplyTransition();

        void onApplyMusic();

        void onToggleVoiceover();

        void onPreviewVoiceover();

        void onDeleteVoiceover();

        void onOpenMaterialCenter(int packageType);

        void onMaterialTextProvided(String text);

        void onUseSampleStickerImage();

        void onChooseStickerImage();

        void onUpdateAppliedMaterial(
                MeisheAppliedMaterial material,
                MeisheAppliedMaterial.Edits edits);

        void onDeleteAppliedMaterial(MeisheAppliedMaterial material);

        void onExport();
    }

    private final Activity activity;
    private final Listener listener;
    private final TextView statusText;
    private final SeekBar timelineSeekBar;
    private final Button playButton;
    private final Button voiceoverButton;
    private final TextView timelineSummaryText;
    private final TextView timelineTimeText;
    private final LinearLayout timelineClipStrip;
    private final HorizontalScrollView timelineClipScrollView;
    private final FrameLayout previewStage;
    private final FrameLayout liveWindowContainer;
    private final TextView projectAspectText;
    private final TextView emptyPreviewText;
    private final TextView voiceoverTrackText;
    private final Button previewVoiceoverButton;
    private final Button deleteVoiceoverButton;
    private final TextView appliedMaterialsSummaryText;
    private final LinearLayout appliedMaterialStrip;

    public MeisheEditorUiBindings(Activity activity, Listener listener) {
        if (activity == null || listener == null) {
            throw new IllegalArgumentException("activity and listener are required");
        }
        this.activity = activity;
        this.listener = listener;
        statusText = activity.findViewById(R.id.editorStatusText);
        timelineSeekBar = activity.findViewById(R.id.timelineSeekBar);
        playButton = activity.findViewById(R.id.playButton);
        voiceoverButton = activity.findViewById(R.id.voiceoverButton);
        timelineSummaryText = activity.findViewById(R.id.timelineSummaryText);
        timelineTimeText = activity.findViewById(R.id.timelineTimeText);
        timelineClipStrip = activity.findViewById(R.id.timelineClipStrip);
        timelineClipScrollView = activity.findViewById(R.id.timelineClipScrollView);
        previewStage = activity.findViewById(R.id.editorPreviewStage);
        liveWindowContainer = activity.findViewById(R.id.editorLiveWindow);
        projectAspectText = activity.findViewById(R.id.projectAspectText);
        emptyPreviewText = activity.findViewById(R.id.editorEmptyPreviewText);
        voiceoverTrackText = activity.findViewById(R.id.voiceoverTrackText);
        previewVoiceoverButton = activity.findViewById(R.id.previewVoiceoverButton);
        deleteVoiceoverButton = activity.findViewById(R.id.deleteVoiceoverButton);
        appliedMaterialsSummaryText = activity.findViewById(R.id.appliedMaterialsSummaryText);
        appliedMaterialStrip = activity.findViewById(R.id.appliedMaterialStrip);
    }

    public FrameLayout liveWindowContainer() {
        return liveWindowContainer;
    }

    public void bind() {
        playButton.setOnClickListener(v -> listener.onTogglePlayback());
        timelineSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (fromUser) {
                    listener.onSeekProgress(progress, seekBar.getMax());
                }
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
                listener.onSeekStarted();
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                listener.onSeekFinished();
            }
        });
        activity.findViewById(R.id.addMediaButton).setOnClickListener(v -> listener.onAddMedia());
        activity.findViewById(R.id.splitButton).setOnClickListener(v -> listener.onSplitClip());
        activity.findViewById(R.id.selectClipButton).setOnClickListener(v -> listener.onSelectClip());
        activity.findViewById(R.id.trimClipButton).setOnClickListener(v -> showTrimDialog());
        activity.findViewById(R.id.deleteClipButton).setOnClickListener(v -> listener.onDeleteClip());
        activity.findViewById(R.id.moveClipButton).setOnClickListener(v -> listener.onMoveClip());
        activity.findViewById(R.id.undoButton).setOnClickListener(v -> listener.onUndo());
        activity.findViewById(R.id.redoButton).setOnClickListener(v -> listener.onRedo());
        activity.findViewById(R.id.filterButton).setOnClickListener(v -> listener.onApplyFilter());
        activity.findViewById(R.id.captionButton).setOnClickListener(v -> showCaptionDialog());
        activity.findViewById(R.id.stickerButton).setOnClickListener(v -> listener.onApplySticker());
        activity.findViewById(R.id.transitionButton).setOnClickListener(v -> listener.onApplyTransition());
        activity.findViewById(R.id.musicButton).setOnClickListener(v -> listener.onApplyMusic());
        voiceoverButton.setOnClickListener(v -> listener.onToggleVoiceover());
        previewVoiceoverButton.setOnClickListener(v -> listener.onPreviewVoiceover());
        deleteVoiceoverButton.setOnClickListener(v -> listener.onDeleteVoiceover());
        activity.findViewById(R.id.editorMaterialsButton).setOnClickListener(v ->
                listener.onOpenMaterialCenter(-1));
        activity.findViewById(R.id.exportButton).setOnClickListener(v -> listener.onExport());

        activity.findViewById(R.id.filterButton).setOnLongClickListener(v -> {
            listener.onOpenMaterialCenter(NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);
            return true;
        });
        activity.findViewById(R.id.captionButton).setOnLongClickListener(v -> {
            listener.onOpenMaterialCenter(NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE);
            return true;
        });
        activity.findViewById(R.id.stickerButton).setOnLongClickListener(v -> {
            listener.onOpenMaterialCenter(
                    NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER);
            return true;
        });
        activity.findViewById(R.id.transitionButton).setOnLongClickListener(v -> {
            listener.onOpenMaterialCenter(
                    NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION);
            return true;
        });
    }

    public void setStatus(String message) {
        statusText.setText(message == null ? "" : message);
    }

    public void setPlaying(boolean playing) {
        playButton.setText(playing ? R.string.editor_pause : R.string.editor_play);
    }

    public void setRecording(boolean recording) {
        voiceoverButton.setText(recording
                ? R.string.editor_stop_voiceover
                : R.string.editor_voiceover);
    }

    public void configurePreviewAspectRatio(int projectWidth, int projectHeight) {
        int safeWidth = Math.max(1, projectWidth);
        int safeHeight = Math.max(1, projectHeight);
        int divisor = greatestCommonDivisor(safeWidth, safeHeight);
        projectAspectText.setText(
                "Project " + safeWidth / divisor + ":" + safeHeight / divisor + " · Fit preview");
        previewStage.post(() -> {
            int availableWidth = Math.max(
                    1,
                    previewStage.getWidth()
                            - previewStage.getPaddingLeft()
                            - previewStage.getPaddingRight());
            int availableHeight = Math.max(
                    1,
                    previewStage.getHeight()
                            - previewStage.getPaddingTop()
                            - previewStage.getPaddingBottom());
            float projectAspect = safeWidth / (float) safeHeight;
            int targetWidth = availableWidth;
            int targetHeight = Math.max(1, Math.round(targetWidth / projectAspect));
            if (targetHeight > availableHeight) {
                targetHeight = availableHeight;
                targetWidth = Math.max(1, Math.round(targetHeight * projectAspect));
            }
            FrameLayout.LayoutParams layoutParams = new FrameLayout.LayoutParams(
                    targetWidth,
                    targetHeight,
                    Gravity.CENTER);
            liveWindowContainer.setLayoutParams(layoutParams);
        });
    }

    public void updateTimelinePosition(long positionUs, long durationUs) {
        if (durationUs <= 0) {
            timelineSeekBar.setProgress(0);
            timelineTimeText.setText(R.string.editor_time_placeholder);
            return;
        }
        int progress = (int) Math.min(
                timelineSeekBar.getMax(),
                positionUs * timelineSeekBar.getMax() / durationUs);
        timelineSeekBar.setProgress(progress);
        timelineTimeText.setText(formatTime(positionUs) + " / " + formatTime(durationUs));
    }

    public void renderTimeline(
            List<MeisheEditorClipUiModel> clips,
            int selectedClipIndex) {
        timelineClipStrip.removeAllViews();
        int clipCount = clips == null ? 0 : clips.size();
        timelineSummaryText.setText("Video track · " + clipCount + " clips");
        if (clips == null) {
            return;
        }
        for (MeisheEditorClipUiModel clip : clips) {
            Button clipButton = new Button(activity);
            clipButton.setTag(clip.clipIndex);
            clipButton.setAllCaps(false);
            clipButton.setGravity(Gravity.CENTER);
            clipButton.setLines(2);
            clipButton.setTextSize(11);
            clipButton.setAllCaps(false);
            clipButton.setMinWidth(0);
            clipButton.setPadding(dp(10), dp(6), dp(10), dp(6));
            clipButton.setText(
                    (clip.clipIndex + 1) + ". " + clip.displayName + "\n"
                            + String.format(Locale.US, "%.1fs", clip.durationUs() / 1_000_000.0));
            clipButton.setOnClickListener(v -> listener.onSelectClipIndex(clip.clipIndex));
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(dp(132), dp(60));
            params.setMarginEnd(dp(6));
            timelineClipStrip.addView(clipButton, params);
        }
        setSelectedTimelineClip(selectedClipIndex);
    }

    public void renderVoiceoverTrack(List<MeisheEditorClipUiModel> voiceoverClips) {
        int clipCount = voiceoverClips == null ? 0 : voiceoverClips.size();
        if (clipCount == 0) {
            voiceoverTrackText.setText("Voiceover track · no recordings");
        } else {
            MeisheEditorClipUiModel latest = voiceoverClips.get(clipCount - 1);
            voiceoverTrackText.setText("Voiceover track · " + clipCount + " takes · latest "
                    + String.format(Locale.US, "%.1f seconds", latest.durationUs() / 1_000_000.0));
        }
        previewVoiceoverButton.setEnabled(clipCount > 0);
        deleteVoiceoverButton.setEnabled(clipCount > 0);
    }

    public void renderAppliedMaterials(List<MeisheAppliedMaterial> materials) {
        appliedMaterialStrip.removeAllViews();
        int materialCount = materials == null ? 0 : materials.size();
        appliedMaterialsSummaryText.setText("Applied materials · " + materialCount);
        if (materialCount == 0) {
            TextView empty = new TextView(activity);
            empty.setText("Nothing added yet; use a tool below or open the material center");
            empty.setTextColor(activity.getResources().getColor(R.color.text_secondary));
            empty.setTextSize(12);
            appliedMaterialStrip.addView(empty);
            return;
        }
        for (MeisheAppliedMaterial material : materials) {
            Button materialButton = new Button(activity);
            materialButton.setAllCaps(false);
            materialButton.setGravity(Gravity.START | Gravity.CENTER_VERTICAL);
            materialButton.setLines(2);
            materialButton.setTextSize(11);
            materialButton.setMinWidth(0);
            materialButton.setPadding(dp(10), dp(4), dp(10), dp(4));
            materialButton.setText(material.title + "\n" + material.summary);
            materialButton.setBackground(createTimelineClipBackground(false));
            materialButton.setTextColor(activity.getResources().getColor(R.color.text_primary));
            materialButton.setOnClickListener(view -> showAppliedMaterialEditor(material));
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(dp(150), dp(56));
            params.setMarginEnd(dp(6));
            appliedMaterialStrip.addView(materialButton, params);
        }
    }

    public void requestMaterialText(String materialLabel, boolean compoundCaption) {
        EditText input = new EditText(activity);
        input.setHint(compoundCaption
                ? "Enter compound-caption text; separate slots with line breaks"
                : "Enter the caption text to display");
        input.setMinLines(compoundCaption ? 3 : 1);
        new AlertDialog.Builder(activity)
                .setTitle("Apply “" + materialLabel + "”")
                .setMessage("This material cannot be added without text. Enter its content first.")
                .setView(input)
                .setPositiveButton("Add to timeline", (dialog, which) ->
                        listener.onMaterialTextProvided(input.getText().toString()))
                .setNegativeButton("Cancel", null)
                .show();
    }

    public void requestCustomStickerImage(String materialLabel) {
        new AlertDialog.Builder(activity)
                .setTitle("Apply “" + materialLabel + "”")
                .setMessage("This is a custom animated-sticker template. Select an image before it can be displayed.")
                .setPositiveButton("Choose image", (dialog, which) -> listener.onChooseStickerImage())
                .setNeutralButton("Use local sample image", (dialog, which) ->
                        listener.onUseSampleStickerImage())
                .setNegativeButton("Cancel", null)
                .show();
    }

    public void setTimelineEmpty(boolean empty) {
        liveWindowContainer.setVisibility(empty ? View.INVISIBLE : View.VISIBLE);
        emptyPreviewText.setVisibility(empty ? View.VISIBLE : View.GONE);
        timelineSeekBar.setEnabled(!empty);
        playButton.setEnabled(!empty);
        int[] contentDependentIds = new int[]{
                R.id.exportButton,
                R.id.splitButton,
                R.id.selectClipButton,
                R.id.trimClipButton,
                R.id.deleteClipButton,
                R.id.moveClipButton,
                R.id.filterButton,
                R.id.captionButton,
                R.id.stickerButton,
                R.id.transitionButton,
                R.id.musicButton,
                R.id.voiceoverButton
        };
        for (int id : contentDependentIds) {
            activity.findViewById(id).setEnabled(!empty);
        }
    }

    public void setSelectedTimelineClip(int selectedClipIndex) {
        Button selectedButton = null;
        for (int index = 0; index < timelineClipStrip.getChildCount(); index++) {
            Button clipButton = (Button) timelineClipStrip.getChildAt(index);
            Object tag = clipButton.getTag();
            boolean selected = tag instanceof Integer && (Integer) tag == selectedClipIndex;
            clipButton.setTextColor(activity.getResources().getColor(
                    selected ? R.color.white : R.color.text_secondary));
            clipButton.setBackground(createTimelineClipBackground(selected));
            if (selected) {
                selectedButton = clipButton;
            }
        }
        if (selectedButton != null) {
            Button target = selectedButton;
            timelineClipScrollView.post(() ->
                    timelineClipScrollView.smoothScrollTo(target.getLeft(), 0));
        }
    }

    public void setControlsEnabled(boolean enabled) {
        playButton.setEnabled(enabled);
        timelineSeekBar.setEnabled(enabled);
        int[] ids = new int[]{
                R.id.exportButton,
                R.id.addMediaButton,
                R.id.splitButton,
                R.id.selectClipButton,
                R.id.trimClipButton,
                R.id.deleteClipButton,
                R.id.moveClipButton,
                R.id.undoButton,
                R.id.redoButton,
                R.id.filterButton,
                R.id.captionButton,
                R.id.stickerButton,
                R.id.transitionButton,
                R.id.musicButton,
                R.id.editorMaterialsButton,
                R.id.previewVoiceoverButton,
                R.id.deleteVoiceoverButton
        };
        for (int id : ids) {
            activity.findViewById(id).setEnabled(enabled);
        }
        voiceoverButton.setEnabled(enabled);
    }

    private void showAppliedMaterialEditor(MeisheAppliedMaterial material) {
        LinearLayout content = new LinearLayout(activity);
        content.setOrientation(LinearLayout.VERTICAL);
        content.setPadding(dp(20), 0, dp(20), 0);

        EditText textInput = null;
        EditText durationInput = null;
        EditText intensityInput = null;
        EditText fontSizeInput = null;
        EditText opacityInput = null;
        EditText scaleInput = null;
        EditText rotationInput = null;
        EditText volumeInput = null;
        EditText fadeInInput = null;
        EditText fadeOutInput = null;

        if (MeisheAppliedMaterial.TYPE_CAPTION.equals(material.type)
                || MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(material.type)) {
            textInput = addTextField(
                    content,
                    MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(material.type)
                            ? "Caption text (separate slots with line breaks)"
                            : "Caption text",
                    material.text);
        }
        if (MeisheAppliedMaterial.TYPE_CAPTION.equals(material.type)
                || MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(material.type)
                || MeisheAppliedMaterial.TYPE_STICKER.equals(material.type)
                || MeisheAppliedMaterial.TYPE_TRANSITION.equals(material.type)) {
            durationInput = addNumberField(content, "Duration (seconds)", secondsValue(material.durationUs));
        }
        if (MeisheAppliedMaterial.TYPE_CLIP_EFFECT.equals(material.type)) {
            intensityInput = addNumberField(
                    content,
                    "Intensity (0–100, when supported by the package)",
                    String.valueOf(Math.round(material.intensity * 100)));
        }
        if (MeisheAppliedMaterial.TYPE_CAPTION.equals(material.type)) {
            fontSizeInput = addNumberField(content, "Font size", decimalValue(material.fontSize));
        }
        if (MeisheAppliedMaterial.TYPE_CAPTION.equals(material.type)
                || MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(material.type)
                || MeisheAppliedMaterial.TYPE_STICKER.equals(material.type)) {
            opacityInput = addNumberField(
                    content,
                    "Opacity (0–100)",
                    String.valueOf(Math.round(material.opacity * 100)));
        }
        if (MeisheAppliedMaterial.TYPE_CAPTION.equals(material.type)
                || MeisheAppliedMaterial.TYPE_COMPOUND_CAPTION.equals(material.type)
                || MeisheAppliedMaterial.TYPE_STICKER.equals(material.type)) {
            scaleInput = addNumberField(
                    content,
                    "Scale (percent)",
                    String.valueOf(Math.round(material.scale * 100)));
            rotationInput = addNumberField(content, "Rotation (degrees)", decimalValue(material.rotation));
        }
        if (MeisheAppliedMaterial.TYPE_STICKER.equals(material.type)
                || MeisheAppliedMaterial.TYPE_AUDIO.equals(material.type)
                || MeisheAppliedMaterial.TYPE_THEME.equals(material.type)) {
            volumeInput = addNumberField(
                    content,
                    "Volume (0–200)",
                    String.valueOf(Math.round(material.volume * 100)));
        }
        if (MeisheAppliedMaterial.TYPE_AUDIO.equals(material.type)) {
            fadeInInput = addNumberField(content, "Fade in (seconds)", secondsValue(material.fadeInUs));
            fadeOutInput = addNumberField(content, "Fade out (seconds)", secondsValue(material.fadeOutUs));
        }

        final EditText finalTextInput = textInput;
        final EditText finalDurationInput = durationInput;
        final EditText finalIntensityInput = intensityInput;
        final EditText finalFontSizeInput = fontSizeInput;
        final EditText finalOpacityInput = opacityInput;
        final EditText finalScaleInput = scaleInput;
        final EditText finalRotationInput = rotationInput;
        final EditText finalVolumeInput = volumeInput;
        final EditText finalFadeInInput = fadeInInput;
        final EditText finalFadeOutInput = fadeOutInput;

        new AlertDialog.Builder(activity)
                .setTitle("Edit “" + material.title + "”")
                .setMessage("Changes are reapplied to the timeline and refresh the preview immediately.")
                .setView(content)
                .setPositiveButton("Save changes", (dialog, which) -> {
                    MeisheAppliedMaterial.Edits edits = new MeisheAppliedMaterial.Edits();
                    edits.text = finalTextInput == null
                            ? material.text
                            : finalTextInput.getText().toString();
                    edits.durationUs = finalDurationInput == null
                            ? material.durationUs
                            : parseSeconds(finalDurationInput, material.durationUs);
                    edits.intensity = finalIntensityInput == null
                            ? material.intensity
                            : parseFloat(finalIntensityInput, material.intensity * 100) / 100.0f;
                    edits.fontSize = finalFontSizeInput == null
                            ? material.fontSize
                            : parseFloat(finalFontSizeInput, material.fontSize);
                    edits.opacity = finalOpacityInput == null
                            ? material.opacity
                            : parseFloat(finalOpacityInput, material.opacity * 100) / 100.0f;
                    edits.scale = finalScaleInput == null
                            ? material.scale
                            : parseFloat(finalScaleInput, material.scale * 100) / 100.0f;
                    edits.rotation = finalRotationInput == null
                            ? material.rotation
                            : parseFloat(finalRotationInput, material.rotation);
                    edits.volume = finalVolumeInput == null
                            ? material.volume
                            : parseFloat(finalVolumeInput, material.volume * 100) / 100.0f;
                    edits.fadeInUs = finalFadeInInput == null
                            ? material.fadeInUs
                            : parseSeconds(finalFadeInInput, material.fadeInUs);
                    edits.fadeOutUs = finalFadeOutInput == null
                            ? material.fadeOutUs
                            : parseSeconds(finalFadeOutInput, material.fadeOutUs);
                    listener.onUpdateAppliedMaterial(material, edits);
                })
                .setNeutralButton("Delete material", (dialog, which) ->
                        listener.onDeleteAppliedMaterial(material))
                .setNegativeButton("Cancel", null)
                .show();
    }

    private EditText addTextField(LinearLayout content, String hint, String value) {
        TextView label = new TextView(activity);
        label.setText(hint);
        label.setTextSize(13);
        label.setPadding(0, dp(8), 0, 0);
        content.addView(label);

        EditText input = new EditText(activity);
        input.setHint(hint);
        input.setContentDescription(hint);
        input.setText(value);
        input.setSelectAllOnFocus(false);
        input.setMinLines(1);
        content.addView(input);
        return input;
    }

    private EditText addNumberField(LinearLayout content, String hint, String value) {
        EditText input = addTextField(content, hint, value);
        input.setInputType(InputType.TYPE_CLASS_NUMBER
                | InputType.TYPE_NUMBER_FLAG_DECIMAL
                | InputType.TYPE_NUMBER_FLAG_SIGNED);
        return input;
    }

    private float parseFloat(EditText input, float fallback) {
        try {
            return Float.parseFloat(input.getText().toString().trim());
        } catch (NumberFormatException exception) {
            return fallback;
        }
    }

    private long parseSeconds(EditText input, long fallbackUs) {
        float seconds = parseFloat(input, fallbackUs / 1_000_000.0f);
        return Math.max(0, Math.round(seconds * 1_000_000.0));
    }

    private String secondsValue(long durationUs) {
        return String.format(Locale.US, "%.2f", Math.max(0, durationUs) / 1_000_000.0);
    }

    private String decimalValue(float value) {
        return String.format(Locale.US, "%.1f", value);
    }

    private String formatTime(long timeUs) {
        long boundedTimeUs = Math.max(0, timeUs);
        long totalTenths = boundedTimeUs / 100_000;
        long minutes = totalTenths / 600;
        long seconds = (totalTenths / 10) % 60;
        long tenths = totalTenths % 10;
        return String.format(Locale.US, "%02d:%02d.%d", minutes, seconds, tenths);
    }

    private int dp(int value) {
        return Math.round(value * activity.getResources().getDisplayMetrics().density);
    }

    private GradientDrawable createTimelineClipBackground(boolean selected) {
        GradientDrawable background = new GradientDrawable();
        background.setShape(GradientDrawable.RECTANGLE);
        background.setCornerRadius(dp(12));
        background.setColor(activity.getResources().getColor(
                selected ? R.color.brand_primary : R.color.surface_elevated));
        background.setStroke(
                dp(selected ? 2 : 1),
                activity.getResources().getColor(
                        selected ? R.color.brand_accent : R.color.divider));
        return background;
    }

    private int greatestCommonDivisor(int firstValue, int secondValue) {
        int first = Math.abs(firstValue);
        int second = Math.abs(secondValue);
        while (second != 0) {
            int remainder = first % second;
            first = second;
            second = remainder;
        }
        return Math.max(1, first);
    }

    private void showCaptionDialog() {
        EditText input = new EditText(activity);
        input.setHint("Caption text");
        new AlertDialog.Builder(activity)
                .setTitle("Add caption")
                .setView(input)
                .setPositiveButton("Add", (dialog, which) ->
                        listener.onAddCaption(input.getText().toString()))
                .setNegativeButton("Cancel", null)
                .show();
    }

    private void showTrimDialog() {
        LinearLayout content = new LinearLayout(activity);
        content.setOrientation(LinearLayout.VERTICAL);
        content.setPadding(dp(22), dp(6), dp(22), 0);

        TextView retainedDurationText = new TextView(activity);
        retainedDurationText.setTextColor(activity.getResources().getColor(R.color.text_primary));
        retainedDurationText.setTextSize(15);
        content.addView(retainedDurationText);

        SeekBar retainedPercentSeekBar = new SeekBar(activity);
        retainedPercentSeekBar.setMax(85);
        retainedPercentSeekBar.setProgress(65);
        content.addView(
                retainedPercentSeekBar,
                new LinearLayout.LayoutParams(
                        LinearLayout.LayoutParams.MATCH_PARENT,
                        dp(52)));

        Runnable updateLabel = () -> retainedDurationText.setText(
                "Keep the first " + (retainedPercentSeekBar.getProgress() + 10) + "% of this clip");
        updateLabel.run();
        retainedPercentSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                updateLabel.run();
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
            }
        });

        new AlertDialog.Builder(activity)
                .setTitle("Trim clip end")
                .setMessage("Drag the slider to choose the retained clip length. The timeline refreshes after applying.")
                .setView(content)
                .setPositiveButton("Apply trim", (dialog, which) ->
                        listener.onTrimClip(retainedPercentSeekBar.getProgress() + 10))
                .setNegativeButton("Cancel", null)
                .show();
    }
}
