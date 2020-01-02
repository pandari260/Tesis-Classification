from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt 
import Plotter as plotter
import Exporter as exporter
import pandas as pd

f= loadmat('../../C_Easy1_noise01.mat')

arrTime = f['spike_times'][0][0][0]
arrClass  = f['spike_class'][0][1][0]
arrData = f['data'][0]
c0,c1 = [], []

print(arrClass)
print(arrTime)
for i in range(0, len(arrTime)):
    clss = c0 if(arrClass[i] == 0) else c1
    clss.append((round(arrData[arrTime[i]],5), arrTime[i], 0))

name = "../INPUT/REAL/SVM/t1-Simulacion1.csv"
print(c0)
print(np.concatenate((c0,c1), axis=0))
exporter.createFileOutputReal(np.concatenate((c0,c1), axis=0), name)

print(c0)
