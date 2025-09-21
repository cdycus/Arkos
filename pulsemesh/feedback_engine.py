class PulseFeedbackEngine:
    def __init__(self):
        self.history = []

    def record_feedback(self, pulse, result):
        self.history.append((pulse["type"], result))