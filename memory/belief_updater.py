def update_beliefs_from_expression(beliefs, expression_text):
    updated = []
    for b in beliefs:
        if b["statement"].lower() in expression_text.lower():
            b["confidence"] = min(1.0, b.get("confidence", 0.5) + 0.05)
            b["used"] = b.get("used", 0) + 1
            updated.append(b)
    return updated
