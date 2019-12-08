'''
Created on 3 dic. 2019

@author: javier
'''

class Sample(object):
    '''
    Esta clase representa una muestra para el metodo CRIO
    '''


    def __init__(self,d):
        '''
        Una muestra contiene una tupla de datos de tipo double
        '''
        self.__data = d
    
    def getDimension(self):
        return len(self.__data)
    
    def getData(self):
        return self.__data
    
    def getFeature(self,index):
        return self.__data[index]
    

    