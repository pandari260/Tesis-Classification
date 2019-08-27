#parametros
    param d := 2;
    set Ft := {1 to d};

    param a := 2;
    set A := {1 to a};
    param puntosA[A*Ft] :=|1,2|
                        |1|2,4|
                        |2|2,3|;
    param b := 2;
    set B := {1 to b};
    param puntosB[B*Ft] :=|1,2|
                        |1|5,1|
                        |2|5,2|;

#variables

    var p[Ft] >= -infinity;
    var q >= -infinity;
    var ob >= -infinity;
#funcion objetivo

    minimize z: ob;

#restricciones
    subto objetive: 
        ob>= (sum <f> in Ft: (p[f])**2);

    subto r1:
        forall <i> in B:
            p[1]*puntosB[i,1] + p[2]*puntosB[i,2] >= q+1;
    
    subto r2: 
        forall <j> in A:
            p[1]*puntosA[j,1] + p[2]*puntosA[j,2] <= q-1;
    
    





                
    

