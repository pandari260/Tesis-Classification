
import numpy as np  
import matplotlib.pyplot as plt  
import Sample as sample
import Exporter as exporter
import TransformSample as transform
import sys
import Plotter as plotter

# input ------------------------------------------
mues = [   [0,0,0],
           [4,4,4],
           [6,6,6] ]
        
coves = [   [[1,0,0],[0,1,0],[0,0,1]], 
            [[1,0,0],[0,1,0],[0,0,1]],
            [[1,0,0],[0,1,0],[0,0,1]]  ]

n = [10,10, 10]
clases = [1,0,1]


mues2 = [   [0,0],
           [6,6] ]
        
coves2 = [   [[1,0],[0,1]], 
            [[1,0],[0,1]] ]

n2 = [10,10]
clases2 = [1,0]

# Se espera 0.997272
# print( coves)

sample = sample.generateSample(mues2, coves2, n2, clases2)
c0, c1 = transform.transformSampleZPL(sample)
plotter.graphSample(sample[0], sample[1])

#------- Format standard for CRIO --------------------#
format = '%s,%s,%s \n'
exporter.exportSampleZPL(c0, format, '../INPUT/CRIO/zplC0.csv')
exporter.exportSampleZPL(c1, format, '../INPUT/CRIO/zplC1.csv')

#------- Format standard for SVM --------------------#
format = ""
for i in range(len(sample[0][0])-1): 
    format += '%s,'
format += '%s \n'
exporter.exportSampleSVM(sample,format,'../INPUT/SVM/input.csv')




plt.show()

sampleC0 = [(1,1),(2,2),(1.3,1.5),(1.7,1.8)]
sampleC1 = [(3,3),(5,5),(5.3,5.5),(6.7,6.8)]
setPlane = [(2,3,10),(0,3,10),(2,0,10),(-3,5,30),(-20,4,10)]

n = np.linspace(-100,100, 100)
plotter.graphDataSet(sampleC0, sampleC1, setPlane, n)

plt.show()

