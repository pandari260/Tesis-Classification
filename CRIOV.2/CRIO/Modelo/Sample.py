'''
Created on 3 dic. 2019

@author: javier
'''

class Sample(object):
    '''
    Esta clase representa una muestra para el metodo CRIO
    '''


    def __init__(self, dim,d):
        '''
        Una muestra contiene una dimension y una tupla de datos de tipo double
        '''
        self.__dimention = dim
        self.__data = d
    
    def getDimention(self):
        return self.__dimention
    
    def getData(self):
        return self.__data
    
    def getFeature(self,index):
        return self.__data(index)