def generate_memory_alerts(beliefs):
    alerts = []
    for b in beliefs:
        if b.get("volatility", 0) > 0.4:
            alerts.append({
                "type": "pulse_memory_policy_signal",
                "belief_id": b["belief_id"],
                "concern": "high volatility",
                "statement": b["statement"]
            })
        if b.get("confidence", 0.0) < 0.2:
            alerts.append({
                "type": "pulse_memory_policy_signal",
                "belief_id": b["belief_id"],
                "concern": "low confidence",
                "statement": b["statement"]
            })
    return alerts
