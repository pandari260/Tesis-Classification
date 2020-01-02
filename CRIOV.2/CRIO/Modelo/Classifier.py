'''
Created on 30 dic. 2019

@author: javier
'''

class Classifier(object):
    '''
    Esta clase se ocupa de determinar si una muestra pertenece a una de dos clases
    '''
    def __init__(self, c0,c1,t0,t1,d,k):
        '''
        Un Classifier se compone de 
        '''
        self.__regions = train(c0,c1,d,k)
        self.__dimension = d
        self.__num_groups = k
        self.__tag0= t0
        self.__tag1 = t1
    
    def classify(self, sample):
        pass

def train(class0,class1,dimension,num_groups):
    
    clusters0 = createClusters(class0,class1,dimension)
    clusters1 = createClusters(class1,class0,dimension)
    groups1 = createGroups(clusters0,clusters1,num_groups)
    regions = createRegions(groups1,clusters0) 
    return regions

def createClusters(classA,classB):
    pass

def createGroups(clusters0,clusters1):
    pass

def createRegions(groups1,clusters0):
    pass 
    
    
    
    
    
    
    
    
    
    
    
    
    