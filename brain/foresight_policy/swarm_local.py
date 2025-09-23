import random

def perturb_scenario(context, belief_ids):
    return [
        { "strategy": "regulate now", "timing": "immediate" },
        { "strategy": "delay 6 months", "timing": "deferred" },
        { "strategy": "delegate to committee", "timing": "externalize" }
    ]

def score_outcome(path, weights):
    reward = random.uniform(0.7, 0.95)
    alignment = random.uniform(0.65, 0.9)
    risk = random.uniform(0.1, 0.4)
    confidence = reward * weights["reward_weight"] + alignment * weights["alignment_weight"] - risk * weights["risk_penalty"]
    return {
        "strategy": path["strategy"],
        "confidence": round(confidence, 3),
        "alignment": round(alignment, 3),
        "reward": round(reward, 3),
        "risk": round(risk, 3),
        "timing": path["timing"]
    }

def simulate(context, belief_ids, weights):
    paths = perturb_scenario(context, belief_ids)
    return [score_outcome(p, weights) for p in paths]
