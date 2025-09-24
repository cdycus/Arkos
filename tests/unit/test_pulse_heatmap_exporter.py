import unittest
import pulse_heatmap_exporter

class TestPulseHeatmapExporter(unittest.TestCase):
    def test_log(self):
        try:
            pulse_heatmap_exporter.log()
        except Exception:
            self.fail("Function log raised an unexpected exception")

    def test_get_summary(self):
        try:
            pulse_heatmap_exporter.get_summary()
        except Exception:
            self.fail("Function get_summary raised an unexpected exception")

    def test_PulseHeatmap_instantiation(self):
        try:
            instance = pulse_heatmap_exporter.PulseHeatmap()
        except Exception:
            self.fail("Class PulseHeatmap failed to instantiate")


if __name__ == "__main__":
    unittest.main()