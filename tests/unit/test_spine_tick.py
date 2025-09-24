import unittest
import spine_tick

class TestSpineTick(unittest.TestCase):
    def test_run_pulse_tick(self):
        try:
            spine_tick.run_pulse_tick()
        except Exception:
            self.fail("Function run_pulse_tick raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()