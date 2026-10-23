# =========================================
# SEGMENTO 21: GRAFOS
# =========================================

# Grafos

Son compuestos por nodos y aristas, las cuales son pares de elementos

G = {V,E}

E = (a,b)

| Símbolo | Qué es | Ejemplo |
|---|---|---|
| **G** | El grafo completo | `G = {V, E}` |
| **V** | Conjunto de **vértices** o nodos (las `llaves` o `keys`) | `V = {A, B, C}` |
| **E** | Conjunto de **aristas**, cada una es un par de vértices | `E = {(A,B), (B,C)}` |
| **(a,b)** | Arista que conecta el vértice `a` con el vértice `b` | `(A,B)` |

## Tipos de grafos

### Según la dirección de las aristas

Grafo sin orden o no dirigidos:

```
A
|
| Adyacencia
|
|___B
```

Grafos ordenados o dirigidos: 

```
A
|
| Adyacencia
|
|-->B

(A,B) -> Arista, no existe adyacencia (B,A)
```

| Aspecto | No dirigido | Dirigido |
|---|---|---|
| **Arista** | `(A,B)` es lo mismo que `(B,A)` | `(A,B)` **no** es lo mismo que `(B,A)` |
| **Recorrido** | Se puede ir en ambos sentidos | Solo en el sentido de la flecha |
| **Dibujo** | Línea simple | Flecha |
| **Ejemplo** | Amistad en una red social | Seguir a alguien, calles de un solo sentido |

Pueden existir casos de grafos con adyacencia hacia si mismo, ósea aristas (A,A)

* A una arista `(A,A)` también se le llama **lazo** o **bucle** (*self-loop*).

### Según la existencia de ciclos

Grafo acíclico, un grafo donde da igual por cuál adyacencia se dirija, no hay ninguna arista que lleve al mismo nodo:

```
A
|
|
|
V
B----->C
```

Grafo cíclico, donde existen ciclos entres las adyacencias que permiten que un mismo nodo se repita en el camino

```
A<
| \
|   \
|    \
|     \
V      \
B -----> C
```

Sigue siendo un grafo cíclico

```
A<
| \
|   \
|    \
|     \
V      \
B -----> C <
        /  |
       /   |
      /    |
      v    D
      F
```

| Tipo | Característica | Ciclo del ejemplo |
|---|---|---|
| **Acíclico** | Ningún camino regresa al nodo de partida | No hay |
| **Cíclico** | Existe al menos un camino que regresa al mismo nodo | `A -> B -> C -> A` |

* Un grafo dirigido y acíclico se conoce como **DAG** (*Directed Acyclic Graph*).
* Un **árbol** es un grafo conexo y acíclico (por eso los árboles AVL y Red-Black son casos particulares de grafos).

## Terminología básica

| Término | Qué es | Ejemplo |
|---|---|---|
| **Vértice** | Cada nodo del grafo | `A` |
| **Arista** | Par de vértices que se relacionan | `(A,B)` |
| **Adyacencia** | Dos vértices unidos por una arista; `B` es adyacente de `A` si existe `(A,B)` | `B` es adyacente de `A` |
| **Camino** | Secuencia de vértices unidos por aristas | `A -> B -> C` |
| **Ciclo** | Camino que empieza y termina en el mismo vértice | `A -> B -> C -> A` |
| **Grado** | Cantidad de aristas de un vértice | `A` con 3 aristas tiene grado 3 |
| **Grado de salida** | Aristas que salen de un vértice (grafos dirigidos) | Aristas `(A,x)` |
| **Grado de entrada** | Aristas que llegan a un vértice (grafos dirigidos) | Aristas `(x,A)` |
| **Grafo conexo** | Existe un camino entre cualquier par de vértices | Todos los nodos se alcanzan |
| **Peso** | Valor asociado a una arista (distancia, costo, tiempo) | `(A,B)` con peso 5 |

## Representación de los grafos

### Lista de adyacencia

Una lista de vértices, y para cada vértice tener una lista de las adyacencias. Una lista de vértices y cada vértice una lista enlazada de sus adyacencias

