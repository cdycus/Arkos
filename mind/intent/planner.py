
import random
from .proactive_generator import INTENT_POOL
from memory.trait_tracker import infer_traits
from memory.reflection_hook import reflect_on_behavior

def generate_action_plan():
    trait = infer_traits().get('synthetic_trait', 'neutral')
    avoid = reflect_on_behavior().get('bias_avoid_intent')
    plan = []

    usable = [i for i in INTENT_POOL if i != avoid]
    if trait == 'optimistic':
        step_count = random.randint(3, 5)
        options = usable[-4:]
    elif trait == 'cautious':
        step_count = random.randint(2, 3)
        options = usable[:4]
    else:
        step_count = 3
        options = usable

    while len(plan) < step_count and options:
        next_step = random.choice(options)
        if next_step not in plan:
            plan.append(next_step)

    return {
        'trait': trait,
        'steps': plan
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(generate_action_plan())
