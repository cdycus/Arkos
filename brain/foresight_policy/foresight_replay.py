import json
import os

class ForesightReplay:
    def __init__(self, delta_log_path="delta_registry.json"):
        self.delta_log_path = delta_log_path
        self.deltas = self.load_deltas()

    def load_deltas(self):
        if os.path.exists(self.delta_log_path):
            with open(self.delta_log_path) as f:
                return json.load(f)
        return []

    def score_delta(self, predicted_conf, actual_score):
        return round(actual_score - predicted_conf, 3)

    def emit_delta_feedback(self, trace_id, predicted_conf, actual_score, action_taken, used):
        delta = self.score_delta(predicted_conf, actual_score)
        entry = {
            "trace_id": trace_id,
            "predicted_confidence": predicted_conf,
            "actual_outcome_score": actual_score,
            "delta": delta,
            "action_taken": action_taken,
            "used": used,
            "error_class": "overconfident" if delta < -0.2 else "accurate" if abs(delta) < 0.1 else "underconfident"
        }
        self.deltas.append(entry)
        self.save_log()

    def save_log(self):
        with open(self.delta_log_path, "w") as f:
            json.dump(self.deltas, f, indent=2)
