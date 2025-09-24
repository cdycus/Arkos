import math

def score_belief(belief):
    age = 2025 - int(belief.get("timestamp", "2023").split("-")[0])  # crude year diff
    usage = belief.get("used", 0)
    emotion = belief.get("confidence", 0.5)
    score = emotion * (usage + 1) / (math.log(age + 2))
    return round(score, 3)
