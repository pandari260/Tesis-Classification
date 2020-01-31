import numpy as np  
import matplotlib.pyplot as plt  
import math
import Sample

scale = np.linspace(-5,5,1000)

#Dado los conjuntos de clase0,clase1 e hiperplanos, este los grafica en la escala definida.
def graphDataSet(sampleC0, sampleC1, setPlane):
	plt.axis([-5,5,-5,5])
	graphSample(sampleC0, sampleC1)
	graphHyperplane(setPlane)
	plt.show()

#Grafica el conjunto de hiperplanos pasado por parametro.
def graphHyperplane(setPlane):
	for i in setPlane:	__drawHyperPlane(i)

#Grafica el conjunto de muestras de clase0 y clase1.
def graphSample(sampleC0, sampleC1):
	__drawSample(sampleC0, 'red')
	__drawSample(sampleC1, 'blue')

#Dibuja un hiperplano
def __drawHyperPlane(coef):
	cFill, cLine = 'black', 'black'
	n = scale[0]*coef[2]
	if((not __isZero(coef[0])) and (not __isZero(coef[1]))):
		plt.plot(scale, __func(coef), color=cLine)
		plt.fill_between(scale, __func(coef), n, color=cFill, alpha=0.1)
	else:
		if(__isZero(coef[0])):
			y = (coef[2] / coef[1])
			plt.axhline(y, color=cLine)
			plt.axhspan(y, n, alpha=0.1, color='green')
		else: 
			x = (coef[2] / coef[0])
			plt.axvline(x, color=cLine)
			plt.axvspan(x, n, alpha=0.1, color='blue')

#Dibuja un par de coordenadas (x,y)
def __drawSample(sample, color):
    x, y = [], []
    area = np.pi*10.0
    for i in sample:
        x.append(i[0])
        y.append(i[1])
    plt.scatter(x, y, s=area, c=color, alpha=1)

#Funcion de la pinta (c - a) / b
def __func(coef):
    return (coef[2] - (coef[0]*scale))  / coef[1]

def __isZero(coef):
	print(0.1-(math.fabs(coef)))
	return True if((0.1-(math.fabs(coef))) >= 0.0) else False
   
