# 🧠 Skippy DNS Spine — Engineering Support Documentation

This document provides detailed technical insights into the modules that drive Skippy’s core pulse architecture in the `spine/` folder.

## 📄 Module: `feedback_engine.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class PulseFeedbackEngine:`
- `def __init__(self):`
- `def record_feedback(self, pulse, result):`

---

## 📄 Module: `cadence.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class PulseCadence:`
- `def __init__(self):`
- `def get_next_interval(self):`

---

## 📄 Module: `coordinator.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class PulseCoordinator:`
- `def __init__(self, config_path: str):`
- `def run_tick(self):`
- `def start_loop(self):`

---

## 📄 Module: `skippy_verify.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

- `def compile_check(py_file):`
- `def import_check(module_path, class_name):`
- `def main():`

---

## 📄 Module: `signer.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class SovereignPulseSigner:`
- `def __init__(self, secret="SkippySecret"):`
- `def sign(self, pulse: dict) -> str:`
- `def verify(self, pulse: dict, signature: str) -> bool:`

---

## 📄 Module: `mesh_router.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class PulseMeshRouter:`
- `def __init__(self, peers):`
- `def broadcast(self, pulse):`

---

## 📄 Module: `pulse_runtime.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

- `def emit_pulse():`
- `def pulse_loop():`

---

## 📄 Module: `router.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

- `def load_mesh():`
- `def broadcast_pulse(pulse: dict):`
- `def inject_pulse(pulse: dict):`

---

## 📄 Module: `__init__.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*


---

## 📄 Module: `meta_health.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class MetaPulseHealth:`
- `def __init__(self, config):`
- `def report(self):`

---

## 📄 Module: `registry.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class PulseRegistry:`
- `def __init__(self, config_path):`
- `def register(self, name, unit):`
- `def get_units(self):`
- `def get_config(self):`
- `def get_active_units(self):`

---

## 📄 Module: `replay_buffer.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class PulseReplayBuffer:`
- `def __init__(self, path="pulse_buffer.jsonl", max_size=1000):`
- `def append(self, pulse: dict):`
- `def replay(self):`

---

## 📄 Module: `pulse_queue.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

### 🔹 Class: `class PulseQueue:`
- `def __init__(self, nats_url="nats://localhost:4222"):`

---

## 📄 Module: `reflex_trigger.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*


---

## 📄 Module: `pulse_peer_registry.py`
### Description:
- *Auto-inferred logic based on class/method names and structure.*

- `def register_pulse_emitter(pulse_type, node_id):`
- `def log_emitter_pulse(pulse_type, node_id):`
