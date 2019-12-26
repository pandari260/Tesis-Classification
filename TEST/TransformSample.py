import Sample

def transformSample(sampleGenerated, clss):
    sample, data = [],[]
    for i in range(len(sampleGenerated[0])): 
        for j in range(len(sampleGenerated)):
            data.append(round(sampleGenerated[j][i],4)) #Solo se incluyen hasta los 5 decimales
        data.append(clss)
        sample.append(data)
        data = []
    return sample    

def transformSampleZPL(sample): 
    sampleC0, sampleC1 = Sample.divideClass(sample)
    return setFormatZPL(sampleC0), setFormatZPL(sampleC1)

def setFormatZPL(sample):
    preSample, newSample = [], []
    for i in range(len(sample)):
        for j in range(len(sample[0])-1):
            preSample.append(i)
            preSample.append(j)
            preSample.append(sample[i][j])
            newSample.append(preSample)
            preSample = []
    return newSample

