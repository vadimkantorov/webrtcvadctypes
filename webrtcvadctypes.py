import os
import ctypes

# TODO: replicate https://github.com/wiseman/py-webrtcvad/blob/master/cbits/pywebrtcvad.c
# https://webrtc.googlesource.com/src/+/refs/heads/main/modules/audio_processing/vad/standalone_vad.cc
# https://github.com/wiseman/py-webrtcvad/blob/master/example.py
# https://github.com/vadimkantorov/readaudio/blob/master/decode_audio.py

# src/common_audio/vad/webrtc_vad.c
# src/common_audio/vad/vad.cc

class Vad(ctypes.c_void_p):
    _webrtcvad = None
    
    @staticmethod
    def ffi(lib_path = os.path.abspath('webrtcvadgmm.so')):
        lib = ctypes.CDLL(lib_path)
        
        # src/common_audio/vad/include/webrtc_vad.h

        ## Creates an instance to the VAD structure.
        #VadInst* WebRtcVad_Create(void);
        lib.WebRtcVad_Create.argtypes = []
        lib.WebRtcVad_Create.restype = ctypes.c_void_p
        
        
        ## Frees the dynamic memory of a specified VAD instance.
        ##
        ## - handle [i] : Pointer to VAD instance that should be freed.
        #void WebRtcVad_Free(VadInst* handle);
        lib.WebRtcVad_Free.argtypes = [ctypes.c_void_p]
        lib.WebRtcVad_Free.restype = None
        
        ## Initializes a VAD instance.
        ##
        ## - handle [i/o] : Instance that should be initialized.
        ##
        ## returns        : 0 - (OK),
        ##                 -1 - (null pointer or Default mode could not be set).
        #int WebRtcVad_Init(VadInst* handle);
        lib.WebRtcVad_Init.argtypes = [ctypes.c_void_p]
        lib.WebRtcVad_Init.restype = ctypes.c_int
        
        
        ## Sets the VAD operating mode. A more aggressive (higher mode) VAD is more
        ## restrictive in reporting speech. Put in other words the probability of being
        ## speech when the VAD returns 1 is increased with increasing mode. As a
        ## consequence also the missed detection rate goes up.
        ##
        ## - handle [i/o] : VAD instance.
        ## - mode   [i]   : Aggressiveness mode (0, 1, 2, or 3).
        ##
        ## returns        : 0 - (OK),
        ##                 -1 - (null pointer, mode could not be set or the VAD instance
        ##                       has not been initialized).
        #int WebRtcVad_set_mode(VadInst* handle, int mode);
        lib.WebRtcVad_set_mode.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.WebRtcVad_set_mode.restype = ctypes.c_int
        
        ## Calculates a VAD decision for the `audio_frame`. For valid sampling rates
        ## frame lengths, see the description of WebRtcVad_ValidRatesAndFrameLengths().
        ##
        ## - handle       [i/o] : VAD Instance. Needs to be initialized by
        ##                        WebRtcVad_Init() before call.
        ## - fs           [i]   : Sampling frequency (Hz): 8000, 16000, or 32000
        ## - audio_frame  [i]   : Audio frame buffer.
        ## - frame_length [i]   : Length of audio frame buffer in number of samples.
        ##
        ## returns              : 1 - (Active Voice),
        ##                        0 - (Non-active Voice),
        ##                       -1 - (Error)
        #int WebRtcVad_Process(VadInst* handle,
        #                      int fs,
        #                      const int16_t* audio_frame,
        #                      size_t frame_length);
        lib.WebRtcVad_Process.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int16) , ctypes.c_size_t]
        lib.WebRtcVad_Process.restype = ctypes.c_int
        
        ## Checks for valid combinations of `rate` and `frame_length`. We support 10,
        ## 20 and 30 ms frames and the rates 8000, 16000 and 32000 Hz.
        ##
        ## - rate         [i] : Sampling frequency (Hz).
        ## - frame_length [i] : Speech frame buffer length in number of samples.
        ##
        ## returns            : 0 - (valid combination), -1 - (invalid combination)
        #int WebRtcVad_ValidRateAndFrameLength(int rate, size_t frame_length);
        lib.WebRtcVad_ValidRateAndFrameLength.argtypes = [ctypes.c_int, ctypes.c_size_t]
        lib.WebRtcVad_ValidRateAndFrameLength.restype = ctypes.c_int
        return lib

    @staticmethod
    def valid_rate_and_frame_length(rate, frame_length):
        return Vad._webrtcvad.WebRtcVad_ValidRateAndFrameLength(rate, frame_length)

    def __init__(self, mode=None):
        # https://stackoverflow.com/questions/17840144/why-does-setting-ctypes-dll-function-restype-c-void-p-return-long 
        if self._webrtcvad is None:
            self._webrtcvad = self.ffi()

        self.value = self._webrtcvad.WebRtcVad_Create()
        assert 0 == Vad._webrtcvad.WebRtcVad_Init(self)
        if mode is not None:
            self.set_mode(mode)

    def __del__(self):
        Vad._webrtcvad.WebRtcVad_Free(self)
        self.value = None
    
    def set_mode(self, mode):
        assert mode in [None, 0, 1, 2, 3]
        if mode is not None:
            assert 0 == Vad._webrtcvad.WebRtcVad_set_mode(self, mode)

    def is_speech(self, buf, sample_rate, length=None):
        assert sample_rate in [8000, 16000, 32000, 48000]
        length = length or int(len(buf) / 2)
        if length * 2 > len(buf):
            raise IndexError('buffer has {} frames, but length argument was {}'.format(int(len(buf) / 2.0), length))
        return Vad._webrtcvad.WebRtcVad_Process(self, sample_rate, buf, length)

