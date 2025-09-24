import unittest
import audio_input_stub

class TestAudioInputStub(unittest.TestCase):
    def test_receive_audio_input(self):
        try:
            audio_input_stub.receive_audio_input()
        except Exception:
            self.fail("Function receive_audio_input raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()