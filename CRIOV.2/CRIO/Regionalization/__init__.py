from pyscipopt import Model, quicksum
from timeit import itertools
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.Group import Group

def assingGroupsToRegions(group,cluster):
    
    def getVals(model,dic):
        ret = {}
        for key,value in dic.items():
            ret[key] = model.getVal(value)
        return ret
    
    dimension = cluster.getDimension()
    
    
        
    ################## model #########################################
    
    model = Model()
    
    piVars = {}
    for f in range(dimension):
        piVars[f] = model.addVar(vtype="CONTINUOUS", name="pi[%s]" % (f),lb=None)
    
    alfaVar = model.addVar(vtype="CONTINUOUS", name="alfa",lb=None)
    objective = model.addVar(vtype="CONTINUOUS", name="objective",lb=None)
    
    model.addCons(quicksum(piVars[f]*piVars[f] for f in range(dimension)) <= objective , "objective_function" )
    
    for sample in cluster.getSamples():
        model.addCons(quicksum(piVars[f]*sample.getFeature(f) for f in range(dimension))>= alfaVar + 1, "r1%s" % (sample))
    
    for sample in group.getSamples():
        model.addCons(quicksum(piVars[f]*sample.getFeature(f) for f in range(dimension)) <= alfaVar - 1,"f2%s" % (sample))
    model.setObjective(objective,sense="minimize")
    model.optimize()

    return (getVals(model,piVars), model.getVal(alfaVar))

def main():
    d = 2
    cluster = Cluster([(7.0,4.0)],d)
    group = Group([(5.0,4.0)],d)
    
    (p,q) = assingGroupsToRegions(group, cluster)
    for k,n in p.items():
        print("feature: " + str(k) + " valor: " + str(n))
    
    print("alfa: " + str(q))

main()    
    
    
    
    ##################################################################