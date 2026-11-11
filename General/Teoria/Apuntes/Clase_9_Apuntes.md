# 9: Heaps y Colas de Prioridad

## Heap

> Idea básica de los Heaps: obtener el máximo elemento o el mínimo elemento, mejorando la complejidad algorítmica para determinar cuál es el elemento mayor o menor.

Se representan como un árbol binario completo. Un árbol binario es un tipo de estructura de datos donde se tiene una colección de elementos llamados **nodos**, conectados por sus aristas; el heap se puede representar como dicho árbol.

### Propiedades del Heap

Tiene 2 propiedades importantes:

* **Árbol binario completo:** un árbol donde los hijos de la derecha no se rellenan sin antes haberse completado aquellos de la izquierda. O sea, debe rellenarse la cantidad de nodos hijos correctos para cada lado.
* **Tipo de heap (máximo o mínimo):**
  * **Máximo:** El padre es mayor que sus dos hijos; esta propiedad se replica para todos los nodos del árbol. La relación entre el hijo derecho y el hijo izquierdo no importa, solamente la relación padre/hijo, donde el padre siempre es mayor.
  * **Mínimo:** El padre es menor que ambos hijos; esta propiedad se replica para todos los nodos del árbol.

> Denominado **Binary Heap**.

```
       20
     /    \
    17     8
   / \    /  \
  10  2  6    5
```

> **Nota adicional:** al ser un árbol binario completo, el Binary Heap **no** es lo mismo que un Árbol Binario de Búsqueda (BST); en un heap no existe orden entre hermanos ni entre subárboles izquierdo/derecho como sí ocurre en un BST, solo se garantiza la relación padre-hijo.

Se puede representar un heap binario como vector o como árbol.

---

## Representación de árbol binario en forma de vector

| 20 | 17 | 8 | 10 | 2 | 6 | 5 | VALOR |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | POS |

> Heap Máximo

La raíz siempre va a ir en la primera posición, seguida por sus hijos. Se tienen que ver los elementos de izquierda a derecha.

### Fórmula para identificar al padre

Para saber cuánto se debe mover o identificar cuál miembro del vector es padre/hijo de quién:

* **Raíz:** Siempre será la posición 0 en el vector.
* **Padre (primer intento):** $\frac{i}{2}$

Dicha fórmula no funciona, ya que otorga un padre diferente para nodos hermanos.

* [17]: $\frac{1}{2}$ = 0  (IndexPadre a buscar: 0)
* [8] : $\frac{2}{2}$ = 1  (IndexPadre a buscar: 0)
* [10]: $\frac{3}{2}$ = 1  (IndexPadre a buscar: 1)
* [2] : $\frac{4}{2}$ = 2  (IndexPadre a buscar: 1)
* [6] : $\frac{5}{2}$ = 2  (IndexPadre a buscar: 2)
* [5] : $\frac{6}{2}$ = 3  (IndexPadre a buscar: 2)

### Fórmula corregida

> Para determinar el padre con exactitud.

Al probarlo con una nueva fórmula descrita como:

* **Raíz:** Siempre será la posición 0 en el vector.
* **Padre:** $\frac{i-1}{2}$

Y cambiando los nuevos valores, se observa que:

* [17]: $\frac{1-1}{2}$ = 0  (IndexPadre a buscar: 0)
* [8]_ : $\frac{2-1}{2}$ = 0  (IndexPadre a buscar: 0)
* [10]: $\frac{3-1}{2}$ = 1  (IndexPadre a buscar: 1)
* [2]_ : $\frac{4-1}{2}$ = 1  (IndexPadre a buscar: 1)
* [6]_ : $\frac{5-1}{2}$ = 2  (IndexPadre a buscar: 2)
* [5]_ : $\frac{6-1}{2}$ = 2  (IndexPadre a buscar: 2)

> Y se demuestra que la nueva fórmula de $\frac{i-1}{2}$ muestra el resultado deseado.

