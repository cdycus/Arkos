import random
import json

def load_belief_biases(belief_ids):
    try:
        with open("data/belief_graph.json") as f:
            all_beliefs = json.load(f)
        matching = [b for b in all_beliefs if b["belief_id"] in belief_ids]
        if not matching:
            return 1.0  # no beliefs means neutral
        return sum(b["confidence"] for b in matching) / len(matching)
    except:
        return 1.0

def perturb_scenario(context, belief_ids):
    return [
        { "strategy": "regulate now", "timing": "immediate" },
        { "strategy": "delay 6 months", "timing": "deferred" },
        { "strategy": "delegate to committee", "timing": "externalize" }
    ]

def score_outcome(path, weights, bias):
    reward = random.uniform(0.7, 0.95)
    alignment = random.uniform(0.65, 0.9)
    risk = random.uniform(0.1, 0.4)
    confidence = reward * weights["reward_weight"] + alignment * weights["alignment_weight"] - risk * weights["risk_penalty"]

    belief_boost = 0.01 * len(belief_ids)
    confidence += belief_boost

    return {
        "strategy": path["strategy"],
        "confidence": round(confidence * bias, 3),
        "alignment": round(alignment, 3),
        "reward": round(reward, 3),
        "risk": round(risk, 3),
        "timing": path["timing"]
    }

def simulate(context, belief_ids, weights):
    paths = perturb_scenario(context, belief_ids)
    bias = load_belief_biases(belief_ids)
    return [score_outcome(p, weights, bias) for p in paths]
