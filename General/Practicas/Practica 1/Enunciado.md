# Práctica 1
## Arquitectura de Software, Memoria, Estructuras de Datos y Recursión

---

### Ejemplo 1

Una empresa decide migrar su sistema de una arquitectura monolítica hacia una de microservicios.

* a) Explique en qué consiste una arquitectura monolítica y mencione una desventaja relacionada con la escalabilidad.
* b) Explique en qué consiste una arquitectura de microservicios y el principio de responsabilidad única aplicado a esta.
* c) ¿Qué es una API y qué función cumple para conectar diferentes microservicios entre sí?
* d) Mencione dos tipos de API mencionados en el curso, indicando cuál es el más común.

---

### Ejemplo 2

Un estudiante quiere entender qué sucede realmente dentro de la computadora cuando se ejecuta un programa.

* a) Explique por qué se dice que RAM y CPU son los componentes necesarios para la ejecución de un programa (Compute).
* b) Explique por qué el código fuente almacenado en el disco duro (HDD/SSD) no es suficiente por sí solo para que un programa se ejecute.
* c) Describa las tres etapas del ciclo de instrucciones (Fetch, Decode, Execute).
* d) ¿Qué componente del CPU se encarga de ejecutar las instrucciones matemáticas y lógicas?

---

### Ejemplo 3

Se tiene el siguiente fragmento de código en C++:

```cpp
int numero = 10;

int suma(int a, int b) {
    int res;
    res = a + b;
    return res;
}

int main() {
    int x = 10;
    int y = 20;
    std::cout << suma(x, y);
    return 10;
}
```

* a) Indique en qué segmento de memoria se almacena el código de las funciones `suma` y `main`, y qué característica especial tiene ese segmento.
* b) Indique en qué segmento de memoria se almacena la variable global `numero`, y por qué se ubica ahí.
* c) Indique en qué segmento de memoria se almacenan las variables locales `x`, `y` y `res`, explicando cómo crece ese segmento.
* d) Explique qué es un "stack frame" y qué información contiene cada vez que se llama a una función.

---

### Ejemplo 4

Se declara en C++ lo siguiente: `int* x = new int[10];`

* a) Explique qué hace el operador `new` en este caso y en qué segmento de memoria se reserva el espacio.
* b) Explique la diferencia entre lo que imprime `cout << x` y lo que imprime `cout << *x`.
* c) Explique qué representa `&x` y en qué segmento de memoria se encuentra almacenada la variable `x` misma.
* d) Explique qué es un "memory leak" y por qué puede ocurrir si se pierde la referencia a la dirección devuelta por `new`.

---

### Ejemplo 5

Una empresa está decidiendo si migrar sus servidores de arquitectura x86-64 a ARM para reducir costos en la nube.

* a) Explique la diferencia principal entre las arquitecturas x86-64 y ARM en cuanto a potencia y consumo de energía.
* b) Explique por qué una migración de x86 a ARM puede generar ahorros económicos importantes en un entorno de cloud computing.
* c) Indique cómo puede variar el tamaño en bytes de un tipo de dato `int` según la arquitectura utilizada.
* d) Explique qué podría ocurrir si un valor muy grande, como `x = 23457890130`, se ejecuta en una arquitectura x86-64 de 32 bits en comparación con una arquitectura ARM de mayor capacidad.

---

### Ejemplo 6

Un programador debe decidir si escribir un módulo de su sistema en C++ (compilado) o en Python (interpretado).

* a) Describa el proceso general de compilación, desde el código fuente hasta el archivo ejecutable, mencionando el rol del "linker".
* b) Describa cómo funciona un lenguaje interpretado, incluyendo el concepto de "bytecode".
* c) Explique por qué, en términos generales, un lenguaje compilado es más rápido en ejecución que uno interpretado.
* d) Explique la ventaja de portabilidad que tienen los lenguajes interpretados frente a los compilados, y por qué esta ventaja no aplica de la misma forma a los compilados.

---

### Ejemplo 7

Un equipo de desarrollo está definiendo su flujo de trabajo con Git para colaborar en un proyecto.

* a) Explique qué es un "commit" en Git y qué información almacena.
* b) Explique la diferencia entre `git merge` y `git rebase` en cuanto al historial de versiones que generan.
* c) Explique para qué se utilizan las "branches" (ramas) dentro de un flujo de trabajo colaborativo.
* d) Mencione qué es un flujo de CI/CD y qué relación tiene con las pruebas de unidad (unit testing) y los contenedores.

---

### Ejemplo 8

Se debe decidir si un archivo se almacenará en formato texto o en formato binario.

* a) Explique la diferencia principal entre un archivo de texto y uno binario en cuanto a su representación en disco.
* b) Explique qué es la codificación de caracteres y mencione la diferencia entre ASCII y Unicode.
* c) Dado que un archivo de texto de cierto conjunto de datos ocupa 23.219.754 bytes y su versión binaria ocupa 16.000.000 bytes, explique por qué los archivos binarios suelen ser preferidos quee los de texto en cuanto a rendimiento.
* d) Explique por qué, aunque los binarios sean más eficientes, en ciertos contextos es preferible usar archivos de texto.

