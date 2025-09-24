import unittest
from runtime_status import check_status

class TestRuntimeStatus(unittest.TestCase):
    def test_check_status_output(self):
        result = check_status()
        self.assertIn("status", result)