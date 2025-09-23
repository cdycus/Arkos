import json
import requests
import time

REGISTRY_PATH = "Arkos/healthcheck/service_registry.json"
QUARANTINE_PATH = "Arkos/healthcheck/quarantine.json"

def load_registry():
    with open(REGISTRY_PATH, 'r') as f:
        return json.load(f)

def save_quarantine(data):
    with open(QUARANTINE_PATH, 'w') as f:
        json.dump(data, f, indent=2)

def check_services():
    registry = load_registry()
    quarantine = {}
    for name, url in registry.items():
        try:
            res = requests.get(url, timeout=1)
            if res.status_code != 200:
                quarantine[name] = "unhealthy"
        except Exception:
            quarantine[name] = "offline"

    save_quarantine(quarantine)
    return quarantine

if __name__ == "__main__":
    while True:
        quarantine = check_services()
        print("Quarantine List:", quarantine)
        time.sleep(10)