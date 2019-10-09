import numpy as np  
import matplotlib.pyplot as plt  

def f(coef, scale):
    return (coef[2] - (coef[0]*scale))  / coef[1]

def drawHyperPlane(coef, scale):
	c = 'orange'
	if(coef[0] != 0 and coef[1]!=0):
		plt.plot(scale, f(coef,scale))
		plt.fill_between(scale, f(coef,scale), scale[0], color=c, alpha=0.3)
	else:
		if(coef[0] == 0):
			y = (coef[2] / coef[1])
			plt.axhline(y)
			plt.axhspan(y, scale[0], alpha=0.3, color=c)
		else: 
			x = (coef[2] / coef[0])
			plt.axvline(x)
			plt.axvspan(x, scale[0], alpha=0.3, color=c)
	
	
def graphHyperplane(setPlane, scale):
	for i in setPlane:
		drawHyperPlane(i, scale)

def graphSample(sampleC0, sampleC1):      
    drawSample(sampleC0, 'red')
    drawSample(sampleC1, 'blue')

def drawSample(sample, color):
    x, y = [], []
    area = np.pi*10
    for i in sample:
        x.append(i[0])
        y.append(i[1])
    plt.scatter(x, y, s=area, c=color, alpha=1)

def graphDataSet(sampleC0, sampleC1, setPlane, scale):
	graphSample(sampleC0, sampleC1)
	graphHyperplane(setPlane, scale)
	plt.show()

#sampleC0 = [(1,1),(2,2),(1.3,1.5),(1.7,1.8)]
#sampleC1 = [(3,3),(5,5),(5.3,5.5),(6.7,6.8)]
#setPlane = [(2,3,10),(0,3,10),(2,0,10)]

#n = np.linspace(-100,100, 100)
#graphDataSet(sampleC0, sampleC1, setPlane, n)