---

### Ejemplo 9

Un programador necesita compartir datos estructurados entre distintos sistemas y evalúa distintos formatos.

* a) Explique cómo se estructura la información en un archivo XML, usando el concepto de etiquetas.
* b) Explique cómo se estructura la información en un archivo JSON, usando el concepto de llaves.
* c) Explique cómo se estructura la información en un archivo YAML.
* d) Explique qué hace la librería `pickle` en Python y qué proceso permite realizar (`dump` y `load`).

---

### Ejemplo 10

Se tiene el siguiente arreglo declarado en C++: `int v[10];`

* a) Explique qué significa que la memoria de un vector debe asignarse de manera continua.
* b) Explique por qué el acceso a un elemento de un vector, como `v[4]`, tiene complejidad O(1).
* c) Explique qué ocurre cuando un vector dinámico se queda sin espacio y necesita crecer (proceso de "Deep Copy").
* d) Explique la estrategia de expansión x2 (duplicar el tamaño) y por qué reduce significativamente la cantidad de operaciones necesarias en comparación con crecer de una en una.

---

### Ejemplo 11

Se compara la implementación de un vector contra una lista enlazada simple para almacenar una colección de datos.

* a) Explique la diferencia principal entre cómo se asigna la memoria en un vector y en una lista enlazada.
* b) Describa la estructura de un nodo de una lista enlazada simple (qué campos contiene).
* c) Explique por qué el acceso a un elemento en una lista enlazada no puede ser O(1) como en un vector.
* d) Mencione una ventaja de la lista enlazada frente al vector, relacionada con la inserción y eliminación de elementos.

---

### Ejemplo 12

Una aplicación necesita implementar una fila de impresión de documentos y un historial de acciones que se puedan deshacer ("undo").

* a) Indique qué tipo de estructura de datos (Cola o Pila) sería más adecuada para la fila de impresión, y explique el principio bajo el cual funciona (FIFO o LIFO).
* b) Indique qué tipo de estructura sería más adecuada para el historial de "undo", y explique su principio de funcionamiento.
* c) Mencione las operaciones principales de una Cola y de una Pila, respectivamente.
* d) Explique por qué implementar una Pila usando una lista doblemente enlazada sería un desperdicio de memoria.

---

### Ejemplo 13

Un desarrollador implementa un carrusel de imágenes en una página web que permite avanzar y retroceder.

* a) Explique por qué una lista enlazada simple no es la estructura más adecuada para este caso.
* b) Describa la estructura de un nodo en una lista doblemente enlazada.
* c) Explique qué es el "overhead" en el contexto de las listas enlazadas y cómo afecta el consumo de memoria.
* d) Si cada puntero (overhead) ocupa 4 bytes y un nodo tiene 2 punteros, calcule cuántos bytes adicionales de overhead se generarían en una lista de 50.000 nodos.

---

### Ejemplo 14

Se tiene la siguiente función recursiva:

```python
def cuenta(n):
    if n == 0:
        return
    cuenta(n - 1)
    print(n)
```

* a) Identifique cuál es el caso base de esta función y explique por qué es necesario.
* b) Explique qué ocurre en la pila (stack) del CPU cada vez que se realiza una llamada recursiva a `cuenta`.
* c) Explique qué es un "stack overflow" y en qué circunstancia podría ocurrir si esta función se ejecutara mal planteada.
* d) Ejecutando `cuenta(3)`, indique en qué orden se imprimirán los valores en pantalla.

---

### Ejemplo 15

Se comparan dos formas de resolver el mismo problema: una versión recursiva y una versión iterativa.

* a) Explique por qué, en términos generales, se prefiere la versión iterativa sobre la recursiva en cuanto a rendimiento.
* b) Explique en qué casos sí conviene utilizar una solución recursiva en lugar de una iterativa.
* c) Explique qué es la recursión de cola (tail recursion) y cómo la aprovechan los compiladores mediante la optimización TCO.
* d) Explique brevemente la técnica de "divide y vencerás" utilizando como ejemplo el cálculo de una sumatoria de forma recursiva (Sn = n + Sn-1).

---

### Ejemplo 16

Un programador afirma que para medir qué tan eficiente es un algoritmo, lo mejor es cronometrar cuánto tarda en ejecutarse en su computadora.

* a) Explique por qué medir el tiempo de ejecución en segundos no es una forma confiable de comparar dos algoritmos.
* b) ¿Qué se mide en su lugar para analizar la eficiencia de un algoritmo de forma independiente del hardware?
* c) Mencione los dos aspectos principales (recursos) que conforman la eficiencia de un algoritmo.
* d) Si dos algoritmos "hacen lo mismo" pero uno tarda 1,075 s y el otro 4,348 s en la misma máquina, ¿por qué esta comparación por sí sola no basta para concluir cuál es más eficiente en general?

---

### Ejemplo 17

Se tiene la siguiente función:

```python
def foo(x):
    res = x + 15
    print(res)
```

