def listStringToInteger(list):
    l = list[:]
    for j in range(0, len(l)):
        l[j] = (int(l[j]))
    return l

#lee el archivo de muestras en formato zpl indicados en la ruta y retorna un lista de muestras en formato de tuplas.  
def readSamples(route, dimension):
    f = open(route,"r")
    lines = f.readlines()
    
    lines = list(map(lambda line: line[:-1], lines))
    lines = list(map(lambda line: line.split(","), lines))
    data = list(map(lambda line: listStringToInteger(line), lines))        
    print("data: " + str(data))
    clase = []
    sample = []

    for i in range(0, len(data) -1,dimension):
        for j in range(0, dimension):
            sample.append(data[i][2])
        clase.append(tuple(sample))
        sample = []

    f.close()
    return clase