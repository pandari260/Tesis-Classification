
class TraductorMuestra:

    @staticmethod
    def traducirACSV(datosGenerados):
        muestra, dato = [],[]
        
        for i in range(len(datosGenerados[0])): 
            for j in range(len(datosGenerados)):
                dato.append(round(datosGenerados[j][i],5))
            if(i%2 == 0):
                dato.append(1)
            else:
                dato.append(0)
            muestra.append(dato)
            dato = []

        return muestra
