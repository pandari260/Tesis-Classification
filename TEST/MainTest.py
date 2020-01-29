import matplotlib.pyplot as plt  
import Plotter as plotter
import CaseTest as caseTest
import Exporter as exporter
import numpy as np
import Sample
import pandas as pd
import csv


def graphTest(sample):
	c0, c1 = Sample.divideForClass(sample)
	plotter.graphSample(c0, c1)
	plt.show()

def readFile(name):
	c0, c1 = [], []
	with open(name, 'r') as csvfile:
		set_data = csv.reader(csvfile, delimiter=',')
		next(set_data)
		aux_set_data = list(set_data).copy()
		c0 = list(map(lambda k: tuple(map(lambda i: float(i), k)),  list(map(lambda j: j[:-1], list(filter(lambda l: int(l[-1]) == 0, aux_set_data))))))
		c1 = list(map(lambda k: tuple(map(lambda i: float(i), k)), list(map(lambda j: j[:-1], list(filter(lambda l: int(l[-1]) == 1, aux_set_data))))))
	return c0, c1

#------- Configuracion general de los casos de prueba ha generar -----#
seed = 2
dimension = 2
d = "R2"

name = "../Resources/"+d+"/t1-ConjuntosDisjuntos.csv"
n = [500, 500]
mMu = [[0,0],[6,0]]
classes = [0,1]
test = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
sample = test.initTest()
exporter.exportCaseTest(sample, name)
#graphTest(sample) 

# ------------ Ejemplo lectura archivo CRIO ----------------
#c0, c1 = readFile(name)
#print(c0)	
#print(c1)  


name = "../Resources/"+d+"/t2-ConjuntosSolapados.csv"
n = [500, 500]
mMu = [[0,0],[3,0]]
classes = [1,0]
test = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
sample = test.initTest()
exporter.exportCaseTest(sample, name)
#graphTest(sample) 

name = "../Resources/"+d+"/t3-CuadranteOpuesto.csv"
n = [500, 500, 500, 500]
mMu = [[0,0],[8,0],[0,8],[8,8]]
classes = [1,0,0,1]
test = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
sample = test.initTest()
exporter.exportCaseTest(sample, name)
#graphTest(sample) 


name = "../Resources/"+d+"/t4-CuadranteOpuestoSolapado.csv"
n = [500, 500, 500, 500]
mMu = [[0,0],[4,0],[0,4],[4,4]]
classes = [1,0,0,1]
test = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
sample = test.initTest()
exporter.exportCaseTest(sample, name)
#graphTest(sample) 


name = "../Resources/"+d+"/t5-Encerrado.csv"
n = [100, 100, 100, 100, 100, 100, 100, 100, 100]
mMu = [[0,0], [0,10], [5,5], [5,0], [10,0], [10,10], [5,10], [0,5], [10,5]]
classes = [1,1,0,1,1,1,1,1,1]
test = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
sample = test.initTest()
exporter.exportCaseTest(sample, name)
#graphTest(sample) 


name = "../Resources/"+d+"/t6-EncerradoSolapado.csv"
n = [100, 100, 100, 500, 100, 100, 100, 100, 100]
mMu = [[5,0],[2,2],[8,2],[5,4],[2,5], [8,5], [5,7]]
classes = [1,1,1,0,1,1,1]
test = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
sample = test.initTest()
exporter.exportCaseTest(sample, name)
#graphTest(sample) 


name = "../Resources/"+d+"/t7-DiagonalIntercalada.csv"
n = [500, 500, 500]
mMu = [[2,10],[9,8],[16,6]]
classes = [1,0,1]
test = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
sample = test.initTest()
exporter.exportCaseTest(sample, name)
#graphTest(sample) 


name = "../Resources/"+d+"/t8-DiagonalIntercaladaSolapada.csv"
n = [500, 500, 500]
mMu = [[2,10],[5,8],[8,6]]
classes = [1,0,1]
test = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
sample = test.initTest()
exporter.exportCaseTest(sample, name)
#graphTest(sample) 

format1 = "--> %s test de dimension %s fueron creados en la carpeta %s."
print(format1 % tuple((n[0],dimension, d)))
