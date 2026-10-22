package {{PACKAGE_NAME}};

import com.meicam.sdk.NvsAssetPackageManager;

import java.util.HashMap;
import java.util.Map;

public final class MeisheSampleAssets {
    public static final String SAMPLE_IMAGE_PATH = "assets:/sample/demo_base.jpg";
    public static final String SAMPLE_OVERLAY_IMAGE_PATH = "assets:/sample/demo_overlay.jpg";
    public static final String SAMPLE_AUDIO_PATH = "assets:/meicam/cartoon/cartoon.m4a";
    public static final String SAMPLE_WATERMARK_PATH = "assets:/watermark/static_watermark.png";
    public static final String SAMPLE_STICKER_IMAGE_PATH = "assets:/watermark/static_watermark.png";
    public static final String SAMPLE_GLITTER_PATH = "assets:/glitter/star4.png";
    public static final String SAMPLE_EMPTY_BACKGROUND_PATH = "assets:/background/nobackground.png";
    public static final String SAMPLE_FONT_PATH = "assets:/font/FZSSJW.ttf";

    public static final PackageAsset FILTER = new PackageAsset(
            "filter",
            "assets:/filter/394EB525-1B7A-4AA1-BBAD-3FD75527A60C/394EB525-1B7A-4AA1-BBAD-3FD75527A60C.5.videofx",
            "assets:/filter/394EB525-1B7A-4AA1-BBAD-3FD75527A60C/394EB525-1B7A-4AA1-BBAD-3FD75527A60C.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);

    public static final PackageAsset TRANSITION = new PackageAsset(
            "transition",
            "assets:/transition/C94516F7-0380-430E-AADC-83D9ED386790/C94516F7-0380-430E-AADC-83D9ED386790.11.videotransition",
            "assets:/transition/C94516F7-0380-430E-AADC-83D9ED386790/C94516F7-0380-430E-AADC-83D9ED386790.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION);

    public static final PackageAsset CAPTION_STYLE = new PackageAsset(
            "captionStyle",
            "assets:/captionstyle/91FC65DD-AE99-4079-B6A4-BDE60A3F6DF9/91FC65DD-AE99-4079-B6A4-BDE60A3F6DF9.2.captionstyle",
            "assets:/captionstyle/91FC65DD-AE99-4079-B6A4-BDE60A3F6DF9/91FC65DD-AE99-4079-B6A4-BDE60A3F6DF9.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTIONSTYLE);

    public static final PackageAsset ANIMATED_STICKER = new PackageAsset(
            "animatedSticker",
            "assets:/customsticker/E14FEE65-71A0-4717-9D66-3397B6C11223/E14FEE65-71A0-4717-9D66-3397B6C11223.5.animatedsticker",
            "assets:/customsticker/E14FEE65-71A0-4717-9D66-3397B6C11223/E14FEE65-71A0-4717-9D66-3397B6C11223.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER);

    public static final PackageAsset CAPTURE_SCENE = new PackageAsset(
            "captureScene",
            "assets:/capturescene/A2F05F58-87AB-4D1D-9609-6C00EF09E4D1/A2F05F58-87AB-4D1D-9609-6C00EF09E4D1.capturescene",
            "assets:/capturescene/A2F05F58-87AB-4D1D-9609-6C00EF09E4D1/A2F05F58-87AB-4D1D-9609-6C00EF09E4D1.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTURESCENE);

    public static final PackageAsset COMPOUND_CAPTION = new PackageAsset(
            "compoundCaption",
            "assets:/compoundcaption/13E33AA6-85DC-4D7E-B5B0-23A9F0317909/13E33AA6-85DC-4D7E-B5B0-23A9F0317909.5.compoundcaption",
            "assets:/compoundcaption/13E33AA6-85DC-4D7E-B5B0-23A9F0317909/13E33AA6-85DC-4D7E-B5B0-23A9F0317909.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION);

    public static final PackageAsset CAPTION_CONTEXT = new PackageAsset(
            "captionContext",
            "assets:/captionbubble/33C8A32B-CC07-4B62-95BA-14A8365B75F1/33C8A32B-CC07-4B62-95BA-14A8365B75F1.2.captioncontext",
            "assets:/captionbubble/33C8A32B-CC07-4B62-95BA-14A8365B75F1/33C8A32B-CC07-4B62-95BA-14A8365B75F1.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_CONTEXT);

    public static final PackageAsset CAPTION_RENDERER = new PackageAsset(
            "captionRenderer",
            "assets:/captionrichword/72D49EAD-B9E4-4ADC-A188-545046835F65/72D49EAD-B9E4-4ADC-A188-545046835F65.5.captionrenderer",
            "assets:/captionrichword/72D49EAD-B9E4-4ADC-A188-545046835F65/72D49EAD-B9E4-4ADC-A188-545046835F65.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_RENDERER);

    public static final PackageAsset CAPTION_ANIMATION = new PackageAsset(
            "captionAnimation",
            "assets:/captionanimation/combination/0DC345B0-A396-4818-A27D-F1BC3D89DEF3/0DC345B0-A396-4818-A27D-F1BC3D89DEF3.2.captionanimation",
            "assets:/captionanimation/combination/0DC345B0-A396-4818-A27D-F1BC3D89DEF3/0DC345B0-A396-4818-A27D-F1BC3D89DEF3.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_CAPTION_ANIMATION);

    public static final PackageAsset STICKER_IN_ANIMATION = new PackageAsset(
            "stickerInAnimation",
            "assets:/stickeranimation/in/ECF06228-5D1F-4728-80FB-0B1943A60C23/ECF06228-5D1F-4728-80FB-0B1943A60C23.1.animatedstickerinanimation",
            "assets:/stickeranimation/in/ECF06228-5D1F-4728-80FB-0B1943A60C23/ECF06228-5D1F-4728-80FB-0B1943A60C23.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER_IN_ANIMATION);

    public static final PackageAsset CLIP_ANIMATION = new PackageAsset(
            "clipAnimation",
            "assets:/animation/in/37154A36-8816-492B-B1F5-F8122660C686/37154A36-8816-492B-B1F5-F8122660C686.1.videofx",
            "assets:/animation/in/37154A36-8816-492B-B1F5-F8122660C686/37154A36-8816-492B-B1F5-F8122660C686.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);

    public static final PackageAsset PARTICLE = new PackageAsset(
            "particle",
            "assets:/particle/touch/34B095C8-628A-4E9D-B36D-093F9774DAF7/34B095C8-628A-4E9D-B36D-093F9774DAF7.1.videofx",
            "assets:/particle/touch/34B095C8-628A-4E9D-B36D-093F9774DAF7/34B095C8-628A-4E9D-B36D-093F9774DAF7.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);

    public static final PackageAsset PIP_EFFECT = new PackageAsset(
            "pipEffect",
            "assets:/picinpic/pip_sreenleftup/64EC065F-17AE-4881-99EB-854C265FE950/64EC065F-17AE-4881-99EB-854C265FE950.1.videofx",
            "assets:/picinpic/pip_sreenleftup/64EC065F-17AE-4881-99EB-854C265FE950/64EC065F-17AE-4881-99EB-854C265FE950.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX);

    public static final PackageAsset AR_SCENE = new PackageAsset(
            "arScene",
            "assets:/arface/EDF352FC-701B-4C05-86CE-B0E293469341/EDF352FC-701B-4C05-86CE-B0E293469341.7.arscene",
            "assets:/arface/EDF352FC-701B-4C05-86CE-B0E293469341/EDF352FC-701B-4C05-86CE-B0E293469341.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ARSCENE);

    public static final PackageAsset FACE_MESH = new PackageAsset(
            "faceMesh",
            "assets:/beauty/shapePackage/CC86C182-62D7-4F1D-AE9D-F5E4E99977A5/CC86C182-62D7-4F1D-AE9D-F5E4E99977A5.2.facemesh",
            "assets:/beauty/shapePackage/CC86C182-62D7-4F1D-AE9D-F5E4E99977A5/CC86C182-62D7-4F1D-AE9D-F5E4E99977A5.lic",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_FACE_MESH);

    public static final PackageAsset THEME = new PackageAsset(
            "theme",
            "assets:/theme/97489A20-5143-4923-9A3D-0F57ED030366.1.theme",
            "",
            NvsAssetPackageManager.ASSET_PACKAGE_TYPE_THEME);

    private static final PackageAsset[] DEFAULT_PACKAGES = {
            FILTER,
            TRANSITION,
            CAPTION_STYLE,
            ANIMATED_STICKER,
            CAPTURE_SCENE
    };

    private MeisheSampleAssets() {
    }

    public static Map<String, String> installDefaultPackages(MeisheAssetInstaller installer) {
        Map<String, String> packageIds = new HashMap<>();
        if (installer == null) {
            return packageIds;
        }
        for (PackageAsset asset : DEFAULT_PACKAGES) {
            String packageId = installer.installOrUpgrade(asset.packagePath, asset.licensePath, asset.packageType);
            if (packageId != null && !packageId.isEmpty()) {
                packageIds.put(asset.key, packageId);
            }
        }
        return packageIds;
    }

    public static final class PackageAsset {
        public final String key;
        public final String packagePath;
        public final String licensePath;
        public final int packageType;

        private PackageAsset(String key, String packagePath, String licensePath, int packageType) {
            this.key = key;
            this.packagePath = packagePath;
            this.licensePath = licensePath;
            this.packageType = packageType;
        }
    }
}
