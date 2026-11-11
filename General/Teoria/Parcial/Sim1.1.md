# EXAMEN DE SIMULACRO — 100 Preguntas

**Instrucciones:** marque con una X la opción correcta.

**1.** ¿Qué componente ejecuta las instrucciones matemáticas y lógicas dentro del CPU?

[ ] a) RAM  

[ ] b) ALU  

[ ] c) Caché L1  

[ ] d) Bus de datos

**2.** En una arquitectura de microservicios, ¿cómo se comunican los módulos entre sí?

[ ] a) Compartiendo variables globales 

[ ] b) A través de APIs 

[ ] c) Mediante el segmento .bss  

[ ] d) Recompilando el monolito

**3.** ¿Cuál es la principal desventaja de una arquitectura monolítica frente a microservicios?

[ ] a) No permite usar bases de datos  

[ ] b) Dificultad para escalar y actualizar de forma independiente  

[ ] c) No puede compilarse  

[ ] d) Requiere más lenguajes de programación

**4.** ¿Qué tipo de API usa mensajes XML estrictos y es común en sistemas bancarios?

[ ] a) REST  

[ ] b) GraphQL  

[ ] c) SOAP 

[ ] d) gRPC

**5.** ¿Cuál es la ventaja principal de GraphQL sobre REST?

[ ] a) Usa menos memoria RAM  

[] b) El cliente pide exactamente los campos que necesita  

[ ] c) No requiere HTTP  

[ ] d) Es más antiguo y estable

**6.** El segmento `.text` de un programa se caracteriza por ser:

[ ] a) De solo lectura  

[ ] b) Modificable en tiempo de ejecución  

[ ] c) Parte del Heap  

[ ] d) Volátil solo en ARM

**7.** ¿En qué segmento de memoria se almacena una variable global inicializada?

[ ] a) .bss  

] b) .data  

[ ] c) Stack  

[ ] d) .text

**8.** ¿En qué segmento se almacena una variable global sin inicializar?

[ ] a) .data  

[ ] b) .bss  

[ ] c) Heap  

[ ] d) .text

**9.** La memoria dinámica reservada con `new` en C++ se almacena en:

[ ] a) Stack  

[ ] b) .data  

[ ] c) Heap  

[ ] d) .text

**10.** ¿Qué estructura crece en dirección contraria (hacia direcciones bajas) dentro del espacio de memoria de un programa?

[ ] a) Heap  

[ ] b) Stack  

[ ] c) .bss  

[ ] d) .text

**11.** En C y C++, ¿quién es responsable de liberar la memoria dinámica manualmente?

[ ] a) El sistema operativo automáticamente 

[ ] b) El recolector de basura  

[ ] c) El programador  

[ ] d) El linker

**12.** ¿Cuál lenguaje maneja la memoria dinámica (heap) de forma automática?

[ ] a) C  

[ ] b) C++  

[ ] c) Python  

[ ] d) Ensamblador

**13.** ¿Qué arquitectura de CPU se asocia típicamente a mayor eficiencia energética?

[ ] a) x86  

[ ] b) ARM  

[ ] c) x86-64  

[ ] d) CISC clásico

**14.** ¿Por qué la migración de x86 a ARM en la nube puede generar ahorros económicos?

[ ] a) ARM tiene más registros  

[ ] b) ARM consume menos energía 

[ ] c) ARM no necesita RAM  

[ ] d) ARM compila más rápido

**15.** ¿Qué operación se traduce internamente `v[4] = 18;` en un vector de enteros?

[ ] a) `*(v + 4)`  

[ ] b) `*(v + 4*sizeof(int))` 

[ ] c) `*(v - 4)`  

[ ] d) `v.get(4)`

**16.** Un archivo compilado en x86-64 no puede ejecutarse directamente en ARM porque:

[ ] a) El código fuente se pierde al compilar  

[ ] b) El lenguaje máquina generado es específico de la arquitectura  

[ ] c) ARM no soporta compilación  

