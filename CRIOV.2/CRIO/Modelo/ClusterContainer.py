'''
Created on 11 dic. 2019

@author: javier
'''
from CRIO.Modelo.SampleContainer import SampleContainer

class ClusterContainer(object):
    '''
    esta clase sirve para contener y brindar acceso a un conjunto de clusters
    '''


    def __init__(self, c,d):
        '''
        un clusterContainer contiene un conjunto de clusters y una dimension
        '''
        self.__clusters = set(c)
        self.__dimension = d
    
    def getClusters(self):
        return self.__clusters
    
    def getDimension(self):
        return self.__dimension
    
    def getSamples(self):
        ret = set()
        for c in self.getClusters():
            ret = ret | c.getSamples()
        return SampleContainer(ret,self.getDimension())
    
    def getSize(self):
        return len(self.__clusters)
    
    def remove(self,c):
        self.__clusters.remove(c)
    
    def add(self,c):
        self.__clusters.add(c)
        
            
    
            
            
            
            
            
            
            
            
            
            
            
            