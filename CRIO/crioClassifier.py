from clustering import *
from pyscipopt import Model
from Grouper import  *
import muestras as Muestras


#TO DO: parametrizar estos parametros
routeClase0 = "clase0.dat"
routeClase1 = "clase1.dat"
routeCluster0 = "cluster0.dat"
routeCluster1 = "cluster1.dat"
routeParameters = "parametros"
dimenssion = 2
k = 2



def trainClasificator():
    print("escribiendo parametros...")
    #writeParameters()

    print("leyendo muestras...")
    class0 = Muestras.leerMuestras(routeClase0, dimenssion)
    class1 = Muestras.leerMuestras(routeClase1, dimenssion)

    print("creando clusters...")
    cluster0 = crearClusters(class0,class1)
    cluster1 = crearClusters(class1,class0)

    print("escribiendo clusters...")
    escribirClusters(routeCluster0, cluster0, class0)
    escribirClusters(routeCluster1, cluster1, class1)

    print("asignando clusters a grupos...")
    groups = assingGroups(cluster1, k)
    print(groups)

def main():
    trainClasificator()

main()
    