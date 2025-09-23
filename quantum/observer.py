class ObserverTracker:
    def __init__(self, focus_tags=None):
        self.focus_tags = focus_tags or []

    def get_focus_bias(self, future):
        description = future["description"].lower()
        bias = 0.0
        for tag in self.focus_tags:
            if tag.lower() in description:
                bias += 0.15
        return round(min(bias, 0.5), 2)
