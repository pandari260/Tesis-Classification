'''
Created on 15 ene. 2020

@author: javier
'''
import unittest
from CRIO.Modelo.Group import Group
from CRIO.Modelo.GroupContainer import GroupContainer


class GroupcontainerTest(unittest.TestCase):

    """equals: indica si dos group container son iguales"""
    
    def test_equals2D(self):
        d = 2
        d3 = 3
        g1 = Group([(0.0,0.0),(1.0,1.0)], d)
        g2 = Group([(1.0,1.0),(2.0,2.0)], d)
        
        container1 = GroupContainer(d)
        container1.addSamples(1, g1.getSamples())
        container1.addSamples(2, g2.getSamples())

        
        container2 = GroupContainer(d)
        container2.addSamples(1, g1.getSamples())
        container2.addSamples(2, g2.getSamples())

        container3 = GroupContainer(d)
        container3.addSamples(1, g1.getSamples())
        
        container4 = GroupContainer(d3)
        container4.addSamples(1, g1.getSamples())
        
        
        self.assertEqual(container1, container2, "el container 1 y 2 deben ser iguales")
        self.assertNotEquals(container1, container3, "el container 1 y 3 deberia ser distintos")
        self.assertNotEquals(container3, container4, "los container no son de la misma dimension")
        
    def test_equals3D(self):
        d = 3
        d4 = 4
        g1 = Group([(0.0,0.0,0.0),(1.0,1.0,0.0)], d)
        g2 = Group([(1.0,1.0,0.0),(2.0,2.0,0.0)], d)
        
        container1 = GroupContainer(d)
        container1.addSamples(1, g1.getSamples())
        container1.addSamples(2, g2.getSamples())

        
        container2 = GroupContainer(d)
        container2.addSamples(1, g1.getSamples())
        container2.addSamples(2, g2.getSamples())

        container3 = GroupContainer(d)
        container3.addSamples(1, g1.getSamples())
        
        container4 = GroupContainer(d4)
        container4.addSamples(1, g1.getSamples())
        
        
        self.assertEqual(container1, container2, "el container 1 y 2 deben ser iguales")
        self.assertNotEquals(container1, container3, "el container 1 y 3 deberia ser distintos")
        self.assertNotEquals(container3, container4, "los container no son de la misma dimension")
    
    def test_equals4D(self):
        d = 4
        d4 = 3
        g1 = Group([(0.0,0.0,0.0,0.0),(1.0,1.0,0.0,0.0)], d)
        g2 = Group([(1.0,1.0,0.0,0.0),(2.0,2.0,0.0,0.0)], d)
        
        container1 = GroupContainer(d)
        container1.addSamples(1, g1.getSamples())
        container1.addSamples(2, g2.getSamples())

        
        container2 = GroupContainer(d)
        container2.addSamples(1, g1.getSamples())
        container2.addSamples(2, g2.getSamples())

        container3 = GroupContainer(d)
        container3.addSamples(1, g1.getSamples())
        
        container4 = GroupContainer(d4)
        container4.addSamples(1, g1.getSamples())
        
        
        self.assertEqual(container1, container2, "el container 1 y 2 deben ser iguales")
        self.assertNotEquals(container1, container3, "el container 1 y 3 deberia ser distintos")
        self.assertNotEquals(container3, container4, "los container no son de la misma dimension")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()