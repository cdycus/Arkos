
from .experience_log import load_recent_experiences
from collections import Counter

def reflect_on_behavior():
    recent = load_recent_experiences()
    if not recent:
        return {}

    intents = [e['intent'] for e in recent]
    results = [e['result'] for e in recent]

    most_common_intent = Counter(intents).most_common(1)[0][0]
    most_common_result = Counter(results).most_common(1)[0][0]

    return {
        "bias_avoid_intent": most_common_intent if most_common_result == "negative" else None,
        "recent_summary": {
            "common_intent": most_common_intent,
            "common_result": most_common_result
        }
    }
