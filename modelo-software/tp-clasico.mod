
/* Parametros */

param N_VECINOS;
param MAX_COLORES;
param TOLERANCIA;

set VECINOS := {0..(N_VECINOS-1)};
set COLORES := {1..(MAX_COLORES)};

param E{i in VECINOS, j in VECINOS};

var X{i in VECINOS, j in COLORES}, binary;
var W{j in COLORES}, binary;

param M := 1000;

/* Restricciones */

# Hay un unico color por vertice
s.t. UNICO_COLOR_POR_VERTICE{i in VECINOS}: sum{j in COLORES} X[i,j] = 1;

# Restriccion de adyacencia entre vecinos 
s.t. ADYACENTES_DISTINTO_COLOR{i in VECINOS, k in VECINOS, j in COLORES: E[i,k] = 1}: X[i,j] + X[k,j] <= W[j];

# Eliminacion de simetria
s.t. ELIMINACION_SIMETRIA{j in COLORES: j <> MAX_COLORES}: sum{i in VECINOS} X[i,j] >= sum{i in VECINOS} X[i,j+1];

# Cantidad de grupos familiares que pueden salir cada dia deben ser similares
s.t. DIFERENCIA_SIMILAR{j in COLORES, l in COLORES: j <> l}: (sum{i in VECINOS} X[i,j]) - (sum{i in VECINOS} X[i,l]) <= TOLERANCIA + M * (1 - W[j]) + M * (1 - W[l]);

/* Funcional */
minimize z: sum{i in COLORES} W[i];

solve;

table tbl{i in VECINOS, j in COLORES: X[i,j] = 1} OUT "CSV" "colores.csv":
i,j;

#table tbl{i in VECINOS, k in VECINOS: E[i,k] = 1} OUT "CSV" "vecinos.csv":
#i,k;


end;
