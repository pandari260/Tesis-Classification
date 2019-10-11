import pandas as pd
import SVM as svm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score

name = "t2d2-ConjuntosSolapados"

file = '../INPUT/SVM/'+name+'.csv'

fdata = pd.read_csv(file)
dataSet = fdata.drop('Class', axis=1)
target = fdata['Class']

resultClassify, dataTest = svm.classify('rbf', dataSet, target)

print("Accuracy: ", accuracy_score(resultClassify, dataTest))
print("Confusion matrix: ")
print(confusion_matrix(resultClassify, dataTest))
print("Metrics report: ")
print(classification_report(resultClassify, dataTest))

