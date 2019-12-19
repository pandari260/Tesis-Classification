'''
Created on 17 dic. 2019

@author: javier
'''
import unittest
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.Group import Group
from CRIO.Regionalization import assingGroupsToRegions


class RegionalizationTest(unittest.TestCase):


    def test_assingGroupsToRegions_trivial_2D(self):
        d = 2
        cluster = Cluster([(7.0,4.0)],d)
        group = Group([(5.0,4.0)],d)
        
        (piVars,alfa) = assingGroupsToRegions(group, cluster)
        print("feature 0:  " + str(piVars[0]))
        print("feature 1:  " + str(piVars[1]))
        print("alfa: " + str(alfa))

        self.assertTrue(0.99999995001 > piVars[0] and 0.99999995000 < piVars[0],"0.99999995001 debe multiplicar la primer incognita")
        self.assertEquals(0.0, piVars[1] ,"0.00014182033481 debe multiplicar la segunda incognita")
        self.assertTrue(5.99999970006 > alfa and 5.99999970005 < alfa, "alfa debe ser 6.0005669814")
    
    def test_assingGroupsToRegions_severalSamples_2D(self):
        d = 2
        cluster = Cluster([(6.5,4.5),(8.0,5.0),(9.0,5.0),(7.0,3.0),(8.0,4.0),(7.0,5.0)],d)
        group = Group([(5.0,4.0),(5.0,5.0),(6.0,5.0),(5.0,6.0),(4.0,6.0)],d)
        (piVars,alfa) = assingGroupsToRegions(group, cluster)
        print("feature 0:  " + str(piVars[0]))
        print("feature 1:  " + str(piVars[1]))
        print("alfa: " + str(alfa))

        self.assertTrue(2.0 < piVars[0] and 2.1 > piVars[0],"0.99999995001 debe multiplicar la primer incognita")
        self.assertTrue(-2.0 < piVars[1] and -1.9 > piVars[1] ,"0.00014182033481 debe multiplicar la segunda incognita")
        self.assertTrue( 3.0 < alfa and 3.1 > alfa, "alfa debe ser 6.0005669814")
    
    def test_assingGroupsToRegions_trivial_3D(self):
        d = 3
        cluster = Cluster([(7.0,4.0,0.0)],d)
        group = Group([(5.0,4.0,0.0)],d)
        
        (piVars,alfa) = assingGroupsToRegions(group, cluster)
        print("feature 0:  " + str(piVars[0]))
        print("feature 1:  " + str(piVars[1]))
        print("feature 2:  " + str(piVars[2]))

    
        print("alfa: " + str(alfa))
        self.assertTrue(0.99999995001 < piVars[0] and 0.99999995002 > piVars[0],"0.99999995001 debe multiplicar la primer incognita")
        self.assertEqual(0.0, piVars[1] ,"0.00014182033481 debe multiplicar la segunda incognita")
        self.assertEqual(0.0,piVars[2],"cero debe multiplicar a la tercera incognita")
        self.assertTrue(5.99999970006 < alfa and 5.99999970007 > alfa, "alfa debe ser 6.0005669814")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()