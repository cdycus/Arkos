import hashlib
import json

class SovereignPulseSigner:
    def __init__(self, secret="SkippySecret"):
        self.secret = secret

    def sign(self, pulse: dict) -> str:
        payload = json.dumps(pulse, sort_keys=True).encode()
        return hashlib.sha256(payload + self.secret.encode()).hexdigest()

    def verify(self, pulse: dict, signature: str) -> bool:
        expected = self.sign(pulse)
        return expected == signature