'''
Created on 30 dic. 2019

@author: javier
'''
from CRIO.Clustering import createClusters
from CRIO.Grouping import createGroups
from CRIO.Regionalization import createRegions
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer


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
        self.__displace_sample = createDisplaceSample(SampleContainer(self.__class0.getSamples().union(self.__class1.getSamples()),d), self.__dimension)
    
    def train(self,creteClustersMethod=createClusters):
        
        
        print("desplazando muestras...")
        displaced_class0 = displace(self.__class0, self.__displace_sample)
        displaced_class1 = displace(self.__class1, self.__displace_sample)

        print("clustering...")
        clusters0 = creteClustersMethod(displaced_class0,displaced_class1)
        clusters1 = creteClustersMethod(displaced_class1,displaced_class0)
        print("cluster0")
        displayClusterContainer(clusters0)
        print("cluster1")
        displayClusterContainer(clusters1)
        
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
        
    def getDisplaceSample(self):
        return self.__displace_sample
    
    
    """Ariel: mover esto a otro lado"""    
    def __rowConfuseMatrix(self, clasifier, sample, color):
        r1, r2 = 0, 0
        for i in sample:  
            if(clasifier.classify(Sample(i)).__eq__(color)):  r1+=1 
            else: r2+=1
        return r1, r2
        
    def generateConfuseMatrix(self, clasifier, sampleC0, sampleC1, t0, t1):
        TP, FP = self.__rowConfuseMatrix(clasifier, sampleC0, t0)
        TN, FN = self.__rowConfuseMatrix(clasifier, sampleC1, t1)  
        return float(TP), float(FP), float(TN), float(FN)
    """----------------------------------------------------------------------"""

    
def displayClusterContainer(c):
    for cls in c.getClusters():
        print(map(lambda s: s.getData(), cls.getSamples()))
   
def createDisplaceSample(samples,d):
    
    def minValuesSample(a,b):
        s = []
        for f in range(0,d):
            if a.getFeature(f) > b.getFeature(f):
                s.append(b.getFeature(f))
            else:
                s.append(a.getFeature(f))
        return tuple(s)
    
    minValues = reduce(lambda a,b: Sample(minValuesSample(a, b)), samples.getSamples())
    return Sample(tuple(map(lambda n: abs(minValues.getFeature(n)), range(d))))
    
    
def displace(samples, scrollSample):
    d = samples.getDimension()
    def sampleSum(s1,s2):
        return Sample(tuple(map(lambda i:s1.getFeature(i) + s2.getFeature(i) , range(d))))
        
    return SampleContainer(map(lambda spl: sampleSum(spl,scrollSample) , samples.getSamples()),d)
 
    
    
    
