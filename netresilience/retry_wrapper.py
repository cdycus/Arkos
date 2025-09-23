import time
import requests
import logging

MAX_ATTEMPTS = 5
BACKOFF_FACTOR = 0.5

def call_with_backoff(url, timeout=1.0):
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            sleep_time = BACKOFF_FACTOR * (2 ** attempt)
            logging.warning(f"Attempt {attempt+1} failed for {url}: {e}. Retrying in {sleep_time:.2f}s...")
            time.sleep(sleep_time)
            attempt += 1
    raise ConnectionError(f"Max attempts exceeded for {url}")

class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_time=30):
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time
        self.failure_count = 0
        self.last_failure_time = None

    def call(self, func, *args, **kwargs):
        if self.failure_count >= self.failure_threshold:
            if time.time() - self.last_failure_time < self.recovery_time:
                raise RuntimeError("Circuit open. Skipping call.")
            else:
                self.failure_count = 0  # reset after cooldown

        try:
            result = func(*args, **kwargs)
            self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            raise e