class VadRnn(ctypes.c_void_p):
    _webrtcvad = None
    
    @staticmethod
    def ffi(lib_path = os.path.abspath('webrtcvadrnn.so')):
        lib = ctypes.CDLL(lib_path)
        lib.WebRtcVadRnn_Create.argtypes = []
        lib.WebRtcVadRnn_Create.restype = ctypes.c_void_p
        lib.WebRtcVadRnn_Free.argtypes = [ctypes.c_void_p]
        lib.WebRtcVadRnn_Free.restype = None
        lib.WebRtcVadRnn_Init.argtypes = [ctypes.c_void_p]
        lib.WebRtcVadRnn_Init.restype = ctypes.c_int
        lib.WebRtcVadRnn_set_mode.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.WebRtcVadRnn_set_mode.restype = ctypes.c_int
        lib.WebRtcVadRnn_Process.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int16) , ctypes.c_size_t]
        lib.WebRtcVadRnn_Process.restype = ctypes.c_float #ctypes.c_int
        lib.WebRtcVadRnn_ValidRateAndFrameLength.argtypes = [ctypes.c_int, ctypes.c_size_t]
        lib.WebRtcVadRnn_ValidRateAndFrameLength.restype = ctypes.c_int
        return lib

    @staticmethod
    def valid_rate_and_frame_length(rate, frame_length):
        return VadRnn._webrtcvad.WebRtcVadRnn_ValidRateAndFrameLength(rate, frame_length)

    def __init__(self, mode=None):
        # https://stackoverflow.com/questions/17840144/why-does-setting-ctypes-dll-function-restype-c-void-p-return-long 
        if self._webrtcvad is None:
            self._webrtcvad = self.ffi()

        self.value = self._webrtcvad.WebRtcVadRnn_Create()
        assert 0 == VadRnn._webrtcvad.WebRtcVadRnn_Init(self)
        if mode is not None:
            self.set_mode(mode)

    def __del__(self):
        VadRnn._webrtcvad.WebRtcVadRnn_Free(self)
        self.value = None
    
    def set_mode(self, mode):
        assert mode in [None, 0, 1, 2]
        if mode is not None:
            assert 0 == VadRnn._webrtcvad.WebRtcVadRnn_set_mode(self, mode)

    def is_speech(self, buf, sample_rate, length=None):
        assert sample_rate in [8000, 16000, 32000, 48000]
        length = length or int(len(buf) / 2)
        if length * 2 > len(buf):
            raise IndexError('buffer has {} frames, but length argument was {}'.format(int(len(buf) / 2.0), length))
        return VadRnn._webrtcvad.WebRtcVadRnn_Process(self, sample_rate, buf, length)


if __name__ == '__main__':
    vad = Vad()
    print(vad)
