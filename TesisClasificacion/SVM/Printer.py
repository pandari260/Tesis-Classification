import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score

def printOutputSVM(Y_test, y_pred):   
    print("Accuracy: ", accuracy_score(Y_test, y_pred))
    print("Confusion matrix: ")
    print(confusion_matrix(Y_test, y_pred))
    print("Metrics report: ")
    print(classification_report(Y_test, y_pred))

