
import os
import json
from datetime import datetime
from mind.intent.planner import generate_action_plan

LOG_FILE = os.path.join(os.path.dirname(__file__), "plan_history.jsonl")

def log_plan(plan):
    plan['timestamp'] = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(plan) + "\n")

if __name__ == "__main__":
    plan = generate_action_plan()
    log_plan(plan)
    print("Logged Plan:", plan)
