class ErrorRouter:
    def __init__(self):
        self.errors = []

    def handle(self, source, message, level="error"):
        error_obj = {
            "source": source,
            "message": message,
            "level": level
        }
        self.errors.append(error_obj)
        print(f"[{level.upper()}] {source} → {message}")
        return error_obj
