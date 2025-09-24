import unittest
import skippy_verify

class TestSkippyVerify(unittest.TestCase):
    def test_compile_check(self):
        try:
            skippy_verify.compile_check()
        except Exception:
            self.fail("Function compile_check raised an unexpected exception")

    def test_import_check(self):
        try:
            skippy_verify.import_check()
        except Exception:
            self.fail("Function import_check raised an unexpected exception")

    def test_main(self):
        try:
            skippy_verify.main()
        except Exception:
            self.fail("Function main raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()