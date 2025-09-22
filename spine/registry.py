
import json

class PulseRegistry:
    def __init__(self, config_path):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.units = {}

    def register(self, name, unit):
        self.units[name] = unit

    def get_units(self):
        return self.units.items()

    def get_config(self):
        return self.config

    def get_active_units(self):
        return list(self.units.values())
