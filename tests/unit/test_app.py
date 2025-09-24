import unittest
import app

class TestApp(unittest.TestCase):
    def test_health_check(self):
        try:
            app.health_check()
        except Exception:
            self.fail("Function health_check raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()