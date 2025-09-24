import unittest
import pulse_performance_test

class TestPulsePerformanceTest(unittest.TestCase):
    def test_run_test(self):
        try:
            pulse_performance_test.run_test()
        except Exception:
            self.fail("Function run_test raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()