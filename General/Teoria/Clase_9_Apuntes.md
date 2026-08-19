# Heaps y Colas de prioridad

## Heap

> Idea básica de los Heaps, obtener el máximo elemento o el mínimo elemento. Mejorar complejidad algorítmica para determinar cuál es el elemento mayor o menor

Se representan como un árbol binario completo. Un árbol binario es un tipo de estructura de datos donde se tiene una colección de elementos llamados nodos conectados por sus aristas, el heap se puede representar como dicho árbol.

Tiene 2 propiedades importantes:
* Tiene que ser un árbol binario completo. Un árbol donde los hijos de las derecha no se rellenan sino antes se han completado aquellos de la izquierda. Osea debe de rellenarse la cantidad de nodos hijos correctos para cada lado.
* Hay 2 tipos de heap: Máximos o mínimos:
  - Máximo: El padre es mayor que sus dos hijos, esta propiedad se replica para todos los nodos del árbol. Relación hijo derecho con hijo izquierdo no importa, solamente la relación padre/hijo donde padre siempre es mayor.
  - Mínimo: El padre es menor que ambos hijos, esta propiedad se replica para todos los nodos del árbol.
 
> Denominado Binary Heap

```
       20
     /    \
    17     8
   / \    /  \
  10  2  6    5
```

Se puede representar un heap binario como vector o como árbol.

## Representación de árbol binario en forma vector
|20|17|8|10|2|6|5|VALOR|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|0|1|2|3|4|5|6|POS|

> Heap Máximos

La raíz siempre va a ir en la primera posición. Seguido por sus hijos. Se tienen que ver los elementos de izquierda a derecha.

Para saber cuanto se debe de mover o identificar cuál miembro del vector es padre/hijo de quién.

* Raíz: Siempre será la posición 0 en el vector.
* Padre: $\frac{i}{2}$

Dicha fórmula no funciona, ya que otorga un padre diferente para nodos hermanos.

* [17]: $\frac{1}{2}$ = 0  (IndexPadre a buscar: 0)
* [8] : $\frac{2}{2}$ = 1  (IndexPadre a buscar: 0)
* [10]: $\frac{3}{2}$ = 1  (IndexPadre a buscar: 1)
* [2] : $\frac{4}{2}$ = 2  (IndexPadre a buscar: 1)
* [6] : $\frac{5}{2}$ = 2  (IndexPadre a buscar: 2)
* [5] : $\frac{6}{2}$ = 3  (IndexPadre a buscar: 2)

### Fórmula

> Para determinar el padre con exactitud

Al probarlo con una nueva fórmula descrita como

* Raíz: Siempre será la posición 0 en el vector.
* Padre: $\frac{i-1}{2}$

Y cambiando los nuevos valores, se observa que:

* [17]: $\frac{1-1}{2}$ = 0  (IndexPadre a buscar: 0)
* [8]_ : $\frac{2-1}{2}$ = 0  (IndexPadre a buscar: 0)
* [10]: $\frac{3-1}{2}$ = 1  (IndexPadre a buscar: 1)
* [2]_ : $\frac{4-1}{2}$ = 1  (IndexPadre a buscar: 1)
* [6]_ : $\frac{5-1}{2}$ = 2  (IndexPadre a buscar: 2)
* [5]_ : $\frac{6-1}{2}$ = 2  (IndexPadre a buscar: 2)

> Y se demuestra que la nueva fórmula de $\frac{i-1}{2}$ muestra el resultado deseado.

Con esto ahora se debe de calcular cuál es el hijo derecho e izquierdo de cada padre.

* Raíz: 0.
* Padre: $\frac{i}{2}$.
* Izq: $(i \times 2) + 1$
* Der: $(i \times 2) + 2$

Y se procede a verificar dichas fórmulas para verificar que conforman el método para encontrar a los hijos de cada nodo padre.

* [20 Hijos] { Izq: $(0 \times 2) + 1$ = 1 (Resultado esperado: 1) } | { Dere: $(0 \times 2) + 2$ = 2 (Resultado esperado: 2) }
* [17 Hijos] { Izq: $(1 \times 2) + 1$ = 3 (Resultado esperado: 3) } | { Dere: $(1 \times 2) + 2$ = 4 (Resultado esperado: 4) }
* [8 Hijos ] { Izq: $(2 \times 2) + 1$ = 5 (Resultado esperado: 5) } | { Dere: $(2 \times 2) + 2$ = 6 (Resultado esperado: 6) }

> Y se demuestra que las fórmula de $(i \times 2) + 1$ y $(i \times 2) + 2$ muestran el resultado deseado.

Recordar que estas fórmulas únicamente sirven si son aplicadas en un binary heap.

### Operaciones del Heap

Heap permite obtener de manera óptima los máximos y mínimos.

* En un heap Máximo, obtener el elemento Max implica una complejidad algorítmica de O(1), en una lista enlazada, la complejidad para dicho caso será de O(n) al tener que recorrer todos los casos.

#### Insertar

> Volviendo al ejemplo del árbol utilizado y el vector representativo

##### Árbol Binario Completo
```
       20
     /    \
    17     8
   / \    /  \
  10  2  6    5
```

##### Vector
|20|17|8|10|2|6|5|VALOR|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|0|1|2|3|4|5|6|POS|

Al insertar un elemento 22, tiene de padre $\frac{7-1}{2}$ = 3. Lo que significa el elemento 10.

A partir de insertar dicho elemento 22, automáticamente deja de ser un heap al romperse la estructura del árbol binario y romper la norma del padre siempre mayor que sus hijos (10 > 22: Falso).

##### Árbol Binario Completo con Inserción de 22 inicial
```
       20
     /    \
    17     8
   / \    /  \
  10  2  6    5
 /
22
```

##### Vector con Inserción de 22 inicial
|20|17|8|10|2|6|5|22|VALOR|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|0|1|2|3|4|5|6|7|POS|

Para resolver este problema, se debe de realizar la operación `Bubble Up`, se toma el elemento y se sube hasta acomodarlo en el lugar correcto. Para este caso particular del ejemplo, se debe de redirigir el nodo 22 hasta la raíz.



