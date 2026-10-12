# =========================================
# SEGMENTO 18: VIRTUAL RED-BLACK / AVL
# =========================================

## Objetivo de la actividad

* **Repasar** los árboles **AVL** y **Red-Black** insertando las mismas secuencias en ambos y **comparando** cuántas rotaciones y recoloreos requiere cada uno.
* Se trabaja con tres herramientas:
  * El **visualizador** de la Universidad de San Francisco (`cs.usfca.edu/~galles/visualization/Algorithms.html`).
  * El **código del repositorio** `estructuras-de-datos` (carpetas `week11` para AVL y `week12` para Red-Black).
  * El script **`operations.py`**, que cuenta las rotaciones automáticamente.

### Pasos de la actividad

| Paso | Qué se hace |
|---|---|
| **a)** | Se reciben **tres secuencias** de llaves; **cada secuencia es un árbol aparte** |
| **b)** | Para cada secuencia se construyen el AVL y el Red-Black en el visualizador, llevando en una **tabla** la cantidad de rotaciones y recoloreos |
| **c)** | Se hacen las mismas inserciones con el código de `week11` y `week12` y se verifica que el **resultado sea igual** al del visualizador |
| **d)** | Se corre `operations.py` y se **comparan** sus resultados con los del paso b) |
| **Nota** | **Se debe arreglar cualquier error** que se encuentre en el código |

---

## Secuencias de llaves

| Árbol | Tipo | Cantidad | Secuencia |
|---|---|---|---|
| **1** | Enteros | 24 | `6, 83, 17, 88, 92, 15, 27, 54, 86, 42, 34, 99, 68, 45, 91, 71, 53, 51, 48, 85, 31, 57, 43, 22` |
| **2** | Palabras | 24 | `apple, river, candle, umbrella, walnut, bridge, eagle, nectar, tiger, harbor, guitar, zebra, pepper, jungle, violet, quartz, mango, lemon, kettle, saddle, forest, orbit, island, dolphin` |
| **3** | Palabras | 30 | `moss, cloud, coral, delta, sage, daisy, cedar, pine, garden, bamboo, hazel, fern, willow, lemon, maple, river, forest, jasmine, cherry, olive, elm, rose, anchor, lake, peach, birch, apple, basil, oak, iris` |

* Las llaves de texto se comparan en **orden alfabético**.
* Las secuencias 1 y 2 tienen el **mismo orden relativo**: la llave número *k* en orden de tamaño (6 ↔ `apple`, 15 ↔ `bridge`, 17 ↔ `candle`...) se inserta en la misma posición. Por eso producen **árboles con la misma forma** y los mismos conteos.

---

## Qué se cuenta en la tabla

| Estructura | Qué se cuenta | Cómo se cuenta |
|---|---|---|
| **AVL** | **Rotaciones** | Una rotación simple cuenta **1**; una rotación doble cuenta **2** (dos rotaciones simples) |
| **Red-Black** | **Rotaciones** | Igual que en AVL: Caso 2 con línea = 1, Caso 2 con triángulo = 2 |
| **Red-Black** | **Recoloreos** | Cada vez que un nodo **cambia de color** (Caso 1, colorear después de rotar, y pintar la raíz de negro) |

* El color inicial de un nodo nuevo (rojo) **no** cuenta como recoloreo.
* Los recoloreos pueden variar un poco según la convención del visualizador; las **rotaciones** y la **forma final del árbol** sí deben coincidir.

### Uso del visualizador

1. Abrir `Algorithms.html` y elegir **AVL Tree** (o **Red-Black Tree**) en la lista.
2. Escribir la llave en el cuadro de texto y presionar **Insert**.
3. Usar **Animation Speed** / **Skip Forward** para ver cada paso: el visualizador muestra cada rotación y cada recoloreo.
4. Anotar en la tabla cuántos pasos de rotación y de recoloreo hubo por cada inserción.
5. Repetir con cada secuencia en un árbol nuevo (**Clear** entre secuencias).

---

## El código del repositorio

### `avl_tree.py` (semana 11)

