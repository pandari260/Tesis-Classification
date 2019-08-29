import scipInterface as scip


routeModel = "model/assingGroups.zpl"

#recibe una lista de clusters de clase 1 y asigna cada uno a uno de los k grupos, de acuerdo a los parametros y al modelo dado.
def assingGroups(cluster1, k):
    cantClusters = len(cluster1)
    model = scip.solveProblem(routeModel)
    arkVars  = model.getVars()[:cantClusters*k]
    groups = dict()
    
    for i in range(0, k):
        g = []
        for j in range(cantClusters*i, cantClusters*(i+1)):
            if(model.getVal(arkVars[j]) == 1):
                g.append(j%cantClusters)
        groups[i] = g

    return groups
    
    


