import unittest
import pulse_simulation_cli

class TestPulseSimulationCli(unittest.TestCase):
    def test_replay_log(self):
        try:
            pulse_simulation_cli.replay_log()
        except Exception:
            self.fail("Function replay_log raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()