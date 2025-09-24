import unittest
import reflection_score

class TestReflectionScore(unittest.TestCase):
    def test_score_reflection(self):
        try:
            reflection_score.score_reflection()
        except Exception:
            self.fail("Function score_reflection raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()