| Parte | Qué hace |
|---|---|
| `_build_ascii_tree` / `pretty_print` | Dibuja el árbol en texto, con ramas alineadas y soporte para llaves de varios dígitos |
| `AVLNode` | Nodo con `key`, `left`, `right` y `height` (altura contada en nodos, inicia en 1) |
| `_height`, `_update`, `_balance` | Altura de un nodo (0 si es `None`), actualización de su altura y factor de balance |
| `rotate_left` / `rotate_right` | Rotaciones simples; actualizan alturas y devuelven la nueva raíz del sub-árbol |
| `insert` / `_insert` | Inserta como BST y balancea con los 4 casos (LL, RR, LR, RL) al regresar de la recursión |
| `delete` / `_delete` | Borra (con sucesor en-orden si hay dos hijos) y balancea usando el balance del hijo |
| `search` | Búsqueda iterativa como en un BST |

### `red_black_tree.py` (semana 12)

| Parte | Qué hace |
|---|---|
| `RBNode` | Nodo con `key`, `color` (`"R"` o `"B"`), `left`, `right` y `parent` |
| `self.NIL` | **Nodo centinela negro** que representa todos los hijos vacíos (los nodos NULL siempre son negros) |
| `rotate_left` / `rotate_right` | Rotaciones simples que también actualizan el `parent` |
| `insert` | Inserción de BST con nodo **rojo** y luego llama a `_insert_fixup` |
| `_insert_fixup` | Repara las propiedades: **Caso 1** (tío rojo) recolorea y sube; **Caso 2** (tío negro) rota y colorea |
| `self.root.color = "B"` | Al final, la raíz siempre queda negra |
| `pretty_print` | Muestra cada nodo como `llave(color)`; el NIL se imprime vacío |

* En `_insert_fixup`, `z.parent` es el **padre**, `z.parent.parent` el **abuelo** y `y` el **tío**.
* `if y and y.color == "R"` es el **Caso 1** (recolorear); el `else` es el **Caso 2** (si `z` es un triángulo se hace rotación doble, si es línea basta una rotación simple).

---

## Errores encontrados en el código y sus correcciones

| # | Archivo | Error | Gravedad |
|---|---|---|---|
| 1 | `red_black_tree.py` | `RBNode` **no se puede crear con `color`, `left`, `right` ni `parent`** | **Crítico**: `RBTree()` falla de inmediato |
| 2 | `avl_tree.py` | Las **llaves repetidas** se mandan a la derecha y **rompen el balance** | Alto |
| 3 | Ambos (impresor) | `root_x = lw + 1 + (sw // 2)` está **desfasado una posición** en el caso de "solo hijo izquierdo" | Medio (el dibujo sale desalineado) |
| 4 | Ambos | `key: any` usa la función `any` como tipo; y `@dataclass` genera `__eq__`/`__repr__` recursivos | Bajo |
| 5 | `operations.py` | El texto de uso dice `comparar_repo.py` pero el archivo es `operations.py`; **no cuenta recoloreos**; depende de un módulo `trees` que puede no existir | Medio |

### Error 1: `RBNode` (el más importante)

* Con `@dataclass`, **solo las variables con anotación de tipo** son campos del constructor.
* En el código, `color = "R"`, `left = None`, etc. **no tienen anotación**, así que son simples atributos de clase y el constructor solo acepta `key`.
* Al ejecutar `RBTree()`, la línea `RBNode(key=None, color="B")` produce:

```
TypeError: RBNode.__init__() got an unexpected keyword argument 'color'
```

**Corrección:**

```python
from dataclasses import dataclass
from typing import Any, Optional

@dataclass(eq=False, repr=False)
class RBNode:
    key: Any
    color: str = "R"
    left: Optional["RBNode"] = None
    right: Optional["RBNode"] = None
    parent: Optional["RBNode"] = None
```

* Ahora `color`, `left`, `right` y `parent` son **campos con valor por defecto**.
* `eq=False` y `repr=False` evitan comparaciones o impresiones recursivas: como cada hijo apunta a su `parent` y el padre apunta al hijo, un `==` o un `print(nodo)` entraría en un ciclo infinito.
* En `AVLNode` el código funcionaba porque solo se crea con `AVLNode(key)`, pero se corrige igual:

```python
@dataclass(eq=False, repr=False)
class AVLNode:
    key: Any
    left: Optional["AVLNode"] = None
    right: Optional["AVLNode"] = None
    height: int = 1
```

### Error 2: llaves repetidas en el AVL

