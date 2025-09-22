class MetaPulseHealth:
    def __init__(self, config):
        self.config = config

    def report(self):
        return {
            "unit_count": len(self.config.get("active_units", []))
        }