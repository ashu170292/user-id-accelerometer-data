from collections import defaultdict
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.fftpack

##Spectral centroid, mean fft across all axes, cross correlation, spectral centroid

def fft_mean_each_component(list_window_df):
    dict_component = defaultdict(list)
    for i in range(len(list_window_df)):
        df_win = list_window_df[i]
        # freq = scipy.fftpack.fftfreq(len(df_win), d=np.mean(np.ediff1d(df_win.timestep.values)))
        fft_x = np.abs(scipy.fftpack.fft(df_win.x.values))
        fft_y = np.abs(scipy.fftpack.fft(df_win.y.values))
        fft_z = np.abs(scipy.fftpack.fft(df_win.z.values))
        spec_cent_x = np.dot(fft_x,df_win.x.values)/len(df_win)
        spec_cent_y = np.dot(fft_y, df_win.y.values) / len(df_win)
        spec_cent_z = np.dot(fft_z, df_win.z.values) / len(df_win)
        dict_component['fft_x_mean'].append(np.mean(fft_x))
        dict_component['fft_y_mean'].append(np.mean(fft_y))
        dict_component['fft_z_mean'].append(np.mean(fft_z))
        dict_component['fft_x_median'].append(np.median(fft_x))
        dict_component['fft_y_median'].append(np.median(fft_y))
        dict_component['fft_z_median'].append(np.median(fft_z))
        dict_component['spec_cent_x'].append(spec_cent_x)
        dict_component['spec_cent_y'].append(spec_cent_y)
        dict_component['spec_cent_z'].append(spec_cent_z)
        # dict_component['cc_fft_xz'].append(np.mean(fft_x)/np.mean(fft_z))
        # dict_component['cc_fft_yz'].append(np.mean(fft_y) / np.mean(fft_z))
    return dict_component