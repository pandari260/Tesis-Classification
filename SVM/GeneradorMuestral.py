import numpy as np  
import array as array
import matplotlib.pyplot as plt

class GeneradorMuestral:

    muestraC1, muestraC2 = [], []

    def generarMuestra(self, mu, v, d, n, clase):
        mean = GeneradorMuestral.generarEsperanzas(mu,d)
        cov = GeneradorMuestral.generarCovarianzas(v,d)
        #np.random.seed(np.random.randint(1,1001)) #generacion aleatoria
        np.random.seed(45)
        muestra = np.random.multivariate_normal(mean, cov, n).T
        return self.convertirMuestra(muestra, clase)

    def convertirMuestra(self, datosGenerados, clase):
        muestra, dato = [],[]
        for i in range(len(datosGenerados[0])): 
            for j in range(len(datosGenerados)):
                dato.append(round(datosGenerados[j][i],4)) #Solo se incluyen hasta los 5 decimales
            dato.append(clase)
            muestra.append(dato)
            dato = []
            
        if(clase == 1): self.muestraC1 += muestra 
        else: self.muestraC2 += muestra
        return muestra    

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

    def getMuestraC1(self):
        return self.muestraC1

    def getMuestraC2(self):
        return self.muestraC2
        
        
            