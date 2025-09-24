import unittest
import pulse_fusion

class TestPulseFusion(unittest.TestCase):
    def test_fuse_domain_outputs(self):
        try:
            pulse_fusion.fuse_domain_outputs()
        except Exception:
            self.fail("Function fuse_domain_outputs raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()