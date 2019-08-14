import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score
from sklearn.model_selection import train_test_split

class ClasificadorSVM:

    clasificador = ""

    def __init__(self, kernel):
        self.clasificador = SVC(C=1, degree=3, gamma='scale', kernel=kernel)
        #C determina la zona de amplificacion al definir los vectores de soporte
        

    def leerMuestra(self, archivo):
        dataSet = pd.read_csv(archivo)
        datos = dataSet.drop('Class', axis=1)
        target = dataSet['Class']

        return datos, target        

    @staticmethod
    def mostrarMetricas(Y_test, y_pred):   
        
        print("Precicion: ", accuracy_score(Y_test, y_pred))
        print("Matriz de confucion: ")
        print(confusion_matrix(Y_test, y_pred))
        print("Reporte de metricas: ")
        print(classification_report(Y_test, y_pred))

    def clasificarMuestra(self, archivo):
        datos, target = self.leerMuestra(archivo)
        X_train, X_test, Y_train, Y_test = train_test_split(datos, target, test_size = 0.7)
        self.clasificador.fit(X_train, Y_train)
        y_pred = self.clasificador.predict(X_test)
        ClasificadorSVM.mostrarMetricas(Y_test, y_pred)

   