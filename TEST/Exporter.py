import TransformSample as transform

def exportSampleSVM(sample, format, formathead, location):
    file = open(location, "w")
    for i in range(len(sample[0][0])-1): file.write(formathead % str(i+1))
    file.write('Class\n')

    for data in sample: setFormat(data, format, file)
    file.close()

def exportSampleZPL(sample, format, location):
    file = open(location, "w")
    setFormat(sample, format, file)
    file.close()

def setFormat(sample, format, file):
    for data in sample: file.write(format % tuple(data))

def createFileOutput(sample, name):
    c0, c1 = transform.transformSampleZPL(sample)
    formato = '%s,%s,%s \n'
    exportSampleZPL(c0, formato, '../INPUT/CRIO/'+name+'C0.csv')
    exportSampleZPL(c1, formato, '../INPUT/CRIO/'+name+'C1.csv')

    formato = ""
    for i in range(len(sample[0][0])-1): formato += '%s,'
    formato += '%s \n'
    exportSampleSVM(sample,formato,"Feature%s,",'../INPUT/SVM/'+name+'.csv')

