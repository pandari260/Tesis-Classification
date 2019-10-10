
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

n2 = [1,1]
clases2 = [1,0]

# Se espera 0.997272
# print( coves)

sample = sample.generateSample(mues2, coves2, n2, clases2)
#c0, c1 = transform.transformSampleZPL(sample)
plotter.graphSample(sample[0], sample[1])


format = '%s,%s,%s \n'
#exporter.exportSampleZPL(c0, format, 'input/zplC0.csv')
#exporter.exportSampleZPL(c1, format, 'input/zplC1.csv')
#print(c0)

#format = ""
#for i in range(len(sample[0][0])-1):
#    format += '%s,'
#format += '%s \n'
exporter.exportSampleSVM(sample,format,'../INPUT/input.csv')

plt.show()

