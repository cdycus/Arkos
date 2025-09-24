def compute_state_of_being(pulse_history, drift_count=0):
    total_conf = sum(p.get("confidence", 0.5) for p in pulse_history[-5:])
    avg_conf = total_conf / max(1, len(pulse_history[-5:]))
    entropy = 1.0 - avg_conf
    fatigue = min(1.0, len(pulse_history) / 50.0)
    alignment = max(0.0, avg_conf - drift_count * 0.05)

    state = {
        "entropy": round(entropy, 3),
        "fatigue": round(fatigue, 3),
        "alignment_score": round(alignment, 3),
        "mood": "stable"
    }

    if state["entropy"] > 0.6 or state["fatigue"] > 0.8:
        state["mood"] = "strained"
    if state["alignment_score"] < 0.5:
        state["mood"] = "misaligned"
    return state
