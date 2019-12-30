'''
Created on 29 dic. 2019

@author: javier
'''
from CRIO.Modelo.SampleContainer import SampleContainer

class Region(SampleContainer):
    '''
    esta clase representa una region para el metodo crio
    '''


    def __init__(self, s,h,d):
        '''
        una region se compone de un conjunto de muestras e hiperplanos
        '''
        super(Region,self).__init__(s,d)
        self.__hyperplanes = set(h)
    
    def getHyperplanes(self):
        return self.__hyperplanes
    
    
    
    
    
    
    
    
    
    
    
    
    
        