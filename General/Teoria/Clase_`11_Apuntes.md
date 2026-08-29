# Algoritmos de Ordenamiento (Sorting)

## Conceptos generales antes de comenzar

* **Complejidad temporal:** cantidad de instrucciones (comparaciones/intercambios) que realiza el algoritmo, medida en el mejor caso, caso promedio y peor caso.
* **Complejidad espacial:** memoria adicional que requiere el algoritmo, más allá del arreglo original.
  * **In-place:** el algoritmo ordena usando O(1) memoria extra (o muy poca), sin necesitar una copia completa del arreglo.
  * **Out-of-place:** requiere memoria adicional proporcional al tamaño de la entrada (O(n) o más).
* **Estabilidad:** un algoritmo es **estable** si mantiene el orden relativo de los elementos que tienen el mismo valor de comparación (por ejemplo, ordenar personas por edad sin alterar el orden original entre quienes tienen la misma edad).
* **Adaptabilidad:** un algoritmo es **adaptativo** si su rendimiento mejora cuando la entrada ya está parcial o totalmente ordenada.

| Algoritmo | Mejor caso | Caso promedio | Peor caso | Espacio | Estable | Adaptativo |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Burbuja | O(n) | O(n²) | O(n²) | O(1) | Sí | Sí |
| Selección | O(n²) | O(n²) | O(n²) | O(1) | No | No |
| Inserción | O(n) | O(n²) | O(n²) | O(1) | Sí | Sí |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | No |
| Mergesort | O(n log n) | O(n log n) | O(n log n) | O(n) | Sí | No |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Sí | No |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n + k) | Sí | No |

> Donde `n` es la cantidad de elementos, `k` es el rango de valores (Counting Sort) o la cantidad de dígitos/posiciones (Radix Sort).

---

## Ordenamiento Burbuja (Bubble Sort)

### Funcionamiento

Recorre el arreglo repetidamente, comparando pares de elementos **adyacentes** e intercambiándolos si están en el orden incorrecto. En cada pasada completa, el elemento más grande (o más pequeño) "burbujea" hasta su posición final, de forma similar a como una burbuja sube a la superficie.

* Se repite el proceso `n-1` veces, reduciendo en cada pasada el rango a revisar, ya que el final del arreglo queda ordenado.
* Se puede optimizar agregando una bandera que detenga el algoritmo si en una pasada completa no hubo ningún intercambio (esto es lo que le da su **adaptabilidad**: si el arreglo ya está ordenado, termina en O(n)).

### Rendimiento

* **Mejor caso O(n):** arreglo ya ordenado (con la optimización de la bandera).
* **Peor caso O(n²):** arreglo ordenado en orden inverso.
* **Espacio O(1):** todos los intercambios se hacen dentro del mismo arreglo (in-place).
* **Estable:** sí, ya que solo se intercambian elementos adyacentes cuando uno es estrictamente mayor que el otro, sin saltar posiciones.

### Código en Python

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio = True
        if not intercambio:  # Optimización: ya está ordenado
            break
    return arr

print(bubble_sort([5, 2, 9, 1, 5, 6]))
```

---

## Ordenamiento por Selección (Selection Sort)

### Funcionamiento

Divide el arreglo en una parte ordenada (al inicio) y una desordenada (al resto). En cada iteración, busca el elemento **mínimo** de la parte desordenada y lo intercambia con el primer elemento de dicha parte, haciendo crecer la porción ordenada en uno.

* A diferencia de burbuja, aquí se realiza **como máximo un intercambio por pasada**, aunque la cantidad de comparaciones sigue siendo la misma sin importar el orden inicial de los datos.

### Rendimiento

* **Todos los casos O(n²):** siempre se recorre la parte desordenada completa para encontrar el mínimo, sin importar si el arreglo ya está ordenado o no; por eso **no es adaptativo**.
* **Espacio O(1):** in-place.
* **No estable:** el intercambio directo entre el mínimo encontrado y la primera posición puede alterar el orden relativo de elementos iguales (por ejemplo, puede "saltar" un elemento igual que estaba antes).

