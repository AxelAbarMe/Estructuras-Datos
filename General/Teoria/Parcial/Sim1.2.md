# Examen de Simulacro 2

> **Temas:** Arquitecturas de Software, Gestión de Memoria, Herramientas y Metodologías (Git, Debugger, TDD/Spec), Manejo de Archivos, Tipos de Datos Abstractos (Vectores, Listas, Pilas, Colas), Recursión, Complejidad Algorítmica (Big-O), Heaps, Colas de Prioridad y Algoritmos de Ordenamiento.

---

## Bloque I: Enunciados Complejos y Código

### Enunciado A (Preguntas 1 a 4)

Considere el siguiente snippet en Python que procesa una lista de valores numéricos de entrada:

```python
def algoritmo_x(arr):
    n = len(arr)
    pasos_comparacion = 0
    pasos_intercambio = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            pasos_comparacion += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            pasos_intercambio += 1
    return pasos_comparacion, pasos_intercambio

datos = [9, 3, 7, 1, 5]
```

**1.** ¿Qué algoritmo de ordenamiento implementa la función `algoritmo_x`?

[ ] a) Ordenamiento por Inserción (Insertion Sort)  

[ ] b) Ordenamiento por Selección (Selection Sort)  

[ ] c) Ordenamiento Burbuja (Bubble Sort)  

[ ] d) Quicksort

**2.** Si ejecutamos la función pasando `datos = [9, 3, 7, 1, 5]`, ¿cuál es el valor retornado para `pasos_comparacion`?

[ ] a) 5  

[ ] b) 8  

[ ] c) 10  

[ ] d) 20

**3.** Para el mismo arreglo `datos = [9, 3, 7, 1, 5]`, ¿cuántos intercambios reales de memoria (`pasos_intercambio`) se efectúan?

[ ] a) 2  

[ ] b) 3  

[ ] c) 4  

[ ] d) 10

**4.** En el peor de los casos para un arreglo de tamaño $n$, ¿cuál es el número máximo posible de intercambios que realiza esta implementación?

[ ] a) $n - 1$  

[ ] b) $(n^2 - n) / 2$  

[ ] c) $n \log n$  

[ ] d) $n^2$

---

### Enunciado B (Preguntas 5 a 8)

Considere la siguiente función recursiva y su monitoreo en el Call Stack:

```python
def rastrear(n):
    if n <= 0:
        return ""
    if n % 2 == 0:
        return rastrear(n // 2) + "X"
    else:
        return "Y" + rastrear(n - 1)
```

**5.** Al ejecutar `rastrear(6)`, ¿cuántas llamadas a la función `rastrear` se apilan en total en el Call Stack antes de comenzar a retornar?

[ ] a) 3  

[ ] b) 4  

[ ] c) 5  

[ ] d) 6

**6.** ¿Cuál es el valor exacto que retorna la llamada `rastrear(6)`?

[ ] a) YXX  

[ ] b) YXX  

[ ] c) YX  

[ ] d) YXXY

**7.** ¿Qué registro interno del CPU modifica su valor con cada instrucción ejecutada dentro de una llamada del Call Stack?

[ ] a) RSP (Stack Pointer)  

[ ] b) RIP (Instruction Pointer)  

[ ] c) ALU  

[ ] d) BSS

**8.** Si se remueve el caso base `if n <= 0: return ""`, ¿qué error se produciría en tiempo de ejecución?

[ ] a) Memory Leak en el Heap  

[ ] b) Out of Memory por saturación de BSS  

[ ] c) Stack Overflow (RecursionError en Python)  

[ ] d) Error de compilación en Linker

---

### Enunciado C (Preguntas 9 a 12)

Dado un Binary Heap Máximo representado en memoria sobre un arreglo como:

`heap = [95, 80, 75, 60, 50, 70, 40]`

**9.** De acuerdo con las reglas de cálculo en arreglos, ¿cuál es el hijo derecho del nodo ubicado en el índice 1 (valor 80)?

[ ] a) 75  

[ ] b) 60  

[ ] c) 50  

[ ] d) 70

**10.** Si insertamos el valor `100` al final de la estructura e invocamos `bubble_up`, ¿cuál será el arreglo final resultante?

[ ] a) `[100, 95, 75, 80, 50, 70, 40, 60]`  

[ ] b) `[100, 80, 75, 95, 50, 70, 40, 60]`  

[ ] c) `[95, 80, 75, 60, 50, 70, 40, 100]`  

[ ] d) `[100, 95, 80, 75, 60, 50, 70, 40]`

**11.** Tras la inserción de `100` y el reordenamiento, ¿cuál es el nuevo padre del elemento que contiene el valor `80`?

[ ] a) 100  

[ ] b) 95  

[ ] c) 75  

[ ] d) 60

**12.** ¿Cuál es la complejidad temporal de la operación de eliminación de la raíz en este heap restaurado?

[ ] a) $O(1)$  

[ ] b) $O(\log n)$  

