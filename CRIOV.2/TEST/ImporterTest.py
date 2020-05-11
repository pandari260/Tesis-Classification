'''
Created on 8 mar. 2020

@author: javier
'''
import unittest
from CRIO.Importer import splitList, readSample


class Test(unittest.TestCase):

    
    #toma una lista de elementos y la separa en una lista de listas de acuerdo a una clave
    def testSplit(self):
        list = [1,2,3,4,5,0,1,1,1,0,1,1,0]
        key = 0
        self.assertEquals(splitList(list, key), [[1,2,3,4,5],[1,1,1],[1,1]])
        
        pass

    def test_importer_test(self):
        route = "splitfileTest.csv"
        c0,c1 = readSample(route)
        print c0
        print c1
        self.assertEquals(c0, [[(0.4737,1.6376),(0.9985,-0.7074)]])
        self.assertEquals(c1, [[(5.0659,-1.3678),(5.1683,0.3713)]])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSplit']
    unittest.main()