# =========================================
# SEGMENTO 20: COLISIONES EN HASHING
# =========================================

# Colisiones en Hashing

Una **colisión** ocurre cuando dos keys distintas generan la misma posición en la tabla hash: `hash(k1) == hash(k2)` pero `k1 != k2`.

> Ejemplo a utilizar para todos los ejemplos posteriores:

```python
def hash(x):
    return x % 3
```

### Tabla Hash

> Datos de ejemplo: `13, 5, 18, 28`

| Key | Operación | Posición |
|---|---|---|
| 13 | `13 % 3` | 1 |
| 5 | `5 % 3` | 2 |
| 18 | `18 % 3` | 0 |
| 28 | `28 % 3` | 1 (**colisión** con el 13) |

| Posición | Valor | Nota |
|:--:|:--:|---|
| 0 | 18 | |
| 1 | 13 | <- Al insertar el 28, ocurre una colisión |
| 2 | 5 | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |

* Con `x % 3` solo se usan las posiciones `0`, `1` y `2`, por eso las colisiones son muy frecuentes en este ejemplo.

> Open Hashing, se necesita incrementar la memoria para trabajar las soluciones. Closed Hashing resuelven las colisiones con el tamaño original del vector, sin agregar memoria nueva

| Familia | Memoria | Técnicas |
|---|---|---|
| **Open Hashing** | Se necesita **más memoria** para resolver las colisiones | Direct Chaining |
| **Closed Hashing** | Se usa el **tamaño original** del vector, sin memoria nueva | Linear Probing, Quadratic Probing, Double Hashing |

## Open Hashing

### Direct Chaining

Se empieza con el hash obtenido previamente antes de su colisión.

| Posición | Valor |
|:--:|:--:|
| 0 | 18 |
| 1 | 13 |
| 2 | 5 |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |

Se agrega la colisión como una lista enlazada en la posición que se ubica. Al insertar el 28 y el 43, se obtiene que ambos llegan a la posición 1.

| Posición | Valor |
|:--:|:--:|
| 0 | 18 |
| 1 | 13 <- 28 <- 43 |
| 2 | 5 |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |

El tiempo en el caso de las listas enlazadas deja de ser O(1) y pasa a ser O(n).

| Aspecto | Descripción |
|---|---|
| **Idea** | Cada posición guarda una lista enlazada con todas las keys que caen allí |
| **Insertar** | Se calcula el hash y se agrega el nodo a la lista de esa posición |
| **Buscar** | Se calcula el hash y se recorre la lista de esa posición |
| **Borrar** | Se calcula el hash y se elimina el nodo de la lista |
| **Memoria extra** | Sí, cada nodo de la lista ocupa memoria adicional (por eso es Open Hashing) |
| **Tiempo promedio** | O(1) si las listas son cortas |
| **Peor caso** | O(n) si todas las keys caen en la misma posición |

## Closed Hashing

### Linear Probing

Utiliza la siguiente posición disponible en la tabla Hash, al insertar los elementos, se generan colisiones, simplemente se busca el siguiente espacio libre y se inserta en dicha posición. Al eliminar el 5 e insertar los elementos 28, 43 y 4, se obtiene la siguiente tabla hash.

| Key | Hash | Posiciones revisadas | Posición final |
|---|---|---|---|
| 28 | 1 | 1 (ocupada), 2 (libre) | 2 |
| 43 | 1 | 1, 2 (ocupadas), 3 (libre) | 3 |
| 4 | 1 | 1, 2, 3 (ocupadas), 4 (libre) | 4 |

| Posición | Valor |
|:--:|:--:|
| 0 | 18 |
| 1 | 13 |
| 2 | 28 |
| 3 | 43 |
| 4 | 4 |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |

```python
# pos = (hash(x) + i) % tam
for i in range(0, n):
    pos = (hash(x) + i) % tam
```

Búsqueda se convierte en O(n) al tener que buscar por el elemento no mapeado en su clave correcta.

* Para buscar un elemento se empieza en `hash(x)` y se avanza hasta encontrarlo o llegar a una posición vacía.
* Al borrar un elemento no se puede dejar la posición simplemente vacía, porque se cortaría la búsqueda de los elementos que colisionaron después; se debe marcar como **borrada** (lápida).

