import unittest
import metrics

class TestMetrics(unittest.TestCase):
    def test_observe_pulse(self):
        try:
            metrics.observe_pulse()
        except Exception:
            self.fail("Function observe_pulse raised an unexpected exception")

    def test_start_prometheus_server(self):
        try:
            metrics.start_prometheus_server()
        except Exception:
            self.fail("Function start_prometheus_server raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()