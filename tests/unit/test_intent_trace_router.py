import unittest
import intent_trace_router

class TestIntentTraceRouter(unittest.TestCase):
    def test_route_by_intent(self):
        try:
            intent_trace_router.route_by_intent()
        except Exception:
            self.fail("Function route_by_intent raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()