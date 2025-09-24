import unittest
import pulse_peer_registry

class TestPulsePeerRegistry(unittest.TestCase):
    def test_register_pulse_emitter(self):
        try:
            pulse_peer_registry.register_pulse_emitter()
        except Exception:
            self.fail("Function register_pulse_emitter raised an unexpected exception")

    def test_log_emitter_pulse(self):
        try:
            pulse_peer_registry.log_emitter_pulse()
        except Exception:
            self.fail("Function log_emitter_pulse raised an unexpected exception")

    def test_update(self):
        try:
            pulse_peer_registry.update()
        except Exception:
            self.fail("Function update raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()