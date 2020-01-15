'''
Created on 15 ene. 2020

@author: javier
'''
import unittest
from CRIO.Modelo.Cluster  import Cluster, mergeClusters, distance

class ClusterTest(unittest.TestCase):


    """merge: combina dos clusters"""
    
    def test_merge_2D(self):
        d = 2
        cluster_A = Cluster([(0.0,0.0),(1.0,1.0)],d)
        cluster_B = Cluster([(2.0,2.0),(3.0,3.0)],d)
        c_test= Cluster([(0.0,0.0),(1.0,1.0),(2.0,2.0),(3.0,3.0)],d)
        c = mergeClusters(cluster_A, cluster_B)
        self.assertEquals(c_test, c, "los cluster deben ser iguales")
        self.assertNotEquals(cluster_A, c, "los clusters no son iguales")
        self.assertNotEquals(cluster_B, c, "los clusters no son iguales")
    
    def test_merge_3D(self):
        d = 3
        cluster_A = Cluster([(0.0,0.0,0.0),(1.0,1.0,0.0)],d)
        cluster_B = Cluster([(2.0,2.0,0.0),(3.0,3.0,0.0)],d)
        c_test= Cluster([(0.0,0.0,0.0),(1.0,1.0,0.0),(2.0,2.0,0.0),(3.0,3.0,0.0)],d)
        c = mergeClusters(cluster_A, cluster_B)
        self.assertEquals(c_test, c, "los cluster deben ser iguales")
        self.assertNotEquals(cluster_A, c, "los clusters no son iguales")
        self.assertNotEquals(cluster_B, c, "los clusters no son iguales")
        
    def test_merge_4D(self):
        d = 4
        cluster_A = Cluster([(0.0,0.0,0.0,0.0),(1.0,1.0,0.0,0.0)],d)
        cluster_B = Cluster([(2.0,2.0,0.0,0.0),(3.0,3.0,0.0,0.0)],d)
        c_test= Cluster([(0.0,0.0,0.0,0.0),(1.0,1.0,0.0,0.0),(2.0,2.0,0.0,0.0),(3.0,3.0,0.0,0.0)],d)
        c = mergeClusters(cluster_A, cluster_B)
        self.assertEquals(c_test, c, "los cluster deben ser iguales")
        self.assertNotEquals(cluster_A, c, "los clusters no son iguales")
        self.assertNotEquals(cluster_B, c, "los clusters no son iguales")
    
    """distance: Calcula la distancia media entre dos clusters"""
    def test_distance2D(self):
        d = 2
        c1 = Cluster([(2.0,5.0),(3.0,5.0),(2.0,4.0),(3.0,4.0)],d)
        c2 = Cluster([(2.0,3.5),(3.0,3.5),(2.0,2.5),(3.0,2.5)],d)
        self.assertEquals(distance(c1, c2), 1.5, "la distancia entre c1 y c2 es 1.5")
    def test_distance3D(self):
        d = 3
        c1 = Cluster([(2.0,5.0,0.0),(3.0,5.0,0.0),(2.0,4.0,0.0),(3.0,4.0,0.0)],d)
        c2 = Cluster([(2.0,3.5,0.0),(3.0,3.5,0.0),(2.0,2.5,0.0),(3.0,2.5,0.0)],d)
        self.assertEquals(distance(c1, c2), 1.5, "la distancia entre c1 y c2 es 1.5")
    def test_distance4D(self):
        d = 4
        c1 = Cluster([(2.0,5.0,0.0,0.0),(3.0,5.0,0.0,0.0),(2.0,4.0,0.0,0.0),(3.0,4.0,0.0,0.0)],d)
        c2 = Cluster([(2.0,3.5,0.0,0.0),(3.0,3.5,0.0,0.0),(2.0,2.5,0.0,0.0),(3.0,2.5,0.0,0.0)],d)
        self.assertEquals(distance(c1, c2), 1.5, "la distancia entre c1 y c2 es 1.5")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()