
class TraductorMuestra:

    @staticmethod
    def traducirACSV(datosGenerados, clase):
        muestra, dato = [],[]
        
        for i in range(len(datosGenerados[0])): 
            for j in range(len(datosGenerados)):
                dato.append(round(datosGenerados[j][i],5)) #Solo se incluyen hasta los 5 decimales
            dato.append(clase)
            muestra.append(dato)
            dato = []

        return muestra
    
    @staticmethod
    def generarArchivoCSV(muestra):
        f=open("input.csv","w")
        for i in range(len(muestra[0])-1):
            f.write("Feature"+str(i+1)+",")
        f.write('Class\n')

        for dato in muestra:
            for k in range(len(dato)):
                f.write(str(dato[k]))
                if(k!=len(dato)-1):
                    f.write(",")
            f.write("\n")
        f.close()


        