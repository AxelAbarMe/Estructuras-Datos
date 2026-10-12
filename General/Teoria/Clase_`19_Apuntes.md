# =========================================
# SEGMENTO 17: ÁRBOLES RED-BLACK
# =========================================

## Árboles Red-Black (Rojo-Negro)

* Un **Red-Black** es un **BST auto-balanceado**: cumple siempre la propiedad de orden del BST (sub-árbol izquierdo menor, sub-árbol derecho mayor).
* Igual que el AVL, se corrige solo después de cada inserción y cada eliminación.
* En lugar de un factor de balance numérico, **cada nodo tiene un color**: **Red** (rojo) o **Black** (negro).
* En los dibujos de clase se usa **N** para negro y **R** para rojo; en este resumen se escribe `(N)` y `(R)` junto a cada llave.
* Su balance es **menos estricto** que el del AVL, por lo que hace **menos rotaciones**.

---

## Propiedades del Red-Black

| # | Propiedad | Explicación |
|---|---|---|
| 1 | Cada nodo tiene un **color** (Red / Black) | Es el dato extra que se guarda en cada nodo |
| 2 | La **raíz** siempre es **Black** | Si una corrección la pinta de rojo, se vuelve a pintar de negro |
| 3 | La **inserción** de un nodo → **Red** | Todo nodo nuevo entra en rojo |
| 4 | Los nodos **"NULL"** siempre son **Black** | Los "hijos vacíos" (hojas NULL) cuentan como nodos negros, aunque no se dibujen |
| 5 | La cantidad de nodos **Black** desde un nodo hasta los nodos más profundos es la **misma** | Se llama **altura negra** y debe ser igual por cualquier camino |
| 6 | Un nodo **Red** no puede tener hijos **Red** | No pueden existir dos rojos seguidos |

* La propiedad 6 no está escrita en el pizarrón, pero es la que obliga a corregir el árbol cuando se inserta un nodo rojo bajo un padre rojo.
* **Nota de la clase:** la altura mayor de cada nodo **no es más del doble** que la altura menor.
* Por eso la altura de un Red-Black con `n` nodos es **O(log n)**: como máximo `2 · log2(n + 1)`.

### ¿Por qué se cumple que la altura mayor no pasa del doble de la menor?

* Todos los caminos tienen la **misma cantidad de nodos negros** (propiedad 5).
* Los nodos rojos nunca están seguidos (propiedad 6), así que entre dos nodos negros hay **a lo sumo un rojo**.
* El camino **más corto** tiene solo nodos negros; el **más largo** alterna negro-rojo-negro-rojo...
* El camino más largo tiene, como máximo, el doble de nodos que el más corto.

```
              N               <- raíz (siempre negra)
            /   \
          N       R
           \       \
            R       N
           / \       \
          R   R       R       <- camino largo (alterna colores)
```

---

## Inserción en un Red-Black

### Pasos generales

1. Se inserta el nodo como en un **BST** normal (comparando llaves).
2. El nodo nuevo se pinta de **rojo**.
3. Se revisa a su **padre**:
   * Si el nuevo nodo es la **raíz** → se pinta de **negro** y termina.
   * Si el **padre es negro** → no se viola ninguna propiedad y termina.
   * Si el **padre es rojo** → hay dos rojos seguidos; se debe corregir según el **color del tío**.
4. El **tío** es el **hermano del padre** (el otro hijo del abuelo).

| Caso | Condición | Solución |
|---|---|---|
| **Caso 1** | El **hermano del padre (tío) es Rojo** | **Recolorear** |
| **Caso 2** | El **tío es Negro** (o NULL) | **Rotaciones** y luego **colorear** |

---

### Caso 1: el tío es rojo (recolorear)

* Se recolorean, en este orden:
  1. El **padre** → pasa a **negro**.
  2. El **tío** (hermano del padre) → pasa a **negro**.
  3. El **padre del padre** (abuelo) → pasa a **rojo**.
* **No se hacen rotaciones.**
* El problema puede subir: el abuelo ahora es rojo y podría tener un padre rojo. Entonces se repite la revisión con el abuelo como nodo actual, **en cascada**, hacia arriba.
* Si el abuelo es la **raíz**, se pinta de negro al final.

```
        G(N)                        G(R)
       /    \                      /    \
    P(R)    T(R)      ->        P(N)    T(N)
    /                           /
 X(R)                        X(R)
