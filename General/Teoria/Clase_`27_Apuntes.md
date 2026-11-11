# =========================================
# SEGMENTO 25: BACKTRACKING Y EL PROBLEMA DE LAS N REINAS
# =========================================

# Backtracking

**Backtracking** (vuelta atrás) es una técnica de **búsqueda exhaustiva** que construye una solución paso a paso, una decisión a la vez, y **retrocede** (deshace la última decisión) cuando descubre que el camino actual no puede llevar a una solución válida o cuando ya registró una solución completa.

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Decisión** | Elección que se toma en cada paso | Escoger `a`, `b` o `c` para la siguiente posición |
| **Solución parcial** | Construcción incompleta en curso | `[a, b]` cuando se necesitan 3 caracteres |
| **Solución completa** | Construcción que cumple el tamaño o la meta | `[a, b, c]` con `n = 3` |
| **Retroceso (*backtrack*)** | Deshacer la última decisión para probar otra | `pop()` del último carácter |
| **Espacio de búsqueda** | Conjunto de todas las construcciones posibles | Todas las cadenas de longitud `n` |
| **Poda (*pruning*)** | Descartar una rama antes de explorarla completa | Abandonar un tablero donde dos reinas ya se atacan |

> Backtracking es **fuerza bruta organizada**: explora todas las posibilidades, pero con la posibilidad de abandonar ramas inválidas antes de recorrerlas por completo.

* Sirve para **explorar** todas las combinaciones de una aplicación, funcionalidad o problema cuando no existe un método directo para calcular la respuesta.
* Usos: contraseñas por fuerza bruta, sudoku, laberintos, N reinas, generación de permutaciones y combinaciones, problemas de asignación y planificación.

## El costo de la fuerza bruta

La complejidad algorítmica de este tipo de problemas es **excesivamente costosa**: hay una penalidad considerable a medida que crece la entrada.

| Aspecto | Descripción |
|---|---|
| **Crecimiento** | Exponencial o factorial respecto al tamaño de la entrada |
| **Causa** | Cada decisión multiplica el número de ramas por el número de opciones |
| **Consecuencia** | Entradas pequeñas son viables; entradas medianas pueden ser imposibles |
| **Mitigación** | Poda, orden de decisiones y mejores estructuras de verificación |

### Ejemplo: adivinar contraseñas

Para adivinar por fuerza bruta una contraseña de `n` caracteres, con un espacio de claves (*key space*) de `a-z`, `A-Z` y `0-9`:

| Conjunto | Cantidad de símbolos |
|---|:--:|
| **Minúsculas** `a-z` | 26 |
| **Mayúsculas** `A-Z` | 26 |
| **Dígitos** `0-9` | 10 |
| **Total** | **62** |

| Longitud `n` | Posibilidades (`62^n`) |
|:--:|---|
| 1 | 62 |
| 4 | 14 776 336 |
| 8 | ≈ 2,18 × 10¹⁴ |
| 12 | ≈ 3,23 × 10²¹ |

* El crecimiento es de la forma `k^n`, donde `k` es el tamaño del espacio de claves y `n` la longitud: **exponencial**. Con 64 símbolos (al incluir algunos caracteres especiales) corresponde a `64^n`.
* Por esto los ataques de fuerza bruta se vuelven inviables al aumentar la longitud de la contraseña.
* **Gestores de contraseñas** (RoboForm, NordPass, 1Password): generan y almacenan contraseñas largas y aleatorias, de modo que el espacio de búsqueda sea impracticable.

## El árbol de decisión

Backtracking recorre un **árbol de decisión**: cada nivel corresponde a una posición por llenar y cada rama a una opción posible.

Ejemplo con `n = 3` y opciones `['a', 'b', 'c']`, posiciones `_ _ _`:

```
                        [ vacío ]
                 ┌──────────┼──────────┐
                 a          b          c
              ┌──┼──┐    ┌──┼──┐    ┌──┼──┐
              a  b  c    a  b  c    a  b  c
             ...                         ...
              (nivel 3: hojas = soluciones completas)
