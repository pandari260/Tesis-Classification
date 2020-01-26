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
        self.__groups = set([])

    
    def addSamples(self, key, value):
        if key in self.__dictionary.keys():
            self.__dictionary[key] = Group(self.__dictionary[key].getSamples() | value, self.__dimension)
        else:
            self.__dictionary[key] = Group(value, self.__dimension)
        
        self.__groups = set(self.__dictionary.values())
    
    def __eq__(self,obj):
        return isinstance(obj,GroupContainer) and compareSets(self.__groups, obj.getGroups()) and self.__dimension == obj.getDimension()
    
    def getGroups(self):
        return self.__groups
    def getDimension(self):
        return self.__dimension
    
def compareSets(a,b):
    l1 = list(a)
    l2 = list(b)
    
      
    
    return all(elem in l1  for elem in l2) and all(elem in l2  for elem in l1)

        