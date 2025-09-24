
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

from spine.runtime.pulse_delta import PulseDelta
from spine.runtime.pulse_throttle import PulseThrottle
from spine.runtime.pulse_quorum import PulseQuorum
from spine.runtime.pulse_signature import PulseSigner
from spine.runtime.pulse_heatmap_exporter import PulseHeatmap
class PulseCoordinator:
    def __init__(self, config_path: str):
        self.registry = PulseRegistry(config_path)
        self.ledger = PulseLedger()
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.delta = PulseDelta()
        self.throttle = PulseThrottle()
        self.signer = PulseSigner()
        self.heatmap = PulseHeatmap()
        self.quorum = PulseQuorum(self.peer_registry.peers)
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
                pulse['signature'] = self.signer.sign(pulse)
                self.heatmap.log(pulse['type'])
                self.delta.update(pulse.get('confidence', 0.0), pulse.get('fatigue', 0.0))

    async def start_loop(self):
        await self.nats_client.connect()
        await self.mesh_router.start_nats_listener()
        while True:
            self.run_tick()
            await self.emit_heartbeat()
            await self.emit_service_specific_pulse()
            await asyncio.sleep(self.throttle.get_wait_time())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    coordinator = PulseCoordinator("spine/registry.json")
    print("🧠 Skippy PulseCoordinator starting tick loop...")
    try:
        loop.run_until_complete(coordinator.start_loop())
    except KeyboardInterrupt:
        print("👋 Coordinator shutdown requested.")



from spine.runtime.pulse_delta import PulseDelta
from spine.runtime.pulse_throttle import PulseThrottle
from spine.runtime.pulse_quorum import PulseQuorum
from spine.runtime.pulse_signature import PulseSigner
from spine.runtime.pulse_heatmap_exporter import PulseHeatmap

    def setup_runtime_modules(self):
        self.pulse_delta = PulseDelta()
        self.pulse_throttle = PulseThrottle()
        self.pulse_quorum = PulseQuorum(self.peer_registry.peers)
        self.pulse_signer = PulseSigner()
        self.pulse_heatmap = PulseHeatmap()

    async def start_loop(self):
        await self.nats_client.connect()
        await self.mesh_router.start_nats_listener()
        self.setup_runtime_modules()
        while True:
            self.run_tick()
            await self.emit_heartbeat()
            await self.emit_service_specific_pulse()
            if self.pulse_delta.should_emit_alert():
                print("🌀 Pulse Delta health check triggered.")
            self.pulse_heatmap.log("tick")
            wait = self.pulse_throttle.get_wait_time()
            await asyncio.sleep(wait)



from spine.runtime.pulse_dependency_graph import PulseDependencyGraph
from spine.runtime.pulse_priority_queue import PulsePriorityQueue
from spine.runtime.pulse_bundle import PulseBundler
from spine.runtime.pulse_fusion import PulseFusion
from spine.runtime.pulse_broadcast_validator import validate_pulse
from spine.runtime.pulse_hash_chain import PulseHashChain
from spine.runtime.pulse_anomaly_checker import PulseAnomalyChecker

    def activate_extended_pulse_modules(self):
        self.dependency_graph = PulseDependencyGraph()
        self.priority_queue = PulsePriorityQueue()
        self.pulse_bundler = PulseBundler()
        self.pulse_fusion = PulseFusion()
        self.hash_chain = PulseHashChain()
        self.anomaly_checker = PulseAnomalyChecker()

    async def start_loop(self):
        await self.nats_client.connect()
        await self.mesh_router.start_nats_listener()
        self.setup_runtime_modules()
        self.activate_extended_pulse_modules()
        while True:
            self.run_tick()
            await self.emit_heartbeat()
            await self.emit_service_specific_pulse()
            if self.pulse_delta.should_emit_alert():
                print("🌀 Pulse Delta health check triggered.")
            self.pulse_heatmap.log("tick")

            # Validate outgoing pulse
            heartbeat = self.build_heartbeat()
            validate_pulse(heartbeat)

            # Example fusion point (optional)
            fused = self.pulse_fusion.fuse([heartbeat])
            self.hash_chain.append(fused)

            wait = self.pulse_throttle.get_wait_time()
            await asyncio.sleep(wait)


from spine.runtime.pulse_dependency_graph import DependencyGraph
from spine.runtime.pulse_priority_queue import PulsePriorityQueue
from spine.runtime.pulse_bundle import PulseBundler
from spine.runtime.pulse_fusion import PulseFusionEngine
from spine.runtime.pulse_hash_chain import PulseHashChain
from spine.runtime.pulse_broadcast_validator import validate_pulse
from spine.runtime.pulse_anomaly_checker import PulseAnomalyDetector

    def setup_extended_modules(self):
        self.dependency_graph = DependencyGraph()
        self.priority_queue = PulsePriorityQueue()
        self.bundler = PulseBundler()
        self.fusion = PulseFusionEngine()
        self.hash_chain = PulseHashChain()
        self.anomaly_detector = PulseAnomalyDetector()

    async def start_loop(self):
        await self.nats_client.connect()
        await self.mesh_router.start_nats_listener()
        self.setup_runtime_modules()
        self.setup_extended_modules()
        while True:
            self.run_tick()
            await self.emit_heartbeat()
            await self.emit_service_specific_pulse()
            self.pulse_heatmap.log("tick")
            if self.pulse_delta.should_emit_alert():
                print("🌀 Delta health pulse triggered.")
            if not self.pulse_quorum.is_quorum_met():
                print("⚠️ Quorum not met, deferring consensus pulses.")
            wait = self.pulse_throttle.get_wait_time()
            await asyncio.sleep(wait)


