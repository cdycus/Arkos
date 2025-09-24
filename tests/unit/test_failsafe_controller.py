import unittest
import failsafe_controller

class TestFailsafeController(unittest.TestCase):
    def test_is_module_responsive(self):
        try:
            failsafe_controller.is_module_responsive()
        except Exception:
            self.fail("Function is_module_responsive raised an unexpected exception")

    def test_safe_pulse_tick(self):
        try:
            failsafe_controller.safe_pulse_tick()
        except Exception:
            self.fail("Function safe_pulse_tick raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()