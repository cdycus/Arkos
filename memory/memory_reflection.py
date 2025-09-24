def selfcheck_beliefs(beliefs):
    seen = {}
    contradictions = []
    for b in beliefs:
        key = b["statement"].strip().lower().replace("not ", "")
        if key in seen and seen[key] != b["statement"]:
            contradictions.append((seen[key], b["statement"]))
        seen[key] = b["statement"]
    return contradictions

def summarize_memory_state(beliefs, limit=5):
    summaries = []
    for b in beliefs[:limit]:
        summaries.append(f"Belief '{b['statement']}' (conf: {b['confidence']})")
    return summaries

def time_filtered_beliefs(beliefs, year="2025"):
    return [b for b in beliefs if b["timestamp"].startswith(year)]

def identify_memory_risks(beliefs):
    return [b for b in beliefs if b.get("volatility", 0) > 0.3]