* A -> B -> E
* B -> A -> D
* C -> B -> D -> E
* D -> A -> B
* E -> A -> B -> C -> D -> E

En ese caso sería que A tiene una arista dirigida hacia B y E, así para todos los casos.

| Vértice | Lista de adyacencias |
|:--:|---|
| **A** | B, E |
| **B** | A, D |
| **C** | B, D, E |
| **D** | A, B |
| **E** | A, B, C, D, E (incluye un lazo `(E,E)`) |

```python
# Lista de adyacencia con un dict (tabla hash)
grafo = {
    "A": ["B", "E"],
    "B": ["A", "D"],
    "C": ["B", "D", "E"],
    "D": ["A", "B"],
    "E": ["A", "B", "C", "D", "E"],
}
```

### Matriz de adyacencia

||A|B|C|D|E|
|:--:|:--:|:--:|:--:|:--:|:--:|
|A|0|1|0|0|1|
|B|1|0|0|1|0|
|C|0|1|0|1|1|
|D|1|1|0|0|0|
|E|1|1|1|1|1|

Utilizando el caso anterior, se hace una matriz de n*n, donde n sea la cantidad de vértices y se coloca un número por cada adyacencia que tenga con su nodo con el que se relaciona. Tomando 0 como que no tiene y 1 como que tiene 1.

En este caso se observa que gran parte de los nodos tienen pocas conexiones entre sí, desaprovechando gran cantidad de la memoria reservada. En el caso de una matriz 20x20, pero que solo se usen 20 casillas en total, sería desaprovechar amplia cantidad de memoria.

* Una matriz 20x20 tiene **400** casillas; si solo se usan 20, se desperdicia el **95%** de la memoria.
* En un grafo con pesos, en lugar de `1` se guarda el peso de la arista.

```python
# Matriz de adyacencia (orden A, B, C, D, E)
matriz = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]
```

### Comparación de representaciones

| Aspecto | Lista de adyacencia | Matriz de adyacencia |
|---|---|---|
| **Memoria** | O(V + E) | O(V²) |
| **¿Existe la arista (a,b)?** | O(grado de a) | **O(1)** |
| **Obtener todas las adyacencias de un vértice** | **O(grado)** | O(V) |
| **Recorrer todo el grafo (BFS / DFS)** | **O(V + E)** | O(V²) |
| **Mejor para** | Grafos **dispersos** | Grafos **densos** |

Se puede decidir cuál usar dependiendo de:

* El problema a resolver
* Su densidad

## Densidad

Se refiere a la cantidad de adyacencias que se encuentren en un grafo, se puede llevar a dos casos:
* Denso: Donde muchos nodos tienen muchas adyacencias entre sí, mejor utilizado con matrices de adyacencia.
* Disperso: Donde muchos nodos tienen pocas adyacencias entre sí, mejor utilizado con listas de adyacencia.

| Tipo | Cantidad de aristas | Representación recomendada |
|---|---|---|
| **Denso** | Cercana al máximo (`E ≈ V²`) | Matriz de adyacencia |
| **Disperso** | Mucho menor al máximo (`E ≈ V`) | Lista de adyacencia |

## Recorridos de un grafo

Un recorrido visita **todos los vértices alcanzables** desde un vértice inicial, visitando cada uno **una sola vez** (se lleva un registro de los vértices ya visitados para no caer en ciclos).

| Recorrido | Estructura que usa | Idea |
|---|---|---|
| **BFS** (*Breadth First Search*, en anchura) | **Cola** | Visita primero todos los vecinos y luego avanza al siguiente nivel |
| **DFS** (*Depth First Search*, en profundidad) | **Pila** o **recursividad** (*backtracking*) | Avanza lo más profundo posible y retrocede cuando no hay más adyacencias |

## Grafo de ejemplo para BFS y DFS

> Los nodos A,B,C,D,E,F representas las `llaves` o `keys`. BFS se utiliza cola

