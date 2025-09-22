import json
import logging
import requests
import uuid
from pathlib import Path

logger = logging.getLogger("skippy-router")

# Track recently seen core_brain IDs to prevent rebroadcast loops
seen_pulses = set()

def load_mesh():
    mesh_path = Path("/app/mesh.json")
    if not mesh_path.exists():
        logger.warning("mesh.json not found, no peers configured")
        return {"self": "unknown", "peers": []}
    with open(mesh_path) as f:
        return json.load(f)

def broadcast_pulse(pulse: dict):
    """Broadcast a pulse to all peers in the mesh.json file."""
    mesh = load_mesh()

    pulse_id = str(uuid.uuid4())
    payload = {
        "emitter": mesh.get("self", "unknown"),
        "pulse_id": pulse_id,
        "payload": pulse
    }

    # Track locally to prevent rebroadcast
    seen_pulses.add(pulse_id)

    for peer in mesh.get("peers", []):
        try:
            url = f"{peer}/pulse/inject"
            r = requests.post(url, json=payload, timeout=2)
            logger.info(f"Forwarded pulse to {peer}, status {r.status_code}")
        except Exception as e:
            logger.error(f"Failed to forward pulse to {peer}: {e}")

def inject_pulse(pulse: dict):
    """Inject a pulse received from another core into the local ledger."""
    pulse_id = pulse.get("pulse_id")
    if not pulse_id:
        logger.error("Received pulse without pulse_id")
        return False

    if pulse_id in seen_pulses:
        logger.info(f"Ignoring already-seen core_brain: {pulse_id}")
        return True  # Not an error, just skip

    seen_pulses.add(pulse_id)

    try:
        from spine.ledger.ledger import PulseLedger
        ledger = PulseLedger()
        ledger.append(pulse["payload"], broadcast=False)
        logger.info(f"Injected pulse from {pulse.get('emitter')}: {pulse}")
        return True
    except Exception as e:
        logger.error(f"Failed to inject pulse: {e}")
        return False
