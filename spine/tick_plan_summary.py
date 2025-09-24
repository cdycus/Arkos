# tick_plan_summary.py

import json
import os
import time

SUMMARY_PATH = "data/audit/tick_plan_summary.jsonl"

def emit_plan(tick, deps, retries, fallback):
    os.makedirs(os.path.dirname(SUMMARY_PATH), exist_ok=True)
    entry = {
        "tick": tick,
        "dependencies": deps,
        "retries": retries,
        "fallback_triggered": fallback,
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    with open(SUMMARY_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")