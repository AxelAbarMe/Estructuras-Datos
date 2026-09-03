# =========================================
# SEGMENTOS 1-2: ARQUITECTURAS DE SOFTWARE Y MEMORIA
# =========================================

## Arquitectura Monolítica
- Todo el código fuente vive en un solo proyecto/lenguaje; se compila a un único ejecutable (Artifact/.exe).
- Corre en un servidor que consume Compute (CPU + RAM).
- Desventajas: difícil de escalar (si no se diseñó para múltiples servidores) y actualizar (hay que bajar todo el servidor).

## Arquitectura de Microservicios
- Cada funcionalidad se separa en un módulo/servicio independiente, cada uno en su propio contenedor.
- Principio de responsabilidad única llevado al nivel de servicio.
- Ventajas: cada servicio puede usar un lenguaje distinto (Java, Python, Rust...), escalado agregando contenedores, actualización por versión (v1 -> v2) sin tumbar todo el sistema.
- Da origen a las **Apps Cloud Native**: escalables y elásticas.
- La comunicación entre módulos se da mediante **APIs** (interfaz pública expuesta de un objeto/servicio).
  * REST (la más común, basada en HTTP y verbos GET/POST/PUT/DELETE)
  * SOAP (XML estricto, típico en banca/empresarial)
  * GraphQL (el cliente pide exactamente los campos que necesita, evita sobrecarga)

## Ejecución de un programa (RAM y CPU = "Compute")
- Código fuente en HDD/SSD (persistente) -> se carga a RAM (volátil) -> CPU ejecuta.
- El disco NO participa en la ejecución en sí, solo almacena.
- Ciclo de instrucción del CPU: **Fetch** (traer instrucción) -> **Decode** (decodificar) -> **Execute** (ejecutar).
- La **ALU** ejecuta operaciones aritmético-lógicas y guarda resultado en Registros.

## Arquitecturas de CPU
| Arquitectura | Potencia | Consumo |
|---|---|---|
| x86-64 (Intel/AMD) | Mayor | Mayor |
| ARM (abierta, multi-fabricante) | Menor | Menor |
- ARM domina en móviles por eficiencia energética; en la nube, migrar de x86 a ARM reduce costos.
- El tamaño de `int` depende de la arquitectura (ej. 4 bytes en x86-64 típico vs variaciones en ARM); esto afecta la portabilidad de binarios compilados.

## Memoria y direcciones
- 1 byte = mínimo direccionable; direcciones en hexadecimal (0x0000...).
- Espacio de direcciones de un programa (de low a high address):
  1. **.text (segmento código):** instrucciones, Read-Only.
  2. **.data:** variables globales/estáticas YA inicializadas.
  3. **.bss:** variables globales/estáticas SIN inicializar.
  4. **Heap:** memoria dinámica (`new`/`malloc` en C/C++; automática en Python/Java). Crece hacia arriba. Mal manejo -> Memory Leak / Out of Memory.
  5. **Stack:** variables locales y retornos de función. Crece hacia direcciones bajas (al revés).
  6. Argumentos de línea de comandos y variables de entorno (high address).
- El compilador genera una **tabla de símbolos** (nombre, tipo, alcance de cada variable).
- Punteros: `x` (variable puntero) vive en el stack; el valor que contiene es una dirección; `*x` desreferencia (da el valor apuntado); `&x` da la dirección donde vive `x`.

## Compilación (C/C++, Java)
- Código fuente -> compilador -> `.obj` (lenguaje máquina según arquitectura, NO portable entre x86/ARM).
- **Linker:** mezcla el `.obj` propio con bibliotecas precompiladas -> genera el `.exe`.
- **Debug** = mismo proceso + flag que hace que el CPU ejecute línea por línea.
- Java es un caso especial: el `.obj`/`.class` es **bytecode**, corre sobre la JVM -> por eso Java sí es portable entre arquitecturas.

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_1-2_Apuntes.md) - Arquitectura, Memory Segment, Monolítico vs Microservicios, Compiler vs Interpreter

# =========================================
# SEGMENTO 3: LENGUAJES INTERPRETADOS, GIT, METODOLOGÍAS
# =========================================

