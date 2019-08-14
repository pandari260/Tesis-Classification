import GraficadorMuestral as graficador
import GeneradorMuestral as generador
import ParserMuestral as parser
import ExportadorArchivo as exportador
import ClasificadorSVM as clasificador
import numpy as np

gen = generador.GeneradorMuestral()
graf = graficador.GraficadorMuestral()
parser = parser.ParserMuestral()
exp = exportador.ExportadorArchivo()
clas = clasificador.ClasificadorSVM('rbf')

muestraClase1 = gen.generarMuestraDN(0,1,2,1000)
muestrasGeneradasC1 = parser.parsearMuestra(muestraClase1,1)

muestraClase2 = gen.generarMuestraDN(3,1,2,1000)
muestrasGeneradasC2 = parser.parsearMuestra(muestraClase2,0)

#print("Clase a la que pertenece: "+str(parser.getClase((0.6731,2.2481,-1.6543))))

esp = [5,5]
cov = [[1,0],[0,1]]
np.random.seed(45)  
x,y = np.random.multivariate_normal(esp, cov, 2000).T
#x,y = gen.generarMuestraDN(0,100,2,100)
graf.graficarBidimensional(x, y)
#exp.exportarArchivoCSV(muestrasGeneradasC1+muestrasGeneradasC2)

#clas.clasificarMuestra('input/input.csv')




