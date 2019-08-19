from clustering import *
from pyscipopt import Model
import muestras as Muestras

rutaClase0 = "clase_0.dat"
rutaClase1 = "clase_1.dat"

rutaCluster0 = "cluster0.dat"
rutaCluster1 = "cluster1.dat"

dimension = 2

def clasificar(clusterA, clusterB):



def main():

    clase0 = Muestras.leerMuestras(rutaClase0, dimension)
    clase1 = Muestras.leerMuestras(rutaClase1, dimension)

    cluster0 = crearClusters(clase0,clase1)
    cluster1 = crearClusters(clase1,clase0)

    escribirClusters(rutaCluster0, cluster0, clase0)
    escribirClusters(rutaCluster1, cluster1, clase1)



   
    

main()
    