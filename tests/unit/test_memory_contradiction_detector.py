import unittest
import memory_contradiction_detector

class TestMemoryContradictionDetector(unittest.TestCase):
    def test_detect_contradictions(self):
        try:
            memory_contradiction_detector.detect_contradictions()
        except Exception:
            self.fail("Function detect_contradictions raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()