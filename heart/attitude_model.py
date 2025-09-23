class AttitudeModel:
    def __init__(self):
        self.mode = "neutral"
        self.counters = {
            "successes": 0,
            "failures": 0
        }

    def update(self, foresight_result):
        if foresight_result.get("used") and foresight_result.get("delta", 0) >= 0:
            self.counters["successes"] += 1
        else:
            self.counters["failures"] += 1

        if self.counters["failures"] > self.counters["successes"]:
            self.mode = "defensive"
        elif self.counters["successes"] > self.counters["failures"]:
            self.mode = "assertive"
        else:
            self.mode = "exploratory"

    def get_attitude(self):
        return self.mode


class AttitudeBayes:
    def update_state(self, successes, failures):
        # Simple posterior estimator
        total = successes + failures
        p_success = successes / total if total else 0.5
        if p_success > 0.7:
            return "assertive"
        elif p_success < 0.3:
            return "defensive"
        return "neutral"