#### Clustering

Clustering, se refiere a agrupar elementos

| Tipo | Qué es | Técnica que lo sufre |
|---|---|---|
| **Primario** | Los elementos se agrupan en bloques contiguos, y cada colisión hace crecer el bloque | Linear Probing |
| **Secundario** | Dos llaves distintas con el mismo hash siguen el mismo camino o patrón | Quadratic Probing |

* Entre más grande el grupo, más probable es que una nueva key caiga dentro de él y lo haga crecer aún más.

#### Factor de carga

Factor de carga -> 0.85, para mantener un espaciado libre.

Tabla hash siempre con 15% del espacio libre, en caso de necesitar más, debe de asignar nueva memoria, copiado y borrado.

| Concepto | Descripción |
|---|---|
| **Fórmula** | `factor de carga = n / m` (elementos guardados / posiciones de la tabla) |
| **Límite del ejemplo** | 0.85, es decir, 15% del espacio siempre libre |
| **Si se supera** | Se asigna una tabla más grande, se copian los elementos (**rehashing**) y se borra la tabla anterior |

> Ejemplo a utilizar para todos los ejemplos posteriores:

> Datos de ejemplo: `13, 48, 7`

```python
def hash(x):
    return x % 10
```

| Key | Operación | Posición |
|---|---|---|
| 13 | `13 % 10` | 3 |
| 48 | `48 % 10` | 8 |
| 7 | `7 % 10` | 7 |

### Quadratic Probing

| Posición | Valor |
|:--:|:--:|
| 0 | |
| 1 | |
| 2 | |
| 3 | 13 |
| 4 | |
| 5 | |
| 6 | |
| 7 | 7 |
| 8 | 48 |
| 9 | |

```python
# En Python ^ es XOR, la potencia se escribe con **
for i in range(0, n):
    pos = (hash(x) + i ** 2) % tam
```

Deja de ser linear, al insertar el 67 se genera una colisión en la posición 7, se genera colisión porque hash(x) = 7 e i^2 = 1 => 8, ocupada nuevamente y al hacer 2^2 = 4 => 11, al ser el hash circular pasa hasta la posición 11 (1) y se inserta en dicha posición.

| i | Cálculo | Posición | Estado |
|---|---|---|---|
| 0 | `7 + 0` | 7 | Ocupada (7) |
| 1 | `7 + 1` | 8 | Ocupada (48) |
| 2 | `7 + 4 = 11` → `11 % 10` | 1 | **Libre** |

Los elementos quedan más dispersos, sufre de clustering secundario. Cuando dos llaves distintas siguen el mismo camino o patron

Al insertar el 67 y 17, queda de esta manera:

| Key | Hash | Posiciones revisadas | Posición final |
|---|---|---|---|
| 67 | 7 | 7, 8, 1 | 1 |
| 17 | 7 | 7, 8, 1 (ocupadas), `7 + 9 = 16` → 6 (libre) | 6 |

| Posición | Valor |
|:--:|:--:|
| 0 | |
| 1 | 67 |
| 2 | |
| 3 | 13 |
| 4 | |
| 5 | |
| 6 | 17 |
| 7 | 7 |
| 8 | 48 |
| 9 | |

> Nota: Se entregan en prácticas lista de elementos y se pide la tabla hash final obtenida al aplicar ciertas resoluciones de colisiones

### Double Hashing

```python
# Solo aplica en caso de colisiones, código necesita verificaciones para evitar calcular hash2(x) para funcionalidad correcta, solo académico

def hash2(x):
    return x % 3 + 2

for i in range(0, n):
    pos = (hash(x) + hash2(x) * i) % tam
```

Al insertar los elementos 67, 17 y 37, se obtiene el hash:

| Key | hash(x) | hash2(x) | Posiciones revisadas | Posición final |
|---|---|---|---|---|
| 67 | 7 | `67 % 3 + 2 = 3` | 7 (ocupada), `7 + 3 = 10` → 0 (libre) | 0 |
| 17 | 7 | `17 % 3 + 2 = 4` | 7 (ocupada), `7 + 4 = 11` → 1 (libre) | 1 |
| 37 | 7 | `37 % 3 + 2 = 3` | 7, 0 (`7 + 3`), 3 (`7 + 6 = 13`) ocupadas, `7 + 9 = 16` → 6 (libre) | 6 |

