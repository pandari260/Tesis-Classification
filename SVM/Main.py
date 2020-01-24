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

directory = ["R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"]
d=0

def __showInfo(i, directory, test, resultClassify, dataTest):
    print("----------- Test nº "+str(i)+" dimension "+directory+" "+str(test)+" -------------\n ")
    print("Accuracy: ", accuracy_score(resultClassify, dataTest))
    print("Confusion matrix: ")
    print(confusion_matrix(resultClassify, dataTest))
    print("Metrics report: ")
    print(classification_report(resultClassify, dataTest))
    print("\n\n")

def __readAllTest(test, directory, d):
    for i in range(len(test)):
        file = '../INPUT/SVM/'+directory[d]+test[i]+'.csv'

        fdata = pd.read_csv(file)
        dataSet = fdata.drop('Class', axis=1)
        target = fdata['Class']

        resultClassify, dataTest = svm.classify('rbf', dataSet, target)
        __showInfo(str(i+1), directory[d], test[i], resultClassify, dataTest)


#__readAllTest(test, directory,d)

file = '../INPUT/REAL/SVM/Test-C_Easy1_noise01.csv'

fdata = pd.read_csv(file)
dataSet = fdata.drop('Class', axis=1)
target = fdata['Class']
resultClassify, dataTest = svm.classify('rbf', dataSet, target)
__showInfo(1, "R2-Real", 5000, resultClassify, dataTest)


