import unittest
import drift_viewer

class TestDriftViewer(unittest.TestCase):
    def test_view_alignment_trend(self):
        try:
            drift_viewer.view_alignment_trend()
        except Exception:
            self.fail("Function view_alignment_trend raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()