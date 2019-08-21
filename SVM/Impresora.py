import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score

def imprimirGraficoBidimensional( x, y):        
    plt.plot(x, y, 'x')
    plt.axis('equal')
    plt.show()

def imprimirOutSVM(Y_test, y_pred):   
    print("Precicion: ", accuracy_score(Y_test, y_pred))
    print("Matriz de confucion: ")
    print(confusion_matrix(Y_test, y_pred))
    print("Reporte de metricas: ")
    print(classification_report(Y_test, y_pred))

