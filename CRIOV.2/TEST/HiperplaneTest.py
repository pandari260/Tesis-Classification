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
        r = Region([h],d)
        
        resul = h.isRedundant(r)
        self.assertFalse(resul,"no puede ser redundante si no hay otro hiperplanos")
        pass
    
    def test_isRedundat_thereIsRedundant_2d(self):
        d = 2
        h1 = Hyperplane([1.0,1.0],5.5)
        h2 = Hyperplane([1.0,1.0],6.0)
        h3 = Hyperplane([1.0,1.0],7.0)

        r = Region([h1,h2,h3],d)
        
        
        self.assertFalse(h1.isRedundant(r),"el hiperplano x + y = 5.5 no es redundante")
        self.assertTrue(h2.isRedundant(r), "el hiperplano x + y = 6 es redundante por el hiperplano x 'y = 5.5")
        self.assertTrue(h3.isRedundant(r), "el hiperplano x + y = 7 es redundante por el hiperplano x 'y = 5.5")

        pass
    
    def test_isRedundant_thereIsNotRedundant_2d(self):
        d = 2
        h1 = Hyperplane([1.0,1.0],5.5)
        h2 = Hyperplane([2.0,1.0],6.0)
        h3 = Hyperplane([3.0,1.0],7.0)

        r = Region([h1,h2,h3],d)
        
        
        self.assertFalse(h1.isRedundant(r),"el hiperplano x + y = 5.5 no es redundante")
        self.assertFalse(h2.isRedundant(r), "el hiperplano 2x + y = 6 no es redundante")
        self.assertFalse(h3.isRedundant(r), "el hiperplano 3x + y = 7 no es redundante")
    
    def test_isRedundat_onlyOneHyperplane_3d(self):
        d = 3
        h = Hyperplane([1.0,1.0,0.0],5)
        r = Region([h],d)
        
        resul = h.isRedundant(r)
        self.assertFalse(resul,"no puede ser redundante si no hay otro hiperplanos")
        pass
    
    def test_isRedundat_thereIsRedundant_3d(self):
        d = 3
        h1 = Hyperplane([1.0,1.0,0.0],5.5)
        h2 = Hyperplane([1.0,1.0,0.0],6.0)
        h3 = Hyperplane([1.0,1.0,0.0],7.0)

        r = Region([h1,h2,h3],d)
        
        
        self.assertFalse(h1.isRedundant(r),"el hiperplano x + y = 5.5 no es redundante")
        self.assertTrue(h2.isRedundant(r), "el hiperplano x + y = 6 es redundante por el hiperplano x 'y = 5.5")
        self.assertTrue(h3.isRedundant(r), "el hiperplano x + y = 7 es redundante por el hiperplano x 'y = 5.5")

        pass
    
    def test_isRedundant_thereIsNotRedundant_3d(self):
        d = 3
        h1 = Hyperplane([1.0,1.0,0.0],5.5)
        h2 = Hyperplane([2.0,1.0,0.0],6.0)
        h3 = Hyperplane([3.0,1.0,0.0],7.0)

        r = Region([h1,h2,h3],d)
        
        
        self.assertFalse(h1.isRedundant(r),"el hiperplano x + y = 5.5 no es redundante")
        self.assertFalse(h2.isRedundant(r), "el hiperplano 2x + y = 6 no es redundante")
        self.assertFalse(h3.isRedundant(r), "el hiperplano 3x + y = 7 no es redundante")
    
    def test_isRedundat_onlyOneHyperplane_4d(self):
        d = 4
        h = Hyperplane([0.0,1.0,1.0,0.0],5)
        r = Region([h],d)
        
        resul = h.isRedundant(r)
        self.assertFalse(resul,"no puede ser redundante si no hay otro hiperplanos")
        pass
    
    def test_isRedundat_thereIsRedundant_4d(self):
        d = 4
        h1 = Hyperplane([0.0,1.0,1.0,0.0],5.5)
        h2 = Hyperplane([0.0,1.0,1.0,0.0],6.0)
        h3 = Hyperplane([0.0,1.0,1.0,0.0],7.0)

        r = Region([h1,h2,h3],d)
        
        
        self.assertFalse(h1.isRedundant(r),"el hiperplano x + y = 5.5 no es redundante")
        self.assertTrue(h2.isRedundant(r), "el hiperplano x + y = 6 es redundante por el hiperplano x 'y = 5.5")
        self.assertTrue(h3.isRedundant(r), "el hiperplano x + y = 7 es redundante por el hiperplano x 'y = 5.5")

        pass
    
    def test_isRedundant_thereIsNotRedundant_4d(self):
        d = 4
        h1 = Hyperplane([0.0,1.0,1.0,0.0],5.5)
        h2 = Hyperplane([0.0,2.0,1.0,0.0],6.0)
        h3 = Hyperplane([0.0,3.0,1.0,0.0],7.0)

        r = Region([h1,h2,h3],d)
        
        
        self.assertFalse(h1.isRedundant(r),"el hiperplano x + y = 5.5 no es redundante")
        self.assertFalse(h2.isRedundant(r), "el hiperplano 2x + y = 6 no es redundante")
        self.assertFalse(h3.isRedundant(r), "el hiperplano 3x + y = 7 no es redundante")
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()