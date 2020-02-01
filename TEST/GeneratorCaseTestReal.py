from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt 
import Plotter as plotter
import Exporter as exporter
import pandas as pd
	
file = [    "C_Easy1_noise01",
            "C_Easy1_noise02",
            "C_Easy1_noise03",
            "C_Easy1_noise04",
            "C_Easy1_noise005",
            "C_Easy2_noise01",
            "C_Easy2_noise02",
            "C_Difficult1_noise01",
            "C_Test_LFPcorr_Easy2_noise015",
            "C_Drift_Easy2_noise015"    ]

def __runTest(file):
    c0, c1, c_ret = [], [], []
    f= loadmat("../../Simulator/"+file+".mat")

    arrTime = f['spike_times'][0][0][0]
    arrClass  = f['spike_class'][0][1][0]
    arrData = f['data'][0]

    for i in range(0, len(arrTime)):
        clss = c0 if(arrClass[i] == 0) else c1
        clss.append((round(arrData[arrTime[i]],5), arrTime[i], arrClass[i]))

    name = "../Resources/R2-Real/Test-"+ file +".csv"
    c_ret.append(c0)
    c_ret.append(c1)
    exporter.exportCaseTest(c_ret, name)
    plotter.graphSample(c0, c1)
    plt.show()


for i in file:  __runTest(i)