## Lenguajes interpretados (Python, JavaScript)
- Un intérprete (VM Runtime) lee una instrucción, genera Bytecode para esa instrucción según arquitectura, la manda a RAM/CPU, y repite con la siguiente.
- Más lento que compilado (repite el proceso instrucción por instrucción) pero más portable (mismo código corre en distintas arquitecturas) y más simple de programar/depurar.
- **JIT (Just-In-Time):** híbrido que compila bytecode a nativo en tiempo de ejecución (JVM, motor V8 de JS) buscando rendimiento cercano al compilado sin perder portabilidad.

## Git — Control de versiones
- **Commit:** snapshot del estado de archivos en un momento dado; Git solo guarda cambios (delta), no copias completas.
- **Push / Pull (Fetch+Merge) / Merge (Merge o Rebase).**
- **Rebase:** reescribe el historial en línea recta (más limpio). **Merge:** conserva las ramas y crea un commit de unión.
- **Branches:** permiten trabajar en paralelo sin afectar main/master hasta que el código esté probado.
- **CI/CD:** automatiza pruebas (QA), construcción de contenedores y despliegue; se apoya en Cloud Computing.
- **Unit Testing:** funciones que verifican una unidad de código.

Comandos clave: `git init`, `git clone <url>`, `git add`, `git commit -m`, `git status`, `git switch -c` / `git checkout -b` (crear rama), `git branch`, `git diff`, `git restore`, `git reset --hard`, `git stash`, `git rebase -i`, `git log --oneline`, `git blame`, `git cherry-pick`, `git remote add`, `git push -u origin <rama>`, `git pull --rebase`.

## Metodologías de desarrollo
- **Spec-Driven Development:** primero se escribe una especificación clara (comportamiento, entradas, salidas, restricciones) que se vuelve fuente de verdad; el punto de partida es la *intención*. Muy relevante para desarrollo asistido por IA.
- **Test-Driven Development (TDD):** las pruebas se escriben ANTES del código. Ciclo **Red-Green-Refactor**:
  1. Red: se escribe una prueba que falla porque el código no existe.
  2. Green: se escribe el código mínimo para pasarla.
  3. Refactor: se limpia el código manteniendo las pruebas en verde.
- Diferencia clave: TDD parte de una prueba ejecutable; Spec-Driven parte de una especificación en lenguaje natural/semi-formal.

## Debugger
- Breakpoints, **Run** (directo) vs **Debug** (flag paso a paso).
- **Step Over (F10):** no entra a la función llamada. **Step Into (F11):** entra a la función.
- **Call Stack:** muestra las llamadas activas. **Variables:** muestra `.data`/`.bss`. **Watch:** expresiones en tiempo real.

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_3_Apuntes.md) - Compiler vs Interpreter, Git, Debugger

# =========================================
# SEGMENTO 4: ARCHIVOS
# =========================================

## Texto vs Binario
- **Texto:** secuencia de caracteres legibles, cada carácter se representa según una codificación.
- **Binario:** representación directa en formato máquina (bits), no legible directamente.
- Los binarios generalmente ocupan MENOS espacio y son más rápidos de leer/escribir (no requieren traducción carácter por carácter).

## Codificación de caracteres
- **ASCII:** 7 bits (128 caracteres) originalmente, extendido a 8 bits (256). Ej: 'A'=65=01000001.
- **Unicode:** hasta ~240,000 caracteres, soporta múltiples idiomas/alfabetos.
- **UTF-8:** codificación de Unicode más usada; compatible hacia atrás con ASCII (1 byte para los primeros 128 caracteres). También existen UTF-16 y UTF-32.
- Emisor y receptor deben usar el MISMO mecanismo de codificación o se corrompen los caracteres.

