import unittest
import foresight_runner

class TestForesightRunner(unittest.TestCase):
    def test_run_foresight_class(self):
        try:
            foresight_runner.run_foresight_class()
        except Exception:
            self.fail("Function run_foresight_class raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()