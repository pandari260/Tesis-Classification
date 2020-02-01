from Importer import readSamples, readHiperplanes
from Plotter import graphDataSet
import numpy as np
import csv

def readFile(name):
	c0, c1 = [], []
	with open(name, 'r') as csvfile:
		set_data = csv.reader(csvfile, delimiter=',')
		next(set_data)
		aux_set_data = list(set_data).copy()
		c0 = list(map(lambda k: tuple(map(lambda i: float(i), k)),  list(map(lambda j: j[:-1], list(filter(lambda l: int(l[-1]) == 0, aux_set_data))))))
		c1 = list(map(lambda k: tuple(map(lambda i: float(i), k)), list(map(lambda j: j[:-1], list(filter(lambda l: int(l[-1]) == 1, aux_set_data))))))
	return c0, c1

routeSolution = "solution"
dimension = 2
d = "R2"
name = "../Resources/"+d+"/t7-DiagonalIntercalada.csv"

def main():
    #clase0 = readSamples(routeClass0,2)
    #clase1 = readSamples(routeClass1,2)
    clase0, clase1 = readFile(name)

    solution = readHiperplanes(routeSolution,2)

    print("Clase0: " + str(clase0)  + "\n\n\n\n\n\n")
    print("Clase1: " + str(clase1)  + "\n\n\n\n\n\n")
    print("Hiperplanos: " + str(solution)  + "\n\n\n\n\n\n")

    graphDataSet(clase0,clase1,solution)


main()
