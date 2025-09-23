import random

class PulseDelta:
    def __init__(self):
        self.last_confidence = 0.85
        self.last_entropy = 0.15

    def update(self, confidence, entropy):
        delta_conf = confidence - self.last_confidence
        delta_entr = entropy - self.last_entropy
        self.last_confidence = confidence
        self.last_entropy = entropy
        return {
            "delta_confidence": round(delta_conf, 3),
            "delta_entropy": round(delta_entr, 3)
        }

    def should_emit_alert(self):
        return random.random() > 0.98  # 2% of the time emit a health check
