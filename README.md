# L-SpEx: Localized Target Speaker Extraction

The data configuration and simulation of [L-SpEx](https://arxiv.org/abs/2202.09995). The code scripts will be released in the future.

## Data Generation:

1. Download LibriSpeech([dev-clean.tar.gz](www.openslr.org/resources/12/dev-clean.tar.gz), [test-clean.tar.gz](www.openslr.org/resources/12/test-clean.tar.gz), [train-clean-100.tar.gz](www.openslr.org/resources/12/train-clean-100.tar.gz), [train-clean-360.tar.gz](www.openslr.org/resources/12/train-clean-360.tar.gz)) and Wham_noise([wham_noise.zip](https://storage.googleapis.com/whisper-public/wham_noise.zip)). And move the librispeech and wham_noise to 'data_simulation/MC-Libri2Mix/spatilize_mixture/'

2. generate the RIRs information.
```bash
python run_sample_reverb_libri.py
```

3. generate the MC-Libri2Mix dataset using RIRs information.
```bash
./generate_librimix.sh YOUR_SAVE_PATH
```
NOTE: you can also download the generated MC-Libri2Mix dataset by using this dropbox link ([Download](https://www.dropbox.com/sh/ifz9w86v2i7zga1/AAArwDWFTtrL6f6wK9dReDm2a?dl=0))

## Environments:

python: 3.8.3

Pytorch: 1.6
