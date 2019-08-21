
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

n2 = [50,50,10]
clases2 = [1,0,1]

# Se espera 0.997272
#print( coves)

muestra = muestra.generarMuestra(mues2, coves2, n2, clases2)
m2 = manipulador.convertirMuestraZPL(muestra)
print(m2)
exportador.exportarArchivoCSV(muestra,'input/input.csv')
resultClasificacion, datosPrueba = svm.clasificar('rbf', 'input/input.csv')
impresora.imprimirOutSVM(resultClasificacion, datosPrueba)