* Con `else: node.right = ...`, una llave igual a la del nodo se manda a la derecha.
* Las condiciones de rotación comparan la llave con la del hijo (`key > node.right.key`); si son **iguales**, ninguna condición se cumple y el árbol queda **desbalanceado**.
* Prueba: insertar `10, 20, 20, 20, 20, 20` deja una cadena de 6 nodos hacia la derecha.

**Corrección** (igual que en el Segmento 16: no se duplica la llave):

```python
def _insert(self, node, key):
    if not node:
        return AVLNode(key)
    if key < node.key:
        node.left = self._insert(node.left, key)
    elif key > node.key:
        node.right = self._insert(node.right, key)
    else:
        return node                     # llave repetida: no se duplica
    _update(node)
    bf = _balance(node)
    # ... (los 4 casos de rotación quedan igual)
```

### Error 3: impresor desalineado

* En el caso de "solo hijo izquierdo", la etiqueta del nodo empieza en la columna `lw`, pero se devolvía `root_x = lw + 1 + (sw // 2)`: el padre dibuja su `/` **una columna a la derecha** de donde está realmente el nodo.
* Ejemplo con `50, 30, 70, 20, 40, 60, 80, 10` (el 20 tiene solo hijo izquierdo):

```
      __50___
     /       \
     30_     70_
    /   \   /   \
  20  40  60  80       <- el "/" de 30 queda desfasado respecto al 20
 /
10
```

**Corrección** (en ambos archivos):

```python
root_x = lw + (sw // 2)      # antes: lw + 1 + (sw // 2)
```

Resultado con la corrección:

```
      __50___
     /       \
    30_     70_
    /   \   /   \
  20  40  60  80
 /
10
```

* También se pueden borrar las variables sin uso `pad = [""] * lh` y `gap = 2`.

---

## `operations.py` corregido

* **Uso** (desde la raíz del repositorio `estructuras-de-datos`):

```
python operations.py          # secuencia de enteros
python operations.py str      # primera secuencia de palabras
python operations.py str2     # segunda secuencia de palabras
```

```python
"""Cuenta las rotaciones (AVL y Rojo-Negro) y los recoloreos (Rojo-Negro) del codigo
de las semanas 11 (AVL) y 12 (Rojo-Negro).

Uso (desde la raiz del repositorio estructuras-de-datos):
    python operations.py          # secuencia de enteros
    python operations.py str      # secuencia de palabras
    python operations.py str2     # segunda secuencia de palabras
No modifica avl_tree.py ni red_black_tree.py: envuelve sus metodos de rotacion
y reemplaza el atributo `color` de RBNode por una propiedad que cuenta los cambios.
"""
import sys
sys.path[:0] = ["week11", "week12"]
import avl_tree, red_black_tree

try:
    from trees import INSERT_INT, DELETE_INT, INSERT_STR, DELETE_STR
except ImportError:        # secuencias de la actividad, por si no existe trees.py
    INSERT_INT = [6, 83, 17, 88, 92, 15, 27, 54, 86, 42, 34, 99, 68, 45, 91, 71, 53, 51, 48, 85, 31, 57, 43, 22]
    DELETE_INT = [17, 54, 6]
    INSERT_STR = ("apple river candle umbrella walnut bridge eagle nectar tiger harbor guitar zebra "
                  "pepper jungle violet quartz mango lemon kettle saddle forest orbit island dolphin").split()
    DELETE_STR = ["candle", "nectar", "apple"]

INSERT_STR2 = ("moss cloud coral delta sage daisy cedar pine garden bamboo hazel fern willow lemon maple "
               "river forest jasmine cherry olive elm rose anchor lake peach birch apple basil oak iris").split()
DELETE_STR2 = ["coral", "pine", "moss"]


def con_contador(cls):
    """Cuenta cada llamada a rotate_left / rotate_right (una doble rotacion cuenta 2)."""
    cls.rotaciones = 0
    for nombre in ("rotate_left", "rotate_right"):
        original = getattr(cls, nombre)
        def envoltura(self, *args, _f=original):
            self.rotaciones += 1
            return _f(self, *args)
        setattr(cls, nombre, envoltura)


def con_contador_colores(node_cls):
    """Cuenta cada vez que un nodo CAMBIA de color (el color inicial no cuenta)."""
    node_cls.recoloreos = 0
    def get(self):
        return self._color
    def set_(self, valor):
        if hasattr(self, "_color") and self._color != valor:
            node_cls.recoloreos += 1
        self._color = valor
    node_cls.color = property(get, set_)


con_contador(avl_tree.AVLTree)
con_contador(red_black_tree.RBTree)
con_contador_colores(red_black_tree.RBNode)

arg = sys.argv[1] if len(sys.argv) > 1 else "int"
ins, dels = {"str": (INSERT_STR, DELETE_STR),
             "str2": (INSERT_STR2, DELETE_STR2)}.get(arg, (INSERT_INT, DELETE_INT))
avl, rb = avl_tree.AVLTree(), red_black_tree.RBTree()
avl.rotaciones = rb.rotaciones = 0

print(f"{'op':<4}{'clave':<10}{'AVL rot':>8}{'RB rot':>8}{'RB color':>9}")
for k in ins:
    a0, r0, c0 = avl.rotaciones, rb.rotaciones, red_black_tree.RBNode.recoloreos
    avl.insert(k); rb.insert(k)
    print(f"{'ins':<4}{str(k):<10}{avl.rotaciones - a0:>8}{rb.rotaciones - r0:>8}"
          f"{red_black_tree.RBNode.recoloreos - c0:>9}")
ins_avl, ins_rb, ins_col = avl.rotaciones, rb.rotaciones, red_black_tree.RBNode.recoloreos
print("\nAVL despues de insertar:"); avl.pretty_print()
print("\nRojo-Negro despues de insertar:"); rb.pretty_print()

for k in dels:
    a0 = avl.rotaciones
    avl.delete(k)
    print(f"{'del':<4}{str(k):<10}{avl.rotaciones - a0:>8}{'-':>8}{'-':>9}")
print("\nAVL despues de eliminar:"); avl.pretty_print()
print(f"\nInserciones: AVL={ins_avl} rotaciones | RB={ins_rb} rotaciones y {ins_col} recoloreos")
print(f"Eliminaciones: AVL={avl.rotaciones - ins_avl} rotaciones (RB: la semana 12 no implementa delete)")
```

