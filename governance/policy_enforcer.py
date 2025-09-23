import json
import os

class PolicyEnforcer:
    def __init__(self, rules_path="policy_rules.json"):
        self.rules_path = rules_path
        self.rules = self.load_rules()

    def load_rules(self):
        if os.path.exists(self.rules_path):
            with open(self.rules_path) as f:
                return json.load(f)
        return {}

    def apply(self, intent):
        for rule in self.rules.get("blocks", []):
            if rule["target"] == intent["target"] and rule["action"] == intent["action"]:
                return {
                    "status": "blocked",
                    "reason": rule["reason"]
                }
        return {"status": "allowed"}
