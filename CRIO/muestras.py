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
def leerMuestras(ruta, dimension):
    f = open(ruta,"r")
    lineas = f.readlines()
    datos = []
    
    #eliminar los saltos de linea del final
    for i in range(0,len(lineas)):
        fila = lineas[i].split(",")
        if i < len(lineas) -1:
            fila[2] = fila[2][:-1]
        fila = listStringToInteger(fila)
        datos.append(fila)   
    
    clase = dict()
    indice = 0
    muestra=[]
    for d in datos:
        indice = indice + 1
        muestra.append(d[2])
        if indice == dimension:
            clase.append(tuple(muestra))
            indice = 0
            muestra = []
        
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
    tam_p = len(samples[0])
    f = open(route, "w")
    for p in range(0,tam):
        for n in range(0,tam_p):
            f.write(THREE_ITEMS_FORMAT % (p,n,samples[p][n]))
    f.close()

def writeParams(params, route):
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