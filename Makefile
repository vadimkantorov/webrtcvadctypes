CFLAGS = -DWEBRTC_POSIX  -DWEBRTC_LINUX -DNOMINMAX 
CPATH = -Isrc -Iabseil-cpp -I.
LDFLAGS = -march=native -shared -fPIC

SOURCESGMM = \
src/common_audio/signal_processing/complex_bit_reverse.c \
src/common_audio/signal_processing/complex_fft.c \
src/common_audio/signal_processing/cross_correlation.c \
src/common_audio/signal_processing/division_operations.c \
src/common_audio/signal_processing/dot_product_with_scale.cc \
src/common_audio/signal_processing/downsample_fast.c \
src/common_audio/signal_processing/energy.c \
src/common_audio/signal_processing/get_scaling_square.c \
src/common_audio/signal_processing/min_max_operations.c \
src/common_audio/signal_processing/resample_48khz.c \
src/common_audio/signal_processing/resample_by_2_internal.c \
src/common_audio/signal_processing/resample_fractional.c \
src/common_audio/signal_processing/spl_init.c \
src/common_audio/signal_processing/spl_inl.c \
src/common_audio/signal_processing/spl_sqrt.c \
src/common_audio/signal_processing/vector_scaling_operations.c \
src/common_audio/third_party/spl_sqrt_floor/spl_sqrt_floor.c \
src/common_audio/vad/vad_core.c \
src/common_audio/vad/vad_filterbank.c \
src/common_audio/vad/vad_gmm.c \
src/common_audio/vad/vad_sp.c \
src/common_audio/vad/webrtc_vad.c \
src/rtc_base/checks.cc

SOURCESRNN = webrtcvadrnn.cc \
src/common_audio/resampler/push_sinc_resampler.cc \
src/common_audio/resampler/sinc_resampler.cc \
src/common_audio/resampler/sinc_resampler_sse.cc \
src/common_audio/resampler/sinc_resampler_avx2.cc \
src/common_audio/audio_util.cc \
src/modules/audio_processing/agc2/cpu_features.cc \
src/modules/audio_processing/agc2/rnn_vad/features_extraction.cc \
src/modules/audio_processing/agc2/rnn_vad/rnn.cc \
src/modules/audio_processing/agc2/biquad_filter.cc \
src/modules/audio_processing/agc2/rnn_vad/vector_math_avx2.cc \
src/modules/audio_processing/agc2/rnn_vad/rnn_gru.cc \
src/modules/audio_processing/agc2/rnn_vad/rnn_fc.cc \
src/modules/audio_processing/agc2/rnn_vad/pitch_search.cc \
src/modules/audio_processing/agc2/rnn_vad/lp_residual.cc \
src/modules/audio_processing/agc2/rnn_vad/auto_correlation.cc \
src/modules/audio_processing/agc2/rnn_vad/pitch_search_internal.cc \
src/modules/audio_processing/agc2/rnn_vad/spectral_features.cc \
src/modules/audio_processing/agc2/rnn_vad/spectral_features_internal.cc \
src/modules/audio_processing/utility/pffft_wrapper.cc \
src/system_wrappers/source/cpu_features.cc \
src/rtc_base/memory/aligned_malloc.cc \
src/rtc_base/logging.cc \
src/rtc_base/string_encode.cc \
src/rtc_base/strings/string_builder.cc \
src/rtc_base/string_utils.cc \
src/rtc_base/time_utils.cc \
src/rtc_base/system_time.cc \
src/rtc_base/platform_thread_types.cc \
src/rtc_base/checks.cc \
third_party/rnnoise/src/rnn_vad_weights.cc \
third_party/pffft/src/pffft.c \
third_party/pffft/src/fftpack.c

webrtcvadctypesgmm.so:
	$(CXX) $(SOURCESGMM) $(CFLAGS) $(CPATH) $(LDFLAGS) -o $@

webrtcvadctypesrnn.so:
	$(CXX) $(SOURCESRNN) $(CFLAGS) $(CPATH) $(LDFLAGS) -o $@
