
import os
import json
import hashlib
import hmac

# Load Skippy's sovereign secret from file or use a fallback
SECRET_FILE = os.path.join(os.path.dirname(__file__), 'skippy_secret.key')

if os.path.exists(SECRET_FILE):
    with open(SECRET_FILE, 'rb') as f:
        SECRET_KEY = f.read()
else:
    SECRET_KEY = b'default-development-key'

def sign_payload(payload: str) -> str:
    return hmac.new(SECRET_KEY, payload.encode(), hashlib.sha256).hexdigest()

def verify_signature(payload: str, signature: str) -> bool:
    expected = sign_payload(payload)
    return hmac.compare_digest(expected, signature)
