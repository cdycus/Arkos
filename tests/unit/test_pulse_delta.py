import unittest
import pulse_delta

class TestPulseDelta(unittest.TestCase):
    def test_update(self):
        try:
            pulse_delta.update()
        except Exception:
            self.fail("Function update raised an unexpected exception")

    def test_should_emit_alert(self):
        try:
            pulse_delta.should_emit_alert()
        except Exception:
            self.fail("Function should_emit_alert raised an unexpected exception")

    def test_PulseDelta_instantiation(self):
        try:
            instance = pulse_delta.PulseDelta()
        except Exception:
            self.fail("Class PulseDelta failed to instantiate")


if __name__ == "__main__":
    unittest.main()