CFLAGS = -DWEBRTC_POSIX  -DWEBRTC_LINUX -DNOMINMAX 

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

INCLUDESGMM = \
src/common_audio/signal_processing/complex_fft_tables.h \
src/common_audio/signal_processing/dot_product_with_scale.h \
src/common_audio/signal_processing/include/real_fft.h \
src/common_audio/signal_processing/include/signal_processing_library.h \
src/common_audio/signal_processing/include/spl_inl.h \
src/common_audio/signal_processing/resample_by_2_internal.h \
src/common_audio/third_party/spl_sqrt_floor/spl_sqrt_floor.h \
src/common_audio/vad/include/webrtc_vad.h \
src/common_audio/vad/vad_core.h \
src/common_audio/vad/vad_filterbank.h \
src/common_audio/vad/vad_gmm.h \
src/common_audio/vad/vad_sp.h \
src/rtc_base/checks.h \
src/rtc_base/compile_assert_c.h \
src/rtc_base/numerics/safe_compare.h \
src/rtc_base/sanitizer.h \
src/rtc_base/system/arch.h \
src/rtc_base/system/inline.h \
src/rtc_base/type_traits.h \
src/system_wrappers/include/cpu_features_wrapper.h

SOURCESRNN = \
src/common_audio/resampler/push_sinc_resampler.cc \
src/common_audio/resampler/sinc_resampler.cc \
src/common_audio/wav_file.cc \
src/rtc_base/checks.cc \
src/rtc_base/logging.cc \
src/rtc_base/string_utils.cc \
src/rtc_base/time_utils.cc \
src/rtc_base/string_encode.cc \
src/rtc_base/platform_thread_types.cc \
src/rtc_base/system/file_wrapper.cc \
src/rtc_base/strings/string_builder.cc \
src/common_audio/wav_header.cc \
src/common_audio/audio_util.cc \
src/modules/audio_processing/agc2/cpu_features.cc \
src/modules/audio_processing/agc2/rnn_vad/features_extraction.cc \
src/modules/audio_processing/agc2/rnn_vad/rnn.cc \
src/modules/audio_processing/agc2/biquad_filter.cc \
src/rtc_base/memory/aligned_malloc.cc \
src/modules/audio_processing/agc2/rnn_vad/pitch_search.cc \
src/modules/audio_processing/agc2/rnn_vad/lp_residual.cc \
src/modules/audio_processing/agc2/rnn_vad/auto_correlation.cc \
src/modules/audio_processing/agc2/rnn_vad/pitch_search_internal.cc \
src/modules/audio_processing/agc2/rnn_vad/spectral_features.cc \
src/modules/audio_processing/agc2/rnn_vad/spectral_features_internal.cc \
src/modules/audio_processing/utility/pffft_wrapper.cc \
third_party/rnnoise/src/rnn_vad_weights.cc \
third_party/pffft/src/pffft.c \
third_party/pffft/src/fftpack.c

INCLUDESRNN = \
src/common_audio/resampler/push_sinc_resampler.h \
src/common_audio/resampler/sinc_resampler.h \
src/common_audio/wav_file.h \
src/rtc_base/checks.h \
src/rtc_base/logging.h \
src/rtc_base/string_utils.h \
src/rtc_base/time_utils.h \
src/rtc_base/atomic_ops.h \
src/rtc_base/sanitizer.h \
src/rtc_base/string_encode.h \
src/rtc_base/thread_annotations.h \
src/rtc_base/platform_thread_types.h \
src/rtc_base/numerics/safe_minmax.h \
src/rtc_base/system/file_wrapper.h \
src/rtc_base/system/unused.h \
src/rtc_base/numerics/safe_conversions.h \
src/rtc_base/numerics/safe_conversions_impl.h \
src/rtc_base/strings/string_builder.h \
src/common_audio/wav_header.h \
src/common_audio/include/audio_util.h \
src/modules/audio_processing/agc2/rnn_vad/features_extraction.h \
src/modules/audio_processing/agc2/rnn_vad/common.h \
src/modules/audio_processing/agc2/rnn_vad/rnn.h \
src/modules/audio_processing/agc2/biquad_filter.h \
src/rtc_base/memory/aligned_malloc.h \
src/modules/audio_processing/agc2/rnn_vad/pitch_info.h \
src/modules/audio_processing/agc2/rnn_vad/pitch_search.h \
src/modules/audio_processing/agc2/rnn_vad/sequence_buffer.h \
src/modules/audio_processing/agc2/rnn_vad/lp_residual.h \
src/modules/audio_processing/agc2/rnn_vad/auto_correlation.h \
src/modules/audio_processing/agc2/rnn_vad/pitch_search_internal.h \
src/modules/audio_processing/agc2/rnn_vad/spectral_features.h \
src/modules/audio_processing/agc2/rnn_vad/spectral_features_internal.h \
src/modules/audio_processing/agc2/rnn_vad/ring_buffer.h \
src/modules/audio_processing/agc2/rnn_vad/symmetric_matrix_buffer.h \
src/modules/audio_processing/utility/pffft_wrapper.h \
third_party/rnnoise/src/rnn_activations.h \
third_party/rnnoise/src/rnn_vad_weights.h \
third_party/pffft/src/pffft.h \
third_party/pffft/src/fftpack.h


webrtcvadgmm.so:
	$(CXX) $(SOURCESGMM) $(CFLAGS) -Isrc -Iabseil-cpp -I. -shared -fPIC -o $@

webrtcvadrnn.so:
	$(CXX) webrtcvadrnn.cc $(SOURCESRNN) $(CFLAGS) -Isrc -Iabseil-cpp -I. -shared -fPIC -o $@
