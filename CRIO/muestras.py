#lee el archivo de muestras en formato zpl indicados en la ruta y retorna un lista de muestras en formato de tuplas.  

def listStringToInteger(list):
    l = list[:]
    for j in range(0, len(l)):
        l[j] = (int(l[j]))
    return l


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
    
    clase = []
    indice = 0
    muestra=[]
    for d in datos:
        indice = indice + 1
        muestra.append(d[2])
        if indice == dimension:
            clase.append(muestra)
            indice = 0
            muestra = []
        
    f.close()
    return clase