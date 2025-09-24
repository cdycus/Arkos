
import random
from memory.trait_tracker import infer_traits
from memory.reflection_hook import reflect_on_behavior

INTENT_POOL = [
    "explore_new_topic",
    "ask_for_feedback",
    "generate_idea",
    "check_system_health",
    "reflect_out_loud",
    "document_learning"
]

def generate_proactive_intent():
    trait = infer_traits().get("synthetic_trait", "neutral")
    avoid = reflect_on_behavior().get("bias_avoid_intent")

    options = [i for i in INTENT_POOL if i != avoid]
    if trait == "optimistic":
        return random.choice(options[-3:])
    elif trait == "cautious":
        return random.choice(options[:3])
    return random.choice(options)

if __name__ == "__main__":
    print("Proactive Intent:", generate_proactive_intent())
