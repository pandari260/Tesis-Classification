import pandas as pd

def obtenerMuestraSVM(archivo):
    dataSet = pd.read_csv(archivo)
    datos = dataSet.drop('Class', axis=1)
    target = dataSet['Class']
    return datos, target   

def convertirMuestraZPL(muestra): 
    muestraC0, muestraC1 = separarClases(muestra)
    return darFormatoZPL(muestraC0), darFormatoZPL(muestraC1)

def separarClases(muestra):
    muestraC0, muestraC1 = [], []
    for item in muestra:
        if(getClase(item[0]) == 0): muestraC0 += item
        else: muestraC1 += item
    return muestraC0, muestraC1

def getClase(item):
    if(item[len(item)-1] == 0): return 0
    else: return 1

def darFormatoZPL(muestra):
    preMuestra, newMuestra = [], []
    for i in range(len(muestra)):
        for j in range(len(muestra[0])-1):
            preMuestra.append(i+1)
            preMuestra.append(j+1)
            preMuestra.append(muestra[i][j])
            newMuestra.append(preMuestra)
            preMuestra = []
    return newMuestra


