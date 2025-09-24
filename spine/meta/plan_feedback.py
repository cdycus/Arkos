
import random
from memory.experience_log import log_experience
from mind.intent.planner import generate_action_plan
from heart.state_of_being import get_current_emotion

def simulate_plan_feedback(plan):
    emotion = get_current_emotion()
    for step in plan['steps']:
        result = random.choice(["positive", "negative"])
        log_experience(intent=step, emotion=emotion, result=result)
        print(f"[FEEDBACK] {step} → {result}")

if __name__ == "__main__":
    plan = generate_action_plan()
    print("Simulating feedback for plan:", plan)
    simulate_plan_feedback(plan)