[ ] c) $O(n)$  

[ ] d) $O(n \log n)$

---

## Bloque II: Preguntas Directas, de Razonamiento y Análisis de Código

**13.** Un programa compilado para una arquitectura x86-64 no puede ejecutarse directamente en un procesador ARM debido a que:

[ ] a) ARM no posee memoria RAM.  

[ ] b) El código máquina/instrucciones del binario son específicos de la arquitectura de la CPU.  

[ ] c) La memoria virtual en ARM solo procesa texto plano.  

[ ] d) x86-64 no utiliza registros de segmento.

**14.** En el espacio de direcciones de un programa en memoria RAM, ¿en qué segmento se ubican las variables globales declaradas que NO poseen valor asignado inicialmente?

[ ] a) `.text`  

[ ] b) `.data`  

[ ] c) `.bss`  

[ ] d) Heap

**15.** ¿Qué ventaja principal ofrece la arquitectura de Microservicios frente a un Monolito?

[ ] a) Elimina la necesidad de utilizar bases de datos.  

[ ] b) Cada servicio se puede escalar e implementar de forma independiente mediante contenedores.  

[ ] c) Garantiza que el código no requiera compilación.  

[ ] d) Reduce el uso de memoria a nivel de ALU.

**16.** En un lenguaje compilado como C++, ¿cuál es la función del Linker?

[ ] a) Traducir el código a bytecode de Java.  

[ ] b) Unir los archivos objeto (`.obj`) con las bibliotecas necesarias para generar el ejecutable.  

[ ] c) Ejecutar el código línea por línea controlando el temporizador.  

[ ] d) Asignar memoria estática en la pila del sistema.

**17.** ¿Por qué los programas en Java son considerados portables entre distintas arquitecturas físicas?

[ ] a) Porque se compilan a un formato binario x86 directo.  

[ ] b) Porque generan Bytecode que se ejecuta sobre una Máquina Virtual (JVM).  

[ ] c) Porque no hacen uso del segmento Heap.  

[ ] d) Porque convierten automáticamente sus instrucciones a texto UTF-8.

**18.** ¿Qué diferencia principal existe entre los comandos `git merge` y `git rebase` al integrar cambios de ramas?

[ ] a) `merge` borra el historial de commits y `rebase` no.  

[ ] b) `merge` conserva el historial de ambas ramas mediante un commit de unión; `rebase` reescribe el historial en una línea recta.  

[ ] c) `rebase` solo funciona con servidores remotos.  

[ ] d) No hay diferencia técnica.

**19.** En la metodología TDD (Test-Driven Development), ¿cuál es la secuencia correcta del ciclo de desarrollo?

[ ] a) Refactor -> Green -> Red  

[ ] b) Green -> Red -> Refactor  

[ ] c) Red -> Green -> Refactor  

[ ] d) Code -> Test -> Deploy

**20.** Al utilizar un debugger, ¿cuál es el comportamiento de la opción **Step Over** (F10)?

[ ] a) Entra en la función invocada para ejecutarla paso a paso.  

[ ] b) Ejecuta la línea actual y, si hay una llamada a función, la completa sin entrar a su detalle interno.  

[ ] c) Detiene la ejecución de todo el programa inmediatamente.  

[ ] d) Remueve todos los breakpoints activos.

**21.** ¿Por qué el almacenamiento de datos en archivos binarios suele ser más eficiente que en archivos de texto plano?

[ ] a) Los archivos binarios evitan hacer uso del bus de datos.  

[ ] b) Almacenan los valores en su representación nativa en bytes sin necesidad de conversiones a caracteres.  

[ ] c) Los archivos de texto consumen $O(n^2)$ de CPU.  

[ ] d) Los archivos binarios solo pueden guardarse en memoria Caché.

**22.** ¿Qué característica hace al formato UTF-8 el más utilizado actualmente para la codificación de caracteres en la web?

[ ] a) Es una codificación fija de 32 bits por carácter.  

[ ] b) Es de tamaño variable y compatible hacia atrás con el estándar ASCII (1 byte para los primeros 128 caracteres).  

[ ] c) Ocupa menos espacio que el formato binario puro en todos los casos.  

[ ] d) No requiere decodificación en la memoria RAM.

**23.** ¿Qué modo de apertura en Python se debe utilizar para agregar información al final de un archivo existente sin borrar su contenido anterior?

[ ] a) `'r+'`  

[ ] b) `'w'`  

[ ] c) `'a'`  

[ ] d) `'wb+'`

**24.** Analice la función en Python sobre listas enlazadas:

```python
def misterio(head):
    actual = head
    while actual and actual.next:
        actual.next = actual.next.next
        actual = actual.next
```

¿Qué efecto produce la ejecución de esta función sobre la lista recibida?

[ ] a) Invierte la lista enlazada por completo.  

[ ] b) Elimina los nodos en posiciones pares de la lista (asumiendo base 1 para el segundo nodo).  

