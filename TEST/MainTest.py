
import matplotlib.pyplot as plt  
import Plotter as plotter
import CaseTest as caseTest
import Exporter as exporter
import numpy as np

seed = 2
dimension = 2
d = "R2"
flag = False

name = d+"/t1-ConjuntosDisjuntos"
n = [500, 500]
mMu = [[0,0],[6,0]]
classes = [1,0]
caso = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
caso.runTest(flag)

name = d+"/t2-ConjuntosSolapados"
n = [500, 500]
mMu = [[0,0],[3,0]]
classes = [1,0]
caso = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
caso.runTest(flag)

name = d+"/t3-CuadranteOpuesto"
n = [500, 500, 500, 500]
mMu = [[0,0],[8,0],[0,8],[8,8]]
classes = [1,0,0,1]
caso = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
caso.runTest(flag)

name = d+"/t4-CuadranteOpuestoSolapado"
n = [500, 500, 500, 500]
mMu = [[0,0],[4,0],[0,4],[4,4]]
classes = [1,0,0,1]
caso = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
caso.runTest(flag)

name = d+"/t5-Encerrado"
n = [100, 100, 100, 100, 100, 100, 100, 100, 100]
mMu = [[0,0], [0,10], [5,5], [5,0], [10,0], [10,10], [5,10], [0,5], [10,5]]
classes = [1,1,0,1,1,1,1,1,1]
caso = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
caso.runTest(flag)

name = d+"/t6-EncerradoSolapado"
n = [100, 100, 100, 500, 100, 100, 100, 100, 100]
mMu = [[5,0],[2,2],[8,2],[5,4],[2,5], [8,5], [5,7]]
classes = [1,1,1,0,1,1,1]
caso = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
caso.runTest(flag)

name = d+"/t7-DiagonalIntercalada"
n = [500, 500, 500]
mMu = [[2,10],[9,8],[16,6]]
classes = [1,0,1]
caso = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
caso.runTest(flag)

name = d+"/t8-DiagonalIntercaladaSolapada"
n = [500, 500, 500]
mMu = [[2,10],[5,8],[8,6]]
classes = [1,0,1]
caso = caseTest.CaseTest(name, dimension, n, (mMu, seed), classes)
caso.runTest(flag)

"""
name = "R2/t9-Piramide"
c0 = [(5,10),(5,9.8),(4.9,9.8),(5.1,9.8),(5.2,9.8),(4.8,9.8)]
c1 = [(5,9.9),(4.9,9.9),(5.1,9.9)]
plotter.graphSample(c0, c1)
plt.show()
"""

"""
c0 = [(4.0, 5.0), (4.0, 3.0), (5.0, 4.0)]
c1 = [(4.0, 4.0), (6.0, 4.0)]
h = [(0.0, -1.99999991038, -6.99999968634),(1.9999999, 1.9999999, 16.99999915),(-0.799999960993,-0.399999980101,-5.39999973532),(-1.99999990568, 0.00043, -10.9999994659)]
n = np.linspace(-10,10,3000)
plotter.graphDataSet(c0,c1,h,n)"""
