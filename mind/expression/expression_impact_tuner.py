def adjust_expression_tone(base, entropy=0.0, urgency=0.0):
    tone = "calm"
    if urgency > 0.6 or entropy > 0.7:
        tone = "urgent"
    elif urgency > 0.3 or entropy > 0.4:
        tone = "cautious"
    return f"[{tone}] {base}"