[ ] c) Duplica los nodos de la lista.  

[ ] d) Transforma la lista en un ciclo.

**25.** ¿Cuál es la ventaja de la estrategia de "Expansión x2" (duplicar la capacidad) en arreglos dinámicos al superar el límite inicial?

[ ] a) Garantiza que el arreglo sea in-place.  

[ ] b) Amortiza el costo de las inserciones a $O(1)$ en promedio.  

[ ] c) Evita el uso del segmento Heap.  

[ ] d) Permite realizar búsquedas binarias en listas desordenadas.

**26.** ¿Qué estructura de datos es la ideal para implementar la funcionalidad "Deshacer" (Undo) en un procesador de textos?

[ ] a) Queue (Cola)  

[ ] b) Binary Heap  

[ ] c) Stack (Pila)  

[ ] d) Lista Doblemente Enlazada sin tope

**27.** ¿Cuál es la complejidad temporal de la operación de inserción (`enqueue`) en una Cola respaldada por una lista enlazada simple con punteros a `front` y `rear`?

[ ] a) $O(1)$  

[ ] b) $O(\log n)$  

[ ] c) $O(n)$  

[ ] d) $O(n^2)$

**28.** ¿Qué diferencia fundamental existe entre una Lista Doblemente Enlazada y una Lista Simple?

[ ] a) La doble permite acceso aleatorio en $O(1)$.  

[ ] b) Cada nodo en la lista doble posee una referencia adicional (`prev`) al nodo anterior.  

[ ] c) La lista simple consume más memoria por nodo.  

[ ] d) La lista simple no requiere memoria del Heap.

**29.** Considere el siguiente código sobre un TDA Pila:

```python
s = Stack()
s.push(10)
s.push(20)
s.push(30)
x = s.pop()
s.push(40)
y = s.pop()
```

¿Cuáles son los valores guardados en `x` y `y` respectivamente?

[ ] a) $x = 10, y = 20$  

[ ] b) $x = 30, y = 40$  

[ ] c) $x = 30, y = 20$  

[ ] d) $x = 10, y = 40$

**30.** Un "Overhead" de memoria elevado en una estructura de datos se refiere a:

[ ] a) La cantidad excesiva de tiempo de CPU requerida.  

[ ] b) El consumo de memoria adicional asignado a metadatos o punteros de control y no a los datos reales.  

[ ] c) La fuga de memoria (Memory Leak) producida por variables globales.  

[ ] d) La saturación de la memoria Caché L1.

**31.** En el análisis de eficiencia algorítmica, la cota superior Big-O ($O$) representa:

[ ] a) El rendimiento esperado en el mejor de los casos.  

[ ] b) El límite del comportamiento del algoritmo en el peor de los casos.  

[ ] c) La exactitud matemática garantizada en casos promedio.  

[ ] d) La memoria consumida durante la compilación.

**32.** Si un algoritmo realiza $3n^2 + 15n + 100$ operaciones fundamentales, ¿cuál es su complejidad en notación Big-O simplificada?

[ ] a) $O(3n^2)$  

[ ] b) $O(n)$  

[ ] c) $O(n^2)$  

[ ] d) $O(100)$

**33.** ¿Cuál de las siguientes complejidades algorítmicas presenta la tasa de crecimiento de operaciones más rápida (menos eficiente) ante entradas grandes?

[ ] a) $O(n \log n)$  

[ ] b) $O(n^2)$  

[ ] c) $O(2^n)$  

[ ] d) $O(n!)$

**34.** La técnica de Memoización permite optimizar algoritmos recursivos al:

[ ] a) Reemplazar la pila por un vector estático.  

[ ] b) Almacenar en una estructura auxiliar los resultados de subproblemas precalculados para evitar recomputaciones.  

[ ] c) Eliminar los casos base.  

[ ] d) Convertir el código a binario.

**35.** ¿Por qué el algoritmo Fibonacci recursivo sin memoización presenta una complejidad de $O(2^n)$?

[ ] a) Porque realiza un ciclo `for` anidado sobre $n$.  

[ ] b) Porque cada llamada genera un árbol de dos llamadas recursivas redundantes que crece exponencialmente.  

[ ] c) Debido a la falta de punteros en la memoria.  

[ ] d) Por el costo de ordenamiento del arreglo.

**36.** En un Binary Heap Mínimo, ¿dónde se encuentra siempre ubicado el elemento con el valor menor de toda la estructura?

[ ] a) En la última hoja del nivel más profundo.  

[ ] b) En la posición raíz del árbol (índice 0 en la representación vectorial).  

[ ] c) En el hijo derecho de la raíz.  

[ ] d) Se requiere una búsqueda lineal $O(n)$ para ubicarlo.

**37.** ¿Qué algoritmo de ordenamiento es In-Place, garantiza una complejidad temporal de $O(n \log n)$ en el peor de los casos y utiliza un heap internamente?

[ ] a) Mergesort  

[ ] b) Quicksort  

