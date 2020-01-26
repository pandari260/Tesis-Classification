from pyscipopt import Model, quicksum
from CRIO.Modelo.Cluster import mergeClusters,Cluster,distance
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer
import numpy as np
from timeit import itertools
from CRIO.Modelo.ClusterContainer import ClusterContainer
import networkx as nx
from functools import reduce


#resive dos SamplesContainer de clase A y B, y retorna clusters de clase A de acuerdo a clustering por menor distacia promedio
def createClusters(samplesA, samplesB):
    clusters = createDefaultClusters(samplesA)
    samples = samplesB
    
    if samplesA.getSize() == 1:
        return clusters
    
    else:       
        
        K = clusters.getSize()
        k = 0
        distances_graph = createDistanceGraph(clusters.getClusters())
        #sorted_edges = sorted(distances_graph.edges(data=True), key=lambda x: x[2]['weight'])
        #print("cantidad de objetos: " + str(len(sorted_edges)))
        while k < K:
           
            #(u,v,w) = sorted_edges[0]
            (u,v) = minimumEdge(distances_graph)
            merged = mergeClusters(u, v)
            if containsOutlier(merged, samples):
                #k = k + 1
                #sorted_edges.remove(sorted_edges[0])
                distances_graph[u][v]['weight'] = float('inf')
                
            else:
                clusters = updateClusterContainer(clusters, u, v, merged)
                distances_graph = updateDistanceGraph(distances_graph, u,v,merged)
                #sorted_edges = sorted(distances_graph.edges(data=True), key=lambda x: x[2]['weight'])
                K = K - 1
                k = 0
            k = k + 1
        
        
        return ClusterContainer(filter(lambda cls: cls.getSize() >= clusters.getSize()*0.01, clusters.getClusters()),clusters.getDimension())
            
            
def updateClusterContainer(clusters, u,v,merged):
    clusters.remove(u)
    clusters.remove(v)
    clusters.add(merged)
    return clusters
    
def updateDistanceGraph(g,u,v,merged):
    g.remove_node(u)
    g.remove_node(v)
    nodes = set(g.nodes)
    for n in nodes:
        g.add_edge(merged,n, weight=distance(merged, n))
    
    return g
    

def minimumEdge(g):
    #print("empeso a buscar")
    return reduce(lambda a,b: a if g[a[0]][a[1]]['weight'] < g[b[0]][b[1]]['weight'] else b , g.edges())

def createDistanceGraph(elements):
    G = nx.Graph()
    for u in elements:
        for v in elements - {u}:
            G.add_edge(u, v,weight= distance(u,v))
    return G
#devulve un ClusterContainer con cada muestra como un cluster
"""TODO: testear"""
def createDefaultClusters(samples):
    print("creando por defecto...")
    d = samples.getDimension()
    return ClusterContainer(map(lambda spl: Cluster([spl],d),samples.getSamples()),d)
    print("terminada la creacion por defecto...")

#determina si hay una muestra perteneciente a "samples" en la componente convexa de entre los clusters A y B 
#ambos clusters deben tener el mismo valor de dimension
def containsOutlier(mergedCluster,samples):
    
    dimension = mergedCluster.getDimension()
    ###################### modelo ############################################
    model = Model()
    model.hideOutput()
    
    delta = model.addVar(vtype="CONTINUOUS", name="delta",lb=None)   
    
    pVars = {}    
    for (spl,f) in itertools.product(samples.getSamples(),range(dimension)):
        pVars[(spl,f)] = model.addVar(vtype="CONTINUOUS", name="p" +str(spl) +"%s" % (f),lb=None)    
    
    qVars = {}
    for spl in samples.getSamples():
        qVars[spl] = model.addVar(vtype="CONTINUOUS", name="q" + str(spl),lb=None)
        
    for spl in samples.getSamples():
        model.addCons((qVars[spl] + quicksum(pVars[(spl,j)] * spl.getFeature(j) for j in range(dimension)))<= -delta,"r%s" % (spl))
    
    for spl in samples.getSamples():
        for clstr_spl in mergedCluster.getSamples():
            model.addCons((qVars[spl] + quicksum(pVars[(spl,j)] * clstr_spl.getFeature(j) for j in range(dimension)))>=delta, "r%s%s" % (spl,clstr_spl))
                    
    model.setObjective(delta, sense="maximize")
    ##########################################################################
    
    model.optimize()
    return model.getObjVal() == 0
    
    


        
    
    

            
    