```

* `X` = nodo insertado, `P` = padre, `T` = tío, `G` = abuelo (padre del padre).
* La altura negra se mantiene: `G` era negro y ahora lo son sus dos hijos, así que todos los caminos siguen con la misma cantidad de negros.

---

### Caso 2: el tío es negro (rotaciones y colorear)

* Se aplican **rotaciones** (las mismas del AVL) y después se **colorea**.
* Se resuelve **una sola vez**: después de la rotación el árbol queda correcto y no hace falta subir.
* El tipo de rotación depende de dónde quedó el nodo nuevo respecto al abuelo `G`:

| Posición del nodo | Nombre (nomenclatura de la clase) | Rotación |
|---|---|---|
| Padre es hijo **izquierdo** y nodo es hijo **izquierdo** | **LL** | Simple a la **derecha** en el abuelo |
| Padre es hijo **derecho** y nodo es hijo **derecho** | **RR** | Simple a la **izquierda** en el abuelo |
| Padre es hijo **izquierdo** y nodo es hijo **derecho** | **RL** | Doble: **izquierda** en el padre, luego **derecha** en el abuelo |
| Padre es hijo **derecho** y nodo es hijo **izquierdo** | **LR** | Doble: **derecha** en el padre, luego **izquierda** en el abuelo |

* **Colorear después de rotar:** el nodo que queda **arriba** del sub-árbol rotado pasa a **negro** y sus **dos hijos** quedan **rojos**.
* Los nombres LL, RR, LR y RL son los mismos del Segmento 16 (AVL); la única diferencia es que aquí se agrega el paso de **colorear**.

#### Caso LL (línea a la izquierda)

```
        G(N)                     P(N)
       /    \                   /    \
    P(R)    T(N)     ->      X(R)    G(R)
    /                                    \
 X(R)                                    T(N)
```

* Rotación simple a la derecha en `G`; luego `P` queda negro y `X`, `G` rojos.

#### Caso RL (triángulo)

```
      G(N)                 G(N)                 X(N)
     /    \               /    \               /    \
  P(R)    T(N)   ->    X(R)    T(N)    ->   P(R)    G(R)
     \                 /                                \
     X(R)           P(R)                                T(N)
```

* Paso 1: rotación a la izquierda en `P`. Paso 2: rotación a la derecha en `G`. Luego `X` queda negro y `P`, `G` rojos.

---

## Ejemplo de la clase: insertar 25, 12, 32, 10, 6

**Insertar 25, 12, 32:** el 25 es raíz (negro); 12 y 32 entran en rojo bajo un padre negro. No hay violación.

```
      25(N)
     /    \
  12(R)   32(R)
```

**Insertar 10:** entra en rojo como hijo izquierdo de 12. El padre (12) es rojo y el tío (32) también es rojo → **Caso 1**.

```
      25(N)                         25(N)
     /    \                        /    \
  12(R)   32(R)        ->       12(N)   32(N)
   /                             /
10(R)                         10(R)
```

* Se recolorean padre (12) y tío (32) a negro, y el abuelo (25) a rojo. Como 25 es la raíz, vuelve a negro.

**Insertar 6:** entra en rojo como hijo izquierdo de 10. Quedan **dos rojos seguidos** (10 y 6).

```
      25(N)
     /    \
  12(N)   32(N)
   /
10(R)
 /
