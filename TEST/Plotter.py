import numpy as np  
import matplotlib.pyplot as plt  

def f(coef, scale):
    return (coef[2] - (coef[0]*scale))  / coef[1]

def drawHyperPlane(coef, scale):
	cFill, cLine = 'orange', 'black'
	if(coef[0] != 0 and coef[1]!=0):
		plt.plot(scale, f(coef,scale), color=cLine)
		plt.fill_between(scale, f(coef,scale), scale[0], color=cFill, alpha=0.2)
	else:
		if(coef[0] == 0):
			y = (coef[2] / coef[1])
			plt.axhline(y, color=cLine)
			plt.axhspan(y, scale[0], alpha=0.2, color=cFill)
		else: 
			x = (coef[2] / coef[0])
			plt.axvline(x, color=cLine)
			plt.axvspan(x, scale[0], alpha=0.2, color=cFill)
	
	
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



