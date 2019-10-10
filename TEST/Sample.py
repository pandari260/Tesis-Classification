import numpy as np  
import array as array
import matplotlib.pyplot as plt

def generateSample(hopes, matCovariance, n, classes):
    sample, preSample = [], []
    for i in range(len(hopes)):
        #np.random.seed(np.random.randint(1,1001)) #generacion aleatoria
        np.random.seed(45)
        preSample = np.random.multivariate_normal(hopes[i], matCovariance[i], n[i]).T
        sample.append(transformSample(preSample, classes[i]))
    return sample

def transformSample(sampleGenerated, clss):
    sample, data = [],[]
    for i in range(len(sampleGenerated[0])): 
        for j in range(len(sampleGenerated)):
            data.append(round(sampleGenerated[j][i],4)) #Solo se incluyen hasta los 5 decimales
        data.append(clss)
        sample.append(data)
        data = []
    return sample    



   
        
            