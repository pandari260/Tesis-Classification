import GraficadorNormal as graficador
import GeneradorMuestras as generador
import TraductorMuestra as traductor
import numpy as np

gen = generador.GeneradorMuestras()
graf = graficador.GraficadorNormal()
traduc = traductor.TraductorMuestra()

muestra = gen.generarNdimensional(3,1000)
muestrasGeneradas = traduc.traducirACSV(muestra)

print('Conjunto de muestras generadas')
#print(muestrasGeneradas)

x,y = gen.generarNdimensional(2,500)
graf.graficarBidimensional(x,y)

traduc.generarArchivoCSV(muestrasGeneradas)





