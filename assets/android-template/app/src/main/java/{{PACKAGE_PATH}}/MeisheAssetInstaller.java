package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsAssetPackageManager;
import com.meicam.sdk.NvsStreamingContext;

import java.util.HashMap;
import java.util.Map;

public final class MeisheAssetInstaller {
    private final NvsAssetPackageManager packageManager;

    public MeisheAssetInstaller(NvsStreamingContext streamingContext) {
        this.packageManager = streamingContext.getAssetPackageManager();
    }

    public String installOrUpgrade(String packagePath, String licensePath, int packageType) {
        MeisheThreading.requireMainThread("installAssetPackage");
        if (packagePath == null || packagePath.isEmpty() || packageType < 0) {
            return "";
        }
        String detectedPackageId = packageManager.getAssetPackageIdFromAssetPackageFilePath(packagePath);
        StringBuilder packageId = new StringBuilder();
        int code = packageManager.installAssetPackage(packagePath, licensePath, packageType, true, packageId);
        String resolvedPackageId = packageId.length() > 0
                ? packageId.toString()
                : (detectedPackageId == null ? "" : detectedPackageId);
        if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
            int installedVersion = packageManager.getAssetPackageVersion(resolvedPackageId, packageType);
            int fileVersion = packageManager.getAssetPackageVersionFromAssetPackageFilePath(packagePath);
            if (fileVersion > installedVersion) {
                int upgradeCode = packageManager.upgradeAssetPackage(
                        packagePath,
                        licensePath,
                        packageType,
                        true,
                        packageId);
                if (upgradeCode != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR) {
                    return "";
                }
            }
        }
        if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
                || code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
            return packageId.length() > 0 ? packageId.toString() : resolvedPackageId;
        }
        return "";
    }

    public int installAsynchronously(
            String packagePath,
            String licensePath,
            int packageType,
            InstallCallback callback) {
        MeisheThreading.requireMainThread("installAssetPackage asynchronously");
        if (packagePath == null || packagePath.isEmpty() || packageType < 0
                || callback == null) {
            return -1;
        }
        String detectedPackageId = packageManager
                .getAssetPackageIdFromAssetPackageFilePath(packagePath);
        StringBuilder requestedPackageId = new StringBuilder();
        packageManager.setCallbackInterface(
                new NvsAssetPackageManager.AssetPackageManagerCallback() {
                    @Override
                    public void onFinishAssetPackageInstallation(
                            String packageId,
                            String filePath,
                            int completedPackageType,
                            int error) {
                        callback.onComplete(new InstallResult(
                                packageId,
                                filePath,
                                completedPackageType,
                                error));
                    }

                    @Override
                    public void onFinishAssetPackageUpgrading(
                            String packageId,
                            String filePath,
                            int completedPackageType,
                            int error) {
                        callback.onComplete(new InstallResult(
                                packageId,
                                filePath,
                                completedPackageType,
                                error));
                    }
                });
        int code = packageManager.installAssetPackage(
                packagePath,
                licensePath,
                packageType,
                false,
                requestedPackageId);
        if (code == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED) {
            callback.onComplete(new InstallResult(
                    requestedPackageId.length() > 0
                            ? requestedPackageId.toString()
                            : detectedPackageId,
                    packagePath,
                    packageType,
                    code));
        } else if (code != NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
                && code != NvsAssetPackageManager
                .ASSET_PACKAGE_MANAGER_ERROR_WORKING_INPROGRESS) {
            callback.onComplete(new InstallResult(
                    requestedPackageId.toString(),
                    packagePath,
                    packageType,
                    code));
        }
        return code;
    }

    public int packageTypeForPath(String packagePath) {
        if (packagePath == null) {
            return -1;
        }
        String normalizedPath = packagePath.toLowerCase(java.util.Locale.ROOT);
        if (normalizedPath.endsWith(".videofx")) {
            return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
        }
        if (normalizedPath.endsWith(".animatedsticker")) {
            return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER;
        }
        if (normalizedPath.endsWith(".template")) {
            return NvsAssetPackageManager.ASSET_PACKAGE_TYPE_TEMPLATE;
        }
        return -1;
    }

    public Map<String, Object> inspectInstalledPackage(String packageId, int packageType) {
        MeisheThreading.requireMainThread("inspect installed asset package");
        Map<String, Object> metadata = new HashMap<>();
        if (packageManager == null || packageId == null || packageId.isEmpty() || packageType < 0) {
            return metadata;
        }
        metadata.put("status", packageManager.getAssetPackageStatus(packageId, packageType));
        metadata.put(
                "supportedAspectRatio",
                packageManager.getAssetPackageSupportedAspectRatio(packageId, packageType));
        if (packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX) {
            metadata.put(
                    "description",
                    packageManager.getVideoFxAssetPackageDescription(packageId));
        }
        if (packageType == NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE) {
            metadata.put("prompt", packageManager.getARSceneAssetPackagePrompt(packageId));
            metadata.put(
                    "cameraPreset",
                    packageManager.getARSceneAssetPackageCameraPreset(packageId));
            metadata.put(
                    "containsFaceMesh",
                    packageManager.isARSceneAssetPackageContainFaceMesh(packageId));
            metadata.put(
                    "containsWarp",
                    packageManager.isARSceneAssetPackageContainWarp(packageId));
        }
        return metadata;
    }

    public interface InstallCallback {
        void onComplete(InstallResult result);
    }

    public static final class InstallResult {
        public final String packageId;
        public final String filePath;
        public final int packageType;
        public final int errorCode;

        InstallResult(String packageId, String filePath, int packageType, int errorCode) {
            this.packageId = packageId == null ? "" : packageId;
            this.filePath = filePath == null ? "" : filePath;
            this.packageType = packageType;
            this.errorCode = errorCode;
        }

        public boolean isSuccess() {
            return errorCode == NvsAssetPackageManager.ASSET_PACKAGE_MANAGER_ERROR_NO_ERROR
                    || errorCode == NvsAssetPackageManager
                    .ASSET_PACKAGE_MANAGER_ERROR_ALREADY_INSTALLED;
        }
    }
}