* a) Explique por qué esta función tiene una complejidad de O(1).
* b) ¿Qué significa que un algoritmo tenga "tiempo constante"?
* c) Indique si la complejidad O(1) depende del valor de entrada `x`. Justifique.
* d) Mencione otro ejemplo de operación que normalmente se considera O(1).

---

### Ejemplo 18

Analice el siguiente fragmento de código:

```python
def foo(n):
    for i in range(1, n+1):    # ciclo 1
        pass
    print(n)
    for i in range(1, n+1):    # ciclo 2
        pass
    return
```

* a) Indique la complejidad de cada uno de los dos ciclos por separado.
* b) Escriba la expresión completa de complejidad antes de simplificar (sumando todos los términos, incluyendo las instrucciones sueltas).
* c) Simplifique la expresión anterior hasta llegar a la notación final en O grande.
* d) Explique por qué se eliminan las constantes multiplicativas y aditivas al simplificar una expresión de complejidad.

---

### Ejemplo 19

Complete la siguiente tabla, indicando la notación en O grande y un ejemplo de algoritmo o situación asociada a cada complejidad:

| Nombre | Notación | Ejemplo de algoritmo |
|:---:|:---:|:---:|
| Constante | | |
| Logarítmica | | |
| Lineal | | |
| Lineal-Logarítmica | | |
| Cuadrática | | |

* a) Complete la tabla anterior.
* b) Explique por qué la búsqueda binaria se clasifica como O(log n).
* c) Explique por qué la búsqueda en una lista enlazada se clasifica como O(n).
* d) Explique por qué el ordenamiento burbuja (con ciclos anidados) se clasifica como O(n²).

---

### Ejemplo 20

Se analiza el rendimiento de un mismo algoritmo bajo tres escenarios distintos de datos de entrada.

* a) Explique qué representa la cota superior (peor caso) de un algoritmo, usando el ejemplo de un algoritmo de ordenamiento.
* b) Explique qué representa la cota inferior (mejor caso) de un algoritmo, usando el mismo ejemplo.
* c) Explique qué representa la cota promedio de un algoritmo.
* d) ¿Por qué la notación O grande se enfoca principalmente en la cota superior, ignorando en la mayoría de los análisis la cota promedio e inferior?

---

## RESPUESTAS

---

### Ejemplo 1

* a) Consiste en tener todo el código fuente de la aplicación en un solo proyecto que se compila y ejecuta como una sola unidad; una desventaja es que si no fue diseñada para usar varios servidores, no se puede escalar fácilmente agregando más instancias.
* b) Consiste en separar cada funcionalidad en módulos totalmente independientes que se ejecutan por separado (usualmente en contenedores), aplicando el principio de responsabilidad única a nivel de servicio completo, no solo de función.
* c) Una API es la parte del código que se expone para que agentes externos puedan consumir la funcionalidad de un módulo; permite que un microservicio consuma la información o funcionalidad de otro sin acceder directamente a su código interno.
* d) REST API, SOAP y GraphQL; la más común es REST API.

---

### Ejemplo 2

* a) Porque el código en ejecución debe estar cargado en la RAM para que el CPU pueda leer y ejecutar sus instrucciones; sin estos dos componentes trabajando juntos, no es posible ejecutar ningún programa.
* b) Porque el disco duro solo almacena la información de forma persistente cuando el sistema está apagado; la RAM es volátil pero es la única memoria desde la cual el CPU puede leer instrucciones para ejecutarlas.
* c) Fetch: se traen las instrucciones desde la RAM; Decode: se toma la instrucción y se decodifica; Execute: una vez lista, se ejecuta.
* d) La ALU (Unidad Aritmético-Lógica).

---

### Ejemplo 3

* a) Se almacenan en el segmento de código (.text); esta parte de la memoria es de solo lectura (Read Only).
* b) Se almacena en el segmento de datos (.data), ya que es una variable global inicializada, y este segmento permite acceder a ella desde cualquier parte del programa.
* c) Se almacenan en el stack; este segmento es el único que crece "al revés", es decir, hacia direcciones de memoria más bajas.
* d) Es la información asociada a cada llamada de función, que incluye la dirección de retorno y las variables locales de esa llamada; se crea un nuevo stack frame en cada llamada.

---

### Ejemplo 4

* a) Reserva suficiente espacio en el heap para almacenar un arreglo de 10 enteros, devolviendo la dirección de memoria donde inicia dicho espacio.
* b) `cout << x` imprime la dirección de memoria a la que apunta `x` (por ejemplo 0x4000); `cout << *x` imprime el valor almacenado en esa dirección (el contenido al que apunta).
* c) `&x` representa la dirección de memoria donde está almacenada la variable `x` en sí; esta se encuentra en el stack, ya que es una variable local de tipo puntero.
* d) Un memory leak ocurre cuando se pierde la referencia a un espacio de memoria reservado dinámicamente sin liberarlo; si se pierde la dirección devuelta por `new`, ya no es posible acceder a ese espacio ni liberarlo, quedando "atrapado" en el heap.

---

### Ejemplo 5

