'''
Created on 12 dic. 2019

@author: javier
'''
import unittest
from CRIO.Modelo.ClusterContainer import ClusterContainer
from CRIO.Modelo.Cluster import Cluster
from CRIO.Grouping import assignClustersToGroups
from CRIO.Modelo.Sample import Sample

def getGroup(dic, cluster, num_groups):
    ret = -1
    for i in range(num_groups):
        #print("valor de diccionario: "  + str(dic[(i,cluster)]) + " Valor de guarda: " + str(dic[(i,cluster)] > 0.99) + " tipo de dato " + str(type(dic[(i,cluster)])))
        if dic[(i,cluster)] > 0.9:
            #print("entro con %s%s" %(i,cluster) + "con el valor de: "  + str(dic[(i,cluster)]))
            ret = i
        #if dic[(i,cluster)] != 0 and dic[(i,cluster)] != 1:
            #print("resultado de la suma de " + str(dic[(i,cluster)]) + " mas 1 es: " + str(dic[(i,cluster)] + 1)) 
    return ret

def usedGroups(num_groups, clusters1, a):
    used_groups = []
    for c in clusters1.getClusters():
        used_groups.append(getGroup(a, c, num_groups))
    return set(used_groups)

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
        
        used_groups = usedGroups(num_groups, clusters1, a)
                    
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
        
        used_groups = usedGroups(num_groups, clusters1, a)
                    
        self.assertEqual(len(used_groups),clusters1.getSize() ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
        pass

    def test_assignClustersToGroups_DetectOutlierClass0_2D(self):
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
    
    def test_assingClustersToGroups_DestectOutlierClass1_2D(self):
        
        d= 2
        num_groups= 1
        
        cls0_0 = Cluster([(6.0,5.0),(6.0,3.0),(3.0,5.0)], d)
        cls0_1 = Cluster([(4.0,3.0)], d)
        clusters0 = ClusterContainer([cls0_0,cls0_1],d)
        
        s1 = Sample((4.28,3.09))
        s2 = Sample((11.0,10.0)) 
        s3 = Sample((11.0,11.0))
        s4 = Sample((12.0,11.0))
        s5 = Sample((12.0,11.0))
        
        cls1_0 = Cluster([s1], d)
        cls1_1 = Cluster([s2,s3,s4,s5], d)
        clusters1 = ClusterContainer([cls1_0,cls1_1],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertTrue(e1[s1] > 1, "la muestra outlier debe ser detectada")
        self.assertTrue(e1[s2] == 0, "la muestra no debe ser detectada como outlier")
        self.assertTrue(e1[s3] == 0, "la muestra no debe ser detectada como outlier")
        self.assertTrue(e1[s4] == 0, "la muestra no debe ser detectada como outlier")
        self.assertTrue(e1[s5] == 0, "la muestra no debe ser detectada como outlier")
        
        self.assertEqual(getGroup(a,cls1_1,num_groups), 0, "el cluster 1 debe estar en el unico grupo definido")
    
    def test_assingClustersToGroups_CombineClusteres_2D(self):
        d = 2
        num_groups = 2
        
        cls0_1 = Cluster([(6.0,5.0),(7.0,5.0)], d)
        clusters0 = ClusterContainer([cls0_1],d)
        
        cls1_1 = Cluster([(3.0,7.0),(4.0,7.0),(3.0,6.0)], d)
        cls1_2 = Cluster([(9.0,7.0),(10.0,7.0),(10.0,6.0)], d)
        cls1_3 = Cluster([(6.5,4.5)], d)
        clusters1= ClusterContainer([cls1_1,cls1_2,cls1_3],d)
        
        
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        

        self.assertEqual(e0.values(), [0.0,0.0], "ninguno cluster de clase 0 deberia tener outlier ya que es posible combinar dos cluster de clase 1")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguno cluster de clase 1 deberia tener outlier ya que es posible combinar dos cluster de clase 1")
        
        for c in clusters1.getClusters():
            self.assertTrue(getGroup(a,c,num_groups) > -1,"todos los clusters deben tener un grupo asignado")
        
        used_groups = usedGroups(num_groups, clusters1, a)
            
        self.assertEqual(len(used_groups),num_groups ,"Debe haver dos clusters asigndos al mismo grupo")
        self.assertEqual(getGroup(a,cls1_1,num_groups), getGroup(a,cls1_2,num_groups),"estos dos cluster deben estar en el mismo grupo")
        
    def test_assignClustersToGroups_SameNumberOfGroupssAndClusters2D_SeveralClusters(self):
        
        d = 2
        num_groups = 5
        
        cls0_1 = Cluster([(5.0,9.0),(8.0,8.0),(6.0,6.0)], d)
        cls0_2 = Cluster([(4.0,12.0),(2.0,10.0)], d)
        cls0_3 = Cluster([(6.0,16.0),(5.0,16.0)], d)
        
        
        cls1_1 = Cluster([(3.0,7.0),(4.0,7.0),(3.0,8.0)],d)
        cls1_2 = Cluster([(6.0,11.0),(7.0,11.0),(7.0,10.0)],d)
        cls1_3 = Cluster([(9.0,5.0),(9.0,6.0),(8.0,5.0)], d)
        cls1_4 = Cluster([(1.0,13.0),(2.0,13.0),(1.0,12.0)], d)
        cls1_5 = Cluster([(6.0,17.0),(5.0,17.0)],d)
        
        clusters0 = ClusterContainer([cls0_1,cls0_2,cls0_3],d)
        clusters1 = ClusterContainer([cls1_1,cls1_2,cls1_3,cls1_4,cls1_5],d)
        
       
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        
        used_groups = usedGroups(num_groups, clusters1, a)
            
        self.assertEqual(len(used_groups),num_groups ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
    
    def test_assignClustersToGroups_MoreNumberOfGroupssThanClusters2D_SeveralClusters(self):
        
        d = 2
        num_groups = 10
        
        cls0_1 = Cluster([(5.0,9.0),(8.0,8.0),(6.0,6.0)], d)
        cls0_2 = Cluster([(4.0,12.0),(2.0,10.0)], d)
        cls0_3 = Cluster([(6.0,16.0),(5.0,16.0)], d)
        
        
        cls1_1 = Cluster([(3.0,7.0),(4.0,7.0),(3.0,8.0)],d)
        cls1_2 = Cluster([(6.0,11.0),(7.0,11.0),(7.0,10.0)],d)
        cls1_3 = Cluster([(9.0,5.0),(9.0,6.0),(8.0,5.0)], d)
        cls1_4 = Cluster([(1.0,13.0),(2.0,13.0),(1.0,12.0)], d)
        cls1_5 = Cluster([(6.0,17.0),(5.0,17.0)],d)
        
        clusters0 = ClusterContainer([cls0_1,cls0_2,cls0_3],d)
        clusters1 = ClusterContainer([cls1_1,cls1_2,cls1_3,cls1_4,cls1_5],d)
        
       
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        
        used_groups = usedGroups(num_groups, clusters1, a)
            
        self.assertEqual(len(used_groups),clusters1.getSize() ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
    
    def test_assingClustersToGroups_CombineClusteres_SeveralClusters(self):
        d = 2
        num_groups = 4
        
        cls0_1 = Cluster([(6.0,5.0),(7.0,5.0)], d)
        cls0_2 = Cluster([(3.0,4.0),(6.0,4.0),(7.0,4.0),(10.0,4.0)],d)
        cls0_3 = Cluster([(3.0,9.0),(10.0,9.0),(7.0,9.0),(6.0,9.0)], d)
        clusters0 = ClusterContainer([cls0_1,cls0_2,cls0_3],d)
        
        cls1_1 = Cluster([(3.0,7.0),(4.0,7.0),(3.0,6.0)], d)
        cls1_2 = Cluster([(9.0,7.0),(10.0,7.0),(10.0,6.0)], d)
        cls1_3 = Cluster([(6.5,4.5)], d)
        cls1_4 = Cluster([(3.0,2.0),(4.0,2.0),(3.0,3.0)], d)
        cls1_5 = Cluster([(10.0,2.0),(10.0,3.0),(9.0,2.0)], d)
        cls1_6 = Cluster([(3.0,12.0),(4.0,12.0),(3.0,11.0)], d)
        cls1_7 = Cluster([(10.0,12.0),(9.0,12.0),(10.0,11.0)], d)
        clusters1= ClusterContainer([cls1_1,cls1_2,cls1_3,cls1_4,cls1_5,cls1_6,cls1_7],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        

        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        

        for c in clusters1.getClusters():
            #print("")
            #print("trabajando con: " + str(c))
            #print("el grupo asginado  a: " + str(c)+ " es: " + str(getGroup(a,c,num_groups)))
            self.assertTrue(getGroup(a,c,num_groups) > -1,"todos los clusters deben tener un grupo asignado")
        #print("")
        used_groups = usedGroups(num_groups, clusters1, a)
            #
        #print("grupos usados:" + str(used_groups))
        self.assertEqual(len(used_groups),num_groups ,"Debe haver 3 grupos con dos clusters")
        self.assertEqual(getGroup(a,cls1_1,num_groups), getGroup(a,cls1_2,num_groups), "el cls1_1 debe estar en el mismo grupo que el cls1_2")
        self.assertEqual(getGroup(a,cls1_4,num_groups), getGroup(a,cls1_5,num_groups), "el cls1_1 debe estar en el mismo grupo que el cls1_2")
        self.assertEqual(getGroup(a,cls1_6,num_groups), getGroup(a,cls1_7,num_groups), "el cls1_1 debe estar en el mismo grupo que el cls1_2")
        #self.assertTrue(False)

    def test_assignClustersToGroups_SameNumberOfGroupssAndClusters3D(self):   
        
        d = 3
        num_groups = 2

        clusters1 = ClusterContainer([Cluster([(2.0,5.0,0.0),(3.0,6.0,0.0),(2.0,6.0,0.0)],d),Cluster([(7.0,2.0,0.0),(8.0,1.0,0.0),(8.0,2.0,0.0),(7.0,1.0,0.0)],d)],d)
        clusters0 = ClusterContainer([Cluster([(4.0,4.0,0.0),(5.0,4.0,0.0),(4.0,3.0,0.0),(5.0,3.0,0.0)],d)],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        
        used_groups = usedGroups(num_groups, clusters1, a)
                    
        self.assertEqual(len(used_groups),num_groups ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
        pass
        
    def test_assignClustersToGroups_MoreNumberOfGroupsThanGroups3D(self):      
        
            
        d = 3
        num_groups = 4

        clusters1 = ClusterContainer([Cluster([(2.0,5.0,0.0),(3.0,6.0,0.0),(2.0,6.0,0.0)],d),Cluster([(7.0,2.0,0.0),(8.0,1.0,0.0),(8.0,2.0,0.0),(7.0,1.0,0.0)],d)],d)
        clusters0 = ClusterContainer([Cluster([(4.0,4.0,0.0),(5.0,4.0,0.0),(4.0,3.0,0.0),(5.0,3.0,0.0)],d)],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 1 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        
        used_groups = usedGroups(num_groups, clusters1, a)
                    
        self.assertEqual(len(used_groups),clusters1.getSize() ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
        pass
    
    def test_assignClustersToGroups_DetectOutlierClass03D(self):
        d = 3
        num_groups = 2
        
        s1 = Sample((5.0,7.0,0.0))
        s2 = Sample((8.0,4.0,0.0))
        s3 = Sample((5.0,4.0,0.0))
        clusters0 = ClusterContainer([Cluster([s1,s2,s3],d)],d)

        c1 = Cluster([(3.0,5.0,0.0),(4.0,6.0,0.0)], d)
        c2 = Cluster([(6.0,2.0,0.0),(7.0,3.0,0.0)], d)
        c3 = Cluster([(7.0,9.0,0.0),(10.0,6.0,0.0)],d)      
        clusters1 = ClusterContainer([c1,c2,c3],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0[s1], 0.0)
        self.assertEqual(e0[s2], 0.0)
        self.assertTrue(e0[s3] > 1.0, "Una de las muestras de clase 0 deberia ser reconosida como outlier si la cantidad de grupos es menor a la cantidad de clusters")

        
        self.assertEqual(getGroup(a,c1,num_groups), getGroup(a,c2,num_groups), "Dos clusters deben pertenercer al mismo grupo si la cantidad de grupos es menor a la catidad de clusters")
        self.assertNotEqual(getGroup(a,c1,num_groups), getGroup(a,c3,num_groups))
    
    def test_assingClustersToGroups_DestectOutlierClass1_3D(self):
        
        d= 3
        num_groups= 1
        
        cls0_0 = Cluster([(6.0,5.0,0.0),(6.0,3.0,0.0),(3.0,5.0,0.0)], d)
        cls0_1 = Cluster([(4.0,3.0,0.0)], d)
        clusters0 = ClusterContainer([cls0_0,cls0_1],d)
        
        s1 = Sample((4.28,3.09,0.0))
        s2 = Sample((11.0,10.0,0.0)) 
        s3 = Sample((11.0,11.0,0.0))
        s4 = Sample((12.0,11.0,0.0))
        s5 = Sample((12.0,11.0,0.0))
        
        cls1_0 = Cluster([s1], d)
        cls1_1 = Cluster([s2,s3,s4,s5], d)
        clusters1 = ClusterContainer([cls1_0,cls1_1],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertTrue(e1[s1] > 1, "la muestra outlier debe ser detectada")
        self.assertTrue(e1[s2] == 0, "la muestra no debe ser detectada como outlier")
        self.assertTrue(e1[s3] == 0, "la muestra no debe ser detectada como outlier")
        self.assertTrue(e1[s4] == 0, "la muestra no debe ser detectada como outlier")
        self.assertTrue(e1[s5] == 0, "la muestra no debe ser detectada como outlier")
        
        self.assertEqual(getGroup(a,cls1_1,num_groups), 0, "el cluster 1 debe estar en el unico grupo definido")

    def test_assingClustersToGroups_CombineClusteres_3D(self):
        d = 3
        num_groups = 2
        
        cls0_1 = Cluster([(6.0,5.0,0.0),(7.0,5.0,0.0)], d)
        clusters0 = ClusterContainer([cls0_1],d)
        
        cls1_1 = Cluster([(3.0,7.0,0.0),(4.0,7.0,0.0),(3.0,6.0,0.0)], d)
        cls1_2 = Cluster([(9.0,7.0,0.0),(10.0,7.0,0.0),(10.0,6.0,0.0)], d)
        cls1_3 = Cluster([(6.5,4.5,0.0)], d)
        clusters1= ClusterContainer([cls1_1,cls1_2,cls1_3],d)
        
        
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        

        self.assertEqual(e0.values(), [0.0,0.0], "ninguno cluster de clase 1 deberia tener outlier ya que es posible combinar dos cluster de clase 1")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguno cluster de clase 1 deberia tener outlier ya que es posible combinar dos cluster de clase 1")
        
        for c in clusters1.getClusters():
            self.assertTrue(getGroup(a,c,num_groups) > -1,"todos los clusters deben tener un grupo asignado")
        
        used_groups = usedGroups(num_groups, clusters1, a)
            
        self.assertEqual(len(used_groups),num_groups ,"Debe haver dos clusters asigndos al mismo grupo")
        self.assertEqual(getGroup(a,cls1_1,num_groups), getGroup(a,cls1_2,num_groups),"estos dos cluster deben estar en el mismo grupo")
        
    def test_assignClustersToGroups_SameNumberOfGroupssAndClusters2D_SeveralClusters_3D(self):
        
        d = 3
        num_groups = 5
        
        cls0_1 = Cluster([(5.0,9.0,0.0),(8.0,8.0,0.0),(6.0,6.0,0.0)], d)
        cls0_2 = Cluster([(4.0,12.0,0.0),(2.0,10.0,0.0)], d)
        cls0_3 = Cluster([(6.0,16.0,0.0),(5.0,16.0,0.0)], d)
        
        
        cls1_1 = Cluster([(3.0,7.0,0.0),(4.0,7.0,0.0),(3.0,8.0,0.0)],d)
        cls1_2 = Cluster([(6.0,11.0,0.0),(7.0,11.0,0.0),(7.0,10.0,0.0)],d)
        cls1_3 = Cluster([(9.0,5.0,0.0),(9.0,6.0,0.0),(8.0,5.0,0.0)], d)
        cls1_4 = Cluster([(1.0,13.0,0.0),(2.0,13.0,0.0),(1.0,12.0,0.0)], d)
        cls1_5 = Cluster([(6.0,17.0,0.0),(5.0,17.0,0.0)],d)
        
        clusters0 = ClusterContainer([cls0_1,cls0_2,cls0_3],d)
        clusters1 = ClusterContainer([cls1_1,cls1_2,cls1_3,cls1_4,cls1_5],d)
        
       
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        
        used_groups = usedGroups(num_groups, clusters1, a)
            
        self.assertEqual(len(used_groups),num_groups ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
    
    def test_assignClustersToGroups_MoreNumberOfGroupssThanClusters_3D_SeveralClusters(self):
        
        d = 3
        num_groups = 10
        
        cls0_1 = Cluster([(5.0,9.0,0.0),(8.0,8.0,0.0),(6.0,6.0,0.0)], d)
        cls0_2 = Cluster([(4.0,12.0,0.0),(2.0,10.0,0.0)], d)
        cls0_3 = Cluster([(6.0,16.0,0.0),(5.0,16.0,0.0)], d)
        
        
        cls1_1 = Cluster([(3.0,7.0,0.0),(4.0,7.0,0.0),(3.0,8.0,0.0)],d)
        cls1_2 = Cluster([(6.0,11.0,0.0),(7.0,11.0,0.0),(7.0,10.0,0.0)],d)
        cls1_3 = Cluster([(9.0,5.0,0.0),(9.0,6.0,0.0),(8.0,5.0,0.0)], d)
        cls1_4 = Cluster([(1.0,13.0,0.0),(2.0,13.0,0.0),(1.0,12.0,0.0)], d)
        cls1_5 = Cluster([(6.0,17.0,0.0),(5.0,17.0,0.0)],d)
        
        clusters0 = ClusterContainer([cls0_1,cls0_2,cls0_3],d)
        clusters1 = ClusterContainer([cls1_1,cls1_2,cls1_3,cls1_4,cls1_5],d)
        
       
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        
        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        
        used_groups = usedGroups(num_groups, clusters1, a)
            
        self.assertEqual(len(used_groups),clusters1.getSize() ,"todos los grupos deberian tener un cluster si la cantidad de clusters es igual a la cantidad de grupos")
    
    def test_assingClustersToGroups_CombineClusteres_SeveralClusters_3D(self):
        d = 3
        num_groups = 4
        
        cls0_1 = Cluster([(6.0,5.0,0.0),(7.0,5.0,0.0)], d)
        cls0_2 = Cluster([(3.0,4.0,0.0),(6.0,4.0,0.0),(7.0,4.0,0.0),(10.0,4.0,0.0)],d)
        cls0_3 = Cluster([(3.0,9.0,0.0),(10.0,9.0,0.0),(7.0,9.0,0.0),(6.0,9.0,0.0)], d)
        clusters0 = ClusterContainer([cls0_1,cls0_2,cls0_3],d)
        
        cls1_1 = Cluster([(3.0,7.0,0.0),(4.0,7.0,0.0),(3.0,6.0,0.0)], d)
        cls1_2 = Cluster([(9.0,7.0,0.0),(10.0,7.0,0.0),(10.0,6.0,0.0)], d)
        cls1_3 = Cluster([(6.5,4.5,0.0)], d)
        cls1_4 = Cluster([(3.0,2.0,0.0),(4.0,2.0,0.0),(3.0,3.0,0.0)], d)
        cls1_5 = Cluster([(10.0,2.0,0.0),(10.0,3.0,0.0),(9.0,2.0,0.0)], d)
        cls1_6 = Cluster([(3.0,12.0,0.0),(4.0,12.0,0.0),(3.0,11.0,0.0)], d)
        cls1_7 = Cluster([(10.0,12.0,0.0),(9.0,12.0,0.0),(10.0,11.0,0.0)], d)
        clusters1= ClusterContainer([cls1_1,cls1_2,cls1_3,cls1_4,cls1_5,cls1_6,cls1_7],d)
        
        (a,e0,e1) = assignClustersToGroups(clusters0, clusters1, num_groups)
        

        self.assertEqual(e0.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        self.assertEqual(e1.values(), [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0], "ninguna muestra de clase 0 deberia ser outlier si la cantidad de cluster es igual a la cantidad de grupos")
        

        for c in clusters1.getClusters():
            #print("")
            #print("trabajando con: " + str(c))
            #print("el grupo asginado  a: " + str(c)+ " es: " + str(getGroup(a,c,num_groups)))
            self.assertTrue(getGroup(a,c,num_groups) > -1,"todos los clusters deben tener un grupo asignado")
        #print("")
        used_groups = usedGroups(num_groups, clusters1, a)
            #
        #print("grupos usados:" + str(used_groups))
        self.assertEqual(len(used_groups),num_groups ,"Debe haver 3 grupos con dos clusters")
        self.assertEqual(getGroup(a,cls1_1,num_groups), getGroup(a,cls1_2,num_groups), "el cls1_1 debe estar en el mismo grupo que el cls1_2")
        self.assertEqual(getGroup(a,cls1_4,num_groups), getGroup(a,cls1_5,num_groups), "el cls1_1 debe estar en el mismo grupo que el cls1_2")
        self.assertEqual(getGroup(a,cls1_6,num_groups), getGroup(a,cls1_7,num_groups), "el cls1_1 debe estar en el mismo grupo que el cls1_2")
        #self.assertTrue(False)
    
    
    
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()