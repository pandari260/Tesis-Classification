'''
Created on 6 dic. 2019

@author: javier
'''
from copy import copy
from CRIO.Modelo.Sample import Sample
from __builtin__ import isinstance

class SampleContainer(object):
    '''
    Clase que da acceso a un array de muestras
    '''


    def __init__(self, s,d):
        '''
        un sampleContainer contiene un conjunto de muestras y la dimension de cada una. Todas deben tener la misma dimension
        '''
        self.__data = set(map(lambda spl: spl if isinstance(spl,Sample) else Sample(spl),s))
        self.__dimension = d
    
    def getDimension(self):
        return self.__dimension
       
    def getSamples(self):
        return self.__data
    
    def getSize(self):
        return len(self.__data)
        