### Fórmulas para hijo izquierdo y derecho

Con esto, ahora se debe calcular cuál es el hijo derecho e izquierdo de cada padre.

* **Raíz:** 0
* **Padre:** $\frac{i-1}{2}$
* **Izq:** $(i \times 2) + 1$
* **Der:** $(i \times 2) + 2$

Y se procede a verificar dichas fórmulas para comprobar que conforman el método para encontrar a los hijos de cada nodo padre.

* [20 Hijos] { Izq: $(0 \times 2) + 1$ = 1 (Resultado esperado: 1) } | { Dere: $(0 \times 2) + 2$ = 2 (Resultado esperado: 2) }
* [17 Hijos] { Izq: $(1 \times 2) + 1$ = 3 (Resultado esperado: 3) } | { Dere: $(1 \times 2) + 2$ = 4 (Resultado esperado: 4) }
* [8 Hijos ] { Izq: $(2 \times 2) + 1$ = 5 (Resultado esperado: 5) } | { Dere: $(2 \times 2) + 2$ = 6 (Resultado esperado: 6) }

> Y se demuestra que las fórmulas de $(i \times 2) + 1$ y $(i \times 2) + 2$ muestran el resultado deseado.

> Recordar que estas fórmulas únicamente sirven si son aplicadas en un **binary heap**.

---

## Operaciones del Heap

El heap permite obtener de manera óptima los máximos y mínimos.

* En un heap Máximo, obtener el elemento Max implica una complejidad algorítmica de **O(1)**; en una lista enlazada, la complejidad para dicho caso sería de **O(n)**, al tener que recorrer todos los elementos.

### Insertar

> Volviendo al ejemplo del árbol utilizado y el vector representativo.

#### Árbol Binario Completo (inicial)

```
       20
     /    \
    17     8
   / \    /  \
  10  2  6    5
```

#### Vector (inicial)

| 20 | 17 | 8 | 10 | 2 | 6 | 5 | VALOR |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | POS |

Al insertar un elemento **22**, tiene de padre $\frac{7-1}{2}$ = 3. Lo que significa el elemento 10.

A partir de insertar dicho elemento 22, automáticamente deja de ser un heap al romperse la estructura del árbol binario y la norma del padre siempre mayor que sus hijos (10 > 22: Falso).

#### Árbol Binario Completo con inserción de 22 (inicial)

```
       20
     /    \
    17     8
   / \    /  \
  10  2  6    5
 /
22
```

#### Vector con inserción de 22 (inicial)

| 20 | 17 | 8 | 10 | 2 | 6 | 5 | 22 | VALOR |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | POS |

Para resolver este problema, se debe realizar la operación **Bubble Up**: se toma el elemento y se sube hasta acomodarlo en el lugar correcto. Para este caso particular del ejemplo, se debe redirigir el nodo 22 hasta la raíz.

> **Proceso:** si es mayor, se intercambia el padre con el hijo.

#### Árbol Binario Completo — primer paso del Bubble Up

```
       20
     /    \
    17     8
   / \    /  \
  22  2  6    5
 /
10
```

#### Vector — primer paso del Bubble Up

| 20 | 17 | 8 | 22 | 2 | 6 | 5 | 10 | VALOR |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | POS |

Se puede observar que no hace falta realizar una verificación de los nodos hermanos, al ya dar por hecho que el nuevo nodo padre es mayor que el que se acaba de intercambiar.

#### Árbol Binario Completo — segundo paso del Bubble Up

```
       20
     /    \
    22     8
   / \    /  \
  17  2  6    5
 /
10
```

#### Vector — segundo paso del Bubble Up

| 20 | 22 | 8 | 17 | 2 | 6 | 5 | 10 | VALOR |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | POS |

Y finalmente se llega al resultado final del Bubble Up.

#### Árbol Binario Completo — tercer paso del Bubble Up (resultado final)

```
       22
     /    \
    20     8
   / \    /  \
  17  2  6    5
 /
10
```

