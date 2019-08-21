import pandas as pd

def obtenerMuestraSVM(archivo):
    dataSet = pd.read_csv(archivo)
    datos = dataSet.drop('Class', axis=1)
    target = dataSet['Class']
    return datos, target   

def convertirMuestraZPL(muestra): 
    nuevaMuestra, dato = [], []
    for i in range(len(muestra)):
        for j in range(len(muestra[i])):
            dato.append(i+1)
            dato.append(j+1)
            dato.append(muestra[i][j])
            nuevaMuestra.append(dato)
            dato = []
    return nuevaMuestra