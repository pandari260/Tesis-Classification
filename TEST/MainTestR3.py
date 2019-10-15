
import matplotlib.pyplot as plt  
import Plotter as plotter
import CaseTest as caseTest
import Exporter as exporter

seed = 2

name = "R3/t1-ConjuntosDisjuntos"
d = 3
n = [500, 500]
mMu = [[0,0],[6,0]]
classes = [1,0]
caso = caseTest.CaseTest(name, d, n, (mMu, seed),  classes)
caso.runTest()

name = "R3/t2-ConjuntosSolapados"
d = 3
n = [500, 500]
mMu = [[0,0],[3,0]]
classes = [1,0]
caso = caseTest.CaseTest(name, d, n, (mMu, seed), classes)
caso.runTest()


name = "R3/t3-CuadranteOpuesto"
d = 3
n = [500, 500, 500, 500]
mMu = [[0,0],[8,0],[0,8],[8,8]]
classes = [1,0,0,1]
caso = caseTest.CaseTest(name, d, n, (mMu, seed), classes)
caso.runTest()

name = "R3/t4-CuadranteOpuestoSolapado"
d = 3
n = [500, 500, 500, 500]
mMu = [[0,0],[4,0],[0,4],[4,4]]
classes = [1,0,0,1]
caso = caseTest.CaseTest(name, d, n, (mMu, seed), classes)
caso.runTest()


name = "R3/t5-Encerrado"
d = 3
n = [100, 100, 100, 100, 100, 100, 100, 100, 100]
mMu = [[0,0], [0,10], [5,5], [5,0], [10,0], [10,10], [5,10], [0,5], [10,5]]
classes = [1,1,0,1,1,1,1,1,1]
caso = caseTest.CaseTest(name, d, n, (mMu, seed), classes)
caso.runTest()

name = "R3/t6-EncerradoSolapado"
d = 3
n = [100, 100, 100, 500, 100, 100, 100, 100, 100]
mMu = [[5,0],[2,2],[8,2],[5,4],[2,5], [8,5], [5,7]]
classes = [1,1,1,0,1,1,1]
caso = caseTest.CaseTest(name, d, n, (mMu, seed), classes)
caso.runTest()


name = "R3/t7-DiagonalIntercalada"
d = 3
n = [500, 500, 500]
mMu = [[2,10],[9,8],[16,6]]
classes = [1,0,1]
caso = caseTest.CaseTest(name, d, n, (mMu, seed), classes)
caso.runTest()


name = "R3/t8-DiagonalIntercaladaSolapada"
d = 3
n = [500, 500, 500]
mMu = [[2,10],[5,8],[8,6]]
classes = [1,0,1]
caso = caseTest.CaseTest(name, d, n, (mMu, seed), classes)
caso.runTest()

