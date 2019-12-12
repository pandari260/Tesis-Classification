'''
Created on 12 dic. 2019

@author: javier
'''
import unittest
from CRIO.Modelo.SampleContainer import SampleContainer
from CRIO.Modelo.ClusterContainer import ClusterContainer
from CRIO.Modelo.Cluster import Cluster
from CRIO.Grouping import assignClustersToGroups
from CRIO.Modelo.Sample import Sample
from posix import getgroups

def getGroup(dic, cluster, num_groups):
            ret = 0
            for i in range(num_groups):
                if dic[(i,cluster)] == 1.0:
                    ret = i
            return ret

class ClusteringTest(unittest.TestCase):

    """asigna uno de k grupos a cada cluster de clase 1. Todos los ClusterContainer y SampleContainer deben tener el mismo valor de dimension. k y d deben ser al menos 1."
    firma: assignClustersToGroups:(samples0:SampleContainer, sample1:SampleContainer, clusters0: ClusterContainer, cluster1:ClusterContainer, k:Integer,d: Integer)"""

    def test_assignClustersToGroups_SameNumberOfGroupssAndClusters2D(self):      
        
            
        d = 2
        num_groups = 2

        clusters1 = ClusterContainer([Cluster([(2.0,5.0),(3.0,6.0),(2.0,6.0)],d),Cluster([(7.0,2.0),(8.0,1.0),(8.0,2.0),(7.0,1.0)],d)],d)
        clusters0 = ClusterContainer([Cluster([(4.0,4.0),(5.0,4.0),(4.0,3.0),(5.0,3.0)],d)],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        
        used_groups = []
        for c in clusters1.getClusters():
            used_groups.append(getGroup(a,c,num_groups))
                    
        self.assertEqual(len(used_groups),num_groups ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
        pass
    
    def test_assignClustersToGroups_MoreNumberOfGroupsThanGroups2D(self):      
        
            
        d = 2
        num_groups = 4

        clusters1 = ClusterContainer([Cluster([(2.0,5.0),(3.0,6.0),(2.0,6.0)],d),Cluster([(7.0,2.0),(8.0,1.0),(8.0,2.0),(7.0,1.0)],d)],d)
        clusters0 = ClusterContainer([Cluster([(4.0,4.0),(5.0,4.0),(4.0,3.0),(5.0,3.0)],d)],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        
        used_groups = []
        for c in clusters1.getClusters():
            used_groups.append(getGroup(a,c,num_groups))
        
                    
        self.assertEqual(len(used_groups),clusters1.getSize() ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
        pass

    def test_assignClustersToGroups_DetectOutlier(self):
        d = 2
        num_groups = 2
        
        s1 = Sample((5.0,7.0))
        s2 = Sample((8.0,4.0))
        s3 = Sample((5.0,4.0))
        clusters0 = ClusterContainer([Cluster([s1,s2,s3],d)],d)

        c1 = Cluster([(3.0,5.0),(4.0,6.0)], d)
        c2 = Cluster([(6.0,2.0),(7.0,3.0)], d)
        c3 = Cluster([(7.0,9.0),(10.0,6.0)],d)      
        clusters1 = ClusterContainer([c1,c2,c3],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0[s1], 0.0)
        self.assertEqual(e0[s2], 0.0)
        self.assertTrue(e0[s3] > 1.0, "Una de las muestras de clase 0 deberia ser reconisida como outlier si la cantidad de grupos es menor a la cantidad de clusters")
        
        self.assertEqual(getGroup(a,c1,num_groups), getGroup(a,c2,num_groups), "Dos clusters deben pertenercer al mismo grupo si la cantidad de grupos es menor a la catidad de clusters")
        self.assertNotEqual(getGroup(a,c1,num_groups), getGroup(a,c3,num_groups))
        
       
        
        
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()