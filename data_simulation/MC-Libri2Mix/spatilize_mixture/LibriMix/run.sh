#!/usr/bin/env bash

set -eu
# generate the RIRs information via pyroomacoustics
python run_sample_reverb_libri.py
# generate MC-Libri2Mix dataset using generated RIRs
./generate_librimix.sh /export/home/nanahou/gm/demo/espnet_ss/espnet/egs2/wsj0_2mix_spatialized/L-SpEx/data_simulation/MC-Libri2Mix/spatilize_mixture
