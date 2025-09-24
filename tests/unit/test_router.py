import unittest
import router

class TestRouter(unittest.TestCase):
    def test_load_mesh(self):
        try:
            router.load_mesh()
        except Exception:
            self.fail("Function load_mesh raised an unexpected exception")

    def test_broadcast_pulse(self):
        try:
            router.broadcast_pulse()
        except Exception:
            self.fail("Function broadcast_pulse raised an unexpected exception")

    def test_inject_pulse(self):
        try:
            router.inject_pulse()
        except Exception:
            self.fail("Function inject_pulse raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()