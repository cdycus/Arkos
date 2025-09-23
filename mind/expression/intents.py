class Intent:
    def __init__(self, action, target, confidence, source="mind", metadata=None):
        self.action = action
        self.target = target
        self.confidence = confidence
        self.source = source
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            "action": self.action,
            "target": self.target,
            "confidence": self.confidence,
            "source": self.source,
            "metadata": self.metadata
        }
