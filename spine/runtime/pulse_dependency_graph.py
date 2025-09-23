class DependencyGraph:
    def __init__(self):
        self.rules = {
            "pulse_foresight_result": ["pulse_foresight_trigger"],
            "pulse_feedback": ["pulse_foresight_result"],
            "pulse_expression": ["pulse_feedback"]
        }

    def is_blocked(self, pulse_type, emitted_types):
        required = self.rules.get(pulse_type, [])
        return any(req not in emitted_types for req in required)
