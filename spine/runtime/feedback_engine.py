
class PulseFeedbackEngine:
    def __init__(self):
        self.history = []
        self.accepted_pulses = 0
        self.overridden_pulses = 0

    def log_feedback(self, pulse_id, accepted=True):
        self.history.append({
            "pulse_id": pulse_id,
            "accepted": accepted
        })
        if accepted:
            self.accepted_pulses += 1
        else:
            self.overridden_pulses += 1

    def effectiveness_score(self):
        total = len(self.history)
        if total == 0:
            return 1.0
        return round(self.accepted_pulses / total, 3)

    def reset(self):
        self.history.clear()
        self.accepted_pulses = 0
        self.overridden_pulses = 0
