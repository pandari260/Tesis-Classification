import pandas as pd

def obtenerMuestraSVM(archivo):
    dataSet = pd.read_csv(archivo)
    datos = dataSet.drop('Class', axis=1)
    target = dataSet['Class']
    return datos, target   

def convertirMuestraZPL(muestra): 
    muestraC0, muestraC1, indiceC0, indiceC1 = [], [], 0, 0
    for item in muestra:
        if(getClase(item) == 0):
          muestraC0.append(darFormatoZPL(item, indiceC0+1))
          indiceC0 = len(item)
        else:
          muestraC1.append(darFormatoZPL(item, indiceC1+1))
          indiceC1 = len(item)
    return muestraC1, muestraC0

def getClase(item):
    tamano = len(item[0])
    if(item[0][tamano-1] == 0): return 0
    else: return 1

def darFormatoZPL(item, indice):
    muestra, preMuestra = [], []
    for i in range(len(item)):
        for j in range(len(item[0])-1):
            preMuestra.append(indice+i)
            preMuestra.append(j+1)
            preMuestra.append(item[i][j])
            muestra.append(preMuestra)
            preMuestra = []
    return muestra