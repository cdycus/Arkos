import unittest
import trigger_handler

class TestTriggerHandler(unittest.TestCase):
    def test_handle_foresight_trigger(self):
        try:
            trigger_handler.handle_foresight_trigger()
        except Exception:
            self.fail("Function handle_foresight_trigger raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()