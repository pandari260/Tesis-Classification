from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt  

def intersection(lst1, lst2): 
    return set(lst1).intersection(lst2) 


f= loadmat('../../C_Easy1_noise01.mat')

print(f.keys())

arrTime = f['spike_times'][0][0][0]
arrClass  = f['spike_class'][0][1][0]
arrData = f['data'][0]
c0,c1 = [], []

print(len(arrTime))

for i in range(0, len(arrTime)):
    if(arrClass[i] == 0): c0.append((round(arrData[arrTime[i]],5), arrTime[i]))
    else:   c1.append((round(arrData[arrTime[i]],5), arrTime[i]))

print(c1)


