import numpy as np  
import array
import matplotlib.pyplot as plt

#Genera un conjunto de muestras multivariblaes con distribucion normal de dimension 'n'.
def generateSample(hopes, matCovariance, n, classes):
    sample, preSample, c0, c1 = [], [], [], []
    for i in range(len(classes)):
        np.random.seed(np.random.randint(1,1001)) #generacion aleatoria
        #np.random.seed(45)
        preSample = np.random.multivariate_normal(hopes[i], matCovariance[i], n[i]).T
        sample.append(__transformSample(preSample, classes[i]))
    return sample

#Dado un conjunto de muestras, aplica el formato usado por CRIO y devuleve los conjuntos clase0 y clase1.
def convertSampleCRIO(sample):
    c0,c1 = divideClass(sample)
    return __popClass(c0), __popClass(c1)

#Dado un conjunto de muestras, las separa por clases.
def divideClass(sample):
    sampleC0, sampleC1 = [], []
    for item in sample:
        if(__getClass(item[0]) == 0): sampleC0 += item
        else: sampleC1 += item
    return sampleC0, sampleC1

#Aplica formato de cantidad de decimales y agrega la clase que pertenece cada una de las muestras.
def __transformSample(sampleGenerated, clss):
    sample, data = [],[]
    header = []
    for i in range(len(sampleGenerated[0])): 
        for j in range(len(sampleGenerated)):
            data.append(round(sampleGenerated[j][i],4)) #Solo se incluyen hasta los 5 decimales
        data.append(clss)
        sample.append(tuple(data))
        data = []
    return sample

#Elimina el campo 'Clase' de la muestra
def __popClass(sample):
    return list(map(lambda line: line[:-1], sample))

def __getClass(item):
    return 0 if(item[len(item)-1] == 0) else 1
