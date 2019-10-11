ONE_ITEM_FORMAT = "%s\n"
TWO_ITEMS_FORMAT = "%s,%s\n"
THREE_ITEMS_FORMAT = "%s,%s,%s\n"





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

"""TO DO: revisar  """
def writeEliminateRedundantInstance(region, t0, route):
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

def writeSolution(regions, route):
    f = open(route, "w")
    for region in regions.values():
        for hiperplane in region:
            f.write(THREE_ITEMS_FORMAT % (hiperplane[0], hiperplane[1], hiperplane[2]))
        
    
    
    
    