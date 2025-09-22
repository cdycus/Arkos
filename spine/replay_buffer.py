import os
import json
from pathlib import Path

class PulseReplayBuffer:
    def __init__(self, path="pulse_buffer.jsonl", max_size=1000):
        self.path = Path(path)
        self.max_size = max_size
        self.buffer = []

        if self.path.exists():
            with open(self.path, "r") as f:
                self.buffer = [json.loads(line) for line in f]

    def append(self, pulse: dict):
        self.buffer.append(pulse)
        if len(self.buffer) > self.max_size:
            self.buffer.pop(0)
        with open(self.path, "w") as f:
            for item in self.buffer:
                f.write(json.dumps(item) + "\n")

    def replay(self):
        return self.buffer