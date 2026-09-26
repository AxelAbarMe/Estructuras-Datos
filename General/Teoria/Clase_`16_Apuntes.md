# =========================================
# SEGMENTO 14: BÚSQUEDA, ALTURA E INSERCIÓN EN ÁRBOLES BINARIOS
# =========================================

## Búsqueda de un elemento en un árbol binario

Buscar en un árbol binario "general" (no ordenado) implica **recorrer todos los nodos** hasta encontrar la llave, ya que no existe ningún criterio de orden que permita descartar ramas completas (a diferencia de un BST).

### Búsqueda Iterativa (con Cola / BFS)

```python
def iterative_search(self, key):
    return self._iterative_search(key)

def _iterative_search(self, key):
    if self.root is None:
        return None
    cola = collections.deque()
    cola.append(self.root)

    while cola:
        tmp = cola.popleft()
        if tmp.key == key:
            return tmp
        if tmp.left is not None:
            cola.append(tmp.left)
        if tmp.right is not None:
            cola.append(tmp.right)
    return None
```

### Búsqueda Recursiva

```python
def recursive_search(self, key):
    return self._recursive_search(self.root, key)

def _recursive_search(self, current_node, key):
    if current_node is None:
        return None
    if current_node.key == key:
        return current_node
    if current_node.left is not None:
        tmp = self._recursive_search(current_node.left, key)
        if tmp is not None:
            return tmp
    if current_node.right is not None:
        tmp = self._recursive_search(current_node.right, key)
        if tmp is not None:
            return tmp
    return None
```

### Búsqueda Recursiva (versión compacta con OR)

```python
def recursive_search(self, key):
    return self._recursive_search(self.root, key)

def _recursive_search(self, node, key):
    if node is None or node.key == key:
        return node
    izq = self._recursive_search(node.left, key)
    return izq if izq is not None else self._recursive_search(node.right, key)
```

* Ambas versiones recursivas son equivalentes; la segunda aprovecha el **cortocircuito del operador `or`** para reducir las líneas de código.
* **Complejidad:** ambas búsquedas (iterativa y recursiva) son **O(n)**, pues en el peor caso deben visitarse todos los nodos.

---

## Altura del árbol

```python
def height(self):
    return self._height(self.root)

def _height(self, root):
    if root is None:
        return -1
    return max(self._height(root.left) + 1, self._height(root.right) + 1)
```

* Es la misma idea que `altura()` del Segmento 12, solo que planteada como `max(altura_izq + 1, altura_der + 1)` en vez de `1 + max(altura_izq, altura_der)`; ambas expresiones son matemáticamente equivalentes.
* Un árbol vacío tiene altura **-1**; un único nodo (hoja) tiene altura **0**.

---

## Inserción (por niveles / BFS)

```python
def insert(self, key):
    if self.root is None:
        self.root = Node(key)
        return
    cola = collections.deque()
    cola.append(self.root)
    while cola:
        tmp = cola.popleft()
        if tmp.key == key:
            return tmp
        if tmp.left is not None:
            cola.append(tmp.left)
        else:
            tmp.left = Node(key)
            return
        if tmp.right is not None:
            cola.append(tmp.right)
        else:
            tmp.right = Node(key)
            return
```

* No es una inserción de **BST** (no compara valores para decidir izquierda/derecha); inserta la nueva llave en el **primer espacio libre** encontrado recorriendo por niveles (igual que llenar un **Heap**), manteniendo el árbol lo más "completo" posible.
* Si la llave ya existe, se detiene sin duplicarla.

---

## Código completo: `arbol.py`

```python
import queue
import collections


class Node:
    def __init__(self, val=None):
        self.key = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def create_from_file(self, filename):
        try:
            handle = open(filename, "r")
        except IOError:
            return None

        self.root = self._create_from_file(handle)
        handle.close()

        if self.root is None:
            return None
        return 1

    def _create_from_file(self, handle):
        c = handle.read(1)
        if c == '$':
            return None

        tmp = Node(c)
        tmp.left = self._create_from_file(handle)
        tmp.right = self._create_from_file(handle)
        return tmp

    def print_tree(self):
        self._print_tree(" ", self.root, False)

    def _print_tree(self, p, r, is_left):
        if r:
            print(p, end='')
            if is_left:
                print("|--", end='')
                s = "|    "
            else:
                print("'--", end='')
                s = "    "
            print(r.key)
            self._print_tree(p + s, r.left, True)
            self._print_tree(p + s, r.right, False)

    def pre_orden(self):
        self._pre_orden(self.root)

    def _pre_orden(self, root):
        if root is None:
            return
        print(root.key, end=' ')
        self._pre_orden(root.left)
        self._pre_orden(root.right)

    def pos_orden(self):
        self._pos_orden(self.root)

    def _pos_orden(self, root):
        if root is None:
            return
        self._pos_orden(root.left)
        self._pos_orden(root.right)
        print(root.key, end=' ')

    def en_orden(self):
        self._en_orden(self.root)

    def _en_orden(self, root):
        if root is None:
            return
        self._en_orden(root.left)
        print(root.key, end=' ')
        self._en_orden(root.right)

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

    def iterative_search(self, key):
        return self._iterative_search(key)

    def _iterative_search(self, key):
        if self.root is None:
            return None
        cola = collections.deque()
        cola.append(self.root)

        while cola:
            tmp = cola.popleft()
            if tmp.key == key:
                return tmp
            if tmp.left is not None:
                cola.append(tmp.left)
            if tmp.right is not None:
                cola.append(tmp.right)
        return None

    def recursive_search(self, key):
        return self._recursive_search(self.root, key)

    def _recursive_search(self, node, key):
        if node is None or node.key == key:
            return node
        izq = self._recursive_search(node.left, key)
        return izq if izq is not None else self._recursive_search(node.right, key)

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return -1
        return max(self._height(root.left) + 1, self._height(root.right) + 1)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        cola = collections.deque()
        cola.append(self.root)
        while cola:
            tmp = cola.popleft()
            if tmp.key == key:
                return tmp
            if tmp.left is not None:
                cola.append(tmp.left)
            else:
                tmp.left = Node(key)
                return
            if tmp.right is not None:
                cola.append(tmp.right)
            else:
                tmp.right = Node(key)
                return