[ ] d) El linker lo impide

**17.** ¿Qué proceso combina el código objeto (.obj) con las bibliotecas precompiladas para generar el ejecutable?

[ ] a) Fetch  

[ ] b) Linker 

[ ] c) Heapify  

[ ] d) Bubble Up

**18.** El bytecode de Java (.class) es portable entre arquitecturas porque:

[ ] a) Se ejecuta directamente en el CPU  

[ ] b) Corre sobre la JVM  

[ ] c) No usa RAM  

[ ] d) Es un archivo de texto plano

**19.** ¿Cuál es la principal diferencia entre un lenguaje compilado y uno interpretado?

[ ] a) El interpretado no usa RAM  

[ ] b) El compilado genera un ejecutable antes de correr; el interpretado traduce en tiempo de ejecución  

[ ] c) El compilado siempre es más portable  

[ ] d) No existe diferencia real

**20.** ¿Qué técnica combina interpretación y compilación para acercarse al rendimiento nativo sin perder portabilidad?

[ ] a) Heapify  

[ ] b) JIT (Just-In-Time)  

[ ] c) TCO  

[ ] d) Linking estático

**21.** ¿Qué comando de Git descarga una copia completa de un repositorio remoto a la máquina local?

[ ] a) git pull  

[ ] b) git fetch  

[ ] c) git clone  

[ ] d) git init

**22.** ¿Qué operación de Git reescribe el historial dejando una línea recta de commits?

[ ] a) Merge  

[ ] b) Rebase  

[ ] c) Fetch  

[ ] d) Stash

**23.** ¿Cuál comando permite crear y cambiar a una nueva rama en un solo paso?

[ ] a) git branch  

[ ] b) git switch -c <nombre>  

[ ] c) git commit -b  

[ ] d) git log --graph

**24.** ¿Qué representa un "commit" en Git?

[ ] a) Una rama nueva  

[ ] b) Un snapshot del estado de los archivos en un momento dado  

[ ] c) Un archivo de configuración  

[ ] d) Una copia del repositorio remoto

**25.** ¿Qué comando descarta todos los cambios locales (staged y unstaged) de forma permanente?

[ ] a) git status  

[ ] b) git reset --hard  

[ ] c) git stash  

[ ] d) git diff

**26.** En un flujo CI/CD, ¿qué se ejecuta automáticamente cada vez que se sube un cambio?

[ ] a) El linker manualmente  

[ ] b) Pruebas de unidad y validaciones de calidad  

[ ] c) El heapify  

[ ] d) La recompilación del kernel

**27.** ¿Cuál es el punto de partida en Spec-Driven Development?

[ ] a) Una prueba automatizada  

[ ] b) Una especificación clara de la intención/comportamiento del sistema  

[ ] c) El código ya funcionando  

[ ] d) El commit inicial

**28.** ¿Cuál es el punto de partida en Test-Driven Development (TDD)?

[ ] a) La documentación del usuario final  

[ ] b) Una prueba automatizada que aún falla  

[ ] c) El diagrama de arquitectura  

[ ] d) El archivo de configuración YAML

**29.** En el ciclo Red-Green-Refactor, ¿qué ocurre en la fase "Green"?

[ ] a) Se documenta el sistema  

[ ] b) Se escribe el código mínimo necesario para pasar la prueba  

[ ] c) Se elimina la prueba  

[ ] d) Se hace deploy a producción

**30.** ¿Qué hace la opción "Step Into" (F11) en un debugger?

[ ] a) Salta la función sin entrar en ella  

[ ] b) Entra a ejecutar línea por línea dentro de la función llamada  

[ ] c) Detiene el debugger  

[ ] d) Reinicia el programa

**31.** Un archivo de texto y uno binario se diferencian principalmente en:

[ ] a) El sistema operativo que los crea  

[ ] b) Cómo se almacenan los datos en disco  

[ ] c) El nombre de la extensión únicamente  

[ ] d) Que los binarios no pueden leerse nunca

