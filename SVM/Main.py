import pandas as pd
import Classifier as svm
import matplotlib.pyplot as plt
import SearcherFile as searcher
import Printer 
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score
import csv

test = [    [   "/t1-ConjuntosDisjuntos",
                "/t2-ConjuntosSolapados",
                "/t3-CuadranteOpuesto",
                "/t4-CuadranteOpuestoSolapado",
                "/t5-Encerrado",
                "/t6-EncerradoSolapado",
                "/t7-DiagonalIntercalada",
                "/t8-DiagonalIntercaladaSolapada"   ],

            [   "/Test-C_Easy1_noise01",
                "/Test-C_Easy1_noise02",
                "/Test-C_Easy1_noise03",
                "/Test-C_Easy1_noise04",
                "/Test-C_Easy1_noise005",
                "/Test-C_Easy2_noise01",
                "/Test-C_Easy2_noise02",
                "/Test-C_Difficult1_noise01",
                "/Test-C_Test_LFPcorr_Easy2_noise015",
                "/Test-C_Drift_Easy2_noise015"    ]  ]

directory = ["R2", "R2-Real", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10","R12","R13","R14","R15","R16","R17","R18","R19", "R20"]
d=10
test = test[0]


for i in range(len(test)):
    dataSet, target = searcher.searchDatafile(directory[d], test[i])
    resultClassify, dataTest = svm.classify('rbf', dataSet, target)
    Printer.showResult(str(i+1), directory[d], test[i], resultClassify, dataTest)
