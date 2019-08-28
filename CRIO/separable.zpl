#parametros
    param n := read "parametros" as "1n" skip 0 use 1; #numero de muestras
    param d := read "parametros" as "1n" skip 1 use 1;#dimecion de las muestras
    set Ft :={0 to d-1};#etiquetas para las caracteristicas de cada muestra;

    #muestras de clase 0
    param mB :=read "parametrosSeparable" as "1n" skip 0 use 1;#cantidad de muestras de clase 0;
    set MB := {0 to mB-1};#etiquetas para las muestras de clase 0
    param ClassB[MB*Ft] := read "claseB.dat" as "<1n,2n> 3n"; 

    #muestras de clase 1
    param mA :=read "parametrosSeparable" as "1n" skip 1 use 1;#cantidad de muestras de clase 1;
    set MA := {0 to mA-1};#etiquetas para las muestras de clase 1
    param ClassA[MA*Ft] := read "claseA.dat" as "<1n,2n> 3n"; 

#varibles
    var delta >= -infinity;
    var p[MB*Ft] >= -infinity;
    var q[MB] >= -infinity;

#funcion obejtivo
    maximize z: delta;

#restricciones
    subto r1:
        forall <i> in MB:            
            q[i] + sum <f> in Ft: p[i,f] * ClassB[i,f] <= -delta;
    
    subto r2:
        forall <i> in MB:
            forall <j> in MA:
                q[i] + sum <f> in Ft: p[i,f] * ClassA[j,f] >= delta;
