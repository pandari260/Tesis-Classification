from CRIO.Grouper import GroupContainer, ModelSolution
from CRIO.Clustering import ClusterContainer
from CRIO.Exporter import writeClusters, writeParameters, writeSample
import CRIO.Grouper as Grouper

import unittest
from CRIO.ScipInterface import solveProblem
from wheel.signatures import assertTrue

routeCluster0 = "../CRIO/model/cluster0.dat"
routeCluster1 = "../CRIO/model/cluster1.dat"
routeParameters = "../CRIO/model/globalParameters"
M = 1000000


def prepare(claseA, claseB, k, d):
        writeSample(claseA, "../CRIO/model/class1.dat")
        writeSample(claseB, "../CRIO/model/class0.dat")
        clusterContainerA = ClusterContainer(claseA, claseB)
        clusterContainerB = ClusterContainer(claseB, claseA)
        writeClusters(clusterContainerB, claseB, routeCluster0)
        writeClusters(clusterContainerA, claseA, routeCluster1)
        parameters = [(len(claseB + claseA)), d, len(claseB), len(claseA), k, clusterContainerB.getCantClusters(), clusterContainerA.getCantClusters(), M]
        writeParameters(parameters, routeParameters)
        model = ModelSolution(solveProblem("../CRIO/model/assingGroups.zpl"), clusterContainerA.getCantClusters(), len(claseB), len(claseA), k)
        return clusterContainerA, model