### Cambios respecto al original

| Cambio | Motivo |
|---|---|
| Docstring con el nombre correcto (`operations.py`) | El original mencionaba `comparar_repo.py` |
| Contador de **recoloreos** con una propiedad en `RBNode.color` | La actividad pide contar rotaciones **y recoloreos**, y el original solo contaba rotaciones |
| `try / except ImportError` para `trees` | Si no existe el módulo `trees`, usa las secuencias de la actividad |
| Argumento `str2` | Permite correr la tercera secuencia |
| Columnas `AVL rot`, `RB rot`, `RB color` | Muestran los tres conteos por inserción |
| Las listas `DELETE_*` de respaldo son solo **ejemplos** | Si existe `trees.py`, se usan sus listas de borrado |

* El script **no modifica** `avl_tree.py` ni `red_black_tree.py` (solo envuelve sus métodos); pero con el `RBNode` original `RBTree()` falla, así que **la corrección del Error 1 es necesaria** antes de ejecutarlo.
* Una **doble rotación cuenta 2** porque `rotate_left` / `rotate_right` se llaman dos veces.
* El borrado en AVL cuenta rotaciones; el Red-Black de la semana 12 **no implementa `delete`**.

---

## Resultados: tablas de conteo

### Resumen por secuencia

| Secuencia | Llaves | AVL rotaciones | RB rotaciones | RB recoloreos | Altura AVL (niveles) | Altura RB (niveles) | Altura negra RB |
|---|---|---|---|---|---|---|---|
| **1 (enteros)** | 24 | **22** | **12** | 40 | 6 | 5 | 4 |
| **2 (palabras)** | 24 | **22** | **12** | 40 | 6 | 5 | 4 |
| **3 (palabras)** | 30 | **27** | **10** | 53 | 6 | 6 | 4 |

* La **altura negra** cuenta el nodo NULL final, como en las propiedades del Segmento 17.

### Desglose por tipo de caso

| Secuencia | AVL: rot. simples | AVL: rot. dobles | RB: Caso 1 (recolorear) | RB: Caso 2 línea (1 rot.) | RB: Caso 2 triángulo (2 rot.) |
|---|---|---|---|---|---|
| **1 y 2** | 4 | 9 | 7 | 4 | 4 |
| **3** | 5 | 11 | 12 | 4 | 3 |

