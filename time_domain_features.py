from collections import defaultdict
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##Min, Max, Mean, Median, Min_x, Min_y, Min_z, Max_x, Max_y, Max_z, Avg timestep b/w obs,
##Cross Correlation, Avg difference from mean

win_length = 100
step = int(win_length/2)

def separate_windows(df):
    win_list = []
    for i in range(0,len(df),step):
        if i+win_length < len(df):
            win_list.append(df[i:i+win_length+1])
    return win_list

def min_max_mean_each_component(list_window_df):
    dict_component = defaultdict(list)
    for i in range(len(list_window_df)):
        df_win = list_window_df[i]
        dict_component['x_mean'].append(np.mean(df_win.x.values))
        dict_component['y_mean'].append(np.mean(df_win.y.values))
        dict_component['z_mean'].append(np.mean(df_win.z.values))
        dict_component['x_median'].append(np.median(df_win.x.values))
        dict_component['y_median'].append(np.median(df_win.y.values))
        dict_component['z_median'].append(np.median(df_win.z.values))
        dict_component['x_min'].append(min(df_win.x.values))
        dict_component['y_min'].append(min(df_win.y.values))
        dict_component['z_min'].append(min(df_win.z.values))
        dict_component['x_max'].append(max(df_win.x.values))
        dict_component['y_max'].append(max(df_win.y.values))
        dict_component['z_max'].append(max(df_win.z.values))
    return dict_component


def min_max_mean_magnitude(list_window_df):
    dict_component = defaultdict(list)
    for i in range(len(list_window_df)):
        df_win = list_window_df[i]
        dict_component['mag_mean'].append(np.mean(df_win.mag_acc.values))
        dict_component['mag_min'].append(min(df_win.mag_acc.values))
        dict_component['mag_max'].append(max(df_win.mag_acc.values))
        dict_component['mag_median'].append(np.median(df_win.mag_acc.values))
    return dict_component

def cross_correlation(list_window_df):
    dict_component = defaultdict(list)
    for i in range(len(list_window_df)):
        df_win = list_window_df[i]
        dict_component['cc_xz'].append(np.mean(df_win.x.values)/np.mean(df_win.z.values))
        dict_component['cc_yz'].append(np.mean(df_win.y.values)/np.mean(df_win.z.values))
    return dict_component

def avg_time_bw_obs(list_window_df):
    dict_component = defaultdict(list)
    for i in range(len(list_window_df)):
        df_win = list_window_df[i]
        dict_component['time_diff'].append(np.mean(np.ediff1d(df_win.timestep.values)))
    return dict_component

def distance_from_mean(list_window_df):
    dict_component = defaultdict(list)
    for i in range(len(list_window_df)):
        df_win = list_window_df[i]
        dict_component['dist_mean_x'].append(np.mean(np.absolute(df_win.x.values - np.mean(df_win.mag_acc.values))))
        dict_component['dist_mean_y'].append(np.mean(np.absolute(df_win.y.values - np.mean(df_win.mag_acc.values))))
        dict_component['dist_mean_z'].append(np.mean(np.absolute(df_win.z.values - np.mean(df_win.mag_acc.values))))
    return dict_component









