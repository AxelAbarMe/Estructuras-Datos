# 5: TDA (Tipo de Datos Abstracto)

## Definición

**Uso más eficiente de la memoria.**

* Datos que se quieren guardar.
* Operaciones (principal diferenciación de una estructura a otra).

### Características

* Ayudan a moderar qué estructuras de datos utilizar para cada situación.
* Lo importante son las características que diferencian cada estructura de datos, para conocer cuál es su implementación más eficiente.

### Implementación

No importa, debido a que esta puede variar, ya que se puede implementar una lista enlazada como vector u otros.

---

## Vector

```cpp
int v[10];
```

### Memoria continua

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| | | | | | | | | | |
| 0x0000 | 0x0004 | 0x0008 | 0x0012 | 0x0016 | 0x0020 | 0x0024 | 0x0028 | 0x0032 | 0x0036 |

A nivel de memoria RAM, lo que se dice es que se reserve (suponiendo arquitectura x86-64) 4B por espacio de memoria, o sea 40B en total.

* En el vector debe cumplirse este requisito: la memoria asignada debe asignarse de manera continua.
* El vector debe saber cuánta memoria debe ser asignada para saber cuánto debe reservar.
* `v` es un puntero, ya que `&v[0]` retorna la dirección de memoria del primer espacio reservado.

> `v[4]=18;` por debajo se transforma en `*(v+4*int)`

Lo que significa: ir a la dirección de `v` y moverse 4 bytes por el tamaño de un `int`, o sea moverse 16 bytes y acceder a `0x0016`.

Esto significa **Acceso Directo**, característica que tiene el vector, con **Complejidad O(1)**, o sea constante.

### Ejemplo — Automático

```cpp
int v[5]; // En este caso C/C++ solo tiene este tamaño fijo y no se puede cambiar.
```

### Ejemplo — Dynamic

```cpp
int v[];
```

| 1 | 2 | → | 1 | 2 |
|:--:|:--:|:--:|:--:|:--:|
| X | X | | | |
| Liberado | Liberado | | Copy | Copy |

No hay garantía de que se pueda almacenar el espacio 2, ya que existe la posibilidad de que esté ocupado por otro elemento.

* Una opción para resolver este problema puede ser verificar si hay espacio; se puede hacer con la librería `realloc`.
* Entonces se busca otro espacio de memoria, se asignan los espacios de memoria, se copia lo previo en el nuevo espacio y luego se libera la memoria previamente utilizada. Esto se llama **Deep Copy**.
* Ineficiente porque necesita realizar el procedimiento varias veces cada vez que se necesita insertar elementos, provocando que vectores dinámicos extremadamente largos consuman mayor cantidad de memoria RAM y realicen mayor cantidad de procedimientos.

Un ejemplo de 1.000.000 de elementos realiza aproximadamente 500.000.000 operaciones al utilizar la fórmula de Gauss.

Para evitar que esto deje de ser ineficiente, se realiza una **expansión x2** del tamaño original, para que en vez de hacer una operación por cada inserción, sea entonces una cantidad menor, reduciendo la cantidad de 500.000.000 operaciones a solamente 2.000.000.

### Operaciones

* Insertar
* Borrar
* Buscar

---

## Lista Enlazada Simple

Difiere de un vector únicamente en cómo se asigna la memoria.

### Nodo

| Dato | Next | → | Dato | Next | → | Dato | Next |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0x4000 (Nodo) | Next guarda 0x7800 | | 0x7800 (Nodo) | Next guarda 0x0600 | | 0x0600 (Nodo) | Next guarda None |

Se tiene un inicio que apunta a la dirección de memoria `0x4000`.

```python
class Nodo:
    def __init__(self, dato=None, next=None):
        self.dato = dato
        self.next = next
```

### Operaciones

* Insertar
* Borrar
* Buscar

---

## Cola (Queue)

### Operaciones

* Enque
* Deque

| | ← | | ← | | ← | | → | None |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Tail (Rear) | | | | | | Head (Front) | | |

### Enque

Inserta un elemento por *tail*, empujando el resto de elementos hacia el frente según se fueron insertando.

```
enque(5)
enque(7)
enque(16)
enque(29)
```

| 29 | ← | 16 | ← | 7 | ← | 5 | → | None |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Tail (Rear) | | | | | | Head (Front) | | |

### Deque

`deque()` devuelve el resultado que apunta *Head*, simulando el efecto de una fila, eliminando el último elemento, o el primero en ser insertado.

**FIFO**

* First
* In
* First
* Out

### Complejidad y usos de la Cola

* `enqueue()` y `dequeue()` tienen complejidad **O(1)**, siempre que se mantenga una referencia directa tanto al *front* como al *rear* (como en la implementación con lista enlazada simple vista más adelante); si solo se tuviera referencia al *front*, insertar al final obligaría a recorrer toda la lista, degradando la operación a O(n).
* **Casos de uso comunes:** colas de impresión, gestión de tareas o procesos en un sistema operativo (el primero en llegar es el primero en ejecutarse), manejo de peticiones en un servidor, algoritmos de recorrido en anchura (BFS) sobre árboles o grafos.
* A diferencia de la Pila, la Cola respeta el **orden de llegada** de los elementos; es la estructura natural para modelar cualquier "fila" del mundo real (banco, caja de supermercado, etc.).

---

## Pila (Stack)

### Operaciones

* `push` (insertar)
* `pop` (recuperar y eliminar)
* `top` (retornar el tope)

### push

`top` es un puntero que apunta al elemento de más arriba (o el último elemento ingresado). Se insertan los elementos y se van relacionando entre ellos.

```
push(7)
push(10)
push(57)
```

```
57 <- TOP
 |
 v
10
 |
 v
 7
```

### pop

```
pop()
```

```
10 <- TOP
 |
 v
 7
```

Retorna `57` y se elimina del stack; a la vez, `top` apunta a `10` al ser el último ingresado disponible.

Si se realiza otro `push(60)`, se inserta y sube de primero, y `top` apuntaría a `60` en vez de `10`.

```
push(60)
```

```
60 <- TOP
 |
 v
10
 |
 v
 7
```

**LIFO**

* Last
* In
* First
* Out

### Complejidad y usos de la Pila

* `push()`, `pop()` y `peek()`/`top()` tienen complejidad **O(1)**, ya que todas las operaciones ocurren únicamente en un extremo de la estructura (el tope), sin necesidad de recorrer ni desplazar el resto de los elementos.
* **Casos de uso comunes:** la función "deshacer" (Undo) de un editor de texto, el historial de navegación de "atrás" en un navegador web, la evaluación de expresiones matemáticas (balanceo de paréntesis), y —como se vio en el tema de Recursión— el **stack de llamadas del CPU**, donde cada `push` corresponde a una nueva llamada de función y cada `pop` a su respectivo retorno.
* Es la estructura conceptual detrás del *stack overflow*: si se hacen demasiados `push` sin sus correspondientes `pop` (por ejemplo, una recursión sin caso base), la pila se llena por completo.

> Las estructuras anteriores (Vector, Lista, Cola, Pila) son llamadas **estructuras de datos lineales**.

> **Nota adicional:** además de las lineales, existen estructuras de datos no lineales (árboles, grafos, tablas hash), donde los elementos no se conectan de forma secuencial sino jerárquica o en red.
