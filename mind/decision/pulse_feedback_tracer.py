def trace_feedback(pulse, feedback_outcome):
    return {
        "pulse_id": pulse.get("pulse_id"),
        "type": pulse.get("type"),
        "decision": pulse.get("decision", "N/A"),
        "feedback": feedback_outcome,
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
    }