[ ] c) Heapsort  

[ ] d) Counting Sort

**38.** ¿Cuál es el inconveniente principal de utilizar Mergesort frente a otros algoritmos como Heapsort sobre arreglos grandes en memoria RAM?

[ ] a) Su complejidad en el peor caso se degrada a $O(n^2)$.  

[ ] b) Requiere memoria adicional $O(n)$ para crear arreglos auxiliares de mezcla.  

[ ] c) No es un algoritmo estable.  

[ ] d) Modifica los punteros de la pila del CPU.

**39.** En el algoritmo Quicksort, la elección de un mal pivote (como el menor o mayor elemento de un arreglo ya ordenado) provoca que su tiempo de ejecución se degrade a:

[ ] a) $O(n \log n)$  

[ ] b) $O(n)$  

[ ] c) $O(n^2)$  

[ ] d) $O(\log n)$

**40.** ¿Qué algoritmo de ordenamiento NO se basa en la comparación de elementos y puede ordenar enteros en un rango acotado $k$ con tiempo $O(n + k)$?

[ ] a) Insertion Sort  

[ ] b) Counting Sort  

[ ] c) Selection Sort  

[ ] d) Quicksort

**41.** ¿Qué significa que un algoritmo de ordenamiento sea "Estable"?

[ ] a) Que consume siempre exactamente $1$ MB de memoria RAM.  

[ ] b) Que conserva el orden relativo original de los elementos que poseen claves o valores iguales.  

[ ] c) Que su mejor caso y peor caso tienen la misma representación Big-O.  

[ ] d) Que no utiliza recursión en su implementación.

**42.** ¿Cuál es la cantidad total de comparaciones que realiza Selection Sort sobre un arreglo de 5 elementos, independientemente de si está ordenado o no?

[ ] a) 4  

[ ] b) 10  

[ ] c) 25  

[ ] d) 2

**43.** Para ordenar un arreglo de tamaño $n$ que ya se encuentra completamente ordenado desde el inicio, ¿cuál algoritmo realiza únicamente $n - 1$ comparaciones?

[ ] a) Selection Sort  

[ ] b) Insertion Sort (con detección adaptativa)  

[ ] c) Quicksort tradicional  

[ ] d) Heapsort

**44.** En aplicaciones embebidas o memorias Flash donde el costo de **escritura** es muy elevado y destructivo, ¿qué algoritmo de ordenamiento básico resulta más conveniente por limitar las escrituras a máximo $n - 1$?

[ ] a) Insertion Sort  

[ ] b) Bubble Sort  

[ ] c) Selection Sort  

[ ] d) Mergesort

**45.** Considere el siguiente bloque de código en Python:

```python
def procesar(n):
    if n <= 1:
        return 1
    return n * procesar(n - 1)
```

¿Cuál es el contenido del Stack Frame activo cuando la función alcanza su caso base con `procesar(4)`?

[ ] a) Guarda únicamente el valor devuelto 24.  

[ ] b) Contiene los marcos apilados para $n=4, n=3, n=2$ y $n=1$, cada uno con sus datos y dirección de retorno pendientes.  

[ ] c) Libera toda la memoria acumulada previa.  

[ ] d) Pasa la memoria al segmento `.data`.

**46.** ¿Qué es la Optimización de Llamada de Cola (Tail Call Optimization - TCO)?

[ ] a) Una rutina para eliminar variables globales de la BSS.  

[ ] b) La capacidad de un compilador de reutilizar el mismo frame de pila cuando la llamada recursiva es la última operación de la función.  

[ ] c) La conversión de un heap en un árbol binario balanceado.  

[ ] d) La técnica de serializar archivos `.json` a binario.

**47.** ¿Por qué la optimización TCO no previene el desbordamiento de pila por defecto en scripts estándar de Python?

[ ] a) Porque Python no utiliza el segmento Stack.  

[ ] b) Porque el intérprete de Python no implementa TCO de forma nativa para preservar el trazado completo del Call Stack.  

[ ] c) Porque Python convierte todo a C++ automáticamente.  

[ ] d) Porque en Python las funciones no admiten retorno.

**48.** ¿Qué diferencia existe entre un TDA (Tipo de Dato Abstracto) y su Estructura de Datos asociada?

[ ] a) El TDA define el "qué hace" (interfaz u operaciones) y la estructura define el "cómo se implementa" en memoria.  

[ ] b) El TDA se compila y la estructura se interpreta.  

[ ] c) No existe diferencia técnica alguna.  

[ ] d) El TDA solo sirve para archivos de texto.

**49.** Considere la expresión en C/C++: `int *ptr = new int(50);`

¿Dónde reside la variable `ptr` y dónde reside el dato de valor `50` respectivamente?

[ ] a) Ambos residen en el Heap.  

[ ] b) Ambos residen en el Stack.  

[ ] c) `ptr` reside en el Stack y la memoria apuntada con valor `50` reside en el Heap.  

