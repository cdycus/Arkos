def fuse(paths):
    sorted_paths = sorted(paths, key=lambda p: p["confidence"], reverse=True)
    best = sorted_paths[0]
    return {
        "decision": best["strategy"],
        "confidence": best["confidence"],
        "fused_trace": best
    }
