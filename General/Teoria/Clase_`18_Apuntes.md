# Árboles AVL

Variable llamada factor de balance (FB). Para todos los nodos, se calcula el factor de balance. Esto es la `Diferencia de la altura del subárbol Izquierdo y el subárbol Derecho`

Con el Factore de balance, el AVL va a determinar: **El árbol está balanceado si el FB no supera 1 (cada nodo del árbol)**. Nota: Los árboles AVL son árboles BST

El factor de balance de las hojas siempre es 0
El de cada nodo, es la diferencia de los FB

Siempre se balancea con cada inserción y cada eliminación

Los árboles AVL y Red-Black son `Auto Balanceados`

## Casos

## Caso 1 LL

**Aplica a inserciones y borrado**

Aplica si la inserción se hace en el sub-árbol izquierdo de hijo izquierdo de "x". Donde x es el nodo donde está el desbalance. Se resuelve con una rotación simple a la derecha, se hace en el nodo "x".

### Ejemplo 1

```
    10
   /  \
  7    19   <- Se arregla siempre el primero que aparezca, el llamado "x", se va a arreglar cualquier otro caso de desbalance, empezando desde abajo hasta arriba
      /
     15
    /
   13  <- Nodo insertado
```

Se aplica la rotación simple a la derecha, moviendo girando el axis hacia la derecha y todos sus nodos en conjunto.

```
    10
   /  \
  7    15      -> Rotación aplicada
      /  \
     13   19
```

### Ejemplo 2

```
       14  <- Es el nodo "x" desbalanceado
      /  \
     6    25
    / \
   4  10
  /
 2
```

En este caso, se debe de colocar el hijo derecho del nodo 6 como hijo izquierdo de la raiz, al hacer la rotación

```
       6 
      /  \
     4    14   <- Hijo derecho de 6 se coloco como hijo izquierdo de 14, la raíz anterior
    /    /  \
   2   10    25
```

## Caso 2 RR

Inserción se hace en el sub-árbol derecho del hijo derecho de "x". Donde x es el nodo donde está el desbalance. Se resuelve con una rotación simple a la izquierda, se hace en el nodo "x".

```
    18
   /  \
  10    23    <- Nodo 10 es el "x" desbalanceado
   \
    15    <_
     \      \  Rotación de los nodos
      17     |
```

```
    18
   /  \
  15    23
 / \
10  17
```

Nota: Aplica lo mismo de que si hijo izquierdo de nodo desbalanceado se pone como el hijo izquierdo de la raiz antigua.

## Caso 3 LR

Inserción se hace en el sub-árbol izquierdo del hijo derecho en "x". Donde x es el nodo donde está el desbalance. Se resuelve con una rotación doble, ósea una rotación simple a la derecha, se hace en el hijo derecho del nodo "x". Luego se aplica una rotación simple a la izquierda, se hace en el nodo "x".

```
    18
   /  \
  10    25   <- Nodo "x" Encontrado por FB 1-3 = 2
 /     /  \
6     20  30
         /  \
        28   33
         \
          29
```

Primer paso, rotación simple derecha en hijo derecho de x

```
    18
   /  \
  10    25   <- "x"
 /     /  \
6     20  28
            \
            30
            / \
          29  33
```

Nota: Árbol siempre debe de cumplir BST en todos sus pasos de rotaciones y movimientos, ahora se aplica segundo paso, rotación simple izquierda en x.

```
    18
   /  \
  10    28
 /     /  \
6     25   30
     /     / \
    20    29  33
```

## Caso 4 RL

Inserción se hace en el sub-árbol derecho del hijo izquierdo en "x". Donde x es el nodo donde está el desbalance. Se resuelve con una rotación doble, ósea una rotación simple a la izquierda, se hace en el hijo izquierdo del nodo "x". Luego se aplica una rotación simple a la derecha, se hace en el nodo "x".


```
    16   <- Nodo "x". FB 3-1 = 2
   /  \
  11    17
 / \    
7   13
      \
       15
```

Primer paso, rotación simple izquierda en hijo izquierdo de x.

```
      16   <- Nodo "x".
     /  \
    13    17
   / \    
  11  15
 /
7
```

Luego se aplica el segundo paso, la rotación derecha en x

```
      13
     /  \
    11   16   <- Recordar que Nodo 15, hijo derecho de hijo izquierdo de nodo x, se mueve como hijo directo izquierdo de nodo x al aplicar la rotación simple.
   /    /  \
  7   15    17
```

## Práctica - Lab

a) Insertar al árbol 19,23,28,7,15,20,13,6

```

```

b) Insertar al árbol 1,2,3,4,5,6,7,8,9,10

```
      13
     /  \
    11   16   
   /    /  \
  7   15    17
```
c) Insertar al árbol 25, 14, 



