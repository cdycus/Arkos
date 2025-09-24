def create_perception_pulse(input_type, source, meta=None):
    return {
        "type": "pulse_perception_event",
        "input_type": input_type,
        "source": source,
        "meta": meta or {},
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
    }
