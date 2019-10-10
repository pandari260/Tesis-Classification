
    
def exportSampleSVM(sample, format, location):
    generateHeader(sample[0], location, "w")    
    file = open(location, "a")
    for data in sample:
        setFormat(data, format, file)
    file.close()

def exportSampleZPL(sample, format, location):
    file = open(location, "w")
    setFormat(sample, format, file)
    file.close()

def generateHeader(sample, location, target):
    file = open(location, target)
    for i in range(len(sample[0])-1):
        file.write("Feature"+str(i+1)+",")
    file.write('Class\n')
    file.close()

def setFormat(sample, format, file):
    for data in sample:
        file.write(format % tuple(data))


