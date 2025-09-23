from collections import defaultdict
import time

class PulseHeatmap:
    def __init__(self):
        self.metrics = defaultdict(list)

    def log(self, pulse_type):
        self.metrics[pulse_type].append(time.time())

    def get_summary(self):
        return {k: len(v) for k, v in self.metrics.items()}
