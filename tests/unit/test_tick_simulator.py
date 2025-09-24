import unittest
import tick_simulator

class TestTickSimulator(unittest.TestCase):
    def test_simulate_tick(self):
        try:
            tick_simulator.simulate_tick()
        except Exception:
            self.fail("Function simulate_tick raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()