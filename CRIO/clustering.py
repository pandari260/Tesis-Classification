import math
import scipInterface as scip

routeClassA= "model/claseA.dat"
routeClassB= "model/claseB.dat"
routeParams = "model/parametrosSeparable"
routeModel ="model/clustering.zpl"


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

# toma dos puntos y retorna la 
def distanciaEntrePuntos(a,b):
    sum = 0
    for i in range(0,len(a)):
        sum = sum + (a[i] - b[i])**2
    return math.sqrt(sum)

#toma dos clusters y retorna la distancia entre los puntos mas cercanos entre ellos
def distanciaEntreClusters(clA, clB):
    d = 0
    for pA in clA:
        for pB in clB:
            aux = distanciaEntrePuntos(pA,pB)
            if aux > d:
                d = aux
    return d

#toma una lista de clusters y retorna una matriz de distancia entre ellos
def crearMatrizDistancia(clusters):
    tam = len(clusters)
    matrizDist = []
    for clA in range(0, tam):
        distancias = []
        for clB in range(clA,tam):
            dAB = 0
            if clA !=clB:
                dAB = distanciaEntreClusters(clusters[clA], clusters[clB]) 
            distancias.append(dAB)
        matrizDist.append(distancias)
    return matrizDist

#toma dos clusters y los combina    
def mergeClusters(clusterA,clusterB):
    c = []
    for p in clusterA:
        c.append(p)
    for p in clusterB:
        c.append(p)
    return c

#mover a manejor de muestras#############################################
def escribirClusterToSamples(ruta, cluster):
    tam = len(cluster)
    tam_p = len(cluster[0])
    f = open(ruta, "w")
    for p in range(0,tam):
        for n in range(0,tam_p):
            f.write(str(p) + "," + str(n) + "," + str(cluster[p][n])+ "\n")
    f.close()

#mover a manejo de archivos##########################
def escribirParametros(ruta, parametros):
    f = open(ruta,"w")
    for p in parametros:
        f.write(str(p)+ "\n")
    f.close()

#determina si dos cluster de Clase A son linealmente separables respecto de la Clase B
def contieneOutlier(Cr, Cs, claseB):
    
    escribirClusterToSamples(routeClassA, mergeClusters(Cr,Cs))
    escribirClusterToSamples(routeClassB, claseB)
    parametros = [len(claseB), (len(Cr) + len(Cs))]
    escribirParametros(routeParams, parametros)
    model = scip.solveProblem(routeModel)
    ret = model.getObjVal()
    if ret != 0:
        ret = 1
    return ret
   

#clusterea el conjunto de muestras de clase A
def crearClusters(cA, cB):#crea clusters para las muestras de cA de clase A    
    c = claseToCluster(cA)
    K = len(c)
    k = 0
    while k < K:
        matDist = crearMatrizDistancia(c)
        r,s = minimaDistancia(matDist)
        if contieneOutlier(c[r],c[s],cB) == 0:
            k = k + 1
        else:
            c.append(mergeClusters(c[r],c[s]))

            if r > s:
                c.pop(s)
                c.pop(r-1)
            else:
                c.pop(r)
                c.pop(s-1)

            K = K - 1
            k = 0
        k = k + 1
    return c

#recibe una lista de clusters y lo escribe en un archivo interpretable por zimpl 
def escribirClusters(ruta, clusters, muestras):
    tam_muestras = len(muestras)
    tam_cluster = len(clusters)
    f = open(ruta, "w")
    for p in range(0, tam_muestras):
        for c in range(0, tam_cluster):
            if muestras[p] in clusters[c]:
                f.write(str(p) + "," +str(c) + "\n" )
    f.close()

#transforma un lista de muestras en una lista de clusters, un cluster por muestra
def claseToCluster(clase):
    cluster = []
    for p in clase:
        l = []
        l.append(p)
        cluster.append(l)
    return  cluster

    


        


