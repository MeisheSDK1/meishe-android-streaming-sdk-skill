package {{PACKAGE_NAME}};

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public final class MeisheLocalMaterialCatalog {
    public static final String ALL_FAMILIES = "All";
    public static final int RESOURCE_TYPE_FONT = -100;

    private static final List<Entry> ENTRIES = Collections.unmodifiableList(Arrays.asList(
            Entry.packageAsset("Effects", "Filter", MeisheSampleAssets.FILTER,
                    MeisheMaterialApplicationKind.FILTER, "Select a target clip, then apply directly", "Intensity, delete"),
            Entry.packageAsset("Effects", "Clip animation", MeisheSampleAssets.CLIP_ANIMATION,
                    MeisheMaterialApplicationKind.CLIP_EFFECT, "Select a target clip, then apply directly", "Intensity when supported, delete"),
            Entry.packageAsset("Effects", "Particle", MeisheSampleAssets.PARTICLE,
                    MeisheMaterialApplicationKind.CLIP_EFFECT, "Select a target clip, then apply directly", "Intensity when supported, delete"),
            Entry.packageAsset("Effects", "Picture-in-picture effect", MeisheSampleAssets.PIP_EFFECT,
                    MeisheMaterialApplicationKind.CLIP_EFFECT, "Select a target clip, then apply directly", "Intensity when supported, delete"),
            Entry.packageAsset("Transitions", "Video transition", MeisheSampleAssets.TRANSITION,
                    MeisheMaterialApplicationKind.TRANSITION, "Requires at least two clips; defaults to the boundary after the selected clip", "Duration, delete"),
            Entry.packageAsset("Captions", "Caption style", MeisheSampleAssets.CAPTION_STYLE,
                    MeisheMaterialApplicationKind.CAPTION_STYLE, "Requires caption text", "Text, duration, font size, opacity, scale, rotation, delete"),
            Entry.packageAsset("Captions", "Compound caption", MeisheSampleAssets.COMPOUND_CAPTION,
                    MeisheMaterialApplicationKind.COMPOUND_CAPTION, "Requires caption text; separate multiple slots with line breaks", "Slot text, duration, opacity, scale, rotation, delete"),
            Entry.packageAsset("Captions", "Caption bubble", MeisheSampleAssets.CAPTION_CONTEXT,
                    MeisheMaterialApplicationKind.CAPTION_CONTEXT, "Requires caption text", "Text, duration, font size, opacity, scale, rotation, delete"),
            Entry.packageAsset("Captions", "Rich caption renderer", MeisheSampleAssets.CAPTION_RENDERER,
                    MeisheMaterialApplicationKind.CAPTION_RENDERER, "Requires caption text", "Text, duration, font size, opacity, scale, rotation, delete"),
            Entry.packageAsset("Captions", "Caption animation", MeisheSampleAssets.CAPTION_ANIMATION,
                    MeisheMaterialApplicationKind.CAPTION_ANIMATION, "Requires caption text", "Text, duration, font size, opacity, scale, rotation, delete"),
            Entry.packageAsset("Stickers", "Custom animated-sticker template", MeisheSampleAssets.ANIMATED_STICKER,
                    MeisheMaterialApplicationKind.CUSTOM_STICKER, "Requires a custom image", "Duration, scale, rotation, opacity, volume, delete"),
            Entry.packageAsset("Stickers", "Sticker in animation", MeisheSampleAssets.STICKER_IN_ANIMATION,
                    MeisheMaterialApplicationKind.STICKER_IN_ANIMATION, "Requires an existing sticker on the timeline", "Sticker duration, scale, rotation, opacity, volume, delete"),
            Entry.packageAsset("Capture and AR", "Capture scene", MeisheSampleAssets.CAPTURE_SCENE,
                    MeisheMaterialApplicationKind.CAPTURE_SCENE, "Capture-preview only; it is not added to the timeline", "Remove or replace it in the camera module"),
            Entry.packageAsset("Capture and AR", "AR scene", MeisheSampleAssets.AR_SCENE,
                    MeisheMaterialApplicationKind.AR_SCENE, "Capture-preview only; it is not added to the timeline", "Remove or replace it in the camera module"),
            Entry.packageAsset("Capture and AR", "Face mesh", MeisheSampleAssets.FACE_MESH,
                    MeisheMaterialApplicationKind.FACE_MESH, "Bind from a beauty or AR module; it is not added to the timeline by itself", "Managed by the beauty or AR module"),
            Entry.packageAsset("Themes", "Theme", MeisheSampleAssets.THEME,
                    MeisheMaterialApplicationKind.THEME, "Can be applied directly to the whole timeline", "Theme music volume, delete"),
            Entry.font("Fonts", "Local sample caption font", MeisheSampleAssets.SAMPLE_FONT_PATH,
                    MeisheMaterialApplicationKind.FONT, "Requires caption text", "Text, duration, font size, opacity, scale, rotation, delete")
    ));

    private MeisheLocalMaterialCatalog() {
    }

    public static List<String> familyLabels() {
        return Arrays.asList(
                ALL_FAMILIES,
                "Effects",
                "Transitions",
                "Captions",
                "Stickers",
                "Capture and AR",
                "Themes",
                "Fonts");
    }

    public static List<Entry> entriesForFamily(String family) {
        List<String> entryFamilies = new ArrayList<>();
        for (Entry entry : ENTRIES) {
            entryFamilies.add(entry.family);
        }
        List<Entry> matches = new ArrayList<>();
        for (int index : MeisheLocalMaterialOperations.matchingIndexes(
                family,
                ALL_FAMILIES,
                entryFamilies)) {
            matches.add(ENTRIES.get(index));
        }
        return matches;
    }

    public static List<String> familiesForPackageType(int packageType) {
        List<String> families = new ArrayList<>();
        for (Entry entry : ENTRIES) {
            if (entry.packageType == packageType && !families.contains(entry.family)) {
                families.add(entry.family);
            }
        }
        return families;
    }

    public static final class Entry {
        public final String family;
        public final String label;
        public final String packagePath;
        public final String licensePath;
        public final int packageType;
        public final String materialKey;
        public final String applicationKind;
        public final String applicationRequirement;
        public final String editableProperties;

        private Entry(
                String family,
                String label,
                String packagePath,
                String licensePath,
                int packageType,
                String materialKey,
                String applicationKind,
                String applicationRequirement,
                String editableProperties) {
            this.family = family;
            this.label = label;
            this.packagePath = packagePath;
            this.licensePath = licensePath;
            this.packageType = packageType;
            this.materialKey = materialKey;
            this.applicationKind = applicationKind;
            this.applicationRequirement = applicationRequirement;
            this.editableProperties = editableProperties;
        }

        static Entry packageAsset(
                String family,
                String label,
                MeisheSampleAssets.PackageAsset asset,
                String applicationKind,
                String applicationRequirement,
                String editableProperties) {
            return new Entry(
                    family,
                    label,
                    asset.packagePath,
                    asset.licensePath,
                    asset.packageType,
                    asset.key,
                    applicationKind,
                    applicationRequirement,
                    editableProperties);
        }

        static Entry font(
                String family,
                String label,
                String assetPath,
                String applicationKind,
                String applicationRequirement,
                String editableProperties) {
            return new Entry(
                    family,
                    label,
                    assetPath,
                    "",
                    RESOURCE_TYPE_FONT,
                    "font",
                    applicationKind,
                    applicationRequirement,
                    editableProperties);
        }

        public boolean isFont() {
            return packageType == RESOURCE_TYPE_FONT;
        }

        @Override
        public String toString() {
            return label + "  [" + family + "]\n" + "Apply target: "
                    + applicationRequirement;
        }
    }
}
