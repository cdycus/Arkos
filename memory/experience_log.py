
import json
import os
from datetime import datetime

LOG_PATH = os.path.join(os.path.dirname(__file__), "experience_store.jsonl")

def log_experience(intent: str, emotion: str, result: str):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "intent": intent,
        "emotion": emotion,
        "result": result
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

def load_recent_experiences(n=10):
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH, "r") as f:
        lines = f.readlines()[-n:]
        return [json.loads(line) for line in lines]
