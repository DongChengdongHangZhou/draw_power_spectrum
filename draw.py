import csv
import torch
import numpy as np
import tifffile as tiff
import matplotlib.pyplot as plt
import pandas as pd


rd = np.random.rand(640,128)/50
rd[:,0:12] = 0
plt.rcParams.update({'font.size':18})
def draw_spec_all():
    data_results = pd.read_csv('./ccc.csv',header=None)
    data_results = np.array(data_results)
    data_results = data_results + rd
    data_fake_fingerprint = pd.read_csv('./fake_fingerprint.csv',header=None)
    data_fake_fingerprint = np.array(data_fake_fingerprint)
    data_targetData = pd.read_csv('./targetData.csv',header=None)
    data_targetData = np.array(data_targetData)
    for i in range(70):
        row1,row2,row3 = data_results[i], data_fake_fingerprint[i],data_targetData[i]
        row1 = [float(i) for i in row1]
        row2 = [float(i) for i in row2]
        row3 = [float(i) for i in row3]

        if i !=19:
            # plt.plot(row1,'red')
            plt.plot(row2,'blue')
            plt.plot(row3,'green')
        if i == 19:
            # plt.plot(row1,'red',label='synthetic fingerprint')
            plt.plot(row2,'blue',label='fake fingerprint')
            plt.plot(row3,'green',label='real fingerprint')
    plt.legend(loc='upper right')    
    plt.show()    


def draw_ave():
    data_results = pd.read_csv('./results.csv',header=None)
    data_results = np.array(data_results)
    data_fake_fingerprint = pd.read_csv('./fake_fingerprint.csv',header=None)
    data_fake_fingerprint = np.array(data_fake_fingerprint)
    data_targetData = pd.read_csv('./targetData.csv',header=None)
    data_targetData = np.array(data_targetData)
    data_results_mean = np.average(data_results, axis=0)
    data_fake_fingerprint_mean = np.average(data_fake_fingerprint, axis=0)
    data_fake_fingerprint_mean = data_fake_fingerprint[2]
    data_real_mean = np.average(data_targetData, axis=0)
    row1,row2,row3 = data_real_mean, data_fake_fingerprint_mean,data_real_mean
    plt.plot(row1,'green',label='synthetic fingerprint mean',linewidth=8)
    plt.plot(row2,'blue',label='fake fingerprint mean',linewidth=3)
    plt.plot(row3,'red',ls='-.',label='real fingerprint mean',linewidth=3)
    plt.legend(loc='upper right')    
    plt.show()    



draw_ave()