import hashlib
import json

class PulseSigner:
    def __init__(self, secret="sovereign_skippy_key"):
        self.secret = secret

    def sign(self, pulse):
        payload = json.dumps(pulse, sort_keys=True)
        return hashlib.sha256((payload + self.secret).encode()).hexdigest()

    def verify(self, pulse, signature):
        return self.sign(pulse) == signature
