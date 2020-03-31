

class MetricsClassifier():
    
    ROW_METRIC = "\t{}\t{:f}\t{:f}\t{:f}\t{}"
    
    def __init__(self, clas, TP, FP, TN, FN):
        self._clas = clas
        self._TP = TP
        self._FP = FP
        self._TN = TN
        self._FN = FN
    
    def showMetrics(self):
        return self.ROW_METRIC.format(self._clas, self.__getPresicion(), self.__getRecall(), self.__getF1Score(), self.__getSupport())
    
    def getAccuracy(self):
        return (self._TP + self._TN)/(self._TP + self._FP + self._TN + self._FN)
    
    def __getPresicion(self):
        return  self._TP/(self._TP + self._FP)
    
    def __getRecall(self):
        return self._TP/(self._TP + self._FN)
    
    def __getF1Score(self):
        return (2*(self.__getPresicion()*self.__getRecall())) / (self.__getPresicion() + self.__getRecall())
        
    def __getSupport(self):
        return int(self._TP + self._FP + self._TN + self._FN)
   