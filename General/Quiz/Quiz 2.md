# Quiz 2

> Temas: Vector, Lista enlazada, Pila, Cola (TDA lineales)

## Instrucciones
* En esta evaluación, usted debe responder una pregunta y continuar con la siguiente. No puede devolverse ni revisar las preguntas al final del cuestionario.
* Una vez que comience el quiz, corre el tiempo para resolverlo. En caso de que se cierre el navegador, puede volver a retomar el quiz y las preguntas que ya haya contestado se mantendrán.
* En las preguntas de selección multiple (cuando tienen que seleccionar dos o más opciones):
  - Revisen bien en el enunciado cuántas respuestas tienen que seleccionar
  - Cada respuesta correcta equivale a un punto adicional, mientras que cada respuesta incorrecta equivale a un punto menos (se resta).

## Pregunta 1
¿Cuál es una de las ventajas de mantener una estructura en un esquema de asignación contigua de memoria?

* Se puede expandir sin necesidad de realizar reubicación de memoria
* Acceso directo a los elementos
* Permite crear objetos bajo demanda
* No es necesario conocer cuánta memoria asignar previamente

> Respuesta Correcta: Acceso directo a los elementos

## Pregunta 2
¿Cuáles de las siguientes opciones muestran ventajas de una lista enlazada con respecto a un arreglo unidimensional con asignación contigua de memoria? (Seleccione 2)

* Permiten acceso aleatorio a los elementos
* Permiten búsquedas en el orden de O(log n)
* Hace un uso más eficiente de recursos cuando se requieren modificaciones
* Tienen una menor utilización de memoria
* No tiene ningún límite en su tamaño

> Respuesta Correcta: Hace un uso más eficiente de recursos cuando se requieren modificaciones
> Respuesta Correcta: No tiene ningún límite en su tamaño

## Pregunta 3
La asignación de memoria para los nodos de una lista enlazada se realiza de manera contigua

* Verdadero
* Falso

> Respuesta Correcta: Falso

## Pregunta 4
Considere una aplicación que requiere almacenar una gran cantidad de información sin ordenar y principalmente se van a realizar inserciones y búsquedas lineales. La memoria disponible en RAM no alcanza para asignar la memoria de manera contigua.
Además, con el fin de optimizar el espacio disponible, la estructura de datos que se deberá implementar tendrá que utilizar una cantidad mínima de información para el funcionamiento de su estructura interna (overhead).
De acuerdo con el enunciado anterior, ¿cuál es la estructura de datos que mejor se adapta para utilizarla en la aplicación?

* Cola
* Lista enlazada doble
* Vector
* Lista enlazada simple
* Pila

> Respuesta Correcta: Lista enlazada simple

## Pregunta 5

¿Cuál componente de hardware se encarga de la ejecución de las instrucciones de los programas?

* SSD
* CPU
* Cache
* RAM
* HDD

> Respuesta Correcta: CPU

## Pregunta 6

Una cola es una estructura de datos de tipo `     ` mientras que una pila es de tipo `     `


> Respuesta Correcta: FIFO
> 
> Respuesta Correcta: LIFO


## Pregunta 7
¿Qué diferencia a un vector de una lista enlazada?

* En que en un vector no aplica aritmética de punteros
* En que el acceso en la lista es más lento
* La cantidad de elementos total
* La manera en que se asigna la memoria
* El tipo de datos que almacenan

> Respuesta Correcta: La manera en que se asigna la memoria

## Pregunta 8
¿Cuáles son las operaciones de una pila (stack)? (Seleccione 2)

* enqueue
* pop
* dequeue
* top
* push

> Respuesta Correcta: pop
> 
> Respuesta Correcta: push

## Pregunta 9
Asocie cada definición con la estructura de datos que corresponda. No todas las opciones se utilizan, pero sí se pueden repetir.

> FIFO: Cola
>
> Acceso Aleatorio: Vector
>
> Acceso secuencial a los elementos: Lista Enlazada Simple
>
> LIFO: Pila
