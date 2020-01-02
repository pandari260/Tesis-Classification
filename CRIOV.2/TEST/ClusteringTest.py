'''
Created on 8 dic. 2019

@author: javier
'''
import unittest
from CRIO.Modelo.Cluster import Cluster,mergeClusters
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer
from CRIO.Clustering import containsOutlier,createDistanceGraph
from CRIO.Modelo.ClusterContainer import ClusterContainer
import networkx as nx
import matplotlib.pyplot as plt

def displayGraph(g):
    elarge = [(u, v) for (u, v, d) in g.edges(data=True) if d['weight'] > 0.5]
    esmall = [(u, v) for (u, v, d) in g.edges(data=True) if d['weight'] <= 0.5]
    
    pos = nx.spring_layout(g)  # positions for all nodes
    
    # nodes
    nx.draw_networkx_nodes(g, pos, node_size=700)
    
    # edges
    nx.draw_networkx_edges(g, pos, edgelist=elarge,
                           width=6)
    nx.draw_networkx_edges(g, pos, edgelist=esmall,
                           width=6, alpha=0.5, edge_color='b', style='dashed')
    labels = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
    
    # labels
    nx.draw_networkx_labels(g, pos, font_size=20, font_family='sans-serif')
    
    plt.axis('off')
    plt.show()

