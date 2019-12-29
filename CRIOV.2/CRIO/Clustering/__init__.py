from pyscipopt import Model, quicksum
from CRIO.Modelo.Cluster import mergeClusters
from CRIO.Modelo.Sample import Sample
from CRIO.Modelo.SampleContainer import SampleContainer
import numpy as np
from timeit import itertools

#determina si hay una muestra perteneciente a "samples" en la componente convexa de entre los clusters A y B 
#ambos clusters deben tener el mismo valor de dimension
def isMergeable(clusterA,clusterB,samples):
    
    dimension = clusterA.getDimension()
    mergedCluster = mergeClusters(clusterA, clusterB)
    
    ###################### modelo ############################################
    model = Model()
    
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

    return model.getObjVal() > 0
    
    


        
    
    

            
    