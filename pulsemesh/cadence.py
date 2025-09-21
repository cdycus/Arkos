class PulseCadence:
    def __init__(self):
        self.entropy_level = 0.0

    def get_next_interval(self):
        return max(0.25, min(2.0, 2.0 - self.entropy_level * 1.75))