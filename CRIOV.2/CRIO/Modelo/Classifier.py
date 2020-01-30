'''
Created on 30 dic. 2019

@author: javier
'''
from CRIO.Clustering import createClusters
from CRIO.Grouping import createGroups
from CRIO.Regionalization import createRegions
from CRIO.Modelo.SampleContainer import SampleContainer
import CRIO.Importer as Importer

class Classifier(object):
    '''
    Esta clase se ocupa de determinar si una muestra pertenece a una de dos clases
    '''
    def __init__(self, c0,c1,t0,t1,d,k):
        '''
        Un Classifier se compone de 
        '''
        self.regions = []
        self.__dimension = d
        self.__num_groups = k
        self.__class1 = c1
        self.__class0 = c0
        self.__tag0 = t0
        self.__tag1 = t1
    
    def train(self):
        
        print("clustering...")
        clusters0 = createClusters(self.__class0,self.__class1)
        clusters1 = createClusters(self.__class1,self.__class0)
        print("grouping...")
        (groups,clusters) = createGroups(clusters0,clusters1,self.__num_groups)
        print("regionalizing...")
        regions = createRegions(groups, clusters)         
        self.regions = regions       
    
    
    def classify(self, sample):        
        
        for r in self.regions:
            if r.contains(sample):
                return self.__tag1
        
        return self.__tag0
            
            
        
    
    def export(self, route,d):
        f = open(route,"w")
        THREE_ITEMS_FORMAT = "%s,%s,%s\n"
        for r in self.regions:
            hiperplanes = r.getHyperplanes()
            for h in hiperplanes:
                data = map(lambda index: h.getCoefficient(index), range(0,d))
                data.append(h.getIntercept())
                f.write(THREE_ITEMS_FORMAT % tuple(data))
        f.close()
        
    def exportRegion(self,route,d,region):
        f = open(route,"w")
        THREE_ITEMS_FORMAT = "%s,%s,%s\n"
       
        for h in region.getHyperplanes():
            data = map(lambda index: h.getCoefficient(index), range(0,d))
            data.append(h.getIntercept())
            f.write(THREE_ITEMS_FORMAT % tuple(data))
        f.close()
        
        
        

   

def main():
    d = 2
    k = 1
    #c0 = SampleContainer([(-0.1663, -0.208), (-1.4265, 1.2276), (-0.7036, 1.0372), (0.2668, -1.6665), (0.2529, -1.9605)],d)
    #c1 = SampleContainer([(5.8384, 0.1114), (6.1911, -0.2508), (6.8148, -0.6143), (5.8302, -1.8956), (7.2234, 1.8256)], d)
    c0,c1 = Importer.readSamples("/home/javier/Documentos/Repositorios Git/Tesis-Classification/INPUT/SVM/R2/t1-ConjuntosDisjuntos.csv", d)
    
    
    t0 = "rojo"
    t1 = "azul"
    clasifier = Classifier(c0,c1,t0,t1,d,k)
    clasifier.train()
    
   
    
    clasifier.export("/home/javier/Documents/LiClipse Workspace/Ploteo/TEST/solution", d)


    


    
    
    
    
    
    