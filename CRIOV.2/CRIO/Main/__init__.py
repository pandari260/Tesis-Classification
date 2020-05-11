

from CRIO.Clustering import createClusters, createClusters2
from CRIO.Grouping import createGroups
from CRIO.Regionalization import createRegions
from CRIO.Modelo.SampleContainer import SampleContainer
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.MetricsClassifier import MetricsClassifier
from CRIO.Modelo.Classifier import Classifier
import CRIO.Importer as Importer
import numpy as np
from operator import ge
from CRIO.Modelo import ConfuseMatrix
from sympy.diffgeom.tests.test_diffgeom import TP
from mpmath import fp

#Ubicar este metodo - Dado una lista la separa segun el porcentaje recibido por parametro
def divideProportionally(lines, porc):
    p = int(len(lines)*porc)
    return lines[:p], lines[p:]
#--------------------------------------------------------------------

def main():
    
    d = 2
    k = 1
    
    c0,c1 = Importer.readSample("/home/javier/Documentos/Repositorios Git/Tesis-Classification/Resources/R2/t7-DiagonalIntercalada.csv")   
    split_samples_0 = map(lambda cluster: divideProportionally(cluster, 0.7),c0)
    split_samples_1 = map(lambda cluster: divideProportionally(cluster, 0.7),c1)  
    
    
    train0 = [item for sublist in map(lambda s: s[0], split_samples_0) for item in sublist] 
    test0 = [item for sublist in map(lambda s: s[1], split_samples_0) for item in sublist] 
    train1 = [item for sublist in map(lambda s: s[0], split_samples_1) for item in sublist] 
    test1 = [item for sublist in map(lambda s: s[1], split_samples_1) for item in sublist] 
    
    train0 = SampleContainer(train0,d)
    train1 = SampleContainer(train1,d)
    t0 = "rojo"
    t1 = "azul"
    
    clasifier = Classifier(train0,train1,t0,t1,d,k)
    clasifier.train(createClustersMethod=createClusters)
    
    TP, FP, TN, FN = ConfuseMatrix.generateConfuseMatrix(clasifier, test0, test1, t0, t1)
   

    metC0 = MetricsClassifier(0, TP, FP, FN, TN)
    metC1 = MetricsClassifier(1, TN, FN, FP, TP)
    
    TITLE_CASETEST ="Titulo del testsss"
    ACCURACY = "\nAccuracy: {}\n"
    CONFUSE_MATRIX = "Matrix Confuse:\n|{}, {}|\n|{}, {}|\n"
    HEADER_METRIC = "Report:\n\tClass\tPresicion\tRecall\t\tF1-Score\tSupport\n"
            
    print (TITLE_CASETEST)
    print (ACCURACY.format(metC0.getAccuracy()))    
    print (CONFUSE_MATRIX.format(int(TP), int(FP), int(FN), int(TN)))
    print (HEADER_METRIC)
    print (metC0.showMetrics())
    print (metC1.showMetrics())
    
    clasifier.export("/home/javier/Documents/LiClipse Workspace/Ploteo/TEST/solution", d)
    clasifier.exportRegion("/home/javier/Documents/LiClipse Workspace/Ploteo/TEST/solutionPrimeraRegion", d, clasifier.regions.pop())

    
    print("vector de desplazamiento: " + str(clasifier.getDisplaceSample().getData()))
    print("DONE")
    

   
main()