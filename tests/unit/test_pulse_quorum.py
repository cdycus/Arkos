import unittest
import pulse_quorum

class TestPulseQuorum(unittest.TestCase):
    def test_is_quorum_met(self):
        try:
            pulse_quorum.is_quorum_met()
        except Exception:
            self.fail("Function is_quorum_met raised an unexpected exception")

    def test_PulseQuorum_instantiation(self):
        try:
            instance = pulse_quorum.PulseQuorum()
        except Exception:
            self.fail("Class PulseQuorum failed to instantiate")


if __name__ == "__main__":
    unittest.main()