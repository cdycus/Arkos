import heapq
import time

class PulsePriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, pulse, priority):
        decay = 1.0 / (1 + (time.time() - pulse.get("timestamp", time.time())))
        adjusted_priority = priority * decay
        heapq.heappush(self.queue, (-adjusted_priority, pulse))

    def dequeue(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]
        return None

    def is_empty(self):
        return len(self.queue) == 0
