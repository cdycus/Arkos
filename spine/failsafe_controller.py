import time
import logging

MAX_LATENCY_MS = 300

def is_module_responsive(module_fn, timeout_ms=MAX_LATENCY_MS):
    start = time.time()
    try:
        module_fn()
    except Exception as e:
        logging.warning(f"Module {module_fn.__name__} failed: {str(e)}")
        return False
    elapsed = (time.time() - start) * 1000
    return elapsed < timeout_ms

def safe_pulse_tick(enforce_limits, memory_fn, belief_fn, foresight_fn=None, feedback_fn=None):
    if not enforce_limits():
        return False

    memory_fn()
    belief_fn()

    # Conditionally run foresight and feedback
    if foresight_fn and is_module_responsive(foresight_fn):
        foresight_fn()
    else:
        logging.warning("⚠️ Skipping foresight: degraded mode")

    if feedback_fn and is_module_responsive(feedback_fn):
        feedback_fn()
    else:
        logging.warning("⚠️ Skipping feedback: degraded mode")

    return True