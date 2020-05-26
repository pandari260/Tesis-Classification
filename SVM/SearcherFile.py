
import pandas as pd

def searchDatafile(directory, d):
    f = '../Resources/'+directory+d+'.csv'    
    fdata, listN = pd.read_csv(f), []
    for row in range(len(fdata['Feature1'])):
        if(fdata['Feature1'][row][0] == "*"):
            listN.append(row)

    fdata = fdata.drop(index= fdata.index[listN])
    dataSet = fdata.drop('Class', axis=1)
    target = fdata['Class']

    return dataSet, target

    
