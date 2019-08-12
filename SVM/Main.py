import GraficadorNormal as graficador
import GeneradorMuestras as generador
import TraductorMuestra as traductor
import numpy as np

gen = generador.GeneradorMuestras()
graf = graficador.GraficadorNormal()
traduc = traductor.TraductorMuestra()


muestraClase1 = gen.generarNdimensional(0,1,5,1000)
muestrasGeneradasC1 = traduc.traducirMuestra(muestraClase1,1)

muestraClase2 = gen.generarNdimensional(3,1,5,1000)
muestrasGeneradasC2 = traduc.traducirMuestra(muestraClase2,0)

muestraClase1a = gen.generarNdimensional(1,1,5,1000)
muestrasGeneradasC1a = traduc.traducirMuestra(muestraClase1a,1)

#print(muestrasGeneradasC1+muestrasGeneradasC2)
x,y = gen.generarNdimensional(0,100,2,100)
#graf.graficarBidimensional(x, y)
#graf.graficarBidimensional(xx,yy)
traduc.generarArchivoCSV(muestrasGeneradasC1+muestrasGeneradasC2+muestrasGeneradasC1a)





