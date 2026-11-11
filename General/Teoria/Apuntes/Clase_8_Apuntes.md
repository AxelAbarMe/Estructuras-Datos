# 8: Eficiencia

## Aspectos de la eficiencia

* **CPU (Tiempo)**
* **RAM (Espacio)**

> Uno de los aspectos de la eficiencia es el tiempo, y se mide a partir del CPU (tiempo de ejecución).

El CPU siempre tiene su arquitectura, velocidad y núcleos (datos variables). Es mala idea medir los algoritmos por el tiempo; se va a medir en cantidad de instrucciones, o sea, cuántas instrucciones deben ejecutarse para terminar el algoritmo. Cuando se habla de eficiencia, es cuál algoritmo le permite al CPU ejecutar menos cantidad de instrucciones.

| Alg A | Alg B | Info |
|:--:|:--:|:--:|
| - | - | Ambos hacen lo mismo |
| 1.075s | 4.348s | Tiempo de ejecución |

```python
def foo(x):
  res = x + 15
  print(res)
```

Observando el código, se puede ver que la instrucción de la suma siempre será la misma cantidad de instrucciones, da igual el valor que tome `x`; siempre durará lo mismo. Esto se llama **Tiempo constante**: `O(1)`.

<img src="https://miro.medium.com/1*ENAP16Z-YXbzEebQllXFYA.jpeg" Alt="O()" width="500">

Con base en los datos de entrada, así se comporta el algoritmo en el tiempo. Complejidad, análisis de algoritmos, complejidad algorítmica [O(1) u otros]: se busca que se acerque lo más posible a O(1).

* **Cota Superior:** cuando el algoritmo se comporta de peor manera.
* **Cota promedio:** cuando el algoritmo corre en un caso intermedio.
* **Cota inferior:** cuando el algoritmo se comporta de mejor manera.

> **Nota adicional:** formalmente estas tres cotas tienen su propia notación matemática: **Big-O (O)** para la cota superior (lo que se usa casi siempre en la práctica), **Big-Omega (Ω)** para la cota inferior, y **Big-Theta (Θ)** cuando la cota superior e inferior coinciden (es decir, el algoritmo se comporta igual sin importar el caso).

## O Grande

Significa la cota superior; la cota promedio e inferior (Theta y Omega) se ignoran al no tener sentido para este análisis.

Pensando en un caso de ordenamiento: la cota inferior sería que ya esté ordenado, la cota promedio sería que hayan algunos ordenados y otros desordenados, y la cota superior es que todos estén desordenados (en la mayoría de los casos).

```python
def sumatoria(n):
  res=0
  for i in range(1,n+1):
    res = res+1
  return res
```

Observando el código, qué sucede cuando `n` vale:

* 1
* 10
* 100

Deja de ser constante; este algoritmo tendrá entonces una complejidad algorítmica **lineal**, o bien llamada `O(n)`.

La cantidad de ciclos permite facilitar el proceso de conocer cuál es la complejidad de un algoritmo.

```python
def foo(n):
  for i in range(1,n+1):   # O(n)
    ---
  print(n)
  ---
  ---
  for i in range(1,n+1):   # O(n)
    ---
  return
```

Observando el código, se tiene que cada uno de los ciclos corresponde a O(n), mientras que el resto de instrucciones corresponde a O(1).

> O(n) + O(n) + O(1) + O(1) + O(1) + O(1)

Simplificando:

> O(2n) + O(4)

Al buscar la cota superior, se mantiene el O grande más grande, o sea, se elimina el O(4).

> O(2n)

Y además, las constantes factor de `n` se eliminan, ya que para entender el algoritmo en el tiempo, dichas constantes no afectan de gran manera el gráfico que dicho algoritmo realiza.

> O(n)

Si se mejora el O grande de un O(n) a un O(1), esto significa cambios en el tiempo de ejecución (cantidad de instrucciones que realiza el CPU), pero esto puede tener implicaciones en el espacio.

> **Nota adicional — Trade-off tiempo/espacio:** un ejemplo clásico de este trade-off es la **memoización**: guardar en una estructura auxiliar (como un diccionario) resultados ya calculados para no recalcularlos, mejorando drásticamente el tiempo (por ejemplo, Fibonacci pasa de O(2ⁿ) a O(n)) a cambio de consumir más memoria RAM para almacenar dichos resultados.

## Tipos de complejidad

* O(1) — Constante
* O(log n) — Logarítmica
* O(n) — Lineal
* O(n log n) — Lineal Logarítmica
* O(n²) — Cuadrática
---
> * Un ejemplo para O(log n) es la búsqueda binaria, donde se va disminuyendo por la mitad la cantidad de instrucciones; siempre que se reduzca a la mitad, es un O(log n). Ejemplo: búsqueda en árbol binario.
> * O(n) es cuando se tiene que ejecutar una operación por cada `n`. Ejemplo: búsqueda en lista enlazada.
> * Muchos ejemplos de O(n log n) están en los algoritmos de ordenamiento.
> * Y para O(n²), es cuando la cantidad de instrucciones se duplica según crece la entrada. Un ejemplo es el ordenamiento burbuja, o los `for` anidados.

Esos 5 tipos de complejidad son los más comunes y los más trabajados.

### Ejemplo de código — O(n²)

```python
def burbuja(n):
  for i in range(i, n+1):
    for j in range(j, n+1):
```

> **Nota adicional:** existe también la complejidad **O(2ⁿ) (exponencial)**, típica de algoritmos recursivos sin memoización (como el cálculo ingenuo de Fibonacci), y la **O(n!) (factorial)**, típica de problemas de fuerza bruta que prueban todas las permutaciones posibles (como el problema del vendedor viajero resuelto sin optimización).

### Tabla comparativa de crecimiento

Para dimensionar el impacto real de cada complejidad, esta tabla muestra aproximadamente cuántas instrucciones ejecutaría cada tipo de algoritmo según el tamaño de la entrada (`n`):

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 10 | 1 | ~3 | 10 | ~33 | 100 |
| 100 | 1 | ~7 | 100 | ~664 | 10.000 |
| 1.000 | 1 | ~10 | 1.000 | ~9.966 | 1.000.000 |

* Nótese cómo O(1) se mantiene constante sin importar cuánto crezca `n`, mientras que O(n²) crece de forma desproporcionada; esta es la razón principal por la que se busca evitar, siempre que sea posible, algoritmos con ciclos anidados sobre grandes volúmenes de datos.
* Esta comparación es también la justificación práctica de por qué, en el tema de TDA, se prefiere el **Acceso Directo O(1)** de un vector sobre el **O(n)** de recorrer una lista enlazada cuando se necesita buscar un elemento por posición.
