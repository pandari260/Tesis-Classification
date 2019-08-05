#Mixed-integer optimization problem for Assing groups to polyhedral regions for CRIO

#parametros
    param n := 12;#numero de muestras
    param d := 2;#dimecion de las muestras
    set Ft :={1 to d};#etiquetas para las caracteristicas de cada muestra;

    #muestras de clase 0
    param m0 := 6;#cantidad de muestras de clase 0;
    set M0 := {1 to m0};#etiquetas para las muestras de clase 0
    param Class0[M0*Ft] := |1,2|
                         |1|8,10|
                         |2|9,10|
                         |3|8,9|
                         |4|4,5|
                         |5|3,4|
                         |6|4,4|;
    #muestras de clase 1
    param m1 := 6;#cantidad de muestras de clase 1;
    set M1 := {1 to m1};#etiquetas para las muestras de clase 1
    param Class1[M1*Ft] := |1,2|
                         |1|7,1|
                         |2|1,7|
                         |3|1,6|
                         |4|2,7|
                         |5|6,1|
                         |6|6,2|;

    #grupos
    param nk := 10;
    set K := {1 to nk};#etiquetas para la particion en grupos de clase 1.

    #clusters
    param k0 := 2;#numero de clusters de clase 0
    set K0 := {1 to k0};#etiquetas para los clusters de clase 0
    param C0[M0] := <1> 1,<2> 1,<3> 1,<4>2,<5>2,<6> 2;#cluster de cada muestras de clase 0
 
    param k1 := 2;#numero de clusters de clase 1
    set K1 := {1 to k1};#etiquetas para los clusters de clase 1
    param C1[M1] :=  <1> 1,<2> 2,<3> 2,<4>2,<5>1,<6>1;#cluster para los clusters de clase 0

    param M := 1000000;#un numero positivo muy grande

#variables
    var a[K*K1] binary;#1 si el cluster r en K1 pertenece al grupo k en K, 0 si no.
    var delta real;
    var e0[M0] real;#margen de error para cada punto de clase 0
    var e1[M1] real;#margen de error para cada punto de clase 1
    var p[K*K0*Ft] real;#rectas que dividen cada grupos de clase 0 con cada grupo de clase 1
    var q[K*K0] real;#ordenada al origen de las rectas

#funcion objetivo
    minimize z: sum <i> in M0: e0[i] + sum <j> in M1: e1[j];

#restricciones
    subto r1:
        forall <k> in K:
            forall <t> in K0:
                forall <i> in M0 with C0[i] == t:
                    p[k,t,1]*Class0[i,1] +  p[k,t,2]*Class0[i,2] + q[k,t] <= -1 + e0[i];
    
    subto r2:
        forall <k> in K:
            forall <r> in K1:
                forall <j> in M1 with C1[j] == r:
                    forall <t> in K0:
                        p[k,t,1]*Class1[j,1] + p[k,t,2]*Class1[j,2] + q[k,t] >= -M + (M + 1)*a[k,r] - e1[j];
    
    subto r3:
        forall <r> in K1:
            sum <k> in K: a[k,r] == 1;
    
    subto r4:
        forall <i> in M0:
            e0[i] >= 0;
    
    subto r5:
        forall <j> in M1:
            e1[j] >= 0;