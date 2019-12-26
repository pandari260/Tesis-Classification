import numpy as np  
import array
import matplotlib.pyplot as plt
import TransformSample as transform

def generateSample(hopes, matCovariance, n, classes):
    sample, preSample = [], []
    for i in range(len(hopes)):
        np.random.seed(np.random.randint(1,1001)) #generacion aleatoria
        #np.random.seed(45)
        preSample = np.random.multivariate_normal(hopes[i], matCovariance[i], n[i]).T
        sample.append(transform.transformSample(preSample, classes[i]))
    return sample

def divideClass(sample):
    sampleC0, sampleC1 = [], []
    for item in sample:
        if(getClass(item[0]) == 0): sampleC0 += item
        else: sampleC1 += item
    return sampleC0, sampleC1

def getClass(item):
    if(item[len(item)-1] == 0): return 0
    else: return 1