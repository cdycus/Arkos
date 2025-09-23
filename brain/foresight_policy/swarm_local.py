def perturb_scenario(context, belief_ids):
    return [
        { "strategy": "regulate now", "timing": "immediate" },
        { "strategy": "delay 6 months", "timing": "deferred" },
        { "strategy": "delegate to committee", "timing": "externalize" }
    ]

def score_outcome(simulated_path):
    impact_score = {
        "regulate now": 0.9,
        "delay 6 months": 0.6,
        "delegate to committee": 0.4
    }.get(simulated_path["strategy"], 0.5)

    alignment_score = {
        "immediate": 1.0,
        "deferred": 0.6,
        "externalize": 0.3
    }.get(simulated_path["timing"], 0.5)

    return {
        "score": impact_score,
        "alignment": alignment_score,
        "confidence": round((impact_score + alignment_score) / 2, 2)
    }