## Rendimiento de archivos
- Disco (HDD/SSD) -> RAM -> CPU (el CPU solo se comunica con RAM, nunca directo con disco).
- Cargar un archivo a memoria es costoso en tiempo.
- Jerarquía: CPU (rápido, poco espacio) > RAM > HDD (lento, mucho espacio).
- **Caché:** guarda información cercana al CPU para evitar viajes a RAM/disco repetidos (clave para *High Performance*).
- Leer/escribir en bloques (o toda la info de una vez) es más eficiente que hacerlo byte por byte (menos operaciones de I/O).
- Comparativa real (1,000,000 registros): el archivo binario pesa menos y se lee/escribe más rápido que el equivalente en texto.

## Modos de apertura en Python (`open()`)
- `'r'`/`'r+'`: lectura (y escritura); falla si no existe.
- `'w'`/`'w+'`: escritura, trunca o crea el archivo.
- `'a'`/`'a+'`: agrega al final, crea si no existe.
- Sufijo `'b'` (`'rb'`, `'wb'`, `'ab'`): modo binario.

```python
with open("datos.txt", "r") as f:
    contenido = f.read()
```

## Serialización
- Convertir datos de memoria (RAM) a un formato guardable en disco (y viceversa).
- **pickle** en Python: `pickle.dump()` serializa, `pickle.load()` deserializa.
- Los binarios se leen sabiendo cuántos bytes leer (no caracteres).

## Formatos de archivo estructurados
- **XML:** por etiquetas (`<tag>valor</tag>`); común en sistemas empresariales/SOAP.
- **JSON:** por llaves `{ "clave": valor }`; el más usado en APIs REST por ser ligero.
- **YAML:** por indentación `clave: valor`; muy usado en archivos de configuración (Docker Compose, CI/CD) por legibilidad humana.

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_4_Apuntes.md) - Archivos (.txt | .bin | .json | .xml | .yaml)

# =========================================
# SEGMENTO 5: TDA — TIPOS DE DATOS ABSTRACTOS (LINEALES)
# =========================================

## Concepto de TDA
- Un TDA se define por los **datos** que guarda y las **operaciones** que permite (no por su implementación interna, que puede variar).
- Permite elegir la estructura más eficiente según el problema.

## Vector (Arreglo)
- Memoria **contigua**; se debe conocer/reservar el tamaño de antemano.
- `v[i]` se traduce internamente en `*(v + i*sizeof(tipo))` -> **Acceso Directo, O(1)**.
- **Vector estático** (tamaño fijo, ej. `int v[5]` en C++) vs **Vector dinámico** (`realloc`, requiere buscar nuevo espacio, copiar todo -> **Deep Copy**, liberar el anterior).
- Redimensionar 1 en 1 es ineficiente (para n inserciones, ~O(n²) operaciones acumuladas vía suma de Gauss); la solución estándar es la **expansión x2** (duplicar capacidad), que reduce drásticamente el número total de copias (amortiza a O(1) por inserción en promedio).
- Operaciones: Insertar, Borrar, Buscar.

## Lista Enlazada Simple
- Cada **Nodo** guarda un dato y un puntero `next` al siguiente nodo; no requiere memoria contigua.
```python
class Nodo:
    def __init__(self, dato=None, next=None):
        self.dato = dato
        self.next = next
```
- Operaciones: Insertar, Borrar, Buscar (recorrido secuencial, O(n) para buscar).

## Cola (Queue) — FIFO
- **First In, First Out.**
- `enqueue()`: inserta por *tail/rear*. `dequeue()`: extrae por *head/front*.
- Con referencia directa a front y rear: ambas operaciones son **O(1)**; si solo se tiene *front*, insertar al final degrada a O(n).
- Usos: colas de impresión, procesos del SO, peticiones de servidor, BFS en árboles/grafos.

## Pila (Stack) — LIFO
- **Last In, First Out.**
- `push()`: inserta en el tope. `pop()`: extrae y elimina el tope. `top()`/`peek()`: consulta el tope sin eliminar.
- Todas las operaciones son **O(1)** (solo se manipula un extremo).
- Usos: Undo de editores, historial "atrás" del navegador, balanceo de paréntesis, **stack de llamadas del CPU** (base de la recursión). Un exceso de `push` sin `pop` -> **Stack Overflow**.

