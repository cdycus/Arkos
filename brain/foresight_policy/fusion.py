def fuse(paths):
    sorted_paths = sorted(paths, key=lambda x: x["confidence"], reverse=True)
    best = sorted_paths[0]
    return {
        "decision": best["strategy"],
        "confidence": best["confidence"],
        "alignment": best["alignment"],
        "trace": best
    }
