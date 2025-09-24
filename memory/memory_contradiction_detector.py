def detect_contradictions(beliefs):
    seen = {}
    conflicts = []
    for b in beliefs:
        statement = b.get("statement", "")
        norm = statement.lower().strip().split()
        key = frozenset(norm)
        if key in seen and seen[key] != statement:
            conflicts.append((seen[key], statement))
        seen[key] = statement
    return conflicts
