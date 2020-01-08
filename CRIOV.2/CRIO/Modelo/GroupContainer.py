'''
Created on 17 dic. 2019

@author: javier
'''
from CRIO.Modelo.SampleContainer import SampleContainer
from CRIO.Modelo.Group import Group

class GroupContainer(object):
    '''
    Clase que da acceso a un conjunto de grupos de muestras
    '''


    def __init__(self, d):
        '''
        Un GroupContainer contiene un conjunto de grupos de muestras y la dimension de dichas muestras
        '''
        self.__dictionary = {}
        self.__dimension = d
        self.__groups = {}
    
    def addSamples(self, key, value):
        if key in self.__dictionary.keys():
            self.__dictionary[key] = Group(self.__dictionary[key].getSamples() + value, self.__dimension)
        else:
            self.__dictionary[key] = Group(value, self.__dimension)
        
        self.__groups = set(self.__dictionary.values())
    
    def getGroups(self):
        return self.__groups
        