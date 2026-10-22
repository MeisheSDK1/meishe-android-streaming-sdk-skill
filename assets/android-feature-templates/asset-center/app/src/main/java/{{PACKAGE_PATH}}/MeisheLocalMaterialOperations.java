package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsStreamingContext;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public final class MeisheLocalMaterialOperations {
    private MeisheLocalMaterialOperations() {
    }

    public static List<Integer> matchingIndexes(
            String selectedFamily,
            String allFamiliesLabel,
            List<String> entryFamilies) {
        if (entryFamilies == null || entryFamilies.isEmpty()) {
            return Collections.emptyList();
        }
        boolean includeAll = selectedFamily == null || selectedFamily.equals(allFamiliesLabel);
        List<Integer> matches = new ArrayList<>();
        for (int index = 0; index < entryFamilies.size(); index++) {
            if (includeAll || selectedFamily.equals(entryFamilies.get(index))) {
                matches.add(index);
            }
        }
        return matches;
    }

    public static String installBundledPackage(
            MeisheAssetInstaller installer,
            String packagePath,
            String licensePath,
            int packageType) {
        if (installer == null || packagePath == null || packagePath.isEmpty() || packageType < 0) {
            return "";
        }
        String packageId = installer.installOrUpgrade(packagePath, licensePath, packageType);
        return packageId == null ? "" : packageId;
    }

    public static String registerBundledFont(
            NvsStreamingContext streamingContext,
            String localFontPath) {
        if (streamingContext == null || localFontPath == null || localFontPath.isEmpty()) {
            return "";
        }
        String family = streamingContext.registerFontByFilePath(localFontPath);
        return family == null ? "" : family;
    }
}
