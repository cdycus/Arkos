import unittest
import fusion_aware

class TestFusionAware(unittest.TestCase):
    def test_fuse_with_modifiers(self):
        try:
            fusion_aware.fuse_with_modifiers()
        except Exception:
            self.fail("Function fuse_with_modifiers raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()