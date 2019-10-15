from CRIO.Grouper import GroupContainer, ModelSolution
from CRIO.Clustering import ClusterContainer
from CRIO.Exporter import writeClusters, writeParameters, writeSample
import CRIO.Grouper as Grouper

import unittest
from CRIO.ScipInterface import solveProblem

routeCluster0 = "model/cluster0.dat"
routeCluster1 = "model/cluster1.dat"
routeParameters = "model/globalParameters"
M = 1000000



class Test(unittest.TestCase):

    """defineGroups: crea una matriz con las listas de muestras que corresponden a un mismo grupo"""
    def testdefineGroups(self):
        
        claseA = [(0.0,1.0),(0.0,2.0),(0.0,3.0),(0.0,4.0),(0.0,5.0),(0.0,6.0),(0.0,7.0),(0.0,8.0),(0.0,9.0),(0.0,10.0)]
        claseB = [(0.0,2.5),(0.0,5.5),(0.0,9.5)]
        
        writeSample(claseA,"model/class1.dat")
        writeSample(claseB,"model/class0.dat")
        
        k = 4
        clusterContainerA = ClusterContainer(claseA,claseB)
        clusterContainerB = ClusterContainer(claseB, claseA)
        
        writeClusters(clusterContainerB, claseB,routeCluster0)
        writeClusters(clusterContainerA, claseA, routeCluster1)
        
        parameters = [(len(claseB + claseA)), 2, len(claseB), len(claseA),k , clusterContainerB.getCantClusters(), clusterContainerA.getCantClusters(),M]
        writeParameters(parameters, routeParameters)
        
        
        model = ModelSolution(solveProblem("model/assingGroups.zpl"), clusterContainerA.getCantClusters(),3,9,k )
        k = 4
        
        
        self.assertEquals([((0.0, 1.0), (0.0, 2.0)), ((0.0, 5.0), (0.0, 3.0), (0.0, 4.0)), ((0.0, 10.0),), ((0.0, 6.0), (0.0, 7.0), (0.0, 8.0), (0.0, 9.0))], Grouper.defineGroups(clusterContainerA, model, k))
        
        
        
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()