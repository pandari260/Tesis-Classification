import pandas as pd
import SVM as svm
import matplotlib.pyplot as plt
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

directory = ["R2", "R3", "R20"]
d=2

for i in range(len(test)):
    file = '../INPUT/SVM/'+directory[d]+test[i]+'.csv'

    fdata = pd.read_csv(file)
    dataSet = fdata.drop('Class', axis=1)
    target = fdata['Class']

    resultClassify, dataTest = svm.classify('rbf', dataSet, target)
    print("----------- Test nº "+str(i+1)+" dimension "+directory[d]+" "+test[i]+" -------------\n ")
    print("Accuracy: ", accuracy_score(resultClassify, dataTest))
    print("Confusion matrix: ")
    print(confusion_matrix(resultClassify, dataTest))
    print("Metrics report: ")
    print(classification_report(resultClassify, dataTest))
    print("\n\n")