6(R)      <- violación: 10 y 6 son rojos
```

* El padre (10) es rojo y el tío es el hijo derecho de 12, que es **NULL (negro)** → **Caso 2**.
* Es una **línea a la izquierda (LL)** → rotación simple a la **derecha** en el abuelo (12).
* Después se colorea: el nodo que queda arriba (10) pasa a **negro**; 6 y 12 quedan **rojos**.

```
      25(N)
     /    \
  10(N)   32(N)
  /   \
6(R)  12(R)
```

* Todos los caminos desde la raíz hasta un NULL tienen **3 nodos negros** (contando el NULL).

---

## Complejidad del balanceo: AVL vs Red-Black

### AVL: costo de balancear

| Operación | Costo del balanceo |
|---|---|
| **Inserción AVL** | **O(1)**: como máximo **una rotación** (simple o doble) |
| **Borrado AVL** | **O(log n)**: puede requerir rotaciones en **cada nivel** hasta la raíz |

* En la inserción, una rotación devuelve al sub-árbol su altura original, así que el desbalance **no se propaga** hacia arriba.
* En el borrado, la rotación puede **reducir la altura** del sub-árbol, lo que desbalancea al nodo de arriba, y así sucesivamente.
* El **peor caso** para el borrado en un AVL es el **árbol de Fibonacci**: el árbol AVL más "flaco" posible para su altura.

### Árbol de Fibonacci (insertar 8, 5, 11, 3, 7, 10, 12, 2, 4, 6, 9, 1)

* Al insertarlos en ese orden no hay ninguna rotación y queda este árbol:

```
              8
            /   \
          5       11
         / \      / \
        3   7   10   12
       / \  /   /
      2  4 6   9
     /
    1
```

**Borrar 12:** el 11 queda con altura 2 a la izquierda y 0 a la derecha (FB = 2). Es un caso LL.

```
              8
            /   \
          5       11   <- nodo "x" (FB = 2)
         / \      /
        3   7   10
       / \  /   /
      2  4 6   9
     /
    1
```

**Rotación simple a la derecha en 11:** el sub-árbol baja de altura 3 a 2 y el desbalance **sube** hasta el 8 (FB = 4 - 2 = 2).

```
              8        <- nuevo "x" (FB = 2)
            /   \
          5       10
         / \      / \
        3   7    9   11
       / \  /
      2  4 6
     /
    1
```

**Rotación simple a la derecha en 8:** queda balanceado.

```
              5
            /   \
          3       8
         / \     / \
        2   4   7   10
       /       /   / \
      1       6   9   11
```

* Un solo borrado produjo **dos rotaciones en cascada**; en un árbol más alto pueden llegar a ser una por nivel → **O(log n)**.

### Red-Black: costo de balancear

| Operación | Rotaciones | Recoloreos |
|---|---|---|
| **Inserción** | Como máximo **2** (Caso 2, una sola vez) | **O(log n)** en cascada (Caso 1) |
| **Borrado** | Como máximo **3** | **O(log n)** |

* Los recoloreos son baratos (solo cambian un dato); las rotaciones son lo costoso. Por eso el Red-Black es más eficiente en **escrituras**.
* El borrado en Red-Black no se detalla aquí por su complejidad; solo se resume el concepto.

---

## Implementación en Python

```python
RED, BLACK = "R", "N"


class NodeRB:
    def __init__(self, val=None, color=RED):
        self.key = val
        self.color = color        # todo nodo nuevo se inserta en ROJO
        self.left = None
        self.right = None
        self.parent = None        # se necesita el padre para encontrar al abuelo y al tío


