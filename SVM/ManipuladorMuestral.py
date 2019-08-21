import pandas as pd

def obtenerMuestraSVM(archivo):
    dataSet = pd.read_csv(archivo)
    datos = dataSet.drop('Class', axis=1)
    target = dataSet['Class']
    return datos, target   

def convertirMuestraZPL(muestra): 
    nuevaMuestra, preMuestra = [], []
    for item in muestra:
        for i in range(len(item)):
            for j in range(len(item[0])):
                preMuestra.append(i+1)
                preMuestra.append(j+1)
                preMuestra.append(item[i][j])
                nuevaMuestra.append(preMuestra)
                preMuestra = []
    return nuevaMuestra