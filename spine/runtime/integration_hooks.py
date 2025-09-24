import json
from mind.expression.expression_planner import select_expression_type
from mind.expression.expression_impact_tuner import adjust_expression_tone
from mind.expression.pulse_expression_intent import build_expression_intent
from mind.expression.expression_integrity_score import compute_integrity

from governance.audit_engine import audit_foresight
from governance.policy_enforcer import enforce_policy
from governance.governance_escalator import escalate

from memory.memory_evolution import decay_beliefs
from memory.memory_reflection import selfcheck_beliefs
from memory.memory_weighting import apply_weights

def run_post_tick_hooks(state):
    if not state.get("enable_hooks", True):
        return []

    logs = []

    if state.get("enable_expression", True):
        expr_type = select_expression_type(state.get("context", {}))
        logs.append(f"Expression type selected: {expr_type}")

    if state.get("enable_memory_decay", True):
        beliefs = state.get("beliefs", [])
        updated = decay_beliefs(beliefs)
        logs.append(f"Beliefs decayed: {len(updated)}")

    if state.get("enable_governance", True):
        result = state.get("foresight_result", {})
        anomalies = audit_foresight(result)
        if anomalies:
            logs.append(f"Governance anomaly: {anomalies}")
            ok, rule = enforce_policy(result, [{"field": "confidence", "condition": "less_than", "threshold": 0.5}])
            if not ok:
                alert = escalate("Policy violation", result.get("trace"))
                logs.append(f"Governance escalation triggered: {alert}")

    return logs


from mind.decision.pulse_feedback_tracer import trace_feedback
from memory.retention_manager import score_belief
from memory.memory_weighting import apply_weights

def process_feedback_and_memory(pulse, feedback_outcome="success"):
    logs = []
    fb_trace = trace_feedback(pulse, feedback_outcome)
    logs.append(f"Feedback Traced: {fb_trace}")

    if "beliefs" in pulse:
        for b in pulse["beliefs"]:
            b["retention_score"] = score_belief(b)
        pulse["beliefs"] = apply_weights(pulse["beliefs"])
        logs.append(f"Beliefs updated: {len(pulse['beliefs'])}")

    return logs


from mind.expression.expression_planner import select_expression_type
from mind.expression.expression_impact_tuner import adjust_expression_tone
from mind.expression.pulse_expression_intent import build_expression_intent
import json, os

def emit_expression():
    expr_type = select_expression_type({"entropy": 0.6})
    base_text = f"Skippy expressing: {expr_type}"
    tuned = adjust_expression_tone(base_text, entropy=0.6)

    intent = build_expression_intent(expr_type)

    os.makedirs("data", exist_ok=True)
    log_path = "data/expression_snapshot_log.jsonl"
    with open(log_path, "a") as f:
        f.write(json.dumps({
            "intent": intent,
            "expression": tuned,
            "timestamp": intent["timestamp"]
        }) + "\n")

    return tuned


from memory.belief_updater import update_beliefs_from_expression

def refresh_beliefs(beliefs, last_expression_text):
    updated = update_beliefs_from_expression(beliefs, last_expression_text)
    return updated


from mind.state.state_of_being import compute_state_of_being
from mind.state.pulse_state_of_being import create_state_pulse

def update_state(pulse_history):
    state = compute_state_of_being(pulse_history)
    pulse = create_state_pulse(state)
    with open("data/mood_log.jsonl", "a") as f:
        import json
        f.write(json.dumps(pulse) + "\n")
    return state
