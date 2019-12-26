import numpy as np  
import matplotlib.pyplot as plt  
import Sample as sample
import Exporter as exporter
import TransformSample as transform
import Plotter as plotter

class CaseTest:

    def __init__(self, name, d, n, mMu, classes):
        self.name = name
        self.d = d
        self.n = n
        self.mMu = self.initMu(mMu[0],mMu[1])
        self.mCov = self.initCov()
        self.classes = classes

    def initCov(self):
        m = []
        for i in range(len(self.n)):
            base = np.identity(self.d)
            m.append(base)    
        return m   

    def initMu(self, mu, seed):
        m = []
        for i in mu:
            base = []
            base.append(i[0])
            base.append(i[1])
            for j in range(self.d-2): base.append(seed)
            m.append(base)
        return m

    def initTest(self):
        return sample.generateSample(self.mMu, self.mCov, self.n, self.classes)