```
|--A--->D--->B
|  |<\  |  />^
|  V   \v/   |
|  F -->E<---C
|  |         ^
v  |         |
G<-|         |
|____________|
```

> Nota: Procesar las adyacencias de menor a mayor

Lista de adyacencia del grafo (dirigido), ordenada de menor a mayor:

| Vértice | Adyacencias |
|:--:|---|
| **A** | D, F, G |
| **B** | (ninguna) |
| **C** | B, E |
| **D** | B, E |
| **E** | A, B |
| **F** | E, G |
| **G** | C |

Matriz de adyacencia del mismo grafo:

||A|B|C|D|E|F|G|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|A|0|0|0|1|0|1|1|
|B|0|0|0|0|0|0|0|
|C|0|1|0|0|1|0|0|
|D|0|1|0|0|1|0|0|
|E|1|1|0|0|0|0|0|
|F|0|0|0|0|1|0|1|
|G|0|0|1|0|0|0|0|

* Es un grafo **cíclico**: por ejemplo, `A -> D -> E -> A`.

## BFS

> Los nodos A,B,C,D,E,F representas las `llaves` o `keys`. BFS se utiliza cola

### Recorrido -> A

* Inserta A (Nodo inicial)
* Sacar vértice de la cola (A)
* Visita V (A)
* Visite Adyacencias {D,F,G} (Solo se visitan 1 vez)
* Se repite

Resultado final: **A,D,F,G,B,E,C**

Entonces, el resumen del proceso es extraer el nodo, ver sus adyacencias e insertar todos en su orden y esto se repite.

| Paso | Se saca de la cola | Se visita | Se insertan (no vistos) | Cola resultante |
|:--:|:--:|:--:|---|---|
| 0 | | | A (inicial) | `[A]` |
| 1 | A | A | D, F, G | `[D, F, G]` |
| 2 | D | D | B, E | `[F, G, B, E]` |
| 3 | F | F | (E y G ya están en la cola) | `[G, B, E]` |
| 4 | G | G | C | `[B, E, C]` |
| 5 | B | B | (sin adyacencias) | `[E, C]` |
| 6 | E | E | (A y B ya fueron visitados) | `[C]` |
| 7 | C | C | (B y E ya fueron visitados) | `[]` |

```python
from collections import deque

def bfs(grafo, inicio):
    visitados = {inicio}
    cola = deque([inicio])
    orden = []
    while cola:
        v = cola.popleft()              # Sacar vértice de la cola
        orden.append(v)                 # Visitar V
        for w in sorted(grafo[v]):      # Adyacencias de menor a mayor
            if w not in visitados:      # Solo se visitan 1 vez
                visitados.add(w)
                cola.append(w)          # Insertar en la cola
    return orden
```

## DFS

> DFS utiliza Pila o Recursividad.. Backtracking

### Pila

* Inserta A (Nodo inicial)
* Sacar vértice de la cola (A)
* Visita V (A)
* Visite Adyacencia menor (Solo se visitan 1 vez) (Push)
* Se repite hasta que ya no tenga adyacencia, entonces se hace Pop

Resultado final: **A,D,B,E,F,G,C**

| Paso | Vértice actual | Acción | Pila |
|:--:|:--:|---|---|
| 1 | A | Visita A, adyacencia menor no vista: D (Push) | `[A, D]` |
| 2 | D | Visita D, adyacencia menor no vista: B (Push) | `[A, D, B]` |
| 3 | B | Visita B, no tiene adyacencias (Pop) | `[A, D]` |
| 4 | D | Siguiente adyacencia no vista: E (Push) | `[A, D, E]` |
| 5 | E | Visita E, A y B ya visitados (Pop) | `[A, D]` |
| 6 | D | Sin más adyacencias (Pop) | `[A]` |
| 7 | A | Siguiente adyacencia no vista: F (Push) | `[A, F]` |
| 8 | F | Visita F, E ya visitado, siguiente: G (Push) | `[A, F, G]` |
| 9 | G | Visita G, siguiente: C (Push) | `[A, F, G, C]` |
| 10 | C | Visita C, B y E ya visitados (Pop) | `[A, F, G]` |
| 11 | G, F, A | Sin más adyacencias (Pop hasta vaciar la pila) | `[]` |

