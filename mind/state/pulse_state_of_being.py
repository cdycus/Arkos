def create_state_pulse(state):
    return {
        "type": "pulse_state_of_being",
        "entropy": state["entropy"],
        "fatigue": state["fatigue"],
        "alignment_score": state["alignment_score"],
        "mood": state["mood"],
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
    }
