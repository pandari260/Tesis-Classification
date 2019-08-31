from clusteringV2 import ClusterContainer 
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
    clusterContainer0 = ClusterContainer(class0,class1)
    clusterContainer1 = ClusterContainer(class1,class0)    

    print("Escribiendo clusters...")
    Muestras.writeClusters(clusterContainer0, class0,routeCluster0)
    Muestras.writeClusters(clusterContainer1, class1, routeCluster1)

    print("Asignando clusters a grupos...")
    groups = Grouper.assingGroups(clusterContainer1, k)
    
    print("clase 0: " + str(class0))
    print("clase 1: " + str(class1))
    print("cluster 0: " + str(clusterContainer0.getCluster()))
    print("cluster 1: " + str(clusterContainer1.getCluster()))
    print ("grupos: " + str(groups))

    print("Definiendo hiperplanos...")
    Hiperplane.defineHiperplanes(groups, clusterContainer0)






def main():
    trainClasificator()

main()
    