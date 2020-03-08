'''
Created on 8 feb. 2020

@author: javier
'''

import CRIO.Importer as Importer
from CRIO.Modelo.Classifier import Classifier
from CRIO.Clustering import createClusters,createClusters2
from CRIO.Modelo.SampleContainer import SampleContainer
from time import time
import os


def alarma():
    os.system('spd-say "yout program is finished"')
    
def displayClusterContainer(c):
    for cls in c.getClusters():
        print(map(lambda s: s.getData(), cls.getSamples()))


    
def mainDeJavier():
    
    d = 2
    k = 1
   
    c0,c1 = Importer.readSample("/home/javier/Documentos/Repositorios Git/Tesis-Classification/Resources/R2/t6-EncerradoSolapado.csv")
    
    class0 = SampleContainer(c0,d)
    class1 = SampleContainer(c1,d)
    t0 = "rojo"
    t1 = "azul"
    clasifier = Classifier(class1,class0,t1,t0,d,k)
    start = time()
    clasifier.train(creteClustersMethod=createClusters2)
    finish = time() - start

   
    
    clasifier.export("/home/javier/Documents/LiClipse Workspace/Ploteo/TEST/solution", d)
    clasifier.exportRegion("/home/javier/Documents/LiClipse Workspace/Ploteo/TEST/solutionPrimeraRegion", d, clasifier.regions.pop())

    
    print("vector de desplazamiento: " + str(clasifier.getDisplaceSample().getData()))
    print("DONE")
    print("tiempo transcurrido: " + str(finish))
    alarma()
    




mainDeJavier()
    