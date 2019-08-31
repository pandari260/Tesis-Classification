import math
import scipInterface as scip
from muestras import writeSample, writeParams

routeClassA= "model/claseA.dat"
routeClassB= "model/claseB.dat"
routeParams = "model/parametrosSeparable"
routeModel ="model/clustering.zpl"

class ClusterContainer():
    
    def __init__(self, cA,cB):
        self.clusters = defineClusters(cA,cB)
        self.clustersForSamples = invertDic(self.clusters)
        self.cantClusters = len(self.clusters)

    def getCluster(self):
        return self.clusters
    
    def getCantClusters(self):
        return self.cantClusters
    
    def getSampleKey(self, sample):
        return self.clustersForSamples[sample]
        

def invertDic(cluster):
    ret = dict()
    for i in range(0, len(cluster)):
        for sample in cluster[i]:
            ret[sample] = i
    return ret

def defineClusters(cA,cB):
    clusters = creatDefaultCluster(cA)
    print(clusters)
    K = len(clusters)
    k = 0
    while k < K:
        matDist = crearMatrizDistancia(clusters)
        
        r,s = minimaDistancia(matDist)

        if contieneOutlier(clusters[r],clusters[s],cB) == 0:
            k = k + 1
        else:
            newCluster = mergeClusters(clusters[r],clusters[s])
            
            if r > s:
                clusters.pop(r)
                clusters.pop(s)
            else:
                clusters.pop(s)
                clusters.pop(r)

            clusters.append(newCluster)
            print("Matriz: " + str(matDist))           

            K = K - 1
            k = 0
        k = k + 1
    return clusters

def indexKeys(clusters):
    ret = dict()
    index = 0
    for key, value in clusters.items():
        ret[index] = value
        index = index + 1
    return ret


def creatDefaultCluster(c):
    clusters = []
    tam = len(c)
    for i in range(0,tam):
        clusters.append([c[i]])
    return clusters

#toma una lista de clusters y retorna una matriz de distancia entre ellos
def crearMatrizDistancia(clusters):
    matrizDist = []
    for keyA in clusters.keys():
        distancias = []
        for keyB in clusters.keys():
            dAB = 0
            if keyA !=keyB:
                dAB = distanciaEntreClusters(clusters[keyA], clusters[keyB]) 
            distancias.append(dAB)
        matrizDist.append(distancias)
    return matrizDist

#toma dos clusters y retorna la distancia entre los puntos mas cercanos entre ellos
def distanciaEntreClusters(clusterA, clusterB):
    d = 0
    for pA in clusterA:
        for pB in clusterA:
            aux = distanciaEntrePuntos(pA[pA.keys()[0]],pB[pB.keys()[0]])
            if aux > d:
                d = aux
    return d

# toma dos puntos y retorna la 
def distanciaEntrePuntos(a,b):
    sum = 0
    for i in range(0,len(a)):
        sum = sum + (a[i] - b[i])**2
    return math.sqrt(sum)

#toma una matria de distancias y retorna las coordenadas del menor valor de la matriz
def minimaDistancia(matriz):
    tam = len(matriz)
    minF, minC = 0,0#minima fila y minima columna
    min = float("inf")

    for r in range(0,tam):
        for s in range(0,(tam-r)):
            n = matriz[r][s]
            if n != 0 and n < min:
                min = n
                minF = r
                minC = s
    return minF,minC

#determina si dos cluster de Clase A son linealmente separables respecto de la Clase B
def contieneOutlier(Cr, Cs, claseB):
    
    writeSample( mergeClusters(Cr,Cs),routeClassA)
    writeSample(claseB, routeClassB)
    params = [len(claseB), (len(Cr) + len(Cs))]

    writeParams(params, routeParams)
    model = scip.solveProblem(routeModel)
    ret = model.getObjVal()
    if ret != 0:
        ret = 1
    return ret

#toma dos clusters y los combina    
def mergeClusters(clusterA,clusterB):
    c = []
    for p in clusterA:
        c.append(p)
    for p in clusterB:
        c.append(p)
    return c

