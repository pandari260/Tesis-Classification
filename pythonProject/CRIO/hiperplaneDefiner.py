from fileManager import writeSample, writeParameters, writeEliminateRedundantInstance
from scipInterface import solveProblem


routeGroup = "model/defineHiperplanesCurrentGruop"
routeCluster ="model/defineHiperplanesCurrentCluster"
routeModelDefineHiperplanes = "model/defineHiperplanes.zpl"
routeModelEliminateRedundat = "model/eliminateRedundant.zpl"
routeParams= "model/defineHiperplanesParameters"
routeRegion = "model/eliminateRedundatCurrentRegion"


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
        
    return eliminateRedundat(clusters, regions)

def eliminateRedundat(clusters, regions):
    for region in regions.values():
        redundant = []
        for c in range(0,len(clusters)):
            writeEliminateRedundantInstance(region, c, routeRegion)
            model = solveProblem(routeModelEliminateRedundat)

            if (model.getObjVal() <= region[c][2]):
                redundant.append(region[c])
            

        
        for r in redundant:
            region.remove(r)

    return regions