class RedBlack:
    def __init__(self):
        self.root = None

    # ---------- Rotaciones (mismas que en AVL, pero actualizando el padre) ----------
    def _rotar_izquierda(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotar_derecha(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    # ---------- Inserción ----------
    def insert(self, key):
        # 1) Inserción normal de BST (el nodo nuevo es ROJO)
        nuevo = NodeRB(key, RED)
        padre, cur = None, self.root
        while cur:
            padre = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return                      # llave repetida: no se duplica
        nuevo.parent = padre
        if padre is None:
            self.root = nuevo
        elif key < padre.key:
            padre.left = nuevo
        else:
            padre.right = nuevo
        # 2) Reparar las propiedades Red-Black
        self._reparar(nuevo)

    def _reparar(self, n):
        while n.parent and n.parent.color == RED:
            padre = n.parent
            abuelo = padre.parent           # existe: la raíz es negra, así que un padre rojo no es la raíz
            if padre is abuelo.left:
                tio = abuelo.right
                if tio and tio.color == RED:            # CASO 1: tío rojo -> recolorear
                    padre.color = BLACK
                    tio.color = BLACK
                    abuelo.color = RED
                    n = abuelo                          # se repite en cascada hacia arriba
                else:                                   # CASO 2: tío negro (o NULL)
                    if n is padre.right:                # triángulo (RL) -> rotación doble
                        n = padre
                        self._rotar_izquierda(n)
                        padre = n.parent
                    padre.color = BLACK                 # línea (LL) -> rotación simple + colorear
                    abuelo.color = RED
                    self._rotar_derecha(abuelo)
            else:                                       # casos simétricos (RR y LR)
                tio = abuelo.left
                if tio and tio.color == RED:
                    padre.color = BLACK
                    tio.color = BLACK
                    abuelo.color = RED
                    n = abuelo
                else:
                    if n is padre.left:
                        n = padre
                        self._rotar_derecha(n)
                        padre = n.parent
                    padre.color = BLACK
                    abuelo.color = RED
                    self._rotar_izquierda(abuelo)
        self.root.color = BLACK                         # la raíz siempre es negra

    # ---------- Búsqueda (igual que en un BST) ----------
    def search(self, key):
        cur = self.root
        while cur and cur.key != key:
            cur = cur.left if key < cur.key else cur.right
        return cur

    # ---------- Impresión ----------
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
            print(f"{r.key}({r.color})")
            self._print_tree(p + s, r.left, True)
            self._print_tree(p + s, r.right, False)
```

### Código de prueba: `main.py`

```python
import rb

arbol = rb.RedBlack()
for v in [25, 12, 32, 10, 6]:
    arbol.insert(v)
arbol.print_tree()
```

Salida esperada:

```
 '--25(N)
     |--10(N)
     |    |--6(R)
     |    '--12(R)
     '--32(N)
```

### Explicación del código

| Parte | Qué hace |
|---|---|
| `NodeRB.color` | Guarda el color del nodo; por defecto es `RED` |
| `NodeRB.parent` | Referencia al padre, necesaria para llegar al **abuelo** y al **tío** |
| `insert` | Inserta como BST y luego llama a `_reparar` |
| `while n.parent and n.parent.color == RED` | Mientras haya dos rojos seguidos, se sigue corrigiendo |
| `tio.color == RED` | **Caso 1**: recolorea padre, tío y abuelo, y sube con `n = abuelo` |
| `else` | **Caso 2**: rotaciones (doble si es triángulo, simple si es línea) y colorear |
| `self.root.color = BLACK` | Garantiza que la raíz sea siempre negra |
| `tio` es `None` | Un hijo `None` cuenta como **NULL negro** |

---

## Práctica: insertar en un Red-Black

### a) Insertar: 25, 14, 33, 6, 10, 40, 38, 35, 12, 8

| Inserción | Padre / Tío | Caso | Acción |
|---|---|---|---|
| 25 | - | Raíz | Se pinta de negro |
| 14 | Padre 25 negro | - | Sin violación |
| 33 | Padre 25 negro | - | Sin violación |
| 6 | Padre 14 rojo, tío 33 rojo | **1** | Recolorear 14 y 33 a negro; 25 rojo → raíz, vuelve a negro |
| 10 | Padre 6 rojo, tío NULL | **2 (RL)** | Izquierda en 6, derecha en 14; 10 negro, 6 y 14 rojos |
| 40 | Padre 33 negro | - | Sin violación |
| 38 | Padre 40 rojo, tío NULL | **2 (LR)** | Derecha en 40, izquierda en 33; 38 negro, 33 y 40 rojos |
| 35 | Padre 33 rojo, tío 40 rojo | **1** | Recolorear 33 y 40 a negro; 38 rojo |
| 12 | Padre 14 rojo, tío 6 rojo | **1** | Recolorear 14 y 6 a negro; 10 rojo |
| 8 | Padre 6 negro | - | Sin violación |

**Insertar 25, 14, 33:** sin violación.

```
      25(N)
     /    \
  14(R)   33(R)
```

**Insertar 6:** el padre (14) y el tío (33) son rojos → Caso 1.

```
      25(N)                        25(N)
     /    \                       /    \
  14(R)   33(R)        ->      14(N)   33(N)
   /                            /
6(R)                         6(R)
```

**Insertar 10:** queda a la derecha de 6. Padre rojo y tío NULL (negro) → Caso 2, triángulo (RL).

```
      25(N)               25(N)               25(N)
     /    \              /    \              /    \
  14(N)   33(N)       14(N)   33(N)       10(N)   33(N)
   /          ->       /          ->      /   \
6(R)                10(R)               6(R)  14(R)
   \                 /
   10(R)          6(R)
```

* Paso 1: rotación a la izquierda en 6. Paso 2: rotación a la derecha en 14. Se colorea: 10 negro; 6 y 14 rojos.

**Insertar 40:** el padre (33) es negro. Sin violación.

```
         25(N)
        /    \
     10(N)   33(N)
     /   \       \
  6(R)  14(R)    40(R)
```

**Insertar 38:** queda a la izquierda de 40. Padre rojo y tío NULL → Caso 2, triángulo (LR).

```
      25(N)                25(N)                  25(N)
     /    \               /    \                 /    \
  10(N)   33(N)        10(N)   33(N)          10(N)   38(N)
  /   \        \        /  \        \         /  \    /   \
6(R) 14(R)    40(R)  6(R) 14(R)    38(R)   6(R) 14(R) 33(R) 40(R)
              /                       \
           38(R)                      40(R)
```

* Paso 1: rotación a la derecha en 40. Paso 2: rotación a la izquierda en 33. Se colorea: 38 negro; 33 y 40 rojos.

**Insertar 35:** queda a la derecha de 33. Padre (33) rojo y tío (40) rojo → Caso 1.

```
          25(N)                              25(N)
         /    \                             /    \
      10(N)   38(N)                      10(N)   38(R)
      /  \    /   \          ->          /  \    /   \
   6(R) 14(R) 33(R) 40(R)             6(R) 14(R) 33(N) 40(N)
                 \                                  \
                 35(R)                              35(R)
```

* El abuelo (38) pasa a rojo; su padre (25) es negro, así que la cascada termina.

**Insertar 12:** queda a la izquierda de 14. Padre (14) rojo y tío (6) rojo → Caso 1.

```
          25(N)                                25(N)
         /    \                               /    \
      10(N)   38(R)                        10(R)   38(R)
      /   \    /   \           ->          /   \    /   \
   6(R)  14(R) 33(N) 40(N)              6(N)  14(N) 33(N) 40(N)
         /         \                           /          \
      12(R)        35(R)                    12(R)         35(R)
```

* El abuelo (10) pasa a rojo; su padre (25) es negro, así que termina.

**Insertar 8:** queda a la derecha de 6. El padre (6) es negro. Sin violación.

**Árbol final:**

```
              25(N)
            /       \
        10(R)        38(R)
        /   \        /   \
     6(N)  14(N)  33(N)  40(N)
       \     /       \
      8(R) 12(R)     35(R)
```

* Altura negra: 3 en todos los caminos (contando el NULL).
* Este árbol tiene **la misma forma** que el AVL del Segmento 16, inciso c); la diferencia es que aquí se guardan **colores** en lugar de factores de balance.
* Se hicieron **2 rotaciones dobles** (en 10 y 38) y **3 recoloreos en cascada** (al insertar 6, 35 y 12).

---

### b) Insertar: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

| Inserción | Padre / Tío | Caso | Acción |
|---|---|---|---|
| 1 | - | Raíz | Se pinta de negro |
| 2 | Padre 1 negro | - | Sin violación |
| 3 | Padre 2 rojo, tío NULL | **2 (RR)** | Izquierda en 1; 2 negro, 1 y 3 rojos |
| 4 | Padre 3 rojo, tío 1 rojo | **1** | Recolorear 3 y 1 a negro; 2 rojo → raíz, vuelve a negro |
| 5 | Padre 4 rojo, tío NULL | **2 (RR)** | Izquierda en 3; 4 negro, 3 y 5 rojos |
| 6 | Padre 5 rojo, tío 3 rojo | **1** | Recolorear 5 y 3 a negro; 4 rojo |
| 7 | Padre 6 rojo, tío NULL | **2 (RR)** | Izquierda en 5; 6 negro, 5 y 7 rojos |
| 8 | Padre 7 rojo, tío 5 rojo | **1**, luego **2 (RR)** | Recolorear; 6 queda rojo bajo 4 rojo → izquierda en 2 |
| 9 | Padre 8 rojo, tío NULL | **2 (RR)** | Izquierda en 7; 8 negro, 7 y 9 rojos |
| 10 | Padre 9 rojo, tío 7 rojo | **1**, luego **1** | Recolorear; 8 rojo bajo 6 rojo con tío 2 rojo → recolorear; 4 rojo → raíz, negro |

**Insertar 1, 2, 3:** el 3 forma una línea a la derecha con padre rojo y tío NULL (Caso 2, RR).

```
 1(N)                 2(N)
   \                 /    \
   2(R)     ->    1(R)    3(R)
     \
     3(R)
```

* Rotación simple a la izquierda en 1; 2 queda negro y sus hijos rojos.

**Insertar 4:** padre (3) y tío (1) rojos → Caso 1.

```
      2(N)                       2(N)
     /    \                     /    \
  1(R)    3(R)       ->      1(N)    3(N)
            \                          \
            4(R)                       4(R)
```

**Insertar 5:** línea a la derecha, tío NULL → Caso 2 (RR), rotación a la izquierda en 3.

```
      2(N)                       2(N)
     /    \                     /    \
  1(N)    3(N)       ->      1(N)    4(N)
            \                       /    \
            4(R)                 3(R)    5(R)
              \
              5(R)
```

**Insertar 6:** padre (5) y tío (3) rojos → Caso 1.

```
      2(N)                           2(N)
     /    \                         /    \
  1(N)    4(N)           ->      1(N)    4(R)
         /    \                         /    \
      3(R)    5(R)                   3(N)    5(N)
                \                                \
                6(R)                             6(R)
```

**Insertar 7:** línea a la derecha, tío NULL → Caso 2 (RR), rotación a la izquierda en 5.

```
      2(N)
     /    \
  1(N)    4(R)
         /    \
      3(N)    6(N)
             /    \
          5(R)    7(R)
```

**Insertar 8:** padre (7) y tío (5) rojos → Caso 1; el 6 queda rojo bajo el 4 rojo, y el tío del 6 (el 1) es negro → Caso 2.

```
      2(N)                        2(N)
     /    \                      /    \
  1(N)    4(R)               1(N)    4(R)
         /    \       ->            /    \
      3(N)    6(N)               3(N)    6(R)    <- 6 y 4 son rojos seguidos
             /    \                     /    \
          5(R)    7(R)               5(N)    7(N)
                    \                          \
                    8(R)                       8(R)
```

* Línea a la derecha (RR) con abuelo 2 → rotación simple a la **izquierda en 2**; el 4 queda negro y el 2 rojo.

```
              4(N)
            /      \
        2(R)        6(R)
        /   \       /   \
     1(N)  3(N)  5(N)   7(N)
                           \
                           8(R)
```

**Insertar 9:** línea a la derecha, tío NULL → Caso 2 (RR), rotación a la izquierda en 7.

```
              4(N)
            /      \
        2(R)        6(R)
        /   \       /   \
     1(N)  3(N)  5(N)   8(N)
                        /   \
                     7(R)   9(R)
```

**Insertar 10:** padre (9) y tío (7) rojos → Caso 1; el 8 queda rojo bajo el 6 rojo, y el tío del 8 (el 2) es rojo → Caso 1 otra vez; el 4 pasa a rojo y, al ser la raíz, vuelve a negro.

```
              4(N)
            /      \
        2(N)        6(N)
        /   \       /   \
     1(N)  3(N)  5(N)   8(R)
                        /   \
                     7(N)   9(N)
                               \
                               10(R)
```

**Árbol final:**

```
              4(N)
            /      \
        2(N)        6(N)
        /   \       /   \
     1(N)  3(N)  5(N)   8(R)
                        /   \
                     7(N)   9(N)
                               \
                               10(R)
```

* Altura negra: 4 en todos los caminos (contando el NULL).
* Se hicieron **5 rotaciones simples** y varios recoloreos.
* La raíz es **4**, igual que en el AVL, pero la forma es distinta: el Red-Black tiene altura 4 y el AVL altura 3, porque el Red-Black balancea de forma menos estricta.

---

## Comparación AVL vs Red-Black

| Característica | AVL | Red-Black |
|---|---|---|
| Dato extra por nodo | Altura / factor de balance | **Color** (rojo o negro) |
| Criterio de balance | **Estricto**: FB de -1, 0 o 1 | **Relajado**: la altura mayor no pasa del doble de la menor |
| Altura máxima | Aproximadamente `1,44 · log2(n)` | Aproximadamente `2 · log2(n)` |
| Búsqueda | O(log n), un poco más rápida | O(log n) |
| Inserción (rotaciones) | Máx. **1** (simple o doble) | Máx. **2** |
| Borrado (rotaciones) | Hasta **O(log n)** (peor caso: árbol de Fibonacci) | Máx. **3** |
| Recoloreos | No aplica | O(log n), en cascada |
| Uso típico | Muchas **búsquedas**, pocas escrituras | Muchas **escrituras**; `TreeMap` en Java, `map` y `set` en C++ |

---

## Resumen general del tema

* Un **Red-Black** es un BST **auto-balanceado** donde cada nodo tiene un **color** (rojo o negro) en lugar de un factor de balance.
* Propiedades: la **raíz es negra**, todo nodo nuevo entra en **rojo**, los nodos **NULL son negros**, no hay **dos rojos seguidos** y todos los caminos tienen la **misma cantidad de nodos negros**.
* La altura mayor de cada nodo no es más del **doble** de la menor, por lo que la altura es **O(log n)**.
* Al insertar, si el padre es rojo se revisa el **tío** (hermano del padre):
  * **Caso 1 (tío rojo):** se **recolorean** padre, tío y abuelo, y se repite hacia arriba en **cascada**.
  * **Caso 2 (tío negro):** se aplican **rotaciones** (simple en línea, doble en triángulo) y luego se **colorea**: el nodo de arriba negro y sus hijos rojos.
* Las rotaciones son las mismas del AVL (LL, RR, LR y RL), con el paso extra de colorear.
* En el **AVL**, el balanceo de una inserción es **O(1)** y el de un borrado es **O(log n)**; el peor caso del borrado es el **árbol de Fibonacci**, donde un borrado desbalancea en cascada hasta la raíz.
* El **Red-Black** hace menos rotaciones (máx. 2 en inserción y 3 en borrado), por eso es más eficiente en escrituras, a cambio de un árbol algo más alto.
* En la práctica: el inciso **a)** (25, 14, 33, 6, 10, 40, 38, 35, 12, 8) requirió 2 rotaciones dobles y 3 recoloreos en cascada, y quedó con la misma forma que el AVL; el inciso **b)** (1 a 10) requirió 5 rotaciones simples y quedó con raíz **4** y altura 4.
