import numpy as np  
import matplotlib.pyplot as plt  
import math
import Sample

def graphDataSet(sampleC0, sampleC1, setPlane, scale):
	graphSample(sampleC0, sampleC1)
	graphHyperplane(setPlane, scale)
	plt.show()

def graphHyperplane(setPlane, scale):
	for i in setPlane:
		drawHyperPlane(i, scale)

def graphSample(sampleC0, sampleC1):      
    drawSample(sampleC0, 'red')
    drawSample(sampleC1, 'blue')

def graphTest(sample):
	c0, c1 = Sample.divideClass(sample)
	graphSample(c0, c1)
	plt.show()

def drawHyperPlane(coef, scale):
	cFill, cLine = 'orange', 'black'
	if((not isZero(coef[0])) and (not isZero(coef[1]))):
		plt.plot(scale, func(coef,scale), color=cLine)
		plt.fill_between(scale, func(coef,scale), scale[0], color=cFill, alpha=0.2)
	else:
		if(isZero(coef[0])):
			y = (coef[2] / coef[1])
			plt.axhline(y, color=cLine)
			plt.axhspan(y, scale[0], alpha=0.2, color=cFill)
		else: 
			x = (coef[2] / coef[0])
			plt.axvline(x, color=cLine)
			plt.axvspan(x, scale[0], alpha=0.2, color=cFill)
	
def drawSample(sample, color):
    x, y = [], []
    area = np.pi*10.0
    for i in sample:
        x.append(i[0])
        y.append(i[1])
    plt.scatter(x, y, s=area, c=color, alpha=1)

def func(coef, scale):
    return (coef[2] - (coef[0]*scale))  / coef[1]

def isZero(coef):
	print(0.1-(math.fabs(coef)))
	if((0.1-(math.fabs(coef))) >= 0.0): return True
	else: return False
   