**32.** ¿Cuántos bits usaba la versión original de ASCII?

[ ] a) 8  

[ ] b) 16  

[ ] c) 7  

[ ] d) 32

**33.** ¿Qué codificación es compatible hacia atrás con ASCII y es la más usada actualmente en la web?

[ ] a) UTF-16  

[ ] b) UTF-32  

[ ] c) UTF-8  

[ ] d) EBCDIC

**34.** ¿Por qué es más eficiente leer un archivo en bloques que carácter por carácter?

[ ] a) Porque reduce la cantidad de operaciones de entrada/salida  

[ ] b) Porque cambia la codificación del archivo  

[ ] c) Porque convierte el archivo a binario automáticamente  

[ ] d) Porque evita usar RAM

**35.** ¿Qué modo de apertura en Python trunca el archivo si ya existe?

[ ] a) 'r'  

[ ] b) 'a'  

[ ] c) 'w'  

[ ] d) 'r+'

**36.** ¿Qué módulo de Python se usa comúnmente para serializar objetos a formato binario?

[ ] a) json  

[ ] b) pickle  

[ ] c) yaml  

[ ] d) os

**37.** ¿Cuál de los siguientes formatos trabaja principalmente por indentación (clave: valor) y es muy legible para humanos?

[ ] a) JSON  

[ ] b) XML  

[ ] c) YAML  

[ ] d) Binario

**38.** ¿Cuál formato es el más común en APIs REST modernas por su ligereza?

[ ] a) XML  

[ ] b) JSON  

[ ] c) YAML  

[ ] d) CSV binario

**39.** El CPU se comunica directamente con:

[ ] a) El disco duro  

[ ] b) La RAM  

[ ] c) La red  

[ ] d) El SSD

**40.** ¿Cuál es la función principal de la caché del CPU?

[ ] a) Guardar el sistema operativo completo  

[ ] b) Mantener información cercana al CPU para reducir viajes a RAM  

[ ] c) Reemplazar al disco duro  

[ ] d) Ejecutar instrucciones lógicas

**41.** Un TDA (Tipo de Dato Abstracto) se define principalmente por:

[ ] a) Su implementación específica en un lenguaje  

[ ] b) Los datos que guarda y las operaciones que permite  

[ ] c) El nombre de la clase  

[ ] d) La cantidad de memoria RAM disponible

**42.** ¿Qué característica de un vector permite acceso en O(1)?

[ ] a) Que use punteros dobles  

[ ] b) Que su memoria esté asignada de forma contigua  

[ ] c) Que sea dinámico  

[ ] d) Que use recursión

**43.** ¿Qué técnica reduce drásticamente el número de copias al redimensionar un vector dinámico?

[ ] a) Reducir el vector a la mitad cada vez  

[ ] b) Expansión x2 del tamaño  

[ ] c) Usar solo memoria estática  

[ ] d) Convertirlo en lista enlazada

**44.** ¿Qué operación en un vector dinámico se conoce como "Deep Copy"?

[ ] a) Copiar solo la dirección de memoria  

[ ] b) Copiar todos los elementos a un nuevo espacio de memoria  

[ ] c) Eliminar el vector  

[ ] d) Ordenar el vector

**45.** ¿Qué estructura NO requiere memoria contigua para almacenar sus elementos?

[ ] a) Vector estático  

[ ] b) Vector dinámico  

[ ] c) Lista enlazada simple  

[ ] d) Arreglo en C

**46.** ¿Cuál es la complejidad de buscar un elemento por posición en una lista enlazada simple?

[ ] a) O(1)  

[ ] b) O(n)  

[ ] c) O(log n)  

[ ] d) O(n²)

**47.** Una cola (Queue) sigue el principio:

[ ] a) LIFO  

[ ] b) FIFO  

[ ] c) Acceso directo  

[ ] d) Aleatorio

**48.** Una pila (Stack) sigue el principio:

[ ] a) FIFO  

[ ] b) LIFO  

[ ] c) Balanceado  

