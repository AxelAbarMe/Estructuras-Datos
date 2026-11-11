# =========================================
# SEGMENTO 12: ÁRBOLES BINARIOS
# =========================================

## Concepto de Árbol
- Estructura de datos **jerárquica** (no lineal): se empieza en un nodo y se desarrolla hacia los nodos inferiores.
- Se divide en **niveles**. El nivel 0 es la raíz, el nivel 1 son sus hijos, y así sucesivamente.
- La relación casi siempre es **padre -> hijos**. En árboles más complejos (ej. Red-Black) también se habla de *tío*, *abuelo*, etc.
- **Árbol binario:** cada nodo puede tener **0, 1 o 2 hijos** como máximo (hijo izquierdo y/o hijo derecho).
- Todos los árboles son **grafos**, pero no todos los grafos son árboles.

```
                 5              <- Nivel 0 (Raíz / Root)
               /   \
             10     3           <- Nivel 1
            /  \   /  \
          20    1 5    17       <- Nivel 2
         /  \
      NULL  NULL                <- Hijos de una hoja
```

## Terminología
| Término | Inglés | Descripción |
|---|---|---|
| Raíz | Root | Nodo más arriba (nivel 0). **No se puede perder**: si se pierde, se pierde todo el árbol. |
| Padre | Parent | Nodo que tiene uno o más hijos. |
| Hijo | Child | Nodo conectado debajo de un padre (`left` / `right`). |
| Hermanos | Siblings | Nodos que comparten el mismo padre. |
| Arista | Edge | Conexión entre dos nodos. |
| Hoja | Leaf | Nodo sin hijos (hijo izquierdo y derecho = `NULL`/`None`). |
| Nodo interno | Internal node | Nodo con al menos un hijo (no es hoja). |
| Nivel | Level | Conjunto de nodos que están a la misma profundidad. |
| Subárbol | Subtree | Árbol formado por un nodo y todos sus descendientes. |

## Estructura del Nodo
- Cada nodo guarda un **dato** y dos referencias: una al hijo izquierdo y otra al derecho (similar a la lista doblemente enlazada, pero apuntando hacia abajo).

```
+-------+-------+-------+
|  IZQ  | DATOS |  DER  |
+-------+-------+-------+
    |                |
    v                v
  (left)          (right)
```

```python
class Node:
    def __init__(self, datos):
        self.datos = datos
        self.left = None
        self.right = None
```

- Un árbol se representa únicamente con la referencia a su **raíz**; desde ella se llega a todos los demás nodos.

## Altura y Profundidad
| Concepto | Definición |
|---|---|
| **Altura** | Cantidad de **aristas** desde el nodo `x` hasta el nodo **más profundo** bajo él (la ruta más larga a la que se puede llegar). |
| **Profundidad (Depth)** | Cantidad de **aristas** desde la **raíz** hasta el nodo `x`. |

- La altura se puede trazar contando niveles o recorriendo nodos hasta llegar al último nivel.
- Un árbol con **solo el nodo raíz** tiene **altura 0**.
- La altura de un **árbol** es la altura de su raíz.
- Una **hoja** siempre tiene altura 0.
- La raíz siempre tiene profundidad 0.
- La altura mira hacia **abajo** (hacia las hojas); la profundidad mira hacia **arriba** (hacia la raíz).

Ejemplo con el árbol de la raíz `5`:
| Nodo | Altura | Profundidad |
|---|---|---|
| 5 (raíz) | 2 | 0 |
| 10 | 1 | 1 |
| 3 | 1 | 1 |
| 20 | 0 | 2 |
| 17 | 0 | 2 |

```python
def altura(nodo):
    if nodo is None:
        return -1          # convención: árbol vacío = -1, así una hoja = 0
    return 1 + max(altura(nodo.left), altura(nodo.right))
```

## Propiedades cuantitativas
- Máximo de nodos en el nivel `k`: **2ᵏ**.
- Máximo de nodos en un árbol de altura `h`: **2^(h+1) − 1**.
- Altura mínima posible con `n` nodos: **⌊log₂ n⌋** (por eso los árboles balanceados dan O(log n)).
- Altura máxima con `n` nodos: **n − 1** (árbol degenerado, equivalente a una lista enlazada).

