def select_intent(current_state):
    # crude selector based on state trigger
    if current_state.get("emotion") == "uncertain":
        return "trust"
    elif current_state.get("pressure") == "high":
        return "policy"
    elif current_state.get("alignment_score", 1.0) < 0.75:
        return "ethics"
    return "default"
