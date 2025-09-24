from mind.reflection.reflection_trace_analyzer import analyze_trace
from mind.reflection.reflection_score.py import score_reflection

def build_reflection(pulses):
    analysis = analyze_trace(pulses)
    score = score_reflection(pulses)
    return {
        "type": "pulse_expression_reflection",
        "summary": analysis,
        "score": score,
        "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
    }
