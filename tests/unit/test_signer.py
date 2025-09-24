import unittest
import signer

class TestSigner(unittest.TestCase):
    def test_sign(self):
        try:
            signer.sign()
        except Exception:
            self.fail("Function sign raised an unexpected exception")

    def test_verify(self):
        try:
            signer.verify()
        except Exception:
            self.fail("Function verify raised an unexpected exception")

    def test_SovereignPulseSigner_instantiation(self):
        try:
            instance = signer.SovereignPulseSigner()
        except Exception:
            self.fail("Class SovereignPulseSigner failed to instantiate")


if __name__ == "__main__":
    unittest.main()