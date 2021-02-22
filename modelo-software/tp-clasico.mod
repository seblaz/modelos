
/* Parametros */

param N_GRUPOS_FAMILIARES;
param N_DIAS;
param TOLERANCIA;

set GRUPOS_FAMILIARES := {0..(N_GRUPOS_FAMILIARES-1)};
set DIAS := {1..(N_DIAS)};

param E{i in GRUPOS_FAMILIARES, j in GRUPOS_FAMILIARES};

var X{i in GRUPOS_FAMILIARES, j in DIAS}, binary;
var W{j in DIAS}, binary;

param M := 1000;

/* Restricciones */

# Hay un unico dia por grupo familiar
s.t. UNICO_DIA_POR_VECINO{i in GRUPOS_FAMILIARES}: sum{j in DIAS} X[i,j] = 1;

# Restriccion de adyacencia entre vecinos 
s.t. ADYACENTES_DISTINTO_DIA{i in GRUPOS_FAMILIARES, k in GRUPOS_FAMILIARES, j in DIAS: E[i,k] = 1}: X[i,j] + X[k,j] <= W[j];

# Eliminacion de simetria
s.t. ELIMINACION_SIMETRIA{j in DIAS: j <> N_DIAS}: sum{i in GRUPOS_FAMILIARES} X[i,j] >= sum{i in GRUPOS_FAMILIARES} X[i,j+1];

# Cantidad de grupos familiares que pueden salir cada dia deben ser similares
s.t. DIFERENCIA_SIMILAR{j in DIAS, l in DIAS: j <> l}: (sum{i in GRUPOS_FAMILIARES} X[i,j]) - (sum{i in GRUPOS_FAMILIARES} X[i,l]) <= TOLERANCIA + M * (1 - W[j]) + M * (1 - W[l]);

/* Funcional */
minimize z: sum{i in DIAS} W[i];

solve;

table tbl{i in GRUPOS_FAMILIARES, j in DIAS: X[i,j] = 1} OUT "CSV" "dias.csv":
i,j;

#table tbl{i in GRUPOS_FAMILIARES, k in GRUPOS_FAMILIARES: E[i,k] = 1} OUT "CSV" "vecinos.csv":
#i,k;


end;
