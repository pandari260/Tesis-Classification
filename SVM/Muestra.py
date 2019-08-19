import numpy as np  
import array as array
import matplotlib.pyplot as plt

class Muestra:

    @staticmethod
    def generarMuestra(mu, v, d, n, clase):
        mean = Muestra.generarEsperanzas(mu,d)
        cov = Muestra.generarCovarianzas(v,d)
        #np.random.seed(np.random.randint(1,1001)) #generacion aleatoria
        np.random.seed(45)
        muestra = np.random.multivariate_normal(mean, cov, n).T
        return Muestra.convertirMuestra(muestra, clase)

    @staticmethod
    def convertirMuestra(datosGenerados, clase):
        muestra, dato = [],[]
        for i in range(len(datosGenerados[0])): 
            for j in range(len(datosGenerados)):
                dato.append(round(datosGenerados[j][i],4)) #Solo se incluyen hasta los 5 decimales
            dato.append(clase)
            muestra.append(dato)
            dato = []
        
        return muestra    

    @staticmethod
    def convertirMuestraZPL(muestra):
        nuevaMuestra, dato = [], []
        for i in range(len(muestra)):
            for j in range(len(muestra[i])):
                dato.append(i+1)
                dato.append(j+1)
                dato.append(muestra[i][j])
                nuevaMuestra.append(dato)
                dato = []
        return nuevaMuestra

    @staticmethod
    def generarEsperanzas(mu,n):
        esp = []
        for i in range(n):  
            esp.append(mu)
        return esp

    @staticmethod
    def generarCovarianzas(v,d):
        cov, cov_i = [], []
        for i in range(d):
            for j in range(d):
                if i==j:
                    cov_i.append(v)                         
                else:
                    cov_i.append(0)
            cov.append(cov_i)
            cov_i = []
        return cov    
        
            