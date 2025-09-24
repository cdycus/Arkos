from mind.expression.expression_planner import select_expression_type
from mind.expression.expression_impact_tuner import adjust_expression_tone
from mind.expression.pulse_expression_intent import build_expression_intent
from memory.belief_updater import update_beliefs_from_expression
from mind.decision.pulse_feedback_tracer import trace_feedback
from memory.retention_manager import score_belief
from memory.memory_weighting import apply_weights

import json, os
from datetime import datetime

def simulate_tick():
    pulse = {
        "pulse_id": "tick_001",
        "type": "pulse_foresight_result",
        "decision": "regulate now",
        "confidence": 0.83,
        "beliefs": [
            {"statement": "regulation improves outcome", "confidence": 0.7, "used": 2, "timestamp": "2024-01-01"},
            {"statement": "risk is elevated", "confidence": 0.6, "used": 5, "timestamp": "2023-08-01"}
        ]
    }

    print("\n▶️ TICK START")
    print("🧠 Pulse:", pulse["type"], "| Decision:", pulse["decision"])

    feedback = trace_feedback(pulse, "success")
    print("✅ Feedback:", feedback)

    for b in pulse["beliefs"]:
        b["retention_score"] = score_belief(b)
    weighted = apply_weights(pulse["beliefs"])
    print("📚 Beliefs weighted:", weighted)

    expr_type = select_expression_type({"entropy": 0.6})
    base = f"Skippy reflecting on decision: {pulse['decision']}"
    expr_text = adjust_expression_tone(base, entropy=0.6)
    print("🗣️ Expression:", expr_text)

    updated_beliefs = update_beliefs_from_expression(weighted, expr_text)
    print("🔁 Beliefs after expression refresh:", updated_beliefs)

    os.makedirs("data", exist_ok=True)
    with open("data/expression_snapshot_log.jsonl", "a") as log:
        log.write(json.dumps({
            "intent": build_expression_intent(expr_type),
            "expression": expr_text,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }) + "\n")

if __name__ == "__main__":
    simulate_tick()
