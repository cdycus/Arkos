
import os
import random
import time

SERVICES = ['mind', 'brain', 'heart']
ACTIONS = ['restart', 'shutdown', 'slowdown']

def simulate_fault(service):
    action = random.choice(ACTIONS)
    print(f"[CHAOS] Simulating '{action}' on {service}")
    time.sleep(random.uniform(0.5, 1.5))
    return action

def recover(service):
    print(f"[RECOVERY] Ensuring {service} is operational...")
    time.sleep(random.uniform(0.5, 1.0))
    print(f"[RECOVERY] {service} restored.")

if __name__ == "__main__":
    for svc in SERVICES:
        result = simulate_fault(svc)
        recover(svc)
