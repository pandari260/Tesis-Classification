'''
Created on 3 dic. 2019

@author: javier
'''

class Cluster(object):
    '''
    esta clase representa un cluster para el metodo CRIO
    '''


    def __init__(self, s,d):
        '''
        un cluster contiene un conjunto de muestras y la dimension de cada una de las muestras. Cada una de las muestras debe tener la misma dimension
        '''
        self.__samples = s
        self.__dimension = d
    
    def getSamples(self):
        return self.__samples
    
    def getSize(self):
        return len(self.__samples)
    
    def getDimension(self):
        return self.__dimension