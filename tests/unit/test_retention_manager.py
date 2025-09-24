import unittest
import retention_manager

class TestRetentionManager(unittest.TestCase):
    def test_score_belief(self):
        try:
            retention_manager.score_belief()
        except Exception:
            self.fail("Function score_belief raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()