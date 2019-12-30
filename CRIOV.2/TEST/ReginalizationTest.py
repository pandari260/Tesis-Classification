'''
Created on 17 dic. 2019

@author: javier:v
'''
import unittest
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.Group import Group
from CRIO.Regionalization import defineHyperplane


class RegionalizationTest(unittest.TestCase):


    def test_defineHyperplane_trivial_2D(self):
        d = 2
        cluster = Cluster([(7.0,4.0)],d)
        group = Group([(5.0,4.0)],d)
        
        (piVars,alfa) = defineHyperplane(group, cluster)
     

        self.assertTrue(0.99999995001 > piVars[0] and 0.99999995000 < piVars[0],"0.99999995001 debe multiplicar la primer incognita")
        self.assertEquals(0.0, piVars[1] ,"0.0 debe multiplicar la segunda incognita")
        self.assertTrue(5.99999970006 > alfa and 5.99999970005 < alfa, "alfa debe ser 5.99999970006")
    
    def test_defineHyperplane_severalSamples_2D(self):
        d = 2
        cluster = Cluster([(6.5,4.5),(8.0,5.0),(9.0,5.0),(7.0,3.0),(8.0,4.0),(7.0,5.0)],d)
        group = Group([(5.0,4.0),(5.0,5.0),(6.0,5.0),(5.0,6.0),(4.0,6.0)],d)
        (piVars,alfa) = defineHyperplane(group, cluster)
      

        self.assertTrue(2.0 < piVars[0] and 2.1 > piVars[0],"2 debe multiplicar la primer incognita")
        self.assertTrue(-2.0 < piVars[1] and -1.9 > piVars[1] ,"-2 debe multiplicar la segunda incognita")
        self.assertTrue( 3.0 < alfa and 3.1 > alfa, "alfa debe ser 3")
    
    def test_defineHyperplane_trivial_3D(self):
        d = 3
        cluster = Cluster([(7.0,4.0,0.0)],d)
        group = Group([(5.0,4.0,0.0)],d)
        
        (piVars,alfa) = defineHyperplane(group, cluster)
        
        print("valor 0: " + str(piVars[0]))
        print("valor 1: " + str(piVars[1]))
        print("valor 2: " + str(piVars[2]))
    
        self.assertTrue(0.99999995001 < piVars[0] and 0.99999995002 > piVars[0],"0.99999995001 debe multiplicar la primer incognita")
        self.assertEqual(0.0, piVars[1] ,"0.0 debe multiplicar la segunda incognita")
        self.assertEqual(0.0,piVars[2],"cero debe multiplicar a la tercera incognita")
        self.assertTrue(5.99999970006 < alfa and 5.99999970007 > alfa, "alfa debe ser 5.99999970007")
    
    def test_defineHyperplane_severalSamples_3D(self):
        d = 3
        cluster = Cluster([(0.0,6.5,4.5),(0.0,8.0,5.0),(0.0,9.0,5.0),(0.0,7.0,3.0),(0.0,8.0,4.0),(0.0,7.0,5.0)],d)
        group = Group([(0.0,5.0,4.0),(0.0,5.0,5.0),(0.0,6.0,5.0),(0.0,5.0,6.0),(0.0,4.0,6.0)],d)
        (piVars,alfa) = defineHyperplane(group, cluster)
        
        self.assertEquals(piVars[0],0.0, "0.0 debe multiplicar la primera innognita")
        self.assertTrue(2.0 < piVars[1] and 2.1 > piVars[1],"2 debe multiplicar la primer incognita")
        self.assertTrue(-2.0 < piVars[2] and -1.9 > piVars[2] ,"-2 debe multiplicar la segunda incognita")
        self.assertTrue( 3.0 < alfa and 3.1 > alfa, "alfa debe ser 3")
        self.assertEqual(piVars[0], 0.0, "la dimension agregada no debe modificar la rectar ya que vale cero en todos los casos en el caso 3D")

    def test_defineHyperplane_trivial_4D(self):
        d = 4
        cluster = Cluster([(7.0,4.0,0.0,0.0)],d)
        group = Group([(5.0,4.0,0.0,0.0)],d)
        
        (piVars,alfa) = defineHyperplane(group, cluster)

        

        self.assertTrue(0.999999950215 < piVars[0] and 0.999999950216 > piVars[0],"0.99999995001 debe multiplicar la primer incognita")
        self.assertEqual(0.0, piVars[1] ,"0.0 debe multiplicar la segunda incognita")
        self.assertEqual(0.0,piVars[2],"cero debe multiplicar a la tercera incognita")
        self.assertEqual(0.0,piVars[3],"cero debe multiplicar a la cuarta incognita")
        self.assertTrue(5.9999997012 < alfa and 5.9999997013 > alfa, "alfa debe ser 5.99999970007")

    def test_defineHyperplane_severalSamples_4D(self):
        d = 4
        cluster = Cluster([(0.0,6.5,4.5,0.0),(0.0,8.0,5.0,0.0),(0.0,9.0,5.0,0.0),(0.0,7.0,3.0,0.0),(0.0,8.0,4.0,0.0),(0.0,7.0,5.0,0.0)],d)
        group = Group([(0.0,5.0,4.0,0.0),(0.0,5.0,5.0,0.0),(0.0,6.0,5.0,0.0),(0.0,5.0,6.0,0.0),(0.0,4.0,6.0,0.0)],d)
        (piVars,alfa) = defineHyperplane(group, cluster)
        
        print("valor 0: " + str(piVars[0]))
        print("valor 1: " + str(piVars[1]))
        print("valor 2: " + str(piVars[2]))
        print("valor 3: " + str(piVars[3]))
        print("valor alfa: " + str(alfa))
        
        self.assertEquals(piVars[0],0.0, "0.0 debe multiplicar la primera innognita")
        self.assertTrue(2.0 < piVars[1] and 2.1 > piVars[1],"2 debe multiplicar la primer incognita")
        self.assertTrue(-2.0 < piVars[2] and -1.9 > piVars[2] ,"-2 debe multiplicar la segunda incognita")
        self.assertEquals(piVars[3], 0.0, "0.0 debe multiplicar la cuarta innognita")
        self.assertTrue( 3.0 < alfa and 3.1 > alfa, "alfa debe ser 3")
        self.assertEqual(piVars[0], 0.0, "la dimension agregada no debe modificar la rectar ya que vale cero en todos los casos en el caso 3D")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()