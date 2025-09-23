class ModelTuner:
    def __init__(self):
        self.config = {
            "swarm_size": 5,
            "confidence_bias": 1.0
        }

    def tune(self, audit_results):
        for drift in audit_results:
            if drift["error_class"] == "overconfident":
                self.config["confidence_bias"] *= 0.95
            elif drift["error_class"] == "underconfident":
                self.config["confidence_bias"] *= 1.05
        return self.config