from spine.runtime.feedback_engine import PulseFeedbackEngine

    def setup_extended_modules(self):
        self.dependency_graph = DependencyGraph()
        self.priority_queue = PulsePriorityQueue()
        self.bundler = PulseBundler()
        self.fusion = PulseFusionEngine()
        self.hash_chain = PulseHashChain()
        self.anomaly_detector = PulseAnomalyDetector()
        self.feedback_engine = PulseFeedbackEngine()

    def log_pulse_feedback(self, pulse, accepted=True):
        pulse_id = pulse.get("timestamp") + "::" + pulse.get("type", "unknown")
        self.feedback_engine.log_feedback(pulse_id, accepted)
        effectiveness = self.feedback_engine.effectiveness_score()
        if effectiveness < 0.7:
            print(f"⚠️ Low effectiveness detected: {effectiveness}")

    def run_tick(self):
        active_units = self.registry.get_active_units()
        for unit in active_units:
            if unit.should_emit({}):
                start = time.time()
                pulse = unit.emit()
                duration = time.time() - start
                observe_pulse(pulse['type'], duration)
                self.ledger.append(pulse)
                self.log_pulse_feedback(pulse)


from spine.runtime.belief_synthesizer import synthesize_from_foresight

    def handle_pulse(self, pulse):
        if pulse.get("type") == "pulse_foresight_trigger":
            f_class = pulse.get("class", "policy")
            context = pulse.get("context", "unspecified")
            beliefs = pulse.get("belief_ids", [])
            result = run_foresight_class(f_class, context, beliefs)
            self.ledger.append(result)
            belief = synthesize_from_foresight(result)
            print(f"📡 Foresight result: {result}")
            print(f"🧠 Belief updated: {belief}")


from spine.runtime.drift_monitor import DriftMonitor

    def check_drift_after_foresight(self, result):
        drift = DriftMonitor()
        if drift.detect_drift(result.get("confidence", 1.0)):
            print("⚠️ Alignment drift detected!")
            self.ledger.append({
                "type": "governance_review",
                "trigger": "drift_monitor",
                "reference": result.get("trace"),
                "reason": "alignment below threshold"
            })


from mind.expression_engine import ExpressionEngine

    def emit_expression_pulse(self):
        engine = ExpressionEngine()
        report = engine.generate_report()
        pulse = {
            "type": "pulse_expression",
            "text": report,
            "timestamp": __import__('datetime').datetime.utcnow().isoformat() + "Z"
        }
        self.ledger.append(pulse)
        print(f"🧠 Expression emitted: {pulse['text']}")


import time

    def start_loop_with_expression(self, interval=60):
        self.last_expression = time.time()
        while True:
            self.run_tick()
            if time.time() - self.last_expression >= interval:
                self.emit_expression_pulse()
                self.last_expression = time.time()
            time.sleep(1)


from spine.runtime.integration_hooks import run_post_tick_hooks
import json

    def run_tick(self):
        active_units = self.registry.get_active_units()
        for unit in active_units:
            if unit.should_emit({}):
                import time
                start = time.time()
                pulse = unit.emit()
                duration = time.time() - start
                self.ledger.append(pulse)

        try:
            with open("spine/runtime/runtime_flags.json") as f:
                flags = json.load(f)
            state = {
                "enable_hooks": flags.get("enable_hooks", True),
                "enable_expression": flags.get("enable_expression", False),
                "enable_memory_decay": flags.get("enable_memory_decay", False),
                "enable_governance": flags.get("enable_governance", False),
                "context": {},
                "beliefs": [],
                "foresight_result": {}
            }
            run_post_tick_hooks(state)
        except Exception as e:
            print("Hook error:", e)


from spine.runtime.integration_hooks import process_feedback_and_memory

    def run_feedback_cycle(self):
        pulse = {
            "pulse_id": "test_pulse_123",
            "type": "pulse_foresight_result",
            "decision": "regulate now",
            "confidence": 0.87,
            "beliefs": [
                {"statement": "regulation improves outcome", "confidence": 0.82, "used": 3, "timestamp": "2024-01-01"},
                {"statement": "risk is elevated", "confidence": 0.77, "used": 5, "timestamp": "2023-08-01"}
            ]
        }
        outcome = "success"
        logs = process_feedback_and_memory(pulse, outcome)
        print("Feedback + Memory Loop:")
        for log in logs:
            print(" -", log)


from spine.runtime.integration_hooks import emit_expression

    def run_expression_cycle(self):
        result = emit_expression()
        print("🗣️ Expression emitted:", result)