* a) x86-64 ofrece mayor potencia pero mayor consumo de energía; ARM ofrece menor potencia relativa pero un consumo de energía significativamente menor.
* b) Porque en la nube el costo está directamente relacionado con el consumo energético; al usar procesadores ARM que consumen menos energía mientras alcanzan niveles de potencia similares a Intel, se generan ahorros considerables.
* c) En arquitecturas x86 puede variar entre 2 y 4 bytes según sea de 32 o 64 bits, mientras que en ARM el tamaño de un `int` suele ser de 8 bytes.
* d) En una arquitectura x86-64 de 32 bits podría generarse un desbordamiento de memoria (overflow) al no poder representar el valor completo, mientras que en una arquitectura con mayor capacidad de bits el valor correría correctamente sin desbordarse.

---

### Ejemplo 6

* a) El código fuente se compila generando un archivo objeto (.obj) en lenguaje máquina; luego, el proceso de "linker" combina ese objeto con las bibliotecas precompiladas del lenguaje para generar el archivo ejecutable final (.exe).
* b) El intérprete lee una instrucción del código fuente y genera el bytecode correspondiente según la arquitectura, lo envía a la RAM y de ahí al CPU para ejecutarse, repitiendo este proceso instrucción por instrucción.
* c) Porque el lenguaje compilado ya tiene todas sus instrucciones traducidas a lenguaje máquina antes de ejecutarse, enviando directamente de RAM a CPU, mientras que el interpretado debe traducir cada instrucción en tiempo real antes de ejecutarla.
* d) Porque el mismo código fuente interpretado puede ejecutarse en distintas arquitecturas sin recompilar, mientras que un ejecutable compilado está atado a la arquitectura para la que fue compilado (por ejemplo, el tamaño de un `int` puede variar entre arquitecturas, generando comportamientos distintos o errores).

---

### Ejemplo 7

* a) Es un historial (snapshot) del estado de los archivos del proyecto en un momento dado.
* b) `git merge` combina las ramas manteniendo el historial de ambas líneas de desarrollo (generando una estructura ramificada), mientras que `git rebase` reescribe el historial para que parezca una secuencia lineal de commits, generando un historial más limpio.
* c) Permiten que distintos desarrolladores trabajen de forma aislada en nuevas funcionalidades sin afectar la línea principal (main/master) hasta que el código haya sido probado y aprobado.
* d) CI/CD es un proceso automatizado que integra pruebas de calidad (QA), pruebas de unidad y la creación de contenedores para actualizar automáticamente la aplicación en un entorno basado en cloud computing.

---

### Ejemplo 8

* a) El archivo de texto almacena cada carácter según su representación codificada, mientras que el archivo binario almacena la representación en formato máquina (bits) tal como está en memoria, sin usar un mecanismo de codificación de caracteres.
* b) La codificación de caracteres define cómo la computadora representa cada símbolo; ASCII usa 7 u 8 bits (128 o 256 caracteres), mientras que Unicode permite representar hasta 240.000 caracteres, reservando mayor cantidad de bits por carácter.
* c) Porque ocupan menos espacio en disco y, al no requerir procesos de codificación/decodificación de caracteres, se leen y escriben más rápido, mejorando el rendimiento general.
* d) Porque los archivos de texto son legibles directamente y permiten conocer fácilmente el significado de la información almacenada, lo cual es útil cuando se necesita revisar o editar el contenido manualmente.

---

### Ejemplo 9

* a) La información se organiza mediante etiquetas de apertura y cierre que envuelven cada valor (por ejemplo `<name>John Doe</name>`).
* b) La información se organiza mediante pares de llave y valor, delimitados por llaves `{}` (por ejemplo `"name": "John Doe"`).
* c) La información se organiza mediante pares de llave y valor separados por dos puntos, usando la indentación para representar jerarquía, sin necesidad de llaves ni etiquetas.
* d) `pickle.dump()` serializa la información dándole un formato adecuado para guardarla en disco; `pickle.load()` lee el archivo y reconstruye los bytes almacenados en su forma original.

---

### Ejemplo 10

* a) Significa que todos los elementos del vector deben estar ubicados en direcciones de memoria consecutivas, sin espacios entre ellos.
* b) Porque, al conocer la dirección de inicio del vector y el tamaño de cada elemento, se puede calcular directamente la dirección del elemento deseado (`v + índice * tamaño`), sin necesidad de recorrer los elementos anteriores.
* c) Se debe buscar un nuevo espacio de memoria con suficiente capacidad, copiar todos los elementos existentes a ese nuevo espacio (Deep Copy) y luego liberar el espacio anteriormente utilizado.
* d) Al duplicar el tamaño en lugar de crecer de uno en uno, se reduce drásticamente la cantidad de veces que se debe realizar el proceso de copia, disminuyendo significativamente el total de operaciones necesarias (por ejemplo, de 500 millones a solo 2 millones en un caso de 1 millón de elementos).

---

### Ejemplo 11

