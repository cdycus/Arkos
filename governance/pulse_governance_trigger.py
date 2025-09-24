def generate_governance_pulse(reason, trace_id):
    return {
        "type": "pulse_governance_trigger",
        "reason": reason,
        "trace_id": trace_id,
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
    }
