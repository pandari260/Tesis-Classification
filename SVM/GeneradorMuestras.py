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
    def generarNdimensional(mu,v,d, n):
        mean = GeneradorMuestras.generarEsperanzas(mu,d)
        cov = GeneradorMuestras.generarCovarianzas(v,d)
        print(cov)
        np.random.seed(np.random.randint(1,1001)) #generacion aleatoria
        #np.random.seed(42)
        return  np.random.multivariate_normal(mean, cov, n).T
         
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

        
        
            