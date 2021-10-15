import numpy as np
from numpy.random import uniform

def draw_params(mic_width=0.05, source_num=3, min_spk_spk_theta_dist=15, reverb_level="medium"):

    # room
    room_dim = np.array([uniform(5, 10),
                         uniform(5, 10),
                         uniform(3, 4)])

    # microphone
    array_x = room_dim[0]/2 + uniform(-0.2, 0.2)
    array_y = room_dim[1]/2 + uniform(-0.2, 0.2)
    array_z = uniform(1.0, 2.0)
    center = np.array([array_x, array_y, array_z])
    mics = np.array([np.array([array_x-1.5*mic_width, array_y, array_z]),
                    np.array([array_x-0.5*mic_width, array_y, array_z]),
                    np.array([array_x+0.5*mic_width, array_y, array_z]),
                    np.array([array_x+1.5*mic_width, array_y, array_z])])

    # speakers (or sources)
    source_num = 3
    success = False
    while success == False:
        spk_doa = []
        spk_dist = []
        spk_pos = []
        for ss in range(source_num):
            s_theta = np.random.randint(0,180)
            spk_doa.append(s_theta)
            mic_spk_dist = uniform(0.75, 2)
            spk_dist.append(mic_spk_dist)
            spk_pos.append(np.array([(array_x+mic_spk_dist*np.cos(s_theta/180*np.pi)),
                            (array_y+mic_spk_dist*np.sin(s_theta/180*np.pi)),
                            array_z]))
        # TODO: check the distance of each speaker, requirement: >= 15 degree
        success = check_spks_pos(spk_doa, min_spk_spk_theta_dist)

    # T60
    if reverb_level == "high":
        T60 = uniform(0.4, 1.0)
    elif reverb_level == "medium":
        T60 = uniform(0.2, 0.6)
    elif reverb_level == "low":
        T60 = uniform(0.1, 0.3)

    return [room_dim, mics, spk_pos, spk_doa, T60, spk_dist]


def check_spks_pos(spk_doa, min_spk_spk_theta_dist):
    for i in range(len(spk_doa)):
        for j in range(i+1, len(spk_doa)):
            if np.abs(spk_doa[i] - spk_doa[j]) < min_spk_spk_theta_dist:
                return False
    return True
