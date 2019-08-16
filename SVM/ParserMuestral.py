class ParserMuestral:

    muestraC1, muestraC2 = [], []
    
    def parsearMuestra(self, datosGenerados, clase):
        muestra, dato = [],[]
        for i in range(len(datosGenerados[0])): 
            for j in range(len(datosGenerados)):
                dato.append(round(datosGenerados[j][i],4)) #Solo se incluyen hasta los 5 decimales
            dato.append(clase)
            muestra.append(dato)
            dato = []
            
        if(clase == 1): self.muestraC1 += muestra 
        else: self.muestraC2 += muestra
        return muestra

    def getClase(self, dato):
        if(self.estaEnMuestra(dato, self.muestraC1)): return 1
        elif(self.estaEnMuestra(dato, self.muestraC2)): return 0
        return -1

    def estaEnMuestra(self, dato, muestra):
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

    def getMuestraC1(self):
        return self.muestraC1

    def getMuestraC2(self):
        return self.muestraC2