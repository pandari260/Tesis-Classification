#Mixed-integer optimization problem for Assing groups to polyhedral regions for CRIO

#parametros
    param n := read "parametros" as "1n" skip 0 use 1; #numero de muestras
    param d := read "parametros" as "1n" skip 1 use 1;#dimecion de las muestras
    set Ft :={1 to d};#etiquetas para las caracteristicas de cada muestra;

    #muestras de clase 0
    param m0 :=read "parametros" as "1n" skip 2 use 1;#cantidad de muestras de clase 0;
    set M0 := {1 to m0};#etiquetas para las muestras de clase 0
    param Class0[M0*Ft] := read "clase_0.dat" as "<1n,2n> 3n"; 

    #muestras de clase 1
    param m1 :=read "parametros" as "1n" skip 3 use 1;#cantidad de muestras de clase 1;
    set M1 := {1 to m1};#etiquetas para las muestras de clase 1
    param Class1[M1*Ft] := read "clase_1.dat" as "<1n,2n> 3n"; 

    #clusters
    param k0 :=read "parametros" as "1n" skip 5 use 1;#numero de clusters de clase 0
    set K0 := {1 to k0};#etiquetas para los clusters de clase 0
    param C0[M0] := read "cluster0.dat" as "<1n> 2n";#cluster de cada muestras de clase 0
 
    param k1 :=read "parametros" as "1n" skip 6 use 1;#numero de clusters de clase 1
    set K1 := {1 to k1};#etiquetas para los clusters de clase 1
    param C1[M1] := read "cluster1.dat" as "<1n> 2n";#cluster para los clusters de clase 0

    #grupos
    param nk :=read "parametros" as "1n" skip 4 use 1;
    set K := {1 to nk};#etiquetas para la particion en grupos de clase 1.
    param Group1[K1] := <1> 2, <2> 1;

    
#variables
    var p[K*K0*Ft] >= -infinity;
    var q[K*K0] >= -infinity;
    var obj >= -infinity;

   
#funcion objetivo
    minimize z : obj;

#restricciones

    subto objetivo:
        obj >= sum <k,t,f> in K*K0*Ft: p[k,t,f]**2;
    subto r1: 
        forall <k> in K:
            forall <t> in K0:
                 forall <i> in M0 with C0[i] == t:
                    sum <f> in Ft:  p[k,t,f]*Class0[i,f] >= q[k,t] + 1

    subto r2:
        forall <k> in K:
            forall <j> in M1 with Group1[C1[j]] == k:
                forall <t> in K0:
                    sum <f> in Ft: p[k,t,f]*Class1[j] <= q[k,t] - 1

                
    

