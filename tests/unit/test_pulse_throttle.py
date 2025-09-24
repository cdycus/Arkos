import unittest
import pulse_throttle

class TestPulseThrottle(unittest.TestCase):
    def test_get_wait_time(self):
        try:
            pulse_throttle.get_wait_time()
        except Exception:
            self.fail("Function get_wait_time raised an unexpected exception")

    def test_PulseThrottle_instantiation(self):
        try:
            instance = pulse_throttle.PulseThrottle()
        except Exception:
            self.fail("Class PulseThrottle failed to instantiate")


if __name__ == "__main__":
    unittest.main()