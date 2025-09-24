import heapq

class FocusQueue:
    def __init__(self):
        self.queue = []

    def add(self, pulse, score):
        heapq.heappush(self.queue, (-score, pulse))

    def top(self):
        return self.queue[0][1] if self.queue else None

    def snapshot(self):
        return [p for _, p in sorted(self.queue, reverse=True)]
