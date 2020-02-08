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


def __getListClass(lines, clas):
    lines = list(filter(lambda line: int(line[-1]) == clas, lines))
    lines = list(map(lambda line: line[:-1], lines))
    return list(map(lambda line: tuple(map(lambda line2: float(line2), line)),  lines))

def readFile(name):
    with open(name, 'r') as csvfile:
        aux_set_data = csv.reader(csvfile, delimiter=',')
        next(aux_set_data)
        aux_set_data = list(aux_set_data)
        c0 = __getListClass(aux_set_data, 0)
        c1 = __getListClass(aux_set_data, 1) 
        return c0, c1
       
def divideProportionally(lines, porc):
    p = int(len(lines)*porc)
    return lines[:p], lines[p:]
#Conseguir los hyperplanos -----------------------------------
routeSolution = "solution"

idTest = files[0][1]
direc = directory[0]

name = "../Resources/"+direc+idTest+".csv"
clase0, clase1 = readFile(name)
print(len(clase0))
train, test = divideProportionally(clase0, 0.22)
print(len(train))
print(len(test))
#print(clase1)
solution = readHiperplanes(routeSolution,2)

#print("Clase0: " + str(clase0)  + "\n\n\n\n\n\n")
#print("Clase1: " + str(clase1)  + "\n\n\n\n\n\n")
#print("Hiperplanos: " + str(solution)  + "\n\n\n\n\n\n")

#graphDataSet(clase0,clase1,solution)


