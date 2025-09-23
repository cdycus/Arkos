import json
import os

class FeedbackEngine:
    def __init__(self, log_file="feedback_log.json"):
        self.log_file = log_file
        self.log = []

    def record(self, memory_id, result, context=None):
        entry = {
            "memory_id": memory_id,
            "result": result,
            "context": context or {}
        }
        self.log.append(entry)
        self._save()

    def _save(self):
        with open(self.log_file, "w") as f:
            json.dump(self.log, f, indent=2)
