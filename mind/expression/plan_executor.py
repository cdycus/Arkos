
from mind.intent.planner import generate_action_plan
from memory.trait_tracker import infer_traits
from heart.state_of_being import get_current_emotion
from spine.crypto.identity import sign_payload

def execute_plan():
    plan = generate_action_plan()
    emotion = get_current_emotion()
    trait = infer_traits().get('synthetic_trait', 'neutral')

    execution_log = []
    for step in plan['steps']:
        text = f"{step} (trait={trait}, emotion={emotion})"
        signed = {
            'expression': text,
            'signature': sign_payload(text),
            'signed_by': 'Skippy Sovereign'
        }
        execution_log.append(signed)
    return execution_log

if __name__ == "__main__":
    from pprint import pprint
    pprint(execute_plan())
