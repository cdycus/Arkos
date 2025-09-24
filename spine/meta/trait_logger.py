
import json
import os
from datetime import datetime
from memory.trait_tracker import infer_traits

LOG_FILE = os.path.join(os.path.dirname(__file__), "trait_history.jsonl")

def log_current_trait():
    traits = infer_traits()
    traits['timestamp'] = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(traits) + "\n")
    return traits

if __name__ == "__main__":
    print("Logging current synthetic trait...")
    print(log_current_trait())
