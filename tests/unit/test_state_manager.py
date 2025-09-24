import unittest
import state_manager

class TestStateManager(unittest.TestCase):
    def test_update_attention(self):
        try:
            state_manager.update_attention()
        except Exception:
            self.fail("Function update_attention raised an unexpected exception")

    def test_decay_attention(self):
        try:
            state_manager.decay_attention()
        except Exception:
            self.fail("Function decay_attention raised an unexpected exception")

    def test_StateManager_instantiation(self):
        try:
            instance = state_manager.StateManager()
        except Exception:
            self.fail("Class StateManager failed to instantiate")


if __name__ == "__main__":
    unittest.main()