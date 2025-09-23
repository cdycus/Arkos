import time

class PulseThrottle:
    def __init__(self):
        self.default_interval = 1.0
        self.last_tick = time.time()

    def get_wait_time(self):
        now = time.time()
        elapsed = now - self.last_tick
        self.last_tick = now
        return max(0.5, min(2.0, 1.0 + (0.3 - elapsed)))
