ONE_ITEM_FORMAT = "%s\n"
TWO_ITEMS_FORMAT = "%s,%s\n"
THREE_ITEMS_FORMAT = "%s,%s,%s\n"



#toma un list de string y la transforma en una list de enteros
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
   
    clase = []
    for i in range(0, len(data) -1,2):
        clase.append(tuple(list(zip(data[i],data[i+1]))[2]))

    f.close()
    return clase

def writeGroup(group, route):
    f = open(route,"w")
    for g in group:
        f.write(TWO_ITEMS_FORMAT % (g))
    f.close()

#recibe una lista de muestras y las escribe en la ruta epecificada 
def writeSample(samples, route):
    tam = len(samples)
    print(samples)
    tam_p = len(samples[0])
    f = open(route, "w")
    for p in range(0,tam):
        for n in range(0,tam_p):
            f.write(THREE_ITEMS_FORMAT % (p,n,samples[p][n]))
    f.close()

def writeParameters(params, route):
    f = open(route,"w")
    for p in params:
        f.write(ONE_ITEM_FORMAT % (p))
    f.close()

#recibe una lista de clusters y lo escribe en un archivo interpretable por zimpl 
def writeClusters(clusters, samples, route):
    lenSamples = len(samples)
    f = open(route, "w")

    for s in range(0, lenSamples):
        key = clusters.getSampleKey(samples[s])
        f.write(TWO_ITEMS_FORMAT % (s,key))
    f.close()

def writeRegion(region, t0, route):
    f = open(route, "w")
    f.write(ONE_ITEM_FORMAT % (t0))
    lenReg = len(region)
    lenHiper = len(region[0])
    for i in range(0,lenReg):
        for j in range(0, lenHiper-1):
            f.write(THREE_ITEMS_FORMAT % (i,j,region[i][j]))
    
    for i in range(0,lenReg):
        f.write(TWO_ITEMS_FORMAT % (i, region[i][2]))
    
    

    f.close()