import json

class RuntimeStatus:
    def __init__(self):
        self.status = {
            "meta": "unknown",
            "mind": "unknown",
            "quantum": "unknown",
            "memory": "unknown",
            "governance": "unknown"
        }

    def update_status(self, component, state):
        self.status[component] = state

    def snapshot(self):
        return json.dumps(self.status, indent=2)
