Para la ejecución del modelo con un dataset determinado utilizando glpk, ejecutar el comando:

```
make clasico SET=<set>
```
Donde `<set>` puede ser `prueba`, `entrega`, `grande` o `enorme`.

Para la ejecución del modelo con `cplex`, debe estar disponible el comando `cplex` en el `PATH` de la terminal. Luego, se ejecuta el siguiente comando:

```
make cplex SET=<set>
```
