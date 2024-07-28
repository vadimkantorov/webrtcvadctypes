SOURCES = \
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

INCLUDES = \
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

webrtcvadctypes.so:
	$(CXX) $(SOURCES) -DWEBRTC_POSIX -Isrc -Iabseil-cpp -shared -fPIC -o $@
