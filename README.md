# L-SpEx: Localized Target Speaker Extraction

The data configuration and simulation of L-SpEx. The code scripts will be released in the future.

## Data Generation:

1. Download LibriSpeech([dev-clean.tar.gz](www.openslr.org/resources/12/dev-clean.tar.gz), [test-clean.tar.gz](www.openslr.org/resources/12/test-clean.tar.gz), [train-clean-100.tar.gz](www.openslr.org/resources/12/train-clean-100.tar.gz), [train-clean-360.tar.gz](www.openslr.org/resources/12/train-clean-360.tar.gz)) and Wham_noise.

2. generate the RIRs information.

3. generate the MC-Libri2Mix dataset using RIRs information.

## Environments:

python: 3.8.3

Pytorch: 1.6
