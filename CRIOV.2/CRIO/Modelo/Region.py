'''
Created on 29 dic. 2019

@author: javier
'''
from CRIO.Modelo.SampleContainer import SampleContainer

class Region(object):
    '''
    esta clase representa una region para el metodo crio
    '''


    def __init__(self,h,d):
        '''
        una region se compone de un conjunto de muestras e hiperplanos
        '''
#        super(Region,self).__init__(s,d)
        self.__hyperplanes = set(h)
        self.__dimension = d
    
    def getHyperplanes(self):
        return self.__hyperplanes
    
    def getDimension(self):
        return self.__dimension
    
    def contains(self, sample):
        is_contained= True
        for hyperplane in self.getHyperplanes():
            result = reduce(lambda x,y: x + y, map(lambda index: sample.getFeature(index) * hyperplane.getCoefficient(index), range(0,self.__dimension)))
            is_contained = is_contained and (result <= hyperplane.getIntercept())

        return is_contained
    
    
    
    
    
    
    
    
    
    
    
    
    
        