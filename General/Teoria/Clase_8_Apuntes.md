# Eficiencia

### CPU (Tiempo)
### RAM (Espacio)

> Uno de los aspectos de la eficiencia es el tiempo, se mide a partir del CPU (Tiempo de ejecución)

CPU siempre tiene su arquitectura, velocidad, núcleos (Datos variables). Es mala idea medir los algoritmos por el tiempo. Se va a medir en cantidad de instrucciones, ósea cuantas instrucciones deben ejecutarse para terminar el algoritmo. Cuando se habla de eficiencia es el que cuál le permite al CPU ejecutar menos cantidad de instrucciones.

|Alg A|Alg B|Info|
|:--:|:--:|:--:|
|-|-|Ambos hacen lo mismo|
|1.075s|4.348s|Tiempo de ejecución|


```python
def foo(x):
  res = x + 15
  print(res)
```

Observando el código, se puede ver que la instrucción de la suma, siempre será la misma cantidad de instrucciones da igual el valor que tome x, siempre durará lo mismo, llamado `Tiempo constante`. O(1)

<img src="https://miro.medium.com/1*ENAP16Z-YXbzEebQllXFYA.jpeg" Alt="O()" width="500">

Con base a los datos de entrada, como se comporta el algoritmo en el tiempo.

Complejidad, análisis de algoritmos, complejidad algorítmica. [O(1) u otros]. Se busca que se acerque lo más posible a O(1).

* Cota Superior: Cuando el algoritmo se comporta de peor manera.
* Cota promedio: Cuando el algoritmo corre
* Cota inferior: Cuando el algoritmo se comporta de mejor manera.

## O Grande

Significa la cota superior, la cota promedio e inferior (Theta y Omega) se ignoran al no tener sentido.

Pensando en un caso de ordenamiento, la cota inferior sería que este ordenado, la cota promedio seria que hayan algunos ordenados y otros desordenados y cota superior es que todos estén desordenados (En la mayoría de los casos).

```python
def sumatoria(n):
  res=0
  for i in range(1,n+1)
    res = res+1
  return res
```

Observando el código, que sucede cuando n vale:
* 1
* 10
* 100

Deja de ser constante, este algoritmo tendrá entonces una complejidad algorítmica `lineal` o bien llamada `O(n)`

La cantidad de ciclos permiten facilitar el proceso de conocer cuál es la complejidad de un algorito.

```python
def foo(n):
  for i in range(1,n+1)   O(n)
    ---
  print(n)
  ---
  ---
  for i in range(1,n+1)   O(n)
    ---
  return
```

Observando el código, se tiene que los ciclos cada uno corresponde a O(n), mientras que el resto de instrucciones corresponde a O(1).

> O(n) + O(n) + O(1) + O(1) + O(1) + O(1)

Simplificando:

> O(2n) + O(4)

Al buscar la cota superior, se mantiene el O grande más grande, ósea se elimina el O(4).

> O(2n)

Y además, las constantes factor de n se eliminan, ya que para entender el algoritmo en el tiempo, dichas constantes no afectan de gran manera en el gráfico que dicho algoritmo realiza.

> O(n)

Si se mejora el O grande de un O(n) a un O(1) esto significa cambios en el tiempo de ejecución de la cantidad de instrucciones que realiza el CPU, pero esto puede tener implicaciones en el espacio.

## Tipos de complejidad

* O(1) Constante
* O(log n) Logarítmica
* O(n) Lineal
* O(n log n) Lineal Logarítmica
* O(n^2) Cuadrática

Un ejemplo para O(log n) es la búsqueda binaria, donde se va disminuyendo por la mitad la cantidad de instrucciones, siempre que se reduzca a la mitad es un O(log n). Búsqueda en árbol binario.

O(n) es cuando se tiene que ejecutar una operación por cada n. Búsqueda en lista enlazada

Muchos ejemplos de O(n log n) en ordenamientos

Y para O(n^2) es cuando la cantidad de instrucciones se duplican. Un ejemplo es el ordenamiento burbuja o los for anidados

Esos 5 tipos de complejidad son los más comunes y los más trabajados.

### Ejemplo Código (O(n^2))

```python
def burbuja(n):
  for i in range(i, n+1)
    for j in range(j, n+1)
```

