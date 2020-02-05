from Importer import readSamples, readHiperplanes
from Plotter import graphDataSet
import numpy as np
import csv

files = [    [  "/t1-ConjuntosDisjuntos",
                "/t2-ConjuntosSolapados",
                "/t3-CuadranteOpuesto",
                "/t4-CuadranteOpuestoSolapado",
                "/t5-Encerrado",
                "/t6-EncerradoSolapado",
                "/t7-DiagonalIntercalada",
                "/t8-DiagonalIntercaladaSolapada"   ],
                
            [   "/Test-C_Easy1_noise01",
                "/Test-C_Easy1_noise02",
                "/Test-C_Easy1_noise03",
                "/Test-C_Easy1_noise04",
                "/Test-C_Easy1_noise005",
                "/Test-C_Easy2_noise01",
                "/Test-C_Easy2_noise02",
                "/Test-C_Difficult1_noise01",
                "/Test-C_Test_LFPcorr_Easy2_noise015",
                "/Test-C_Drift_Easy2_noise015"   ]  ]

directory = [   "R2", 
                "R2-Real" ]


def readFile(name):
	c0, c1 = [], []
	with open(name, 'r') as csvfile:
		aux_set_data = csv.reader(csvfile, delimiter=',')
		next(aux_set_data)
		aux_set_data = list(aux_set_data)
		c0 = list(map(lambda k: tuple(map(lambda i: float(i), k)),  list(map(lambda j: j[:-1], list(filter(lambda l: int(l[-1]) == 0, aux_set_data))))))
		c1 = list(map(lambda k: tuple(map(lambda i: float(i), k)), list(map(lambda j: j[:-1], list(filter(lambda l: int(l[-1]) == 1, aux_set_data))))))
	return c0, c1

#Conseguir los hyperplanos -----------------------------------
routeSolution = "solution"

idTest = files[0][1]
direc = directory[0]

name = "../Resources/"+direc+idTest+".csv"
clase0, clase1 = readFile(name)
solution = readHiperplanes(routeSolution,2)

print("Clase0: " + str(clase0)  + "\n\n\n\n\n\n")
print("Clase1: " + str(clase1)  + "\n\n\n\n\n\n")
print("Hiperplanos: " + str(solution)  + "\n\n\n\n\n\n")

graphDataSet(clase0,clase1,solution)


