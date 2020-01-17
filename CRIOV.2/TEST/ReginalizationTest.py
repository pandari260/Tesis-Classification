'''
Created on 17 dic. 2019

@author: javier:v
'''
import unittest
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.Group import Group
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.Region import Region
from CRIO.Regionalization import defineHyperplane, createRegions
from CRIO.Modelo.GroupContainer import GroupContainer
from CRIO.Modelo.ClusterContainer import ClusterContainer


class RegionalizationTest(unittest.TestCase):


    def test_defineHyperplane_trivial_2D(self):
        d = 2
        cluster = Cluster([(7.0,4.0)],d)
        group = Group([(5.0,4.0)],d)
        
        hyperplane = defineHyperplane(group, cluster)
     

        self.assertTrue(0.99999995001 > hyperplane.getCoefficient(0) and 0.99999995000 < hyperplane.getCoefficient(0),"0.99999995001 debe multiplicar la primer incognita")
        self.assertEquals(0.0, hyperplane.getCoefficient(1) ,"0.0 debe multiplicar la segunda incognita")
        self.assertTrue(5.99999970006 > hyperplane.getIntercept() and 5.99999970005 < hyperplane.getIntercept(), "alfa debe ser 5.99999970006")
    
    def test_defineHyperplane_severalSamples_2D(self):
        d = 2
        cluster = Cluster([(6.5,4.5),(8.0,5.0),(9.0,5.0),(7.0,3.0),(8.0,4.0),(7.0,5.0)],d)
        group = Group([(5.0,4.0),(5.0,5.0),(6.0,5.0),(5.0,6.0),(4.0,6.0)],d)
        hyperplane = defineHyperplane(group, cluster)
      

        self.assertTrue(2.0 < hyperplane.getCoefficient(0) and 2.1 > hyperplane.getCoefficient(0),"2 debe multiplicar la primer incognita")
        self.assertTrue(-2.0 < hyperplane.getCoefficient(1) and -1.9 > hyperplane.getCoefficient(1) ,"-2 debe multiplicar la segunda incognita")
        self.assertTrue( 3.0 < hyperplane.getIntercept() and 3.1 > hyperplane.getIntercept(),"alfa debe ser 3")
    
    def test_defineHyperplane_trivial_3D(self):
        d = 3
        cluster = Cluster([(7.0,4.0,0.0)],d)
        group = Group([(5.0,4.0,0.0)],d)
        
        hyperplane = defineHyperplane(group, cluster)
       
    
        self.assertTrue(0.99999995001 < hyperplane.getCoefficient(0) and 0.99999995002 > hyperplane.getCoefficient(0),"0.99999995001 debe multiplicar la primer incognita")
        self.assertEqual(0.0, hyperplane.getCoefficient(1) ,"0.0 debe multiplicar la segunda incognita")
        self.assertEqual(0.0,hyperplane.getCoefficient(2),"cero debe multiplicar a la tercera incognita")
        self.assertTrue(5.99999970006 < hyperplane.getIntercept() and 5.99999970007 > hyperplane.getIntercept(), "alfa debe ser 5.99999970007")
    
    def test_defineHyperplane_severalSamples_3D(self):
        d = 3
        cluster = Cluster([(0.0,6.5,4.5),(0.0,8.0,5.0),(0.0,9.0,5.0),(0.0,7.0,3.0),(0.0,8.0,4.0),(0.0,7.0,5.0)],d)
        group = Group([(0.0,5.0,4.0),(0.0,5.0,5.0),(0.0,6.0,5.0),(0.0,5.0,6.0),(0.0,4.0,6.0)],d)
        hyperplane = defineHyperplane(group, cluster)
        
        self.assertEquals(hyperplane.getCoefficient(0),0.0, "0.0 debe multiplicar la primera innognita")
        self.assertTrue(2.0 < hyperplane.getCoefficient(1) and 2.1 > hyperplane.getCoefficient(1),"2 debe multiplicar la primer incognita")
        self.assertTrue(-2.0 < hyperplane.getCoefficient(2) and -1.9 > hyperplane.getCoefficient(2) ,"-2 debe multiplicar la segunda incognita")
        self.assertTrue( 3.0 < hyperplane.getIntercept() and 3.1 > hyperplane.getIntercept(), "alfa debe ser 3")

    def test_defineHyperplane_trivial_4D(self):
        d = 4
        cluster = Cluster([(7.0,4.0,0.0,0.0)],d)
        group = Group([(5.0,4.0,0.0,0.0)],d)
        
        hyperplane = defineHyperplane(group, cluster)

        

        self.assertTrue(0.999999950215 < hyperplane.getCoefficient(0) and 0.999999950216 > hyperplane.getCoefficient(0),"0.99999995001 debe multiplicar la primer incognita")
        self.assertEqual(0.0, hyperplane.getCoefficient(1) ,"0.0 debe multiplicar la segunda incognita")
        self.assertEqual(0.0,hyperplane.getCoefficient(2),"cero debe multiplicar a la tercera incognita")
        self.assertEqual(0.0,hyperplane.getCoefficient(3),"cero debe multiplicar a la cuarta incognita")
        self.assertTrue(5.9999997012 < hyperplane.getIntercept() and 5.9999997013 > hyperplane.getIntercept(), "alfa debe ser 5.99999970007")

    def test_defineHyperplane_severalSamples_4D(self):
        d = 4
        cluster = Cluster([(0.0,6.5,4.5,0.0),(0.0,8.0,5.0,0.0),(0.0,9.0,5.0,0.0),(0.0,7.0,3.0,0.0),(0.0,8.0,4.0,0.0),(0.0,7.0,5.0,0.0)],d)
        group = Group([(0.0,5.0,4.0,0.0),(0.0,5.0,5.0,0.0),(0.0,6.0,5.0,0.0),(0.0,5.0,6.0,0.0),(0.0,4.0,6.0,0.0)],d)
        hyperplane = defineHyperplane(group, cluster)
        
       
        
        self.assertEquals(hyperplane.getCoefficient(0),0.0, "0.0 debe multiplicar la primera innognita")
        self.assertTrue(2.0 < hyperplane.getCoefficient(1) and 2.1 > hyperplane.getCoefficient(1),"2 debe multiplicar la primer incognita")
        self.assertTrue(-2.0 < hyperplane.getCoefficient(2) and -1.9 > hyperplane.getCoefficient(2) ,"-2 debe multiplicar la segunda incognita")
        self.assertEquals(hyperplane.getCoefficient(3), 0.0, "0.0 debe multiplicar la cuarta innognita")
        self.assertTrue( 3.0 < hyperplane.getIntercept() and 3.1 > hyperplane.getIntercept(), "alfa debe ser 3")
    
    "crea un conjunto de regiones partir de un conjunto de grupos de clase 1 y "
    def test_createRegions_trivial2D(self):
        d = 2
        groups = GroupContainer(d)
        groups.addSamples(1,[Sample((5.0,4.0))])
        clusters = ClusterContainer([Cluster([(7.0,4.0)],d)],d)
        regions = createRegions(groups, clusters)
        hiperplanes = regions[0].getHyperplanes().pop()
        
        self.assertTrue(0.99999995001 > hiperplanes.getCoefficient(0) and 0.99999995000 < hiperplanes.getCoefficient(0),"0.99999995001 debe multiplicar la primer incognita")
        self.assertEquals(0.0,  hiperplanes.getCoefficient(1) ,"0.0 debe multiplicar la segunda incognita")
        self.assertTrue(5.99999970006 > hiperplanes.getIntercept() and 5.99999970005 < hiperplanes.getIntercept(), "alfa debe ser 5.99999970006")
    
    def test_createRegions_trivial3D(self):
        d = 3
        groups = GroupContainer(d)
        groups.addSamples(1,[Sample((5.0,4.0,0.0))])
        clusters = ClusterContainer([Cluster([(7.0,4.0,0.0)],d)],d)
        regions = createRegions(groups, clusters)
        hiperplanes = regions[0].getHyperplanes().pop()
        
        print(hiperplanes.getCoefficient(0))
        self.assertTrue(0.99999995001 < hiperplanes.getCoefficient(0) and 0.99999995002 > hiperplanes.getCoefficient(0),"0.99999995001 debe multiplicar la primer incognita")
        self.assertEquals(0.0,  hiperplanes.getCoefficient(1) ,"0.0 debe multiplicar la segunda incognita")
        self.assertEquals(0.0,  hiperplanes.getCoefficient(2) ,"0.0 debe multiplicar la tercera incognita")
        self.assertTrue(5.99999970006 < hiperplanes.getIntercept() and 5.99999970007 > hiperplanes.getIntercept(), "alfa debe ser 5.99999970006")
    
    def test_createRegions_trivial4D(self):
        d = 4
        groups = GroupContainer(d)
        groups.addSamples(1,[Sample((5.0,4.0,0.0,0.0))])
        clusters = ClusterContainer([Cluster([(7.0,4.0,0.0,0.0)],d)],d)
        regions = createRegions(groups, clusters)
        hiperplanes = regions[0].getHyperplanes().pop()
        
        print(hiperplanes.getIntercept())
        self.assertTrue(0.999999950215 < hiperplanes.getCoefficient(0) and 0.999999950216 > hiperplanes.getCoefficient(0),"0.99999995001 debe multiplicar la primer incognita")
        self.assertEquals(0.0,  hiperplanes.getCoefficient(1) ,"0.0 debe multiplicar la segunda incognita")
        self.assertTrue(5.9999997013 > hiperplanes.getIntercept() and 5.9999997012 < hiperplanes.getIntercept(), "alfa debe ser 5.9999997013")


        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()