class Test(unittest.TestCase):

    """isMergeableTest"""
    def testIsMergeable2D(self):
        d = 2
        cluster_A = Cluster([(0.0,2.0),(0.0,4.0)], d)
        cluster_B = Cluster([(4.0,2.0),(4.0,4.0)], d)
        
        samples = SampleContainer([(6.0,3.0)],d) 
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(False, resul, "Dos clusters deberian ser mergeables si forman una componente convexa sin outliers")
        
        samples = SampleContainer([(2.3,3.0)],d)
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(True, resul, "Dos clusters no deberian ser mergeables si forman una componente convexa con outliers")        
        pass
    
    def testIsMergeable3D(self):
        
        d = 3
        cluster_A = Cluster([(3.0,2.0,0.0),(4.0,2.0,0.0),(4.0,1.0,0.0),(3.0,1.0,0.0)], d)
        cluster_B = Cluster([(3.0,5.0,0.0),(5.0,5.0,0.0),(4.0,6.0,0.0)], d)
        
        samples = SampleContainer([(7.0,5.0,0.0),(7.0,4.0,0.0)],d)
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(False, resul, "Dos clusters deberian ser mergeables si forman una componente convexa sin outliers en dimension %s" %(d))
        
        
        samples = SampleContainer([(4.0,4.0,0.0),(3.0,4.0,0.0),(5.0,4.0,0.0)], d)        
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(True, resul, "Dos clusters no deberian ser mergeables si forman una componente convexa con outliers en dimension %s" %(d)) 
        
        
    def testIsMergeable4D(self):
        
        d = 4
        cluster_A = Cluster([(0.0,3.0,2.0,0.0),(0.0,4.0,2.0,0.0),(0.0,4.0,1.0,0.0),(0.0,3.0,1.0,0.0)], d)
        cluster_B = Cluster([(0.0,3.0,5.0,0.0),(0.0,5.0,5.0,0.0),(0.0,4.0,6.0,0.0)], d)
        
        samples = SampleContainer([(0.0,7.0,5.0,0.0),(0.0,7.0,4.0,0.0)],d)
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(False, resul, "Dos clusters deberian ser mergeables si forman una componente convexa sin outliers en dimension %s" %(d))        
        
        samples = SampleContainer([(0.0,4.0,4.0,0.0),(0.0,3.0,4.0,0.0),(0.0,5.0,4.0,0.0)], d)      
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(True, resul, "Dos clusters no deberian ser mergeables si forman una componente convexa con outliers %s" %(d))
    
    def testIsMergeable5D(self):
        
        d = 5
        cluster_A = Cluster([(0.0,3.0,0.0,2.0,0.0),(0.0,4.0,0.0,2.0,0.0),(0.0,4.0,0.0,1.0,0.0),(0.0,3.0,0.0,1.0,0.0)], d)
        cluster_B = Cluster([(0.0,3.0,0.0,5.0,0.0),(0.0,5.0,0.0,5.0,0.0),(0.0,4.0,0.0,6.0,0.0)], d)
        
        samples = SampleContainer([(0.0,7.0,0.0,5.0,0.0),(0.0,7.0,0.0,4.0,0.0)],d)
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(False, resul, "Dos clusters deberian ser mergeables si forman una componente convexa sin outliers en dimension %s" %(d))        
        
        samples = SampleContainer([(0.0,4.0,0.0,4.0,0.0),(0.0,3.0,0.0,4.0,0.0),(0.0,5.0,0.0,4.0,0.0)], d)
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(True, resul, "Dos clusters no deberian ser mergeables si forman una componente convexa con outliers %s" %(d))
    
    def testisMergeableEmptyOutliers(self):
        
        d=2     
        cluster_A = Cluster([(0.0,2.0),(0.0,4.0)], d)
        cluster_B = Cluster([(4.0,2.0),(4.0,4.0)], d)
        samples = SampleContainer([],d)
        resul = containsOutlier(mergeClusters(cluster_A, cluster_B), samples)
        self.assertEqual(False, resul, "Dos clusters deberian ser mergeables si no hay otras muestras")
    
    """createDistanceGraph"""
    
    def test_createDistanceGraph_2D(self):
        d = 2
        c1 = Cluster([(2.0,6.0)], d)
        c2 = Cluster([(2.0,2.0)], d)
        c3 = Cluster([(5.0,6.0)], d)
        c4 = Cluster([(5.0,2.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        
        self.assertEquals(g.get_edge_data(c1, c2)['weight'],4.0,"la distancia debe ser 4")
        self.assertEquals(g.get_edge_data(c1, c3)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c1, c4)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c3)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c4)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c3, c4)['weight'],4.0,"la distancia debe ser 4")  
    
    def test_createDistanceGraph_3D(self):
        d = 3
        c1 = Cluster([(2.0,6.0,0.0)], d)
        c2 = Cluster([(2.0,2.0,0.0)], d)
        c3 = Cluster([(5.0,6.0,0.0)], d)
        c4 = Cluster([(5.0,2.0,0.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        
        self.assertEquals(g.get_edge_data(c1, c2)['weight'],4.0,"la distancia debe ser 4")
        self.assertEquals(g.get_edge_data(c1, c3)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c1, c4)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c3)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c4)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c3, c4)['weight'],4.0,"la distancia debe ser 4")  
    
    def test_createDistanceGraph_4D(self):
        d = 4
        c1 = Cluster([(2.0,6.0,0.0,0.0)], d)
        c2 = Cluster([(2.0,2.0,0.0,0.0)], d)
        c3 = Cluster([(5.0,6.0,0.0,0.0)], d)
        c4 = Cluster([(5.0,2.0,0.0,0.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        
        self.assertEquals(g.get_edge_data(c1, c2)['weight'],4.0,"la distancia debe ser 4")
        self.assertEquals(g.get_edge_data(c1, c3)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c1, c4)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c3)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c4)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c3, c4)['weight'],4.0,"la distancia debe ser 4")  

    def test_createDistanceGraph_severalSamplesInClusters_2D(self):
        d = 2
        c1 = Cluster([(1.0,7.0),(3.0,7.0),(1.0,5.0),(3.0,5.0)], d)
        c3 = Cluster([(4.0,7.0),(6.0,5.0),(6.0,7.0),(4.0,5.0)], d)
        c2 = Cluster([(1.0,3.0),(3.0,3.0),(1.0,1.0),(3.0,1.0)], d)
        c4 = Cluster([(4.0,3.0),(4.0,1.0),(6.0,1.0),(6.0,3.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        
        print(g.get_edge_data(c1, c2)['weight'])
        self.assertEquals(g.get_edge_data(c1, c2)['weight'],4.0,"la distancia debe ser 4")
        self.assertEquals(g.get_edge_data(c1, c3)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c1, c4)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c3)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c4)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c3, c4)['weight'],4.0,"la distancia debe ser 4")
        
    def test_createDistanceGraph_severalSamplesInClusters_3D(self):
        d = 3
        c1 = Cluster([(1.0,7.0,0.0),(3.0,7.0,0.0),(1.0,5.0,0.0),(3.0,5.0,0.0)], d)
        c3 = Cluster([(4.0,7.0,0.0),(6.0,5.0,0.0),(6.0,7.0,0.0),(4.0,5.0,0.0)], d)
        c2 = Cluster([(1.0,3.0,0.0),(3.0,3.0,0.0),(1.0,1.0,0.0),(3.0,1.0,0.0)], d)
        c4 = Cluster([(4.0,3.0,0.0),(4.0,1.0,0.0),(6.0,1.0,0.0),(6.0,3.0,0.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        
        print(g.get_edge_data(c1, c2)['weight'])
        self.assertEquals(g.get_edge_data(c1, c2)['weight'],4.0,"la distancia debe ser 4")
        self.assertEquals(g.get_edge_data(c1, c3)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c1, c4)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c3)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c4)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c3, c4)['weight'],4.0,"la distancia debe ser 4")

    def test_createDistanceGraph_severalSamplesInClusters_4D(self):
        d = 4
        c1 = Cluster([(1.0,7.0,0.0,0.0),(3.0,7.0,0.0,0.0),(1.0,5.0,0.0,0.0),(3.0,5.0,0.0,0.0)], d)
        c3 = Cluster([(4.0,7.0,0.0,0.0),(6.0,5.0,0.0,0.0),(6.0,7.0,0.0,0.0),(4.0,5.0,0.0,0.0)], d)
        c2 = Cluster([(1.0,3.0,0.0,0.0),(3.0,3.0,0.0,0.0),(1.0,1.0,0.0,0.0),(3.0,1.0,0.0,0.0)], d)
        c4 = Cluster([(4.0,3.0,0.0,0.0),(4.0,1.0,0.0,0.0),(6.0,1.0,0.0,0.0),(6.0,3.0,0.0,0.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        
        print(g.get_edge_data(c1, c2)['weight'])
        self.assertEquals(g.get_edge_data(c1, c2)['weight'],4.0,"la distancia debe ser 4")
        self.assertEquals(g.get_edge_data(c1, c3)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c1, c4)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c3)['weight'],5.0,"la distancia debe ser 5") 
        self.assertEquals(g.get_edge_data(c2, c4)['weight'],3.0,"la distancia debe ser 3") 
        self.assertEquals(g.get_edge_data(c3, c4)['weight'],4.0,"la distancia debe ser 4")
    
   
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()