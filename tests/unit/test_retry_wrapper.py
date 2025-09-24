import unittest
import retry_wrapper

class TestRetryWrapper(unittest.TestCase):
    def test_call_with_backoff(self):
        try:
            retry_wrapper.call_with_backoff()
        except Exception:
            self.fail("Function call_with_backoff raised an unexpected exception")

    def test_call(self):
        try:
            retry_wrapper.call()
        except Exception:
            self.fail("Function call raised an unexpected exception")

    def test_CircuitBreaker_instantiation(self):
        try:
            instance = retry_wrapper.CircuitBreaker()
        except Exception:
            self.fail("Class CircuitBreaker failed to instantiate")


if __name__ == "__main__":
    unittest.main()