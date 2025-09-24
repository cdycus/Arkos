import unittest
import pulse_feedback_tracer

class TestPulseFeedbackTracer(unittest.TestCase):
    def test_trace_feedback(self):
        try:
            pulse_feedback_tracer.trace_feedback()
        except Exception:
            self.fail("Function trace_feedback raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()