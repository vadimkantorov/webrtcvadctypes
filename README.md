Variant of https://github.com/wiseman/py-webrtcvad but based on pure ctypes wrapper of https://webrtc.googlesource.com/src/+/refs/heads/main/modules/audio_processing/vad/, so might be slightly slower but does not require compiling and installing a Python module (instead a providing an absolute path to a native `.so` shared library is sufficient).

Also includes a similar-interfaced variant of https://webrtc.googlesource.com/src/+/refs/heads/main/modules/audio_processing/agc2/rnn_vad/ but it is not tested.

Not production ready, for working with long audios you will want to add a function that performs the frame loop in C++ and binds that.

```shell
git clone https://github.com/vadimkantorov/webrtcvadctypes --recursive
make libwebrtcvadctypesgmm.so
make libwebrtcvadctypesrnn.so
python test_webrtcvadctypes.py

# git submodule add --branch lts_2024_07_22 git@github.com:abseil/abseil-cpp.git
# git submodule add https://webrtc.googlesource.com/src/
```

# Notes
- `webrtcvadctypes.py` interface and `test_webrtcvadctypes.py` are taken from https://github.com/wiseman/py-webrtcvad
- `third_party` contents is taken from https://chromium.googlesource.com/chromium/src/third_party/

# References
- https://github.com/wiseman/py-webrtcvad
- https://github.com/wiseman/py-webrtcvad/issues/69
- https://github.com/jzi040941/webrtc_rnnvad
- https://github.com/ladenedge/WebRtcVadSharp/blob/main/WebRtcVadSharp/WebRtc/WebRtcDll.cs
- https://webrtc.googlesource.com/src/
- https://webrtc.googlesource.com/src/+/refs/heads/main/modules/audio_processing/agc2/rnn_vad/
- https://webrtc.googlesource.com/src/+/refs/heads/master/modules/audio_processing/agc2/rnn_vad/
- https://chromium.googlesource.com/external/webrtc/+log/master/modules/audio_processing/agc2/rnn_vad
- https://chromium.googlesource.com/external/webrtc/+log/main/modules/audio_processing/agc2/rnn_vad
- https://github.com/wiseman/py-webrtcvad/blob/master/example.py
