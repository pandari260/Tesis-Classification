from muestras import writeSample, writeParams
from scipInterface import solveProblem

routeGroup = "model/grupo"
routeModel = "model/defineHiperplanes.zpl"
routeCluster ="model/cluster"
routeParametros = "model/parametrosHiperplanes"



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
            writeParams((len(g), len(c)), routeParametros)
            model = solveProblem(routeModel)
            hiperplaneVars = model.getVars()
            for var in hiperplaneVars:
                hiperplane.append(model.getVal(var))
            region.append(hiperplane)
        regions[g] = region
    return regions
