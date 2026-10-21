# Grafos

Son compuestos por nodos y aristas, las cuales son pares de elementos

G = {V,E}

E = (a,b)

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

Pueden existir casos de grafos con adyacencia hacia si mismo, ósea aristas (A,A)


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

## Representación de los grafos

### Lista de adyacencia

Una lista de vértices, y para cada vértice tener una lista de las adyacencias. Una lista de vértices y cada vértice una lista enlazada de sus adyacencias

* A -> B -> E
* B -> A -> D
* C -> B -> D -> E
* D -> A -> B
* E -> A -> B -> C -> D -> E

En ese caso sería que A tiene una arista dirigida hacia B y E, así para todos los casos.

### Matriz de adyacencia

||A|B|C|D|E|
|:--:|:--:|:--:|:--:|:--:|:--:
|A|0|1|0|0|1
|B|1|0|0|1|0
|C|0|1|0|1|1
|D|1|1|0|0|0
|E|1|1|1|1|1

Utilizando el caso anterior, se hace una matriz de n*n, donde n sea la cantidad de vértices y se coloca un número por cada adyacencia que tenga con su nodo con el que se relaciona. Tomando 0 como que no tiene y 1 como que tiene 1.

En este caso se observa que gran parte de los nodos tienen pocas conexiones entre sí, desaprovechando gran cantidad de la memoria reservada. En el caso de una matriz 20x20, pero que solo se usen 20 casillas en total, sería desaprovechar amplia cantidad de memoria.

Se puede decidir cuál usar dependiendo de:

* El problema a resolver
* Su densidad

## Densidad

Se refiere a la cantidad de adyacencias que se encuentren en un grafo, se puede llevar a dos casos:
* Denso: Donde muchos nodos tienen muchas adyacencias entre sí, mejor utilizado con matrices de adyacencia.
* Disperso: Donde muchos nodos tienen pocas adyacencias entre sí, mejor utilizado con listas de adyacencia.

## BFS

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

### Recorrido -> A

* Inserta A (Nodo inicial)
* Sacar vértice de la cola (A)
* Visita V (A)
* Visite Adyacencias {D,F,G} (Solo se visitan 1 vez)
* Se repite

Resultado final: **A,D,F,G,B,E,C**

Entonces, el resumen del proceso es extraer el nodo, ver sus adyacencias e insertar todos en su orden y esto se repite.

## DFS

> DFS utiliza Pila o Recursividad.. Backtracking

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

### Pila

* Inserta A (Nodo inicial)
* Sacar vértice de la cola (A)
* Visita V (A)
* Visite Adyacencia menor (Solo se visitan 1 vez) (Push)
* Se repite hasta que ya no tenga adyacencia, entonces se hace Pop

Resultado final: **A,D,B,E,F,G,C**

#### Ejemplo de práctica del mismo ejemplo, empezando en E:

Recorrido BFS: **E,A,B,D,F,G,C**

Recorrido DFS: **E,A,D,B,F,G,C**
