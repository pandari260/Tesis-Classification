#parametros
    param routeParams := "parametrosHiperplanes";
    param d := 2;
    set Ft := {0 to d-1};

    param nk := read routeParams as "1n" skip 0 use 1; 
    set K := {0 to nk-1};
    param group[K*Ft] := read "grupo" as "<1n,2n> 3n";#leer el grupo actual

    param k0 := read routeParams as "1n" skip 1 use 1; 
    set K0 := {0 to k0-1};
    param C0[K0*Ft] := read "cluster" as "<1n,2n> 3n";

#variables

    var p[Ft] >= -infinity;
    var q >= -infinity;
    var obj >= -infinity;
#funcion objetivo

    minimize z: obj;

#restricciones
    subto objetive: 
        obj>= (sum <f> in Ft: (p[f])**2);

    subto r1:
        forall <i> in K0:
            p[0]*C0[i,0] + p[1]*C0[i,1] >= q+1;
    
    subto r2: 
        forall <j> in K:
            p[0]*group[j,0] + p[1]*group[j,1] <= q-1;
    
    





                
    

