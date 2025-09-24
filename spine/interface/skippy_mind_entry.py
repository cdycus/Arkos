import json
from datetime import datetime

from mind.reflection.expression_reflection import build_reflection
from mind.intent.intent_selector import select_intent
from mind.state.state_of_being import compute_state_of_being
from mind.expression.expression_planner import select_expression_type
from mind.expression.expression_impact_tuner import adjust_expression_tone

LOG_PATH = "data/mind_entry_log.jsonl"

def receive_input(payload):
    mode = payload.get("mode", "state")
    context = payload.get("context", {})
    result = {}

    if mode == "reflect":
        pulses = context.get("pulse_history", [])
        result = build_reflection(pulses)

    elif mode == "state":
        history = context.get("pulse_history", [])
        result = compute_state_of_being(history)

    elif mode == "expression":
        mood = context.get("mood", "stable")
        expr_type = select_expression_type({"mood": mood})
        result = {
            "expression_type": expr_type,
            "expression": adjust_expression_tone(f"Skippy reflects: {expr_type}", entropy=context.get("entropy", 0.5))
        }

    elif mode == "intent":
        intent = select_intent(context)
        result = { "intent_selected": intent }

    else:
        result = { "error": f"Unknown mode: {mode}" }

    entry = {
        "input": payload,
        "output": result,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return result
