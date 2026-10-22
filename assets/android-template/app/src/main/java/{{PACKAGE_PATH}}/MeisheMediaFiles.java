package {{PACKAGE_NAME}};

import android.content.Context;
import android.database.Cursor;
import android.net.Uri;
import android.provider.OpenableColumns;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

public final class MeisheMediaFiles {
    private MeisheMediaFiles() {
    }

    public static String copyContentUriToCache(Context context, Uri uri) throws IOException {
        if (context == null || uri == null) {
            throw new IOException("Missing context or media URI");
        }
        String displayName = null;
        try (Cursor cursor = context.getContentResolver().query(
                uri,
                new String[]{OpenableColumns.DISPLAY_NAME},
                null,
                null,
                null)) {
            if (cursor != null && cursor.moveToFirst()) {
                int index = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME);
                if (index >= 0) {
                    displayName = cursor.getString(index);
                }
            }
        } catch (RuntimeException ignored) {
            // Fall back to a generated name when a provider exposes no metadata.
        }
        String safeName = (displayName == null ? "selected-media" : displayName)
                .replaceAll("[^A-Za-z0-9._-]", "_");
        if (safeName.isEmpty()) {
            safeName = "selected-media";
        }
        File directory = new File(
                new File(context.getCacheDir(), "selected-media"),
                String.valueOf(System.currentTimeMillis()));
        if (!directory.exists() && !directory.mkdirs()) {
            throw new IOException("Cannot create media cache directory");
        }
        // SDK asset-package parsers can require the original UUID-based file name.
        File output = new File(directory, safeName);
        try (InputStream input = context.getContentResolver().openInputStream(uri);
             FileOutputStream stream = new FileOutputStream(output)) {
            if (input == null) {
                throw new IOException("Cannot open selected media");
            }
            byte[] buffer = new byte[16 * 1024];
            int count;
            while ((count = input.read(buffer)) != -1) {
                stream.write(buffer, 0, count);
            }
        }
        return output.getAbsolutePath();
    }

    public static String copyAssetToProject(
            Context context,
            String assetPath,
            String fileName) throws IOException {
        if (context == null || assetPath == null || assetPath.isEmpty()
                || fileName == null || fileName.isEmpty()) {
            throw new IOException("Missing bundled media input");
        }
        String safeName = fileName.replaceAll("[^A-Za-z0-9._-]", "_");
        if (safeName.isEmpty()) {
            throw new IOException("Bundled media name is invalid");
        }
        File directory = new File(context.getFilesDir(), "sample-media");
        if (!directory.exists() && !directory.mkdirs()) {
            throw new IOException("Cannot create sample media directory");
        }
        File output = new File(directory, safeName);
        if (output.isFile() && output.length() > 0) {
            return output.getAbsolutePath();
        }
        try (InputStream input = context.getAssets().open(assetPath);
             FileOutputStream stream = new FileOutputStream(output)) {
            byte[] buffer = new byte[16 * 1024];
            int count;
            while ((count = input.read(buffer)) != -1) {
                stream.write(buffer, 0, count);
            }
        } catch (IOException exception) {
            if (output.exists() && !output.delete()) {
                output.deleteOnExit();
            }
            throw exception;
        }
        if (!output.isFile() || output.length() == 0) {
            throw new IOException("Bundled media copy is empty");
        }
        return output.getAbsolutePath();
    }
}
