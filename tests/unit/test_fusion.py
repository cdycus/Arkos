import unittest
import fusion

class TestFusion(unittest.TestCase):
    def test_fuse(self):
        try:
            fusion.fuse()
        except Exception:
            self.fail("Function fuse raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()