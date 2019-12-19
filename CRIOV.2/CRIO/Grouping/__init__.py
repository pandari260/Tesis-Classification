from pyscipopt import Model, quicksum
from timeit import itertools
from CRIO.Modelo.SampleContainer import SampleContainer
from prometheus_client import samples
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.ClusterContainer import ClusterContainer
from prompt_toolkit.layout import dimension
from CRIO.Modelo.Sample import Sample


M = 100000 #parametro grande

"""asigna uno de k grupos a cada cluster de clase 1. Todos los ClusterContainer y SampleContainer deben tener el mismo valor de dimension. k y d deben ser al menos 1."
firma: assignClustersToGroups:(samples0:SampleContainer, sample1:SampleContainer, clusters0: ClusterContainer, cluster1:ClusterContainer, k:Integer,d: Integer)"""

def assignClustersToGroups(clusters0, clusters1, num_groups):
    
    def getVals(model,dic):
        ret = {}
        for key,value in dic.items():
            ret[key] = model.getVal(value)
        return ret
        
    dimension = clusters0.getDimension()
    samples0 = clusters0.getSamples()
    samples1 = clusters1.getSamples()
    
    print("dimension: " +str(dimension))
    print("samples 0: " + str(samples0.getSamples()))
    print("samples 1:" + str(samples1.getSamples()))
    ############################## Modelo ######################################
    model = Model()
    
    
    aVars = {}    
    for (k,clstr) in itertools.product(range(num_groups), clusters1.getClusters()):
        aVars[(k,clstr)] = model.addVar(vtype="BINARY", name="a" + "%s" % (k) + str(clstr))
    
    pVars = {}
    for (k,clstr,f) in itertools.product(range(num_groups), clusters0.getClusters(),range(dimension)):
        pVars[(k,clstr,f)] = model.addVar(vtype="CONTINUOUS",name="p" + "%s" % (k) + str(clstr) + "%s" % (f),lb=None)
    
    qVars = {}
    for (k,clstr) in itertools.product(range(num_groups), clusters0.getClusters()):
        qVars[(k,clstr)] = model.addVar(vtype="CONTINUOUS", name="q" + "%s" % (k) + str(clstr),lb=None)
    
    e0Vars = {}
    for spl in samples0.getSamples():
        e0Vars[spl] = model.addVar(vtype="CONTINUOUS",name="e0" + str(spl))
    
    e1Vars = {}
    for spl in samples1.getSamples():
        e1Vars[spl] = model.addVar(vtype="CONTINUOUS", name="e1" + str(spl))
        
    for k in range(num_groups):
        for clstr in clusters0.getClusters():
            for spl in samples0.getSamples().intersection(clstr.getSamples()):
                model.addCons((qVars[k,clstr] + quicksum(pVars[k,clstr,f]*spl.getFeature(f) for f in range(dimension)))<= -1 + e0Vars[spl],"r1%s%s%s" % (k,clstr,spl))
    
    for k in range(num_groups):
        for clstr1 in clusters1.getClusters():
            for spl in samples1.getSamples().intersection(clstr1.getSamples()):
                for clstr0 in clusters0.getClusters():
                    model.addCons((qVars[k,clstr0] + quicksum(pVars[k,clstr0,f]*spl.getFeature(f) for f in range(dimension))) >= -M + (M + 1)*aVars[k,clstr1]-e1Vars[spl],"r2%s%s%s%s" % (k,clstr1,spl,clstr0))
    
    for clstr in clusters1.getClusters():
        model.addCons((quicksum(aVars[k,clstr] for k in range(num_groups))) == 1,"r3%s" %(clstr))
    
     
    
    
    model.setObjective(quicksum(e0Vars[spl] for spl in samples0.getSamples()) + quicksum(e1Vars[spl] for spl in samples1.getSamples()),sense="minimize")
    model.optimize()
    ###########################################################################
    
    print("valores de p")
    for key in pVars.keys():
        print("clave: " + str(key) + " valor: " + str(model.getVal(pVars[key])))
    
    print("valores de q")
    for key in qVars.keys():
        print("clave: " + str(key) + " valor: " + str(model.getVal(qVars[key])))
    
    print("valores de a")
    for key in aVars.keys():
        print("clave: " + str(key) + " valor: " + str(model.getVal(aVars[key])))
    
    print("valores de e0")
    for key in e0Vars.keys():
        print("clave: " + str(key) + " valor: " + str(model.getVal(e0Vars[key])))
    
    print("valores de e1")
    for key in e1Vars.keys():
        print("clave: " + str(key) + " valor: " + str(model.getVal(e1Vars[key])))
    
    
    
    return (getVals(model, aVars), getVals(model, e0Vars), getVals(model, e1Vars))
    
    


def main():
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

main()
    

        
    
    

    
    
    
    