* Comprobación para la secuencia 1: AVL = `4 · 1 + 9 · 2 = 22`; RB = `4 · 1 + 4 · 2 = 12`.
* Comprobación para la secuencia 3: AVL = `5 · 1 + 11 · 2 = 27`; RB = `4 · 1 + 3 · 2 = 10`.

### Tabla por inserción: secuencias 1 y 2

| # | Llave (entero / palabra) | AVL rot | RB rot | RB recoloreos |
|---|---|---|---|---|
| 1 | 6 / apple | 0 | 0 | 1 |
| 2 | 83 / river | 0 | 0 | 0 |
| 3 | 17 / candle | 2 | 2 | 2 |
| 4 | 88 / umbrella | 0 | 0 | 4 |
| 5 | 92 / walnut | 1 | 1 | 2 |
| 6 | 15 / bridge | 0 | 0 | 0 |
| 7 | 27 / eagle | 0 | 0 | 3 |
| 8 | 54 / nectar | 2 | 2 | 2 |
| 9 | 86 / tiger | 2 | 2 | 5 |
| 10 | 42 / harbor | 2 | 0 | 0 |
| 11 | 34 / guitar | 2 | 2 | 2 |
| 12 | 99 / zebra | 1 | 0 | 0 |
| 13 | 68 / pepper | 0 | 0 | 0 |
| 14 | 45 / jungle | 0 | 0 | 7 |
| 15 | 91 / violet | 0 | 0 | 0 |
| 16 | 71 / quartz | 2 | 0 | 3 |
| 17 | 53 / mango | 2 | 1 | 2 |
| 18 | 51 / lemon | 1 | 1 | 5 |
| 19 | 48 / kettle | 2 | 1 | 2 |
| 20 | 85 / saddle | 1 | 0 | 0 |
| 21 | 31 / forest | 2 | 0 | 0 |
| 22 | 57 / orbit | 0 | 0 | 0 |
| 23 | 43 / island | 0 | 0 | 0 |
| 24 | 22 / dolphin | 0 | 0 | 0 |
| **Total** | | **22** | **12** | **40** |

### Tabla por inserción: secuencia 3

| # | Llave | AVL rot | RB rot | RB recoloreos |
|---|---|---|---|---|
| 1 | moss | 0 | 0 | 1 |
| 2 | cloud | 0 | 0 | 0 |
| 3 | coral | 2 | 2 | 2 |
| 4 | delta | 0 | 0 | 4 |
| 5 | sage | 0 | 0 | 0 |
| 6 | daisy | 2 | 0 | 3 |
| 7 | cedar | 0 | 0 | 0 |
| 8 | pine | 2 | 0 | 0 |
| 9 | garden | 0 | 0 | 0 |
| 10 | bamboo | 1 | 1 | 2 |
| 11 | hazel | 2 | 2 | 5 |
| 12 | fern | 1 | 0 | 0 |
| 13 | willow | 0 | 0 | 0 |
| 14 | lemon | 0 | 0 | 7 |
| 15 | maple | 2 | 1 | 2 |
| 16 | river | 0 | 0 | 3 |
| 17 | forest | 2 | 0 | 0 |
| 18 | jasmine | 2 | 0 | 6 |
| 19 | cherry | 2 | 0 | 3 |
| 20 | olive | 0 | 0 | 0 |
| 21 | elm | 2 | 0 | 0 |
| 22 | rose | 1 | 0 | 3 |
| 23 | anchor | 0 | 0 | 0 |
| 24 | lake | 2 | 1 | 2 |
| 25 | peach | 1 | 0 | 0 |
| 26 | birch | 0 | 0 | 0 |
| 27 | apple | 1 | 1 | 5 |
| 28 | basil | 2 | 0 | 0 |
| 29 | oak | 0 | 0 | 0 |
| 30 | iris | 0 | 2 | 5 |
| **Total** | | **27** | **10** | **53** |

* Se observa que **la misma inserción puede costar distinto en cada árbol**: por ejemplo `iris` no requiere rotaciones en el AVL pero sí una doble en el Red-Black, y `42 / harbor` ocurre al revés.