[ ] d) `ptr` reside en `.text` y `50` en `.bss`.

**50.** ¿Qué tipo de arquitectura de CPU es predominante en dispositivos móviles debido a su menor consumo energético y diseño RISC?

[ ] a) x86  

[ ] b) x86-64  

[ ] c) ARM  

[ ] d) SPARC

---

### Enunciado D (Preguntas 51 a 54)

Analice la siguiente rutina de partición usada en un algoritmo de ordenamiento:

```python
def particion(arr, bajo, alto):
    pivote = arr[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

datos = [28, 12, 19, 35, 15]
```

**51.** ¿A qué algoritmo de ordenamiento pertenece el esquema de particionado implementado en el código (esquema de Lomuto)?

[ ] a) Mergesort  

[ ] b) Quicksort  

[ ] c) Heapsort  

[ ] d) Radix Sort

**52.** Al ejecutar `particion(datos, 0, 4)`, ¿cuál es el valor seleccionado como pivote?

[ ] a) 28  

[ ] b) 19  

[ ] c) 15  

[ ] d) 35

**53.** ¿Cuál es el arreglo `datos` resultante inmediatamente después de culminar la ejecución de `particion(datos, 0, 4)`?

[ ] a) `[12, 15, 19, 35, 28]`  

[ ] b) `[12, 15, 19, 28, 35]`  

[ ] c) `[12, 19, 15, 35, 28]`  

[ ] d) `[15, 12, 19, 35, 28]`

**54.** ¿Qué índice retorna la función `particion` para la lista analizada?

[ ] a) 0  

[ ] b) 1  

[ ] c) 2  

[ ] d) 4

---

### Enunciado E (Preguntas 55 a 58)

Se requiere diseñar un sistema de atención prioritaria para una sala de emergencias médica donde los pacientes ingresan con un nivel de gravedad (entero de 1 a 10).

**55.** ¿Qué TDA es el más adecuado para gestionar el orden de atención de los pacientes?

[ ] a) Pila (Stack)  

[ ] b) Cola FIFO Estándar  

[ ] c) Cola de Prioridad (Priority Queue)  

[ ] d) Arreglo Circular

**56.** ¿Qué estructura de datos subyacente ofrece la mejor eficiencia temporal $O(\log n)$ para la inserción de nuevos pacientes y extracción del más grave?

[ ] a) Lista Simplemente Enlazada no ordenada  

[ ] b) Binary Heap  

[ ] c) Arreglo dinámico ordenado  

[ ] d) Matriz bidimensional

**57.** Si ingresan pacientes con las siguientes prioridades en orden: `4, 8, 2, 9`, ¿cuál es la prioridad del primer paciente atendido bajo un comportamiento de Heap Máximo?

[ ] a) 2  

[ ] b) 4  

[ ] c) 8  

[ ] d) 9

**58.** Si implementáramos esta estructura sobre una lista enlazada simple no ordenada, ¿cuál sería la complejidad temporal de la extracción del paciente con mayor prioridad?

[ ] a) $O(1)$  

[ ] b) $O(\log n)$  

[ ] c) $O(n)$  

[ ] d) $O(n^2)$

---

## Bloque III: Preguntas Continuas (59 a 100)

**59.** El comando `git clone <URL>` realiza la siguiente acción:

[ ] a) Crea una rama vacía en la nube.  

[ ] b) Copia un repositorio remoto completo, incluyendo historial y ramas, a la máquina local.  

[ ] c) Fusiona los archivos del directorio actual con el servidor.  

[ ] d) Borra el directorio `.git`.

**60.** ¿Qué ocurre cuando ejecutamos `git stash` en nuestro entorno local?

[ ] a) Se envían los cambios al servidor remoto.  

[ ] b) Se guardan temporalmente los cambios no confirmados en un área de almacenamiento temporal para dejar el directorio de trabajo limpio.  

[ ] c) Se elimina la rama actual.  

[ ] d) Se ejecuta una suite de pruebas de unidad.

**61.** ¿Qué función cumple la tabla de símbolos generada por un compilador?

[ ] a) Mantiene el registro de los breakpoints activos.  

[ ] b) Almacena la relación entre los nombres de variables, sus tipos, alcances y direcciones de memoria correspondientes.  

[ ] c) Traduce archivos `.json` a formato XML.  

[ ] d) Mide el tiempo en milisegundos del ciclo Fetch.

**62.** Un archivo con extensión `.yaml` se utiliza principalmente para:

[ ] a) Código ejecutable de alto rendimiento.  

[ ] b) Archivos de configuración estructurados mediante sangría/indentación.  

[ ] c) Almacenamiento binario comprimido.  

[ ] d) Hojas de estilo de bases de datos.

**63.** ¿Cuál es la representación en número de bytes requerida por la codificación ASCII estándar original?

[ ] a) 7 bits (almacenados usualmente en 1 byte)  

[ ] b) 4 bytes  

[ ] c) 16 bits  

[ ] d) 64 bits

