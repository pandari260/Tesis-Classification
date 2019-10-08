import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score

def printSampleR2(sampleC0, sampleC1, setHiperplan):      
    loadHiperplan(setHiperplan)
    loadSample(sampleC0, 'red')
    loadSample(sampleC1, 'blue')
    plt.show()

def loadHiperplan(setHiperplan):
    X  = np.linspace(-15,15, 10)

    for recta in setHiperplan:
        plt.plot(X, f(recta, X), color='orange')
        plt.fill_between(X, f(recta,X),-100,color='orange',alpha=.5)

def loadSample(sample, color):
    x, y = [], []
    area = np.pi*10
    for i in sample:
        x.append(i[0])
        y.append(i[1])
    plt.scatter(x, y, s=area, c=color, alpha=0.5)

def f(recta,x):
    return recta[0]*x + recta[1]*x + recta[2] 

def printOutputSVM(Y_test, y_pred):   
    print("Accuracy: ", accuracy_score(Y_test, y_pred))
    print("Confusion matrix: ")
    print(confusion_matrix(Y_test, y_pred))
    print("Metrics report: ")
    print(classification_report(Y_test, y_pred))

