import unittest
import dispatcher

class TestDispatcher(unittest.TestCase):
    def test_dispatch(self):
        try:
            dispatcher.dispatch()
        except Exception:
            self.fail("Function dispatch raised an unexpected exception")

    def test_Dispatcher_instantiation(self):
        try:
            instance = dispatcher.Dispatcher()
        except Exception:
            self.fail("Class Dispatcher failed to instantiate")


if __name__ == "__main__":
    unittest.main()