import unittest
import api

class TestApi(unittest.TestCase):
    def test_health_check(self):
        try:
            api.health_check()
        except Exception:
            self.fail("Function health_check raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()