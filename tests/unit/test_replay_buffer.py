import unittest
import replay_buffer

class TestReplayBuffer(unittest.TestCase):
    def test_append(self):
        try:
            replay_buffer.append()
        except Exception:
            self.fail("Function append raised an unexpected exception")

    def test_replay(self):
        try:
            replay_buffer.replay()
        except Exception:
            self.fail("Function replay raised an unexpected exception")

    def test_PulseReplayBuffer_instantiation(self):
        try:
            instance = replay_buffer.PulseReplayBuffer()
        except Exception:
            self.fail("Class PulseReplayBuffer failed to instantiate")


if __name__ == "__main__":
    unittest.main()