> Vector, Lista Enlazada, Cola y Pila son estructuras **lineales**. Existen también estructuras **no lineales** (árboles, grafos, tablas hash) donde los elementos se relacionan jerárquica o reticularmente, no de forma secuencial.

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_5_Apuntes.md) - TDA Simple (Lista enlazada simple, vector, stack, queue)

# =========================================
# SEGMENTO 6: LISTAS DOBLEMENTE ENLAZADAS, COLAS Y PILAS (IMPLEMENTACIÓN)
# =========================================

## Lista Doblemente Enlazada
- Cada nodo tiene `prev`, `data` y `next` -> permite recorrer la lista en ambas direcciones (una lista simple solo avanza y obligaría a reiniciar desde el head para "retroceder").
- Ejemplo típico de uso: un carrusel de imágenes (`< [ ] >`).
```python
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
```
- **Overhead:** memoria extra necesaria por la estructura misma (los punteros `prev`/`next`), no por los datos útiles. A mayor cantidad de nodos, mayor el costo acumulado de overhead; relevante en hardware con RAM limitada.

## Cola implementada con lista simple
- Usar una lista doblemente enlazada para una cola desperdicia memoria (overhead innecesario), porque una cola nunca retrocede manualmente; basta una lista simple con referencias a `front` y `rear`.
```python
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        nuevo = Nodo(value)
        if self.rear is None:
            self.front = self.rear = nuevo
            return
        self.rear.next = nuevo
        self.rear = nuevo
```

## Pila implementada con lista simple
```python
class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        n = Nodo(value)
        n.next = self.top
        self.top = n
    def pop(self):
        if self.top is None:
            return None
        v = self.top.value
        self.top = self.top.next
        return v
```
- Colas y pilas se pueden implementar con vector o con lista enlazada; lo importante es saber **cuándo usar cada TDA**, no memorizar la implementación (en Python existen `queue.Queue`, `queue.LifoQueue`, y sobre todo `collections.deque`, la opción recomendada para ambas por su eficiencia al insertar/eliminar en los extremos).

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_6_Apuntes.md) - Lista doblemente enlazada, stack, queue

# =========================================
# SEGMENTO 7: RECURSIÓN
# =========================================

## Definición
- Una función que se llama a sí misma. Requiere:
  1. **Caso base** (detiene la recursión).
  2. **Caso recursivo / repetición** (avanza hacia el caso base).
- Sin caso base -> recursión infinita -> **Stack Overflow**.

## Registros del CPU relevantes
- **RIP (Instruction Pointer):** dirección de la siguiente instrucción a ejecutar.
- **RSP (Stack Pointer):** dirección del tope actual de la pila del sistema.
- Cada llamada crea un **Stack Frame** (guarda parámetros, variables locales y dirección de retorno `RET`).
- Cada llamada = `push` al stack; cada `return` = `pop` del stack (regresa a la dirección `RET` guardada).
- Variables locales con el mismo nombre en distintas llamadas NO se pisan entre sí: cada una vive en su propio stack frame.

## Backtracking
- Técnica donde, ante un "punto muerto" (dead point), el algoritmo recursivo puede devolverse (pop) y probar otro camino. Ejemplo clásico: resolver un laberinto.

## Recursión vs. Iteración
- En general la versión iterativa rinde mejor (menos overhead de stack frames); se prefiere recursión solo cuando el problema es naturalmente recursivo o muy difícil de plantear iterativamente.

## Recursión de cola (Tail Recursion)
- Ocurre cuando la llamada recursiva es la última instrucción de la función, sin operaciones pendientes después.
- Los compiladores pueden aplicar **TCO (Tail Call Optimization)** y reutilizar el mismo stack frame (equivalente a un ciclo).
- **Python NO implementa TCO**: cada llamada recursiva de cola sigue consumiendo un stack frame nuevo -> puede producir `RecursionError`.

## Divide y Vencerás (ejemplos clásicos)
```python
def sumatoria(n):
    if n == 0:
        return 0
    return n + sumatoria(n-1)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```
- Cada llamada apila un stack frame con su `RET` pendiente; los resultados se resuelven "de abajo hacia arriba" conforme se hace `pop` de cada frame.

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_7_Apuntes.md) - Recursividad

