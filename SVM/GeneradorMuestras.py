import numpy as np  
import array as array
import matplotlib.pyplot as plt

class GeneradorMuestras:
    
    @staticmethod
    def generarUnidimensional(mu, sigma, n):
        np.random.seed(np.random.randint(1,1001)) # Ver si queda la semilla o no
        s = np.random.normal(mu, sigma, size=(n))
        return s

    @staticmethod
    def generarNdimensional(d, n):
        mean = GeneradorMuestras.generarEsperanzas(d)
        cov = GeneradorMuestras.generarCovarianzas(d)
        print(cov)
        np.random.seed(np.random.randint(1,1001)) #generacion aleatoria
        #np.random.seed(42)
        return  np.random.multivariate_normal(mean, cov, n).T
         
    @staticmethod
    def generarEsperanzas(n):
        esp = []
        for i in range(n):  
            esp.append(0)
        return esp

    @staticmethod
    def generarCovarianzas(n):
        cov, cov_i = [], []
        for i in range(n):
            for j in range(n):
                if i==j:
                    cov_i.append(1)                         
                else:
                    cov_i.append(0)
            cov.append( cov_i)
            cov_i = []
        return cov    

        
        
            