class ReplayBuffer:
    def __init__(self, max_size=10):
        self.buffer = []
        self.max_size = max_size

    def add(self, memory):
        self.buffer.append(memory)
        if len(self.buffer) > self.max_size:
            self.buffer.pop(0)

    def get_recent(self):
        return self.buffer[-1] if self.buffer else None

    def list_all(self):
        return self.buffer
