import unittest
import drift_monitor

class TestDriftMonitor(unittest.TestCase):
    def test_get_recent_alignment(self):
        try:
            drift_monitor.get_recent_alignment()
        except Exception:
            self.fail("Function get_recent_alignment raised an unexpected exception")

    def test_detect_drift(self):
        try:
            drift_monitor.detect_drift()
        except Exception:
            self.fail("Function detect_drift raised an unexpected exception")

    def test_DriftMonitor_instantiation(self):
        try:
            instance = drift_monitor.DriftMonitor()
        except Exception:
            self.fail("Class DriftMonitor failed to instantiate")


if __name__ == "__main__":
    unittest.main()