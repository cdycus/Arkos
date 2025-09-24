import unittest
import coherence

class TestCoherence(unittest.TestCase):
    def test_check(self):
        try:
            coherence.check()
        except Exception:
            self.fail("Function check raised an unexpected exception")

    def test_CoherenceChecker_instantiation(self):
        try:
            instance = coherence.CoherenceChecker()
        except Exception:
            self.fail("Class CoherenceChecker failed to instantiate")


if __name__ == "__main__":
    unittest.main()