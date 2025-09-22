import json
from datetime import datetime

REGISTRY_FILE = "pulse_peer_registry.json"
LEDGER_FILE = "pulse_ledger.jsonl"

def register_pulse_emitter(pulse_type, node_id):
    now = datetime.utcnow().isoformat() + "Z"
    try:
        with open(REGISTRY_FILE, "r") as f:
            registry = json.load(f)
    except FileNotFoundError:
        registry = {}

    if pulse_type not in registry:
        registry[pulse_type] = []

    if node_id not in [entry["node_id"] for entry in registry[pulse_type]]:
        registry[pulse_type].append({
            "node_id": node_id,
            "first_seen": now,
            "last_seen": now
        })
    else:
        for entry in registry[pulse_type]:
            if entry["node_id"] == node_id:
                entry["last_seen"] = now

    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2)

def log_emitter_pulse(pulse_type, node_id):
    register_pulse_emitter(pulse_type, node_id)
    event = {
        "type": "peer_pulse_seen",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "pulse_type": pulse_type,
        "node_id": node_id
    }
    with open(LEDGER_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")
    print(f"🔎 Registered pulse '{pulse_type}' from node '{node_id}'")

if __name__ == "__main__":
    log_emitter_pulse("pulse_expression", "skippy-alpha-v1")
