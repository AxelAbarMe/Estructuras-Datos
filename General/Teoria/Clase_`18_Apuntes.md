# =========================================
# SEGMENTO 16: ÁRBOLES AVL
# =========================================

## Árboles AVL

* Un **AVL** es un **BST auto-balanceado**: cumple siempre la propiedad de orden del BST (sub-árbol izquierdo menor, sub-árbol derecho mayor).
* Los árboles **AVL** y **Red-Black** son **auto-balanceados**: se corrigen solos después de cada operación.
* Se balancea con **cada inserción** y con **cada eliminación**.
* En un programa con **muchas inserciones** se pierde rendimiento, porque cada inserción puede provocar rotaciones.

---

## Factor de balance (FB)

* Es una variable que se calcula para **todos los nodos** del árbol.
* Se define como la **diferencia entre la altura del sub-árbol izquierdo y la del sub-árbol derecho**:

```
FB(nodo) = altura(sub-árbol izquierdo) - altura(sub-árbol derecho)
```

| Situación | FB |
|---|---|
| Nodo **hoja** | 0 |
| Sub-árbol izquierdo más alto | Positivo |
| Sub-árbol derecho más alto | Negativo |
| Nodo **balanceado** | -1, 0 o 1 |
| Nodo **desbalanceado** | 2 o -2 (o más en valor absoluto) |

* **El árbol está balanceado si el FB no supera 1 (en valor absoluto) en cada nodo del árbol.**
* Si algún nodo tiene FB fuera de ese rango, se llama **nodo "x"** al nodo donde está el desbalance.
* Se arregla **siempre primero el nodo "x" más bajo** (el primero que aparece subiendo desde el nodo insertado). Al corregirlo, normalmente se corrigen también los desbalances de los nodos superiores.

---

## Casos de desbalance

| Caso | Dónde se hizo la inserción (respecto a "x") | Solución |
|---|---|---|
| **1. LL** | Sub-árbol **izquierdo** del hijo **izquierdo** | Rotación simple a la **derecha** en "x" |
| **2. RR** | Sub-árbol **derecho** del hijo **derecho** | Rotación simple a la **izquierda** en "x" |
| **3. LR** | Sub-árbol **izquierdo** del hijo **derecho** | Rotación doble: derecha en el hijo derecho de "x", luego izquierda en "x" |
| **4. RL** | Sub-árbol **derecho** del hijo **izquierdo** | Rotación doble: izquierda en el hijo izquierdo de "x", luego derecha en "x" |

* Los casos **LL** y **RR** (rotaciones simples) aplican tanto a **inserciones** como a **borrados**.
* Después de **cada** rotación el árbol debe seguir cumpliendo la propiedad **BST**.
* La nomenclatura LR / RL usada aquí sigue la de la clase (nombrada por el lugar donde se inserta respecto a "x"); en otros textos puede aparecer intercambiada.

---

## Caso 1: LL (rotación simple a la derecha)

* Aplica si la inserción se hace en el **sub-árbol izquierdo del hijo izquierdo** de "x".
* Se resuelve con una **rotación simple a la derecha** en el nodo "x".
* Se gira el eje hacia la derecha, moviendo todos sus nodos en conjunto.

### Ejemplo 1

```
    10
   /  \
  7    19   <- "x" = 19 (el primer desbalance desde abajo)
      /
     15
    /
   13  <- Nodo insertado
```

Se aplica la rotación simple a la derecha en 19:

```
    10
   /  \
  7    15      -> Rotación aplicada
      /  \
     13   19
```

### Ejemplo 2

```
       14  <- Nodo "x" desbalanceado
      /  \
     6    25
    / \
   4  10
  /
 2
```

* Al rotar, el **hijo derecho del nodo 6** (el 10) pasa a ser el **hijo izquierdo de la raíz antigua** (el 14).

```
       6
      /  \
     4    14   <- 10 (hijo derecho de 6) ahora es hijo izquierdo de 14
    /    /  \
   2   10    25
```

---

## Caso 2: RR (rotación simple a la izquierda)

* Aplica si la inserción se hace en el **sub-árbol derecho del hijo derecho** de "x".
* Se resuelve con una **rotación simple a la izquierda** en el nodo "x".

```
    18
   /  \
  10    23    <- Nodo 10 es el "x" desbalanceado
   \
    15
     \
      17     <- Nodo insertado
