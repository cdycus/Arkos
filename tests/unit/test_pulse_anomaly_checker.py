import unittest
import pulse_anomaly_checker

class TestPulseAnomalyChecker(unittest.TestCase):
    def test_detect(self):
        try:
            pulse_anomaly_checker.detect()
        except Exception:
            self.fail("Function detect raised an unexpected exception")

    def test_PulseAnomalyDetector_instantiation(self):
        try:
            instance = pulse_anomaly_checker.PulseAnomalyDetector()
        except Exception:
            self.fail("Class PulseAnomalyDetector failed to instantiate")


if __name__ == "__main__":
    unittest.main()