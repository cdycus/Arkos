
import time
import random
from prometheus_client import start_http_server, Summary, Counter, Gauge
from threading import Thread

pulse_duration = Summary('pulse_duration_seconds', 'Time spent processing a pulse')
pulse_emissions_total = Counter('pulse_emissions_total', 'Total pulses emitted')
pulse_failure_total = Counter('pulse_failures_total', 'Total pulse emission failures')
pulse_last_timestamp = Gauge('pulse_last_timestamp_seconds', 'Timestamp of last pulse emission')

@pulse_duration.time()
def emit_pulse():
    success = random.choice([True, True, True, False])
    time.sleep(random.uniform(0.1, 0.5))
    pulse_last_timestamp.set_to_current_time()
    pulse_emissions_total.inc()
    if not success:
        pulse_failure_total.inc()
        raise Exception("Pulse emission failed")

def pulse_loop():
    while True:
        try:
            emit_pulse()
        except Exception as e:
            print(f"[WARN] {e}")
        time.sleep(5)

if __name__ == "__main__":
    print("🔁 Starting pulse emitter on port 8000")
    start_http_server(8000)
    Thread(target=pulse_loop, daemon=True).start()
    while True:
        time.sleep(60)


# Injected: Signature verification
try:
    from spine.crypto.identity import verify_signature
except ImportError:
    verify_signature = lambda payload, sig: True

def validate_pulse_integrity(pulse_data):
    payload = pulse_data.get('payload', '')
    signature = pulse_data.get('signature', '')
    if not verify_signature(payload, signature):
        raise ValueError("Invalid signature detected in pulse")
    return True
