def audit_foresight(result):
    anomalies = []
    if result.get("confidence", 1.0) < 0.4:
        anomalies.append("Low confidence foresight")
    if result.get("alignment", 1.0) < 0.5:
        anomalies.append("Misaligned output")
    return anomalies
