import unittest
import perception_logger

class TestPerceptionLogger(unittest.TestCase):
    def test_log_perception(self):
        try:
            perception_logger.log_perception()
        except Exception:
            self.fail("Function log_perception raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()