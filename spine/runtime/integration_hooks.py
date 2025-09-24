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