### Código en Python

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]
    return arr

print(selection_sort([5, 2, 9, 1, 5, 6]))
```

---

## Ordenamiento por Inserción (Insertion Sort)

### Funcionamiento

Construye el arreglo ordenado de a un elemento a la vez. Toma cada elemento de la parte desordenada y lo **inserta** en la posición correcta dentro de la parte ya ordenada, desplazando los elementos mayores hacia la derecha.

* Es muy similar a cómo una persona ordena cartas en la mano: toma una carta nueva y la inserta en el lugar que le corresponde entre las que ya tiene ordenadas.

### Rendimiento

* **Mejor caso O(n):** arreglo ya ordenado (cada elemento se compara solo una vez con su vecino y no requiere desplazamientos).
* **Peor caso O(n²):** arreglo ordenado en orden inverso (cada elemento debe desplazarse hasta el inicio).
* **Espacio O(1):** in-place.
* **Estable:** sí, ya que un elemento solo se inserta antes de otro si es estrictamente menor, preservando el orden entre iguales.
* Es especialmente eficiente para arreglos **pequeños** o **casi ordenados**; muchos algoritmos híbridos (como Timsort, usado internamente por Python) lo utilizan para sub-arreglos pequeños.

### Código en Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = actual
    return arr

print(insertion_sort([5, 2, 9, 1, 5, 6]))
```

---

## Quicksort

### Funcionamiento

Algoritmo de tipo **divide y vencerás**. Selecciona un elemento como **pivote**, y reorganiza (particiona) el arreglo de modo que todos los elementos menores al pivote queden a su izquierda, y los mayores a su derecha. Luego se aplica recursivamente el mismo proceso a las dos sub-particiones.

* La elección del pivote es crítica para el rendimiento: elegir siempre el primer o último elemento en un arreglo ya ordenado genera el peor caso.
* Estrategias comunes para elegir el pivote: primer elemento, último elemento, elemento del medio, o un elemento aleatorio (esta última reduce drásticamente la probabilidad del peor caso).

### Rendimiento

* **Mejor y caso promedio O(n log n):** cuando el pivote divide el arreglo en partes razonablemente balanceadas.
* **Peor caso O(n²):** cuando el pivote elegido resulta ser siempre el menor o el mayor elemento (por ejemplo, un arreglo ya ordenado con pivote = primer elemento), generando particiones muy desbalanceadas.
* **Espacio O(log n):** no requiere un arreglo auxiliar completo (es in-place), pero sí espacio en el stack de llamadas recursivas.
* **No estable:** los intercambios durante la partición pueden alterar el orden relativo de elementos iguales.
* Es, en la práctica, uno de los algoritmos de ordenamiento **más rápidos** para uso general, gracias a su buen uso de la caché y bajo overhead por comparación.

### Código en Python

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)

print(quicksort([5, 2, 9, 1, 5, 6]))
```

---

## Mergesort (Ordenamiento por Mezcla)

### Funcionamiento

También es **divide y vencerás**. Divide el arreglo repetidamente a la mitad hasta llegar a sub-arreglos de un solo elemento (caso base, ya ordenado por definición), y luego **mezcla (merge)** dichos sub-arreglos de dos en dos, combinándolos en orden, hasta reconstruir el arreglo completo ya ordenado.

* El paso clave es la función `merge`, que combina dos listas ya ordenadas en una sola lista ordenada, comparando siempre el elemento más pequeño disponible de cada una.

### Rendimiento

* **Todos los casos O(n log n):** siempre divide el arreglo a la mitad (log n niveles) y siempre mezcla todos los elementos en cada nivel (n operaciones por nivel), sin importar el orden inicial; por eso **no es adaptativo**.
* **Espacio O(n):** requiere arreglos auxiliares para realizar la mezcla, por lo que **no es in-place** en su implementación estándar.
* **Estable:** sí, siempre que en el `merge` se elija primero el elemento de la lista izquierda cuando hay un empate, preservando el orden original.
* Es el algoritmo preferido cuando se necesita **garantizar** O(n log n) sin importar el caso (a diferencia de Quicksort), y es muy usado para ordenar **listas enlazadas** o datos externos (como archivos que no caben en memoria).

### Código en Python

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:  # <= preserva estabilidad
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

print(merge_sort([5, 2, 9, 1, 5, 6]))
```

