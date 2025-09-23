def fuse(paths):
    return max(paths, key=lambda p: p["confidence"])
