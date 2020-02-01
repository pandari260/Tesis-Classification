import pandas as pd
import SVM as svm
import matplotlib.pyplot as plt
import SearcherFile as searcher
import Printer 
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score


test = [        "/t1-ConjuntosDisjuntos",
                "/t2-ConjuntosSolapados",
                "/t3-CuadranteOpuesto",
                "/t4-CuadranteOpuestoSolapado",
                "/t5-Encerrado",
                "/t6-EncerradoSolapado",
                "/t7-DiagonalIntercalada",
                "/t8-DiagonalIntercaladaSolapada"   ]

test_real = [   "/Test-C_Easy1_noise01",
                "/Test-C_Easy1_noise02",
                "/Test-C_Easy1_noise03",
                "/Test-C_Easy1_noise04",
                "/Test-C_Easy1_noise005",
                "/Test-C_Easy2_noise01",
                "/Test-C_Easy2_noise02",
                "/Test-C_Difficult1_noise01",
                "/Test-C_Test_LFPcorr_Easy2_noise015",
                "/Test-C_Drift_Easy2_noise015"    ]

directory = ["R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"]
directory_real = ["R2-Real"]
d=0

test = test_real
directory = directory_real

for i in range(len(test)):
    dataSet, target = searcher.searchDatafile(directory[d], test[i])
    resultClassify, dataTest = svm.classify('linear', dataSet, target)
    Printer.showResult(str(i+1), directory[d], test[i], resultClassify, dataTest)
