package {{PACKAGE_NAME}};

import android.content.ContentResolver;
import android.content.Context;
import android.database.Cursor;
import android.net.Uri;
import android.provider.OpenableColumns;
import android.webkit.MimeTypeMap;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Locale;
import java.util.UUID;

public final class MeisheMediaImporter {
    private MeisheMediaImporter() {
    }

    public static File copyToProjectFile(Context context, Uri uri) throws IOException {
        if (context == null || uri == null) {
            throw new IllegalArgumentException("context and uri are required");
        }
        String displayName = "";
        try (Cursor cursor = context.getContentResolver().query(
                uri,
                new String[]{OpenableColumns.DISPLAY_NAME},
                null,
                null,
                null)) {
            if (cursor != null && cursor.moveToFirst()) {
                int column = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME);
                if (column >= 0) {
                    String value = cursor.getString(column);
                    displayName = value == null ? "" : value;
                }
            }
        }
        if (displayName.isEmpty()) {
            String mimeType = context.getContentResolver().getType(uri);
            String extension = "bin";
            if ("video/mp4".equals(mimeType)) {
                extension = "mp4";
            } else if ("image/jpeg".equals(mimeType)) {
                extension = "jpg";
            } else if ("image/png".equals(mimeType)) {
                extension = "png";
            }
            displayName = "media." + extension;
        }
        String safeName = displayName.replaceAll("[^a-zA-Z0-9._-]", "_");
        if (safeName.isEmpty()) {
            safeName = "media.bin";
        }
        File projectDir = new File(context.getFilesDir(), "project-media");
        if (!projectDir.exists() && !projectDir.mkdirs()) {
            throw new IOException("Cannot create project media directory: " + projectDir);
        }
        File outputFile = new File(projectDir, UUID.randomUUID() + "_" + safeName);
        try {
            try (InputStream input = context.getContentResolver().openInputStream(uri);
                 FileOutputStream output = new FileOutputStream(outputFile)) {
                if (input == null) {
                    throw new IOException("Cannot open selected media: " + uri);
                }
                byte[] buffer = new byte[64 * 1024];
                int read;
                while ((read = input.read(buffer)) != -1) {
                    output.write(buffer, 0, read);
                }
            }
        } catch (IOException exception) {
            if (outputFile.isFile()) {
                outputFile.delete();
            }
            throw exception;
        }
        return outputFile;
    }

    private static String queryDisplayName(ContentResolver resolver, Uri uri) {
        try (Cursor cursor = resolver.query(
                uri,
                new String[]{OpenableColumns.DISPLAY_NAME},
                null,
                null,
                null)) {
            if (cursor != null && cursor.moveToFirst()) {
                int column = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME);
                if (column >= 0) {
                    String value = cursor.getString(column);
                    return value == null ? "" : value;
                }
            }
        }
        return "";
    }

    private static String extensionFromMimeType(String mimeType) {
        String extension = MimeTypeMap.getSingleton().getExtensionFromMimeType(mimeType);
        return extension == null || extension.isEmpty() ? "bin" : extension.toLowerCase(Locale.US);
    }

    private static String sanitizeName(String value) {
        String sanitized = value.replaceAll("[^a-zA-Z0-9._-]", "_");
        return sanitized.isEmpty() ? "media.bin" : sanitized;
    }
}
