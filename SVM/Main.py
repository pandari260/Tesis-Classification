
import numpy as np
import Sample as sample
import SVM as svm
import Printer as printer
import Exporter as exporter
import ManipuladorMuestral as manipulador




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

n2 = [100,100,100]
clases2 = [1,0,1]

# Se espera 0.997272
#print( coves)

sample = sample.generateSample(mues2, coves2, n2, clases2)
c0,c1 = manipulador.convertirMuestraZPL(sample)
exporter.exportSampleZPL(c0,'input/zplC0.csv')
exporter.exportSampleZPL(c1,'input/zplC1.csv')
exporter.exportSampleSVM(sample,'input/input.csv')
resultClassify, dataTest = svm.classify('rbf', 'input/input.csv')
printer.printOutputSVM(resultClassify, dataTest)






