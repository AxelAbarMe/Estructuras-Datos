# =========================================
# SEGMENTO 15: BORRADO EN ÁRBOLES BINARIOS Y BST
# =========================================

## Tuplas en Python

* Una **tupla** es como una lista, pero es **inmutable**: una vez creada, sus elementos no se pueden modificar, agregar ni eliminar.
* Se escribe con paréntesis: `(nodo, padre)`.
* En la cola se usa una tupla `(nodo, padre)` por elemento, de modo que al sacarla se puede **desempaquetar** directamente en dos variables.

```python
from collections import deque

q = deque([(self.root, None)])   # cola con una tupla: (nodo, padre)

cur, parent = q.popleft()        # desempaquetado de la tupla
# cur    -> root
# parent -> None
```

---

## Estado de la cola `q` durante el recorrido

| Posición en la cola | Contenido (tupla) | Significado |
|---|---|---|
| 1 | `(root, None)` | La raíz no tiene padre |
| 2 | `(n1, root)` | `n1` es hijo de `root` |
| 3 | `(n2, n1)` | `n2` es hijo de `n1` |
| ... | ... | ... |

* El **primer nodo** que se inserta en `q` es la raíz, cuyo padre es `None`.
* Cada elemento guarda el **padre** porque al final será necesario para **"desconectar"** el último nodo del árbol.

---

## Borrar de un árbol binario (general)

```python
def delete(self, val):
    if self.root is None:
        return False

    target = None
    last, last_parent = None, None
    q = deque([(self.root, None)])

    while q:
        cur, parent = q.popleft()
        if target is None and cur.key == val:
            target = cur
        last, last_parent = cur, parent
        if cur.left:
            q.append((cur.left, cur))
        if cur.right:
            q.append((cur.right, cur))

    if target is None:
        return False

    target.key = last.key

    if last_parent is None:
        self.root = None
    elif last_parent.right is last:
        last_parent.right = None
    else:
        last_parent.left = None
    return True
```

### Idea del algoritmo

1. Se recorre el árbol por niveles (**BFS**) con una cola de tuplas `(nodo, padre)`.
2. Durante el recorrido se **busca el nodo `target`** con el valor a borrar.
3. Al terminar el recorrido, `last` es el **último nodo** visitado por niveles (el más profundo y más a la derecha), y `last_parent` es su padre.
4. Se **copia la llave del último nodo** en `target` (`target.key = last.key`).
5. Se **elimina el último nodo** desconectándolo de su padre.

### Desconexión del último nodo

| Condición | Acción | Significado |
|---|---|---|
| `last_parent is None` | `self.root = None` | El árbol tenía un solo nodo (la raíz) |
| `last_parent.right is last` | `last_parent.right = None` | El último es hijo derecho |
| En otro caso | `last_parent.left = None` | El último es hijo izquierdo |

* Si `target is None`, el valor no existe y la función retorna `False`.
* Si se borró correctamente, retorna `True`.
* **Complejidad:** **O(n)**, pues siempre se recorre todo el árbol.
* Se borra el **último nodo** (y no el `target` directamente) para no dejar huecos ni romper la estructura del árbol.

---

## BST (Binary Search Tree)

* **BST** = **Binary Search Tree** (Árbol Binario de Búsqueda).
* **Propiedad de orden:** para cada nodo, los elementos del **sub-árbol izquierdo** son **menores** y los del **sub-árbol derecho** son **mayores**.

---

## Resumen general del tema

* Una **tupla** es como una lista pero **inmutable**; se usa en la cola como `(nodo, padre)` para conservar el padre de cada nodo.
* El primer elemento de la cola es `(root, None)`, ya que la raíz no tiene padre.
* El **borrado en un árbol binario general** busca el nodo a borrar, encuentra el último nodo por niveles, copia su valor en el nodo a borrar y luego desconecta el último nodo.
* La complejidad del borrado es **O(n)**.
* Un **BST** es un árbol donde, para cada nodo, el sub-árbol izquierdo contiene elementos menores y el derecho elementos mayores.

## Implementación de un BST (operaciones básicas)

### Objetivo

* Implementar las funciones básicas de un **árbol binario de búsqueda (BST)**.

### Operaciones requeridas

* **Insertar** un valor en el árbol.
* **Borrar** un elemento del árbol.
* **Buscar** un elemento del árbol.
* **Verificar** si un árbol (dado un nodo raíz) es un BST o no.

