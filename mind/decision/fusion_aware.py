import json

def fuse_with_modifiers(paths, beliefs=[], drift_score=0.0):
    weights = {
        "confidence_weight": 1.0 - drift_score,
        "belief_boost": 0.01 * len(beliefs)
    }

    for p in paths:
        p["score"] = round(p["confidence"] * weights["confidence_weight"] + weights["belief_boost"], 3)

    sorted_paths = sorted(paths, key=lambda p: p["score"], reverse=True)
    best = sorted_paths[0]
    return best, weights
