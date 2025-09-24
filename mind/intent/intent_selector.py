def select_intent(context):
    if context.get("mood") == "misaligned":
        return "restore_alignment"
    if context.get("fatigue", 0) > 0.7:
        return "recovery"
    if context.get("entropy", 0) > 0.6:
        return "stability"
    return "exploration"