```

| Elemento del árbol | Significado |
|---|---|
| **Raíz** | Nodo `[vacío]`: aún no se tomó ninguna decisión |
| **Hijos** | Cada opción posible para la siguiente posición (aquí, 3 hijos: `A`, `B`, `C`) |
| **Nivel** | Cantidad de decisiones tomadas |
| **Hoja** | Solución completa (nivel `n`) |
| **Ruta raíz-hoja** | Una solución candidata, por ejemplo `a -> b -> c` |

| Cálculo | Valor para `n = 3`, 3 opciones |
|---|:--:|
| **Hojas del árbol** | `3³ = 27` |
| **Nodos totales** | `1 + 3 + 9 + 27 = 40` |

### Decision Tree y Greedy

| Aspecto | Backtracking (árbol de decisión) | Voraz (*Greedy*) |
|---|---|---|
| **Estrategia** | Explora todas las ramas y retrocede | Toma la mejor opción local y no vuelve atrás |
| **Reconsidera decisiones** | Sí (`pop`) | No |
| **Garantiza hallar solución** | Sí, si existe | Solo en problemas con propiedad voraz |
| **Costo** | Alto | Bajo |
| **Ejemplos** | N reinas, sudoku, contraseñas | Kruskal, Prim, Dijkstra |

## Cómo funciona: push - pop

El patrón se basa en una **pila** de decisiones: se agrega una opción (*push*), se explora a partir de ella y luego se retira (*pop*) para probar la siguiente.

| Paso | Qué se hace |
|---|---|
| **1** | Si la solución parcial está completa, **guardarla** como resultado |
| **2** | Si no, recorrer las **opciones** disponibles para la siguiente posición |
| **3** | **Agregar** la opción a la solución parcial (*push*) |
| **4** | **Llamar recursivamente** para completar el resto |
| **5** | **Quitar** la opción (*pop*) para dejar el estado como estaba y probar otra |

* Busca las opciones.
* Las guarda cuando son una solución completa.
* Hace `pop` para probar otra opción.

> Regla de oro: lo que se agrega antes de la llamada recursiva **debe deshacerse** después de ella. Así cada rama parte del mismo estado.

## Segmento de código

```python
def generar(n, opciones):
    resultado = []

    def backtracking(parcial):
        if len(parcial) == n:                    # solución completa
            resultado.append("".join(parcial))   # agregar solución
            return
        for c in opciones:                       # buscar opciones
            parcial.append(c)                    # push: tomar la decisión
            backtracking(parcial)                # explorar a partir de ella
            parcial.pop()                        # pop: deshacer y probar otra

    backtracking([])
    return resultado


print(generar(2, ["a", "b", "c"]))
# ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
```

| Parte del código | Función |
|---|---|
| **`parcial`** | Solución en construcción (la pila de decisiones) |
| **Caso base** `len(parcial) == n` | Detecta una solución completa |
| **`resultado.append(...)`** | Registra la solución encontrada |
| **`for c in opciones`** | Recorre las opciones posibles |
| **`parcial.append(c)`** | *Push*: toma la decisión |
| **`backtracking(parcial)`** | Explora el subárbol de esa decisión |
| **`parcial.pop()`** | *Pop*: retrocede |

### Traza para `n = 2`, opciones `a, b, c`

| Paso | Acción | `parcial` | Resultado |
|:--:|---|---|---|
| 1 | Push `a` | `[a]` | — |
| 2 | Push `a` | `[a, a]` | Guarda `aa` |
| 3 | Pop | `[a]` | — |
| 4 | Push `b` | `[a, b]` | Guarda `ab` |
| 5 | Pop | `[a]` | — |
| 6 | Push `c` | `[a, c]` | Guarda `ac` |
| 7 | Pop, pop | `[]` | — |
| 8 | Push `b` y continúa igual | `[b]` | ... |

## Plantilla general

```python
def backtracking(estado):
    if es_solucion(estado):
        guardar(estado)
        return
    for opcion in opciones(estado):
        if es_valida(opcion, estado):    # poda: descarta ramas inválidas
            aplicar(opcion, estado)      # push
            backtracking(estado)
            deshacer(opcion, estado)     # pop
```

| Función | Qué responde |
|---|---|
| **`es_solucion`** | ¿La construcción ya es completa y correcta? |
| **`opciones`** | ¿Qué decisiones se pueden tomar desde aquí? |
| **`es_valida`** | ¿Esta decisión puede llevar a una solución? (poda) |
| **`aplicar` / `deshacer`** | Tomar la decisión y revertirla |

## Complejidad

| Problema | Tamaño del espacio de búsqueda |
|---|---|
| **Cadenas de longitud `n` con `k` símbolos** | `k^n` |
| **Permutaciones de `n` elementos** | `n!` |
| **Subconjuntos de `n` elementos** | `2^n` |
| **Con poda** | Menor en la práctica, pero el peor caso sigue siendo exponencial |

---

# Problema de las N Reinas (N-Queens)

Dado un tablero de **N × N casillas**, colocar **N reinas** de modo que **ninguna ataque a otra**.

| Regla | Descripción |
|---|---|
| **Fila** | Dos reinas no pueden estar en la misma fila |
| **Columna** | Dos reinas no pueden estar en la misma columna |
| **Diagonal** | Dos reinas no pueden estar en la misma diagonal (en ambos sentidos) |
| **Cantidad** | Se deben colocar exactamente `N` reinas |

## Ejemplo: tablero 4 × 4

Solución representada como posiciones `[01, 13, 20, 32]`, donde cada par es `(fila, columna)`:

| Reina | Posición `(fila, columna)` |
|:--:|:--:|
| 1 | `(0, 1)` |
| 2 | `(1, 3)` |
| 3 | `(2, 0)` |
| 4 | `(3, 2)` |

```
      col 0  col 1  col 2  col 3
