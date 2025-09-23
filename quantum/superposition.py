import random

class SuperpositionEngine:
    def __init__(self, context):
        self.context = context
        self.future_templates = {
            "scaling": [
                {"description": "Scale up immediately"},
                {"description": "Wait for trend confirmation"},
                {"description": "Trigger autoscaling logic"}
            ],
            "performance": [
                {"description": "Optimize database"},
                {"description": "Reduce load via cache"},
                {"description": "Alert developer team"}
            ],
            "default": [
                {"description": "Log and monitor"},
                {"description": "Do nothing"},
                {"description": "Request human input"}
            ]
        }

    def generate_futures(self):
        tag = self.context.thought.get("category", "default")
        templates = self.future_templates.get(tag, self.future_templates["default"])

        self.context.possible_futures = []
        for i, temp in enumerate(templates):
            self.context.possible_futures.append({
                "id": f"{tag[:3].upper()}-{i}",
                "description": temp["description"],
                "probability": round(random.uniform(0.3, 0.9), 2)
            })

        return self.context.possible_futures
