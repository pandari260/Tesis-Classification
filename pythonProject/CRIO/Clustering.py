from CRIO import ScipInterface as scip
from CRIO.Exporter import writeSample, writeParameters
from gtk.keysyms import exclamdown
from sympy.physics.quantum.tests.test_qapply import po
from ErrorMessages import *
from CRIO.Importer import readSamples

routeClassA = "model/clusteringClassA.dat"
routeClassB = "model/clusteringClassB.dat"
routeParams = "model/clusteringParameters"
routeModel = "model/clustering.zpl"

import numpy as np


class ClusterContainer():
    
    def __init__(self, classA, classB):
        self.clusters = defineClusters(classA, classB)
        self.clustersForSamples = sampleKeyDict(self.clusters)
        self.cantClusters = len(self.clusters)

    def getClusters(self):
        return self.clusters
    
    def getCantClusters(self):
        return self.cantClusters
    
    def getSampleKey(self, sample):
        return self.clustersForSamples[sample]
    
    def removeSample(self, sample):
        self.clusters[self.getSampleKey(sample)].remove(sample)
        

# toma una matriz no vacia y la transforma en un diccionario cuyas claves son los elementos de la matriz y 
# los valores el indice correspondiente a cada lista
def sampleKeyDict(matrix):
    
    try:
        size = len(matrix)
        if size == 0:
            print(EMPTY_MATRIX_ERROR_MESSAGE)
            return None
    
        ret = dict()
        for i in range(0, size):
            row = matrix[i]
            
            if len(row) == 0:
                print(EMPTY_CLUSTER_ERROR_MESSAGE)
                return None
            
            for sample in row:
                ret[sample] = i
        return ret
    except TypeError: 
        print(NOT_MATRIX_ERROR_MESSAGE)
        return None
    

# crea cluster con las muestras de clase A que no contienen muestras de clase B
def defineClusters(classA, classB):
    
    if len(classA) == 1:
        return [classA]
    else:
        clusters = creatDefaultCluster(classA)
        K = len(clusters)
        k = 0
        while k < K:
            matDist = crearMatrizDistancia(clusters)        
            r, s = minimaDistancia(matDist)
            if contieneOutlier(clusters[r], clusters[s], classB) == 0:
                k = k + 1            
            else:
                newCluster = clusters[s] + clusters[r]
                clusters.append(newCluster)   
                clusters.remove(clusters[r])    
                clusters.remove(clusters[s])              
                
                print("\n\n\n\n\n\n\n\n\n\n nuevo cluster" + str(newCluster))
                print("todos los clueter: " + str(clusters) + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

                K = K - 1
                k = 0
            k = k + 1
        return clusters


def creatDefaultCluster(c):
    return list(map(lambda sample: [sample], c))


# toma una lista de clusters y retorna una matriz de distancia entre ellos
def crearMatrizDistancia(clusters):
    tam = len(clusters)
    matrizDist = []
    for clusterA in range(0, tam):
        distancias = []
        for clusterB in range(0, clusterA):
            distanceAB = distanceBtwClusters(clusters[clusterA], clusters[clusterB]) 
            distancias.append(distanceAB)
        matrizDist.append(distancias)
    return matrizDist

# toma dos clusters y retorna la distancia entre los puntos mas cercanos entre ellos


def distanceBtwClusters(clusterA, clusterB):
    return distanceBtwSamples(np.mean(clusterA, 0), np.mean(clusterB, 0))
# toma dos puntos y retorna la distancia entre ellos


def distanceBtwSamples(sampleA, sampleB):
    return np.linalg.norm(list(map(lambda x: x[0] - x[1], list(zip(sampleA, sampleB)))))


# toma una matria de distancias y retorna las coordenadas del menor valor de la matriz
def minimaDistancia(matriz):
    tam = len(matriz)
    minF, minC = -1, -1  # minima fila y minima columna
    min = float("inf")

    for r in range(0, tam):
        for s in range(0, r):
            n = matriz[r][s]
            if n != 0 and n < min:
                min = n
                minF = r
                minC = s
    return minF, minC


# determina si dos cluster de Clase A son linealmente separables respecto de la Clase B
def contieneOutlier(Cr, Cs, claseB):
    
    writeSample(Cr + Cs, routeClassA)
    writeSample(claseB, routeClassB)
    parameters = [len(claseB), (len(Cr) + len(Cs)), len(claseB[0])]

    writeParameters(parameters, routeParams)
    model = scip.solveProblem(routeModel)
    ret = model.getObjVal()
    if ret != 0:
        ret = 1
    return ret

