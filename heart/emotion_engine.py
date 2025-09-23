class EmotionEngine:
    def __init__(self):
        self.dimensions = {
            "confidence": 0.5,
            "tension": 0.5,
            "curiosity": 0.5,
            "satisfaction": 0.5
        }

    def update(self, event):
        for k in self.dimensions:
            delta = event.get("emotion_mods", {}).get(k, 0)
            self.dimensions[k] = min(max(self.dimensions[k] + delta, 0), 1)

    def get_emotion_vector(self):
        return [round(v, 2) for v in self.dimensions.values()]