| Posición | Valor |
|:--:|:--:|
| 0 | 67 |
| 1 | 17 |
| 2 | |
| 3 | 13 |
| 4 | |
| 5 | |
| 6 | 37 |
| 7 | 7 |
| 8 | 48 |
| 9 | |

No sufre de clustering

* El **salto** depende de la key (`hash2(x)`), por lo que dos keys con el mismo hash siguen caminos distintos.
* `hash2(x)` nunca debe dar `0`, porque la posición no avanzaría; por eso se usa `x % 3 + 2`.

> Nota: Arreglar código (en el código mostrado ya se agregó el paréntesis faltante, el `% tam` para que la tabla sea circular y `hash2` quedó definida antes de usarse)

## Comparación de técnicas

| Técnica | Familia | Memoria extra | Clustering | Búsqueda en peor caso |
|---|---|---|---|---|
| **Direct Chaining** | Open Hashing | Sí (listas enlazadas) | No aplica | O(n) |
| **Linear Probing** | Closed Hashing | No | Primario | O(n) |
| **Quadratic Probing** | Closed Hashing | No | Secundario | O(n) |
| **Double Hashing** | Closed Hashing | No | No sufre | O(n) |

| Técnica | Fórmula de la posición |
|---|---|
| **Linear** | `(hash(x) + i) % tam` |
| **Quadratic** | `(hash(x) + i ** 2) % tam` |
| **Double Hash** | `(hash(x) + hash2(x) * i) % tam` |

## Ejemplo de Examen

> 25, 82, 17, 55, 2, 10, 36, 48, 14

```python
#define MAX_TAM 10
int v[10]

def hash(x):
    return x % 11

def hash2(x):
    return 3 - x % 3
```

* Linear
* Quad
* Double Hash

> Nota: `hash(x) = x % 11` produce posiciones de 0 a 10, por lo que se resuelve con una tabla de **11 posiciones** (0 a 10). Con 10 posiciones la key `10` quedaría fuera del vector.

| Key | hash(x) | hash2(x) |
|---|---|---|
| 25 | 3 | `3 - 25 % 3 = 2` |
| 82 | 5 | `3 - 82 % 3 = 2` |
| 17 | 6 | `3 - 17 % 3 = 1` |
| 55 | 0 | `3 - 55 % 3 = 2` |
| 2 | 2 | `3 - 2 % 3 = 1` |
| 10 | 10 | `3 - 10 % 3 = 2` |
| 36 | 3 | `3 - 36 % 3 = 3` |
| 48 | 4 | `3 - 48 % 3 = 3` |
| 14 | 3 | `3 - 14 % 3 = 1` |

### Plantilla vacía

| Posición | Valor |
|:--:|:--:|
| 0 | |
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |

### Solución: Linear Probing

| Key | Posiciones revisadas | Posición final |
|---|---|---|
| 25 | 3 | 3 |
| 82 | 5 | 5 |
| 17 | 6 | 6 |
| 55 | 0 | 0 |
| 2 | 2 | 2 |
| 10 | 10 | 10 |
| 36 | 3 (ocupada), 4 | 4 |
| 48 | 4, 5, 6 (ocupadas), 7 | 7 |
| 14 | 3, 4, 5, 6, 7 (ocupadas), 8 | 8 |

| Posición | Valor |
|:--:|:--:|
| 0 | 55 |
| 1 | |
| 2 | 2 |
| 3 | 25 |
| 4 | 36 |
| 5 | 82 |
| 6 | 17 |
| 7 | 48 |
| 8 | 14 |
| 9 | |
| 10 | 10 |

### Solución: Quadratic Probing

| Key | Posiciones revisadas | Posición final |
|---|---|---|
| 25 | 3 | 3 |
| 82 | 5 | 5 |
| 17 | 6 | 6 |
| 55 | 0 | 0 |
| 2 | 2 | 2 |
| 10 | 10 | 10 |
| 36 | 3 (ocupada), `3 + 1 = 4` | 4 |
| 48 | 4 (ocupada), `4 + 1 = 5` (ocupada), `4 + 4 = 8` | 8 |
| 14 | 3 (ocupada), `3 + 1 = 4` (ocupada), `3 + 4 = 7` | 7 |

