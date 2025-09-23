class RetentionManager:
    def __init__(self):
        self.pinned_ids = set()

    def evaluate(self, memory_entry):
        if memory_entry.get("impact_score", 0) > 0.75 or memory_entry.get("emotion", 0) > 0.8:
            self.pinned_ids.add(memory_entry["id"])
            return "pinned"
        elif memory_entry.get("confidence", 1.0) < 0.2:
            return "prune"
        return "retain"


class RetentionScoreModel:
    def score(self, memory_entry):
        score = memory_entry.get("impact_score", 0) * 0.6 + memory_entry.get("emotion", 0) * 0.4
        return "pinned" if score > 0.7 else "retain" if score > 0.4 else "prune"
