import unittest
import memory_weighting

class TestMemoryWeighting(unittest.TestCase):
    def test_apply_weights(self):
        try:
            memory_weighting.apply_weights()
        except Exception:
            self.fail("Function apply_weights raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()