| Posición | Valor |
|:--:|:--:|
| 0 | 55 |
| 1 | |
| 2 | 2 |
| 3 | 25 |
| 4 | 36 |
| 5 | 82 |
| 6 | 17 |
| 7 | 14 |
| 8 | 48 |
| 9 | |
| 10 | 10 |

### Solución: Double Hashing

| Key | Posiciones revisadas | Posición final |
|---|---|---|
| 25 | 3 | 3 |
| 82 | 5 | 5 |
| 17 | 6 | 6 |
| 55 | 0 | 0 |
| 2 | 2 | 2 |
| 10 | 10 | 10 |
| 36 | 3 (ocupada), `3 + 3 = 6` (ocupada), `3 + 6 = 9` | 9 |
| 48 | 4 | 4 |
| 14 | 3, `3 + 1 = 4`, `3 + 2 = 5`, `3 + 3 = 6` (ocupadas), `3 + 4 = 7` | 7 |

| Posición | Valor |
|:--:|:--:|
| 0 | 55 |
| 1 | |
| 2 | 2 |
| 3 | 25 |
| 4 | 48 |
| 5 | 82 |
| 6 | 17 |
| 7 | 14 |
| 8 | |
| 9 | 36 |
| 10 | 10 |

* Comparando las tres tablas se ve que **la misma lista de keys produce tablas distintas** según la técnica de resolución de colisiones.

# Diccionario de Python (`dict`)

> Un diccionario de Python (`dict`) es una tabla hash

Un `dict` almacena pares **llave: valor**. Internamente aplica `hash(llave)` para decidir en qué posición de la tabla se guarda cada par, por eso insertar, buscar y borrar son **O(1)** en promedio.

```python
notas = {"ana": 90, "luis": 75, "sofia": 88}

notas["ana"]          # 90, buscar
notas["pedro"] = 60   # insertar
notas["luis"] = 80    # actualizar
del notas["sofia"]    # borrar
"ana" in notas        # True, comprobar si existe la llave
```

## Características

| Característica | Descripción |
|---|---|
| **Pares llave: valor** | Cada llave se asocia a un valor |
| **Llaves únicas** | Si se inserta una llave repetida, se **reemplaza** el valor anterior |
| **Llaves hashable** | Deben ser inmutables: `int`, `str`, `float`, `tuple` (de elementos inmutables), `bool`, `frozenset` |
| **Valores** | Pueden ser de cualquier tipo, incluso otro `dict` o una lista |
| **Mutable** | Se pueden agregar, modificar y borrar pares |
| **Orden de inserción** | Desde Python 3.7 se mantiene el orden en que se insertaron las llaves |
| **Sin índices numéricos** | Se accede por llave, no por posición |

```python
d = {[1, 2]: "x"}      # TypeError: unhashable type: 'list'
d = {(1, 2): "x"}      # Correcto, la tupla sí es hashable
```

## Operaciones y complejidad

| Operación | Código | Promedio | Peor caso |
|---|---|---|---|
| **Insertar / actualizar** | `d[k] = v` | O(1) | O(n) |
| **Buscar** | `d[k]` o `d.get(k)` | O(1) | O(n) |
| **Borrar** | `del d[k]` o `d.pop(k)` | O(1) | O(n) |
| **Pertenencia** | `k in d` | O(1) | O(n) |
| **Recorrer** | `for k in d` | O(n) | O(n) |
| **Tamaño** | `len(d)` | O(1) | O(1) |

* El peor caso ocurre cuando muchas llaves colisionan en la misma posición.

## Métodos principales

