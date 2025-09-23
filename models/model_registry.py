import json
import os

class ModelRegistry:
    def __init__(self, path='models/model_registry.json'):
        self.path = path
        self.models = self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        return {}

    def register(self, name, version, accuracy, trusted=True):
        self.models[name] = {
            "version": version,
            "accuracy": accuracy,
            "trusted": trusted
        }
        self.save()

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.models, f, indent=2)

    def is_trusted(self, name):
        return self.models.get(name, {}).get("trusted", False)
