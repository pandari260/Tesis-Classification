
class ConsultorClase:

    @staticmethod
    def consultarClase(dato, muestraC1, muestraC2):
        if(ConsultorClase.perteneceA(dato, muestraC1)): return 1
        elif(ConsultorClase.perteneceA(dato, muestraC2)): return 0
        return -1

    @staticmethod
    def perteneceA(dato, muestra):
        encontrado = []
        for i in range(len(dato)):
            for j in range(len(muestra)):
                if(dato[i] == muestra[j][i]):
                    ConsultorClase.agregar(i, encontrado)

        if(len(encontrado) == len(dato)): return True
        return False
    
    @staticmethod
    def agregar(indice, muestra):
        cont = 0
        if(len(muestra) != 0):
            for i in range(len(muestra)):
                if(indice == muestra[i]):
                    cont += 1
        if(cont == 0):
            muestra.append(indice)