def analyze_trace(pulses):
    decisions = [p["decision"] for p in pulses if "decision" in p]
    shift = len(set(decisions[-5:]))
    return {
        "recent_decisions": decisions[-5:],
        "decision_variability": shift
    }
