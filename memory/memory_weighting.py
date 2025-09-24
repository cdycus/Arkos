def apply_weights(beliefs):
    for b in beliefs:
        age = 2025 - int(b.get("timestamp", "2023").split("-")[0])
        volatility = 1.0 if b.get("volatile", False) else 0.5
        b["weight"] = round(b.get("confidence", 0.7) / (age + 1) * volatility, 3)
    return beliefs