**64.** ¿Qué módulo en Python permite convertir cualquier objeto estructurado en memoria RAM a un flujo de bytes binarios?

[ ] a) `json`  

[ ] b) `pickle`  

[ ] c) `sys`  

[ ] d) `math`

**65.** ¿Cuál es el orden de velocidad de acceso a los datos, del más rápido al más lento?

[ ] a) Disco SSD -> RAM -> Registros de CPU -> Caché L1  

[ ] b) Registros de CPU -> Caché L1 -> RAM -> Disco SSD  

[ ] c) RAM -> Caché L1 -> Registros de CPU -> Disco SSD  

[ ] d) Registros de CPU -> RAM -> Caché L1 -> Disco SSD

**66.** En un arreglo estático de C++, ¿cuál es la fórmula de dirección utilizada internamente para resolver el acceso a `arr[i]`?

[ ] a) `Direccion_Base + i`  

[ ] b) `Direccion_Base + (i * sizeof(TipoDato))`  

[ ] c) `Direccion_Base / i`  

[ ] d) `*(Direccion_Base) + i`

**67.** La diferencia fundamental entre un algoritmo In-Place y uno Out-of-Place es:

[ ] a) El algoritmo In-Place requiere memoria adicional de orden $O(1)$, mientras que Out-of-Place requiere memoria auxiliar proporcional a la entrada.  

[ ] b) In-Place solo funciona sobre vectores estáticos.  

[ ] c) Out-of-Place no utiliza procesador.  

[ ] d) In-Place es exclusivo de lenguajes interpretados.

**68.** Analice el siguiente bloque de código:

```python
def funcion_a(n):
    for i in range(n):
        j = 1
        while j < n:
            j = j * 2
```

¿Cuál es la complejidad algorítmica Big-O de la función anterior?

[ ] a) $O(n)$  

[ ] b) $O(n^2)$  

[ ] c) $O(n \log n)$  

[ ] d) $O(\log n)$

**69.** ¿Cuál es la complejidad temporal de acceder al último elemento ingresado en un TDA Pila (Stack) de $n$ elementos?

[ ] a) $O(1)$  

[ ] b) $O(n)$  

[ ] c) $O(\log n)$  

[ ] d) $O(n^2)$

**70.** ¿Qué estructura se utiliza internamente para gestionar el recorrido en anchura (BFS) sobre un árbol o grafo?

[ ] a) Stack  

[ ] b) Queue (Cola)  

[ ] c) Vector estático sin punteros  

[ ] d) BSS

**71.** ¿Qué estructura se utiliza internamente para gestionar el recorrido en profundidad (DFS) de manera iterativa?

[ ] a) Queue  

[ ] b) Stack (Pila)  

[ ] c) Heap Mínimo  

[ ] d) Archivo de texto plano

**72.** En el algoritmo Radix Sort, ¿por qué es indispensable que el método de ordenamiento auxiliar utilizado para cada dígito sea ESTABLE?

[ ] a) Para reducir la memoria del Heap a $O(1)$.  

[ ] b) Para preservar el ordenamiento ya logrado en los dígitos menos significativos en las pasadas previas.  

[ ] c) Porque si no es estable se produce un Stack Overflow.  

[ ] d) Para evitar convertir números a texto.

**73.** Considere la función sobre arreglos:

```python
def swap_test(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
```

¿Cuál es la complejidad en espacio auxiliar consumida por la función `swap_test`?

[ ] a) $O(n)$  

[ ] b) $O(1)$  

[ ] c) $O(n^2)$  

[ ] d) $O(\log n)$

**74.** Un algoritmo con complejidad $O(\log n)$ se caracteriza porque:

[ ] a) Duplica el número de operaciones cada vez que la entrada crece en 1.  

[ ] b) Reduce el tamaño del problema a resolver a una fracción (usualmente la mitad) en cada paso.  

[ ] c) Realiza un recorrido secuencial sobre todos los elementos.  

[ ] d) Consume toda la memoria RAM disponible.

**75.** En un Binary Heap representado en un arreglo, para un nodo ubicado en el índice `i = 5`, ¿cuál es el índice de su nodo Padre?

[ ] a) 2  

[ ] b) 1  

[ ] c) 3  

[ ] d) 0

**76.** Para la misma posición `i = 5`, ¿cuál es el índice de su Hijo Izquierdo?

[ ] a) 10  

[ ] b) 11  

[ ] c) 12  

[ ] d) 6

**77.** ¿Qué algoritmo de ordenamiento por comparación garantiza un rendimiento de $O(n \log n)$ en el PEOR caso y es además ESTABLE?

[ ] a) Quicksort  

[ ] b) Mergesort  

[ ] c) Heapsort  

[ ] d) Selection Sort

**78.** ¿Cuál es la cota inferior estricta ($\Omega$) de comparaciones para cualquier algoritmo de ordenamiento basado en comparación de elementos?

[ ] a) $\Omega(n)$  

