class PulseBundler:
    def __init__(self, batch_size=3):
        self.batch_size = batch_size
        self.buffer = []

    def add(self, pulse):
        self.buffer.append(pulse)
        if len(self.buffer) >= self.batch_size:
            return self.flush()
        return []

    def flush(self):
        batch = self.buffer[:]
        self.buffer.clear()
        return batch
