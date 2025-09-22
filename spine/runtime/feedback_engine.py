class PulseFeedbackEngine:
    def __init__(self):
        self.history = []

    def record_feedback(self, pulse, result):
        self.history.append((pulse["type"], result))

    def should_throttle(self, pulse_type: str) -> bool:
        # Simple heuristic: if too many failures of same type, throttle
        recent = [r for t, r in self.history[-10:] if t == pulse_type]
        return recent.count(False) > 5
