from CRIO.Exporter import writeSample, writeParameters, writeEliminateRedundantInstance
from CRIO.ScipInterface import solveProblem


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
            if(len(c) > 0):
                hiperplane = []
                writeSample(g,routeGroup)
                writeSample(c,routeCluster)
                writeParameters([len(g), len(c),len(c[0])], routeParams)
                model = solveProblem(routeModelDefineHiperplanes)
                hiperplaneVars = model.getVars()
                for var in hiperplaneVars[:-1]:
                    hiperplane.append(model.getVal(var))
                region.append(hiperplane)
            else:
                region.append([0.0,0.0,0.0])
        regions[g] = region
        
    return eliminateRedundat(clusters, regions)

def eliminateRedundat(clusters, regions):
    for region in regions.values():
        redundant = []
        for c in range(0,len(clusters)):
            print("region: " + str(region))
            writeEliminateRedundantInstance(region, c, routeRegion)
            model = solveProblem(routeModelEliminateRedundat)

            if (model.getObjVal() <= region[c][len(region[c])-1]):
                redundant.append(region[c])
            

        
        for r in redundant:
            region.remove(r)

    return regions



