
def exportarArchivoCSV(muestra, ubicacion):
    f=open(ubicacion,"w")
    for i in range(len(muestra[0][0])-1):
        f.write("Feature"+str(i+1)+",")
    f.write('Class\n')

    for dato in muestra:
        for k in dato:
            for j in range(len(k)):
                f.write(str(k[j]))
                if(j!=len(k)-1):
                   f.write(",")
            f.write("\n")
    f.close()
