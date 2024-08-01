/*
 *  Copyright (c) 2018 The WebRTC project authors. All Rights Reserved.
 *
 *  Use of this source code is governed by a BSD-style license
 *  that can be found in the LICENSE file in the root of the source
 *  tree. An additional intellectual property rights grant can be found
 *  in the file PATENTS.  All contributing project authors may
 *  be found in the AUTHORS file in the root of the source tree.
 */


#include <array>
#include <string>
#include <vector>

#include "common_audio/include/audio_util.h"
#include "common_audio/resampler/push_sinc_resampler.h"
#include "modules/audio_processing/agc2/rnn_vad/common.h"
#include "modules/audio_processing/agc2/rnn_vad/features_extraction.h"
#include "modules/audio_processing/agc2/rnn_vad/rnn.h"

static const int kInitCheck = 42;
static const int kValidRates[] = { 8000, 16000, 32000, 48000 };
static const size_t kRatesSize = sizeof(kValidRates) / sizeof(*kValidRates);

struct VadRnnInstT
{
    int init_flag;
    webrtc::rnn_vad::FeaturesExtractor features_extractor;
    webrtc::rnn_vad::RnnVad rnn_vad;
    std::array<float, webrtc::rnn_vad::kFrameSize10ms24kHz> samples_10ms_24kHz;
    std::array<float, webrtc::rnn_vad::kFeatureVectorSize> feature_vector;
    std::vector<float> samples8khz_10ms, samples16khz_10ms, samples32khz_10ms, samples48khz_10ms;
    webrtc::PushSincResampler resampler8khz, resampler16khz, resampler32khz, resampler48khz;

    VadRnnInstT() :
                           rnn_vad(webrtc::GetAvailableCpuFeatures()), 
                features_extractor(webrtc::GetAvailableCpuFeatures()),
                init_flag(0),
                samples8khz_10ms ( 8000 / 100), resampler8khz ( 8000 / 100, webrtc::rnn_vad::kFrameSize10ms24kHz), 
                samples16khz_10ms(16000 / 100), resampler16khz(16000 / 100, webrtc::rnn_vad::kFrameSize10ms24kHz), 
                samples32khz_10ms(32000 / 100), resampler32khz(32000 / 100, webrtc::rnn_vad::kFrameSize10ms24kHz), 
                samples48khz_10ms(48000 / 100), resampler48khz(48000 / 100, webrtc::rnn_vad::kFrameSize10ms24kHz) 
    { }
};

typedef struct VadRnnInstT VadRnnInst;

//typedef struct WebRtcVadInst VadInst;

//extern "C"  {

extern "C" VadRnnInst* WebRtcVadRnn_Create()
{
    VadRnnInstT* self = new VadRnnInstT();
    self->init_flag = 0;
    VadRnnInst* handle = (VadRnnInst*)self;
    return handle;
}

extern "C" void WebRtcVadRnn_Free(VadRnnInst* handle)
{
    VadRnnInstT* self = (VadRnnInst*)handle;
    delete self;
}

extern "C" int WebRtcVadRnn_Init(VadRnnInst* handle)
{
    VadRnnInstT* self = (VadRnnInst*)handle;
    if (self == NULL) {
        return -1;
    }
    self->init_flag = kInitCheck;
    return 0;
}

extern "C" int WebRtcVadRnn_set_mode(VadRnnInst* handle, int mode) {
    VadRnnInstT* self = (VadRnnInstT*) handle;

    if (handle == NULL) {
        return -1;
    }
    if (self->init_flag != kInitCheck) {
        return -1;
    }

    return 0;
}

extern "C" int WebRtcVadRnn_ValidRateAndFrameLength(int rate, size_t frame_length)
{
  const int valid_length_ms = 10;
  // We only allow 10ms frames. Loop through valid frame rates and see if we have a matching pair.
  for (size_t i = 0; i < kRatesSize; i++)
  {
      if (kValidRates[i] == rate)
      {
          size_t valid_length = (size_t)(kValidRates[i] / 1000 * valid_length_ms);
          if (frame_length == valid_length) return 0;
          break;
      }
  }
  return -1;
}

extern "C" float WebRtcVadRnn_Process(VadRnnInst* handle, int fs, const int16_t* audio_frame, size_t frame_length)
{
    int vad = -1;
    VadRnnInstT* self = (VadRnnInstT*) handle;
    
    if (handle == NULL) {
        return -1;
    }

    if (self->init_flag != kInitCheck) {
        return -1;
    }
    if (audio_frame == NULL) {
        return -1;
    }
    if (WebRtcVadRnn_ValidRateAndFrameLength(fs, frame_length) != 0) {
        return -1;
    }
    //if (read_samples < frame_size_10ms) break; 
    
    auto& samples_10ms = fs == 8000 ? self->samples8khz_10ms : fs == 16000 ? self->samples16khz_10ms : fs == 32000 ? self->samples32khz_10ms : self->samples48khz_10ms;
    auto& resampler = fs == 8000 ? self->resampler8khz : fs == 16000 ? self->resampler16khz : fs == 32000 ? self->resampler32khz : self->resampler48khz;
    
    webrtc::S16ToFloatS16(audio_frame, frame_length, samples_10ms.data());

    resampler.Resample(samples_10ms.data(), samples_10ms.size(), self->samples_10ms_24kHz.data(), self->samples_10ms_24kHz.size());
    bool is_silence = self->features_extractor.CheckSilenceComputeFeatures(self->samples_10ms_24kHz, self->feature_vector);
    return self->rnn_vad.ComputeVadProbability(self->feature_vector, is_silence);
}

//}
