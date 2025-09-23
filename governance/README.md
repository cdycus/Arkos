# Governance Layer

This module governs Skippy's foresight and decision logic. It includes:

- `audit_engine.py` — checks foresight results for confidence thresholds
- `policy_enforcer.py` — applies written rules to intents
- `escalation_log.py` — logs all overrides or policy violations

Policy file: `policy_rules.json` defines intent-level blocking rules.