| Método | Qué hace | Ejemplo |
|---|---|---|
| `d.get(k, defecto)` | Devuelve el valor o el defecto si no existe (sin error) | `d.get("x", 0)` |
| `d.keys()` | Vista de todas las llaves | `list(d.keys())` |
| `d.values()` | Vista de todos los valores | `sum(d.values())` |
| `d.items()` | Vista de pares `(llave, valor)` | `for k, v in d.items()` |
| `d.pop(k)` | Elimina la llave y devuelve su valor | `d.pop("ana")` |
| `d.popitem()` | Elimina y devuelve el último par insertado | `d.popitem()` |
| `d.update(otro)` | Agrega o reemplaza pares de otro diccionario | `d.update({"a": 1})` |
| `d.setdefault(k, v)` | Devuelve el valor; si no existe la llave la inserta con `v` | `d.setdefault("a", 0)` |
| `d.clear()` | Borra todos los pares | `d.clear()` |
| `d.copy()` | Copia superficial | `d2 = d.copy()` |

```python
d = {"a": 1, "b": 2}

d["c"]                 # KeyError si la llave no existe
d.get("c")             # None, no genera error
d.get("c", 0)          # 0

for llave, valor in d.items():
    print(llave, valor)
```

## Cómo funciona por dentro

| Aspecto | Descripción |
|---|---|
| **Estructura** | Vector (memoria contigua) con posiciones para el mapeo |
| **Función hash** | Se usa `hash(llave)` de Python; el resultado se ajusta al tamaño de la tabla |
| **Colisiones** | Closed Hashing (**open addressing**): si la posición está ocupada, se busca otra dentro de la misma tabla con un patrón pseudoaleatorio parecido al probing visto en este segmento |
| **Comparación** | Si dos llaves caen en la misma posición, compara con `==` para saber si es la misma llave |
| **Factor de carga** | Cuando la tabla se llena aproximadamente a 2/3, crea una tabla más grande y reinserta los elementos (**rehashing**) |
| **Tamaño** | Siempre una potencia de 2 |

```python
hash(23)        # 23, los enteros pequeños se mapean a sí mismos
hash("hola")    # Número grande; para str cambia entre ejecuciones del programa
```

* Para usar un objeto propio como llave, la clase debe definir `__hash__` y `__eq__`, y **si dos objetos son iguales deben tener el mismo hash**.
* Los hash de `str` cambian entre ejecuciones (por seguridad), por lo que no se debe depender de su valor numérico.

## Relación con lo visto en hashing

| Concepto del tema | En el `dict` de Python |
|---|---|
| **Key** | La llave del diccionario |
| **Tabla hash** | Vector interno del `dict` |
| **Colisión** | Se resuelve con open addressing (Closed Hashing) |
| **Factor de carga** | Se mantiene bajo (~2/3) con rehashing automático |
| **Rehashing** | Ocurre automáticamente al crecer el diccionario |
| **Clustering** | Se reduce con el patrón pseudoaleatorio de búsqueda |
| **O(1)** | Insertar, buscar y borrar en promedio |

## Recorrer y construir diccionarios

```python
# Por comprensión
cuadrados = {x: x ** 2 for x in range(5)}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Desde dos listas
nombres = ["ana", "luis"]
edades = [20, 25]
d = dict(zip(nombres, edades))              # {"ana": 20, "luis": 25}

# Contar frecuencias
conteo = {}
for letra in "banana":
    conteo[letra] = conteo.get(letra, 0) + 1
# {"b": 1, "a": 3, "n": 2}
```

## `dict` frente a otras estructuras

| Estructura | Buscar | Insertar | Orden por llave | Usa hash |
|---|---|---|---|---|
| **`dict`** | O(1) promedio | O(1) promedio | No (solo orden de inserción) | Sí |
| **`set`** | O(1) promedio | O(1) promedio | No | Sí (solo llaves, sin valores) |
| **Lista** | O(n) | O(1) al final | No | No |
| **Árbol AVL / Red-Black** | O(log n) | O(log n) | **Sí** | No |

* Si se necesita acceso rápido por llave se usa `dict`; si se necesita mantener las llaves **ordenadas**, se usa un árbol balanceado.

## Resumen

| Idea | Resumen |
|---|---|
| **Qué es** | Una tabla hash de pares llave: valor |
| **Llaves** | Únicas e inmutables (hashable) |
| **Tiempos** | O(1) promedio en insertar, buscar y borrar |
| **Colisiones** | Open addressing dentro de la misma tabla |
| **Crecimiento** | Rehashing automático al llenarse |
| **Orden** | Se conserva el orden de inserción (Python 3.7+) |
