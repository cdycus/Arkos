import unittest
import pulse_signature

class TestPulseSignature(unittest.TestCase):
    def test_sign(self):
        try:
            pulse_signature.sign()
        except Exception:
            self.fail("Function sign raised an unexpected exception")

    def test_verify(self):
        try:
            pulse_signature.verify()
        except Exception:
            self.fail("Function verify raised an unexpected exception")

    def test_PulseSigner_instantiation(self):
        try:
            instance = pulse_signature.PulseSigner()
        except Exception:
            self.fail("Class PulseSigner failed to instantiate")


if __name__ == "__main__":
    unittest.main()