## Tipos de árboles binarios
| Tipo | Característica |
|---|---|
| **Lleno (Full)** | Todo nodo tiene 0 o 2 hijos. |
| **Completo (Complete)** | Todos los niveles llenos excepto quizá el último, que se llena de izquierda a derecha (base del **Heap**). |
| **Perfecto (Perfect)** | Todos los niveles completamente llenos y todas las hojas al mismo nivel. |
| **Degenerado** | Cada nodo tiene un solo hijo; se comporta como lista enlazada (altura n − 1). |
| **Balanceado** | La diferencia de altura entre subárbol izquierdo y derecho es pequeña en todos los nodos. |

## Llaves
- De ahora en adelante los datos se organizan pensando en **llaves** (key).
- Es deseable (y suele ser un requisito) que las llaves sean **ÚNICAS**, ej: `id`.

## Divide y Vencerás (Subárboles)
- Todo nodo es la raíz de un **subárbol**. Un árbol se compone de: **Raíz + Subárbol Izquierdo + Subárbol Derecho**.
- Cada subárbol es a su vez un árbol, por lo que se resuelve con el mismo procedimiento: **recursión**.
- Si se domina esta idea, resolver problemas con árboles se vuelve mucho más sencillo.

```
            (Raíz)
           /      \
   [Sub-Árbol   [Sub-Árbol
     Izq]          Der]
      \_______  _______/
              \/
            (Todo)
```

- Estructura general de una función recursiva sobre árboles:
  1. **Caso base:** el nodo es `None` -> se detiene.
  2. **Caso recursivo:** se procesa el subárbol izquierdo y el derecho.
- También se pueden implementar de forma **iterativa** (con una cola o una pila explícita).

## Recorridos de un Árbol
- **Recorrer** un árbol es pasar por todos sus nodos; **visitar** un nodo es procesarlo (ej. imprimirlo).
- Durante el recorrido se *pasa* por un nodo varias veces (al bajar, al volver desde el hijo izquierdo, al volver desde el hijo derecho), pero solo se *visita* **una vez**. El momento en que se visita define el tipo de recorrido.
- Las dos grandes categorías de búsqueda son:

| Categoría | Nombre | Estrategia |
|---|---|---|
| **BFS** | Breadth-First Search | Por **amplitud** (anchura): se procesan **todos los nodos de un nivel** antes de pasar al siguiente, de izquierda a derecha. |
| **DFS** | Depth-First Search | Por **profundidad**: se baja lo más posible por una rama antes de retroceder. Tiene tres variantes: Pre-Orden, En-Orden y Pos-Orden. |

> **Nota:** programar estos algoritmos no es tan fácil como verlos en papel.

### BFS (En orden por nivel)
- Usa una **Cola (Queue, FIFO)**: se visita un nodo y se encolan sus hijos (izquierdo primero, luego derecho).

```python
from collections import deque

def bfs(raiz):
    if raiz is None:
        return
    cola = deque([raiz])
    while cola:
        nodo = cola.popleft()          # dequeue
        print(nodo.datos)              # visitar
        if nodo.left is not None:
            cola.append(nodo.left)     # enqueue
        if nodo.right is not None:
            cola.append(nodo.right)

# O también

class Node:
    def __init__(self,val=None):
      self.key = val
      self.left = None
      self.right = None

class Tree:
    def __init__(self):
      self.root = None

    def bfs(self):
        if self.root is None:
            return []

        result = []
        cola = queue.Queue()
        cola.put(self.root)

        while not cola.empty():
            tmp = cola.get()
            result.append(tmp.key)
            if tmp.left is not None:
                cola.put(tmp.left)
            if tmp.right is not None:
                cola.put(tmp.right)

        return result
```

### DFS (Por profundidad)
- Se implementa de forma natural con **recursión** (usa el *stack* de llamadas del CPU) o de forma iterativa con una **Pila (Stack, LIFO)**.
- La diferencia entre las tres variantes es **cuándo se visita la raíz** respecto a sus subárboles:

| Recorrido | Orden | Raíz se visita... |
|---|---|---|
| **Pre-Orden** | Raíz - Izq - Der | Antes de los subárboles |
| **En-Orden** | Izq - Raíz - Der | Entre los subárboles |
| **Pos-Orden** | Izq - Der - Raíz | Después de los subárboles |

