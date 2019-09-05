from muestras import writeSample, writeParameters
from scipInterface import solveProblem


routeGroup = "model/grupo"
routeModel = "model/defineHiperplanes.zpl"
routeCluster ="model/cluster"
routeParams= "model/parametrosHiperplanes"


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
            model = solveProblem(routeModel)
            hiperplaneVars = model.getVars()
            for var in hiperplaneVars[:-1]:
                hiperplane.append(model.getVal(var))
            region.append(hiperplane)
        regions[g] = region
    return regions