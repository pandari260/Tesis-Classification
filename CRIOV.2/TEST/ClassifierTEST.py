'''
Created on 30 ene. 2020

@author: javier
'''
import unittest
from mock import create_autospec
from CRIO.Modelo.Classifier import Classifier, createScrollSample, displace
from CRIO.Modelo.Hyperplane import Hyperplane
from CRIO.Modelo.Region import Region
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer




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
    
    def test_Classify_irregularPolyhedron(self):
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
        
    def test_Classify_squarePolyedrom(self):
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

    def test_classify_twoSquarePoliedrom(self):
        d = 2
        k = 2
        t0 = "blue"
        t1 = "red"
        sample_blue1 = Sample((8.0,8.0))
        sample_blue2 = Sample((2.0,2.0))
        sample_red = Sample((5.0,5.0))
        
        h1 = Hyperplane({0:1,1:0},4)
        h2 = Hyperplane({0:-1,1:0},0)
        h3 = Hyperplane({0:0,1:1},4)
        h4 = Hyperplane({0:1,1:-1},0)
        
        h5 = Hyperplane({0:1,1:0},10)
        h6 = Hyperplane({0:-1,1:0},-6)
        h7 = Hyperplane({0:0,1:1},10)
        h8 = Hyperplane({0:0,1:-1},-6)



        classifier = Classifier([],[],t0,t1,d,k)
        classifier.regions = [Region([h1,h2,h3,h4],d),Region([h5,h6,h7,h8],d)]
        
        self.assertEquals(t1,classifier.classify(sample_blue1), "la muestra debe ser azul")
        self.assertEquals(t1,classifier.classify(sample_blue2), "la muestra debe ser azul")

        self.assertEquals(t0,classifier.classify(sample_red), "la muestra debe ser roja")
    
    def test_classify_Polytope(self):
        d = 2
        k = 2
        t0 = "blue"
        t1 = "red"
        sample_blue = Sample((-5.0,-5.0))
        sample_red = Sample((5.0,5.0))
        
        h1 = Hyperplane({0:1,1:2},5)
        h2 = Hyperplane({0:1,1:0.5},5)     
        
        classifier = Classifier([],[],t0,t1,d,k)
        classifier.regions = [Region([h1,h2],d)]
        
        self.assertEquals(t1,classifier.classify(sample_blue), "la muestra debe ser azul")

        self.assertEquals(t0,classifier.classify(sample_red), "la muestra debe ser roja")
    
    def test_classify_twoPolytope(self):
        d = 2
        k = 2
        t0 = "blue"
        t1 = "red"
        sample_blue1 = Sample((-10.0,-5.0))
        sample_blue2 = Sample((40.0,20.0))

        sample_red = Sample((5.0,5.0))
        
        h1 = Hyperplane({0:1,1:2},5)
        h2 = Hyperplane({0:1,1:0.5},5)         
        h3 = Hyperplane({0:-1,1:-2},-30)
        h4 = Hyperplane({0:-1,1:-0.5},-30)     
        
        classifier = Classifier([],[],t0,t1,d,k)
        classifier.regions = [Region([h1,h2],d), Region([h3,h4],d)]
        
        self.assertEquals(t1,classifier.classify(sample_blue1), "la muestra debe ser azul")
        self.assertEquals(t1,classifier.classify(sample_blue2), "la muestra debe ser azul")
        self.assertEquals(t0,classifier.classify(sample_red), "la muestra debe ser roja")



    def test_createScrollTuple(self):
        d = 2
        samples = SampleContainer([(2.0,3.0),(-2.0,3.0),(-2.0,-2.0),(3.0,-2.0),(-4.0,4.0),(-4.0,-2.0),(1.0,-3.0)],d)
        
        
        gb = createScrollSample(samples, d)
        for i in range(d):
            print(gb.getFeature(i))
            
        self.assertEquals(Sample((4.0,3.0)), createScrollSample(samples, d))
    def test_displace(self):
        d = 2
        samples = SampleContainer([(2.0,3.0),(-2.0,3.0),(-2.0,-2.0),(3.0,-2.0),(-4.0,4.0),(-4.0,-2.0),(1.0,-3.0)],d)
        scroll = Sample((4.0,3.0))
        
        
        test = displace(samples,scroll)
        print(map(lambda s:s.getData(),test.getSamples()))
        self.assertEqual(SampleContainer([(6.0,6.0),(2.0,6.0),(2.0,1.0),(7.0,1.0),(0.0,7.0),(0.0,1.0),(5.0,0.0)],d), displace(samples,scroll))
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testClassify']
    unittest.main()
    
    
    
    
    