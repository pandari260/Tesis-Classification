from pyscipopt import Model

routeModel = "crio.zpl"

#recibe una lista de clusters de clase 1 y asigna cada uno a uno de los k grupos, de acuerdo a los parametros y al modelo dado.
def assingGroups(cluster1, k):
    cantClusters = len(cluster1)
    model = Model()
    model.readProblem(routeModel)
    model.optimize()
    arkVars  = model.getVars()[:cantClusters*k]
    groups = dict()

    for t in range(len(arkVars)):
        print(str(arkVars[t]) + " " + str(model.getVal(arkVars[t])))
    for i in range(0, k):
        for j in range(cantClusters*i, cantClusters*(i+1)):
            if(model.getVal(arkVars[j]) == 1):
                groups[j%cantClusters] = i
                print(k)

    return groups
    
    


