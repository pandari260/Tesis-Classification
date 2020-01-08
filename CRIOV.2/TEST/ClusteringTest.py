'''
Created on 8 dic. 2019

@author: javier
'''
import unittest
from CRIO.Modelo.Cluster import Cluster,mergeClusters
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer
from CRIO.Clustering import containsOutlier,createDistanceGraph, minimumEdge,createClusters
from CRIO.Modelo.ClusterContainer import ClusterContainer
import networkx as nx
import matplotlib.pyplot as plt
from timeit import itertools

#getSamples
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
        
    def test_minimumDistance_trivial_2d(self):
        d = 2
        c1 = Cluster([(0.0,0.0)], d)
        c2 = Cluster([(1.0,0.0)], d)
        clusters = ClusterContainer([c1,c2],d)
        g = createDistanceGraph(clusters.getClusters())
        
        (u,v) = minimumEdge(g)
        self.assertEquals(g[u][v]['weight'], 1.0, "la minima arista tiene peso 1")
        
    def test_minimumDistance_trivial_3d(self):
        d = 3
        c1 = Cluster([(0.0,0.0,0.0)], d)
        c2 = Cluster([(1.0,0.0,0.0)], d)
        clusters = ClusterContainer([c1,c2],d)
        g = createDistanceGraph(clusters.getClusters())
        
        (u,v) = minimumEdge(g)
        self.assertEquals(g[u][v]['weight'], 1.0, "la minima arista tiene peso 1")
    
    def test_minimumDistance_trivial_4d(self):
        d = 4
        c1 = Cluster([(0.0,0.0,0.0,0.0)], d)
        c2 = Cluster([(1.0,0.0,0.0,0.0)], d)
        clusters = ClusterContainer([c1,c2],d)
        g = createDistanceGraph(clusters.getClusters())
        
        (u,v) = minimumEdge(g)
        self.assertEquals(g[u][v]['weight'], 1.0, "la minima arista tiene peso 1")
        

        
    def test_minimunDistanceOnlyOneSamplesForCluster_2D(self):
        d = 2
        c1 = Cluster([(2.0,6.0)], d)
        c2 = Cluster([(2.0,2.0)], d)
        c3 = Cluster([(5.0,6.0)], d)
        c4 = Cluster([(5.0,2.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        (u,v) = minimumEdge(g)
        self.assertEquals(g[u][v]['weight'], 3.0, "la minima arista tiene peso 3")
        
    def test_minimunDistanceOnlyOneSamplesForCluster_3D(self):
        d = 3
        c1 = Cluster([(2.0,6.0,0.0)], d)
        c2 = Cluster([(2.0,2.0,0.0)], d)
        c3 = Cluster([(5.0,6.0,0.0)], d)
        c4 = Cluster([(5.0,2.0,0.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        (u,v) = minimumEdge(g)
        self.assertEquals(g[u][v]['weight'], 3.0, "la minima arista tiene peso 3")
        
    def test_minimunDistanceOnlyOneSamplesForCluster_4D(self):
        d = 4
        c1 = Cluster([(2.0,6.0,0.0,0.0)], d)
        c2 = Cluster([(2.0,2.0,0.0,0.0)], d)
        c3 = Cluster([(5.0,6.0,0.0,0.0)], d)
        c4 = Cluster([(5.0,2.0,0.0,0.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        (u,v) = minimumEdge(g)
        self.assertEquals(g[u][v]['weight'], 3.0, "la minima arista tiene peso 3")
    
    def test_minimumDistance_severalSamplesInClusters_2D(self):
        d = 2
        c1 = Cluster([(1.0,7.0),(3.0,7.0),(1.0,5.0),(3.0,5.0)], d)
        c2 = Cluster([(1.0,3.0),(3.0,3.0),(1.0,1.0),(3.0,1.0)], d)
        c3 = Cluster([(4.0,7.0),(6.0,5.0),(6.0,7.0),(4.0,5.0)], d)
        c4 = Cluster([(4.0,3.0),(4.0,1.0),(6.0,1.0),(6.0,3.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        
        (u,v) = minimumEdge(g)
        self.assertEquals(g[u][v]['weight'], 3.0, "la minima arista tiene peso 3")
    
    def test_minimumDistance_severalSamplesInClusters_3D(self):
        d = 4
        c1 = Cluster([(1.0,7.0,0.0),(3.0,7.0,0.0),(1.0,5.0,0.0),(3.0,5.0,0.0)], d)
        c2 = Cluster([(1.0,3.0,0.0),(3.0,3.0,0.0),(1.0,1.0,0.0),(3.0,1.0,0.0)], d)
        c3 = Cluster([(4.0,7.0,0.0),(6.0,5.0,0.0),(6.0,7.0,0.0),(4.0,5.0,0.0)], d)
        c4 = Cluster([(4.0,3.0,0.0),(4.0,1.0,0.0),(6.0,1.0,0.0),(6.0,3.0,0.0)], d)
        clusters = ClusterContainer([c1,c2,c3,c4],d)
        g = createDistanceGraph(clusters.getClusters())
        
        (u,v) = minimumEdge(g)
        self.assertEquals(g[u][v]['weight'], 3.0, "la minima arista tiene peso 3")
    
    """ def test_createClusters_allSamplesInTheSameCluster_2D(self):
        d = 2
        s0_1,s0_2,s0_3 = Sample((3.0,3.0)),Sample((4.0,4.0)),Sample((3.0,4.0))
        s1_1,s1_2,s1_3,s1_4,s1_5,s1_6 = Sample((0.0,1.0)),Sample((0.0,2.0)),Sample((0.0,3.0)),Sample((1.0,0.0)),Sample((1.0,1.0)),Sample((1.0,2.0))
        
        class0 = SampleContainer([s0_1,s0_2,s0_3],d)
        class1 = SampleContainer([s1_1,s1_2,s1_3,s1_4,s1_5,s1_6],d)
        
        cluster = createClusters(class1, class0).getClusters().pop()
        
        for spl in class1.getSamples():
            self.assertTrue(spl in cluster.getSamples(), "la muestra " + str(spl) + "debe estar en el unico cluster")  
        
    def test_createClusters_allSamplesInTheSameCluster_3D(self):
        d = 3
        s0_1,s0_2,s0_3 = Sample((3.0,3.0,0.0)),Sample((4.0,4.0,0.0)),Sample((3.0,4.0,0.0))
        s1_1,s1_2,s1_3,s1_4,s1_5,s1_6 = Sample((0.0,1.0,0.0)),Sample((0.0,2.0,0.0)),Sample((0.0,3.0,0.0)),Sample((1.0,0.0,0.0)),Sample((1.0,1.0,0.0)),Sample((1.0,2.0,0.0))
        
        class0 = SampleContainer([s0_1,s0_2,s0_3],d)
        class1 = SampleContainer([s1_1,s1_2,s1_3,s1_4,s1_5,s1_6],d)
        
        cluster = createClusters(class1, class0).getClusters().pop()
        
        for spl in class1.getSamples():
            self.assertTrue(spl in cluster.getSamples(), "la muestra " + str(spl) + "debe estar en el unico cluster") 
    
    def test_createClusters_allSamplesInTheSameCluster_4D(self):
        d = 4
        s0_1,s0_2,s0_3 = Sample((0.0,3.0,3.0,0.0)),Sample((0.0,4.0,4.0,0.0)),Sample((0.0,3.0,4.0,0.0))
        s1_1,s1_2,s1_3,s1_4,s1_5,s1_6 = Sample((0.0,0.0,1.0,0.0)),Sample((0.0,0.0,2.0,0.0)),Sample((0.0,0.0,3.0,0.0)),Sample((0.0,1.0,0.0,0.0)),Sample((0.0,1.0,1.0,0.0)),Sample((0.0,1.0,2.0,0.0))
        
        class0 = SampleContainer([s0_1,s0_2,s0_3],d)
        class1 = SampleContainer([s1_1,s1_2,s1_3,s1_4,s1_5,s1_6],d)
        
        cluster = createClusters(class1, class0).getClusters().pop()
        
        for spl in class1.getSamples():
            self.assertTrue(spl in cluster.getSamples(), "la muestra " + str(spl) + "debe estar en el unico cluster")
        
    def test_DefineClusterNoneOutlierOnlyOneSample_2D(self):
        d = 2
        sA = Sample((0.0,0.0))
        classA = SampleContainer([sA],d)
        classB = SampleContainer([(4.0,0.0)], d)
        
        clusters = createClusters(classA, classB)
        
        self.assertEquals(clusters.getSize(), 1, "solo debe generarce un cluster")
        self.assertTrue(sA in clusters.getClusters().pop().getSamples())
        
    def test_DefineClusterNoneOutlierOnlyOneSample_3D(self):
        d = 3
        sA = Sample((0.0,0.0,0.0))
        classA = SampleContainer([sA],d)
        classB = SampleContainer([(4.0,0.0,0.0)], d)
        
        clusters = createClusters(classA, classB)
        
        self.assertEquals(clusters.getSize(), 1, "solo debe generarce un cluster")
        self.assertTrue(sA in clusters.getClusters().pop().getSamples())
        
    def test_DefineClusterNoneOutlierOnlyOneSample_4D(self):
        d = 4
        sA = Sample((0.0,0.0,0.0,0.0))
        classA = SampleContainer([sA],d)
        classB = SampleContainer([(0.0,4.0,0.0,0.0)], d)
        
        clusters = createClusters(classA, classB)
        
        self.assertEquals(clusters.getSize(), 1, "solo debe generarce un cluster")
        self.assertTrue(sA in clusters.getClusters().pop().getSamples())
        
    def test_onlyOneSampleForCluster_2D(self):
        d = 2
        s0_1,s0_2,s0_3,s0_4 = (0.0,2.0),(0.0,4.0),(0.0,6.0),(0.0,8.0)
        s1_1,s1_2,s1_3,s1_4 = (0.0,1.0),(0.0,3.0),(0.0,5.0),(0.0,7.0)        
        classA = SampleContainer([s1_1,s1_2,s1_3,s1_4],d)
        classB = SampleContainer([s0_1,s0_2,s0_3,s0_4],d)
        
        clusters = createClusters(classA, classB)
        
        self.assertEqual(clusters.getSize(), 4, "debe haver un cluster por cada muestra")
        for clstr in clusters.getClusters():
            self.assertEqual(clstr.getSize(), 1, "todos los cluster deben tener exactamente una muestra")
        
        for (c1,c2) in itertools.product(clusters.getClusters(),clusters.getClusters()):
            if c1 != c2:
                self.assertEquals(c1.getSamples().intersection(c2.getSamples()), set([]), "cada muestra debe estar en un cluster diferente")
    
    def test_onlyOneSampleForCluster_3D(self):
        d = 3
        s0_1,s0_2,s0_3,s0_4 = (0.0,2.0,0.0),(0.0,4.0,0.0),(0.0,6.0,0.0),(0.0,8.0,0.0)
        s1_1,s1_2,s1_3,s1_4 = (0.0,1.0,0.0),(0.0,3.0,0.0),(0.0,5.0,0.0),(0.0,7.0,0.0)        
        classA = SampleContainer([s1_1,s1_2,s1_3,s1_4],d)
        classB = SampleContainer([s0_1,s0_2,s0_3,s0_4],d)
        
        clusters = createClusters(classA, classB)
        
        self.assertEqual(clusters.getSize(), 4, "debe haver un cluster por cada muestra")
        for clstr in clusters.getClusters():
            self.assertEqual(clstr.getSize(), 1, "todos los cluster deben tener exactamente una muestra")
        
        for (c1,c2) in itertools.product(clusters.getClusters(),clusters.getClusters()):
            if c1 != c2:
                self.assertEquals(c1.getSamples().intersection(c2.getSamples()), set([]), "cada muestra debe estar en un cluster diferente")
               
    def test_onlyOneSampleForCluster_4D(self):
        d = 4
        s0_1,s0_2,s0_3,s0_4 = (0.0,0.0,2.0,0.0),(0.0,0.0,4.0,0.0),(0.0,0.0,6.0,0.0),(0.0,0.0,8.0,0.0)
        s1_1,s1_2,s1_3,s1_4 = (0.0,0.0,1.0,0.0),(0.0,0.0,3.0,0.0),(0.0,0.0,5.0,0.0),(0.0,0.0,7.0,0.0)        
        classA = SampleContainer([s1_1,s1_2,s1_3,s1_4],d)
        classB = SampleContainer([s0_1,s0_2,s0_3,s0_4],d)
        
        clusters = createClusters(classA, classB)
        
        self.assertEqual(clusters.getSize(), 4, "debe haver un cluster por cada muestra")
        for clstr in clusters.getClusters():
            self.assertEqual(clstr.getSize(), 1, "todos los cluster deben tener exactamente una muestra")
        
        for (c1,c2) in itertools.product(clusters.getClusters(),clusters.getClusters()):
            if c1 != c2:
                self.assertEquals(c1.getSamples().intersection(c2.getSamples()), set([]), "cada muestra debe estar en un cluster diferente")
    
    def test_onlyOneOutlier_2D(self):
        d = 2
        classA = SampleContainer([(0.0,0.0),(0.0,1.0),(0.0,2.0),(0.0,3.0)],d)
        classB = SampleContainer([(0.0,1.5)],d)
        clusters = createClusters(classA, classB)
        #print("cantidad de clusters: " + str(clusters.getSize()))
        #self.assertEquals(clusters.getSize(), 2, "deben generarce dos clusters")
        cls1 = clusters.getClusters().pop()
        cls2 = clusters.getClusters().pop()
        #print(map(lambda s: s.getData(), cls1.getSamples()))
        #print(map(lambda s: s.getData(), cls2.getSamples()))
        self.assertTrue(False)"""
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()