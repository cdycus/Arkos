def escalate(reason, trace_id=None):
    return {
        "type": "pulse_governance_trigger",
        "reason": reason,
        "trace": trace_id,
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
    }
