from CRIO.Modelo.SampleContainer import SampleContainer
import csv
def listStringToFloat(list):
    l = list[:]
    for j in range(0, len(l)):
        l[j] = (float(l[j]))
    return l
'''
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
'''
def readSample(name):
    c0, c1 = [], []
    with open(name, 'r') as csvfile:
        aux_set_data = csv.reader(csvfile, delimiter=',')
        next(aux_set_data )
        aux_set_data = list(aux_set_data )
        c0 = list(map(lambda k: tuple(map(lambda i: float(i), k)), list(map(lambda j: j[:-1], list(filter(lambda l: int(l[-1]) == 0, aux_set_data))))))
        c1 = list(map(lambda k: tuple(map(lambda i: float(i), k)), list(map(lambda j: j[:-1], list(filter(lambda l: int(l[-1]) == 1, aux_set_data))))))
    return c0, c1
