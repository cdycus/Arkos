import asyncio
import logging
import time
from prometheus_client import Gauge, Counter

# Prometheus metrics
tick_duration_gauge = Gauge("microtick_duration_seconds", "Duration of each microtick", ["tick"])
tick_failure_counter = Counter("microtick_failures_total", "Number of microtick failures", ["tick"])

async def run_guarded_tick(name, coro):
    start = time.time()
    try:
        result = await asyncio.wait_for(coro(), timeout=0.3)
        tick_duration_gauge.labels(tick=name).set(time.time() - start)
        return result
    except Exception as e:
        tick_failure_counter.labels(tick=name).inc()
        logging.exception(f"[{name}] microtick failed: {e}")
        return None