---

## Heapsort

### Funcionamiento

Utiliza la estructura de datos **Heap** (vista anteriormente) para ordenar. Consta de dos fases:

1. **Heapify:** se convierte el arreglo completo en un Heap Máximo (complejidad O(n), como se explicó en el tema de Heaps).
2. **Extracción:** se intercambia repetidamente la raíz del heap (el elemento máximo) con el último elemento del heap "activo", se reduce el tamaño del heap en uno, y se aplica un `sift-down`/`bubble-down` para restaurar la propiedad de heap. Este proceso se repite hasta que el heap queda vacío, dejando el arreglo completamente ordenado.

### Rendimiento

* **Todos los casos O(n log n):** el Heapify inicial es O(n), y cada una de las `n` extracciones cuesta O(log n) para restaurar el heap; por eso **no es adaptativo**, su comportamiento es igual sin importar el orden inicial.
* **Espacio O(1):** in-place, ya que el heap se construye directamente sobre el mismo arreglo (representado como vector, tal como se vio en el tema de Heaps).
* **No estable:** los intercambios entre la raíz y elementos lejanos del arreglo pueden alterar el orden relativo de elementos iguales.
* Es una excelente opción cuando se necesita **O(n log n) garantizado** junto con **espacio O(1)**, algo que ni Quicksort (peor caso O(n²)) ni Mergesort (espacio O(n)) logran combinar al mismo tiempo.

### Código en Python

```python
def heapify(arr, n, i):
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq
    if der < n and arr[der] > arr[mayor]:
        mayor = der

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)  # Bubble-down recursivo

def heap_sort(arr):
    n = len(arr)

    # Construir el Heap Máximo (Heapify)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Mover raíz al final
        heapify(arr, i, 0)               # Restaurar heap con tamaño reducido

    return arr

print(heap_sort([5, 2, 9, 1, 5, 6]))
```

---

## Counting Sort (Ordenamiento por Conteo)

### Funcionamiento

A diferencia de los anteriores, **no compara elementos entre sí**; en su lugar, cuenta cuántas veces aparece cada valor dentro de un rango conocido, y usa esa información para colocar directamente cada elemento en su posición final.

**Pasos:**
1. Se crea un arreglo auxiliar de conteo, de tamaño igual al rango de valores posibles (`k`).
2. Se recorre el arreglo original, incrementando el contador correspondiente a cada valor.
3. Se transforma el arreglo de conteo en **conteo acumulado** (cada posición indica cuántos elementos son menores o iguales a ese valor).
4. Se recorre el arreglo original (de derecha a izquierda, para mantener estabilidad) y se coloca cada elemento en su posición final según el conteo acumulado.

### Rendimiento

* **Todos los casos O(n + k):** donde `k` es el rango de valores posibles; si `k` es muy grande comparado con `n`, el algoritmo deja de ser eficiente.
* **Espacio O(n + k):** requiere el arreglo de conteo (tamaño k) y el arreglo de salida (tamaño n); **no es in-place**.
* **Estable:** sí, siempre que se recorra el arreglo original de derecha a izquierda al momento de ubicar los elementos en su posición final.
* **No aplica comparaciones**, por lo que puede superar la barrera teórica de O(n log n) que tienen los algoritmos basados en comparación; sin embargo, solo funciona bien con **números enteros dentro de un rango conocido y razonablemente pequeño**.

### Código en Python

