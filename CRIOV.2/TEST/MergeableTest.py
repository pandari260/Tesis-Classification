'''
Created on 8 dic. 2019

@author: javier
'''
import unittest
from CRIO.Modelo import * 
from CRIO.Clustering import *


class Test(unittest.TestCase):

    #determina si hay una muestra perteneciente a "samples" en la componente convexa de entre los clusters A y B 
    #ambos clusters deben tener el mismo valor de dimension
    def isMergeableTest(self):
        d = 2
        cluster_A = Cluster([Sample((0.0,2.0)),Sample((0.0,4.0))], 2)
        cluster_B = Cluster([Sample((4.0,2.0)),Sample((4.0,4.0))], 2)
        
        samples = SampleContainer([Sample((2.0,3.0))]) 
        resul = isMergeable(cluster_A, cluster_B, samples)
        self.assertEqual(False, resul)        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()