[ ] d) Ninguno de los anteriores

**49.** ¿Cuáles son las dos operaciones principales de una pila?

[ ] a) enqueue y dequeue  

[ ] b) push y pop  

[ ] c) insert y delete  

[ ] d) get y set

**50.** ¿Cuáles son las dos operaciones principales de una cola?

[ ] a) push y pop  

[ ] b) enqueue y dequeue  

[ ] c) top y peek  

[ ] d) heapify y bubble up

**51.** Si una cola solo mantiene referencia al *front*, insertar al final tiene complejidad:

[ ] a) O(1)  

[ ] b) O(log n)  

[ ] c) O(n)  

[ ] d) O(n²)

**52.** ¿Cuál es un caso de uso típico de una pila?

[ ] a) Cola de impresión  

[ ] b) Función "Deshacer" (Undo) de un editor  

[ ] c) BFS en grafos  

[ ] d) Gestión de turnos en un banco

**53.** ¿Cuál es un caso de uso típico de una cola?

[ ] a) Historial de "atrás" del navegador  

[ ] b) Stack de llamadas del CPU  

[ ] c) Gestión de procesos en orden de llegada en un sistema operativo  

[ ] d) Balanceo de paréntesis

**54.** ¿Qué información adicional necesita una lista doblemente enlazada respecto a una simple?

[ ] a) Un puntero al elemento raíz  

[ ] b) Un puntero `prev` en cada nodo  

[ ] c) Un arreglo auxiliar  

[ ] d) Un contador global de nodos

**55.** El "overhead" de una estructura de datos se refiere a:

[ ] a) La cantidad de datos útiles almacenados  

[ ] b) La memoria adicional requerida por la estructura interna, además de los datos  

[ ] c) El tiempo de compilación  

[ ] d) El número de hilos usados

**56.** ¿Por qué implementar una cola con lista doblemente enlazada es ineficiente en memoria?

[ ] a) Porque una cola nunca necesita recorrerse hacia atrás  

[ ] b) Porque las colas no permiten punteros  

[ ] c) Porque no cabe en RAM  

[ ] d) Porque rompe el principio FIFO

**57.** En Python, ¿qué estructura de la librería estándar es recomendada para implementar pilas y colas eficientes?

[ ] a) list  

[ ] b) tuple  

[ ] c) collections.deque  

[ ] d) set

**58.** ¿Qué elementos requiere obligatoriamente una función recursiva bien definida?

[ ] a) Un ciclo for  

[ ] b) Un caso base y un caso recursivo  

[ ] c) Una variable global  

[ ] d) Un puntero nulo

**59.** ¿Qué registro del CPU almacena la dirección de la siguiente instrucción a ejecutar?

[ ] a) RSP  

[ ] b) RIP  

[ ] c) ALU  

[ ] d) RBX

**60.** ¿Qué registro del CPU actúa como puntero al tope de la pila del sistema?

[ ] a) RIP  

[ ] b) RSP  

[ ] c) EAX  

[ ] d) PC lógico

**61.** Cada llamada a una función recursiva genera en la pila del sistema un:

[ ] a) Heapify  

[ ] b) Stack frame  

[ ] c) Bytecode  

[ ] d) Bubble down

**62.** ¿Qué técnica de recursión permite, ante un "punto muerto", regresar y probar otra alternativa?

[ ] a) Memoización  

[ ] b) Backtracking  

[ ] c) Heapify  

[ ] d) TCO

**63.** ¿Qué ocurre si una función recursiva no tiene un caso base bien definido?

[ ] a) Se optimiza automáticamente  

[ ] b) Puede causar un Stack Overflow  

[ ] c) El compilador la convierte en iterativa  

[ ] d) Se ejecuta en O(1)

**64.** La recursión de cola (tail recursion) se caracteriza porque:

[ ] a) La llamada recursiva es la primera instrucción de la función  

[ ] b) La llamada recursiva es la última instrucción, sin operaciones pendientes después  

