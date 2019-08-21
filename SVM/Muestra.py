import numpy as np  
import array as array
import matplotlib.pyplot as plt

def generarMuestra(esperanzas, matCovarianza, n, clases):
    muestra, preMuestra = [], []
    for i in range(len(esperanzas)):
        #np.random.seed(np.random.randint(1,1001)) #generacion aleatoria
        np.random.seed(45)
        preMuestra = np.random.multivariate_normal(esperanzas[i], matCovarianza[i], n[i]).T
        muestra.append(convertirMuestra(preMuestra, clases[i]))
    return muestra

def convertirMuestra(datosGenerados, clase):
    muestra, dato = [],[]
    for i in range(len(datosGenerados[0])): 
        for j in range(len(datosGenerados)):
            dato.append(round(datosGenerados[j][i],4)) #Solo se incluyen hasta los 5 decimales
        dato.append(clase)
        muestra.append(dato)
        dato = []
    return muestra    



   
        
            