
import numpy as np  
import matplotlib.pyplot as plt  
import Sample as sample
import Exporter as exporter
import TransformSample as transform
import sys
import Plotter as plotter

d = 2
n = [100, 100, 100]
mu = [0,5,10]
clases = [1,0,1]


mMu, mCov = [], []

for i in range(len(n)):
    t = []
    for j in range(d):
        t.append(mu[i])
    mMu.append(t)

for i in range(len(n)):
    base = []
    for j in range(d):
        t = []
        for k in range(d):
            if(k == j): t.append(1)
            else: t.append(0)
        base.append(t)
    mCov.append(base)           

print(mCov)
print(mMu)



sample = sample.generateSample(mMu, mCov, n, clases)
#c0, c1 = transform.transformSampleZPL(sample)
plotter.graphSample(sample[0]+sample[2], sample[1])
print(sample[0])
#------- Format standard for CRIO --------------------#
format = '%s,%s,%s \n'
#exporter.exportSampleZPL(c0, format, '../INPUT/CRIO/zplC0.csv')
#exporter.exportSampleZPL(c1, format, '../INPUT/CRIO/zplC1.csv')

#------- Format standard for SVM --------------------#
format = ""
for i in range(len(sample[0][0])-1): 
   format += '%s,'
format += '%s \n'
exporter.exportSampleSVM(sample,format,'../INPUT/SVM/input.csv')

plt.show()

#------------------ graficar hyperplanos y muestras -------------#
#sampleC0 = [(1,1),(2,2),(1.3,1.5),(1.7,1.8)]
#sampleC1 = [(3,3),(5,5),(5.3,5.5),(6.7,6.8)]
#setPlane = [(2,3,10),(0,3,10),(2,0,10),(-3,5,30),(-20,4,10)]

#n = np.linspace(-100,100, 100)
#plotter.graphDataSet(sampleC0, sampleC1, setPlane, n)

#plt.show()

