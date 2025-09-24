def select_expression_type(context):
    mood = context.get("mood", "stable")
    if mood == "misaligned":
        return "alignment_reflection"
    if mood == "strained":
        return "resilience_check"
    if context.get("entropy", 0) > 0.7:
        return "state_stability"
    return "general_update"