* a) En el vector la memoria se asigna de forma continua; en la lista enlazada cada nodo puede estar ubicado en cualquier parte de la memoria, conectado mediante punteros al siguiente nodo.
* b) Contiene un campo de dato y un campo `next`, que almacena la dirección de memoria del siguiente nodo.
* c) Porque no existe una fórmula directa para calcular la dirección de un elemento intermedio; es necesario recorrer los nodos uno por uno desde el inicio hasta llegar al elemento deseado.
* d) La inserción y eliminación de elementos no requiere desplazar ni copiar el resto de los elementos, como sí ocurre en un vector al crecer o reducirse.

---

### Ejemplo 12

* a) Una Cola, bajo el principio FIFO (First In, First Out), ya que el primer documento enviado a imprimir debe ser el primero en procesarse.
* b) Una Pila, bajo el principio LIFO (Last In, First Out), ya que la última acción realizada debe ser la primera en deshacerse.
* c) Cola: enqueue (insertar) y dequeue (remover); Pila: push (insertar), pop (recuperar y eliminar) y top/peek (consultar el tope).
* d) Porque una pila, por su naturaleza, nunca necesita recorrerse hacia atrás manualmente ni acceder a elementos intermedios; usar una lista doblemente enlazada agregaría punteros adicionales (overhead) sin ninguna funcionalidad útil para este caso.

---

### Ejemplo 13

* a) Porque en una lista simple no es posible retroceder; para volver a un elemento anterior se debe recorrer nuevamente desde el inicio de la lista.
* b) Contiene un campo de valor (dato), un puntero `prev` que apunta al nodo anterior y un puntero `next` que apunta al nodo siguiente.
* c) El overhead es la memoria adicional que se consume por los punteros necesarios para mantener la estructura de la lista, la cual no forma parte de los datos en sí, pero es indispensable para el funcionamiento de la estructura.
* d) 2 punteros × 4 bytes = 8 bytes de overhead por nodo; 8 bytes × 50.000 nodos = 400.000 bytes (aproximadamente 400 KB) de overhead adicional.

---

### Ejemplo 14

* a) El caso base es `if n == 0: return`; es necesario porque detiene las llamadas recursivas, evitando que la función se siga llamando a sí misma indefinidamente.
* b) Cada llamada genera un nuevo "stack frame" que se apila (push) en el stack, guardando la dirección de retorno y el valor local de `n` para esa llamada específica.
* c) Un stack overflow ocurre cuando se realizan demasiadas llamadas recursivas sin llegar al caso base, llenando por completo el stack disponible; podría ocurrir si el caso base estuviera mal definido o ausente.
* d) Se imprimirán en el orden: 1, 2, 3 (ya que los `print` se ejecutan al momento de "regresar" de cada llamada recursiva, en orden inverso a como fueron llamadas).

---

### Ejemplo 15

* a) Porque las versiones iterativas suelen tener menor consumo de memoria (no generan múltiples stack frames) y, en general, ofrecen mejor rendimiento en tiempo de ejecución.
* b) Cuando el problema es naturalmente recursivo o el planteamiento iterativo resulta muy complejo de programar, como en el caso de recorrer un laberinto con backtracking.
* c) Ocurre cuando la llamada recursiva es la última instrucción de la función, sin operaciones pendientes después de ella; los compiladores pueden aprovechar esto mediante la Optimización de Llamadas de Cola (TCO) para reutilizar el mismo stack frame y transformar la recursión en un ciclo eficiente.
* d) Consiste en resolver un problema grande dividiéndolo en subproblemas más pequeños del mismo tipo; en el caso de Sn = n + Sn-1, cada llamada reduce el problema en 1 hasta llegar al caso base (S0 = 0), y luego se van resolviendo y combinando los resultados en el camino de regreso (pop) de cada stack frame.

---

### Ejemplo 16

* a) Porque el tiempo de ejecución depende de factores variables del hardware (arquitectura del CPU, velocidad, cantidad de núcleos), por lo que el mismo algoritmo puede tardar diferente en distintas máquinas.
* b) Se mide la cantidad de instrucciones que debe ejecutar el algoritmo para terminar, independientemente del hardware utilizado.
* c) El tiempo (CPU) y el espacio (RAM).
* d) Porque el tiempo medido en segundos depende del equipo donde se ejecutó la prueba; lo relevante es analizar cuántas instrucciones ejecuta cada algoritmo, ya que eso sí permite una comparación justa entre ellos independientemente del hardware.

---

### Ejemplo 17

* a) Porque la operación de suma y el print se ejecutan siempre la misma cantidad de veces, sin importar el valor de `x`, por lo que la cantidad de instrucciones no crece con la entrada.
* b) Significa que la cantidad de instrucciones ejecutadas no depende del tamaño o valor de los datos de entrada; siempre toma la misma cantidad de pasos.
* c) No depende del valor de `x`; la función realiza la misma cantidad de operaciones sin importar si `x` es pequeño o grande.
* d) Acceder a un elemento de un vector mediante su índice (acceso directo).

---

### Ejemplo 18

* a) Cada uno de los dos ciclos tiene complejidad O(n).
* b) O(n) + O(n) + O(1) + O(1) + O(1) + O(1), que puede reescribirse como O(2n) + O(4).
* c) Al eliminar constantes multiplicativas y aditivas, se obtiene O(n).
* d) Porque dichas constantes no cambian el comportamiento general (la forma de la curva) del algoritmo a medida que `n` crece; lo relevante para el análisis es la tendencia de crecimiento, no los valores exactos.

