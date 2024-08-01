# webrtcvadctypes

```shell
git clone https://github.com/vadimkantorov/webrtcvadctypes --recursive
make webrtcvadctypesgmm.so
make webrtcvadctypesrnn.so

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
