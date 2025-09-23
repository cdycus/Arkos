import time, json

from brain.foresight_policy import swarm_local as policy_swarm, fusion as policy_fusion
from brain.foresight_ethics import swarm_local as ethics_swarm, fusion as ethics_fusion
from brain.foresight_trust import swarm_local as trust_swarm, fusion as trust_fusion

def run_foresight_class(f_class, context, belief_ids):
    if f_class == "policy":
        with open("brain/foresight_policy/config.json") as f:
            weights = json.load(f)
        results = policy_swarm.simulate(context, belief_ids, weights)
        fused = policy_fusion.fuse(results)

    elif f_class == "ethics":
        with open("brain/foresight_ethics/config.json") as f:
            weights = json.load(f)
        results = ethics_swarm.simulate(context, belief_ids, weights)
        fused = ethics_fusion.fuse(results)

    elif f_class == "trust":
        with open("brain/foresight_trust/config.json") as f:
            weights = json.load(f)
        results = trust_swarm.simulate(context, belief_ids, weights)
        fused = trust_fusion.fuse(results)

    else:
        raise ValueError("Unsupported foresight class")

    pulse_id = f"foresight_{int(time.time())}"
    trace = {
        "pulse_id": pulse_id,
        "class": f_class,
        "context": context,
        "result": fused,
        "timestamp": int(time.time())
    }

    with open("data/foresight_trace.jsonl", "a") as log:
        log.write(json.dumps(trace) + "\n")

    foresight_result = {
        "type": "pulse_foresight_result",
        "class": f_class,
        "decision": fused.get("strategy", fused.get("agent")),
        "confidence": fused["confidence"],
        "trace": pulse_id,
        "timestamp": trace["timestamp"]
    }

    return foresight_result