```python
def dfs(grafo, v, visitados=None, orden=None):
    if visitados is None:
        visitados, orden = set(), []
    visitados.add(v)
    orden.append(v)                         # Visitar V
    for w in sorted(grafo[v]):              # Adyacencia menor primero
        if w not in visitados:              # Solo se visitan 1 vez
            dfs(grafo, w, visitados, orden) # Push (llamada recursiva)
    return orden                            # Al terminar la función, Pop
```

#### Ejemplo de práctica del mismo ejemplo, empezando en E:

Recorrido BFS: **E,A,B,D,F,G,C**

Recorrido DFS: **E,A,D,B,F,G,C**

| Paso | Cola | Visita | Resultado parcial |
|:--:|---|:--:|---|
| 1 | `[E]` | E | E |
| 2 | `[A, B]` | A | E,A |
| 3 | `[B, D, F, G]` | B | E,A,B |
| 4 | `[D, F, G]` | D | E,A,B,D |
| 5 | `[F, G]` | F | E,A,B,D,F |
| 6 | `[G]` | G | E,A,B,D,F,G |
| 7 | `[C]` | C | E,A,B,D,F,G,C |

| Paso | Vértice | Acción | Pila |
|:--:|:--:|---|---|
| 1 | E | Visita E, menor adyacencia: A (Push) | `[E, A]` |
| 2 | A | Visita A, menor adyacencia: D (Push) | `[E, A, D]` |
| 3 | D | Visita D, menor adyacencia: B (Push) | `[E, A, D, B]` |
| 4 | B | Visita B, sin adyacencias (Pop) | `[E, A, D]` |
| 5 | D | E ya visitado (Pop) | `[E, A]` |
| 6 | A | Siguiente adyacencia: F (Push) | `[E, A, F]` |
| 7 | F | Visita F, siguiente: G (Push) | `[E, A, F, G]` |
| 8 | G | Visita G, siguiente: C (Push) | `[E, A, F, G, C]` |
| 9 | C | Visita C (Pop hasta vaciar la pila) | `[]` |

## Comparación BFS y DFS

| Aspecto | BFS | DFS |
|---|---|---|
| **Estructura** | Cola (FIFO) | Pila (LIFO) o recursividad |
| **Orden de visita** | Por niveles (vecinos primero) | En profundidad (*backtracking*) |
| **Resultado desde A** | A,D,F,G,B,E,C | A,D,B,E,F,G,C |
| **Resultado desde E** | E,A,B,D,F,G,C | E,A,D,B,F,G,C |
| **Tiempo (lista de adyacencia)** | O(V + E) | O(V + E) |
| **Tiempo (matriz de adyacencia)** | O(V²) | O(V²) |
| **Memoria extra** | Cola con hasta un nivel completo | Pila con hasta la profundidad máxima |
| **Usos comunes** | Camino con menos aristas, nivel de un nodo | Detectar ciclos, orden topológico, laberintos |

* Ambos recorridos visitan cada vértice **una sola vez**, por eso se necesita marcar los vértices visitados.
* Si el grafo no es conexo, el recorrido desde un vértice solo visita los vértices alcanzables desde él.

## Resumen

| Idea | Resumen |
|---|---|
| **Qué es** | Un conjunto de vértices y aristas: `G = {V, E}` |
| **Dirección** | No dirigido (`(A,B) = (B,A)`) o dirigido (`(A,B) ≠ (B,A)`) |
| **Ciclos** | Cíclico (un nodo se repite en el camino) o acíclico |
| **Representación** | Lista de adyacencia (dispersos) o matriz de adyacencia (densos) |
| **BFS** | Usa cola, recorre por niveles |
| **DFS** | Usa pila o recursividad, recorre en profundidad con backtracking |
| **Regla de práctica** | Procesar las adyacencias de menor a mayor |
