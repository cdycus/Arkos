def compute_integrity(expressions):
    if len(expressions) < 2:
        return 1.0
    score = 1.0
    recent = [e["text"] for e in expressions[-3:]]
    if any("not" in e and "is" in e for e in recent):
        score -= 0.3
    return round(score, 3)
