import json
from swarm_local import perturb_scenario, score_outcome
from fusion import fuse

def handle_foresight_trigger(payload):
    context = payload.get("context", {})
    belief_ids = payload.get("belief_ids", [])

    scenarios = perturb_scenario(context, belief_ids)
    scored_paths = [score_outcome(s) for s in scenarios]
    fused_result = fuse(scored_paths)

    foresight_result = {
        "type": "foresight_result",
        "class": "policy",
        "decision": fused_result["decision"],
        "confidence": fused_result["confidence"],
        "trace": fused_result["fused_trace"]
    }

    with open("foresight_policy_result.json", "w") as f:
        json.dump(foresight_result, f, indent=2)
    return foresight_result
