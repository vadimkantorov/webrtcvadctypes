import unittest
import wave
import webrtcvadctypes
#import os; webrtcvadctypes.Vad.lib_path = os.path.abspath('webrtcvadctypesrnn.so') # does not pass tests yet

class WebRtcVadTests(unittest.TestCase):
    @staticmethod
    def _load_wave(file_name):
        fp = wave.open(file_name, 'rb')
        try:
            assert fp.getnchannels() == 1, (
                '{0}: sound format is incorrect! Sound must be mono.'.format(
                    file_name))
            assert fp.getsampwidth() == 2, (
                '{0}: sound format is incorrect! '
                'Sample width of sound must be 2 bytes.').format(file_name)
            assert fp.getframerate() in (8000, 16000, 32000), (
                '{0}: sound format is incorrect! '
                'Sampling frequency must be 8000 Hz, 16000 Hz or 32000 Hz.')
            sampling_frequency = fp.getframerate()
            sound_data = fp.readframes(fp.getnframes())
        finally:
            fp.close()
            del fp
        return sound_data, sampling_frequency

    def test_constructor(self):
        vad = webrtcvadctypes.Vad()

    def test_set_mode(self):
        vad = webrtcvadctypes.Vad()
        vad.set_mode(0)
        vad.set_mode(1)
        vad.set_mode(2)
        vad.set_mode(3)
        self.assertRaises(
            AssertionError,#ValueError,
            vad.set_mode, 4)

    def test_valid_rate_and_frame_length(self):
        self.assertTrue(webrtcvadctypes.valid_rate_and_frame_length(8000, 160))
        self.assertTrue(webrtcvadctypes.valid_rate_and_frame_length(16000, 160))
        self.assertFalse(webrtcvadctypes.valid_rate_and_frame_length(32000, 160))
        #self.assertRaises(
        #    (ValueError, OverflowError),
        #    webrtcvadctypes.valid_rate_and_frame_length, 2 ** 35, 10)

    def test_process_zeroes(self):
        frame_len = 160
        self.assertTrue(
            webrtcvadctypes.valid_rate_and_frame_length(8000, frame_len))
        sample = b'\x00' * frame_len * 2
        vad = webrtcvadctypes.Vad()
        self.assertFalse(vad.is_speech(sample, 16000))

    def test_process_file(self, frame_ms= 30):
        with open('test-audio.raw', 'rb') as f:
            data = f.read()
        n = int(8000 * 2 * frame_ms / 1000.0)
        frame_len = int(n / 2)
        self.assertTrue(
            webrtcvadctypes.valid_rate_and_frame_length(8000, frame_len))
        chunks = list(data[pos:pos + n] for pos in range(0, len(data), n))
        if len(chunks[-1]) != n:
            chunks = chunks[:-1]
        expecteds = [
            '011110111111111111111111111100',
            '011110111111111111111111111100',
            '000000111111111111111111110000',
            '000000111111111111111100000000'
        ]
        for mode in (0, 1, 2, 3):
            vad = webrtcvadctypes.Vad(mode)
            result = ''
            for chunk in chunks:
                voiced = vad.is_speech(chunk, 8000)
                result += '1' if voiced else '0'
            self.assertEqual(expecteds[mode], result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