[ ] c) Nunca tiene caso base  

[ ] d) Solo existe en Python

**65.** ¿Python implementa optimización de llamadas de cola (TCO) de forma nativa?

[ ] a) Sí, siempre  

[ ] b) No  

[ ] c) Solo en Python 3.12+  

[ ] d) Solo con recursión de árbol

**66.** En general, ¿qué se prefiere entre recursión e iteración por rendimiento?

[ ] a) Recursión siempre  

[ ] b) Iteración, salvo que el problema sea naturalmente recursivo  

[ ] c) Es indiferente  

[ ] d) Ninguna de las dos, solo bucles while anidados

**67.** ¿Qué mide principalmente el análisis de complejidad algorítmica (Big-O)?

[ ] a) El tiempo real en segundos  

[ ] b) La cantidad de instrucciones que ejecuta el algoritmo según el tamaño de entrada  

[ ] c) El consumo de batería  

[ ] d) La cantidad de líneas de código

**68.** ¿Qué notación representa la cota superior (peor caso) de un algoritmo?

[ ] a) Big-Omega (Ω)  

[ ] b) Big-Theta (Θ)  

[ ] c) Big-O (O)  

[ ] d) Big-Sigma

**69.** ¿Qué notación representa la cota inferior (mejor caso)?

[ ] a) Big-O  

[ ] b) Big-Omega (Ω)  

[ ] c) Big-Theta  

[ ] d) Ninguna

**70.** Al simplificar `O(3n) + O(5)`, el resultado final es:

[ ] a) O(3n+5)  

[ ] b) O(n)  

[ ] c) O(15n)  

[ ] d) O(1)

**71.** ¿Qué complejidad tiene una búsqueda binaria sobre un arreglo ordenado?

[ ] a) O(1)  

[ ] b) O(n)  

[ ] c) O(log n)  

[ ] d) O(n²)

**72.** ¿Qué complejidad tiene un algoritmo con dos ciclos `for` anidados que recorren completamente n elementos cada uno?

[ ] a) O(n)  

[ ] b) O(log n)  

[ ] c) O(n²)  

[ ] d) O(n log n)

**73.** La técnica de memoización mejora principalmente:

[ ] a) El uso de disco duro  

[ ] b) El tiempo de ejecución, a cambio de más memoria  

[ ] c) La legibilidad del código  

[ ] d) La portabilidad entre arquitecturas

**74.** ¿Qué complejidad es típica del cálculo de Fibonacci recursivo sin memoización?

[ ] a) O(n)  

[ ] b) O(log n)  

[ ] c) O(2ⁿ)  

[ ] d) O(n log n)

**75.** ¿Qué complejidad es típica de un algoritmo de fuerza bruta que prueba todas las permutaciones posibles?

[ ] a) O(n²)  

[ ] b) O(n!)  

[ ] c) O(n log n)  

[ ] d) O(log n)

**76.** En un Binary Heap Máximo, la relación que se cumple es:

[ ] a) El padre es siempre menor que sus hijos  

[ ] b) El padre es siempre mayor que sus hijos  

[ ] c) Los hermanos deben estar ordenados entre sí  

[ ] d) Es idéntico a un BST

**77.** Un Binary Heap se diferencia de un Árbol Binario de Búsqueda (BST) porque:

[ ] a) El heap no garantiza orden entre hermanos ni subárboles, solo padre-hijo  

[ ] b) El heap siempre está balanceado alfabéticamente  

[ ] c) El BST no puede representarse en vector  

[ ] d) No hay diferencia, son lo mismo

**78.** Dado un nodo en la posición `i` de un heap representado como vector, ¿cuál es la fórmula correcta para encontrar a su padre?

[ ] a) i/2  

[ ] b) (i-1)/2  

[ ] c) (i*2)+1  

[ ] d) (i*2)+2

**79.** ¿Cuál es la fórmula para encontrar el hijo izquierdo de un nodo en posición `i`?

[ ] a) (i-1)/2  

