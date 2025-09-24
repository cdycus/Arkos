import unittest
import state_of_being

class TestStateOfBeing(unittest.TestCase):
    def test_compute_state_of_being(self):
        try:
            state_of_being.compute_state_of_being()
        except Exception:
            self.fail("Function compute_state_of_being raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()