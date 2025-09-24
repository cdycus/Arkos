import unittest
import belief_updater

class TestBeliefUpdater(unittest.TestCase):
    def test_update_beliefs_from_expression(self):
        try:
            belief_updater.update_beliefs_from_expression()
        except Exception:
            self.fail("Function update_beliefs_from_expression raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()