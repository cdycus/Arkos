import unittest
import foresight_replay

class TestForesightReplay(unittest.TestCase):
    def test_load_deltas(self):
        try:
            foresight_replay.load_deltas()
        except Exception:
            self.fail("Function load_deltas raised an unexpected exception")

    def test_score_delta(self):
        try:
            foresight_replay.score_delta()
        except Exception:
            self.fail("Function score_delta raised an unexpected exception")

    def test_emit_delta_feedback(self):
        try:
            foresight_replay.emit_delta_feedback()
        except Exception:
            self.fail("Function emit_delta_feedback raised an unexpected exception")

    def test_save_log(self):
        try:
            foresight_replay.save_log()
        except Exception:
            self.fail("Function save_log raised an unexpected exception")

    def test_ForesightReplay_instantiation(self):
        try:
            instance = foresight_replay.ForesightReplay()
        except Exception:
            self.fail("Class ForesightReplay failed to instantiate")


if __name__ == "__main__":
    unittest.main()