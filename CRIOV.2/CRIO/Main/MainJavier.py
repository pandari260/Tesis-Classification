'''
Created on 8 feb. 2020

@author: javier
'''

import numpy as np
import CRIO.Importer as Importer
from CRIO.Modelo.Classifier import Classifier
from CRIO.Clustering import createClusters,createClusters2
import matplotlib.pyplot as plt
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
    k = 5
   
    c0,c1 = Importer.readSample("/home/javier/Documentos/Repositorios Git/Tesis-Classification/Resources/R2/t6-EncerradoSolapado.csv")
    
    class0 = SampleContainer(c0,d)
    class1 = SampleContainer(c1,d)
    t0 = "rojo"
    t1 = "azul"
    clasifier = Classifier(class0,class1,t0,t1,d,k)
    start = time()
    clasifier.train(creteClustersMethod=createClusters2)
    finish = time() - start

   
    
    clasifier.export("/home/javier/Documents/LiClipse Workspace/Ploteo/TEST/solution", d)
    clasifier.exportRegion("/home/javier/Documents/LiClipse Workspace/Ploteo/TEST/solutionPrimeraRegion", d, clasifier.regions.pop())

    
    print("vector de desplazamiento: " + str(clasifier.getDisplaceSample().getData()))
    print("DONE")
    print("tiempo transcurrido: " + str(finish))
    alarma()
    
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
    