```

---

## Código completo: `main.py`

```python
import arbol

arbolito = arbol.Tree()
arbolito.create_from_file("arbol.txt")
arbolito.print_tree()

arbolito.pre_orden()
print()
arbolito.en_orden()
print()
arbolito.pos_orden()
print()

print(arbolito.bfs())

print(arbolito.iterative_search("H").key)
print(arbolito.recursive_search("N").key)
print(arbolito.height())

arbolito.insert("Z")
print(arbolito.bfs())
```

Con `arbol.txt = CEF$H$$B$$GA$$NJ$$K$$`, la salida esperada es:

| Operación | Resultado |
|---|---|
| **Pre-Orden** | C E F H B G A N J K |
| **En-Orden** | F H E B C A G J N K |
| **Pos-Orden** | H F B E A J K N G C |
| **BFS** | ['C', 'E', 'G', 'F', 'B', 'A', 'N', 'H', 'J', 'K'] |
| **iterative_search("H").key** | H |
| **recursive_search("N").key** | N |
| **height()** | 3 |
| **BFS tras `insert("Z")`** | Z se agrega como hijo izquierdo de `F` (primer espacio libre por niveles) |

---

## Árboles Binarios, BST, AVL y Red-Black (resumen breve)

### Árbol Binario (recordatorio)
* Cada nodo tiene **como máximo 2 hijos** (izquierdo y derecho).
* No impone ningún orden entre las llaves: para buscar/insertar se debe recorrer el árbol completo -> **O(n)**.

### Árbol Binario de Búsqueda (BST)

* **Propiedad de orden:** para cada nodo, todo el **subárbol izquierdo** contiene llaves **menores**, y todo el **subárbol derecho** contiene llaves **mayores**.
* Esta propiedad permite **descartar la mitad del árbol** en cada paso, evitando recorrer todos los nodos.

```python
def bst_insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = bst_insert(root.left, key)
    else:
        root.right = bst_insert(root.right, key)
    return root

def bst_search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return bst_search(root.left, key)
    return bst_search(root.right, key)
```

* **Problema:** si las llaves se insertan en orden (ascendente o descendente), el BST se **degenera** en una lista enlazada, con altura `n - 1` y búsquedas **O(n)**.

### Árbol AVL

* Es un **BST auto-balanceado**: para cada nodo, la diferencia de altura entre su subárbol izquierdo y derecho (**factor de balance**) debe ser **-1, 0 o 1**.
* Cuando una inserción o eliminación rompe el balance, se corrige mediante **rotaciones**: simple izquierda (LL), simple derecha (RR), doble izquierda-derecha (LR) y doble derecha-izquierda (RL).

```python
def rotar_derecha(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

def rotar_izquierda(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y
```

* Garantiza altura **O(log n)** siempre, por lo que búsqueda, inserción y eliminación son **O(log n)** en el peor caso.

### Árbol Red-Black (Rojo-Negro)

* También es un **BST auto-balanceado**, pero usa un **color (rojo o negro)** por nodo en lugar de un factor de balance numérico.

**Propiedades que debe cumplir:**
1. Todo nodo es **rojo o negro**.
2. La **raíz** siempre es **negra**.
3. Todo nodo **rojo** tiene ambos hijos **negros** (no puede haber dos rojos seguidos).
4. Todo camino desde un nodo hasta sus hojas (`NULL`) tiene la **misma cantidad de nodos negros**.
5. Cada hoja `NULL` se considera **negra**.

* El balance no es tan estricto como en AVL (permite hasta el doble de altura en un lado), por lo que las **rotaciones son menos frecuentes**, haciéndolo más eficiente en escrituras.
* No se detalla su implementación aquí por su complejidad; solo se resume el concepto.

### Comparación rápida

| Estructura | Balanceo | Búsqueda (peor caso) | Uso típico |
|---|---|---|---|
| **BST** | Ninguno | O(n) (puede degenerar) | Casos simples, pocos datos |
| **AVL** | Estricto (factor ±1) | O(log n) garantizado | Muchas búsquedas, pocas escrituras |
| **Red-Black** | Relajado (colores) | O(log n) garantizado | `TreeMap`/`HashMap` en Java, `map`/`set` en C++ |

---

## Resumen general del tema

* La **búsqueda en un árbol binario general** requiere recorrer todos los nodos (O(n)), ya sea de forma **iterativa** (con cola) o **recursiva**.
* La **altura** de un árbol se calcula recursivamente comparando la altura de ambos subárboles y sumando 1; un árbol vacío tiene altura **-1**.
* La **inserción por niveles** coloca la nueva llave en el primer espacio disponible recorriendo el árbol con BFS, manteniendo la estructura lo más completa posible.
* El **BST** introduce una propiedad de orden que acelera las operaciones a **O(log n)** en promedio, pero puede degenerarse a O(n) si no está balanceado.
* Los árboles **AVL** y **Red-Black** resuelven ese problema mediante **auto-balanceo**: el AVL con un control estricto de altura y rotaciones, y el Red-Black con un sistema de colores que relaja ese control para lograr un mejor rendimiento en escrituras, garantizando siempre **O(log n)**.
