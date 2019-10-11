
import numpy as np  
import matplotlib.pyplot as plt  
import Sample as sample
import Exporter as exporter
import TransformSample as transform
import Plotter as plotter
name = "t1d2-ConjuntosDisjuntos"
import CaseTest as caseTest

d = 2
n = [500, 500]
mMu = [[0,0],[6,0]]
classes = [1,0]
mCov = []
caso = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso.runTest()


name = "t2d2-ConjuntosSolapados"
d = 2
n = [500, 500]
mMu = [[0,0],[3,0]]
classes = [1,0]
mCov = []
caso = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso.runTest()


name = "t3d2-ConjuntosDiagonalizados"
d = 2
n = [500, 500]
mMu = [[0,0],[0.3,0]]
classes = [1,0]
mCov = [[[10,100],[10,100]], [[10,100],[10,100]]]
caso = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso.runTest()



name = "t4d2-ConjuntosDiagonalizadosSolapados"
d = 2
n = [500, 500]
mMu = [[0,0],[0,0]]
classes = [1,0]
mCov = [[[10,100],[10,100]], [[10,100],[10,100]]]
caso = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso.runTest()


name = "t5d2-ConjuntosCruz"
d = 2
n = [500, 500]
mMu = [[0,0],[0,0]]
classes = [1,0]
mCov = [[[10,10],[5000,10]], [[10,10],[1000,1000]]]
caso = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
#caso.runTest()


name = "t6d2-CuadranteOpuesto"
d = 2
n = [500, 500, 500, 500]
mMu = [[0,0],[6,0],[0,8],[6,8]]
classes = [1,0,1,0]
mCov = []
caso = caseTest.CaseTest(name, d, n, mMu, mCov, classes)
caso.runTest()


"""

#------------------ graficar hyperplanos y muestras -------------#
"""sampleC0 = [(1,1),(2,2),(1.3,1.5),(1.7,1.8)]
sampleC1 = [(3,3),(5,5),(5.3,5.5),(6.7,6.8)]
setPlane = [(2,3,10),(0,3,10),(2,0,10),(-3,5,30),(-20,4,10)]
n = np.linspace(-100,100, 100)
plotter.graphDataSet(sampleC0, sampleC1, setPlane, n)

plt.show()

