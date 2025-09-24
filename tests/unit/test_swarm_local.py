import unittest
import swarm_local

class TestSwarmLocal(unittest.TestCase):
    def test_simulate(self):
        try:
            swarm_local.simulate()
        except Exception:
            self.fail("Function simulate raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()