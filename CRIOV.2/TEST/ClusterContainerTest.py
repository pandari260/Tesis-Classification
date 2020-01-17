'''
Created on 15 ene. 2020

@author: javier
'''
import unittest
from CRIO.Modelo.ClusterContainer import ClusterContainer
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.Sample import Sample

class ClusterContainerTest(unittest.TestCase):

    """equals"""

    def test_equalsTest_sameInstance_2D(self):
        d2 = 2
        d3 = 3
        s1 = Sample((0.0,0.0))
        s2 = Sample((1.0,0.0))
        s3 = Sample((2.0,0.0))
        s4 = Sample((3.0,0.0))
        s5 = Sample((3.0,1.0))
        s6 = Sample((0.0,0.0,0.0))


        c1 = Cluster([s1,s2,s3],d2)
        c2 = Cluster([s4],d2)
        c3 = Cluster([s5],d2)
        c4 = Cluster([s6],d3)

        container1 = ClusterContainer([c1,c2],d2)
        container2 = ClusterContainer([c1,c2],d2)
        container3 = ClusterContainer([c1,c3],d2)
        container4 = ClusterContainer([c3],d2)
        container5 = c3
        container6 = ClusterContainer([c4],d3)

        self.assertEquals(container1, container2, "los container son iguales")
        self.assertNotEquals(container1,container3, "los container no son iguales")
        self.assertNotEquals(container1,container4, "los container no son iguales")
        self.assertNotEquals(container1,container5, "container 5 no es un container")
        self.assertNotEquals(container1,container6, "container 6 es una dimension diferente")





    def test_equalsTest_differentInstancesOfTheSameData2D(self):

        d = 2
        d3 = 3
        c1 = ClusterContainer([Cluster([(0.0,1.0),(1.0,1.0),(2.0,1.0)],d), Cluster([(2.6,3.4)],d)],d)
        c2 = ClusterContainer([Cluster([(0.0,1.0),(1.0,1.0),(2.0,1.0)],d), Cluster([(2.6,3.4)],d)],d)
        c3 = ClusterContainer([Cluster([(0.0,1.0),(1.0,1.0),(2.0,1.0)],d), Cluster([(2.7,3.4)],d)],d)
        c4 = ClusterContainer([Cluster([(2.6,3.4)],d)],d)
        c5 = Cluster([(2.6,3.4)],d)
        c6 = ClusterContainer([Cluster([(0.0,1.0,0.0),(1.0,1.0,0.0),(2.0,1.0,0.0)],d), Cluster([(2.6,3.4,0.0)],d3)],d3)

        self.assertEquals(c1,c2,"Los dos clusters container son iguales")
        self.assertNotEquals(c1,c3, "los clusters container no son iguales")
        self.assertNotEquals(c1, c4, "Los clusters container no son iguales")
        self.assertNotEquals(c1, c5, "c5 no es un cluster container")
        self.assertNotEquals(c1, c6, "los cluster container son de dimension diferente")

    def test_equalsTest_differentInstancesOfTheSameData3D(self):

        d = 3
        d4 = 4
        c1 = ClusterContainer([Cluster([(0.0,1.0,0.0),(1.0,1.0,0.0),(2.0,1.0,0.0)],d), Cluster([(2.6,3.4,0.0)],d)],d)
        c2 = ClusterContainer([Cluster([(0.0,1.0,0.0),(1.0,1.0,0.0),(2.0,1.0,0.0)],d), Cluster([(2.6,3.4,0.0)],d)],d)
        c3 = ClusterContainer([Cluster([(0.0,1.0,0.0),(1.0,1.0,0.0),(2.0,1.0,0.0)],d), Cluster([(2.7,3.4,0.0)],d)],d)
        c4 = ClusterContainer([Cluster([(2.6,3.4,0.0)],d)],d)
        c5 = Cluster([(2.6,3.4,0.0)],d)
        c6 = ClusterContainer([Cluster([(0.0,1.0,0.0,0.0),(1.0,1.0,0.0,0.0),(2.0,1.0,0.0,0.0)],d), Cluster([(2.6,3.4,0.0,0.0)],d4)],d4)

        self.assertEquals(c1,c2,"Los dos clusters container son iguales")
        self.assertNotEquals(c1,c3, "los clusters container no son iguales")
        self.assertNotEquals(c1, c4, "Los clusters container no son iguales")
        self.assertNotEquals(c1, c5, "c5 no es un cluster container")
        self.assertNotEquals(c1, c6, "los cluster container son de dimension diferente")





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
