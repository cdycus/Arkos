class AuditEngine:
    def __init__(self, threshold=0.7):
        self.threshold = threshold

    def evaluate(self, foresight_result):
        confidence = foresight_result.get("confidence", 0.0)
        if confidence < self.threshold:
            return {
                "status": "block",
                "reason": "Confidence below threshold",
                "confidence": confidence
            }
        return {"status": "pass", "confidence": confidence}


class ConfidenceAnomalyDetector:
    def detect(self, foresight_result):
        if foresight_result.get("confidence", 0) < 0.4:
            return "low_confidence_anomaly"
        return "normal"
