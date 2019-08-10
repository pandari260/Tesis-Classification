import math


def crearClusters(cA, cB):#crea clusters para las muestras de cA de clase A
    K = len(cA)
    k = 0

def distanciaEntre(a,b):
    sum = 0
    for i in range(0,len(a)):
        sum = sum + (a[i] - b[i])**2
    return math.sqrt(sum)

def crearMatrizDistancia(clusters):
    tam = len(clusters)
    matrizDist = []
    for clustA in clusters:
        distancias =[]
        for clustB in clusters:
            dAB = 0
            if clustA != clustB:
                dAB = distanciaEntre(clustA[0],clustB[0])
                for a in clustA:
                    for b in clustB:
                        aux = distanciaEntre(a,b)
                        if aux < dAB:
                            dAB = aux
            distancias.append(dAB)    
        matrizDist.append(distancias)
    return matrizDist







def main():
    clase1 =[[[1,7]],[[7,1]],[[1,6]],[[2,7]],[[6,1]],[[6,2]]]
    clase0 =[[[8,10]],[[9,10]],[[8,9]],[[4,5]],[[3,4]],[[4,4]]]
    
    print(crearMatrizDistancia(clase1))


    #cluster1 = crearClusters(clase1, clase0)
    

main()
    
