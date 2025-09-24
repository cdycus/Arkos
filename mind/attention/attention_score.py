def score_attention(pulse):
    urgency = pulse.get("urgency", 0.5)
    novelty = 1.0 if pulse.get("novel", False) else 0.2
    recency = 1.0 - (pulse.get("age", 0.0) / 10.0)
    score = (urgency * 0.5) + (novelty * 0.3) + (recency * 0.2)
    return round(score, 3)
