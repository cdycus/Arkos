import unittest
import pulse_hash_chain

class TestPulseHashChain(unittest.TestCase):
    def test_hash_pulse(self):
        try:
            pulse_hash_chain.hash_pulse()
        except Exception:
            self.fail("Function hash_pulse raised an unexpected exception")

    def test_PulseHashChain_instantiation(self):
        try:
            instance = pulse_hash_chain.PulseHashChain()
        except Exception:
            self.fail("Class PulseHashChain failed to instantiate")


if __name__ == "__main__":
    unittest.main()