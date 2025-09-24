import unittest
import pulse_bundle

class TestPulseBundle(unittest.TestCase):
    def test_add(self):
        try:
            pulse_bundle.add()
        except Exception:
            self.fail("Function add raised an unexpected exception")

    def test_flush(self):
        try:
            pulse_bundle.flush()
        except Exception:
            self.fail("Function flush raised an unexpected exception")

    def test_PulseBundler_instantiation(self):
        try:
            instance = pulse_bundle.PulseBundler()
        except Exception:
            self.fail("Class PulseBundler failed to instantiate")


if __name__ == "__main__":
    unittest.main()