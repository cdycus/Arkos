def select_expression_type(context):
    if context.get("drift", False):
        return "alignment_reflection"
    if context.get("emotion") == "low":
        return "resilience_check"
    if context.get("entropy", 0) > 0.7:
        return "state_stability"
    return "general_update"
