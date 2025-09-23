
import os
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from spine.registry import PulseRegistry
from spine.ledger.ledger import PulseLedger
from spine.runtime.metrics import observe_pulse, start_prometheus_server
from spine.runtime.mesh_router import PulseMeshRouter
from spine.runtime.pulse_broadcast import PulseBroadcaster
from spine.runtime.nats_client import NATSClient
from spine.pulse_peer_registry import PulsePeerRegistry
from spine.pulse_queue import PulseQueue

class PulseCoordinator:
    def __init__(self, config_path: str):
        self.registry = PulseRegistry(config_path)
        self.ledger = PulseLedger()
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.peer_registry = PulsePeerRegistry("peer_registry.json")
        self.pulse_queue = PulseQueue()
        self.nats_client = NATSClient("spine/nats_config.json")
        self.pulse_broadcaster = PulseBroadcaster(self.nats_client)
        self.mesh_router = PulseMeshRouter(self.pulse_queue, self.peer_registry, self.pulse_broadcaster)
        start_prometheus_server()

    def get_service_name(self):
        return os.getenv("SKIPPY_SERVICE", "unknown")

    def build_heartbeat(self):
        return {
            "type": "pulse_heartbeat",
            "sovereign_id": "skippy-alpha-v1",
            "service": self.get_service_name(),
            "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z",
            "confidence": 0.87,
            "fatigue": 0.15
        }

    async def emit_heartbeat(self):
        pulse = self.build_heartbeat()
        await self.pulse_broadcaster.broadcast_heartbeat(pulse)

    async def emit_service_specific_pulse(self):
        service = self.get_service_name()
        pulse = {
            "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z",
            "sovereign_id": "skippy-alpha-v1",
            "service": service
        }

        if service == "Brain":
            pulse.update({
                "type": "pulse_foresight",
                "strategy": "regulate now",
                "confidence": 0.91
            })
            await self.nats_client.publish("pulse.foresight", pulse)

        elif service == "Heart":
            pulse.update({
                "type": "pulse_feedback",
                "emotion": "calm",
                "entropy": 0.12
            })
            await self.nats_client.publish("pulse.feedback", pulse)

        elif service == "Mind":
            pulse.update({
                "type": "pulse_expression",
                "self_report": "I am currently aligned and stable.",
                "alignment_score": 0.93
            })
            await self.nats_client.publish("pulse.expression", pulse)

    def run_tick(self):
        active_units = self.registry.get_active_units()
        for unit in active_units:
            if unit.should_emit({}):
                start = time.time()
                pulse = unit.emit()
                duration = time.time() - start
                observe_pulse(pulse['type'], duration)
                self.ledger.append(pulse)

    async def start_loop(self):
        await self.nats_client.connect()
        await self.mesh_router.start_nats_listener()
        while True:
            self.run_tick()
            await self.emit_heartbeat()
            await self.emit_service_specific_pulse()
            await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    coordinator = PulseCoordinator("spine/registry.json")
    print("🧠 Skippy PulseCoordinator starting tick loop...")
    try:
        loop.run_until_complete(coordinator.start_loop())
    except KeyboardInterrupt:
        print("👋 Coordinator shutdown requested.")
