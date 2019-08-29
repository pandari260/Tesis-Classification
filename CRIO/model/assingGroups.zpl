#Mixed-integer optimization problem for Assing groups to polyhedral regions for CRIO

#parametros
    param n := read "parametros" as "1n" skip 0 use 1; #numero de muestras
    param d := read "parametros" as "1n" skip 1 use 1;#dimecion de las muestras
    set Ft :={0 to d-1};#etiquetas para las caracteristicas de cada muestra;

    #muestras de clase 0
    param m0 :=read "parametros" as "1n" skip 2 use 1;#cantidad de muestras de clase 0;
    set M0 := {0 to m0-1};#etiquetas para las muestras de clase 0
    param Class0[M0*Ft] := read "clase0.dat" as "<1n,2n> 3n"; 

    #muestras de clase 1
    param m1 :=read "parametros" as "1n" skip 3 use 1;#cantidad de muestras de clase 1;
    set M1 := {0 to m1-1};#etiquetas para las muestras de clase 1
    param Class1[M1*Ft] := read "clase1.dat" as "<1n,2n> 3n"; 


    #grupos
    param nk :=read "parametros" as "1n" skip 4 use 1;
    set K := {0 to nk-1};#etiquetas para la particion en grupos de clase 1.

    #clusters
    param k0 :=read "parametros" as "1n" skip 5 use 1;#numero de clusters de clase 0
    set K0 := {0 to k0-1};#etiquetas para los clusters de clase 0
    param C0[M0] := read "cluster0.dat" as "<1n> 2n";#cluster de cada muestras de clase 0
 
    param k1 :=read "parametros" as "1n" skip 6 use 1;#numero de clusters de clase 1
    set K1 := {0 to k1-1};#etiquetas para los clusters de clase 1
    param C1[M1] := read "cluster1.dat" as "<1n> 2n";#cluster para los clusters de clase 0

    param M := read "parametros" as "1n" skip 7 use 1;#un numero positivo muy grande

#variables
    var a[K*K1] binary;#1 si el cluster r en K1 pertenece al grupo k en K, 0 si no.
    var delta >=-infinity;
    var e0[M0] >=-infinity;#margen de error para cada punto de clase 0
    var e1[M1] >= -infinity;#margen de error para cada punto de clase 1
    var p[K*K0*Ft] >= -infinity;#rectas que dividen cada grupos de clase 0 con cada grupo de clase 1
    var q[K*K0] >= -infinity;#ordenada al origen de las rectas

#funcion objetivo
    minimize z: sum <i> in M0: e0[i] + sum <j> in M1: e1[j];

#restricciones
    subto r1:
        forall <k> in K:
            forall <t> in K0:
                forall <i> in M0 with C0[i] == t:
                    q[k,t] + sum <f> in Ft: p[k,t,f]*Class0[i,f]  <= -1 + e0[i];
    
    subto r2:
        forall <k> in K:
            forall <r> in K1:
                forall <j> in M1 with C1[j] == r:
                    forall <t> in K0:
                        q[k,t] + sum <f> in Ft: p[k,t,f]*Class1[j,f]  >= -M + (M + 1)*a[k,r] - e1[j];
    
    subto r3:
        forall <r> in K1:
            sum <k> in K: a[k,r] == 1;
    
    subto r4:
        forall <i> in M0:
            e0[i] >= 0;
    
    subto r5:
        forall <j> in M1:
            e1[j] >= 0;