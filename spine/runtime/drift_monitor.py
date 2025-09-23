import json, os

class DriftMonitor:
    def __init__(self, trace_path="data/foresight_trace.jsonl"):
        self.path = trace_path

    def get_recent_alignment(self, window=5):
        if not os.path.exists(self.path):
            return []
        with open(self.path) as f:
            lines = f.readlines()[-window:]
        values = []
        for l in lines:
            try:
                entry = json.loads(l)
                if "alignment" in entry.get("result", {}):
                    values.append(entry["result"]["alignment"])
            except:
                continue
        return values

    def detect_drift(self, current):
        history = self.get_recent_alignment()
        if len(history) < 2:
            return False
        avg = sum(history) / len(history)
        return current < avg * 0.9
