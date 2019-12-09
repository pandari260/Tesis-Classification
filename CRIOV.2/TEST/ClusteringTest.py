'''
Created on 8 dic. 2019

@author: javier
'''
import unittest
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer
from CRIO.Clustering import isMergeable


class Test(unittest.TestCase):

    def testIsMergeable2D(self):
        d = 2
        cluster_A = Cluster([Sample((0.0,2.0)),Sample((0.0,4.0))], d)
        cluster_B = Cluster([Sample((4.0,2.0)),Sample((4.0,4.0))], d)
        
        samples = SampleContainer([Sample((6.0,3.0))],d) 
        resul = isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(True, resul, "Dos clusters deberian ser mergeables si forman una componente convexa sin outliers")
        
        samples = SampleContainer([Sample((2.3,3.0))],d)
        resul = isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(False, resul, "Dos clusters no deberian ser mergeables si forman una componente convexa con outliers")        
        pass
    
    def testIsMergeable3D(self):
        
        d = 3
        cluster_A = Cluster([Sample((3.0,2.0,0.0)),Sample((4.0,2.0,0.0)),Sample((4.0,1.0,0.0)),Sample((3.0,1.0,0.0))], d)
        cluster_B = Cluster([Sample((3.0,5.0,0.0)),Sample((5.0,5.0,0.0)),Sample((4.0,6.0,0.0))], d)
        
        samples = SampleContainer([Sample((7.0,5.0,0.0)),Sample((7.0,4.0,0.0))],d)
        resul =isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(True, resul, "Dos clusters deberian ser mergeables si forman una componente convexa sin outliers en dimension %s" %(d))
        
        
        samples = SampleContainer([Sample((4.0,4.0,0.0)),Sample((3.0,4.0,0.0)),Sample((5.0,4.0,0.0))], d)        
        resul =isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(False, resul, "Dos clusters no deberian ser mergeables si forman una componente convexa con outliers en dimension %s" %(d)) 
        
        
    def testIsMergeable4D(self):
        
        d = 4
        cluster_A = Cluster([Sample((0.0,3.0,2.0,0.0)),Sample((0.0,4.0,2.0,0.0)),Sample((0.0,4.0,1.0,0.0)),Sample((0.0,3.0,1.0,0.0))], d)
        cluster_B = Cluster([Sample((0.0,3.0,5.0,0.0)),Sample((0.0,5.0,5.0,0.0)),Sample((0.0,4.0,6.0,0.0))], d)
        
        samples = SampleContainer([Sample((0.0,7.0,5.0,0.0)),Sample((0.0,7.0,4.0,0.0))],d)
        resul =isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(True, resul, "Dos clusters deberian ser mergeables si forman una componente convexa sin outliers en dimension %s" %(d))        
        
        samples = SampleContainer([Sample((0.0,4.0,4.0,0.0)),Sample((0.0,3.0,4.0,0.0)),Sample((0.0,5.0,4.0,0.0))], d)      
        resul =isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(False, resul, "Dos clusters no deberian ser mergeables si forman una componente convexa con outliers %s" %(d))
    
    def testIsMergeable5D(self):
        
        d = 5
        cluster_A = Cluster([Sample((0.0,3.0,0.0,2.0,0.0)),Sample((0.0,4.0,0.0,2.0,0.0)),Sample((0.0,4.0,0.0,1.0,0.0)),Sample((0.0,3.0,0.0,1.0,0.0))], d)
        cluster_B = Cluster([Sample((0.0,3.0,0.0,5.0,0.0)),Sample((0.0,5.0,0.0,5.0,0.0)),Sample((0.0,4.0,0.0,6.0,0.0))], d)
        
        samples = SampleContainer([Sample((0.0,7.0,0.0,5.0,0.0)),Sample((0.0,7.0,0.0,4.0,0.0))],d)
        resul =isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(True, resul, "Dos clusters deberian ser mergeables si forman una componente convexa sin outliers en dimension %s" %(d))        
        
        samples = SampleContainer([Sample((0.0,4.0,0.0,4.0,0.0)),Sample((0.0,3.0,0.0,4.0,0.0)),Sample((0.0,5.0,0.0,4.0,0.0))], d)
        resul =isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(False, resul, "Dos clusters no deberian ser mergeables si forman una componente convexa con outliers %s" %(d))
    
    def testisMergeableEmptyOutliers(self):
        
        d=2     
        cluster_A = Cluster([Sample((0.0,2.0)),Sample((0.0,4.0))], d)
        cluster_B = Cluster([Sample((4.0,2.0)),Sample((4.0,4.0))], d)
        samples = SampleContainer([],d)
        resul =isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(True, resul, "Dos clusters deberian ser mergeables si no hay otras muestras")
        
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()