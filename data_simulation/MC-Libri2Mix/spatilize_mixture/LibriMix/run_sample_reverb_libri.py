import numpy as np
import pandas as pd
import os
from sample_reverb_libri import draw_params

SPLIT_NAMES = {'Train-100': 'train-clean-100', 'Train-360': 'train-clean-360', 'Valid': 'dev-clean', 'Test': 'test-clean'}

SEED = 17
np.random.seed(SEED)

FILELIST_STUB = os.path.join('metadata', 'Libri2Mix', 'libri2mix_{}.csv')
REVERB_STUB = os.path.join('reverb_params', 'Libri2Mix', 'libri2mix_{}.csv')
if not os.path.exists(os.path.dirname(REVERB_STUB)):
    os.makedirs(os.path.dirname(REVERB_STUB))

for split_long, split_short in SPLIT_NAMES.items():
    print('Running {} Set'.format(split_long))
    filelist_path = FILELIST_STUB.format(split_short)
    filelist_df = pd.read_csv(filelist_path)
    utt_ids = list(filelist_df['mixture_ID'])

    #mic_spacing = list(filelist_df['mic_spacing'])
    #reverb_level = list(filelist_df['reverb_level'])

    utt_list, param_list = [], []
    for utt in utt_ids:
        room_params = draw_params(mic_width=0.05, source_num=3, min_spk_spk_theta_dist=15, reverb_level="medium")

        room_dim = room_params[0]
        mics = room_params[1]
        s1 = room_params[2][0]
        s2 = room_params[2][1]
        s3 = room_params[2][2]
        s1_doa = room_params[3][0]
        s2_doa = room_params[3][1]
        s3_doa = room_params[3][2]
        T60 = room_params[4]

        param_dict = { 'room_x' : room_dim[0],
                       'room_y' : room_dim[1],
                       'room_z' : room_dim[2],
                       'mic1_x' : mics[0][0],
                       'mic2_x' : mics[1][0],
                       'mic3_x' : mics[2][0],
                       'mic4_x' : mics[3][0],
                       'mic_y' : mics[0][1],
                       'mic_z' : mics[0][2],
                       's1_x' : s1[0],
                       's1_y' : s1[1],
                       's1_z' : s1[2],
                       's2_x' : s2[0],
                       's2_y' : s2[1],
                       's2_z' : s2[2],
                       's3_x' : s3[0],
                       's3_y' : s3[1],
                       's3_z' : s3[2],
                       's1_doa' : s1_doa,
                       's2_doa' : s2_doa,
                       's3_doa' : s3_doa,
                       'T60' : T60 }

        utt_list.append(utt)
        param_list.append(param_dict)

    reverb_param_df = pd.DataFrame(data=param_list, index=utt_list,
                                   columns=['room_x', 'room_y', 'room_z', 'mic1_x', 'mic2_x', 'mic3_x', 'mic4_x', 'mic_y', 'mic_z', 's1_x', 's1_y', 's1_z', 's2_x', 's2_y', 's2_z', 's3_x', 's3_y', 's3_z', 's1_doa', 's2_doa', 's3_doa', 'T60'])
    reverb_param_path = REVERB_STUB.format(split_short)
    reverb_param_df.to_csv(reverb_param_path, index=True, index_label='mixture_ID')
