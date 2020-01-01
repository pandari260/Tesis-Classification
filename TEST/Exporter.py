#Guarda en el correspondiente archivo el caso de test generado
def exportCaseTest(sample, name):
    formato = ""
    for i in range(len(sample[0][0])-1): formato += '%s,'
    formato += '%s \n'
    __exportSample(sample,formato,"Feature%s,",name)

#Escribe en archivo un conjunto de muestras
def __exportSample(sample, format, formathead, location):
    file = open(location, "w")
    for i in range(len(sample[0][0])-1): file.write(formathead % str(i+1))
    file.write('Class\n')

    for data in sample: __setFormat(data, format, file)
    file.close()

def __setFormat(sample, format, file):
    for data in sample: file.write(format % tuple(data))

#----En elaboracionn-----
def createFileOutputReal(c0, c1, name):
    formato = ""
    for i in range(0, 3): formato += '%s,'
    formato += '%s \n'
    __exportSample(c0+c1, formato,"Feature%s,",'../INPUT/REAL/SVM/'+name+'.csv')