'''
Created on 3 dic. 2019

@author: javier
'''
from __builtin__ import isinstance

class Sample(object):
    '''
    Esta clase representa una muestra para el metodo CRIO
    '''


    def __init__(self,d):
        '''
        Una muestra contiene una tupla de datos de tipo double
        '''
        self.__data = d
    
    def __str__(self, *args, **kwargs):
        return str(self.__data)
    def __eq__(self,obj):
        return isinstance(Sample) and self.__data == obj.getData()
        
    def getDimension(self):
        return len(self.__data)
    
    def getData(self):
        return self.__data
    
    def getFeature(self,index):
        return self.__data[index]
    

    