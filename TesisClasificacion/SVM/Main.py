import pandas as pd
import SVM.SVM as svm
import SVM.Printer as printer


file = '../INPUT/SVM/input.csv'

fdata = pd.read_csv(file)
dataSet = fdata.drop('Class', axis=1)
target = fdata['Class']

resultClassify, dataTest = svm.classify('rbf', dataSet, target)
printer.printOutputSVM(resultClassify, dataTest)



