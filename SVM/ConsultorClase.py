
class ConsultorClase:

    muestraC1, muestraC2 = [], []

    def __init__(self, muestraC1, muestraC2):
        self.muestraC1 = muestraC1
        self.muestraC2 = muestraC2

    def consultarClase(self, dato):

        if(self.perteneceA(dato, self.muestraC1)): return 1
        elif(self.perteneceA(dato, self.muestraC2)): return 0
        return -1

    def perteneceA(self, dato, muestra):
        encontrado = []
        for i in range(len(dato)):
            for j in range(len(muestra)):
                if(dato[i] == muestra[j][i]):
                    self.agregar(i, encontrado)

        if(len(encontrado) == len(dato)): return True
        return False
    
    def agregar(self, indice, muestra):
        cont = 0
        if(len(muestra) != 0):
            for i in range(len(muestra)):
                if(indice == muestra[i]):
                    cont += 1
        if(cont == 0):
            muestra.append(indice)