class PulseAnomalyDetector:
    def __init__(self):
        self.last_seen = {}

    def detect(self, pulse_type, timestamp):
        if pulse_type not in self.last_seen:
            self.last_seen[pulse_type] = timestamp
            return False
        delta = timestamp - self.last_seen[pulse_type]
        self.last_seen[pulse_type] = timestamp
        return delta < 0.5  # anomaly if frequency too high
