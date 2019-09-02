
    
def exportSampleSVM(sample, location):
    generateHeader(sample, location, "w")        
    file = open(location, "a")
    for data in sample:
        setFormat(data, file)
    file.close()

def exportSampleZPL(sample, location):
    file = open(location, "w")
    setFormat(sample, file)
    file.close()

def generateHeader(sample, location, target):
    file = open(location, target)
    for i in range(len(sample[0][0])-1):
        file.write("Feature"+str(i+1)+",")
    file.write('Class\n')
    file.close()

def setFormat(sample, file):
    for data in sample:
        for j in range(len(data)):
            file.write(str(data[j]))
            if(j!=len(data)-1):
                file.write(",")
        file.write("\n")


