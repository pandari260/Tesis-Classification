import pandas as pd
import SVM as svm
import Printer as printer

file = '../INPUT/input.csv'
dataSet = pd.read_csv(file)
sample = dataSet.drop('Class', axis=1)
target = dataSet['Class']

resultClassify, dataTest = svm.classify('rbf', dataSet, target)
printer.printOutputSVM(resultClassify, dataTest)






