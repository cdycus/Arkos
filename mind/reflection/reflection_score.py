def score_reflection(pulses):
    if not pulses:
        return 0.0
    avg_conf = sum(p.get("confidence", 0.5) for p in pulses[-5:]) / min(5, len(pulses))
    variability = len(set(p["decision"] for p in pulses[-5:] if "decision" in p))
    penalty = variability * 0.05
    return round(avg_conf - penalty, 3)
