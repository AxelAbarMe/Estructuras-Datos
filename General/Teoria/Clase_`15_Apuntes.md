# =========================================
# SEGMENTO 13: WRAPPERS, ENCAPSULAMIENTO Y HERRAMIENTAS AVANZADAS DE PYTHON
# =========================================

## Concepto de Wrapper
- Un **wrapper** es un patrón de diseño de programación que busca **ocultar la complejidad interna** de una estructura o algoritmo, exponiendo al usuario una interfaz simple y limpia.
- Se logra mediante el uso de **métodos privados**: el método público (sin underscore) es el que el usuario llama directamente, mientras que internamente delega el trabajo pesado (usualmente recursivo) a un método privado (con underscore).
- El usuario no necesita conocer detalles internos (por ejemplo, que un recorrido se implementa con recursión y requiere un parámetro adicional como el nodo actual); solo necesita llamar al método público.

```
Usuario -> arbolito.pre_orden()      <- Interfaz pública (wrapper)
                     |
                     v
           arbolito._pre_orden(root) <- Lógica interna (privada, recursiva)
```

> Esto es justamente lo que se observa en la implementación de `arbol.py` del Segmento 12: cada recorrido (`pre_orden`, `en_orden`, `pos_orden`, `bfs`) tiene un método público que actúa como wrapper y llama a un método interno (`_pre_orden`, `_en_orden`, `_pos_orden`) que recibe el nodo raíz como parámetro.

## Métodos privados en Python
- Python **no tiene** verdaderos modificadores de acceso privados como otros lenguajes (Java, C++). La privacidad es una **convención**.
- Anteponer un **guion bajo** (`_metodo`) al nombre de un método o atributo indica que es de uso **interno**; es una señal para otros desarrolladores de "no tocar esto directamente desde fuera de la clase".
- Anteponer **doble guion bajo** (`__metodo`) activa el **name mangling**: Python renombra internamente el atributo a `_NombreClase__metodo`, dificultando (aunque no impidiendo) el acceso externo accidental.

```python
class Tree:
    def pre_orden(self):          # método público (wrapper)
        self._pre_orden(self.root)

    def _pre_orden(self, root):   # método "privado" por convención
        if root is None:
            return
        print(root.key, end=' ')
        self._pre_orden(root.left)
        self._pre_orden(root.right)
```

| Prefijo | Nombre | Comportamiento |
|---|---|---|
| Sin guion (`metodo`) | Público | Accesible libremente desde fuera de la clase. |
| Un guion (`_metodo`) | Protegido (convención) | Uso interno; accesible pero no recomendado desde fuera. |
| Doble guion (`__metodo`) | Privado (name mangling) | Python lo renombra para dificultar el acceso externo. |

### Ejemplo aplicado (BFS con wrapper)
> A partir del diagrama de pizarra: se construye una cola (`Queue`), se inserta la raíz, y mientras la cola no esté vacía se extrae un nodo, se visita (`print`), y se encolan sus hijos izquierdo y derecho.

```python
import queue

class Tree:
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

> Con el árbol serializado `CEF$H$$B$$GA$$NJ$$K$$` (donde `$` representa nodo nulo), el orden por niveles (BFS) resultante es: **C - E - G - F - B - A - N - H - J - K**.

## Property (`@property`)
- El decorador `@property` permite exponer un **método como si fuera un atributo**, sin necesidad de llamarlo con paréntesis.
- Es la forma "pythónica" de implementar **getters y setters**, manteniendo el encapsulamiento sin sacrificar una sintaxis simple.
- Se combina con `@nombre.setter` para permitir la asignación controlada (validaciones, por ejemplo).

```python
class Node:
    def __init__(self, val=None):
        self._key = val   # atributo "privado" por convención

    @property
    def key(self):
        """Getter: se accede como node.key, sin paréntesis."""
        return self._key

    @key.setter
    def key(self, valor):
        """Setter: permite validar antes de asignar."""
        if valor is None:
            raise ValueError("La llave no puede ser None")
        self._key = valor
```

```python
n = Node(5)
print(n.key)     # 5   (no n.key())
n.key = 10        # usa el setter internamente
```

> `@property` es otra forma de "wrapper": oculta la lógica interna (validaciones, cálculos) detrás de una interfaz que luce como un simple atributo.

## Dataclasses (`@dataclass`)
- El decorador `@dataclass` (módulo `dataclasses`) genera automáticamente métodos "boilerplate" como `__init__`, `__repr__` y `__eq__` a partir de las anotaciones de tipo de la clase.
- Reduce drásticamente el código repetitivo al definir clases que principalmente almacenan datos (como un `Node`).

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Node:
    key: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None

