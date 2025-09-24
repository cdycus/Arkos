import unittest
import interference

class TestInterference(unittest.TestCase):
    def test_detect_conflict(self):
        try:
            interference.detect_conflict()
        except Exception:
            self.fail("Function detect_conflict raised an unexpected exception")

    def test_InterferenceDetector_instantiation(self):
        try:
            instance = interference.InterferenceDetector()
        except Exception:
            self.fail("Class InterferenceDetector failed to instantiate")


if __name__ == "__main__":
    unittest.main()