---

### Ejemplo 19

* a)

| Nombre | Notación | Ejemplo de algoritmo |
|:---:|:---:|:---:|
| Constante | O(1) | Acceso directo a un elemento de un vector |
| Logarítmica | O(log n) | Búsqueda binaria / búsqueda en árbol binario |
| Lineal | O(n) | Búsqueda en una lista enlazada |
| Lineal-Logarítmica | O(n log n) | Algoritmos de ordenamiento eficientes |
| Cuadrática | O(n²) | Ordenamiento burbuja / ciclos anidados |

* b) Porque en cada paso se descarta la mitad de los elementos restantes, reduciendo el problema a la mitad sucesivamente, lo cual es característico de una complejidad logarítmica.
* c) Porque, al no tener acceso directo como en un vector, se debe recorrer nodo por nodo desde el inicio hasta encontrar el elemento buscado, en el peor caso recorriendo todos los elementos.
* d) Porque compara cada elemento con todos los demás mediante ciclos anidados, generando una cantidad de comparaciones proporcional al cuadrado de la cantidad de elementos.

---

### Ejemplo 20

* a) Es el escenario en el que el algoritmo requiere la mayor cantidad de instrucciones para completar su tarea; para un ordenamiento, sería el caso en que todos los elementos están completamente desordenados.
* b) Es el escenario en el que el algoritmo requiere la menor cantidad de instrucciones; para un ordenamiento, sería el caso en que los datos ya están ordenados.
* c) Es un escenario intermedio, donde algunos elementos están ordenados y otros no, representando un caso "típico" de ejecución.
* d) Porque la cota superior garantiza un límite máximo de instrucciones sin importar el caso, lo que permite comparar algoritmos de forma segura y consistente, mientras que la cota promedio e inferior dependen de características específicas de los datos de entrada, que no siempre se conocen de antemano.

---



---

# Práctica de Laboratorio
## Estructuras de Datos, Recursión y Archivos en Python

## Instrucciones
Resolver los siguientes ejercicios en Python. Cuando se indique, los datos deben recibirse como argumentos por línea de comandos (`sys.argv`).

---

### Ejercicio 1: Validador de paréntesis balanceados

Implemente una Pila (usando una lista enlazada, con `push`, `pop` y `peek`) y utilícela para verificar si una expresión recibida por línea de comandos tiene los paréntesis, corchetes y llaves correctamente balanceados.

```
python ej01.py "(a+[b*c]-{d/e})"
```

---

### Ejercicio 2: Simulador de fila de impresión

Implemente una Cola (usando una lista enlazada, con `enqueue` y `dequeue`) que reciba una serie de nombres de documentos por línea de comandos y simule el orden en que serían impresos, mostrando cada documento en el momento en que "sale" de la cola.

```
python ej02.py doc1.pdf doc2.pdf doc3.pdf
```

---

### Ejercicio 3: Potencia recursiva con contador de llamadas

Implemente una función recursiva que calcule `base^exponente` sin usar el operador `**`, contando y mostrando al final cuántas llamadas recursivas fueron necesarias.

```
python ej03.py 2 10
```

---

### Ejercicio 4: Suma de dígitos recursiva

Implemente una función recursiva que reciba un número entero y calcule la suma de sus dígitos (por ejemplo, 1234 → 1+2+3+4 = 10).

```
python ej04.py 4821
```

---

### Ejercicio 5: Lista enlazada simple con búsqueda y conteo

Implemente una lista enlazada simple con un método `agregar(valor)`, un método `contar_nodos()` que recorra la lista y devuelva la cantidad de nodos, y un método `buscar(valor)` que indique si el valor existe. Reciba los valores a insertar por línea de comandos.

```
python ej05.py 5 12 8 3 12 9
```

---

### Ejercicio 6: Lista doblemente enlazada con recorrido inverso

Basándose en una lista doblemente enlazada, implemente un método `recorrer_reversa()` que imprima todos los elementos de la lista comenzando desde el último nodo hasta el primero, aprovechando el puntero `prev`.

```
python ej06.py 1 2 3 4 5
```

---

### Ejercicio 7: Comparación de lectura de archivos línea por línea vs completo

Cree un archivo de texto de prueba de al menos 5MB. Implemente dos funciones: una que lea el archivo línea por línea acumulando el conteo de palabras, y otra que lea el archivo completo de una sola vez (`read()`) y luego cuente las palabras. Mida y muestre el tiempo de cada una.

```
python ej07.py archivo_prueba.txt
```

---

### Ejercicio 8: Comparación de tamaño JSON vs Pickle

Reciba un nombre base de archivo por línea de comandos, genere una estructura de datos (por ejemplo, una lista de diccionarios con información de personas) y guárdela tanto en formato JSON como usando `pickle`. Compare e imprima el tamaño en bytes de ambos archivos resultantes.

```
python ej08.py datos
```

