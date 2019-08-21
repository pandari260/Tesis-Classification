
import numpy as np
import Muestra2 as muestr
import SVM as svm
import ExportadorArchivo as exportador




# input ------------------------------------------
mues = [   [0,0,0],
           [4,4,4],
           [6,6,6] ]
        
coves = [   [[1,0,0],[0,1,0],[0,0,1]], 
            [[1,0,0],[0,1,0],[0,0,1]],
            [[1,0,0],[0,1,0],[0,0,1]]  ]

n = [5000,5000, 5000]
clases = [1,0,0]

# Se espera 0.997272
#print( coves)

muestra = muestr.generarMuestra(mues, coves, n, clases)
exportador.exportarArchivoCSV(muestra,'input/input.csv')
svm.clasificar('rbf', 'input/input.csv')




#dato = [(0.026, 0.2603, 453,4),(0.026, 0.2603, 45356,5),(0.026, 0.2603, 76445,6),(0.026, 0.2603, 6546, 23,7)]

#print(muestraClase1)
#print(gen.convertirMuestraZPL(dato))

#print("Clase a la que pertenece: "+str(consul.consultarClase((-0.4995,0.6731))))

#esp = [4,4]
#cov = [[1,0],[0,1]]
#np.random.seed(45)  
#x,y = np.random.multivariate_normal(esp, cov, 5000).T
#x,y = gen.generarMuestraDN(0,100,2,100)
#graf.graficarBidimensional(x,y)
#exp.exportarArchivoCSV(muestraClase1+muestraClase2, "input/input.csv")

#clas.clasificar('input/input.csv')




