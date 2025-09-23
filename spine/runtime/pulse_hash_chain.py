import hashlib
import json

class PulseHashChain:
    def __init__(self):
        self.previous_hash = "0" * 64

    def hash_pulse(self, pulse):
        payload = json.dumps(pulse, sort_keys=True)
        combined = self.previous_hash + payload
        new_hash = hashlib.sha256(combined.encode()).hexdigest()
        self.previous_hash = new_hash
        return new_hash
