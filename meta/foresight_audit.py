import json
import os

class ForesightAudit:
    def __init__(self, trace_path="delta_registry.json", threshold=0.2):
        self.trace_path = trace_path
        self.threshold = threshold
        self.drift_flags = []

    def run_audit(self):
        if not os.path.exists(self.trace_path):
            return []

        with open(self.trace_path) as f:
            traces = json.load(f)

        for t in traces:
            if abs(t["delta"]) > self.threshold:
                self.drift_flags.append({
                    "trace_id": t["trace_id"],
                    "delta": t["delta"],
                    "error_class": t["error_class"]
                })

        return self.drift_flags


class DriftPredictor:
    def predict_drift(self, delta):
        return "likely_recurrence" if abs(delta) > 0.25 else "transient"
