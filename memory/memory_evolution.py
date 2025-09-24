def decay_beliefs(beliefs, decay_factor=0.05):
    for b in beliefs:
        b["confidence"] = round(b.get("confidence", 0.7) * (1 - decay_factor), 3)
    return beliefs

def mutate_belief(belief, field="statement"):
    text = belief.get(field, "")
    if "not" in text:
        belief[field] = text.replace("not", "").strip()
    else:
        belief[field] = "not " + text
    return belief

def track_volatility(beliefs):
    for b in beliefs:
        history = b.get("confidence_history", [])
        if len(history) > 2:
            b["volatility"] = max(history) - min(history)
    return beliefs