---

### Ejercicio 9: Vector dinámico simulado con estrategia de duplicado

Implemente una clase `VectorDinamico` que simule el crecimiento de un vector: cuando se llena, duplica su capacidad interna (usando una lista de Python como respaldo, pero controlando manualmente el tamaño "usado" vs "reservado"). Reciba la cantidad de elementos a insertar por línea de comandos y muestre cuántas veces tuvo que "redimensionarse" el vector.

```
python ej09.py 20
```

---

### Ejercicio 10: Fibonacci recursivo vs iterativo con conteo de operaciones

Implemente dos funciones que calculen el n-ésimo término de Fibonacci: una recursiva (sin memoización) y otra iterativa. Ambas deben contar cuántas operaciones (llamadas o iteraciones) realizaron. Reciba `n` por línea de comandos y compare ambos resultados.

```
python ej10.py 25
```


## Eficiencia y Complejidad Algorítmica en Python

---

### Ejercicio 11: Medición empírica de complejidad lineal vs cuadrática

Reciba un número `n` por línea de comandos. Implemente una función con complejidad O(n) (un solo ciclo que suma los primeros `n` números) y otra con complejidad O(n²) (dos ciclos anidados que recorren una matriz de `n x n`). Mida el tiempo de cada una con el módulo `time` y muestre cuántas veces más lenta fue la versión O(n²).

```
python ej11.py 2000
```

---

### Ejercicio 12: Contador de comparaciones en ordenamiento burbuja

Implemente el algoritmo de ordenamiento burbuja sobre una lista de `n` números aleatorios (`n` recibido por línea de comandos). El programa debe contar cuántas comparaciones realizó en total y mostrar dicho número junto con el valor teórico aproximado de n² para comparar.

```
python ej12.py 100
```

---

### Ejercicio 13: Búsqueda binaria con contador de pasos logarítmicos

Reciba un número `n` por línea de comandos, genere una lista ordenada de `n` elementos y busque el último elemento de la lista utilizando búsqueda binaria. El programa debe contar e imprimir cuántas comparaciones realizó, y comparar ese valor contra `log2(n)` calculado matemáticamente con la librería `math`.

```
python ej13.py 1000000
```

---

## RESPUESTAS

---

### Ejercicio 1

```python
import sys

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pila:
    def __init__(self):
        self.top = None

    def push(self, valor):
        nodo = Nodo(valor)
        nodo.next = self.top
        self.top = nodo

    def pop(self):
        if self.top is None:
            return None
        valor = self.top.valor
        self.top = self.top.next
        return valor

    def esta_vacia(self):
        return self.top is None

def balanceado(expresion):
    pila = Pila()
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in "([{":
            pila.push(caracter)
        elif caracter in ")]}":
            if pila.esta_vacia() or pila.pop() != pares[caracter]:
                return False

    return pila.esta_vacia()

expresion = sys.argv[1]
print("Balanceado" if balanceado(expresion) else "No balanceado")
```

---

### Ejercicio 2

```python
import sys

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Cola:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, valor):
        nodo = Nodo(valor)
        if self.rear is None:
            self.front = self.rear = nodo
            return
        self.rear.next = nodo
        self.rear = nodo

    def dequeue(self):
        if self.front is None:
            return None
        valor = self.front.valor
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return valor

cola = Cola()
for documento in sys.argv[1:]:
    cola.enqueue(documento)

print("Orden de impresión:")
while True:
    documento = cola.dequeue()
    if documento is None:
        break
    print(f"Imprimiendo: {documento}")
```

---

### Ejercicio 3

```python
import sys

llamadas = 0

def potencia(base, exponente):
    global llamadas
    llamadas += 1
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(sys.argv[1])
exponente = int(sys.argv[2])

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")
print(f"Llamadas recursivas realizadas: {llamadas}")
```

---

### Ejercicio 4

```python
import sys

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

numero = int(sys.argv[1])
print(f"Suma de dígitos de {numero}: {suma_digitos(numero)}")
```

---

### Ejercicio 5

```python
import sys

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.head is None:
            self.head = nodo
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nodo

    def contar_nodos(self):
        contador = 0
        actual = self.head
        while actual:
            contador += 1
            actual = actual.next
        return contador

    def buscar(self, valor):
        actual = self.head
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.next
        return False

lista = ListaEnlazada()
for valor in sys.argv[1:]:
    lista.agregar(int(valor))

print(f"Cantidad de nodos: {lista.contar_nodos()}")
print(f"¿Existe el 12?: {lista.buscar(12)}")
```

---

### Ejercicio 6

```python
import sys

class DoubleNode:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.prev = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar(self, valor):
        nodo = DoubleNode(valor)
        if self.head is None:
            self.head = self.tail = nodo
            return
        self.tail.next = nodo
        nodo.prev = self.tail
        self.tail = nodo

    def recorrer_reversa(self):
        actual = self.tail
        elementos = []
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.prev
        print(" -> ".join(elementos))

lista = ListaDoble()
for valor in sys.argv[1:]:
    lista.agregar(int(valor))

print("Recorrido en reversa:")
lista.recorrer_reversa()
```

