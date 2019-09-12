import math
import scipInterface as scip
from fileManager import writeSample, writeParameters

routeClassA= "model/clusteringClassA.dat"
routeClassB= "model/clusteringClassB.dat"
routeParams = "model/clusteringParameters"
routeModel ="model/clustering.zpl"

class ClusterContainer():
    
    def __init__(self, cA,cB):
        self.clusters = defineClusters(cA,cB)
        self.clustersForSamples = invertDic(self.clusters)
        self.cantClusters = len(self.clusters)

    def getClusters(self):
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
    K = len(clusters)
    k = 0
    while k < K:
        matDist = crearMatrizDistancia(clusters)
        
        r,s = minimaDistancia(matDist)

        if contieneOutlier(clusters[r],clusters[s],cB) == 0:
            k = k + 1
            print("\n\nclusters: " + str(clusters) + "-------------------------------------------\n\n") 
            print("r: " + str(r) + ", s: " + str(s) + "------------------------------------------------\n\n")
            print("Matriz: ---------------------------------------------------------------------------\n\n")
            for row in matDist:
                print(str(row) + "\n\n")  
        else:
            newCluster = mergeClusters(clusters[r],clusters[s])            
            print("\n\nclusters antes: " + str(clusters) + "-------------------------------------------\n\n") 
            print("Matriz: ---------------------------------------------------------------------------\n\n")
            for row in matDist:
                print(str(row) + "\n\n")  
            print("r: " + str(r) + ", s: " + str(s) + "------------------------------------------------\n\n")
            if r > s:
                clusters.pop(r)
                clusters.pop(s)
            else:
                clusters.pop(s)
                clusters.pop(r)

            clusters.append(newCluster)
            
            
            print("clusters despues: " + str(clusters) + "---------------------------------------------------------\n\n")         

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
    tam = len(clusters)
    matrizDist = []
    for clA in range(0, tam):
        distancias = []
        for clB in range(0,tam):
            dAB = 0
            if clA !=clB:
                dAB = distanciaEntreClusters(clusters[clA], clusters[clB]) 
            distancias.append(dAB)
        matrizDist.append(distancias)
    return matrizDist

#toma dos clusters y retorna la distancia entre los puntos mas cercanos entre ellos
def distanciaEntreClusters(clA, clB):
    d = 0
    for pA in clA:
        for pB in clB:
            aux = distanciaEntrePuntos(pA,pB)
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
    parameters = [len(claseB), (len(Cr) + len(Cs))]

    writeParameters(parameters, routeParams)
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


def main():
    print(distanciaEntreClusters([(6,7)], [(8,9)]))

main()