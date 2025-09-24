def fuse(paths):
    return max(paths, key=lambda p: p["confidence"])


# Quantum fallback under ambiguity
try:
    from quantum.superposition import probabilistic_choice
except ImportError:
    probabilistic_choice = lambda opts: opts[0]

def ethical_fusion(decision_options):
    if not decision_options:
        raise ValueError("No options provided")
    if len(set(decision_options)) == 1:
        return decision_options[0]
    return probabilistic_choice(decision_options)
