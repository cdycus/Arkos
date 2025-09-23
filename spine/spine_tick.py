# Pulse Tick Logic
from Arkos.netresilience.retry_wrapper import CircuitBreaker

breaker_foresight = CircuitBreaker()
breaker_feedback = CircuitBreaker()

def run_pulse_tick():
    ...
    # memory_fn() and belief_fn() assumed to be safe and fast
    memory_fn()
    belief_fn()

    # foresight with breaker
    try:
        breaker_foresight.call(foresight_fn)
    except RuntimeError:
        logging.warning("⚠️ Circuit breaker open for foresight — skipping.")

    # feedback with breaker
    try:
        breaker_feedback.call(feedback_fn)
    except RuntimeError:
        logging.warning("⚠️ Circuit breaker open for feedback — skipping.")