'''
Created on 29 dic. 2019

@author: javier
'''
import unittest
from CRIO.Modelo.Region import Region
from CRIO.Modelo.Hyperplane import Hyperplane


class HiperplaneTest(unittest.TestCase):


    def test_isRedundat_onlyOneHyperplane_2d(self):
        d = 2
        h = Hyperplane([1.0,1.0],5)
        r = Region([(2.0,1.0),(2.0,2.0),(3.0,1.0),(3.0,2.0)],[h],d)
        
        resul = h.isRedundant(r)
        self.assertFalse(resul,"no puede ser redundante si no hay otro hiperplanos")
        pass
    
    def test_isRedundat_thereIsRedundant_2d(self):
        d = 2
        h1 = Hyperplane([1.0,1.0],5.5)
        h2 = Hyperplane([1.0,1.0],6.0)
        h3 = Hyperplane([1.0,1.0],7.0)

        r = Region([(2.0,1.0),(2.0,2.0),(3.0,1.0),(3.0,2.0)],[h1,h2,h3],d)
        
        
        self.assertFalse(h1.isRedundant(r),"el hiperplano x + y = 5.5 no es redundante")
        self.assertTrue(h2.isRedundant(r), "el hiperplano x + y = 6 es redundante por el hiperplano x 'y = 5.5")
        self.assertTrue(h3.isRedundant(r), "el hiperplano x + y = 7 es redundante por el hiperplano x 'y = 5.5")

        pass
    
    def test_isRedundant_thereIsNotRedundant_2d(self):
        d = 2
        h1 = Hyperplane([1.0,1.0],5.5)
        h2 = Hyperplane([2.0,1.0],6.0)
        h3 = Hyperplane([3.0,1.0],7.0)

        r = Region([(0.0,1.0),(1.0,2.0),(1.0,1.0)],[h1,h2,h3],d)
        
        
        self.assertFalse(h1.isRedundant(r),"el hiperplano x + y = 5.5 no es redundante")
        self.assertFalse(h2.isRedundant(r), "el hiperplano x + y = 6 es redundante por el hiperplano x 'y = 5.5")
        self.assertFalse(h3.isRedundant(r), "el hiperplano x + y = 7 es redundante por el hiperplano x 'y = 5.5")
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()