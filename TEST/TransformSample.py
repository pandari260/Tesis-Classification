
def transformSampleZPL(sample): 
    sampleC0, sampleC1 = divideClass(sample)
    return setFormatZPL(sampleC0), setFormatZPL(sampleC1)

def divideClass(sample):
    sampleC0, sampleC1 = [], []
    for item in sample:
        if(getClass(item[0]) == 0): sampleC0 += item
        else: sampleC1 += item
    return sampleC0, sampleC1

def getClass(item):
    if(item[len(item)-1] == 0): return 0
    else: return 1

def setFormatZPL(sample):
    preSample, newSample = [], []
    for i in range(len(sample)):
        for j in range(len(sample[0])-1):
            preSample.append(i+1)
            preSample.append(j+1)
            preSample.append(sample[i][j])
            newSample.append(preSample)
            preSample = []
    return newSample

