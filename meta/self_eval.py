import datetime

def evaluate_thought_chain(thought, outcome, state):
    log = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "thought": thought,
        "outcome": outcome,
        "state_of_being": state,
        "confidence": outcome.get("confidence", 0.5)
    }
    with open("meta/self_eval.log", "a") as f:
        f.write(str(log) + "\n")
    return log