# Equivalente, sin dataclass, requeriría escribir manualmente:
# def __init__(self, key, left=None, right=None): ...
# def __repr__(self): ...
# def __eq__(self, other): ...
```

```python
n1 = Node("C")
n2 = Node("C")
print(n1)          # Node(key='C', left=None, right=None)  <- __repr__ automático
print(n1 == n2)     # True  <- __eq__ automático (compara por valores)
```

| Ventaja | Descripción |
|---|---|
| Menos código | No es necesario escribir `__init__` manualmente. |
| `__repr__` automático | Facilita depuración e impresión de objetos. |
| `__eq__` automático | Compara instancias por valor, no por identidad. |
| Tipado explícito | Obliga (o al menos sugiere) declarar el tipo de cada atributo. |

## Métodos estáticos (`@staticmethod`)
- Un **método estático** pertenece a la clase, pero **no recibe** ni `self` (instancia) ni `cls` (clase) como primer parámetro.
- Se usa para funciones que están **lógicamente relacionadas** con la clase, pero que no necesitan acceder ni modificar el estado de una instancia ni de la clase.
- Se invoca directamente desde la clase, sin necesidad de crear un objeto.

```python
class Tree:
    @staticmethod
    def es_hoja(nodo):
        """No usa self: es una función de utilidad relacionada con árboles."""
        return nodo is not None and nodo.left is None and nodo.right is None
```

```python
Tree.es_hoja(nodo_x)          # se llama desde la clase directamente
arbolito.es_hoja(nodo_x)      # también funciona desde una instancia
```

| Decorador | Primer parámetro | Acceso a `self` | Acceso a `cls` | Uso típico |
|---|---|---|---|---|
| (ninguno) | `self` | Sí | No | Métodos normales de instancia |
| `@classmethod` | `cls` | No | Sí | Constructores alternativos, lógica de la clase |
| `@staticmethod` | (ninguno) | No | No | Funciones utilitarias relacionadas con la clase |

## Módulos de utilidad de Python

### `request` (biblioteca `requests` / `urllib.request`)
- Permite realizar **peticiones HTTP** (GET, POST, PUT, DELETE) desde Python, comúnmente usado para consumir APIs externas.

```python
import requests

respuesta = requests.get("https://api.ejemplo.com/datos")
if respuesta.status_code == 200:
    datos = respuesta.json()
```

### `uuid`
- Genera **identificadores únicos universales** (Universally Unique Identifier), útiles para asignar llaves únicas a nodos, registros o entidades sin depender de un contador centralizado.

```python
import uuid

id_unico = uuid.uuid4()   # genera un UUID aleatorio (versión 4)
print(id_unico)           # ej: 3f2504e0-4f89-11d3-9a0c-0305e82c3301
```

### `time`
- Provee funciones para medir tiempo de ejecución, pausar procesos y trabajar con marcas de tiempo (timestamps).

```python
import time

inicio = time.time()
# ... proceso a medir ...
time.sleep(1)  # pausa la ejecución 1 segundo
fin = time.time()
print(f"Duración: {fin - inicio} segundos")
```

### `typing.Protocol` y `@runtime_checkable`
- `Protocol` (módulo `typing`) permite definir **tipado estructural** (similar a las *interfaces* de otros lenguajes): una clase "cumple" con un protocolo si implementa los métodos/atributos definidos, **sin necesidad de heredar explícitamente** de él.
- `@runtime_checkable` permite usar `isinstance()` para verificar en tiempo de ejecución si un objeto cumple con el protocolo.

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Recorrible(Protocol):
    def bfs(self) -> list:
        ...
    def pre_orden(self) -> None:
        ...

def procesar(estructura: Recorrible):
    """Acepta cualquier objeto que tenga bfs() y pre_orden(),
    sin importar su clase real ni herencia explícita."""
    return estructura.bfs()

print(isinstance(arbolito, Recorrible))  # True, si Tree implementa esos métodos
```

| Concepto | Descripción |
|---|---|
| Tipado estructural | "Si camina como pato y grazna como pato, es un pato" (*duck typing* formalizado). |
| Sin herencia obligatoria | La clase no necesita heredar de `Protocol` explícitamente. |
| `runtime_checkable` | Habilita `isinstance()` sobre el protocolo. |
| Uso típico | Definir contratos de interfaz para funciones que reciben distintos tipos de objetos. |

## Resumen integrador
- Los **wrappers** (métodos públicos que delegan en privados) son la base del encapsulamiento manual en Python.
- `@property` extiende esta idea permitiendo que la interfaz pública luzca como un atributo simple.
- `@dataclass` automatiza la creación de clases de datos, reduciendo el código repetitivo de constructores como el `Node` del árbol.
- `@staticmethod` agrupa funciones utilitarias dentro de una clase sin necesidad de estado.
- `uuid`, `time` y `request` son herramientas de la biblioteca estándar (o de terceros) para identificación única, medición de tiempo y comunicación HTTP, respectivamente.
- `typing.Protocol` con `@runtime_checkable` permite definir contratos flexibles de tipado estructural, útiles al diseñar funciones genéricas que operan sobre estructuras como árboles, listas o colas.
