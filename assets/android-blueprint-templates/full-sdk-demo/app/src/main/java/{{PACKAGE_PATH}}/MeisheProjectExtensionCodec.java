package {{PACKAGE_NAME}};

import org.json.JSONException;
import org.json.JSONObject;

public interface MeisheProjectExtensionCodec<T> {
    String namespace();

    JSONObject encode(T value) throws JSONException;

    T decode(JSONObject value) throws JSONException;
}
