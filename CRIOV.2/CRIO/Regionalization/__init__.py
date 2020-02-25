from pyscipopt import Model, quicksum
from timeit import itertools
from CRIO.Modelo.Cluster import Cluster
from CRIO.Modelo.Group import Group
from CRIO.Modelo.Hyperplane import Hyperplane
from CRIO.Modelo.Region import Region


def defineHyperplane(group,cluster):
    
    def getVals(model,dic):
        ret = {}
        for key,value in dic.items():
            ret[key] = model.getVal(value)
        return ret
    
    dimension = cluster.getDimension()  
    
        
    ################## model #########################################
    
    model = Model()
    model.hideOutput()
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

    return Hyperplane(getVals(model,piVars), model.getVal(alfaVar))    
    
    
    ################################################################## 

def createRegions(groups, clusters):
    
    regions = set([])
    for grp in groups.getGroups():
        hiperplanes = []
        for clstr in clusters.getClusters():
            hiperplanes.append(defineHyperplane(grp,clstr))
        regions.add(Region(hiperplanes,clusters.getDimension()))
      
    return map(lambda rgn: eliminateRedundant(rgn), regions)

def eliminateRedundant(region):
    return Region(filter(lambda hypr: hypr.isRedundant(region) == False, region.getHyperplanes()),region.getDimension()) 
    
            
    
    
    