# =========================================
# SEGMENTO 8: EFICIENCIA (COMPLEJIDAD ALGORÍTMICA)
# =========================================

## Aspectos de la eficiencia
- **Tiempo (CPU):** se mide en cantidad de instrucciones ejecutadas, NO en segundos reales (el hardware varía).
- **Espacio (RAM):** memoria adicional que consume el algoritmo.
- Mejorar tiempo puede implicar sacrificar espacio (y viceversa) -> **trade-off tiempo/espacio**. Ejemplo: **memoización** (guardar resultados ya calculados en una estructura auxiliar, ej. Fibonacci pasa de O(2ⁿ) a O(n) a cambio de más memoria).

## Cotas
- **Cota superior (Big-O, "O"):** peor caso; la más usada en la práctica.
- **Cota inferior (Big-Omega, "Ω"):** mejor caso.
- **Cota ajustada (Big-Theta, "Θ"):** cuando el mejor y peor caso coinciden.

## Simplificación de Big-O
- Se suman las complejidades de cada bloque, se elimina todo lo que no sea el término dominante y se eliminan las constantes multiplicativas.
  * Ej: O(2n) + O(4) -> se descarta O(4) (constante) -> O(2n) -> se elimina el 2 -> **O(n)**.

## Tipos de complejidad más comunes (de mejor a peor)
| Complejidad | Nombre | Ejemplo típico |
|---|---|---|
| O(1) | Constante | Acceso directo a un vector |
| O(log n) | Logarítmica | Búsqueda binaria, árbol binario |
| O(n) | Lineal | Recorrer lista enlazada |
| O(n log n) | Lineal-Logarítmica | Mergesort, Heapsort, Quicksort (promedio) |
| O(n²) | Cuadrática | Ciclos anidados, Bubble/Selection Sort |
| O(2ⁿ) | Exponencial | Fibonacci recursivo sin memoización |
| O(n!) | Factorial | Fuerza bruta de permutaciones (vendedor viajero) |

## Tabla de crecimiento (aprox. de instrucciones)
| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) |
|---|---|---|---|---|---|
| 10 | 1 | ~3 | 10 | ~33 | 100 |
| 100 | 1 | ~7 | 100 | ~664 | 10,000 |
| 1,000 | 1 | ~10 | 1,000 | ~9,966 | 1,000,000 |

- Esto justifica por qué se prefiere O(1) del vector sobre O(n) de una lista enlazada para acceso por posición, y por qué se evitan ciclos anidados sobre grandes volúmenes de datos.

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_8_Apuntes.md) - Eficiencia y O Grande

# =========================================
# SEGMENTO 9: HEAPS Y COLAS DE PRIORIDAD
# =========================================

## Heap (Binary Heap)
- Árbol binario **completo** (se llenan los hijos de izquierda a derecha, nivel por nivel, sin huecos).
- No es lo mismo que un BST: solo garantiza la relación padre-hijo, no un orden entre hermanos.
- **Heap Máximo:** el padre siempre es mayor que sus hijos.
- **Heap Mínimo:** el padre siempre es menor que sus hijos.

## Representación como vector
Dado un nodo en la posición `i`:
- Raíz: posición 0.
- Padre: `(i-1) // 2`
- Hijo izquierdo: `(i*2) + 1`
- Hijo derecho: `(i*2) + 2`

## Operaciones y complejidad
- Obtener el máximo (heap máx) o mínimo (heap mín): **O(1)** (siempre está en la raíz), vs **O(n)** en una lista enlazada sin ordenar.
- **Insertar:** se agrega al final del vector y se aplica **Bubble Up** (sube intercambiando con su padre mientras lo supere) -> **O(log n)** (proporcional a la altura del árbol).
- **Heapify:** convierte un vector arbitrario en un heap válido, recorriendo desde el último nodo no-hoja hacia la raíz aplicando bubble-down cuando corresponde -> **O(n)** total.

```python
def bubble_up(heap, i):
    padre = (i - 1) // 2
    if i > 0 and heap[i] > heap[padre]:
        heap[i], heap[padre] = heap[padre], heap[i]
        bubble_up(heap, padre)
```