```python
def pre_orden(nodo):
    if nodo is None:
        return
    print(nodo.datos)          # Raíz
    pre_orden(nodo.left)       # Izq
    pre_orden(nodo.right)      # Der

def en_orden(nodo):            # solo 4 líneas
    if nodo:
        en_orden(nodo.left)    # Izq
        print(nodo.datos)      # Raíz
        en_orden(nodo.right)   # Der

def pos_orden(nodo):
    if nodo is None:
        return
    pos_orden(nodo.left)       # Izq
    pos_orden(nodo.right)      # Der
    print(nodo.datos)          # Raíz
```

- Versión iterativa de Pre-Orden con pila (se apila primero el hijo derecho para que el izquierdo salga antes):
```python
def pre_orden_iterativo(raiz):
    if raiz is None:
        return
    pila = [raiz]
    while pila:
        nodo = pila.pop()
        print(nodo.datos)
        if nodo.right is not None:
            pila.append(nodo.right)
        if nodo.left is not None:
            pila.append(nodo.left)
```

## Ejemplo 1
```
              C                    Nivel 0
            /   \
          G       H                Nivel 1
           \     /  \
            R   P    Z             Nivel 2
               / \
              E   J                Nivel 3
             / \
            S   Y                  Nivel 4
```

| Recorrido | Resultado |
|---|---|
| **BFS** | C - G - H - R - P - Z - E - J - S - Y |
| **Pre-Orden** | C - G - R - H - P - E - S - Y - J - Z |
| **En-Orden** | G - R - C - S - E - Y - P - J - H - Z |
| **Pos-Orden** | R - G - S - Y - E - J - P - Z - H - C |

- Hojas: `R`, `Z`, `J`, `S`, `Y`. Altura del árbol: **4**. Profundidad de `Y`: **4**.

```python
raiz = Node("C")
raiz.left = Node("G")
raiz.left.right = Node("R")
raiz.right = Node("H")
raiz.right.right = Node("Z")
raiz.right.left = Node("P")
raiz.right.left.left = Node("E")
raiz.right.left.right = Node("J")
raiz.right.left.left.left = Node("S")
raiz.right.left.left.right = Node("Y")
```

## Ejemplo 2
```
                20                         Nivel 0
              /    \
            3        28                    Nivel 1
           /        /   \
          7        8      5                Nivel 2
         / \      / \    / \
       11   4   NULL NULL 14  21           Nivel 3
```

| Recorrido | Resultado |
|---|---|
| **BFS (En orden por nivel)** | 20 - 3 - 28 - 7 - 8 - 5 - 11 - 4 - 14 - 21 |
| **Pre-Orden** (Raíz-Izq-Der) | 20 - 3 - 7 - 11 - 4 - 28 - 8 - 5 - 14 - 21 |
| **En-Orden** (Izq-Raíz-Der) | 11 - 7 - 4 - 3 - 20 - 8 - 28 - 14 - 5 - 21 |
| **Pos-Orden** (Izq-Der-Raíz) | 11 - 4 - 7 - 3 - 8 - 14 - 21 - 5 - 28 - 20 |

- Hojas: `11`, `4`, `8`, `14`, `21`. Altura del árbol: **3**.
- Traza de Pre-Orden: se visita `20`, se baja a `3`, luego a `7`, luego a `11` (hoja, retrocede), luego a `4` (hoja, retrocede hasta `20`), y se repite el proceso en el subárbol derecho (`28`).

## Complejidad
| Recorrido | Tiempo | Espacio extra | Estructura auxiliar |
|---|---|---|---|
| BFS | O(n) | O(w), *w* = ancho máximo del árbol | Cola |
| DFS (Pre / En / Pos) | O(n) | O(h), *h* = altura del árbol | Stack de llamadas o Pila |

- Todos los recorridos visitan cada nodo exactamente una vez -> **O(n)**.
- En un árbol degenerado, `h = n − 1`, por lo que la recursión puede provocar **Stack Overflow**.

## ¿Cuándo usar cuál? (resumen rápido)
- **BFS:** procesar por niveles, encontrar el nodo más cercano a la raíz, calcular el ancho del árbol.
- **Pre-Orden:** copiar o serializar un árbol (la raíz se procesa primero, permite reconstruirlo).
- **En-Orden:** en un árbol de búsqueda (BST) entrega los datos **ordenados**.
- **Pos-Orden:** eliminar o liberar un árbol (los hijos se procesan antes que el padre) y evaluar expresiones.
