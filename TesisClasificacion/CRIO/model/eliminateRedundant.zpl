#parametros
    param routeParam := "globalParameters";
    param routeData := "eliminateRedundatCurrentRegion";
    param n := read routeParam as "1n" skip 0 use 1; #numero de muestras
    param d := read routeParam as "1n" skip 1 use 1;#dimecion de las muestras
    set Ft :={0 to d-1};#etiquetas para las caracteristicas de cada muestra;

    #clusters
    param k0 :=read routeParam as "1n" skip 5 use 1;#numero de clusters de clase 0
    set K0 := {0 to k0-1};#etiquetas para los clusters de clase 0

    param t0 := read routeData as "1n" use 1;
    param p[K0*Ft] := read routeData as "<1n,2n> 3n" skip 1 use (k0*d);
    param q[K0] := read routeData as "<1n> 2n" skip (k0*d+1);

#variables
    var x[Ft] >= -infinity;

   
       
    maximize obj : sum <f> in Ft: p[t0,f] * x[f];
    
    subto r1: 
        forall <t> in K0 with t != t0:
            (sum <f> in Ft: p[t,f] * x[f]) <= q[t];
            #-1.99 * x[0] - 0* x[1] <= -10.9; 
    subto r2:
        (sum <f> in Ft: p[t0,f] * x[f]) <= q[t0] + 1;
        #    -0.79 * x[0] -0.39 * x[1] <= -5.39+1; 

     do forall <t> in K0 with t != t0: print t; 
        do forall <t> in K0 with t != t0:  print q[t];
        do forall <t> in K0 with t != t0:  print p[t,0];
        do forall <t> in K0 with t != t0:  print p[t,1];
    do print "-----------------------------------------";

    do print t0;
    do print q[t0];
    do print p[t0,0];
    do print p[t0,1];
    do print "-----------------------------------------";

