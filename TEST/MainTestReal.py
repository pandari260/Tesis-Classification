from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt 
import Plotter as plotter

def intersection(lst1, lst2): 
    return set(lst1).intersection(lst2) 


f= loadmat('../../C_Easy1_noise01.mat')

print(f.keys())

arrTime = f['spike_times'][0][0][0]
arrClass  = f['spike_class'][0][1][0]
arrData = f['data'][0]
c0,c1 = [], []

for i in range(0, len(arrTime)):
    if(arrClass[i] == 0): c0.append([round(arrData[arrTime[i]],5), arrTime[i], 0])
    else:   c1.append([round(arrData[arrTime[i]],5), arrTime[i], 1])

print(c1)
#plotter.graphSample(c0,c1)
#plt.show()