---

## Árboles finales (recorrido por niveles)

### Secuencia 1 (enteros)

```
AVL: 68, 42, 88, 17, 53, 83, 92, 6, 31, 48, 54, 71, 86, 91, 99, 15, 27, 34, 45, 51, 57, 85, 22, 43

RB : 54(N), 34(N), 88(N), 17(R), 45(R), 83(R), 92(N), 6(N), 27(N), 42(N), 51(N), 68(N), 86(N),
     91(R), 99(R), 15(R), 22(R), 31(R), 43(R), 48(R), 53(R), 57(R), 71(R), 85(R)
```

**AVL**

```
               ______________68_________
              /                         \
     ________42_________           ____88___
    /                   \         /         \
 __17_____           __53_       83___     92_
/         \         /     \     /     \   /   \
6_       31_       48_   54_   71    86  91  99
  \     /   \     /   \     \       /
 15    27  34    45  51    57      85
      /         /
     22        43
```

**Red-Black** (`B` = negro, `R` = rojo en la salida del programa)

```
                                ________________________________54(B)________________________________
                               /                                                                     \
            _________________34(B)____________                                         ____________88(B)_______
           /                                  \                                       /                        \
   ______17(R)_______                _______45(R)_______                     _______83(R)_______           __92(B)__
  /                  \              /                   \                   /                   \         /         \
6(B)__           __27(B)__        42(B)__           __51(B)__           __68(B)__           __86(B)     91(R)     99(R)
      \         /         \              \         /         \         /         \         /
    15(R)     22(R)     31(R)          43(R)     48(R)     53(R)     57(R)     71(R)     85(R)
```

### Secuencia 2 (palabras, misma forma que la secuencia 1)

```
AVL: pepper, harbor, umbrella, candle, mango, river, walnut, apple, forest, kettle, nectar, quartz,
     tiger, violet, zebra, bridge, eagle, guitar, jungle, lemon, orbit, saddle, dolphin, island

RB : nectar(N), guitar(N), umbrella(N), candle(R), jungle(R), river(R), walnut(N), apple(N), eagle(N),
     harbor(N), lemon(N), pepper(N), tiger(N), violet(R), zebra(R), bridge(R), dolphin(R), forest(R),
     island(R), kettle(R), mango(R), orbit(R), quartz(R), saddle(R)
```

### Secuencia 3 (palabras)

```
AVL: hazel, delta, pine, cedar, forest, maple, sage, bamboo, cloud, fern, garden, lake, olive, river,
     willow, anchor, birch, cherry, coral, elm, jasmine, lemon, moss, peach, rose, apple, basil, daisy,
     iris, oak

RB : delta(N), cedar(N), moss(R), bamboo(R), coral(R), jasmine(N), sage(N), anchor(N), birch(N),
     cloud(N), daisy(N), garden(R), lemon(R), pine(R), willow(N), apple(R), basil(R), cherry(R),
     fern(N), hazel(N), lake(N), maple(N), olive(N), river(N), elm(R), forest(R), iris(R), oak(R),
     peach(R), rose(R)
```

## Secuencia 2: AVL

```
 '--pepper
     |--harbor
     |    |--candle
     |    |    |--apple
     |    |    |    '--bridge
     |    |    '--forest
     |    |        |--eagle
     |    |        |    |--dolphin
     |    |        '--guitar
     |    '--mango
     |        |--kettle
     |        |    |--jungle
     |        |    |    |--island
     |        |    '--lemon
     |        '--nectar
     |            '--orbit
     '--umbrella
         |--river
         |    |--quartz
         |    '--tiger
         |        |--saddle
         '--walnut
             |--violet
             '--zebra
```

## Secuencia 2: Red-Black

```
 '--nectar(N)
     |--guitar(N)
     |    |--candle(R)
     |    |    |--apple(N)
     |    |    |    '--bridge(R)
     |    |    '--eagle(N)
     |    |        |--dolphin(R)
     |    |        '--forest(R)
     |    '--jungle(R)
     |        |--harbor(N)
     |        |    '--island(R)
     |        '--lemon(N)
     |            |--kettle(R)
     |            '--mango(R)
     '--umbrella(N)
         |--river(R)
         |    |--pepper(N)
         |    |    |--orbit(R)
         |    |    '--quartz(R)
         |    '--tiger(N)
         |        |--saddle(R)
         '--walnut(N)
             |--violet(R)
             '--zebra(R)
```

