from pyscipopt import Model, quicksum
from CRIO.Modelo.Cluster import mergeClusters,Cluster,distance
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer
import numpy as np
from timeit import itertools
from CRIO.Modelo.ClusterContainer import ClusterContainer
import networkx as nx
from functools import reduce
import CRIO.Importer as Importer

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
        while k < K:
           
            #(u,v,w) = sorted_edges[0]
            (u,v) = minimumEdge(distances_graph)
            merged = mergeClusters(u, v)
            print("se puede fusionar: " + str(not containsOutlier(merged, samples)) + " k: " + str(k) + " K: " + str(K))
            print("cluster u: " + str(map(lambda s : s.getData(), u.getSamples())))
            print("cluster v: " + str(map(lambda s : s.getData(), v.getSamples())))
            print("cluster merged: " + str(map(lambda s : s.getData(), merged.getSamples())))
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
        
        
        return ClusterContainer(filter(lambda cls: cls.getSize() >= samplesA.getSize()*0.01, clusters.getClusters()),clusters.getDimension())

def createClusters2(samplesA, samplesB):
    
    
    clusters = createDefaultClusters(samplesA)
    samples = samplesB
    
    if samplesA.getSize() == 1:
        return clusters
    
    else:       
        
        K = clusters.getSize()
        k = 0
        print("creando grafo de distancias...")
        distances_graph = createDistanceGraph(clusters.getClusters())
        #print("ordenando aristas...")
        sorted_edges = sorted(distances_graph.edges(data=True), key=lambda x: x[2]['weight'])
        has_already_been_merged  = createMap(distances_graph.nodes)
        #print("Cantidad de aristas " + str(len(sorted_edges)))
        #print("Cantidad de clusters: " + str(clusters.getSize()))

        print("reduciendo clusters...")
        while k < K:
            
            if len(sorted_edges) == 0:
                #print("re-ordenando...")
                sorted_edges = sorted(distances_graph.edges(data=True), key=lambda x: x[2]['weight'])
                has_already_been_merged  = createMap(distances_graph.nodes)
                print("Cantidad de aristas " + str(len(sorted_edges)))
                print("Cantidad de clusters: " + str(clusters.getSize()))
                print("cantidad de clusters: " + str(map(lambda s: s.getSize(),clusters.getClusters())))
                print("K: " + str(K))


            else:
                (u,v,w) = sorted_edges[0]
                #(u,v) = minimumEdge(distances_graph)    
                if(not has_already_been_merged[v] and not has_already_been_merged[u]):
                    merged = mergeClusters(u, v)
                    print("se puede fusionar: " + str(not containsOutlier(merged, samples)) + " k: " + str(k) + " K: " + str(K))
                    print("cluster u: " + str(map(lambda s : s.getData(), u.getSamples())))
                    print("cluster v: " + str(map(lambda s : s.getData(), v.getSamples())))
                    print("cluster merged: " + str(map(lambda s : s.getData(), merged.getSamples())))

                    

                    if not containsOutlier(merged, samples):
                        clusters = updateClusterContainer(clusters, u, v, merged)
                        distances_graph = updateDistanceGraph(distances_graph, u,v,merged)
                        has_already_been_merged[v] = True
                        has_already_been_merged[u] = True
                        K = K - 1
                        k = 0
                    k = k + 1
                sorted_edges.remove(sorted_edges[0])
                
        print(map(lambda c: c.getSize(), clusters.getClusters()))        
        
        
        
        
        return ClusterContainer(filter(lambda cls: cls.getSize() >= samplesA.getSize()*0.01, clusters.getClusters()),clusters.getDimension())

            
            
        
            
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
    
def createMap(values):
    d = {}
    for v in values:
        d[v] = False
    
    return d



def minimumEdge(g):
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
    d = samples.getDimension()
    return ClusterContainer(map(lambda spl: Cluster([spl],d),samples.getSamples()),d)

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
    """print("valor objetivo: " + str(model.getObjVal()))
    for s in samples.getSamples():
        print(str(qVars[spl]) + ": "   + str(model.getVal(qVars[s])))
        
    for (spl,f) in itertools.product(samples.getSamples(),range(dimension)):
        print(str(pVars[spl,f]) + ": "   + str(model.getVal(pVars[spl,f])))"""

    return model.getObjVal() == 0


    


        
    
    

            
    