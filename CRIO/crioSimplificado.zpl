#este el modelo presentado en (6) es el modelo mas basico sin ninguna mejora o optimzacion.

#parametros
    param n := 6;#cantidad de muestras

    param m0 := 1;#cantidad de puntos azules
    param m1 := 1;#cantidad de puntos rojos
    param d  := 2;#cantidad de dimensiones por muestra
    
    set Ft := {1 to d};#indices para las muestras  
    set M0 := {1 to m0};#indices para los puntos azules
    set M1 := {1 to m1};#indices para los puntos rojos

    param Class0[M0*Ft] := |1,2|# puntos azules
                    |1|2,6|;
                    #|2|3,6|
                    #|3|2,5|;

    param Class1[M1*Ft] := |1,2|# puntos rojos
                        |1|7,1|;
                        #|2|7,2|
                        #|3|6,1|;

    param nk := 1;# cantidad de grupos disjuntos de puntos rojos
    set K := {1 to nk};# indices para los grupos

    #variables
    var a[K*M1] binary;#1 si una muestra m de clase 1 pertence al grupo k en K, 0 si no.
    var px;
    var py;#las pendientes de todas las rectas que separan cada muestra de clase 0 con cada grupo k de clase 1.
    var q;#las ordenadas al origen las rectas que separan cada muestra de clase 0 con cada grupo k de clase 1. 
    var delta;# queremos que delta  sea mayor a 0 para que no haya puntos de clase 0 en compoenetes convexas de clase uno como se muestra en las formulas (1) (2) de paper



    do print Class0[1,1];
    do print Class0[1,2];
    do print Class1[1,1];
    do print Class1[1,2];

    maximize z : delta; #la solucion es reemplazar px = 5, py = -5 q = 1 
        
    subto r1: 1 + 5*Class0[1,1]+(-5)*Class0[1,2]<=-delta;
            #q + px*Class0[1,1]+(py)*Class0[1,2]<=-delta;
                
    subto r2:
        1+5*Class1[1,1]+(-5)*Class1[1,2] >= 0;
        #q+px*Class1[1,1]+(py)*Class1[1,2] >= 0;

    subto r3: 
        forall <j> in M1 do
            sum <k> in K: a[k,j] == 1;
    
    subto r4: delta <= 1;

    
    
    
    

