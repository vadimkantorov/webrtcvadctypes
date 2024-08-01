import os
import ctypes

# https://github.com/wiseman/py-webrtcvad/blob/master/example.py
# src/common_audio/vad/webrtc_vad.c
# src/common_audio/vad/vad.cc
# src/modules/audio_processing/vad/standalone_vad.cc

class Vad(ctypes.c_void_p):
    lib_path = os.path.abspath('webrtcvadctypesgmm.so')
    _webrtcvad = None
    
    @staticmethod
    def initialize(lib_path):
        Vad._webrtcvad = Vad.ffi(lib_path)

    @staticmethod
    def ffi(lib_path):
        # using Vad in place of ctypes.c_void_p in bindings for some reason leads to memory corruption during test
        # https://stackoverflow.com/questions/78808780/deriving-from-ctypes-c-void-p-to-represent-a-custom-handler
        lib = ctypes.CDLL(lib_path)
        
        # src/common_audio/vad/include/webrtc_vad.h

        ## Creates an instance to the VAD structure.
        #VadInst* WebRtcVad_Create(void);
        lib.WebRtcVad_Create.argtypes = []
        lib.WebRtcVad_Create.restype = Vad #ctypes.c_void_p
        
        
        ## Frees the dynamic memory of a specified VAD instance.
        ##
        ## - handle [i] : Pointer to VAD instance that should be freed.
        #void WebRtcVad_Free(VadInst* handle);
        lib.WebRtcVad_Free.argtypes = [Vad]
        lib.WebRtcVad_Free.restype = None
        
        ## Initializes a VAD instance.
        ##
        ## - handle [i/o] : Instance that should be initialized.
        ##
        ## returns        : 0 - (OK),
        ##                 -1 - (null pointer or Default mode could not be set).
        #int WebRtcVad_Init(VadInst* handle);
        lib.WebRtcVad_Init.argtypes = [Vad]#[ctypes.c_void_p]
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
        lib.WebRtcVad_set_mode.argtypes = [Vad, ctypes.c_int] #[ctypes.c_void_p, ctypes.c_int]
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
        lib.WebRtcVad_Process.argtypes = [Vad, ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t]
        #lib.WebRtcVad_Process.argtypes = [Vad, ctypes.c_int, ctypes.POINTER(ctypes.c_int16), ctypes.c_size_t]
        # marshalling of bytes object to ctypes.POINTER(ctypes.c_int16) does not work automatically (need an explicit ctypes.cast, see below), but to ctypes.c_void_p works:
        # https://stackoverflow.com/questions/72624136/python-bytes-to-ctypes-void-pointer
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
    def valid_rate_and_frame_length(rate, frame_length, lib_path = None):
        if Vad._webrtcvad is None:
            Vad.initialize(lib_path or Vad.lib_path)
        return 0 == Vad._webrtcvad.WebRtcVad_ValidRateAndFrameLength(rate, frame_length)
    
    def set_mode(self, mode):
        assert Vad._webrtcvad is not None
        assert mode in [None, 0, 1, 2, 3]
        if mode is not None:
            assert 0 == Vad._webrtcvad.WebRtcVad_set_mode(self, mode)

    def is_speech(self, buf, sample_rate, length=None):
        assert Vad._webrtcvad is not None
        assert sample_rate in [8000, 16000, 32000, 48000]
        length = length or (len(buf) // 2)
        assert length * 2 <= len(buf), f'buffer has {len(buf) // 2} frames, but length argument was {length}'
        #buf = ctypes.cast(buf, ctypes.POINTER(ctypes.c_int16))
        return 1 == Vad._webrtcvad.WebRtcVad_Process(self, sample_rate, buf, length)

    def __new__(cls, mode=None, lib_path = None):
        # https://stackoverflow.com/questions/17840144/why-does-setting-ctypes-dll-function-restype-c-void-p-return-long 
        if Vad._webrtcvad is None:
            Vad.initialize(lib_path or Vad.lib_path)
        assert Vad._webrtcvad is not None
        return Vad._webrtcvad.WebRtcVad_Create()

    def __init__(self, mode=None, lib_path = None):
        assert Vad._webrtcvad is not None
        assert 0 == Vad._webrtcvad.WebRtcVad_Init(self)
        if mode is not None:
            self.set_mode(mode)
    
    def __del__(self):
        assert Vad._webrtcvad is not None
        Vad._webrtcvad.WebRtcVad_Free(self)
        self.value = None

valid_rate_and_frame_length = Vad.valid_rate_and_frame_length
