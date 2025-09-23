import json

class MetaInsightLog:
    def __init__(self, path="meta_insight_log.json"):
        self.path = path
        self.entries = []

    def record(self, insight):
        self.entries.append(insight)
        self.save()

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.entries, f, indent=2)
