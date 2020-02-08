'''
Created on 30 dic. 2019

@author: javier
'''
from CRIO.Clustering import createClusters,createClusters2
from CRIO.Grouping import createGroups
from CRIO.Regionalization import createRegions
from CRIO.Modelo.SampleContainer import SampleContainer
import CRIO.Importer as Importer
import Sample
import MetricsClassifier as Metrics
import numpy as np
import matplotlib.pyplot as plt  


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
    
    def train(self,creteClustersMethod=createClusters):
        
        print("clustering...")
        clusters0 = creteClustersMethod(self.__class0,self.__class1)
        #displayClusterContainer(clusters0)
        graphClusters(self.__class0,self.__class1,clusters0)
        clusters1 = creteClustersMethod(self.__class1,self.__class0)
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

def displayClusterContainer(c):
    for cls in c.getClusters():
        print(map(lambda s: s.getData(), cls.getSamples()))

def maindeAriel():
    
    
    
    
    TP, FP, TN, FN = clasifier.generateConfuseMatrix(clasifier, sampleC0, sampleC1, t0, t1)
    metC0 = Metrics.MetricsClassifier(0, TP, FP, TN, FN)
    metC1 = Metrics.MetricsClassifier(1, FN, TN, FP, TP)
    
    print ("Titulo del testsss")
    print ("\nAccuracy: {}\n".format(metC0.getAccuracy()))    
    print ("Matrix Confuse:\n|{}, {}|\n|{}, {}|\n".format(int(TP), int(FP), int(TN), int(FN)))
    print ("Report:\n\tClass\tPresicion\tRecall\t\tF1-Score\tSupport\n")
    metC0.showMetrics()
    metC1.showMetrics()
    
def mainDeJavier():
    
    d = 2
    k = 2
   
    c0,c1 = Importer.readSamples("/home/javier/Documentos/Repositorios Git/Tesis-Classification/Resources/R2/t2-ConjuntosSolapados-200.csv", d)
    
    
    t0 = "rojo"
    t1 = "azul"
    clasifier = Classifier(c0,c1,t0,t1,d,k)
    clasifier.train(creteClustersMethod=createClusters2)
    
   
    
    clasifier.export("/home/javier/Documents/LiClipse Workspace/Ploteo/TEST/solution", d)
    clasifier.export("/home/javier/Documents/LiClipse Workspace/Ploteo3/TEST/solution", d)
    print("DONE")
    
def graphClusters(sampleC0,sampleC1, clusters):
    
    graphSample(sampleC0, sampleC1)
    graphCircles(clusters)
    plt.show()

def graphCircles(clusters):
    
    def centerCluster(cluster):
        return np.mean(map(lambda spl: spl.getData(), cluster.getSamples()),0)
    

    circles = []
    for c in clusters.getClusters():
        print(centerCluster(c))
        circles.append(plt.Circle(centerCluster(c), 0.75, color='black', fill=False))
    
    ax=plt.gca()
    
    
    
    plt.xlim(-3.0,6.25)
    plt.ylim(-3.25,6.25)    
    
    for c in circles:
        ax.add_patch(c)
    
    
    #plt.title('How to plot a circle with matplotlib ?', fontsize=8)
    
    #plt.savefig("plot_circle_matplotlib_02.png", bbox_inches='tight')
    
    #plt.show()
    
def graphSample(sampleC0, sampleC1):
    def __drawSample(sample, color):
        x, y = [], []
        area = np.pi*10.0
        for i in sample.getSamples():
            x.append(i.getFeature(0))
            y.append(i.getFeature(1))
        plt.scatter(x, y, s=area, c=color, alpha=1)
    __drawSample(sampleC0, 'red')
    __drawSample(sampleC1, 'blue')
    
mainDeJavier()

    


   
    
    
    
    
    
    