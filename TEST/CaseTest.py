import numpy as np  
import matplotlib.pyplot as plt  
import Sample as sample
import Exporter as exporter
import TransformSample as transform
import Plotter as plotter

class CaseTest:

    def __init__(self, name, d, n, mMu, mCov, classes):
        self.name = name
        self.d = d
        self.n = n
        self.mMu = mMu
        self.mCov = mCov
        self.classes = classes

    def generateMcov(self):
        for i in range(len(self.n)):
            base = []
            for j in range(self.d):
                t = []
                for k in range(self.d):
                    if(k == j): t.append(1)
                    else: t.append(0)
                base.append(t)
            self.mCov.append(base)       

    def generateMmu(self, mu):
        for i in range(len(self.n)):
            base = []
            for j in range(self.d):
                base.append(mu[i])
            self.mMu.append(base)
            
    def groupClass(self, sample):
        c0, c1 = [], []
        for i in range(len(sample)):
            if(self.classes[i] == 0): c0 += sample[i]
            else: c1 += sample[i]
        return c0, c1

    def runTest(self):
        s = sample.generateSample(self.mMu, self.mCov, self.n, self.classes)
        self.createFileOutput(s)  
        c0, c1 = self.groupClass(s)
        plotter.graphSample(c0, c1)
        plt.show()
    
    def createFileOutput(self, sample):
        c0, c1 = transform.transformSampleZPL(sample)
        formato = '%s,%s,%s \n'
        exporter.exportSampleZPL(c0, formato, '../INPUT/CRIO/'+self.name+'C0.csv')
        exporter.exportSampleZPL(c1, formato, '../INPUT/CRIO/'+self.name+'C1.csv')

        formato = ""
        for i in range(len(sample[0][0])-1): 
            formato += '%s,'
        formato += '%s \n'
        exporter.exportSampleSVM(sample,formato,'../INPUT/SVM/'+self.name+'.csv')
    