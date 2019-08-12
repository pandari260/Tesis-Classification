#parametros
    param n := read "parametros" as "1n" skip 0 use 1;
    param d := read "parametros" as "1n" skip 1 use 1;
    param m0 :=read "parametros" as "1n" skip 2 use 1;
    param m1 :=read "parametros" as "1n" skip 3 use 1;
    param nk :=read "parametros" as "1n" skip 4 use 1;
    param k0 :=read "parametros" as "1n" skip 5 use 1;
    param k1 :=read "parametros" as "1n" skip 6 use 1;
    param M := read "parametros" as "1n" skip 7 use 1;

        set Ft :={1 to d};#etiquetas para las caracteristicas de cada muestra;

    set M0 := {1 to m0};#etiquetas para las muestras de clase 0
    param Class0[M0*Ft] := read "clase_0.dat" as "<1n,2n> 3n"; 
    do forall <m> in M0:
        forall <f> in Ft:
            print Class0[m,f];
# muestras de clase 