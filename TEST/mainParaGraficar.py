from Importer import readSamples, readHiperplanes
from Plotter import graphDataSet
import numpy as np

routeClass0 = "class0.dat"
routeClass1 = "class1.dat"
routeSolution = "solution"

def main():
    clase0 = readSamples(routeClass0,2)
    clase1 = readSamples(routeClass1,2)
    solution = readHiperplanes(routeSolution,2)

    print("Clase0: " + str(clase0)  + "\n\n\n\n\n\n")
    print("Clase1: " + str(clase1)  + "\n\n\n\n\n\n")
    print("Hiperplanos: " + str(solution)  + "\n\n\n\n\n\n")

    graphDataSet(clase0,clase1,solution,np.linspace(-5,5,3000))


main()
