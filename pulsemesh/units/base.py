class PulseUnit:
    def __init__(self, name: str, config: dict):
        self.name = name
        self.config = config

    def should_emit(self, context: dict) -> bool:
        return True

    def emit(self) -> dict:
        return {
            "type": self.name,
            "timestamp": 0
        }