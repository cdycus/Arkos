import unittest
import resonance

class TestResonance(unittest.TestCase):
    def test_match(self):
        try:
            resonance.match()
        except Exception:
            self.fail("Function match raised an unexpected exception")

    def test_ResonanceEvaluator_instantiation(self):
        try:
            instance = resonance.ResonanceEvaluator()
        except Exception:
            self.fail("Class ResonanceEvaluator failed to instantiate")


if __name__ == "__main__":
    unittest.main()