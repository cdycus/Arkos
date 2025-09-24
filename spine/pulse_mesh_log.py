import json
import time
import os

LOG_PATH = "data/audit/pulse_mesh_log.jsonl"

def log_tick_status(name, status, duration, summary):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    entry = {
        "tick": name,
        "status": status,
        "duration_ms": round(duration * 1000, 2),
        "summary": summary,
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")