## Cola de Prioridad
- TDA con operaciones **insertar** y **pop/dequeue**, que siempre devuelve el elemento de mayor (o menor) prioridad.
- Se puede implementar con Heap (O(log n) por operación) o con lista enlazada (O(n)); el Heap es la opción eficiente.
- Aplicaciones reales: algoritmo de **Dijkstra** (camino más corto), compresión de **Huffman**, `heapq` en Python y `PriorityQueue` en Java (ambos basados en Heap Mínimo).

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_9_Apuntes.md) - Heap y Cola de prioridad

# =========================================
# SEGMENTO 10: ALGORITMOS DE ORDENAMIENTO
# =========================================

## Conceptos previos
- **Complejidad temporal:** mejor, promedio y peor caso, medida en comparaciones/intercambios.
- **Complejidad espacial:** memoria extra requerida.
  * **In-place:** O(1) memoria extra.
  * **Out-of-place:** memoria proporcional a n (O(n) o más).
- **Estabilidad:** conserva el orden relativo de elementos iguales.
- **Adaptabilidad:** mejora su rendimiento si la entrada ya está parcial/totalmente ordenada.

## Tabla comparativa (complejidades)
| Algoritmo | Mejor | Promedio | Peor | Espacio | Estable | Adaptativo |
|---|---|---|---|---|---|---|
| Burbuja | O(n) | O(n²) | O(n²) | O(1) | Sí | Sí |
| Selección | O(n²) | O(n²) | O(n²) | O(1) | No | No |
| Inserción | O(n) | O(n²) | O(n²) | O(1) | Sí | Sí |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | No |
| Mergesort | O(n log n) | O(n log n) | O(n log n) | O(n) | Sí | No |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Sí | No |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Sí | No |

## Comparaciones e intercambios exactos: Selección vs Inserción
### Selección
- **Comparaciones (siempre las mismas, no depende del orden):** (n² − n) / 2
- **Intercambios:** 0 en el mejor caso (no ocurre realmente, pero teóricamente el mínimo posible) — n−1 en el peor caso (como máximo un intercambio por pasada, y hay n−1 pasadas).

### Inserción
- **Comparaciones — mejor caso:** n − 1 (arreglo ya ordenado, una sola comparación por elemento).
- **Intercambios (desplazamientos) — mejor caso:** 0. **Peor caso:** (n² − n) / 2 (arreglo en orden inverso, cada elemento se desplaza hasta el inicio).

> **Conclusión práctica:** Selección conviene cuando escribir/intercambiar es costoso (ej. limitaciones de escritura en disco), porque en su peor caso solo hace n−1 intercambios, mientras que Inserción puede llegar a (n²−n)/2 intercambios en su peor caso. Selección "paga" ese ahorro con más comparaciones fijas ((n²−n)/2 siempre), mientras que Inserción es más barata en comparaciones cuando los datos ya están casi ordenados.

## Ordenamiento Burbuja (Bubble Sort)
- Compara pares **adyacentes** e intercambia si están desordenados; en cada pasada "burbujea" el mayor hacia el final.
- Optimización con bandera de "sin intercambios" -> permite terminar en O(n) si ya está ordenado (adaptativo).
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        cambio = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cambio = True
        if not cambio:
            break
    return arr
```

## Ordenamiento por Selección (Selection Sort)
- Busca el mínimo de la porción desordenada y lo intercambia con la primera posición desordenada.
- Siempre recorre todo, por eso no es adaptativo; máximo 1 intercambio por pasada.
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr
```

## Ordenamiento por Inserción (Insertion Sort)
- Inserta cada elemento en su posición correcta dentro de la parte ya ordenada (como ordenar cartas en la mano).
- Muy eficiente en arreglos pequeños o casi ordenados; usado por Timsort (Python) en sub-arreglos pequeños.
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > actual:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = actual
    return arr
