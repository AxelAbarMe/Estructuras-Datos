# Quiz 1

> Temas: Arquitectura monolítica vs Microservicios, segmentos de memoria, git, compilador vs intérpretes, ARM vs x86, tipos de archivos y su rendimiento y TDA lineales (Vector, Lista enlazada, Pila, Cola)

## Instrucciones
* En esta evaluación, usted debe responder una pregunta y continuar con la siguiente. No puede devolverse ni revisar las preguntas al final del cuestionario.
* Una vez que comience el quiz, corre el tiempo para resolverlo. En caso de que se cierre el navegador, puede volver a retomar el quiz y las preguntas que ya haya contestado se mantendrán.
* En las preguntas de selección multiple (cuando tienen que seleccionar dos o más opciones):
  - Revisen bien en el enunciado cuántas respuestas tienen que seleccionar
  - Cada respuesta correcta equivale a un punto adicional, mientras que cada respuesta incorrecta equivale a un punto menos (se resta).

## Pregunta 1
El segmento de código de un programa se puede modificar en tiempo de ejecución.

* Verdadero
* Falso

> Respuesta Correcta: Falso

## Pregunta 2
¿Cuál es el impacto principal del paso de una arquitectura monolítica a una de microservicios?

* Refuerza el uso de un solo lenguaje de programación
* Elimina la necesidad de pruebas automatizadas
* Simplifica la estructura de datos interna del sistema
* Permite desplegar componentes independientemente y escalar de manera modular

> Respuesta Correcta: Permite desplegar componentes independientemente y escalar de manera modular

## Pregunta 3
¿Cuáles opciones describen las situaciones en las cuales se da un memory leak en un programa? (Seleccione 2)

* Cuando no se libera la memoria asignada
* Cuando no existe más espacio disponible en el stack
* A la hora de hacer "delete" a un espacio de memoria que no se había definido con anterioridad
* Cuando se desreferencia un apuntador a NULL
* Cuando se pierde la referencia a la dirección de memoria devuelta por new

> Respuesta Correcta: Cuando no se libera la memoria asignada
> Respuesta Correcta: Cuando se pierde la referencia a la dirección de memoria devuelta por new

## Pregunta 4
Un memory leak ocurre en tiempo de compilación

* Verdadero
* Falso

> Respuesta Correcta: Falso

## Pregunta 5
Considere el siguiente código en Python:

```python
my_list = [2, 4, 6]
for i in range(5):
    my_list[i] = my_list[i] + i
```
¿Cuál es el valor de my_list justo antes de que ocurra la excepción IndexError? Proporcione el valor en el cuadro de texto en formato de lista (por ejemplo, [1, 2, 3])

> Respuesta Correcta: [2, 5, 8]

## Pregunta 6

Considere el siguiente código en Python:

```python
sentence = "Trust the debugger"
words = sentence.split()
result = ""

for i in range(len(words)):
    token = words[i]
    if i == 0:

        result += token[::-1].capitalize()
    elif i == 1:
        result += token[::-1].upper()
    else:
        result += token[::-1]

    result += "-"
```
¿Cuál valor es el valor de i cuando result es igual a "Tsurt-EHT-reggubed-"?

> Respuesta Correcta: 2

## Pregunta 7
Cuál comando permite copiar un repositorio remoto en Github a la computadora local?

* git commit
* git clone
* git fetch
* git pull
* git status

> Respuesta Correcta: git clone

## Pregunta 8

Considere el siguiente código en Python:

```python
flags = [True, True, False, True, False, True]
value = 20

for idx, f in enumerate(flags):
    if f or value % 4 == 0:
        value += idx
    else:
        value = value // 2
```
¿Cuál valor se asigna a value en la primera iteración en la que f es igual a False? 

> Respuesta Correcta: 10

## Pregunta 9
¿Cuál de las siguientes características distingue a un compilador respecto a un intérprete?

* Genera un archivo binario ejecutable antes de la ejecución
* Proporciona retroalimentación nmediata al programador
* Es más útil para entornos interactivos como Python
* Traduce el código línea por línea en tiempo de ejecución

> Respuesta Correcta: Genera un archivo binario ejecutable antes de la ejecución

## Pregunta 10

Considere el siguiente código en Python:

```python
x = 0
for i in range(7):  # i from 0 to 6
    if i % 2 == 0:
        x += i
    else:
        x -= (i * 2)
```
¿Cuál es el valor de x al finalizar la quinta iteración?

> Respuesta Correcta: -2

## Pregunta 11

Considere el siguiente código en Python:

```python
s = "debugging"
result = ""
for i in range(len(s)):
    if i % 2 == 0:
        result = s[i] + result
    else:
        result = result + s[i]
```
¿Cuál es el valor de i cuando result es igual a "igbdeug"?

> Respuesta Correcta: 6

## Pregunta 12
Arrastre cada cuadro de texto en el lugar que corresponda de acuerdo con la imagen, de manera que describa correctamente la funcionalidad de cada segmento de memoria

> STACK: Variables automáticas
> 
> HEAP: Memoria dinámica
> 
> DATOS (.bss): Variables estáticas sin inicializar
> 
> DATOS (.data): Variables globales inicializadas
> 
> CÓDIGO (.text): Instrucciones

## Pregunta 13
¿Cuál sería una razón técnica por la cual un lenguaje interpretado podría ser más lento que uno compilado?

* El intérprete ejecuta directamente el código fuente con cada instrucción
* Los intérpretes realizan optimización en tiempo de compilación
* Los compiladores requieren más recursos en tiempo de ejecución
* Los lenguajes compilados no requieren estructuras de datos

> Respuesta Correcta: El intérprete ejecuta directamente el código fuente con cada instrucción

## Pregunta 14
¿Cuáles de los siguientes beneficios técnicos se derivan de una adopción bien planificada de microservicios y APIs? (Seleccione 2)

* Despliegue independiente
* Limita a las aplicaciones a ejecutarse en servidores físicos
* Mayor facilidad de diseño de las aplicaciones y bases de datos
* Escalabilidad por servicio
* Alto acomplamiento entre módulos

> Respuesta Correcta: Despliegue independiente
> Respuesta Correcta: Escalabilidad por servicio

## Pregunta 15
¿Cuál de las siguientes afirmaciones es falsa?

* La cache L1 es más rápida que la cache L2
* La velocidad de lectura/escritura de un disco HDD es más lenta que un SSD
* La RAM tiene menor latencia que la cache L3
* El acceso a disco duro es más lento que a la memoria RAM
* Existe una cache L2 por cada núcleo de un CPU x86-64

> Respuesta Correcta: La RAM tiene menor latencia que la cache L3
