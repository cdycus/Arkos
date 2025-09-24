import unittest
import reflection_trace_analyzer

class TestReflectionTraceAnalyzer(unittest.TestCase):
    def test_analyze_trace(self):
        try:
            reflection_trace_analyzer.analyze_trace()
        except Exception:
            self.fail("Function analyze_trace raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()