import pandas as pd
import SVM as svm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score

testd2 = [  "R2/t1d2-ConjuntosDisjuntos",
            "R2/t2d2-ConjuntosSolapados",
            "R2/t3d2-ConjuntosDiagonalizados",
            "R2/t4d2-ConjuntosDiagonalizadosSolapados",
            "R2/t5d2-ConjuntosCruz",
            "R2/t6d2-CuadranteOpuesto",
            "R2/t7d2-DiagonalIntercalada",
            "R2/t8d2-DiagonalIntercaladaSolapada",
            "R2/t9d2-Encerrado",
            "R2/t10d2-Piramide"                 ]

testd3 = [  "R3/t1d3-ConjuntosDisjuntos",
            "R3/t2d3-ConjuntosSolapados",
            "R3/t3d3-ConjuntosDiagonalizados"
        ]

testd = [   "R2/t3d2-ConjuntosDiagonalizados",
            "R3/t3d3-ConjuntosDiagonalizados"
            ]

test = testd
for i in range(len(test)):
    file = '../INPUT/SVM/'+test[i]+'.csv'

    fdata = pd.read_csv(file)
    dataSet = fdata.drop('Class', axis=1)
    target = fdata['Class']

    resultClassify, dataTest = svm.classify('rbf', dataSet, target)
    print("----------- Test nº "+str(i+1)+" "+test[i]+" -------------\n ")
    print("Accuracy: ", accuracy_score(resultClassify, dataTest))
    print("Confusion matrix: ")
    print(confusion_matrix(resultClassify, dataTest))
    print("Metrics report: ")
    print(classification_report(resultClassify, dataTest))
    print("\n\n")

