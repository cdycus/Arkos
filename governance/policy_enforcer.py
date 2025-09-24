def enforce_policy(result, policy_rules):
    for rule in policy_rules:
        if rule["field"] in result:
            val = result[rule["field"]]
            if rule["condition"] == "less_than" and val >= rule["threshold"]:
                return False, rule
            if rule["condition"] == "greater_than" and val <= rule["threshold"]:
                return False, rule
    return True, None
