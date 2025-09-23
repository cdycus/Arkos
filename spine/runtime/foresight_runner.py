import time, json
from brain.foresight_policy import swarm_local, fusion

def run_foresight_class(f_class, context, belief_ids):
    if f_class != "policy":
        raise ValueError("Only 'policy' foresight class is implemented.")

    with open("brain/foresight_policy/config.json") as f:
        weights = json.load(f)

    results = swarm_local.simulate(context, belief_ids, weights)
    fused = fusion.fuse(results)

    trace = {
        "pulse_id": f"foresight_{int(time.time())}",
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
        "decision": fused["decision"],
        "confidence": fused["confidence"],
        "trace": trace["pulse_id"],
        "timestamp": trace["timestamp"]
    }

    return foresight_result
