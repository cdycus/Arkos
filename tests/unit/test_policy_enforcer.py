import unittest
import policy_enforcer

class TestPolicyEnforcer(unittest.TestCase):
    def test_enforce_policy(self):
        try:
            policy_enforcer.enforce_policy()
        except Exception:
            self.fail("Function enforce_policy raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()