---

### Ejercicio 7

```python
import sys
import time

def leer_linea_por_linea(nombre_archivo):
    contador_palabras = 0
    with open(nombre_archivo, "r") as f:
        for linea in f:
            contador_palabras += len(linea.split())
    return contador_palabras

def leer_completo(nombre_archivo):
    with open(nombre_archivo, "r") as f:
        contenido = f.read()
    return len(contenido.split())

nombre_archivo = sys.argv[1]

inicio1 = time.time()
palabras1 = leer_linea_por_linea(nombre_archivo)
fin1 = time.time()

inicio2 = time.time()
palabras2 = leer_completo(nombre_archivo)
fin2 = time.time()

print(f"Línea por línea: {palabras1} palabras, tiempo: {fin1 - inicio1:.4f}s")
print(f"Archivo completo: {palabras2} palabras, tiempo: {fin2 - inicio2:.4f}s")
```

---

### Ejercicio 8

```python
import sys
import json
import pickle
import os

nombre_base = sys.argv[1]

datos = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Luis", "edad": 30, "activo": False},
    {"nombre": "Marta", "edad": 22, "activo": True}
]

archivo_json = f"{nombre_base}.json"
archivo_pickle = f"{nombre_base}.pkl"

with open(archivo_json, "w") as f:
    json.dump(datos, f)

with open(archivo_pickle, "wb") as f:
    pickle.dump(datos, f)

tamaño_json = os.path.getsize(archivo_json)
tamaño_pickle = os.path.getsize(archivo_pickle)

print(f"Tamaño JSON: {tamaño_json} bytes")
print(f"Tamaño Pickle: {tamaño_pickle} bytes")
```

---

### Ejercicio 9

```python
import sys

class VectorDinamico:
    def __init__(self):
        self.capacidad = 1
        self.tamaño = 0
        self.datos = [None] * self.capacidad
        self.redimensionamientos = 0

    def insertar(self, valor):
        if self.tamaño == self.capacidad:
            self.capacidad *= 2
            nuevo_arreglo = [None] * self.capacidad
            for i in range(self.tamaño):
                nuevo_arreglo[i] = self.datos[i]
            self.datos = nuevo_arreglo
            self.redimensionamientos += 1
        self.datos[self.tamaño] = valor
        self.tamaño += 1

cantidad = int(sys.argv[1])
vector = VectorDinamico()

for i in range(cantidad):
    vector.insertar(i)

print(f"Elementos insertados: {vector.tamaño}")
print(f"Capacidad final: {vector.capacidad}")
print(f"Cantidad de redimensionamientos: {vector.redimensionamientos}")
```

---

### Ejercicio 10

```python
import sys

llamadas_recursivas = 0

def fib_recursivo(n):
    global llamadas_recursivas
    llamadas_recursivas += 1
    if n <= 1:
        return n
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)

def fib_iterativo(n):
    iteraciones = 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        iteraciones += 1
    return a, iteraciones

n = int(sys.argv[1])

resultado_recursivo = fib_recursivo(n)
resultado_iterativo, iteraciones = fib_iterativo(n)

print(f"Fibonacci({n}) recursivo = {resultado_recursivo}, llamadas: {llamadas_recursivas}")
print(f"Fibonacci({n}) iterativo = {resultado_iterativo}, iteraciones: {iteraciones}")
```

---

### Ejercicio 11

```python
import sys
import time

n = int(sys.argv[1])

def suma_lineal(n):
    total = 0
    for i in range(n):
        total += i
    return total

def suma_cuadratica(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total

inicio1 = time.time()
suma_lineal(n)
fin1 = time.time()
tiempo_lineal = fin1 - inicio1

inicio2 = time.time()
suma_cuadratica(n)
fin2 = time.time()
tiempo_cuadratico = fin2 - inicio2

print(f"Tiempo O(n): {tiempo_lineal:.6f}s")
print(f"Tiempo O(n^2): {tiempo_cuadratico:.6f}s")

if tiempo_lineal > 0:
    print(f"La versión O(n^2) fue aproximadamente {tiempo_cuadratico / tiempo_lineal:.2f} veces más lenta")
```

---

### Ejercicio 12

```python
import sys
import random

n = int(sys.argv[1])
lista = [random.randint(1, 1000) for _ in range(n)]

def burbuja(lista):
    comparaciones = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return comparaciones

comparaciones = burbuja(lista)
teorico = n ** 2

print(f"Comparaciones reales realizadas: {comparaciones}")
print(f"Valor aproximado de n^2: {teorico}")
```

---

### Ejercicio 13

```python
import sys
import math

n = int(sys.argv[1])
lista = list(range(n))
valor_buscado = lista[-1]

def busqueda_binaria(lista, valor):
    comparaciones = 0
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        comparaciones += 1
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return comparaciones
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return comparaciones

comparaciones = busqueda_binaria(lista, valor_buscado)
log_teorico = math.log2(n)

print(f"Comparaciones realizadas: {comparaciones}")
print(f"log2({n}) calculado: {log_teorico:.2f}")
```
