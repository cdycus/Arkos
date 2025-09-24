
import time
from mind.expression.plan_executor import execute_plan
from spine.meta.plan_feedback import simulate_plan_feedback
from spine.meta.plan_logger import log_plan
from spine.meta.skippy_self_check import update_skippy_state

INTERVAL_SECONDS = 15  # Autonomous loop frequency

def autonomous_cycle():
    print("\n🌀 Autonomous Cycle Starting")
    plan_executed = {"steps": [s['expression'] for s in execute_plan()]}
    log_plan(plan_executed)
    simulate_plan_feedback(plan_executed)
    state = update_skippy_state()
    print("🧠 Skippy state updated:", state)

if __name__ == "__main__":
    while True:
        autonomous_cycle()
        time.sleep(INTERVAL_SECONDS)
