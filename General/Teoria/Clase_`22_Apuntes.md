# Colisiones en Hashing

> Ejemplo a utilizar para todos los ejemplos posteriores:

```python
def hash(x):
  return x % 3
```

### Tabla Hash

> Datos de ejemplo: `13,5,18,28`

|0|18
|:--:|:--:|
|1|13|  <-Al insertar el 28, ocurre una colisión
|2|5 |
|3|  |
|4|7 |
|5|  |
|6|  |
|7|  |
|8|  |
|9|  |

> Open Hashing, se necesita incrementar la memoria para trabajar las soluciones. Closed Hashing resuelven las colisiones con el tamaño original del vector, sin agregar memoria nueva

## Open Hashing

### Direct Chaining

Se empieza con el hash obtenido previamente antes de su colisión.

|0|18
|:--:|:--:|
|1|13|
|2|5 |
|3|  |
|4|  |
|5|  |
|6|  |
|7|  |
|8|  |
|9|  |

Se agrega la colisión como una lista enlazada en la posición que se ubica. Al insertar el 28 y el 43, se obtiene que ambos llegan a la posición 1.

|0|18
|:--:|:--:|
|1|13 <- 28 <- 43|
|2|5 |
|3|  |
|4|  |
|5|  |
|6|  |
|7|  |
|8|  |
|9|  |

El tiempo en el caso de las listas enlazadas deja de ser O(1) y pasa a ser O(n).

## Closed Hashing

### Linear Probing

Utiliza la siguiente posición disponible en la tabla Hash, al insertar los elementos, se generan colisiones, simplemente se busca el siguiente espacio libre y se inserta en dicha posición. Al eliminar el 5 e insertar los elementos 28, 43 y 4, se obtiene la siguiente tabla hash.

|0|18
|:--:|:--:|
|1|13|
|2|28|
|3|43|
|4|4 |
|5|  |
|6|  |
|7|  |
|8|  |
|9|  |

Búsqueda se convierte en O(n) al tener que buscar por el elemento no mapeado en su clave correcta.

Ckustering, se refiere a agrupar elementos

* Primario
* Secundario

Factor de carga -> 0.85, para mantener un espaciado libre.

Tabla hash siempre con 15% del espacio libre, en caso de necesitar más, debe de asignar nueva memoria, copiado y borrado.

> Ejemplo a utilizar para todos los ejemplos posteriores:

> Datos de ejemplo: `13,48,7`

```python
def hash(x):
  return x % 10
```

### Quadratic Probing

|0||
|:--:|:--:|
|1|  |
|2|  |
|3|13|
|4|  |
|5|  |
|6|  |
|7|7 |
|8|48|
|9|  |

```python
for i in range(0,n):
  pos = hash(x)+i^2
```

Deja de ser linear, al insertar el 67 se genera una colisión en la posición 7, se genera colisión porque hash(x) = 7 e i^2 = 1 => 8, ocupada nuevamente y al hacer 2^2 = 4 => 11, al ser el hash circular pasa hasta la posición 11 (1) y se inserta en dicha posición.

Los elementos quedan más dispersos, sufre de clustering secundario. Cuando dos llaves distintas siguen el mismo camino o patron


Al insertar el 67 y 17, queda de esta manera:

|0||
|:--:|:--:|
|1|67|
|2|  |
|3|13|
|4|  |
|5|  |
|6|17|
|7|7 |
|8|48|
|9|  |

> Nota: Se entregan en prácticas lista de elementos y se pide la tabla hash final obtenida al aplicar ciertas resoluciones de colisiones

### Double Hashing

```python
# Solo aplica en caso de colisiones, código necesita verificaciones para evitar calcular hash2(x) para funcionalidad correcta, solo académico

for i in range(0,n):
  pos = (hash(x)+hash2(x) * i

def hash2(x):
  return x % 3 + 2
```

Al insertar los elementos 67, 17 y 37, se obtiene el hash:

|0|67|
|:--:|:--:|
|1|17|
|2|  |
|3|13|
|4|  |
|5|  |
|6|  |
|7|7 |
|8|48|
|9|  |

No sufre de clustering

> Nota: Arreglar código