[ ] b) (i*2)+1  

[ ] c) (i*2)+2  

[ ] d) i/2

**80.** ¿Qué operación se usa para restaurar la propiedad de heap después de insertar un nuevo elemento al final?

[ ] a) Heapify completo  

[ ] b) Bubble Up  

[ ] c) Merge  

[ ] d) Partición

**81.** ¿Cuál es la complejidad de insertar un elemento en un heap?

[ ] a) O(1)  

[ ] b) O(n)  

[ ] c) O(log n)  

[ ] d) O(n²)

**82.** ¿Cuál es la complejidad de obtener el elemento máximo en un Heap Máximo?

[ ] a) O(n)  

[ ] b) O(log n)  

[ ] c) O(1)  

[ ] d) O(n log n)

**83.** ¿Cuál es la complejidad total del proceso de Heapify sobre un vector completo?

[ ] a) O(n log n)  

[ ] b) O(n)  

[ ] c) O(log n)  

[ ] d) O(n²)

**84.** Una cola de prioridad implementada con Heap, comparada con una implementada con lista enlazada, ofrece:

[ ] a) Peor rendimiento siempre  

[ ] b) Mejor rendimiento en insertar/extraer (O(log n) vs O(n))  

[ ] c) El mismo rendimiento exacto  

[ ] d) Solo mejora el espacio, no el tiempo

**85.** ¿Qué algoritmo clásico de caminos más cortos en grafos usa una cola de prioridad basada en heap?

[ ] a) Bubble Sort  

[ ] b) Dijkstra  

[ ] c) Counting Sort  

[ ] d) TDD

**86.** En Python, el módulo `heapq` implementa internamente:

[ ] a) Un Heap Máximo  

[ ] b) Un Heap Mínimo  

[ ] c) Una lista doblemente enlazada  

[ ] d) Un árbol AVL

**87.** ¿Qué algoritmo de ordenamiento compara siempre elementos adyacentes e intercambia si están en el orden incorrecto?

[ ] a) Selección  

[ ] b) Burbuja  

[ ] c) Quicksort  

[ ] d) Counting Sort

**88.** ¿Cuál es la cantidad exacta de comparaciones que realiza Selection Sort, sin importar el orden inicial de los datos?

[ ] a) n-1  

[ ] b) (n²-n)/2  

[ ] c) n log n  

[ ] d) 2n

**89.** ¿Cuál es la cantidad de intercambios en el peor caso de Selection Sort?

[ ] a) (n²-n)/2  

[ ] b) n-1  

[ ] c) 0  

[ ] d) n²

**90.** ¿Cuál es la cantidad de comparaciones en el mejor caso de Insertion Sort (arreglo ya ordenado)?

[ ] a) (n²-n)/2  

[ ] b) n-1  

[ ] c) n²  

[ ] d) log n

**91.** ¿Cuál es la cantidad de intercambios/desplazamientos en el peor caso de Insertion Sort?

[ ] a) n-1  

[ ] b) (n²-n)/2  

[ ] c) 0  

[ ] d) n log n

**92.** Si se tienen limitaciones fuertes de escritura en disco (cada escritura es costosa), ¿qué algoritmo de los dos siguientes conviene más: Selección o Inserción?

[ ] a) Inserción, porque tiene menos comparaciones siempre  

[ ] b) Selección, porque en el peor caso solo hace n-1 intercambios  

[ ] c) Ambos son iguales en intercambios  

[ ] d) Ninguno, se debe usar Bubble Sort

**93.** ¿Cuál es la principal diferencia entre Selection Sort e Insertion Sort en cuanto a intercambios?

[ ] a) Selección hace como máximo un intercambio por pasada; Inserción puede desplazar varios elementos por pasada  

[ ] b) Ambos hacen la misma cantidad de intercambios  

[ ] c) Inserción nunca hace intercambios  

[ ] d) Selección siempre es O(n)

**94.** ¿Qué estrategia de selección de pivote en Quicksort agrega una complejidad O(n) adicional al algoritmo?

