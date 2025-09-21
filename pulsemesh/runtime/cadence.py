class PulseCadence:
    def __init__(self):
        self.base_interval = 1.0  # seconds
        self.entropy_level = 0.0  # simulated input

    def update_entropy(self, level: float):
        self.entropy_level = max(0.0, min(1.0, level))

    def get_interval(self) -> float:
        # Higher entropy = faster core_brain, min 0.25s, max 2s
        return max(0.25, min(2.0, 2.0 - self.entropy_level * 1.75))
