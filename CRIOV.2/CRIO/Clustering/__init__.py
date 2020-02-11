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

def main():
    c0,c1 = Importer.readSample("/home/javier/Documentos/Repositorios Git/Tesis-Classification/Resources/R2/t1-ConjuntosDisjuntos-10.csv")
    
    #print(c1)
    #print(not containsOutlier(Cluster([(-0.5716,-1.3338), (-1.0047,-0.02892)],2), SampleContainer(c1,2)))
    #print(not containsOutlier(Cluster([(-0.5716,-1.3338), (-1.0047,-0.02892)],2), SampleContainer([(4.8919,-0.1003)],2)))
    #print(not containsOutlier(Cluster([(5.5716, 4.3338), (4.0047,5.02892)],2), SampleContainer([(9.8919,5.1003)],2)))
    """print(not containsOutlier(Cluster([(-1.0, -1.0), (-2.0,0.0)],2), SampleContainer([(5.0,0.0)],2)))
    print(not containsOutlier(Cluster([(-6.0, -2.0), (-4.0,-4.0)],2), SampleContainer([(1.0,-2.0)],2)))
    print(not containsOutlier(Cluster([(-9.0, -5.0), (-8.0,-6.0)],2), SampleContainer([(-2.0,-5.0)],2)))
    print(not containsOutlier(Cluster([(-7.0, 4.0), (-6.0,3.0)],2), SampleContainer([(2.0,4.0)],2)))
    print(not containsOutlier(Cluster([(-9.0, 7.0), (-8.0,6.0)],2), SampleContainer([(-2.0,7.0)],2)))
    print(not containsOutlier(Cluster([(2.0, 6.0), (4.0,4.0)],2), SampleContainer([(9.0,6.0)],2)))
    print(not containsOutlier(Cluster([(3.0, -1.0), (2.0,0.0)],2), SampleContainer([(9.0,0.0)],2)))
    print(not containsOutlier(Cluster([(2.0, -2.0), (4.0,-4.0)],2), SampleContainer([(9.0,-2.0)],2)))
    print(not containsOutlier(Cluster([(6.0, -2.0), (7.0,-1.0)],2), SampleContainer([(13.0,0.0)],2)))
    print(not containsOutlier(Cluster([(-0.5, 0.5), (7.0,-1.0)],2), SampleContainer([(7.0,0.5)],2)))
    print(not containsOutlier(Cluster([(2.0, 7.0), (1.0,6.0)],2), SampleContainer([(-7.0,7.0)],2)))"""
    
    print(not containsOutlier(Cluster([(-4.0, -2.0), (-3.0,-1.0)],2), SampleContainer([(-4.0,5.0)],2)))
    print(not containsOutlier(Cluster([(-8.0, 4.0), (-7.0,5.0)],2), SampleContainer([(-8.0,11.0)],2)))
    print(not containsOutlier(Cluster([(-10.0, -10.0), (-9.0,-9.0)],2), SampleContainer([(-10.0,-3.0)],2)))
    print(not containsOutlier(Cluster([(6.0, 3.0), (7.0,4.0)],2), SampleContainer([(6.0,10.0)],2)))
    print(not containsOutlier(Cluster([(4.0, -5.0), (5.0,-4.0)],2), SampleContainer([(4.0,2.0)],2)))
    print(not containsOutlier(Cluster([(8.0, -11.0), (9.0,-10.0)],2), SampleContainer([(8.0,-4.0)],2)))
    print(not containsOutlier(Cluster([(10.0, 2.0), (11.0,1.0)],2), SampleContainer([(10.0,-5.0)],2)))
    print(not containsOutlier(Cluster([(-12.0, 3.0), (-11.0,2.0)],2), SampleContainer([(-12.0,-4.0)],2)))
    
    """print(not containsOutlier(Cluster([(-3.0, 4.0), (-3.0,2.0)],2), SampleContainer([(2.0,5.0)],2)))
    print(not containsOutlier(Cluster([(-3.0, 4.0), (-3.0,2.0)],2), SampleContainer([(2.0,3.0)],2)))
    print(not containsOutlier(Cluster([(-3.0, 4.0), (-3.0,2.0)],2), SampleContainer([(2.0,1.0)],2)))
    print(not containsOutlier(Cluster([(9.0, -3.0), (11.0,-3.0)],2), SampleContainer([(8.0,2.0)],2)))
    print(not containsOutlier(Cluster([(9.0, -3.0), (11.0,-3.0)],2), SampleContainer([(10.0,2.0)],2)))
    print(not containsOutlier(Cluster([(9.0, -3.0), (11.0,-3.0)],2), SampleContainer([(12.0,2.0)],2)))
    print(not containsOutlier(Cluster([(19.0, 1.0), (21.0,1.0)],2), SampleContainer([(22.0,-2.0)],2)))
    print(not containsOutlier(Cluster([(19.0, 1.0), (21.0,1.0)],2), SampleContainer([(18.0,-2.0)],2)))
    print(not containsOutlier(Cluster([(19.0, 1.0), (21.0,1.0)],2), SampleContainer([(20.0,-2.0)],2)))
    print(not containsOutlier(Cluster([(1.0, -3.0), (1.0,-5.0)],2), SampleContainer([(-2.0,-2.0)],2)))
    print(not containsOutlier(Cluster([(1.0, -3.0), (1.0,-5.0)],2), SampleContainer([(-2.0,-4.0)],2)))
    print(not containsOutlier(Cluster([(1.0, -3.0), (1.0,-5.0)],2), SampleContainer([(-2.0,-6.0)],2)))"""
    
    
main()
    
    


        
    
    

            
    