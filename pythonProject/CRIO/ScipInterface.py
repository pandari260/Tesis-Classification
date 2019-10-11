from pyscipopt import Model

def solveProblem(routeModel):
    model = Model()
    model.readProblem(routeModel)
    model.optimize()
    return model