[ ] b) $\Omega(n \log n)$  

[ ] c) $\Omega(n^2)$  

[ ] d) $\Omega(1)$

**79.** Un desarrollador requiere procesar una lista de 10 millones de registros de personas, ordenándolos por su edad (un número entero entre 0 y 120 años). ¿Cuál algoritmo ofrece el mejor rendimiento temporal absoluto en este escenario?

[ ] a) Quicksort  

[ ] b) Counting Sort  

[ ] c) Insertion Sort  

[ ] d) Mergesort

**80.** ¿Qué valor retorna la función `len()` aplicada sobre una pila implementada con nodos enlazados?

[ ] a) Depende del tamaño de la variable `.text`.  

[ ] b) Retorna el contador de nodos en $O(1)$ si se mantiene una variable de control, o en $O(n)$ si se recorren los nodos.  

[ ] c) Siempre realiza una lectura de disco $O(n^2)$.  

[ ] d) No se puede calcular.

**81.** Analice la función de ordenamiento:

```python
def ordenar_demo(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
```

¿Qué algoritmo representa el código anterior?

[ ] a) Selection Sort  

[ ] b) Insertion Sort  

[ ] c) Bubble Sort  

[ ] d) Counting Sort

**82.** ¿Cuál es la complejidad temporal de `ordenar_demo` si el arreglo de entrada ya se encuentra completamente en orden inverso?

[ ] a) $O(n)$  

[ ] b) $O(n \log n)$  

[ ] c) $O(n^2)$  

[ ] d) $O(1)$

**83.** ¿Cuál es la razón principal por la cual Quicksort suele ser en la práctica más rápido que Mergesort en arreglos de memoria RAM, a pesar de compartir complejidad promedio $O(n \log n)$?

[ ] a) Quicksort no usa comparaciones.  

[ ] b) Posee una excelente localidad de referencia y menor costo de asignación de memoria (in-place sobre datos).  

[ ] c) Quicksort nunca cae en casos desbalanceados.  

[ ] d) Mergesort no funciona en CPU de 64 bits.

**84.** En un entorno de CI/CD, la fase de "Build" o construcción incluye la instrucción de:

[ ] a) Compilar el código, resolver dependencias y empaquetar ejecutables/artefactos.  

[ ] b) Desinstalar el sistema operativo.  

[ ] c) Limpiar manualmente la BSS.  

[ ] d) Escribir las especificaciones en lenguaje natural.

**85.** ¿Qué ocurre en el Stack de un programa durante un "Stack Overflow"?

[ ] a) Se llena la memoria del BSS de ceros.  

[ ] b) La pila supera el límite de memoria asignado por el sistema operativo al acumular demasiados stack frames sin liberar.  

[ ] c) El disco duro detiene la lectura.  

[ ] d) Se borran los punteros globales.

**86.** La estrategia "Divide y Vencerás" (Divide and Conquer) consiste en:

[ ] a) Probar todas las soluciones posibles mediante ciclos anidados.  

[ ] b) Dividir un problema en subproblemas más pequeños del mismo tipo, resolverlos recursivamente y combinar sus soluciones.  

[ ] c) Usar únicamente estructuras de memoria contigua.  

[ ] d) Escribir las pruebas antes que el código.

**87.** En Python, ¿qué estructura de la biblioteca estándar ofrece operaciones de inserción y eliminación eficientes $O(1)$ en ambos extremos?

[ ] a) `list`  

[ ] b) `tuple`  

[ ] c) `collections.deque`  

[ ] d) `set`

**88.** ¿Cuál es el espacio de memoria auxiliar utilizado por el algoritmo Heapsort durante el proceso de ordenamiento?

[ ] a) $O(n)$  

[ ] b) $O(1)$  

[ ] c) $O(n \log n)$  

[ ] d) $O(\log n)$

**89.** Si un vector estático en C++ se declara como `float datos[100];` y la dirección base es `0x1000`, ¿cuál es la dirección de memoria de `datos[2]` si un `float` ocupa 4 bytes?

[ ] a) `0x1002`  

[ ] b) `0x1004`  

[ ] c) `0x1008`  

[ ] d) `0x1016`

**90.** ¿Qué valor tiene la variable `c` tras ejecutar la recursión `misterio_num(3)`?

```python
def misterio_num(n):
    if n == 0:
        return 0
    return n + misterio_num(n - 1)
```

[ ] a) 3  

[ ] b) 6  

[ ] c) 9  

[ ] d) 0

**91.** En el desarrollo asistido con especificaciones (Spec-Driven Development), la fuente de verdad principal del sistema es:

[ ] a) El archivo ejecutable compilado.  

[ ] b) El documento formal de especificaciones de comportamiento e intenciones.  

[ ] c) La tabla de símbolos del sistema operativo.  

[ ] d) El archivo de log del debugger.

**92.** ¿Cuál es la ventaja de la memoria Caché L1 integrada en la CPU frente a la memoria RAM primaria?

