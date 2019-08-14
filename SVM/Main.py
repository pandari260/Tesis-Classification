import GraficadorMuestral as graficador
import GeneradorMuestral as generador
import ConversorMuestral as conversor
import ExportadorArchivo as exportador
import ClasificadorSVM as clasificador
import numpy as np

gen = generador.GeneradorMuestral()
graf = graficador.GraficadorMuestral()
conver = conversor.ConversorMuestral()
exp = exportador.ExportadorArchivo()
clas = clasificador.ClasificadorSVM()

muestraClase1 = gen.generarMuestraDN(0,1,3,100)
muestrasGeneradasC1 = conver.convertirMuestra(muestraClase1,1)

muestraClase2 = gen.generarMuestraDN(2,1,3,100)
muestrasGeneradasC2 = conver.convertirMuestra(muestraClase2,0)

print("Clase a la que pertenece: "+str(conver.getClase((0.6731,2.2481,-1.6543))))

#print(muestrasGeneradasC1+muestrasGeneradasC2)
#x,y = gen.generarNdimensional(0,100,2,100)
#graf.graficarBidimensional(x, y)
#graf.graficarBidimensional(xx,yy)
exp.exportarArchivoCSV(muestrasGeneradasC1+muestrasGeneradasC2)
#clas.clasificarMuestra()

clas.clasificarMuestra('input/input.csv')




