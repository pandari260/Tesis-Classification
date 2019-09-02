
import numpy as np
import Sample as sample
import SVM as svm
import Printer as printer
import Exporter as exporter
import TransformSample as transform




# input ------------------------------------------
mues = [   [0,0,0],
           [4,4,4],
           [6,6,6] ]
        
coves = [   [[1,0,0],[0,1,0],[0,0,1]], 
            [[1,0,0],[0,1,0],[0,0,1]],
            [[1,0,0],[0,1,0],[0,0,1]]  ]

n = [100,100, 100]
clases = [1,0,1]


mues2 = [   [0,0],
           [3,3],
           [5,5] ]
        
coves2 = [   [[1,0],[0,1]], 
            [[1,0],[0,1]],
            [[1,0],[0,1]] ]

n2 = [5,5,5]
clases2 = [1,0,1]

# Se espera 0.997272
# print( coves)

sample = sample.generateSample(mues2, coves2, n2, clases2)
c0,c1 = transform.transformSampleZPL(sample)
#print(sample)
exporter.exportSampleZPL(c0,'%s,%s,%s \n', 'input/zplC0.csv')
exporter.exportSampleZPL(c1,'%s,%s,%s \n', 'input/zplC1.csv')
print(c0)
#exporter.exportSampleSVM(sample,'%s,%s,%s \n','input/input.csv')
#resultClassify, dataTest = svm.classify('rbf', 'input/input.csv')
#printer.printOutputSVM(resultClassify, dataTest)