---

### Código completo: `bst.py`

```python
class Node:
    def __init__(self, val=None):
        self.key = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ---------- Insertar ----------
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    # ---------- Buscar ----------
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # ---------- Borrar ----------
    def delete(self, key):
        self.root, borrado = self._delete(self.root, key)
        return borrado

    def _delete(self, node, key):
        if node is None:
            return None, False

        if key < node.key:
            node.left, borrado = self._delete(node.left, key)
            return node, borrado
        if key > node.key:
            node.right, borrado = self._delete(node.right, key)
            return node, borrado

        # Se encontró el nodo a borrar
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        # Dos hijos: se reemplaza por el sucesor en-orden
        sucesor = node.right
        while sucesor.left is not None:
            sucesor = sucesor.left
        node.key = sucesor.key
        node.right, _ = self._delete(node.right, sucesor.key)
        return node, True

    # ---------- Recorrido en-orden ----------
    def en_orden(self):
        resultado = []
        self._en_orden(self.root, resultado)
        return resultado

    def _en_orden(self, node, resultado):
        if node is None:
            return
        self._en_orden(node.left, resultado)
        resultado.append(node.key)
        self._en_orden(node.right, resultado)


# ---------- Verificar si un árbol es BST ----------
def is_bst(root):
    return _is_bst(root, None, None)

def _is_bst(node, minimo, maximo):
    if node is None:
        return True
    if minimo is not None and node.key <= minimo:
        return False
    if maximo is not None and node.key >= maximo:
        return False
    return (_is_bst(node.left, minimo, node.key) and
            _is_bst(node.right, node.key, maximo))
```

---

### Código de prueba: `main.py`

```python
import bst

arbol = bst.BST()
for v in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    arbol.insert(v)

print(arbol.en_orden())          # [1, 3, 4, 6, 7, 8, 10, 13, 14]
print(arbol.search(6).key)       # 6
print(arbol.search(99))          # None

print(arbol.delete(3))           # True
print(arbol.en_orden())          # [1, 4, 6, 7, 8, 10, 13, 14]
print(arbol.delete(99))          # False

print(bst.is_bst(arbol.root))    # True

# Árbol que NO es BST
malo = bst.Node(5)
malo.left = bst.Node(3)
malo.right = bst.Node(7)
malo.left.right = bst.Node(9)    # 9 está en el sub-árbol izquierdo de 5 pero es mayor
print(bst.is_bst(malo))          # False
```

---

### Explicación de las operaciones

#### Insertar

* Si el nodo actual es `None`, se crea el nuevo nodo en esa posición.
* Si la llave es **menor**, se inserta en el sub-árbol **izquierdo**; si es **mayor**, en el **derecho**.
* Si la llave ya existe, no se duplica.

#### Buscar

* Se compara la llave con el nodo actual y se **descarta la mitad** del árbol en cada paso (izquierda si es menor, derecha si es mayor).

#### Borrar

| Caso | Acción |
|---|---|
| Nodo **sin hijos** (hoja) | Se elimina devolviendo `None` (se toma `node.right`, que es `None`) |
| Nodo con **un solo hijo** | Se reemplaza el nodo por su único hijo |
| Nodo con **dos hijos** | Se copia la llave del **sucesor en-orden** (el menor del sub-árbol derecho) y luego se borra ese sucesor |

* La función retorna `True` si se borró y `False` si la llave no existía.

#### Verificar si es BST

* No basta con comparar cada nodo con sus hijos directos: se debe garantizar que **todo el sub-árbol izquierdo sea menor** y **todo el derecho sea mayor**.
* Por eso se pasan los límites `minimo` y `maximo` en la recursión:
  * Al bajar a la **izquierda**, el nodo actual pasa a ser el nuevo **máximo**.
  * Al bajar a la **derecha**, el nodo actual pasa a ser el nuevo **mínimo**.
* Alternativa: un recorrido **en-orden** de un BST produce una secuencia estrictamente creciente.

---

### Complejidad

| Operación | Promedio | Peor caso (árbol degenerado) |
|---|---|---|
| **Insertar** | O(log n) | O(n) |
| **Buscar** | O(log n) | O(n) |
| **Borrar** | O(log n) | O(n) |
| **Verificar si es BST** | O(n) | O(n) |
