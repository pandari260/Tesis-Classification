import numpy as np  
import matplotlib.pyplot as plt  
import Sample as sample
import Exporter as exporter
import Plotter as plotter

class CaseTest:

    def __init__(self, name, d, n, mMu, classes):
        self.__name = name
        self.__d = d
        self.__n = n
        self.__mMu = self.__initMu(mMu[0],mMu[1])
        self.__mCov = self.__initCov()
        self.__classes = classes

    #Inicializa la matriz de covarianzas.
    def __initCov(self):
        m = []
        for i in range(len(self.__n)):
            base = np.identity(self.__d)
            m.append(base)    
        return m   

    #Inicializa la matriz de esperanzas.
    def __initMu(self, mu, seed):
        m = []
        for i in mu:
            base = []
            base.append(i[0])
            base.append(i[1])
            for j in range(self.__d-2): base.append(seed)
            m.append(base)
        return m

    #genera un conjunto de muestras con los parametros indicados.
    def initTest(self):
        return sample.generateSample(self.__mMu, self.__mCov, self.__n, self.__classes)