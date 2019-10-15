from CRIO.Importer import readSamples, listStringToFloat
import unittest


class Test(unittest.TestCase):


    def testreadSamplesSeveralDimention(self):
        route = "testFiles/class_2D"
        self.assertEquals([(1.0,1.0),(2.0,2.0),(3.0,3.0)], readSamples(route,2))
        
        route = "testFiles/class_3D"
        self.assertEquals([(1.0,1.0,1.0),(2.0,2.0,2.0),(3.0,3.0,3.0)], readSamples(route,3))
        
        route = "testFiles/class_4D"
        self.assertEquals([(1.0,1.0,1.0,1.0),(2.0,2.0,2.0,2.0),(3.0,3.0,3.0,3.0)], readSamples(route,4))
    
    def testlistStringToFloat(self):
        lista = ["0","1","2","3","4","5","6","7","8"]
        self.assertEquals([0,1,2,3,4,5,6,7,8], listStringToFloat(lista))
        
        
        
    
    
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testreadSamplesSeveralDimention']
    unittest.main()