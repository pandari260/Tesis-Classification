
import numpy as np  
import matplotlib.pyplot as plt  
import Sample as sample
import Exporter as exporter
import TransformSample as transform
import Plotter as plotter
import CaseTest as caseTest

name = "t1d2-ConjuntosDisjuntos"
d = 2
n = [500, 500]
mMu = [[0,0],[6,0]]
classes = [1,0]
mCov = []
caso1 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso1.runTest()


name = "t2d2-ConjuntosSolapados"
d = 2
n = [500, 500]
mMu = [[0,0],[3,0]]
classes = [1,0]
mCov = []
caso2 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso2.runTest()


name = "t3d2-ConjuntosDiagonalizados"
d = 2
n = [500, 500]
mMu = [[0,0],[0.3,0]]
classes = [1,0]
mCov = [[[10,100],[10,100]], [[10,100],[10,100]]]
caso3 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso3.runTest()



name = "t4d2-ConjuntosDiagonalizadosSolapados"
d = 2
n = [500, 500]
mMu = [[0,0],[0,0]]
classes = [1,0]
mCov = [[[10,100],[10,100]], [[10,100],[10,100]]]
caso4 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso4.runTest()


name = "t5d2-ConjuntosCruz"
d = 2
n = [500, 500]
mMu = [[0,0],[0,0]]
classes = [0,1]
mCov = [[[10,10],[5000,10]], [[10,10],[1000,1000]]]
caso5 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso5.runTest()


name = "t6d2-CuadranteOpuesto"
d = 2
n = [500, 500, 500, 500]
mMu = [[0,0],[8,0],[0,8],[8,8]]
classes = [1,0,0,1]
mCov = []
caso6 = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso6.runTest()