fila 0  .      Q      .      .
fila 1  .      .      .      Q
fila 2  Q      .      .      .
fila 3  .      .      Q      .
```

| Número de reinas `N` | Soluciones distintas |
|:--:|:--:|
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 8 | 92 |

## Cómo se resuelve con backtracking

| Elemento | Descripción |
|---|---|
| **Decisión** | En qué columna colocar la reina de la fila actual |
| **Nivel del árbol** | La fila que se está llenando |
| **Solución parcial** | Lista con la columna de cada fila ya ocupada |
| **Poda** | Si la columna o alguna diagonal ya está ocupada, no se explora esa rama |
| **Caso base** | Se llenaron las `N` filas |

* Se coloca **una reina por fila**: así nunca hay conflicto de fila y el problema se reduce a elegir una columna por fila.
* Si en una fila **ninguna** columna es válida, se retrocede a la fila anterior y se mueve su reina.

### Verificación de ataques

| Conflicto | Condición entre `(f1, c1)` y `(f2, c2)` |
|---|---|
| **Misma columna** | `c1 == c2` |
| **Diagonal principal** | `f1 - c1 == f2 - c2` |
| **Diagonal secundaria** | `f1 + c1 == f2 + c2` |

* En la diagonal, la diferencia de filas es igual a la diferencia de columnas: `abs(f1 - f2) == abs(c1 - c2)`.

## Segmento de código

```python
def n_reinas(n):
    soluciones = []
    columnas = []                      # columnas[f] = columna de la reina en la fila f

    def es_segura(fila, col):
        for f in range(fila):          # compara con las reinas ya colocadas
            c = columnas[f]
            if c == col or abs(f - fila) == abs(c - col):
                return False           # misma columna o misma diagonal
        return True

    def backtracking(fila):
        if fila == n:                  # todas las reinas colocadas
            soluciones.append(list(columnas))
            return
        for col in range(n):
            if es_segura(fila, col):   # poda
                columnas.append(col)   # push
                backtracking(fila + 1)
                columnas.pop()         # pop

    backtracking(0)
    return soluciones


for sol in n_reinas(4):
    print([f"{f}{c}" for f, c in enumerate(sol)])
# ['01', '13', '20', '32']
# ['02', '10', '23', '31']
```

| Parte del código | Función |
|---|---|
| **`columnas`** | Pila de decisiones: columna elegida en cada fila |
| **`es_segura`** | Revisa columna y diagonales contra las reinas previas |
| **`fila == n`** | Caso base: hay solución completa |
| **`columnas.append(col)`** | *Push*: coloca la reina |
| **`columnas.pop()`** | *Pop*: la retira y prueba otra columna |

### Traza parcial para `N = 4`

| Paso | Acción | `columnas` | Resultado |
|:--:|---|---|---|
| 1 | Fila 0, columna 0 | `[0]` | Segura |
| 2 | Fila 1, columnas 0 y 1 | `[0]` | Atacadas (columna y diagonal) |
| 3 | Fila 1, columna 2 | `[0, 2]` | Segura |
| 4 | Fila 2, columnas 0 a 3 | `[0, 2]` | Todas atacadas: **retroceso** |
| 5 | Pop en fila 1, columna 3 | `[0, 3]` | Segura |
| 6 | Fila 2, columna 1 | `[0, 3, 1]` | Segura |
| 7 | Fila 3, todas atacadas | `[0, 3, 1]` | **Retroceso** hasta la fila 0 |
| 8 | Fila 0, columna 1 | `[1]` | Continúa hasta `[1, 3, 0, 2]` |

## Complejidad

| Enfoque | Posibilidades |
|---|---|
| **Todas las colocaciones posibles (sin restricción)** | `C(N², N)` |
| **Una reina por fila** | `N^N` |
| **Una reina por fila y columna (permutaciones)** | `N!` |
| **Backtracking con poda** | Mucho menor en la práctica; peor caso exponencial |

| Aspecto | Valor |
|---|---|
| **Tiempo** | Exponencial en `N` |
| **Espacio** | `O(N)`: la pila de decisiones y la recursión |
| **Verificación por reina** | `O(N)` con la comparación contra reinas previas |

## Resumen de backtracking

| Idea | Resumen |
|---|---|
| **Backtracking** | Búsqueda exhaustiva que construye soluciones y retrocede con `pop` |
| **Árbol de decisión** | Raíz vacía; cada nivel es una decisión y cada hoja, una solución |
| **Patrón** | Push, llamada recursiva, pop |
| **Costo** | Exponencial: `k^n` posibilidades |
| **Poda** | Descartar ramas inválidas antes de explorarlas |
| **Frente a Greedy** | Backtracking reconsidera decisiones; Greedy no |
| **N Reinas** | Una reina por fila, probar columnas, podar por columna y diagonal |
| **Contraseñas** | La fuerza bruta es inviable al crecer la longitud y el espacio de claves |