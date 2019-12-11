from pyscipopt import Model, quicksum
from timeit import itertools
from CRIO.Modelo.SampleContainer import SampleContainer
from prometheus_client import samples
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.ClusterContainer import ClusterContainer


M = 100000 #parametro grande

"""asigna uno de k grupos a cada cluster de clase 1. Todos los ClusterContainer y SampleContainer deben tener el mismo valor de dimension. k y d deben ser al menos 1."
firma: assignClustersToGroups:(samples0:SampleContainer, sample1:SampleContainer, clusters0: ClusterContainer, cluster1:ClusterContainer, k:Integer,d: Integer)"""

def assignClustersToGroups(samples0, samples1, clusters0, clusters1, num_groups):
    
    dimension = samples0.getDimension()
    ############################## Modelo ######################################
    model = Model()
    
    
    aVars = {}    
    for (k,clstr) in itertools.product(range(num_groups), clusters1.getClusters()):
        aVars[(k,clstr)] = model.addVar(vtype="B", name="a" + "%s" % (k) + str(clstr))
    
    pVars = {}
    for (k,clstr,f) in itertools.product(range(num_groups), clusters0.getClusters(),range(dimension)):
        pVars[(k,clstr,f)] = model.addVar(vtype="C",name="p" + "%s" % (k) + str(clstr) + "%s" % (f),lb=None)
    
    qVars = {}
    for (k,clstr) in itertools.product(range(num_groups), clusters0.getClusters()):
        qVars[(k,clstr)] = model.addVar(vtype="C", name="q" + "%s" % (k) + str(clstr),lb=None)
    
    e0Vars = {}
    for spl in samples0.getSamples():
        e0Vars[spl] = model.addVar(vtype="C",name="e0" + str(spl))
    
    e1Vars = {}
    for spl in samples1.getSamples():
        e1Vars[spl] = model.addVar(vtype="C", name="e1" + str(spl))
        
    for k in range(num_groups):
        for clstr in clusters0.getClusters():
            for spl in samples0.getSamples().intersection(clstr.getSamples()):
                model.addCons((qVars[k,clstr] + quicksum(pVars[k,clstr,f]*spl.getFeature(f) for f in range(dimension)))<= -1 + e0Vars[spl])
    
    for k in range(num_groups):
        for clstr1 in clusters1.getClusters():
            for spl in clstr1.getSamples():
                for clstr0 in clusters0.getClusters():
                    model.addCons((qVars[k,clstr0] + quicksum(pVars[k,clstr0,f]*spl.getFeature(f) for f in range(dimension))) >= -M + (M + 1)*aVars[k,clstr1])
    
    for clstr in clusters1.getClusters():
        model.addCons(quicksum(aVars[k,clstr] for k in range(num_groups)) == 1)
    
    model.setObjective(quicksum(e0Vars[spl] for spl in samples0.getSamples()) + quicksum(e1Vars[spl] for spl in samples1.getSamples()),sense="minimize")
    model.optimize()
    for v in e1Vars.values():
        print model.getVal(v)
    return model.getObjVal()
    
    


def main():
    d = 2
    samples0 = SampleContainer([(4.0,4.0),(5.0,4.0),(4.0,3.0),(5.0,3.0)],d)
    samples1 = SampleContainer([(2.0,5.0),(3.0,6.0),(2.0,6.0),(7.0,2.0),(8.0,1.0),(8.0,2.0),(7.0,1.0)],d)

    clusters1 = ClusterContainer([Cluster([(2.0,5.0),(3.0,6.0),(2.0,6.0)],d),Cluster([(7.0,2.0),(8.0,1.0),(8.0,2.0),(7.0,1.0)],d)],d)
    clusters0 = ClusterContainer([Cluster([(2.0,5.0),(3.0,6.0),(2.0,6.0),(7.0,2.0),(8.0,1.0),(8.0,2.0),(7.0,1.0)],d)],d)
    num_groups = 2
    assignClustersToGroups(samples0, samples1, clusters0, clusters1, num_groups)    

main()
    

        
    
    

    
    
    
    