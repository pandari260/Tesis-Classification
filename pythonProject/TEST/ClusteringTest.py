import unittest
import CRIO.Clustering as Clustering
import math
from __builtin__ import dict
from CRIO.Exporter import writeSample
from scipy.cluster._hierarchy import cluster_dist

routeClassA= "../CRIO/model/clusteringClassA.dat"
routeClassB= "../CRIO/model/clusteringClassB.dat"
routeParams = "../CRIO/model/clusteringParameters"
routeModel ="../CRIO/model/clustering.zpl"


class Test(unittest.TestCase):

    """ SampleKeyDict: toma una matriz no vacia y la transforma en un diccionario cuyas claves 
    son los elementos de la matriz y los valores el indice correspondiente a cada lista """
    
    def testSampleKeyEmptyMatrix(self):
        print("caso matriz vacia:\n")
        matrix = []
        self.assertEquals(None, Clustering.sampleKeyDict(matrix))
        pass
    
    def testSampleKeyNotMatrix(self):
        print("caso no es una matriz:\n")
        matrix = [0.0]
        num = 4.0        
        self.assertEquals(None, Clustering.sampleKeyDict(matrix))
        self.assertEquals(None, Clustering.sampleKeyDict(num))
        pass
    
    def testSampleKeyEmptyCluster(self):
        print("caso hay un cluster vacio:\n")
        matrix = [[]]
        self.assertEquals(None, Clustering.sampleKeyDict(matrix))
        
        matrix = [[0.0],[2.0],[2.0],[]]
        self.assertEquals(None, Clustering.sampleKeyDict(matrix)) 
        
        matrix = [[0.0],[2.0],[],[2.0]]
        self.assertEquals(None, Clustering.sampleKeyDict(matrix))        
        pass
    
    def testSampleKey(self):
        print("caso favorable:\n")
        
        matrix = [[0.0]]
        dict = {0:0}
        self.assertEquals(dict, Clustering.sampleKeyDict(matrix))
        
        matrix = [[0.0],[1.0],[2.0],[3.0]]
        dict = {0.0:0.0,1.0:1.0,2.0:2.0,3.0:3.0}
        self.assertEquals(dict, Clustering.sampleKeyDict(matrix))
        
    """defineClusters: crea cluster con las muestras de clase A que no contienen muestras de clase B """
    def testDefineClusterNoneOutlier(self):
        classA = [(0.0,0.0),(0.0,1.0),(0.0,2.0),(0.0,3.0)]
        classB = [(0.0,4.0),(0.0,5.0),(0.0,6),(0.0,7)]
        self.assertEquals([classA], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,0.0,0.0),(0.0,0.0,1.0),(0.0,0.0,2.0),(0.0,0.0,3.0)]
        classB = [(0.0,0.0,4.0),(0.0,0.0,5.0),(0.0,0.0,6.0),(0.0,0.0,7.0)]
        self.assertEquals([classA], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,0.0,0.0),(0.0,1.0,0.0),(0.0,2.0,0.0),(0.0,3.0,0.0)]
        classB = [(0.0,4.0,0.0),(0.0,5.0,0.0),(0.0,6.0,0.0),(0.0,7.0,0.0)]
        self.assertEquals([classA], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
    
    def testDefineClusterNoneOutlierOnlyOneSample(self):
        classA = [(0.0,0.0)]
        classB = [(0.0,4.0)]
        self.assertEquals([classA], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,0.0,0.0)]
        classB = [(0.0,0.0,4.0)]
        self.assertEquals([classA], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,0.0)]
        classB = [(0.0,4.0)]
        self.assertEquals([classA], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,0.0,0.0)]
        classB = [(0.0,4.0,0.0)]
        self.assertEquals([classA], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
    
    def testDefineClusterOneSampleCluster(self):
        classA = [(0.0,1.0),(0.0,3.0),(0.0,5.0),(0.0,7.0)]
        classB = [(0.0,2.0),(0.0,4.0),(0.0,6.0),(0.0,8.0)]
        self.assertEquals([[(0.0,1.0)],[(0.0,3.0)],[(0.0,5.0)],[(0.0,7.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([[(0.0,2.0)],[(0.0,4.0)],[(0.0,6.0)],[(0.0,8.0)]], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,0.0,1.0),(0.0,0.0,3.0),(0.0,0.0,5.0),(0.0,0.0,7)]
        classB = [(0.0,0.0,2.0),(0.0,0.0,4.0),(0.0,0.0,6),(0.0,0.0,8)]
        self.assertEquals([[(0.0,0.0,1.0)],[(0.0,0.0,3.0)],[(0.0,0.0,5.0)],[(0.0,0.0,7.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([[(0.0,0.0,2.0)],[(0.0,0.0,4.0)],[(0.0,0.0,6)],[(0.0,0.0,8.0)]], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,1.0,0.0),(0.0,3.0,0.0),(0.0,5.0,0.0),(0.0,7.0,0.0)]
        classB = [(0.0,2.0,0.0),(0.0,4.0,0.0),(0.0,6.0,0.0),(0.0,8.0,0.0)]
        
        print("el cluster: " + str(Clustering.defineClusters(classB,classA)))
        self.assertEquals([[(0.0,1.0,0.0)],[(0.0,3.0,0.0)],[(0.0,5.0,0.0)],[(0.0,7.0,0.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([[(0.0,2.0,0.0)],[(0.0,4.0,0.0)],[(0.0,6.0,0.0)],[(0.0,8.0,0.0)]], Clustering.defineClusters(classB, classA))
    
    def testDefineClusterOneSampleClusterOnlyOneOutlier(self):
        classA = [(0.0,0.0),(0.0,1.0),(0.0,2.0),(0.0,3.0)]
        classB = [(0.0,1.5)]      
        self.assertEquals([[(0.0,0.0),(0.0,1.0)],[(0.0,2.0),(0.0,3.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,0.0,0.0),(0.0,0.0,1.0),(0.0,0.0,2.0),(0.0,0.0,3.0)]
        classB = [(0.0,0.0,1.5)]      
        self.assertEquals([[(0.0,0.0,0.0),(0.0,0.0,1.0)],[(0.0,0.0,2.0),(0.0,0.0,3.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
        
        classA = [(0.0,0.0,0.0),(0.0,1.0,0.0),(0.0,2.0,0.0),(0.0,3.0,0.0)]
        classB = [(0.0,1.5,0.0)]      
        self.assertEquals([[(0.0,0.0,0.0),(0.0,1.0,0.0)],[(0.0,2.0,0.0),(0.0,3.0,0.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([classB], Clustering.defineClusters(classB, classA))
    
    def testDefineClusterExtremeOutliers(self):
        classA = [(0.0,0.0),(0.0,1.0),(0.0,2.0),(0.0,3.0)]
        classB = [(0.0,-1.0),(0.0,1.5),(0.0,4.0)]
        self.assertEquals([[(0.0,0.0),(0.0,1.0)],[(0.0,2.0),(0.0,3.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([[(0.0,-1.0)],[(0.0,1.5)],[(0.0,4.0)]], Clustering.defineClusters(classB, classA))  
    

        classA = [(0.0,0.0,0.0),(0.0,0.0,1.0),(0.0,0.0,2.0),(0.0,0.0,3.0)]
        classB = [(0.0,0.0,-1.0),(0.0,0.0,1.5),(0.0,0.0,4.0)]       
        self.assertEquals([[(0.0,0.0,0.0),(0.0,0.0,1.0)],[(0.0,0.0,2.0),(0.0,0.0,3.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([[(0.0,0.0,-1.0)],[(0.0,0.0,1.5)],[(0.0,0.0,4.0)]], Clustering.defineClusters(classB, classA)) 
        
        classA = [(0.0,0.0,0.0,0.0),(0.0,0.0,1.0,0.0),(0.0,0.0,2.0,0.0),(0.0,0.0,3.0,0.0)]
        classB = [(0.0,0.0,-1.0,0.0),(0.0,0.0,1.5,0.0),(0.0,0.0,4.0,0.0)]       
        self.assertEquals([[(0.0,0.0,0.0,0.0),(0.0,0.0,1.0,0.0)],[(0.0,0.0,2.0,0.0),(0.0,0.0,3.0,0.0)]], Clustering.defineClusters(classA, classB))
        self.assertEquals([[(0.0,0.0,-1.0,0.0)],[(0.0,0.0,1.5,0.0)],[(0.0,0.0,4.0,0.0)]], Clustering.defineClusters(classB, classA))
    

        
    """createDefoultCluster: dado un conjunto de muestras retorna una lista de clusters trivial"""
    def testcreateDefoultcluster(self):
        class2 = [(1.0,1.0),(2.0,2.0),(3.0,3.0),(4.0,4.0)]
        self.assertEquals([[(1.0,1.0)],[(2.0,2.0)],[(3.0,3.0)],[(4.0,4.0)]], Clustering.creatDefaultCluster(class2))
        class3 = [(1.0,1.0,1.0),(2.0,2.0,2.0),(3.0,3.0,3.0),(4.0,4.0,4.0)]
        self.assertEquals([[(1.0,1.0,1.0)],[(2.0,2.0,2.0)],[(3.0,3.0,3.0)],[(4.0,4.0,4.0)]], Clustering.creatDefaultCluster(class3))
        class3 = [(1.0,1.0,1.0,1.0),(2.0,2.0,2.0,2.0),(3.0,3.0,3.0,3.0),(4.0,4.0,4.0,4.0)]
        self.assertEquals([[(1.0,1.0,1.0,1.0)],[(2.0,2.0,2.0,2.0)],[(3.0,3.0,3.0,3.0)],[(4.0,4.0,4.0,4.0)]], Clustering.creatDefaultCluster(class3))    
    
    
    """ crearMatrizDistancia: Tomas una lista cluster y crea una matriz con las disancias entre cada uno """
    def testcrearMatrizDistancia(self):
        clusters= [[(0.0,1.0)],[(0.0,2.0)],[(0.0,3.0)]]
        self.assertEqual([[],[1.0],[2.0,1.0]], Clustering.crearMatrizDistancia(clusters))
        
        clusters= [[(0.0,0.0,1.0)],[(0.0,0.0,2.0)],[(0.0,0.0,3.0)]]
        self.assertEqual([[],[1.0],[2.0,1.0]], Clustering.crearMatrizDistancia(clusters))
        
        clusters= [[(0.0,0.0,0.0,1.0)],[(0.0,0.0,0.0,2.0)],[(0.0,0.0,0.0,3.0)]]
        self.assertEqual([[],[1.0],[2.0,1.0]], Clustering.crearMatrizDistancia(clusters))
        
    def testcrearMatrizDistanciaSeveralSamplesInCluster(self):
        clusters = [[(0.0,0.0),(0.0,1.0)],[(0.0,2.0),(0.0,3.0)],[(0.0,4.0),(0.0,5.0)]]
        self.assertEqual([[],[2.0],[4.0,2.0]], Clustering.crearMatrizDistancia(clusters))
        
        clusters = [[(0.0,0.0,0.0),(0.0,0.0,1.0)],[(0.0,0.0,2.0),(0.0,0.0,3.0)],[(0.0,0.0,4.0),(0.0,0.0,5.0)]]
        self.assertEqual([[],[2.0],[4.0,2.0]], Clustering.crearMatrizDistancia(clusters))
        
        clusters = [[(0.0,0.0,0.0,0.0),(0.0,0.0,1.0,0.0)],[(0.0,0.0,2.0,0.0),(0.0,0.0,3.0,0.0)],[(0.0,0.0,4.0,0.0),(0.0,0.0,5.0,0.0)]]
        self.assertEqual([[],[2.0],[4.0,2.0]], Clustering.crearMatrizDistancia(clusters))
    
    def testcrearMatrizDistanciaEmpty(self):
        clusters = []
        self.assertEqual([], Clustering.crearMatrizDistancia(clusters))
    

    """ distanceBtwSamples: Toma dos muestras y devuelve la distancia entre ellos"""
    def testdistanceBtwSamples(self):
        sampleA = (1.0,0.0)
        sampleB = (2.0,0.0)
        self.assertEquals(1.0, Clustering.distanceBtwSamples(sampleA, sampleB))
        
        sampleA = (1.0,0.0,0.0)
        sampleB = (2.0,0.0,0.0)
        self.assertEquals(1.0, Clustering.distanceBtwSamples(sampleA, sampleB))
        
        sampleA = (1.0,0.0,0.0,0.0)
        sampleB = (2.0,0.0,0.0,0.0)
        self.assertEquals(1.0, Clustering.distanceBtwSamples(sampleA, sampleB))
    
    """distanceBtwClusters: Toma dos clusters y calcula la distancia entre los centro de cada uno
    el centro de un cluster es el 'punto' que se forma al calcular el promedio de cada coordenada
    de todas las muestras"""
    def testdistanceBtwClusters(self):
        clusterA = [(1.0,2.0),(2.0,2.0),(1.0,3.0),(2.0,3.0)]
        clusterB = [(3.0,1.0),(4.0,1.0),(3.0,2.0),(4.0,2.0)]
        self.assertEquals(math.sqrt(5), Clustering.distanceBtwClusters(clusterA, clusterB)) 
        
        clusterA = [(0.0,1.0,2.0),(0.0,2.0,2.0),(0.0,1.0,3.0),(0.0,2.0,3.0)]
        clusterB = [(0.0,3.0,1.0),(0.0,4.0,1.0),(0.0,3.0,2.0),(0.0,4.0,2.0)]
        self.assertEquals(math.sqrt(5), Clustering.distanceBtwClusters(clusterA, clusterB)) 
        
        clusterA = [(0.0,0.0,1.0,2.0),(0.0,0.0,2.0,2.0),(0.0,0.0,1.0,3.0),(0.0,0.0,2.0,3.0)]
        clusterB = [(0.0,0.0,3.0,1.0),(0.0,0.0,4.0,1.0),(0.0,0.0,3.0,2.0),(0.0,0.0,4.0,2.0)]
        self.assertEquals(math.sqrt(5), Clustering.distanceBtwClusters(clusterA, clusterB)) 
    
    """minimaDistancia: dada una matriz de distancia retorna las coordenadas (fila, columna) del menor valor"""
    def testMinimaDistancia(self):
        matriz = [[],[1.0, 3.0],[1.4,2.0,3.0]]
        self.assertEquals((1,0), Clustering.minimaDistancia(matriz))
        
        matriz = [[],[6.0, 3.0],[9.0,2.0,3.0], [2.0,5.0,5.0,5.0]]
        self.assertEquals((2,1), Clustering.minimaDistancia(matriz))
        
        matriz = []
        self.assertEquals((-1,-1), Clustering.minimaDistancia(matriz))
        
    """contieneOutlier: Determina si hay un outlier que impide que se fucionen dos clusters devuelve uno si no contiene, 0 si contiene"""
    def testcontieneOutlierNoneOutlier(self):
        Cs = [(1.0,1.0),(2.0,2.0),(3.0,1.0)]
        Cr = [(3.0,4.0),(4.0,4.0),(4.0,5.0)]
        claseB =[(1000.0,1000.0)]
        
        self.assertEquals(1, Clustering.contieneOutlier(Cr, Cs, claseB))
        
        Cs = [(1.0,1.0),(2.0,2.0),(3.0,1.0)]
        Cr = [(3.0,4.0),(4.0,4.0),(4.0,5.0)]
        claseB =[(3.0,3.0)]
        
        self.assertEquals(0, Clustering.contieneOutlier(Cr, Cs, claseB))
        
        Cs = [(1.0,1.0,0.0),(2.0,2.0,0.0),(3.0,1.0,0.0)]
        Cr = [(3.0,4.0,0.0),(4.0,4.0,0.0),(4.0,5.0,0.0)]
        claseB =[(1000.0,1000.0,0.0)]
        
        self.assertEquals(1, Clustering.contieneOutlier(Cr, Cs, claseB))
        
        Cs = [(1.0,1.0,0.0),(2.0,2.0,0.0),(3.0,1.0,0.0)]
        Cr = [(3.0,4.0,0.0),(4.0,4.0,0.0),(4.0,5.0,0.0)]
        claseB =[(3.0,3.0,0.0)]
        
        self.assertEquals(0, Clustering.contieneOutlier(Cr, Cs, claseB))
        
        Cs = [(0.0,1.0,1.0,0.0),(0.0,2.0,2.0,0.0),(0.0,3.0,1.0,0.0)]
        Cr = [(0.0,3.0,4.0,0.0),(0.0,4.0,4.0,0.0),(0.0,4.0,5.0,0.0)]
        claseB =[(0.0,1000.0,1000.0,0.0)]
        
        self.assertEquals(1, Clustering.contieneOutlier(Cr, Cs, claseB))
        
        Cs = [(0.0,1.0,1.0,0.0),(0.0,2.0,2.0,0.0),(0.0,3.0,1.0,0.0)]
        Cr = [(0.0,3.0,4.0,0.0),(0.0,4.0,4.0,0.0),(0.0,4.0,5.0,0.0)]
        claseB =[(0.0,3.0,3.0,0.0)]
        
        self.assertEquals(0, Clustering.contieneOutlier(Cr, Cs, claseB))
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()