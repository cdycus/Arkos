class InterferenceDetector:
    def detect_conflict(self, futures):
        conflicts = []
        action_keywords = ["scale up", "scale down", "wait", "act", "deploy", "rollback"]
        for i, f1 in enumerate(futures):
            for j, f2 in enumerate(futures):
                if i >= j:
                    continue
                for k in action_keywords:
                    if k in f1["description"].lower() and any(
                        alt for alt in action_keywords if alt != k and alt in f2["description"].lower()
                    ):
                        conflicts.append((f1["id"], f2["id"]))
        return conflicts
