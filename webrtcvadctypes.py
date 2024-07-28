import os
import ctypes

lib_path = os.path.abspath('webrtcvadctypes.so')
lib = ctypes.CDLL(lib_path)