```

## Quicksort
- Divide y vencerás: elige un **pivote**, particiona en menores/mayores, y ordena recursivamente cada partición.
- Elección del pivote crítica: primer/último elemento en arreglo ya ordenado -> peor caso O(n²).
- **Dos formas comunes de elegir el pivote:**
  * Usar la **mediana** (buen balance, pero agrega O(n) adicional al cálculo).
  * Usar un **elemento aleatorio (random)**, que en la práctica rinde de forma similar a la mediana y evita el peor caso con alta probabilidad.
- No estable; espacio O(log n) por la pila de recursión; muy rápido en la práctica por buen uso de caché.
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)
```

## Mergesort
- Divide y vencerás: divide a la mitad hasta llegar a elementos individuales, luego mezcla (**merge**) manteniendo el orden.
- Garantiza O(n log n) en todos los casos (no adaptativo); requiere O(n) de espacio extra (no in-place); estable si se elige primero el elemento izquierdo en empates.
- Preferido cuando se necesita estabilidad garantizada o se ordenan listas enlazadas/datos externos.
```python
def merge(izq, der):
    r = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            r.append(izq[i]); i += 1
        else:
            r.append(der[j]); j += 1
    return r + izq[i:] + der[j:]
```

## Heapsort
- Fase 1: **Heapify** del arreglo completo (O(n)).
- Fase 2: extraer repetidamente la raíz (máximo), intercambiarla al final, reducir el heap y aplicar bubble-down -> n extracciones de O(log n) cada una.
- O(n log n) garantizado en todos los casos, espacio O(1) (in-place), pero NO estable. Combina lo mejor de tiempo garantizado y espacio constante (algo que ni Quicksort ni Mergesort logran juntos).

## Counting Sort
- No compara elementos; cuenta ocurrencias de cada valor en un rango conocido `k` y las acumula para ubicar cada elemento en su posición final.
- O(n+k) tiempo y espacio; estable si se recorre de derecha a izquierda al colocar; solo eficiente si `k` es pequeño respecto a `n`.
```python
def counting_sort(arr):
    if not arr: return arr
    mn, mx = min(arr), max(arr)
    conteo = [0]*(mx-mn+1)
    for x in arr:
        conteo[x-mn] += 1
    for i in range(1, len(conteo)):
        conteo[i] += conteo[i-1]
    salida = [0]*len(arr)
    for x in reversed(arr):
        conteo[x-mn] -= 1
        salida[conteo[x-mn]] = x
    return salida
```

## Radix Sort
- Ordena por dígitos, del menos al más significativo (LSD), usando Counting Sort estable como subrutina en cada pasada.
- O(n·k), donde k = cantidad de dígitos; requiere que la subrutina sea estable para preservar el orden de pasadas anteriores.
- Útil para grandes volúmenes de enteros o cadenas de longitud fija.

## ¿Cuándo usar cuál? (resumen rápido)
- **Burbuja/Selección/Inserción:** datasets muy pequeños, fines educativos, o casi ordenados (Burbuja/Inserción, por ser adaptativos). Selección conviene si escribir/intercambiar es costoso.
- **Quicksort:** el más rápido en la práctica; no requiere estabilidad; se mitiga el peor caso con pivote aleatorio.
- **Mergesort:** cuando se necesita O(n log n) garantizado + estabilidad, o listas enlazadas/ordenamiento externo.
- **Heapsort:** cuando se necesita O(n log n) garantizado + espacio O(1) a la vez.
- **Counting/Radix Sort:** enteros en un rango conocido y acotado; superan la barrera teórica O(n log n) de los algoritmos por comparación.

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_%6011_Apuntes.md) - Algoritmos de Ordenamiento

# =========================================
# 11. Comparativas entre algoritmos de ordenamiento
# =========================================

### Burbuja
- **Comparaciones:** $(n^2 - n) / 2$ en todos los casos (sin optimización) o $n - 1$ en el mejor caso (con bandera de intercambio).
- **Intercambios:** $0$ (Mejor caso), $(n^2 - n) / 2$ (Peor caso).
- **Información clave:** Algoritmo adaptativo si se usa bandera de control. Es ineficiente debido al alto número de intercambios adyacentes en el peor caso.

