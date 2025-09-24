
import json
import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), "adaptive_behavior_log.jsonl")

def log_behavior_bias(info: dict):
    info['timestamp'] = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(info) + "\n")
