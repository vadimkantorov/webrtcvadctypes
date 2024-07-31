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

#include "common_audio/resampler/push_sinc_resampler.h"
#include "common_audio/wav_file.h"
#include "modules/audio_processing/agc2/rnn_vad/common.h"
#include "modules/audio_processing/agc2/rnn_vad/features_extraction.h"
#include "modules/audio_processing/agc2/rnn_vad/rnn.h"
#include "rtc_base/logging.h"

struct VadRnnInst {
    webrtc::rnn_vad::FeaturesExtractor features_extractor;
    webrtc::rnn_vad::RnnBasedVad rnn_vad;
    
    std::array<float, kFrameSize10ms24kHz> samples_10ms_24kHz;
    std::array<float, kFeatureVectorSize> feature_vector;
    
    std::vector<float> samples8khz_10ms, samples16khz_10ms, samples32khz_10ms, samples48khz_10ms;
    webrtc::rnn_vad::PushSincResampler resampler8khz, resampler16khz, resampler32khz, resampler48khz;

    VadRnnInst() : samples8khz_10ms(8000 / 100), resampler8khz(8000 / 100, kFrameSize10ms24kHz), samples16khz_10ms(16000 / 100), resampler16khz(16000 / 100, kFrameSize10ms24kHz), samples32khz_10ms(32000 / 100), resampler32khz(32000 / 100, kFrameSize10ms24kHz), samples32khz_10ms(48000 / 100), resampler48khz(48000 / 100, kFrameSize10ms24kHz), 
    {
    }
}

extern "C" {

VadRnnInst* WebRtcVadRnn_Create()
{
    return new VadnnInst();
}

int WebRtcVadRnn_Init(VadRnnInst* self)
{
    return 0;
}

void WebRtcVadRnn_Free(VadRnnInst* self)
{
    delete self;
}

int WebRtcVadRnn_ValidRateAndFrameLength(int rate, size_t frame_length)
{
    return 0;
}

float WebRtcVadRnn_Process(VadRnnInst* self, int fs, const int16_t* audio_frame, size_t frame_length)
{
    //if (read_samples < frame_size_10ms) break; 
    vector<float>& samples10ms = fs == 8000 ? self->samples8khz_10ms : fs == 16000 ? self->samples16khz_10ms : fs == 32000 ? self->samples32khz_10ms : self->samples48khz_10ms;
    self->resampler.Resample(samples_10ms.data(), samples_10ms.size(), self->samples_10ms_24kHz.data(), self->samples_10ms_24kHz.size());
    bool is_silence = self->features_extractor.CheckSilenceComputeFeatures(self->samples_10ms_24kHz, self->feature_vector);
    return self->rnn_vad.ComputeVadProbability(self->feature_vector, is_silence);
}

}
