import clusteringV2 as Clusterer
from pyscipopt import Model
import grouper as Grouper
import muestras as Muestras
import hiperplaneDefiner as Hiperplane



#TO DO: parametrizar estos parametros
routeClase0 = "model/clase0.dat"
routeClase1 = "model/clase1.dat"
routeCluster0 = "model/cluster0.dat"
routeCluster1 = "model/cluster1.dat"
routeParameters = "model/parametros"
routeGroups = "model/grupos"
dimenssion = 2
k = 2



def trainClasificator():
    print("escribiendo parametros...")
    #writeParameters()

    print("Leyendo muestras...")
    class0 = Muestras.leerMuestras(routeClase0, dimenssion)
    class1 = Muestras.leerMuestras(routeClase1, dimenssion)

    print("Creando clusters...")
    cluster0 = Clusterer.crearClusters(class0,class1)
    cluster1 = Clusterer.crearClusters(class1,class0)
    

    print("Escribiendo clusters...")
    Muestras.escribirClusters(routeCluster0, cluster0, class0)
    Muestras.escribirClusters(routeCluster1, cluster1, class1)

    print("Asignando clusters a grupos...")
    groups = Grouper.assingGroups(cluster1, k)
    print("cluster 0: " + str(cluster0))
    print("cluster 1: " + str(cluster1))

    print groups

    print("Definiendo hiperplanos...")
    Hiperplane.defineHiperplanes(groups, cluster0)






def main():
    trainClasificator()

main()
    