#### Vector — tercer paso del Bubble Up (resultado final)

| 22 | 20 | 8 | 17 | 2 | 6 | 5 | 10 | VALOR |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | POS |

Otro ejemplo aplicando la operación de insertar: al insertar en el heap el elemento **19**, solo hay que realizar 1 solo movimiento.

#### Árbol Binario Completo — inserción de 19

```
       22
     /    \
    20     8
   / \    /  \
  19  2  6    5
 /  \
10   17
```

#### Vector — inserción de 19

| 22 | 20 | 8 | 19 | 2 | 6 | 5 | 10 | 17 | VALOR |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | POS |

La complejidad algorítmica de cada operación de inserción implica un **O(log n)**, al solo tener que pasar por la mitad (o el nivel de altura) del árbol en cada inserción.

---

### Heapify

> Trata de tomar un vector y convertirlo en un Heap.

#### Vector de ejemplo

| 8 | 11 | 2 | 16 | 5 | 7 | 13 | 20 | VALOR |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | POS |

```
       8
     /   \
    11     2
   / \    /  \
  16  5  7    13
 /  
20   
```

Uno de los procesos es tomar los valores desde el final y volver hasta el inicio, aplicando la operación Bubble Up cada vez que se necesite.

> Con el elemento de valor 20:

```
       20
     /    \
    16     13
   / \    /  \
  11  5  7    2
 /  
8  
```

Al realizar cada intercambio, se verifica que 20 es mayor a 16 → Bubble Up. El siguiente elemento, 13, ya es heap; igual aplica para 7 y 5. Al llegar de nuevo a 20, este es mayor a 11 → Bubble Up.

Cada vez que se hace un Bubble Up, se debe verificar la integridad del heap del nuevo elemento hijo con cada hijo que tenga dicho elemento, para asegurarse de que no sea menor. En el caso del 11, al tener un hijo mayor (en este caso el 16), se intercambian nuevamente. Al llegar a un caso en que un elemento es menor, este debe intercambiarse por el mayor de sus hijos.

Finalmente, al llegar a 8, este es menor y se debe seleccionar al mayor de sus hijos. Al realizar el intercambio entre 8 ↔ 20, se realiza la verificación, y así sucesivamente, intercambiando el 8 con el 16 y con el 11.

> **Resumen:** yendo desde el último hasta el primero, se verifica si es heap y, si no lo es, se intercambia; en caso de intercambio, se verifica de nuevo el heap. Al finalizar la verificación, se devuelve al inicio.
>
> Este algoritmo tiene una complejidad de **O(n)**.

---

## Cola de prioridad

> Cualquier caso donde se tenga que ordenar los elementos según una prioridad.

Es una estructura de datos donde se toma el elemento que sigue con respecto a una prioridad. Es un **TDA** con las operaciones **insertar** y un **pop** o **dequeue**, que devuelven el elemento con la prioridad máxima o más alta.

Se puede implementar a través de un Heap Máximo o un Heap Mínimo. En el caso de ejemplo, un Heap Máx con clases `Persona`, donde a cada una se le asigna una prioridad numérica.

```
       P10
     /    \
    P8     P7
   / \    
  P4  P3      
```

La cola de prioridad es la abstracción de lo que debe realizarse en un Heap; también se puede implementar como lista enlazada, pero en términos de complejidad algorítmica esta siempre estará en los rangos de **O(n)**, mientras que el Heap estará en los rangos de **O(n)** o **O(log n)**.

> Es más eficiente trabajar una cola de prioridad en un heap que en una lista enlazada.

> **Nota adicional — Aplicaciones reales:** las colas de prioridad basadas en heap se utilizan en algoritmos como **Dijkstra** (encontrar el camino más corto en un grafo) y en algoritmos de compresión como **Huffman**; también son la base de estructuras como `PriorityQueue` en Java o `heapq` en Python, que implementan internamente un Heap Mínimo.
