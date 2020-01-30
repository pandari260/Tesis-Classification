'''
Created on 30 ene. 2020

@author: javier
'''
import unittest
from mock import create_autospec
from CRIO.Modelo.Classifier import Classifier
from CRIO.Modelo.Hyperplane import Hyperplane
from CRIO.Modelo.Region import Region
from CRIO.Modelo.Sample import Sample




class Test(unittest.TestCase):


    def test_Classify_trivial(self):
        d = 2
        k = 1
        t0 = "blue"
        t1 = "red"
        sample_blue = Sample((2.0,0.0))
        sample_red = Sample((6.0,0.0))
        
        hyperplane = Hyperplane({0:4,1:0},16)
        
        classifier = Classifier([],[],t0,t1,d,k)
        classifier.regions = [Region([hyperplane],d)]
        
        self.assertEquals(t1,classifier.classify(sample_blue), "la muestra debe ser azul")
        self.assertEquals(t0,classifier.classify(sample_red), "la muestra debe ser roja")
    
    def test_Classify_squarePolyhedron(self):
        d = 2
        k = 1
        t0 = "blue"
        t1 = "red"
        sample_blue = Sample((0.0,0.0))
        sample_red = Sample((20.0,20.0))
        
        h1 = Hyperplane({0:1,1:1},10)
        h2 = Hyperplane({0:-10,1:-1},10)
        h3 = Hyperplane({0:4,1:-1},50)
        h4 = Hyperplane({0:1,1:-1},10)


        classifier = Classifier([],[],t0,t1,d,k)
        classifier.regions = [Region([h1,h2,h3,h4],d)]
        
        self.assertEquals(t1,classifier.classify(sample_blue), "la muestra debe ser azul")
        self.assertEquals(t0,classifier.classify(sample_red), "la muestra debe ser roja")
        
    def test_Classify_irregularPolyhedron(self):
        d = 2
        k = 1
        t0 = "blue"
        t1 = "red"
        sample_blue = Sample((2.0,2.0))
        sample_red = Sample((6.0,0.0))
        
        h1 = Hyperplane({0:1,1:0},4)
        h2 = Hyperplane({0:-1,1:0},0)
        h3 = Hyperplane({0:0,1:1},4)
        h4 = Hyperplane({0:1,1:-1},0)


        classifier = Classifier([],[],t0,t1,d,k)
        classifier.regions = [Region([h1,h2,h3,h4],d)]
        
        self.assertEquals(t1,classifier.classify(sample_blue), "la muestra debe ser azul")
        self.assertEquals(t0,classifier.classify(sample_red), "la muestra debe ser roja")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testClassify']
    unittest.main()