```

```
    18
   /  \
  15    23
 / \
10  17
```

* Aplica lo mismo: el **hijo izquierdo** del nuevo nodo raíz del sub-árbol pasa a ser el **hijo derecho** de la raíz antigua (cuando existe).

---

## Caso 3: LR (rotación doble)

* Aplica si la inserción se hace en el **sub-árbol izquierdo del hijo derecho** de "x".
* Se resuelve con una **rotación doble**:
  1. Rotación simple a la **derecha** en el **hijo derecho** de "x".
  2. Rotación simple a la **izquierda** en "x".

```
    18
   /  \
  10    25   <- Nodo "x" encontrado por FB = 1 - 3 = -2
 /     /  \
6     20  30
         /  \
        28   33
         \
          29  <- Nodo insertado
```

**Paso 1:** rotación simple a la derecha en el hijo derecho de x (el 30).

```
    18
   /  \
  10    25   <- "x"
 /     /  \
6     20  28
            \
             30
            /  \
          29    33
```

* El árbol siempre debe cumplir BST en todos los pasos de las rotaciones y movimientos.

**Paso 2:** rotación simple a la izquierda en x (el 25).

```
    18
   /  \
  10    28
 /     /  \
6     25   30
     /     / \
    20    29  33
```

---

## Caso 4: RL (rotación doble)

* Aplica si la inserción se hace en el **sub-árbol derecho del hijo izquierdo** de "x".
* Se resuelve con una **rotación doble**:
  1. Rotación simple a la **izquierda** en el **hijo izquierdo** de "x".
  2. Rotación simple a la **derecha** en "x".

```
    16   <- Nodo "x". FB = 3 - 1 = 2
   /  \
  11    17
 / \
7   13
      \
       15   <- Nodo insertado
```

**Paso 1:** rotación simple a la izquierda en el hijo izquierdo de x (el 11).

```
      16   <- Nodo "x"
     /  \
    13    17
   /  \
  11   15
 /
7
```

**Paso 2:** rotación simple a la derecha en x (el 16).

```
      13
     /  \
    11   16
   /    /  \
  7   15    17
```

* El nodo 15 (hijo derecho del hijo izquierdo de x) se mueve como **hijo izquierdo directo** de x al aplicar la rotación simple.

---

## Implementación en Python

```python
class NodeAVL:
    def __init__(self, val=None):
        self.key = val
        self.left = None
        self.right = None
        self.height = 1          # altura contada en nodos


def altura(n):
    return n.height if n else 0

def actualizar(n):
    n.height = 1 + max(altura(n.left), altura(n.right))

def factor_balance(n):
    return altura(n.left) - altura(n.right) if n else 0


def rotar_derecha(y):
    x = y.left
    y.left = x.right
    x.right = y
    actualizar(y)
    actualizar(x)
    return x

