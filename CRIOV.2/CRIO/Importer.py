from CRIO.Modelo.SampleContainer import SampleContainer
def listStringToFloat(list):
    l = list[:]
    for j in range(0, len(l)):
        l[j] = (float(l[j]))
    return l

#lee el archivo de muestras en formato zpl indicados en la ruta y retorna un lista de muestras en formato de tuplas.  
def readSamples(route, dimension):
    f = open(route,"r")
    lines = f.readlines()#f
    lines = lines[1:len(lines)]
    lines = list(map(lambda line: line[:-1], lines))
    lines = list(map(lambda line: line.split(","), lines))
    lines = list(map(lambda line: listStringToFloat(line), lines))  
    data0 = SampleContainer(map(lambda spl: tuple(spl),filter(lambda spl: spl[dimension] == 0, lines)),dimension)
    data1 = SampleContainer(map(lambda spl: tuple(spl),filter(lambda spl: spl[dimension] == 1, lines)),dimension)
    
    
    return data0,data1