[ ] a) Elegir el primer elemento  

[ ] b) Elegir la mediana  

[ ] c) Elegir un elemento aleatorio  

[ ] d) Elegir el último elemento

**95.** ¿Qué estrategia de selección de pivote en Quicksort suele tener un rendimiento similar a usar la mediana, sin el costo adicional de calcularla?

[ ] a) Elegir siempre el primer elemento  

[ ] b) Elegir un elemento aleatorio (random)  

[ ] c) Elegir siempre el último elemento  

[ ] d) No elegir pivote

**96.** ¿En qué caso Quicksort alcanza su peor caso O(n²)?

[ ] a) Cuando el arreglo ya está desordenado aleatoriamente  

[ ] b) Cuando el pivote elegido resulta ser siempre el menor o el mayor elemento (particiones desbalanceadas)  

[ ] c) Cuando se usa recursión de cola  

[ ] d) Cuando el arreglo tiene números repetidos

**97.** ¿Qué algoritmo de ordenamiento garantiza O(n log n) en todos los casos pero requiere O(n) de espacio adicional?

[ ] a) Quicksort  

[ ] b) Heapsort  

[ ] c) Mergesort  

[ ] d) Selection Sort

**98.** ¿Qué algoritmo de ordenamiento garantiza O(n log n) en todos los casos Y usa espacio O(1) (in-place), sacrificando estabilidad?

[ ] a) Mergesort  

[ ] b) Heapsort  

[ ] c) Bubble Sort  

[ ] d) Counting Sort

**99.** ¿Qué algoritmo de ordenamiento NO realiza comparaciones directas entre elementos, sino que cuenta ocurrencias dentro de un rango conocido?

[ ] a) Quicksort  

[ ] b) Mergesort  

[ ] c) Counting Sort  

[ ] d) Heapsort

**100.** Radix Sort depende de que su subrutina interna (Counting Sort) sea estable porque:

[ ] a) Sin estabilidad no compila  

[ ] b) El orden logrado en pasadas de dígitos menos significativos debe preservarse al ordenar por dígitos más significativos  

[ ] c) Solo así soporta números negativos  

[ ] d) La estabilidad reduce el uso de memoria

---

## Soluciones del Examen de Simulacro

| # | R | # | R | # | R | # | R | # | R |
|---|---|---|---|---|---|---|---|---|---|
| 1 | b | 21 | c | 41 | b | 61 | b | 81 | c |
| 2 | b | 22 | b | 42 | b | 62 | b | 82 | c |
| 3 | b | 23 | b | 43 | b | 63 | b | 83 | b |
| 4 | c | 24 | b | 44 | b | 64 | b | 84 | b |
| 5 | b | 25 | b | 45 | c | 65 | b | 85 | b |
| 6 | a | 26 | b | 46 | b | 66 | b | 86 | b |
| 7 | b | 27 | b | 47 | b | 67 | b | 87 | b |
| 8 | b | 28 | b | 48 | b | 68 | c | 88 | b |
| 9 | c | 29 | b | 49 | b | 69 | b | 89 | b |
| 10 | b | 30 | b | 50 | b | 70 | b | 90 | b |
| 11 | c | 31 | b | 51 | c | 71 | c | 91 | b |
| 12 | c | 32 | c | 52 | b | 72 | c | 92 | b |
| 13 | b | 33 | c | 53 | c | 73 | b | 93 | a |
| 14 | b | 34 | a | 54 | b | 74 | c | 94 | b |
| 15 | b | 35 | c | 55 | b | 75 | b | 95 | b |
| 16 | b | 36 | b | 56 | a | 76 | b | 96 | b |
| 17 | b | 37 | c | 57 | c | 77 | a | 97 | c |
| 18 | b | 38 | b | 58 | b | 78 | b | 98 | b |
| 19 | b | 39 | b | 59 | b | 79 | b | 99 | c |
| 20 | b | 40 | b | 60 | b | 80 | b | 100| b |
