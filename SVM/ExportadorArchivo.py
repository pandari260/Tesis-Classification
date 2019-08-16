
class ExportadorArchivo:

    @staticmethod
    def exportarArchivoCSV(muestra, ubicacion):
        f=open(ubicacion,"w")
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
