from prometheus_client import Gauge, start_http_server
from datetime import datetime

pulse_emit_count = Gauge("pulse_emits_total", "Total pulses emitted", ["type"])
pulse_last_emit = Gauge("pulse_last_emit_timestamp", "Timestamp of last core_brain", ["type"])
pulse_latency = Gauge("pulse_emit_latency_seconds", "Latency of core_brain emit function", ["type"])

def observe_pulse(pulse_type: str, duration: float):
    pulse_emit_count.labels(type=pulse_type).inc()
    pulse_last_emit.labels(type=pulse_type).set_to_current_time()
    pulse_latency.labels(type=pulse_type).set(duration)

def start_prometheus_server(port: int = 8000):
    start_http_server(port)
