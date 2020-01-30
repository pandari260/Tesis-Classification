
import pandas as pd

def searchDatafile(directory, d):
    f = '../Resources/'+directory+d+'.csv'
    fdata = pd.read_csv(f)
    dataSet = fdata.drop('Class', axis=1)
    target = fdata['Class']

    return dataSet, target
    
