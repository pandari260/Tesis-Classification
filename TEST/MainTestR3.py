
import matplotlib.pyplot as plt  
import Plotter as plotter
import CaseTest as caseTest
import Exporter as exporter

name = "R3/t1d3-ConjuntosDisjuntos"
d = 3
n = [500, 500]
mMu, mCov = [], []
classes = [1,0,1]
caso1 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
caso1.generateMcov()
caso1.generateMmu([0,6])
#caso1.runTest()


name = "R3/t2d3-ConjuntosSolapados"
d = 3
n = [500, 500]
mMu, mCov = [], []
classes = [1,0]
caso2 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
caso2.generateMcov()
caso2.generateMmu([0,2.5])
#caso2.runTest()


name = "R3/t3d3-ConjuntosDiagonalizados"
d = 3
n = [500, 500]
mMu = []
classes = [1,0]
mCov = [[[10,100,0],[10,100,0],[10,100,0]], [[10,100,0],[10,100,0],[10,100,0]]]
caso3 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
caso3.generateMmu([0,0])
caso3.runTest()
