'''
Created on 6 dic. 2019

@author: javier
'''
from copy import copy

class SampleContainer(object):
    '''
    Clase que da acceso a un array de muestras
    '''


    def __init__(self, arr,d):
        '''
        un sampleContainer contiene un array de muestras y la dimension de cada una. Todas deben tener la misma dimension
        '''
        self.__data = arr
        self.__dimension = d
    
    def getDimension(self):
        return self.__dimension
    
    def getSample(self,index):
        return self.__data[index]
    
    def getData(self):
        return self.__data
    
    def getSize(self):
        return len(self.__data)
        