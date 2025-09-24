
import json
from memory.reflection_hook import reflect_on_behavior
from memory.trait_tracker import infer_traits

STATE_FILE = "meta_skippy_state.json"

def update_skippy_state():
    reflection = reflect_on_behavior()
    traits = infer_traits()

    state = {
        "alignment_score": reflection.get("alignment_score", 0),
        "bias_avoid_intent": reflection.get("bias_avoid_intent"),
        "synthetic_trait": traits.get("synthetic_trait"),
        "dominant_emotion": traits.get("dominant_emotion"),
        "positivity_ratio": traits.get("positivity_ratio"),
    }

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

    return state

if __name__ == "__main__":
    print("🧠 Updated Skippy Self-Awareness State:")
    print(update_skippy_state())
