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

## Caso 2 PR

Inserción se hace en el sub-árbol derecho del hijo derecho de "x". Donde x es el nodo donde está el desbalance. Se resuelve con una rotación simple a la izquierda, se hace en el nodo "x".

```
    18
   /  \
  10    23    <- Nodo 10 es el "x" desbalanceado
   \
    15    <_
     \      \
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

Inserción se hace en el sub-árbol izquierdo del hijo derecho en "x". Donde x es el nodo donde está el desbalance. Se resuelve con una rotación doble, ósea una rotación simple a la derecha, se hace en el hijo del nodo "x". Luego se aplica una rotación simple a la izquierda, se hace en el nodo "x".




