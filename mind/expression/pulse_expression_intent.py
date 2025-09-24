def build_expression_intent(reason, pulse_id=None):
    return {
        "type": "pulse_expression_intent",
        "reason": reason,
        "linked_pulse": pulse_id,
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
    }
