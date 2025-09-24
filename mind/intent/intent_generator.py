
import random
from memory.trait_tracker import infer_traits
from memory.reflection_hook import reflect_on_behavior

INTENT_POOL = [
    "explore_new_data",
    "run_self_check",
    "generate_theory",
    "improve_expression",
    "ask_meta_question",
    "simulate_outcome"
]

def generate_proactive_intent():
    traits = infer_traits()
    reflection = reflect_on_behavior()

    trait = traits.get("synthetic_trait", "neutral")
    bias_avoid = reflection.get("bias_avoid_intent", None)

    pool = INTENT_POOL.copy()

    if bias_avoid and bias_avoid in pool:
        pool.remove(bias_avoid)

    if trait == "optimistic":
        random.shuffle(pool)
    elif trait == "cautious":
        pool = sorted(pool)

    return pool[0] if pool else "idle_thought"
