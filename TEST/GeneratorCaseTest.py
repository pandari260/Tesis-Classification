import matplotlib.pyplot as plt  
import Plotter as plotter
import CaseTest as caseTest
import Exporter as exporter
import numpy as np
import Sample
import pandas as pd
import csv


files =  [  "/t1-ConjuntosDisjuntos",
            "/t2-ConjuntosSolapados",
            "/t3-CuadranteOpuesto",
            "/t4-CuadranteOpuestoSolapado",
            "/t5-Encerrado",
            "/t6-EncerradoSolapado",
            "/t7-DiagonalIntercalada",
            "/t8-DiagonalIntercaladaSolapada"   ]

n = [		[500, 500],
			[500, 500],
			[500, 500, 500, 500],
			[500, 500, 500, 500],
			[100, 100, 100, 100, 100, 100, 100, 100, 100],
			[100, 100, 100, 500, 100, 100, 100, 100, 100],
			[500, 500, 500],
			[500, 500, 500]		]

mMu = 	[	[[0,0],[6,0]],
	  		[[0,0],[3,0]],
	   		[[0,0],[8,0],[0,8],[8,8]],
			[[0,0],[4,0],[0,4],[4,4]],
			[[0,0], [0,10], [5,5], [5,0], [10,0], [10,10], [5,10], [0,5], [10,5]],
			[[5,0],[2,2],[8,2],[5,4],[2,5], [8,5], [5,7]],
			[[2,10],[9,8],[16,6]],
			[[2,10],[5,8],[8,6]]	]

classes = [	[0,1],
			[1,0],
			[1,0,0,1],
			[1,0,0,1],
			[1,1,0,1,1,1,1,1,1],
			[1,1,1,0,1,1,1],
			[1,0,1],
			[1,0,1]		]

seed = 2
dimension = 30
d = "R30"	

def __main__():
	for i in range(len(files)):
		name = "../Resources/"+ d + files[i] +".csv"
		test = caseTest.CaseTest(name, dimension, n[i], (mMu[i], seed), classes[i])
		sample = test.initTest()
		exporter.exportCaseTest(sample, name)
		c0, c1 = Sample.divideForClass(sample)
		plotter.graphSample(c0, c1)
		#plt.show()

	print("--> {} test de dimension {} fueron creados en la carpeta {}.".format(n[0], dimension, d))

__main__()
