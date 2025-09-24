import unittest
import expression_integrity_score

class TestExpressionIntegrityScore(unittest.TestCase):
    def test_compute_integrity(self):
        try:
            expression_integrity_score.compute_integrity()
        except Exception:
            self.fail("Function compute_integrity raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()