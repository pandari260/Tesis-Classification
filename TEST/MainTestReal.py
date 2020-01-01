from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt 
import Plotter as plotter
import Exporter as exporter

f= loadmat('../../C_Easy1_noise01.mat')

arrTime = f['spike_times'][0][0][0]
arrClass  = f['spike_class'][0][1][0]
arrData = f['data'][0]
c0,c1 = [], []

for i in range(0, len(arrTime)):
    if(arrClass[i] == 0): c0.append([round(arrData[arrTime[i]],5), arrTime[i], 0])
    else:   c1.append([round(arrData[arrTime[i]],5), arrTime[i], 1])

name = "t1-Simulacion1"
exporter.createFileOutputReal(c0, c1, name)

fdata = pd.read_csv(file)
dataSet = fdata.drop('Class', axis=1)
target = fdata['Class']

resultClassify, dataTest = svm.classify('rbf', dataSet, target)
#plotter.graphSample(c0,c1)
#plt.show()
