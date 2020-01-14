'''
Created on 3 dic. 2019

@author: javier
'''
import numpy as np
from CRIO.Modelo.SampleContainer import SampleContainer

class Cluster(SampleContainer):
    
    '''
    esta clase representa un cluster para el metodo CRIO
    '''

    def setSamples(self, samples):
        self.__data = samples

    def __eq__(self,obj):
        return isinstance(obj,Sample) and self.__data == obj.getData()
    

#toma dos clusters y los fusiona. Los clusters deben tener el mismo valor de dimension
def mergeClusters(cluster_A,cluster_B):
    return Cluster(cluster_A.getSamples() | cluster_B.getSamples(), cluster_A.getDimension())

def distance(c1, c2):
    sampleA = np.mean(map(lambda spl: spl.getData(), c1.getSamples()),0)
    sampleB = np.mean(map(lambda spl: spl.getData(), c2.getSamples()),0)
    return np.linalg.norm(list(map(lambda x: x[0] - x[1], list(zip(sampleA, sampleB)))))    
    