[ ] a) Posee una capacidad de almacenamiento de varios Terabytes.  

[ ] b) Posee una velocidad de acceso infinitamente superior al estar en el mismo chip de la CPU, reduciendo la latencia de bus.  

[ ] c) Es de tipo no volátil.  

[ ] d) Reemplaza al segmento `.text`.

**93.** Un archivo codificado en JSON presenta la siguiente ventaja estructural principal sobre XML:

[ ] a) Requiere compilación.  

[ ] b) Es más compacto, fácil de parsear por navegadores/APIs y libre de etiquetas de cierre pesadas.  

[ ] c) Garantiza ordenamiento en $O(1)$.  

[ ] d) Soporta datos binarios no serializados.

**94.** ¿Cuál es la complejidad temporal de reconstruir completamente un arreglo desordenado en un Heap válido utilizando el algoritmo de **Heapify** (Floyd's algorithm)?

[ ] a) $O(n \log n)$  

[ ] b) $O(n)$  

[ ] c) $O(n^2)$  

[ ] d) $O(\log n)$

**95.** El algoritmo de ordenamiento por Inserción (Insertion Sort) funciona de manera idéntica a:

[ ] a) Organizar fichas en un tablero de ajedrez.  

[ ] b) Ordenar cartas en la mano insertando cada una en su lugar correspondiente entre las ya ordenadas.  

[ ] c) Buscar la hoja más profunda de un árbol binario.  

[ ] d) Intercambiar elementos de los extremos hacia el centro.

**96.** ¿Qué comando de Git permite deshacer todos los cambios locales no confirmados y restaurar el espacio de trabajo al último commit de manera destructiva?

[ ] a) `git status`  

[ ] b) `git reset --hard HEAD`  

[ ] c) `git log --oneline`  

[ ] d) `git checkout -b`

**97.** En un programa donde se realizan múltiples operaciones de inserción al inicio de una secuencia de datos, ¿qué estructura ofrece mejor complejidad temporal?

[ ] a) Vector estático  

[ ] b) Lista Enlazada Simple  

[ ] c) Arreglo dinámico sin expansión  

[ ] d) Matriz estática

**98.** ¿Cuál es el papel del registro RSP (Stack Pointer) en la gestión de funciones?

[ ] a) Guardar el código máquina.  

[ ] b) Apuntar a la dirección actual del tope del Stack de llamadas.  

[ ] c) Realizar sumas en la ALU.  

[ ] d) Leer bloques desde el disco SSD.

**99.** ¿Cuál es la cota ajustada ($\Theta$) de complejidad para el algoritmo Mergesort en su **MEJOR** caso?

[ ] a) $\Theta(n)$  

[ ] b) $\Theta(n \log n)$  

[ ] c) $\Theta(1)$  

[ ] d) $\Theta(n^2)$

**100.** En la implementación de una Cola de Prioridad basada en Heap, la extracción del elemento con mayor prioridad requiere un proceso de:

[ ] a) Intercambiar la raíz con el último elemento, eliminar la última posición y aplicar `bubble_down` (o `heapify`) desde la raíz.  

[ ] b) Recorrer todo el arreglo linealmente.  

[ ] c) Invertir los punteros de la lista.  

[ ] d) Duplicar la capacidad del vector.

---

## Bloque de Respuestas Correctas

| # | R | # | R | # | R | # | R | # | R |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | b | **21** | b | **41** | b | **61** | b | **81** | b |
| **2** | c | **22** | b | **42** | b | **62** | b | **82** | c |
| **3** | b | **23** | c | **43** | b | **63** | a | **83** | b |
| **4** | a | **24** | b | **44** | c | **64** | b | **84** | a |
| **5** | b | **25** | b | **45** | b | **65** | b | **85** | b |
| **6** | a | **26** | c | **46** | b | **66** | b | **86** | b |
| **7** | b | **27** | a | **47** | b | **67** | a | **87** | c |
| **8** | c | **28** | b | **48** | a | **68** | c | **88** | b |
| **9** | c | **29** | b | **49** | c | **69** | a | **89** | c |
| **10** | a | **30** | b | **50** | c | **70** | b | **90** | b |
| **11** | b | **31** | b | **51** | b | **71** | b | **91** | b |
| **12** | b | **32** | c | **52** | c | **72** | b | **92** | b |
| **13** | b | **33** | d | **53** | a | **73** | b | **93** | b |
| **14** | c | **34** | b | **54** | b | **74** | b | **94** | b |
| **15** | b | **35** | b | **55** | c | **75** | a | **95** | b |
| **16** | b | **36** | b | **56** | b | **76** | b | **96** | b |
| **17** | b | **37** | c | **57** | d | **77** | b | **97** | b |
| **18** | b | **38** | b | **58** | c | **78** | b | **98** | b |
| **19** | c | **39** | c | **59** | b | **79** | b | **99** | b |
| **20** | b | **40** | b | **60** | b | **80** | b | **100** | a |
