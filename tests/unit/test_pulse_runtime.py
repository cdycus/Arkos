import unittest
import pulse_runtime

class TestPulseRuntime(unittest.TestCase):
    def test_emit_pulse(self):
        try:
            pulse_runtime.emit_pulse()
        except Exception:
            self.fail("Function emit_pulse raised an unexpected exception")

    def test_pulse_loop(self):
        try:
            pulse_runtime.pulse_loop()
        except Exception:
            self.fail("Function pulse_loop raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()