### Selección
- **Comparaciones:** $(n^2 - n) / 2$ en todos los casos.
- **Intercambios:** $0$ (Mejor caso), $n - 1$ (Peor caso).
- **Información clave:** Es ideal cuando el costo de escritura/intercambio en memoria es muy alto (ej. memorias Flash), ya que realiza como máximo $n - 1$ intercambios. No es adaptativo ni estable.

### Inserción
- **Comparaciones:** $n - 1$ (Mejor caso), $(n^2 - n) / 2$ (Peor caso).
- **Intercambios / Desplazamientos:** $0$ (Mejor caso), $(n^2 - n) / 2$ (Peor caso).
- **Información clave:** Sumamente eficiente para arreglos pequeños o casi ordenados. Sirve de base para algoritmos híbridos como Timsort.

### Quicksort
- **Comparaciones:** $O(n \log n)$ (Mejor y caso promedio), $(n^2 - n) / 2$ (Peor caso).
- **Intercambios:** $O(n \log n)$ en promedio.
- **Información clave:** El rendimiento depende críticamente de la selección del pivote. Utilizar la mediana agrega $O(n)$ adicional por nivel, mientras que seleccionar un elemento aleatorio reduce drásticamente la probabilidad del peor caso manteniendo un rendimiento óptimo en la práctica. In-place respecto a los datos, pero requiere $O(\log n)$ espacio en la pila de llamadas.

### Mergesort
- **Comparaciones:** Entre $\frac{1}{2} n \log_2 n$ y $n \log_2 n - n + 1$.
- **Asignaciones / Copias de memoria:** $O(n \log n)$ debido a los arreglos auxiliares de mezcla.
- **Información clave:** Garantiza siempre $O(n \log n)$ independientemente de la distribución de los datos. No es in-place ($O(n)$ de espacio extra). Ideal para listas enlazadas y ordenamiento externo de archivos masivos.

### Heapsort
- **Comparaciones:** $\approx 2n \log_2 n$ en el peor caso.
- **Intercambios:** $O(n \log n)$ en el proceso de extracción de la raíz.
- **Información clave:** Combina lo mejor del peor caso de Mergesort ($O(n \log n)$ garantizado) con el consumo de memoria de Selección ($O(1)$ espacio extra). No es estable ni adaptativo.

### Counting Sort
- **Comparaciones:** $0$ (Algoritmo no basado en comparaciones).
- **Operaciones totales:** $O(n + k)$, donde $k$ es el rango de los valores ($max - min + 1$).
- **Información clave:** Supera la barrera del $O(n \log n)$, pero requiere $O(n + k)$ espacio adicional. Solo es práctico si el rango $k$ no es significativamente mayor que $n$.

### Radix Sort
- **Comparaciones:** $0$ (Algoritmo no basado en comparaciones).
- **Operaciones totales:** $O(d \cdot (n + k))$, donde $d$ es la cantidad de dígitos/posiciones y $k$ la base numérica (ej. 10 para decimales).
- **Información clave:** Procesa los datos por posiciones (LSD) utilizando Counting Sort como subrutina. Requiere que la subrutina sea estrictamente estable para preservar el orden de las pasadas previas.

---

> **Diferencia de eficiencia en escrituras:** Selección es mejor que Inserción y Burbuja cuando existen limitaciones en escrituras de disco/memoria, debido a que en el peor de los casos realiza solo $n - 1$ intercambios, mientras que Inserción y Burbuja realizan $\frac{n^2 - n}{2}$.

> **Estrategias de pivote en Quicksort:** El funcionamiento y balanceo de las particiones depende del pivote:
> - *Mediana real:* Garantiza particiones equilibradas pero agrega un costo adicional de $O(n)$ por nivel.
> - *Pivote aleatorio:* Tiene un costo computacional despreciable y logra un rendimiento cercano al caso óptimo en la práctica.

> [Resumen Completo](https://github.com/AxelAbarMe/Estructuras-Datos/blob/main/General/Teoria/Clase_%6012_Apuntes.md) - Comparativa entre algoritmos de ordenamiento

---

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

----


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


