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
    
    def export(self, route,d):
        f = open(route,"w")
        THREE_ITEMS_FORMAT = "%s,%s,%s\n"
        for r in self.__regions:
            hiperplanes = r.getHyperplanes()
            for h in hiperplanes:
                data = map(lambda index: h.getCoefficient(index), range(0,d))
                data.append(h.getIntercept())
            f.write(THREE_ITEMS_FORMAT % tuple(data))
        f.close()
        
        pass

def train(class0,class1,dimension,num_groups):
    
    clusters0 = createClusters(class0,class1,dimension)
    clusters1 = createClusters(class1,class0,dimension)
    groups1 = createGroups(clusters0,clusters1,num_groups)
    regions = createRegions(groups1,clusters0) 
    return regions


def createClusters(classA,classB):
    pass

def createGroups(clusters0,clusters1,num_groups):
    pass

def createRegions(groups1,clusters0):
    pass 
    
    
    
    
    
    
    
    
    
    
    
    
    