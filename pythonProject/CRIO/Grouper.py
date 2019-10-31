from CRIO.ScipInterface import solveProblem


routeModel = "model/assingGroups.zpl"

class GroupContainer():
    
    def __init__(self,class0, class1,clusterContainer,k):
        self.model = ModelSolution(solveProblem(routeModel),clusterContainer.getCantClusters(), len(class0),len(class1),k)
        deleteOutliers(class1, clusterContainer, self.model.e1Vals)        
        self.groups = defineGroups(clusterContainer,self.model, k)
        self.cantGroups = len(self.groups)    
        
    
    def getGroups(self):
        return self.groups
    
    def getNumberGroups(self):
        return self.cantGroups



#crea una matriz con las listas de muestras que corresponden a un mismo grupo
def defineGroups(clusterContainer, model, k):
    
    assings = assingGroups(clusterContainer.getCantClusters(), model, k)
    
    clusters = clusterContainer.getClusters()

    groups=[]
    for value in assings.values():
        samples=[]
        for i in value:
            samples = samples + clusters[i]
        if len(samples) > 0:
            groups.append(tuple(samples))
    return groups


#assigna cada id de cluster a uno de los k grupos
def assingGroups(cantClusters,model, k):
    
    groups = dict()
    arkVals = model.arkVals  
    
        
    for i in range(0, k):
        g = []
        for j in range(cantClusters*i, cantClusters*(i+1)):
            if(arkVals[j] == 1):
                g.append(j%cantClusters)
        groups[i] = g

    return groups

def deleteOutliers(samples, clusterContainer, eVals):
    
    for e in range(0, len(eVals)):
        if eVals[e] > 1:
            clusterContainer.removeSample(samples[e])  
    
    return 0
    
    
class ModelSolution():
    
    def __init__(self, model, cantClusters,m0,m1 , k):
            self.arkVals = list(map(lambda var: model.getVal(var),model.getVars()[:cantClusters*k]))    
            self.e0Vals = list(map(lambda var: model.getVal(var),model.getVars()[cantClusters*k:cantClusters*k+m0] ))   
            self.e1Vals = list(map(lambda var: model.getVal(var),model.getVars()[cantClusters*k+m0:cantClusters*k+m0+ m1])) 
        
        
            
            

