import unittest
import video_input_stub

class TestVideoInputStub(unittest.TestCase):
    def test_receive_video_input(self):
        try:
            video_input_stub.receive_video_input()
        except Exception:
            self.fail("Function receive_video_input raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()