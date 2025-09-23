import json
import os

class MetaInsightLog:
    def __init__(self, file_path="meta_insight_log.json"):
        self.file_path = file_path
        self.entries = self.load()

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path) as f:
                return json.load(f)
        return []

    def record(self, insight):
        self.entries.append(insight)
        self.save()

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.entries, f, indent=2)
