import unittest
import alignment

class TestAlignment(unittest.TestCase):
    def test_check_alignment(self):
        try:
            alignment.check_alignment()
        except Exception:
            self.fail("Function check_alignment raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()