def rotar_izquierda(x):
    y = x.right
    x.right = y.left
    y.left = x
    actualizar(x)
    actualizar(y)
    return y


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return NodeAVL(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        actualizar(node)
        fb = factor_balance(node)

        # Caso 1: LL
        if fb > 1 and key < node.left.key:
            return rotar_derecha(node)
        # Caso 2: RR
        if fb < -1 and key > node.right.key:
            return rotar_izquierda(node)
        # Caso 4: RL (derecho del hijo izquierdo)
        if fb > 1 and key > node.left.key:
            node.left = rotar_izquierda(node.left)
            return rotar_derecha(node)
        # Caso 3: LR (izquierdo del hijo derecho)
        if fb < -1 and key < node.right.key:
            node.right = rotar_derecha(node.right)
            return rotar_izquierda(node)

        return node
```

---

## Práctica - Lab

### a) Insertar al árbol: 19, 23, 28, 7, 15, 20, 13, 6

| Inserción | ¿Desbalance? | Nodo "x" | Caso | Rotación |
|---|---|---|---|---|
| 19 | No | - | - | - |
| 23 | No | - | - | - |
| 28 | Sí | 19 | RR | Simple a la izquierda en 19 |
| 7 | No | - | - | - |
| 15 | Sí | 19 | RL | Izquierda en 7, derecha en 19 |
| 20 | Sí | 23 | RL | Izquierda en 15, derecha en 23 |
| 13 | Sí | 15 | RL | Izquierda en 7, derecha en 15 |
| 6 | No | - | - | - |

**Insertar 19, 23, 28:** la inserción de 28 desbalancea el 19 (FB = -2), caso RR.

```
 19                 23
   \               /  \
    23     ->    19    28
      \
       28
```

**Insertar 7 y 15:** el 15 queda como hijo derecho de 7, y el 19 se desbalancea (FB = 2), caso RL.

```
      23                  23                 23
     /  \                /  \               /  \
   19    28             19   28           15    28
  /                    /                 /  \
 7             ->    15        ->       7    19
  \                  /
   15               7
```

* Paso 1: rotación a la izquierda en 7. Paso 2: rotación a la derecha en 19.

**Insertar 20:** el 20 queda a la derecha de 19, y el 23 se desbalancea (FB = 2), caso RL.

```
        23                    23                    19
       /  \                  /  \                  /  \
     15    28              19    28              15    23
    /  \          ->      /  \          ->       /     /  \
   7    19              15    20                7    20    28
          \            /
           20         7
```

* Paso 1: rotación a la izquierda en 15. Paso 2: rotación a la derecha en 23.

**Insertar 13:** el 13 queda a la derecha de 7, y el 15 se desbalancea (FB = 2), caso RL.

```
        19                       19                      19
       /  \                     /  \                    /  \
     15    23                 13    23                13    23
    /     /  \       ->      /  \   /  \      ->     /  \  /  \
   7    20    28           7    15 20   28           7   15 20  28
    \
     13
```

* Paso 1: rotación a la izquierda en 7. Paso 2: rotación a la derecha en 15.

**Insertar 6:** se inserta como hijo izquierdo de 7. No hay desbalance.

**Árbol final:**

```
       19
     /    \
    13      23
   /  \    /  \
  7    15 20    28
 /
6
```

---

### b) Insertar al árbol: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

| Inserción | ¿Desbalance? | Nodo "x" | Caso | Rotación |
|---|---|---|---|---|
| 1 | No | - | - | - |
| 2 | No | - | - | - |
| 3 | Sí | 1 | RR | Simple a la izquierda en 1 |
| 4 | No | - | - | - |
| 5 | Sí | 3 | RR | Simple a la izquierda en 3 |
| 6 | Sí | 2 | RR | Simple a la izquierda en 2 |
| 7 | Sí | 5 | RR | Simple a la izquierda en 5 |
| 8 | No | - | - | - |
| 9 | Sí | 7 | RR | Simple a la izquierda en 7 |
| 10 | Sí | 6 | RR | Simple a la izquierda en 6 |

**Insertar 1, 2, 3:** desbalance en 1 (RR).

```
 1                2
  \              / \
   2      ->    1   3
    \
     3
```

**Insertar 4:** sin desbalance.

```
    2
   / \
  1   3
       \
        4
```

**Insertar 5:** desbalance en 3 (RR).

```
    2                  2
   / \                / \
  1   3              1   4
       \     ->         / \
        4              3   5
         \
          5
```

**Insertar 6:** desbalance en 2 (FB = 1 - 3 = -2), caso RR. El 3 (hijo izquierdo del nuevo raíz 4) pasa a ser hijo derecho del 2.

```
    2                      4
   / \                    /  \
  1   4                  2    5
     / \        ->      / \    \
    3   5              1   3    6
         \
          6
```

**Insertar 7:** desbalance en 5 (RR).

```
      4                    4
     /  \                 /  \
    2    5               2    6
   / \    \      ->     / \  / \
  1   3    6           1   3 5   7
            \
             7
```

**Insertar 8:** sin desbalance.

```
      4
     /  \
    2    6
   / \  / \
  1  3 5   7
            \
             8
```

**Insertar 9:** desbalance en 7 (RR).

```
      4                       4
     /  \                    /  \
    2    6                  2    6
   / \  / \                / \  / \
  1  3 5   7      ->      1  3 5   8
            \                     / \
             8                   7   9
              \
               9
```

**Insertar 10:** desbalance en 6 (FB = 1 - 3 = -2), caso RR. El 7 pasa a ser hijo derecho del 6.

```
      4                         4
     /  \                      /  \
    2    6                    2    8
   / \  / \                  / \  / \
  1  3 5   8       ->       1  3 6   9
          / \                   / \   \
         7   9                 5   7   10
              \
               10
```

**Árbol final:**

```
          4
        /   \
      2       8
     / \     /  \
    1   3   6    9
           / \    \
          5   7    10
```

---

### c) Insertar al árbol: 25, 14, 33, 6, 10, 40, 38, 35, 12, 8

| Inserción | ¿Desbalance? | Nodo "x" | Caso | Rotación |
|---|---|---|---|---|
| 25 | No | - | - | - |
| 14 | No | - | - | - |
| 33 | No | - | - | - |
| 6 | No | - | - | - |
| 10 | Sí | 14 | RL | Izquierda en 6, derecha en 14 |
| 40 | No | - | - | - |
| 38 | Sí | 33 | LR | Derecha en 40, izquierda en 33 |
| 35 | No | - | - | - |
| 12 | No | - | - | - |
| 8 | No | - | - | - |

**Insertar 25, 14, 33, 6:** sin desbalance.

```
     25
    /  \
  14    33
 /
6
```

**Insertar 10:** el 10 queda a la derecha de 6, y el 14 se desbalancea (FB = 2), caso RL.

```
     25                 25                 25
    /  \               /  \               /  \
  14    33           14    33           10    33
 /            ->    /             ->    /  \
6                 10                  6    14
 \               /
  10            6
```

* Paso 1: rotación a la izquierda en 6. Paso 2: rotación a la derecha en 14.

**Insertar 40:** sin desbalance.

```
      25
     /  \
   10    33
  /  \     \
 6    14    40
```

**Insertar 38:** el 38 queda a la izquierda de 40, y el 33 se desbalancea (FB = -2), caso LR.

```
      25                25                  25
     /  \              /  \                /  \
   10    33          10    33            10    38
  /  \     \        /  \     \          /  \   /  \
 6    14    40     6   14     38       6   14 33   40
            /                   \
          38                     40
```

* Paso 1: rotación a la derecha en 40. Paso 2: rotación a la izquierda en 33.

**Insertar 35:** se inserta como hijo derecho de 33. No hay desbalance (FB(25) = 2 - 3 = -1).

```
        25
       /  \
     10    38
    /  \   /  \
   6   14 33   40
            \
             35
```

**Insertar 12:** se inserta como hijo izquierdo de 14. No hay desbalance.

**Insertar 8:** se inserta como hijo derecho de 6. No hay desbalance (FB(10) = 2 - 2 = 0).

**Árbol final:**

```
              25
            /    \
          10       38
         /  \     /  \
        6    14  33   40
         \   /     \
          8 12      35
```

---

## Resumen general del tema

* Un **AVL** es un BST **auto-balanceado** que se corrige con **cada inserción y cada eliminación**, usando el **factor de balance (FB)**.
* **FB = altura del sub-árbol izquierdo - altura del sub-árbol derecho**; el árbol está balanceado si el FB de cada nodo es **-1, 0 o 1**. Las hojas siempre tienen FB = 0.
* Se corrige siempre el **primer nodo "x" desbalanceado** desde abajo hacia arriba.
* Hay **4 casos**: **LL** (rotación simple a la derecha), **RR** (rotación simple a la izquierda), **LR** (derecha en el hijo derecho y luego izquierda en "x") y **RL** (izquierda en el hijo izquierdo y luego derecha en "x").
* Durante todas las rotaciones el árbol debe seguir cumpliendo la propiedad **BST**.
* Con muchas inserciones se pierde rendimiento por las rotaciones, pero se garantiza altura **O(log n)** y operaciones **O(log n)** en el peor caso.
* En la práctica: el inciso **a)** requirió 1 rotación simple y 3 dobles, el **b)** (valores ascendentes) requirió 6 rotaciones simples y quedó con raíz **4**, y el **c)** requirió solo 2 rotaciones dobles.