class Test(unittest.TestCase):

    """defineGroups: crea una matriz con las listas de muestras que corresponden a un mismo grupo"""

    def testdefineGroups2D(self):
        
        claseA = [(0.0, 1.0), (0.0, 2.0), (0.0, 3.0), (0.0, 4.0), (0.0, 5.0), (0.0, 6.0), (0.0, 7.0), (0.0, 8.0), (0.0, 9.0), (0.0, 10.0)]
        claseB = [(0.0, 2.5), (0.0, 5.5), (0.0, 9.5)]
        k = 4
        d = 2
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        
        self.assertEquals([((0.0, 1.0), (0.0, 2.0)), ((0.0, 5.0), (0.0, 3.0), (0.0, 4.0)), ((0.0, 10.0),), ((0.0, 6.0), (0.0, 7.0), (0.0, 8.0), (0.0, 9.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass
    
    def testdefineGroups3D(self):
        
        claseA = [(0.0, 0.0, 1.0), (0.0, 0.0, 2.0), (0.0, 0.0, 3.0), (0.0, 0.0, 4.0), (0.0, 0.0, 5.0), (0.0, 0.0, 6.0), (0.0, 0.0, 7.0), (0.0, 0.0, 8.0), (0.0, 0.0, 9.0), (0.0, 0.0, 10.0)]
        claseB = [(0.0, 0.0, 2.5), (0.0, 0.0, 5.5), (0.0, 0.0, 9.5)]
        k = 4
        d = 3
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        
        self.assertEquals(set([((0.0, 0.0, 1.0), (0.0, 0.0, 2.0)), ((0.0, 0.0, 5.0), (0.0, 0.0, 3.0), (0.0, 0.0, 4.0)), ((0.0, 0.0, 10.0),), ((0.0, 0.0, 6.0), (0.0, 0.0, 7.0), (0.0, 0.0, 8.0), (0.0, 0.0, 9.0))]), set(Grouper.defineGroups(clusterContainerA, model, k)))
        pass

    def testdefineGroups4D(self):
        
        claseA = [(0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 2.0, 0.0), (0.0, 0.0, 3.0, 0.0), (0.0, 0.0, 4.0, 0.0), (0.0, 0.0, 5.0, 0.0), (0.0, 0.0, 6.0, 0.0), (0.0, 0.0, 7.0, 0.0), (0.0, 0.0, 8.0, 0.0), (0.0, 0.0, 9.0, 0.0), (0.0, 0.0, 10.0, 0.0), (0.0, 0.0, 11.0, 0.0)]
        claseB = [(0.0, 0.0, 2.5, 0.0), (0.0, 0.0, 5.5, 0.0), (0.0, 0.0, 9.5, 0.0)]
        k = 4
        d = 4
        
        writeSample(claseA, "model/class1.dat")
        writeSample(claseB, "model/class0.dat")
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        
        self.assertEquals(set([((0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 2.0, 0.0)), ((0.0, 0.0, 5.0, 0.0), (0.0, 0.0, 3.0, 0.0), (0.0, 0.0, 4.0, 0.0)), ((0.0, 0.0, 10.0, 0.0), (0.0, 0.0, 11.0, 0.0)), ((0.0, 0.0, 6.0, 0.0), (0.0, 0.0, 7.0, 0.0), (0.0, 0.0, 8.0, 0.0), (0.0, 0.0, 9.0, 0.0))]), set(Grouper.defineGroups(clusterContainerA, model, k)))

        pass
    
    def testDefineGroupsOnlyOneSampleK1(self):
        claseA = [(1.0, 1.0)]
        claseB = [(0.0, 0.0), (2.0, 2.0)]
        k = 1
        d = 2
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((1.0, 1.0),)], Grouper.defineGroups(clusterContainerA, model, k))
        
    def testDefineGroupsOnlyOneSampleK2(self):
        claseA = [(1.0, 1.0)]
        claseB = [(0.0, 0.0), (2.0, 2.0)]
        k = 2
        d = 2
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((1.0, 1.0),)], Grouper.defineGroups(clusterContainerA, model, k))
    
    def testDefineGroupsOnlyOneSampleK3(self):
        claseA = [(1.0, 1.0)]
        claseB = [(0.0, 0.0), (2.0, 2.0)]
        k = 3
        d = 2
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((1.0, 1.0),)], Grouper.defineGroups(clusterContainerA, model, k))
        
    def testDefineGroupsOnlyOneSample3DK1(self):
        claseA = [(1.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 0.0), (2.0, 2.0, 0.0)]
        k = 1
        d = 3
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((1.0, 1.0, 0.0),)], Grouper.defineGroups(clusterContainerA, model, k))
        
    def testDefineGroupsOnlyOneSample3DK2(self):
        claseA = [(1.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 0.0), (2.0, 2.0, 0.0)]
        k = 2
        d = 3
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((1.0, 1.0, 0.0),)], Grouper.defineGroups(clusterContainerA, model, k))
        
    def testDefineGroupsOnlyOneSample3DK3(self):
        claseA = [(1.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 0.0), (2.0, 2.0, 0.0)]
        k = 3
        d = 3
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((1.0, 1.0, 0.0),)], Grouper.defineGroups(clusterContainerA, model, k))
    
    def testDefineGroupsOnlyOneSample4DK1(self):
        claseA = [(0.0, 1.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 0.0, 0.0), (0.0, 2.0, 2.0, 0.0)]
        k = 1
        d = 4
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((0.0, 1.0, 1.0, 0.0),)], Grouper.defineGroups(clusterContainerA, model, k))
    
    def testDefineGroupsOnlyOneSample4DK2(self):
        claseA = [(0.0, 1.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 0.0, 0.0), (0.0, 2.0, 2.0, 0.0)]
        k = 2
        d = 4
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((0.0, 1.0, 1.0, 0.0),)], Grouper.defineGroups(clusterContainerA, model, k)) 
    
    def testDefineGroupsOnlyOneSample4DK3(self):
        claseA = [(0.0, 1.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 0.0, 0.0), (0.0, 2.0, 2.0, 0.0)]
        k = 3
        d = 4
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((0.0, 1.0, 1.0, 0.0),)], Grouper.defineGroups(clusterContainerA, model, k)) 
       
    def testDefineGroupsOnlyOneGroupK1(self):
        claseA = [(1.0, 1.0), (2.0, 1.0), (3.0, 1.0)]
        claseB = [(0.0, 1.0), (4.0, 1.0)]
        k = 1
        d = 2
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((3.0, 1.0), (1.0, 1.0), (2.0, 1.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass

    def testDefineGroupsOnlyOneGroupK2(self):
        claseA = [(1.0, 1.0), (2.0, 1.0), (3.0, 1.0)]
        claseB = [(0.0, 1.0), (4.0, 1.0)]
        k = 2
        d = 2
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((3.0, 1.0), (1.0, 1.0), (2.0, 1.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass
    
    def testDefineGroupsOnlyOneGroupK3(self):
        claseA = [(1.0, 1.0), (2.0, 1.0), (3.0, 1.0)]
        claseB = [(0.0, 1.0), (4.0, 1.0)]
        k = 3
        d = 2
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((3.0, 1.0), (1.0, 1.0), (2.0, 1.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass
    
    def testDefineGroupsOnlyOneGroup3D(self):
        claseA = [(1.0, 1.0, 0.0), (2.0, 1.0, 0.0), (3.0, 1.0, 0.0)]
        claseB = [(0.0, 1.0, 0.0), (4.0, 1.0, 0.0)]
        k = 1
        d = 3
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((3.0, 1.0, 0.0), (1.0, 1.0, 0.0), (2.0, 1.0, 0.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass

    def testDefineGroupsOnlyOneGroupK23D(self):
        claseA = [(1.0, 1.0, 0.0), (2.0, 1.0, 0.0), (3.0, 1.0, 0.0)]
        claseB = [(0.0, 1.0, 0.0), (4.0, 1.0, 0.0)]
        k = 2
        d = 3
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((3.0, 1.0, 0.0), (1.0, 1.0, 0.0), (2.0, 1.0, 0.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass
    
    def testDefineGroupsOnlyOneGroupK33D(self):
        claseA = [(1.0, 1.0, 0.0), (2.0, 1.0, 0.0), (3.0, 1.0, 0.0)]
        claseB = [(0.0, 1.0, 0.0), (4.0, 1.0, 0.0)]
        k = 3
        d = 3
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((3.0, 1.0, 0.0), (1.0, 1.0, 0.0), (2.0, 1.0, 0.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass
    
    def testDefineGroupsOnlyOneGroup4D(self):
        claseA = [(0.0, 1.0, 1.0, 0.0), (0.0, 2.0, 1.0, 0.0), (0.0, 3.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 1.0, 0.0), (0.0, 4.0, 1.0, 0.0)]
        k = 1
        d = 4
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((0.0, 3.0, 1.0, 0.0), (0.0, 1.0, 1.0, 0.0), (0.0, 2.0, 1.0, 0.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass

    def testDefineGroupsOnlyOneGroupK24D(self):
        claseA = [(0.0, 1.0, 1.0, 0.0), (0.0, 2.0, 1.0, 0.0), (0.0, 3.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 1.0, 0.0), (0.0, 4.0, 1.0, 0.0)]
        k = 2
        d = 4
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((0.0, 3.0, 1.0, 0.0), (0.0, 1.0, 1.0, 0.0), (0.0, 2.0, 1.0, 0.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass
    
    def testDefineGroupsOnlyOneGroupK34D(self):
        claseA = [(0.0, 1.0, 1.0, 0.0), (0.0, 2.0, 1.0, 0.0), (0.0, 3.0, 1.0, 0.0)]
        claseB = [(0.0, 0.0, 1.0, 0.0), (0.0, 4.0, 1.0, 0.0)]
        k = 3
        d = 4
        clusterContainerA, model = prepare(claseA, claseB, k, d)

        self.assertEquals([((0.0, 3.0, 1.0, 0.0), (0.0, 1.0, 1.0, 0.0), (0.0, 2.0, 1.0, 0.0))], Grouper.defineGroups(clusterContainerA, model, k))
        pass
    
    def testDefineGroupsOneGroupForeachSample(self):
        claseA = [(0.0, 0.0), (0.0, 2.0), (2.0, 0.0), (2.0, 2.0)]
        claseB = [(0.0, 0.1), (1.0, 2.0), (2.0, 1.0), (0.0, 1.0), (1.0, 1.0)]
        k = 4
        d = 2
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((0.0, 0.0),), ((2.0, 0.0),), ((2.0, 2.0),), ((0.0, 2.0),)], Grouper.defineGroups(clusterContainerA, model, k))
    
    def testDefineGroupsOneGroupForeachSample3D(self):
        claseA = [(0.0, 0.0, 0.0), (0.0, 2.0, 0.0), (2.0, 0.0, 0.0), (2.0, 2.0, 0.0)]
        claseB = [(0.0, 0.1, 0.0), (1.0, 2.0, 0.0), (2.0, 1.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0)]
        k = 4
        d = 3
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((0.0, 0.0, 0.0),), ((2.0, 0.0, 0.0),), ((2.0, 2.0, 0.0),), ((0.0, 2.0, 0.0),)], Grouper.defineGroups(clusterContainerA, model, k))
    
    def testDefineGroupsOneGroupForeachSample4D(self):
        claseA = [(0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 2.0, 0.0), (0.0, 2.0, 0.0, 0.0), (0.0, 2.0, 2.0, 0.0)]
        claseB = [(0.0, 0.0, 0.1, 0.0), (0.0, 1.0, 2.0, 0.0), (0.0, 2.0, 1.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 1.0, 1.0, 0.0)]
        k = 4
        d = 4
        
        clusterContainerA, model = prepare(claseA, claseB, k, d)
        self.assertEquals([((0.0, 0.0, 0.0, 0.0),), ((0.0, 2.0, 0.0, 0.0),), ((0.0, 2.0, 2.0, 0.0),), ((0.0, 0.0, 2.0, 0.0),)], Grouper.defineGroups(clusterContainerA, model, k))
    
    """ def assingGroups(cantClusters,model, k): #assigna cada id de cluster a uno de los k grupos """

    
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
