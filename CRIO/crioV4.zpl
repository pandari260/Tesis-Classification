
#parametros
param x0 := 2;
param y0 := 6;

param x1 := 7;
param y1 := 1;



#variables
var delta >= -infinity;
var px >= -infinity;
var py >= -infinity;
var q >= -infinity;



maximize z: delta;

subto r1:
    px*x0 + py*y0 + q <= -delta;
    #2*x0 -2*y0 + 0 <= -delta;

subto r2:
    px*x1  + py*y1 + q >= 0;
    #2*x1 -2*y1 +0 >= 0;

subto r0:
    delta <= 1;
