
import numpy as np
import Muestra as muestra
import SVM as svm
import Impresora as impresora
import ExportadorArchivo as exportador
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

muestra = muestra.generarMuestra(mues2, coves2, n2, clases2)
c0,c1 = manipulador.convertirMuestraZPL(muestra)
exportador.exportarArchivoZPL(c0,'input/zplC0.csv')
exportador.exportarArchivoZPL(c1,'input/zplC1.csv')
exportador.exportarArchivoCSV(muestra,'input/input.csv')
resultClasificacion, datosPrueba = svm.clasificar('rbf', 'input/input.csv')
impresora.imprimirOutSVM(resultClasificacion, datosPrueba)






