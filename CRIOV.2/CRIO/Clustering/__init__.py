from pyscipopt import Model, quicksum
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer
import numpy as np
from prompt_toolkit.layout import dimension
from timeit import itertools

#determina si hay una muestra perteneciente a "samples" en la componente convexa de entre los clusters A y B 
#ambos clusters deben tener el mismo valor de dimension
def isMergeable(clusterA,clusterB,samples):
    model = Model()
    
    dimension = clusterA.getDimension()
    samples_size = samples.getSize()
    samples_in_clusters = SampleContainer(clusterA.getSamples() + clusterB.getSamples(), clusterA.getDimension())
    samples_in_cluster_size = samples_in_clusters.getSize()
    
    ###################### modelo ############################################
    delta = model.addVar(vtype="C", name="delta",lb=None)   
    
    pVars = {}    
    for (spl,f) in itertools.product(samples.getData(),range(dimension)):
        pVars[(spl,f)] = model.addVar(vtype="C", name="p" +str(spl) +"%s" % (f),lb=None)    
    
    qVars = {}
    for spl in samples.getData():
        qVars[spl] = model.addVar(vtype="C", name="q" + str(spl),lb=None)
        
    for spl in samples.getData():
        model.addCons((qVars[spl] + quicksum(pVars[(spl,j)] * spl.getFeature(j) for j in range(dimension)))<= -delta,"r%s" % (spl))
    
    for spl in samples.getData():
        for clstr_spl in samples_in_clusters.getData():
            model.addCons((qVars[spl] + quicksum(pVars[(spl,j)] * clstr_spl.getFeature(j) for j in range(dimension)))>=delta, "r%s%s" % (spl,clstr_spl))
                    
    model.setObjective(delta, sense="maximize")
    ##########################################################################
    
    model.optimize()

    return model.getObjVal() > 0
    
    


        
    
    

            
    