## Secuencia 3: AVL

```
 '--hazel
     |--delta
     |    |--cedar
     |    |    |--bamboo
     |    |    |    |--anchor
     |    |    |    |    '--apple
     |    |    |    '--birch
     |    |    |        |--basil
     |    |    '--cloud
     |    |        |--cherry
     |    |        '--coral
     |    |            '--daisy
     |    '--forest
     |        |--fern
     |        |    |--elm
     |        '--garden
     '--pine
         |--maple
         |    |--lake
         |    |    |--jasmine
         |    |    |    |--iris
         |    |    '--lemon
         |    '--olive
         |        |--moss
         |        |    '--oak
         |        '--peach
         '--sage
             |--river
             |    '--rose
             '--willow
```

## Secuencia 3: Red-Black

```
 '--delta(N)
     |--cedar(N)
     |    |--bamboo(R)
     |    |    |--anchor(N)
     |    |    |    '--apple(R)
     |    |    '--birch(N)
     |    |        |--basil(R)
     |    '--coral(R)
     |        |--cloud(N)
     |        |    |--cherry(R)
     |        '--daisy(N)
     '--moss(R)
         |--jasmine(N)
         |    |--garden(R)
         |    |    |--fern(N)
         |    |    |    |--elm(R)
         |    |    |    '--forest(R)
         |    |    '--hazel(N)
         |    |        '--iris(R)
         |    '--lemon(R)
         |        |--lake(N)
         |        '--maple(N)
         '--sage(N)
             |--pine(R)
             |    |--olive(N)
             |    |    |--oak(R)
             |    |    '--peach(R)
             |    '--river(N)
             |        '--rose(R)
             '--willow(N)
```

* `|--` es hijo **izquierdo** y `'--` es hijo **derecho**; `(N)` = negro y `(R)` = rojo.

---

## Verificaciones realizadas con el código corregido

| Verificación | Resultado |
|---|---|
| AVL: factor de balance de **todos** los nodos entre -1 y 1, alturas bien actualizadas y recorrido en-orden ordenado (3 secuencias) | Correcto |
| AVL: 300 árboles aleatorios de 60 llaves, borrando 40 de ellas, revisando el balance tras cada borrado | Correcto |
| AVL: llaves repetidas (`10, 20, 20, 20, 20, 20`) | Correcto tras la corrección |
| Red-Black: raíz negra, ningún nodo rojo con hijo rojo, misma altura negra por todos los caminos (3 secuencias) | Correcto (altura negra = 4) |
| Impresor: árbol con nodos de un solo hijo izquierdo | Alineado tras la corrección |

---

## Comparación de resultados y conclusiones

| Aspecto | AVL | Red-Black |
|---|---|---|
| **Rotaciones** (secuencias 1/2/3) | 22 / 22 / 27 | **12 / 12 / 10** |
| **Recoloreos** | No aplica | 40 / 40 / 53 |
| **Altura** (niveles, secuencias 1/2/3) | **6 / 6 / 6** | 5 / 5 / 6 |
| **Criterio de balance** | Estricto (FB de -1, 0 o 1) | Relajado (colores y altura negra) |

* El **Red-Black hizo bastante menos rotaciones** que el AVL (alrededor de la mitad en las secuencias 1 y 2, y un tercio en la 3), porque en el **Caso 1** corrige el árbol **solo con recoloreos**, sin rotar.
* Esos recoloreos son baratos (solo cambian un dato del nodo), por eso el Red-Black es más eficiente en **escrituras**.
* El **AVL** es más estricto, por lo que el árbol queda **más bajo o igual** (en la secuencia 1, 6 niveles contra 5 del Red-Black no es una ventaja: el Red-Black quedó incluso más bajo por la forma en que se insertaron las llaves); la garantía del AVL es un **peor caso** de altura menor, lo que favorece las **búsquedas**.
* Ambos mantienen altura **O(log n)** y operaciones de búsqueda, inserción y borrado en **O(log n)**.
* Con el visualizador deben coincidir las **rotaciones** y la **forma final** de cada árbol; si no coinciden, hay que revisar el orden de inserción o un error de transcripción de las llaves.
