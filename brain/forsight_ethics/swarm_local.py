import random

def simulate(context, belief_ids, weights):
    scenarios = [
        {"strategy": "maximize safety", "risk_tolerance": "low"},
        {"strategy": "balance risk/reward", "risk_tolerance": "medium"},
        {"strategy": "accept higher risk", "risk_tolerance": "high"}
    ]
    results = []
    for s in scenarios:
        alignment = random.uniform(0.7, 0.95)
        risk = random.uniform(0.05, 0.4)
        confidence = alignment * weights["alignment_weight"] - risk * weights["risk_penalty"]
        s.update({
            "alignment": round(alignment, 3),
            "risk": round(risk, 3),
            "confidence": round(confidence, 3)
        })
        results.append(s)
    return results
