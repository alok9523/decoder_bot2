import base64

def decode_base64(encoded_text):
    """Decodes a Base64-encoded string."""
    try:
        decoded_bytes = base64.b64decode(encoded_text)
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        return f"Decoding error: {str(e)}"

def decode_hex(encoded_text):
    """Decodes a Hex-encoded string."""
    try:
        return bytes.fromhex(encoded_text).decode("utf-8")
    except Exception as e:
        return f"Decoding error: {str(e)}"
