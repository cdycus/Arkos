from concurrent.futures import ThreadPoolExecutor
from spine.registry import PulseRegistry
from spine.ledger.ledger import PulseLedger
from spine.runtime.metrics import observe_pulse, start_prometheus_server

class PulseCoordinator:
    def __init__(self, config_path: str):
        self.registry = PulseRegistry(config_path)
        self.ledger = PulseLedger()
        self.executor = ThreadPoolExecutor(max_workers=5)
        start_prometheus_server()

    def run_tick(self):
        active_units = self.registry.get_active_units()
        for unit in active_units:
            if unit.should_emit({}):
                import time
                start = time.time()
                pulse = unit.emit()
                duration = time.time() - start
                observe_pulse(pulse['type'], duration)
                self.ledger.append(pulse)

    def start_loop(self):
        import time
        while True:
            self.run_tick()
            time.sleep(1)
