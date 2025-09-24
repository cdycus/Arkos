import json
import os
from statistics import mean

class ExpressionEngine:
    def __init__(self):
        self.foresight_path = "data/foresight_trace.jsonl"
        self.belief_path = "data/belief_graph.json"
        self.expression_log = "data/expression_trace.jsonl"

    def summarize_foresight(self, window=5):
        if not os.path.exists(self.foresight_path):
            return "No foresight data."
        with open(self.foresight_path) as f:
            lines = f.readlines()[-window:]
        alignments = []
        strategies = []
        for l in lines:
            try:
                entry = json.loads(l)
                alignments.append(entry["result"]["alignment"])
                strategies.append(entry["result"]["strategy"])
            except:
                continue
        avg_align = round(mean(alignments), 3) if alignments else "N/A"
        most_common_strategy = max(set(strategies), key=strategies.count) if strategies else "N/A"
        return f"In the last {window} foresight cycles, avg alignment: {avg_align}, strategy: {most_common_strategy}"

    def summarize_beliefs(self):
        if not os.path.exists(self.belief_path):
            return "No beliefs stored."
        with open(self.belief_path) as f:
            beliefs = json.load(f)
        recent = beliefs[-3:] if beliefs else []
        lines = [f"Belief: {b['statement']} (conf: {b['confidence']})" for b in recent]
        return "Recent beliefs:\n" + "\n".join(lines)

    def generate_report(self):
        foresight = self.summarize_foresight()
        beliefs = self.summarize_beliefs()
        report = f"🧠 Skippy Expression\n{foresight}\n{beliefs}"
        self.log_expression(report)
        return report

    def log_expression(self, report):
        entry = {
            "type": "pulse_expression",
            "text": report,
            "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
        }
        os.makedirs("data", exist_ok=True)
        with open(self.expression_log, "a") as f:
            f.write(json.dumps(entry) + "\n")


# Emotional influence injection
try:
    from heart.state_of_being import get_current_emotion
except ImportError:
    def get_current_emotion():
        return "neutral"

def apply_emotion_to_expression(expression):
    emotion = get_current_emotion()
    return f"{expression} [{emotion}]"


# Injected: Sovereign signature for expression output
try:
    from spine.crypto.identity import sign_payload
except ImportError:
    sign_payload = lambda x: "unsigned"

def sovereign_expression(text):
    return {
        "expression": text,
        "signature": sign_payload(text),
        "signed_by": "Skippy Sovereign"
    }


# Injected: Reflection bias hook
try:
    from memory.reflection_hook import reflect_on_behavior
except ImportError:
    reflect_on_behavior = lambda: {}

def bias_expression_choice(candidates):
    bias = reflect_on_behavior().get('bias_avoid_intent')
    if bias and bias in candidates:
        candidates.remove(bias)
    return candidates[0] if candidates else "fallback_expression"