```python
def counting_sort(arr):
    if not arr:
        return arr
    
    maximo = max(arr)
    minimo = min(arr)
    rango = maximo - minimo + 1
    
    conteo = [0] * rango
    salida = [0] * len(arr)
    
    # Contar ocurrencias
    for numero in arr:
        conteo[numero - minimo] += 1
    
    # Conteo acumulado
    for i in range(1, rango):
        conteo[i] += conteo[i - 1]
    
    # Colocar en posición final (de derecha a izquierda: estabilidad)
    for i in range(len(arr) - 1, -1, -1):
        numero = arr[i]
        conteo[numero - minimo] -= 1
        salida[conteo[numero - minimo]] = numero
    
    return salida

print(counting_sort([5, 2, 9, 1, 5, 6]))
```

---

## Radix Sort

### Funcionamiento

También evita comparaciones directas entre elementos completos; en su lugar, ordena los números procesando sus **dígitos**, de menor a mayor significancia (LSD - *Least Significant Digit first*), utilizando **Counting Sort como subrutina estable** en cada pasada.

**Pasos:**
1. Se determina el número con más dígitos, para saber cuántas pasadas se necesitan.
2. Se ordena el arreglo según el dígito de las unidades (usando Counting Sort).
3. Se vuelve a ordenar (sobre el resultado anterior) según el dígito de las decenas.
4. Se repite el proceso para centenas, millares, etc., hasta cubrir el dígito más significativo.

> Es fundamental que el Counting Sort usado en cada pasada sea **estable**, ya que Radix Sort depende de que el orden logrado en pasadas anteriores (dígitos menos significativos) se preserve al ordenar por los dígitos más significativos.

### Rendimiento

* **Todos los casos O(n·k):** donde `k` es la cantidad de dígitos (o pasadas) necesarias; si `k` es pequeño y constante, se comporta esencialmente como O(n).
* **Espacio O(n + k):** requiere estructuras auxiliares similares a Counting Sort en cada pasada; **no es in-place**.
* **Estable:** sí, siempre y cuando la subrutina de ordenamiento por dígito (Counting Sort) también lo sea.
* Es muy usado para ordenar **grandes cantidades de enteros** o **cadenas de longitud fija**, superando en la práctica a los algoritmos basados en comparación cuando la cantidad de dígitos es baja.

### Código en Python

```python
def counting_sort_por_digito(arr, exp):
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10  # Dígitos van de 0 a 9

    for numero in arr:
        digito = (numero // exp) % 10
        conteo[digito] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    for i in range(n - 1, -1, -1):
        digito = (arr[i] // exp) % 10
        conteo[digito] -= 1
        salida[conteo[digito]] = arr[i]

    return salida

def radix_sort(arr):
    if not arr:
        return arr
    
    maximo = max(arr)
    exp = 1
    while maximo // exp > 0:
        arr = counting_sort_por_digito(arr, exp)
        exp *= 10
    
    return arr

print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
```

---

## Resumen comparativo — ¿Cuándo usar cuál?

* **Burbuja / Selección / Inserción:** solo recomendables para conjuntos de datos **muy pequeños**, con fines educativos, o cuando el arreglo ya está casi ordenado (Inserción y Burbuja son adaptativos).
* **Quicksort:** la opción más rápida en la práctica para uso general, cuando no se requiere estabilidad y se puede tolerar (o mitigar con pivote aleatorio) el riesgo del peor caso O(n²).
* **Mergesort:** cuando se necesita **garantizar** O(n log n) sin importar el caso, se requiere **estabilidad**, o se trabaja con estructuras como listas enlazadas o datos que no caben en memoria (ordenamiento externo).
* **Heapsort:** cuando se necesita O(n log n) garantizado **y** memoria O(1) al mismo tiempo (sacrificando estabilidad).
* **Counting Sort / Radix Sort:** cuando los datos son enteros dentro de un rango conocido y acotado, permitiendo superar la barrera de O(n log n) propia de los algoritmos basados en comparación.

## Tabla comparativa

<img width="700" alt="image" src="https://github.com/user-attachments/assets/1cacb05d-177f-4b9b-bda8-239dc53a4eb5" />

