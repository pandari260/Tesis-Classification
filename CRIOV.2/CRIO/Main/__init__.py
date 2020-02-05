

from CRIO.Clustering import createClusters
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

#Ubicar este metodo - Dado una lista la separa segun el porcentaje recibido por parametro
def divideProportionally(lines, porc):
    p = int(len(lines)*porc)
    return lines[:p], lines[p:]
#--------------------------------------------------------------------

def main():
    
    d = 2
    k = 1
    
    c0,c1 = Importer.readSample("/home/pandari/Escritorio/Tesis-Classification/Resources/R2/t1-ConjuntosDisjuntos.csv")
  
    '''
    train0 = [(-0.1663, -0.208), (-1.4265, 1.2276), (6.8148, -0.6143), (-0.7036, 1.0372), (0.2668, -1.6665), (0.2529, -1.9605)]
    train1 = [(-0.1663, -0.208), (-1.4265, 1.2276), (-0.7036, 1.0372), (0.2668, -1.6665), (0.2529, -1.9605)]
    
    test0 = [(-0.1663, -0.208), (-1.4265, 1.2276), (6.8148, -0.6143), (-0.7036, 1.0372), (0.2668, -1.6665), (0.2529, -1.9605)]
    test1 = [(-0.1663, -0.208), (-1.4265, 1.2276), (-0.7036, 1.0372), (0.2668, -1.6665), (0.2529, -1.9605)]
    '''
    train0, test0 = divideProportionally(c0, 0.9)
    train1, test1 = divideProportionally(c1, 0.9)  
    
    print("train0 %d", len(train0))
    print("train1 %d", len(train1))
    print("test0 %d", len(test0))
    print("test1 %d", len(test1))
    
    train0 = SampleContainer(train0,d)
    train1 = SampleContainer(train1,d)
    t0 = "rojo"
    t1 = "azul"
    
    clasifier = Classifier(train0,train1,t0,t1,d,k)
    clasifier.train()
    
    TP, FP, TN, FN = ConfuseMatrix.generateConfuseMatrix(clasifier, test0, test1, t0, t1)
    metC0 = MetricsClassifier(0, TP, FP, TN, FN)
    metC1 = MetricsClassifier(1, FN, TN, FP, TP)
    
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