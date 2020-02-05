'''
Created on 30 dic. 2019

@author: javier
'''
from CRIO.Clustering import createClusters
from CRIO.Grouping import createGroups
from CRIO.Regionalization import createRegions
from CRIO.Modelo.SampleContainer import SampleContainer
import CRIO.Importer as Importer
import Sample
import MetricsClassifier as Metrics
import numpy as np
from operator import ge


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
        
    def __rowConfuseMatrix(self, clasifier, sample, color):
        r1, r2 = 0, 0
        for i in sample:  
            if(clasifier.classify(Sample.Sample(i)).__eq__(color)):  r1+=1 
            else: r2+=1
        return r1, r2
        
    def generateConfuseMatrix(self, clasifier, sampleC0, sampleC1, t0, t1):
        TP, FP = self.__rowConfuseMatrix(clasifier, sampleC0, t0)
        TN, FN = self.__rowConfuseMatrix(clasifier, sampleC1, t1)  
        return float(TP), float(FP), float(TN), float(FN)
            

def main():
    
    d = 2
    k = 1
    
    c0,c1 = Importer.readSample("/home/pandari/Escritorio/Tesis-Classification/Resources/R2/t1-ConjuntosDisjuntos.csv")

    for k in c0:
        print (k)    
        
    c0 = SampleContainer(c0,d)
    c1 = SampleContainer(c1,d)
    
    sampleC0 = [(-0.1663, -0.208), (-1.4265, 1.2276), (6.8148, -0.6143), (-0.7036, 1.0372), (0.2668, -1.6665), (0.2529, -1.9605)]
    sampleC1 = [(-0.1663, -0.208), (-1.4265, 1.2276), (-0.7036, 1.0372), (0.2668, -1.6665), (0.2529, -1.9605)]
    
    t0 = "rojo"
    t1 = "azul"
    clasifier = Classifier(c0,c1,t0,t1,d,k)
    clasifier.train()
    
    TP, FP, TN, FN = clasifier.generateConfuseMatrix(clasifier, sampleC0, sampleC1, t0, t1)
    metC0 = Metrics.MetricsClassifier(0, TP, FP, TN, FN)
    metC1 = Metrics.MetricsClassifier(1, FN, TN, FP, TP)
    
    TITLE_CASETEST ="Titulo del testsss"
    ACCURACY = "\nAccuracy: {}\n"
    CONFUSE_MATRIX = "Matrix Confuse:\n|{}, {}|\n|{}, {}|\n"
    HEADER_METRIC = "Report:\n\tClass\tPresicion\tRecall\t\tF1-Score\tSupport\n"
    
    print (TITLE_CASETEST)
    print (ACCURACY.format(metC0.getAccuracy()))    
    print (CONFUSE_MATRIX.format(int(TP), int(FP), int(TN), int(FN)))
    print (HEADER_METRIC)
    print (metC0.showMetrics())
    print (metC1.showMetrics())

   
main()
    
    
    
    
    
    