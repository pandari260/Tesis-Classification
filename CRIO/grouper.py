import scipInterface as scip


routeModel = "model/assingGroups.zpl"

class GroupContainer():
    def __init__(self, c,k):
        self.assings = assingGroups(c, k)
        self.groups = defineGroups(c.getClusters(), self.assings)
        self.cantGroups = len(self.groups)
    
    def getGroups(self):
        return self.groups
    
    def getNumberGroups(self):
        return self.cantGroups

#recibe una lista de clusters de clase 1 y asigna cada uno a uno de los k grupos, de acuerdo a los parametros y al modelo dado.
def assingGroups(clusterContainer, k):
    model = scip.solveProblem(routeModel)
    cantClusters = clusterContainer.getCantClusters()
    arkVars  = model.getVars()[:cantClusters*k]
    groups = dict()
    
    for i in range(0, k):
        g = []
        for j in range(cantClusters*i, cantClusters*(i+1)):
            if(model.getVal(arkVars[j]) == 1):
                g.append(j%cantClusters)
        groups[i] = g

    return groups

#toma una lista de clusters y los agrupa de acuerdo al grupo asignado en assings
def defineGroups(clusters, assings):
    groups=[]
    for value in assings.values():
        samples=[]
        for i in value:
            samples = samples + clusters[i]
        groups.append(tuple(samples))
    return groups
