from fastapi import FastAPI, Request
import uvicorn
from concurrent.futures import ThreadPoolExecutor
#from spine.registry import PulseRegistry
#from spine.ledger.ledger import PulseLedger
#from spine.runtime.metrics import observe_pulse, start_prometheus_server

if __name__ == '__main__':
    import registry as registry
if __name__ == '__main__':
    import runtime.metrics as start_prometheus_server
#if __name__ == '__main__':
   # import runtime.start_prometheus_server

if __name__ == '__main__':
    import ledger as PulseLedger

class PulseCoordinator:
    def __init__(self, config_path: str):
        self.registry = registry(config_path)
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
