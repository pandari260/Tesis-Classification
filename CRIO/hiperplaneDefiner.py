from muestras import writeSample, writeParameters, writeRegion
from scipInterface import solveProblem


routeGroup = "model/grupo"
routeCluster ="model/cluster"
routeModelDefineHiperplanes = "model/defineHiperplanes.zpl"
routeModelEliminateRedundat = "model/eliminateRedundant.zpl"
routeParams= "model/parametrosHiperplanes"
routeRegion = "model/region"


def defineHiperplanes(groupContainer, clusterContainer):

    groups = groupContainer.getGroups()
    clusters= clusterContainer.getClusters()
    regions = {}

    for g in groups:
        region =[]
        for c in clusters:
            hiperplane = []
            writeSample(g,routeGroup)
            writeSample(c,routeCluster)
            writeParameters((len(g), len(c)), routeParams)
            model = solveProblem(routeModelDefineHiperplanes)
            hiperplaneVars = model.getVars()
            for var in hiperplaneVars[:-1]:
                hiperplane.append(model.getVal(var))
            region.append(hiperplane)
        regions[g] = region

    
    print("-----------------------------------------------------------------------------------------------------------\n")
    for key, value in regions.items():
        print("Region: " + str(key) + "\n Hiperplanos:\n ")
        print("cantidad: " + str(len(key)))
        for hiperplano in value:
                print(str(hiperplano) + "\n")
        print("-----------------------------------------------------------------------------------------------------------\n")
    return eliminateRedundat(clusters, regions)

def eliminateRedundat(clusters, regions):
    for region in regions.values():
        redundant = []
        for c in range(0,len(clusters)):
            writeRegion(region, c, routeRegion)
            model = solveProblem(routeModelEliminateRedundat)
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXxobjetivo: " + str(model.getObjVal()) + " " + "q: " + str(region[c][2]) + "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

            if (model.getObjVal() <= region[c][2]):
                redundant.append(region[c])
            print("|||||||||||||||||||||| region: " + str(region) + ", c: " + str(c))
            print("||||||||||||||||||||||x0: " + str(model.getVal(model.getVars()[0])) + "\n")
            print("||||||||||||||||||||||x1: " + str(model.getVal(model.getVars()[1])))

        
        for r in redundant:
            region.remove(r)

    return regions



