import unittest
import skippy_mind_entry

class TestSkippyMindEntry(unittest.TestCase):
    def test_receive_input(self):
        try:
            skippy_mind_entry.receive_input()
        except Exception:
            self.fail("Function receive_input raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()