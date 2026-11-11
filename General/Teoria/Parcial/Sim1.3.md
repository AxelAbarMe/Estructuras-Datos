# EXAMEN DE SIMULACRO 3 — 100 Preguntas (Primer Parcial)

> **Temas:** Conceptos generales (arquitectura de hardware, compilación, memoria, APIs, formatos de archivo, complejidad Big-O), Estructuras de Datos Lineales (Vector, Lista Enlazada, Pila, Cola), Recursividad, Heaps y Colas de Prioridad, Algoritmos de Ordenamiento.

**Instrucciones:**
- Marque con una **X** la(s) opción(es) correcta(s) donde se indique.
- Las preguntas de selección múltiple indican cuántas opciones se deben marcar (2 de 5).
- Las preguntas de respuesta corta indican un ejemplo del formato esperado.
- Las preguntas de "Explique" requieren una justificación breve y concreta.
- **Tiempo estimado total: 1 hora 30 minutos (100 preguntas).**
- Nivel: alto. No se puede regresar a preguntas anteriores una vez avanzado el examen real.

---

## BLOQUE I: CONCEPTOS GENERALES (Preguntas 1–25)

**1. ¿Cuál es la secuencia correcta del ciclo de instrucción del CPU?**

* [ ] a) Decode → Fetch → Execute  
* [ ] b) Fetch → Execute → Decode  
* [ ] c) Fetch → Decode → Execute  
* [ ] d) Execute → Fetch → Decode  

**2. ¿Cuál es la función principal del registro conocido como "Program Counter" (RIP en x86-64)?**

* [ ] a) Almacenar el resultado devuelto por la ALU  
* [ ] b) Apuntar a la dirección de memoria de la siguiente instrucción a ejecutar  
* [ ] c) Indicar la dirección del tope actual de la pila del sistema  
* [ ] d) Traducir bytecode a lenguaje máquina  

**3. Una empresa determina que su carga de trabajo es intensiva en cómputo, pero muy sensible al costo energético al ejecutarse en la nube. ¿Qué arquitectura de CPU convendría evaluar primero para reducir costos?**

* [ ] a) x86-64 clásico  
* [ ] b) Una arquitectura CISC de alto voltaje  
* [ ] c) ARM  
* [ ] d) Ninguna, el consumo energético no depende de la arquitectura  

**4. En C++, el tamaño en bytes de un tipo `int`:**

* [ ] a) Siempre es de 8 bytes, sin importar la arquitectura  
* [ ] b) Puede variar según la arquitectura y el compilador, lo cual afecta la portabilidad de binarios  
* [ ] c) Se determina en tiempo de ejecución dentro del heap  
* [ ] d) No tiene ningún efecto al migrar un programa entre arquitecturas  

**5. ¿Por qué un ejecutable compilado para ARM no puede correr directamente sobre un procesador x86-64?**

* [ ] a) Porque ARM no posee registros internos  
* [ ] b) Porque el lenguaje máquina generado es específico de cada arquitectura de CPU  
* [ ] c) Porque el proceso de linker bloquea explícitamente la ejecución cruzada  
* [ ] d) Porque el archivo `.obj` de ARM se encuentra encriptado  

**6. Considere el siguiente fragmento en C++:**

```cpp
int total = 0;          // variable global inicializada
static int contador;    // variable global SIN inicializar
int main() {
    int local = 5;
}
```

¿En qué segmento de memoria se ubica la variable `contador`?

* [ ] a) `.data`  
* [ ] b) `.bss`  
* [ ] c) Heap  
* [ ] d) Stack  

**7. ¿Cuál de las siguientes afirmaciones sobre el segmento `.text` es correcta?**

* [ ] a) Es de solo lectura y almacena las instrucciones del programa  
* [ ] b) Crece dinámicamente durante la ejecución del programa  
* [ ] c) Almacena las variables locales de cada función  
* [ ] d) Es el único segmento que puede modificarse en tiempo de ejecución  

**8. *(Selección múltiple — Seleccione 2)* ¿Cuáles de las siguientes situaciones provocan directamente un "memory leak"?**

* [ ] a) Perder la referencia a una dirección devuelta por `new`/`malloc` sin liberarla  
* [ ] b) Declarar una variable local dentro de una función  
* [ ] c) No ejecutar `delete`/`free` sobre memoria dinámica que ya no se utiliza  
* [ ] d) Provocar un desbordamiento (overflow) de un entero  
* [ ] e) Utilizar recursión de cola  

**9. Dado `int* p = new int(5);`, ¿en qué segmentos residen respectivamente la variable puntero `p` y el valor `5`?**

* [ ] a) Ambos residen en el heap  
* [ ] b) `p` reside en el stack y `5` reside en el heap  
* [ ] c) `p` reside en el heap y `5` reside en el stack  
* [ ] d) Ambos residen en el stack  

**10. *(Respuesta corta)* Indique, en el orden correcto desde la dirección de memoria más baja (low address) hasta la más alta (high address), la secuencia de los segmentos de memoria de un programa compilado en C++, utilizando únicamente estos nombres: `text`, `data`, `bss`, `heap`, `stack`.**

Proporcione la respuesta en el cuadro de texto en el siguiente formato de ejemplo (con nombres distintos a la respuesta real):
```
stack, heap, bss, data, text
```

**11. ¿Cuál es la función del *linker* dentro del proceso de compilación?**

* [ ] a) Traduce el código fuente directamente a bytecode  
* [ ] b) Combina el archivo `.obj` generado con las bibliotecas precompiladas para producir el ejecutable final  
* [ ] c) Ejecuta el programa línea por línea durante el debug  
* [ ] d) Genera la tabla de símbolos del intérprete  

**12. Un archivo `.class` de Java es portable entre distintas arquitecturas de CPU porque:**

* [ ] a) Se compila directamente a código máquina universal  
* [ ] b) Contiene bytecode que es ejecutado sobre la JVM  
* [ ] c) No hace uso de los segmentos heap ni stack  
* [ ] d) Es un archivo de texto plano interpretado línea por línea  

**13. *(Explique corta)* Explique por qué, a diferencia de un ejecutable de C++, un mismo archivo `.class` de Java puede ejecutarse tanto en una máquina x86-64 como en una ARM sin necesidad de recompilar el código fuente.**

**14. Un lenguaje interpretado como Python resulta, en términos generales, más lento en ejecución que uno compilado como C++ porque:**

* [ ] a) Python no permite el uso de funciones recursivas  
* [ ] b) El intérprete traduce y ejecuta instrucción por instrucción en tiempo de ejecución, repitiendo el proceso en cada corrida del programa  
* [ ] c) Los lenguajes interpretados no hacen uso de memoria RAM  
* [ ] d) Python siempre se ejecuta sobre arquitectura ARM  

**15. Un módulo bancario requiere comunicación mediante mensajes con estructura XML estrictamente validada bajo un contrato formal. ¿Qué tipo de API describe mejor este escenario?**

* [ ] a) REST  
* [ ] b) GraphQL  
* [ ] c) SOAP  
* [ ] d) WebSocket  

**16. Un cliente de una aplicación móvil solo necesita 2 de los 15 campos que normalmente devuelve un endpoint. ¿Cuál es la ventaja principal de usar GraphQL en este escenario, frente a REST?**

* [ ] a) GraphQL evita por completo el uso del protocolo HTTP  
* [ ] b) El cliente puede solicitar exactamente los campos que necesita, evitando la sobrecarga de datos innecesarios  
* [ ] c) GraphQL no requiere de un servidor backend  
* [ ] d) REST no puede devolver respuestas en formato JSON  

**17. *(Explique corta)* Explique por qué, en una arquitectura de microservicios, comunicar los módulos mediante APIs permite que cada servicio se implemente en un lenguaje de programación distinto.**

**18. ¿Cuál formato estructura la información principalmente mediante indentación, sin requerir llaves ni etiquetas de cierre?**

* [ ] a) JSON  
* [ ] b) XML  
* [ ] c) YAML  
* [ ] d) Binario  

**19. *(Respuesta corta)* Convierta el siguiente objeto JSON a su equivalente en formato YAML: `{"nombre": "Marta", "edad": 29}`.**

Proporcione la respuesta en el cuadro de texto, usando el siguiente formato de ejemplo (con datos distintos a los de la pregunta):
```
id: 3
activo: false
```

**20. ¿Por qué JSON es el formato más utilizado actualmente en APIs REST modernas, en comparación con XML?**

* [ ] a) Porque JSON no puede representar arreglos de datos  
* [ ] b) Porque es más compacto y no requiere etiquetas de cierre pesadas  
* [ ] c) Porque JSON es en realidad un formato binario  
* [ ] d) Porque XML no puede ser leído por humanos  

**21. Un archivo de configuración de un pipeline (por ejemplo, Docker Compose) suele preferir el formato YAML principalmente por:**

* [ ] a) Su tamaño binario reducido en disco  
* [ ] b) Su legibilidad para humanos gracias al uso de indentación  
* [ ] c) Que permite ejecutar código directamente al ser interpretado  
* [ ] d) Que siempre se parsea más rápido que JSON, sin excepción  

---

### Enunciado A — Complejidad algorítmica (Preguntas 22 a 25)

Analice el siguiente fragmento de código en Python:

```python
def procesar(lista):
    total = 0
    for i in range(len(lista)):          # ciclo externo
        for j in range(i, len(lista)):   # ciclo interno (empieza en i)
            total += lista[i] * lista[j]
    return total
```

**22. *(Análisis de complejidad)* ¿Cuál es la complejidad temporal en notación Big-O de la función `procesar`?**

* [ ] a) O(n)  
* [ ] b) O(n log n)  
* [ ] c) O(n²)  
* [ ] d) O(2ⁿ)  

**23. *(Análisis de resultado en x iteración)* Si `lista = [1, 2, 3]`, ¿cuál es el valor de `total` inmediatamente después de terminar la primera iteración completa del ciclo externo (`i = 0`)?**

* [ ] a) 3  
* [ ] b) 6  
* [ ] c) 9  
* [ ] d) 14  

**24. *(Análisis de causa de error)* Si el ciclo interno se modificara para iniciar en `range(0, len(lista))` en lugar de `range(i, len(lista))`, manteniendo todo lo demás igual, ¿qué consecuencia tendría sobre el resultado calculado, comparado con la versión original?**

* [ ] a) No cambia el resultado; solamente mejora la complejidad a O(n)  
* [ ] b) El resultado aumentaría, pues cada par (i, j) con i ≠ j se contabilizaría dos veces  
* [ ] c) Se produciría un `IndexError` en tiempo de ejecución  
* [ ] d) La función dejaría de terminar (bucle infinito)  

**25. *(Explique corta)* Explique por qué, al simplificar la expresión de complejidad `O(3n²) + O(5n) + O(20)`, el resultado final se expresa simplemente como `O(n²)`.**

---

## BLOQUE II: ESTRUCTURAS DE DATOS LINEALES (Preguntas 26–50)

### Enunciado B — Validación de expresiones con Pila (Preguntas 26 a 30)

Se implementa una Pila para validar el balance de la expresión: `{a*(b+[c-d])}`

**26. ¿Cuál es el estado de la pila (de abajo hacia arriba) justo después de procesar el carácter `[`, antes de encontrar el primer símbolo de cierre?**

* [ ] a) `{  (  [`  
* [ ] b) `[  (  {`  
* [ ] c) `{  [  (`  
* [ ] d) `(  {  [`  

**27. ¿En qué orden se extraen (`pop`) los símbolos de apertura al procesar, en orden, los símbolos de cierre `]`, `)`, `}`?**

* [ ] a) `{, (, [`  
* [ ] b) `[, (, {`  
* [ ] c) `(, [, {`  
* [ ] d) `{, [, (`  

**28. Si al procesar la expresión llegara un símbolo `)` cuando el tope de la pila es `[`, ¿qué indica esta situación al algoritmo de validación?**

* [ ] a) Que la expresión está correctamente balanceada  
* [ ] b) Que existe un desbalance, ya que el símbolo de cierre no corresponde al símbolo en el tope de la pila  
* [ ] c) Que se debe hacer `push` del carácter `)`  
* [ ] d) Que se debe vaciar la pila completa e ignorar el error  

**29. *(Explique corta)* Explique por qué es indispensable usar una estructura de tipo Pila (LIFO) y no una Cola (FIFO) para validar el balance de símbolos de una expresión.**

**30. *(Análisis de complejidad)* ¿Cuál es la complejidad temporal total del algoritmo de validación de paréntesis para una expresión de longitud n, si la Pila se implementa mediante una lista enlazada simple?**

* [ ] a) O(1)  
* [ ] b) O(n)  
* [ ] c) O(n log n)  
* [ ] d) O(n²)  

---

### Enunciado C — Cola de impresión (Preguntas 31 a 34)

Un sistema de impresión mantiene una Cola implementada con lista enlazada simple, con punteros `front` y `rear`. Llegan los documentos en este orden: `doc1, doc2, doc3, doc4`.

**31. ¿Cuál documento se procesará primero al aplicar `dequeue()`?**

* [ ] a) doc4  
* [ ] b) doc1  
* [ ] c) doc3  
* [ ] d) Depende del tamaño del documento  

**32. Si el sistema únicamente mantuviera una referencia al nodo `front` (sin referencia a `rear`), ¿cuál sería la complejidad de la operación `enqueue()` (insertar al final)?**

* [ ] a) O(1)  
* [ ] b) O(log n)  
* [ ] c) O(n)  
* [ ] d) O(n²)  

**33. *(Selección múltiple — Seleccione 2)* ¿Cuáles de las siguientes son aplicaciones reales típicas de una estructura tipo Cola (FIFO)?**

* [ ] a) Función "Deshacer" de un editor de texto  
* [ ] b) Gestión de procesos en orden de llegada dentro de un sistema operativo  
* [ ] c) Balanceo de paréntesis en una expresión  
* [ ] d) Recorrido en anchura (BFS) sobre un grafo  
* [ ] e) Cálculo del stack de llamadas en la recursión  

**34. *(Respuesta corta)* Se han encolado los documentos `"doc1"`, `"doc2"`, `"doc3"` en ese orden. Luego se ejecuta un `dequeue()`, seguido de un `enqueue("doc4")`. Indique el contenido final de la cola de front a rear.**

Proporcione la respuesta en formato de lista, ejemplo esperado:
```
[x, y, z]
```

---

### Enunciado D — Inserción en Lista Doblemente Enlazada (Preguntas 35 a 38)

Se tiene una lista doblemente enlazada con los valores (de head a tail): `10, 20, 30, 40`. Se desea implementar `InsertarEnPosicion(elemento, posicion)`, donde la primera posición cuenta a partir de 1.

**35. Si se ejecuta `InsertarEnPosicion(25, 3)`, ¿cuál sería el nuevo contenido de la lista, de head a tail?**

* [ ] a) `10, 20, 25, 30, 40`  
* [ ] b) `10, 25, 20, 30, 40`  
* [ ] c) `10, 20, 30, 25, 40`  
* [ ] d) `25, 10, 20, 30, 40`  

**36. ¿Cuál validación es indispensable realizar antes de insertar, para garantizar que la función trabaje apropiadamente en todos los casos?**

* [ ] a) Verificar que el elemento a insertar sea un número entero  
* [ ] b) Verificar que la posición sea mayor a 0 y no exceda en más de 1 la cantidad actual de nodos de la lista  
* [ ] c) Verificar que la lista tenga al menos 100 elementos  
* [ ] d) Verificar que la lista no sea doblemente enlazada  

**37. *(Análisis de causa de error)* Si la función no actualizara el puntero `prev` del nodo que queda inmediatamente después del nuevo nodo insertado, ¿qué problema ocurriría al recorrer la lista en reversa desde el `tail`?**

* [ ] a) No ocurriría ningún problema; el recorrido sería idéntico  
* [ ] b) El recorrido en reversa fallaría o se saltaría el nodo recién insertado  
* [ ] c) Se generaría inmediatamente un Stack Overflow  
* [ ] d) Se liberaría automáticamente la memoria del nodo insertado  

**38. *(Explique corta)* Explique por qué insertar un elemento en una posición intermedia de una lista doblemente enlazada tiene complejidad O(n) en el peor caso, a pesar de que enlazar los punteros del nuevo nodo es una operación O(1).**

---

### Enunciado E — Fusión de listas enlazadas ordenadas (Preguntas 39 a 42)

Se tienen dos listas enlazadas simples ordenadas ascendentemente: `L1: 2 → 5 → 8` y `L2: 1 → 6 → 9 → 10`. Se desea concatenarlas de forma iterativa en una sola lista ordenada, con complejidad no mayor a O(n).

**39. ¿Cuál sería el contenido correcto de la lista resultante, de head a tail?**

* [ ] a) `1, 2, 5, 6, 8, 9, 10`  
* [ ] b) `2, 5, 8, 1, 6, 9, 10`  
* [ ] c) `1, 2, 6, 5, 8, 9, 10`  
* [ ] d) `1, 6, 9, 10, 2, 5, 8`  

**40. *(Análisis de complejidad)* ¿Cuál es la complejidad espacial (memoria adicional) de este algoritmo, si se reutilizan los nodos existentes de L1 y L2 sin crear nodos nuevos?**

* [ ] a) O(n)  
* [ ] b) O(1)  
* [ ] c) O(log n)  
* [ ] d) O(n²)  

**41. ¿Por qué este algoritmo NO podría implementarse con la misma eficiencia (O(n)) si las listas estuvieran representadas como vectores desordenados en lugar de listas enlazadas ordenadas?**

* [ ] a) Porque los vectores no pueden almacenar números enteros  
* [ ] b) Porque, al estar desordenados, primero habría que ordenarlos, agregando al menos O(n log n)  
* [ ] c) Porque los vectores no tienen un tamaño fijo  
* [ ] d) Porque los vectores son estructuras no lineales  

**42. *(Explique corta)* Explique por qué, durante la fusión de dos listas ya ordenadas, basta con comparar únicamente los nodos "actuales" (el frente de cada lista) para decidir cuál insertar a continuación en la lista resultante.**

---

**43. Considere `int v[8];` en C++, con dirección base `0x2000` y cada entero de 4 bytes. ¿Cuál es la dirección de memoria de `v[5]`?**

* [ ] a) `0x2005`  
* [ ] b) `0x2014`  
* [ ] c) `0x2020`  
* [ ] d) `0x2004`  

**44. Un vector dinámico tiene capacidad 4 y está lleno. Al insertar un quinto elemento usando la estrategia de expansión x2, ¿qué ocurre?**

* [ ] a) La nueva capacidad es 5, y los elementos existentes se mueven solo a la nueva posición 5  
* [ ] b) La nueva capacidad es 8, y se realiza un Deep Copy de los 4 elementos existentes al nuevo espacio  
* [ ] c) La nueva capacidad permanece en 4; no ocurre ningún cambio  
* [ ] d) La nueva capacidad es 8, pero los elementos antiguos se descartan  

**45. *(Selección múltiple — Seleccione 2)* ¿Cuáles de las siguientes afirmaciones sobre las listas enlazadas simples son verdaderas?**

* [ ] a) Requieren memoria contigua para funcionar correctamente  
* [ ] b) El acceso a un elemento por posición es O(n) en el peor caso  
* [ ] c) Cada nodo almacena únicamente el dato, sin ningún puntero adicional  
* [ ] d) Permiten insertar y eliminar elementos sin necesidad de desplazar otros elementos  
* [ ] e) Su tamaño total debe conocerse de antemano antes de crear la lista  

**46. *(Respuesta corta)* Sobre una Pila vacía se ejecutan, en este orden: `push(5)`, `push(8)`, `push(2)`, `pop()`, `push(9)`, `pop()`. Indique la secuencia de los dos valores retornados por las llamadas a `pop()`, en el orden en que ocurrieron.**

Proporcione la respuesta en formato de lista, ejemplo esperado:
```
[x, y]
```

**47. ¿Cuál es la razón principal por la que implementar una Cola con una lista doblemente enlazada se considera un desperdicio de memoria (overhead innecesario)?**

* [ ] a) Porque las colas no permiten insertar más de 100 elementos  
* [ ] b) Porque una cola nunca necesita recorrerse en reversa, por lo que el puntero `prev` no aporta funcionalidad útil  
* [ ] c) Porque las listas doblemente enlazadas no soportan el principio FIFO  
* [ ] d) Porque consumiría memoria del segmento `.bss`  

**48. *(Análisis de causa de error)* Analice el siguiente fragmento de una Cola implementada con lista enlazada simple:**

```python
def dequeue(self):
    valor = self.front.valor
    self.front = self.front.next
    return valor
```

Si esta cola tiene únicamente un elemento y se ejecuta `dequeue()`, ¿qué error potencial NO está siendo manejado por el código?

* [ ] a) No se libera correctamente la memoria del heap en Python  
* [ ] b) No se actualiza la referencia `rear` a `None` cuando la cola queda vacía, lo que puede causar inconsistencias en futuros `enqueue()`  
* [ ] c) El código genera inmediatamente un `TypeError`  
* [ ] d) El código no compila  

**49. En Python, ¿cuál estructura de la librería estándar es la más recomendada para implementar tanto pilas como colas de forma eficiente en ambos extremos?**

* [ ] a) `list`  
* [ ] b) `tuple`  
* [ ] c) `collections.deque`  
* [ ] d) `set`  

**50. *(Explique corta)* Un desarrollador debe elegir entre un Vector y una Lista Enlazada Simple para una aplicación donde se realizan constantemente inserciones al inicio de la secuencia de datos, y prácticamente nunca se accede a elementos por posición aleatoria. Explique cuál estructura es más adecuada y por qué.**

---

## BLOQUE III: RECURSIVIDAD (Preguntas 51–65)

### Enunciado F — Función recursiva `espejo` (Preguntas 51 a 55)

```python
def espejo(n, profundidad=0):
    if n == 0:
        return profundidad
    return espejo(n // 10, profundidad + 1)
```

**51. *(Análisis de recursividad)* Al ejecutar `espejo(4321)`, ¿cuántas llamadas totales a la función `espejo` se realizan (incluyendo la llamada inicial y la que alcanza el caso base)?**

* [ ] a) 3  
* [ ] b) 4  
* [ ] c) 5  
* [ ] d) 6  

**52. *(Análisis de resultado)* ¿Cuál es el valor retornado por `espejo(4321)`?**

* [ ] a) 4321  
* [ ] b) 4  
* [ ] c) 1234  
* [ ] d) 0  

**53. *(Análisis de causa de error)* Si se invoca `espejo(-15)`, considerando que en Python `-15 // 10` da como resultado `-2`, y que la división entera de números negativos nunca llega a valer exactamente `0` en este patrón de decrecimiento, ¿qué comportamiento tendría la función?**

* [ ] a) Retorna un valor negativo correctamente  
* [ ] b) Entra en una recursión infinita porque `n` nunca alcanza exactamente el valor 0, provocando un `RecursionError` (Stack Overflow)  
* [ ] c) Retorna 0 inmediatamente  
* [ ] d) Lanza un error de sintaxis  

**54. *(Análisis de complejidad)* ¿Cuál es la complejidad temporal y espacial (en términos de stack de llamadas) de `espejo` para un número de `d` dígitos?**

* [ ] a) O(d) en tiempo y O(d) en espacio de pila  
* [ ] b) O(1) en tiempo y O(1) en espacio  
* [ ] c) O(d²) en tiempo y O(1) en espacio  
* [ ] d) O(log d) en tiempo y O(d) en espacio  

**55. *(Explique corta)* Explique por qué `espejo` es un ejemplo de recursión de cola (tail recursion), y por qué en Python esto no evita que se consuma un stack frame por cada llamada.**

---

### Enunciado G — Permutaciones recursivas (Preguntas 56 a 59)

Se implementa una función recursiva `permutar(cadena)` que calcula todas las permutaciones posibles de una cadena de longitud n, eligiendo un carácter a la vez.

**56. *(Análisis de complejidad)* ¿Cuál es la complejidad temporal aproximada de este algoritmo?**

* [ ] a) O(n)  
* [ ] b) O(n²)  
* [ ] c) O(2ⁿ)  
* [ ] d) O(n!)  

**57. Para una cadena de longitud 4 (por ejemplo `"abcd"`), ¿cuántas permutaciones distintas debería retornar la función?**

* [ ] a) 4  
* [ ] b) 8  
* [ ] c) 16  
* [ ] d) 24  

**58. ¿Cuál sería el caso base más adecuado para `permutar(cadena)`?**

* [ ] a) Cuando la cadena tiene longitud 0 (o 1), se retorna la cadena misma como única permutación posible  
* [ ] b) Cuando la cadena tiene longitud mayor a 10  
* [ ] c) Cuando la cadena está vacía, se lanza una excepción  
* [ ] d) No requiere caso base, ya que termina automáticamente  

**59. *(Análisis de causa de error)* Si la función recursiva de permutaciones no maneja el caso donde la cadena de entrada tiene caracteres repetidos, ¿qué problema podría presentarse en el resultado final?**

* [ ] a) La función no compilaría  
* [ ] b) Se generarían permutaciones duplicadas en el resultado, ya que el algoritmo trata cada posición como distinta aunque el carácter sea igual  
* [ ] c) Se produciría inevitablemente un Stack Overflow  
* [ ] d) El resultado tendría menos permutaciones de las esperadas  

---

**60. Un algoritmo recursivo que divide un problema en dos subproblemas de la mitad del tamaño, y luego combina los resultados en tiempo O(n), corresponde a la estrategia de:**

* [ ] a) Backtracking  
* [ ] b) Memoización  
* [ ] c) Divide y Vencerás  
* [ ] d) Recursión de cola  

**61. ¿Qué técnica permite que un algoritmo recursivo evite recalcular subproblemas ya resueltos, mejorando el tiempo a cambio de mayor uso de memoria?**

* [ ] a) Backtracking  
* [ ] b) Memoización  
* [ ] c) Tail Call Optimization  
* [ ] d) Heapify  

**62. *(Explique corta)* Utilizando el ejemplo del cálculo recursivo de Fibonacci sin memoización, explique por qué su complejidad es exponencial O(2ⁿ).**

**63. ¿En qué circunstancia se recomienda preferir una solución recursiva sobre una iterativa, a pesar de su mayor consumo de memoria por los stack frames?**

* [ ] a) Siempre; la recursión es más eficiente en todos los casos  
* [ ] b) Cuando el problema es naturalmente recursivo, o su planteamiento iterativo resulta extremadamente complejo (ej. backtracking en un laberinto)  
* [ ] c) Solo cuando se programa en Python  
* [ ] d) Nunca; la recursión debe evitarse siempre  

---

### Enunciado H — Función recursiva `acumula` (Preguntas 64 y 65)

```python
def acumula(n):
    if n == 0:
        return 0
    return n + acumula(n - 2)
```

**64. *(Análisis de resultado)* ¿Cuál es el valor retornado por `acumula(4)`?**

* [ ] a) 4  
* [ ] b) 6  
* [ ] c) 10  
* [ ] d) 0  

**65. *(Análisis de causa de error)* Si se invoca `acumula(5)` (un número impar), dado que el caso base solo contempla `n == 0`, ¿qué ocurriría?**

* [ ] a) Retorna 9 correctamente  
* [ ] b) Entra en recursión infinita hasta provocar un Stack Overflow (`RecursionError`), pues `n` nunca llega a valer exactamente 0  
* [ ] c) Retorna 0  
* [ ] d) Lanza un error de tipo de dato  

---

## BLOQUE IV: HEAPS Y COLAS DE PRIORIDAD (Preguntas 66–80)

### Enunciado I — Heap Máximo representado en vector (Preguntas 66 a 70)

`heap = [50, 40, 45, 20, 35, 42, 10]`

**66. ¿Cuál es el hijo izquierdo del nodo ubicado en el índice 2 (valor 45)?**

* [ ] a) 20  
* [ ] b) 35  
* [ ] c) 42  
* [ ] d) 10  

**67. ¿Cuál es el padre del nodo ubicado en el índice 5 (valor 42)?**

* [ ] a) 50  
* [ ] b) 40  
* [ ] c) 45  
* [ ] d) 20  

**68. *(Análisis de resultado)* Se inserta el valor `60` al final del vector y se aplica `bubble_up`. ¿Cuál es el vector resultante final?**

* [ ] a) `[60, 50, 45, 40, 35, 42, 10, 20]`  
* [ ] b) `[60, 40, 45, 20, 35, 42, 10, 50]`  
* [ ] c) `[50, 40, 45, 20, 35, 42, 10, 60]`  
* [ ] d) `[60, 45, 50, 40, 35, 42, 10, 20]`  

**69. Tras la inserción anterior, ¿cuántas operaciones de intercambio (`bubble up`) se realizaron en total?**

* [ ] a) 1  
* [ ] b) 2  
* [ ] c) 3  
* [ ] d) 4  

**70. *(Análisis de complejidad)* ¿Cuál es la complejidad temporal general de la operación de inserción en un heap de n elementos, y a qué se debe?**

* [ ] a) O(1), porque siempre se inserta al final  
* [ ] b) O(log n), porque el `bubble up` recorre como máximo la altura del árbol  
* [ ] c) O(n), porque se debe recorrer toda la estructura  
* [ ] d) O(n log n), por la combinación de heapify e inserción  

---

### Enunciado J — Heapify sobre un arreglo desordenado (Preguntas 71 a 74)

`arr = [15, 5, 20, 2, 8]`. Se desea aplicar el algoritmo de Heapify para construir un Heap Máximo.

**71. *(Análisis de resultado en x iteración)* ¿Cuál es el estado del arreglo inmediatamente después de procesar el índice 1 (primera iteración del heapify), antes de procesar el índice 0?**

* [ ] a) `[15, 8, 20, 2, 5]`  
* [ ] b) `[8, 15, 20, 2, 5]`  
* [ ] c) `[15, 5, 20, 2, 8]`  
* [ ] d) `[20, 8, 15, 2, 5]`  

**72. ¿Cuál es el arreglo final resultante al completar todo el proceso de Heapify?**

* [ ] a) `[20, 8, 15, 2, 5]`  
* [ ] b) `[20, 15, 8, 2, 5]`  
* [ ] c) `[15, 8, 20, 5, 2]`  
* [ ] d) `[20, 8, 5, 2, 15]`  

**73. *(Análisis de complejidad)* ¿Cuál es la complejidad temporal total del algoritmo de Heapify aplicado sobre un arreglo completo de n elementos?**

* [ ] a) O(n log n)  
* [ ] b) O(n)  
* [ ] c) O(log n)  
* [ ] d) O(n²)  

**74. *(Explique corta)* Explique por qué el algoritmo de Heapify recorre el arreglo comenzando desde el último nodo no-hoja hacia la raíz, y no desde la raíz hacia las hojas.**

---

### Enunciado K — Cola de prioridad en un hospital (Preguntas 75 a 78)

Un hospital implementa una cola de prioridad basada en un Heap Máximo para atender pacientes según su nivel de gravedad (1 a 10, donde 10 es más grave). Llegan los pacientes con las siguientes prioridades, en este orden: `6, 9, 3, 9, 7`.

**75. ¿Cuál es la prioridad del primer paciente que sería atendido (extracción de la raíz) una vez insertados todos?**

* [ ] a) 6  
* [ ] b) 9  
* [ ] c) 7  
* [ ] d) 3  

**76. Si dos pacientes tienen exactamente la misma prioridad (9 y 9), y el Heap no garantiza estabilidad, ¿qué implicación tiene esto para el sistema?**

* [ ] a) El heap eliminará automáticamente uno de los dos registros duplicados  
* [ ] b) No se garantiza que el paciente que llegó primero con esa prioridad sea atendido antes que el otro con la misma prioridad  
* [ ] c) El sistema lanzará un error de duplicado  
* [ ] d) Los heaps no permiten valores repetidos  

**77. *(Análisis de complejidad)* ¿Cuál es la complejidad de extraer al paciente más grave (eliminar la raíz) y restaurar la propiedad del heap, para un heap de n pacientes?**

* [ ] a) O(1)  
* [ ] b) O(log n)  
* [ ] c) O(n)  
* [ ] d) O(n log n)  

**78. *(Explique corta)* Explique por qué, para este escenario hospitalario, una Cola de Prioridad basada en Heap es más adecuada que una simple Cola FIFO estándar.**

---

**79. En Python, el módulo `heapq` implementa internamente un:**

* [ ] a) Heap Máximo  
* [ ] b) Heap Mínimo  
* [ ] c) Árbol AVL  
* [ ] d) Lista doblemente enlazada ordenada  

**80. ¿Cuál es la diferencia estructural principal entre un Binary Heap y un Árbol Binario de Búsqueda (BST)?**

* [ ] a) El heap garantiza orden entre todos los nodos, igual que un BST  
* [ ] b) El heap solo garantiza la relación padre-hijo (mayor o menor), sin ningún orden definido entre hermanos o subárboles  
* [ ] c) El BST no puede representarse como vector  
* [ ] d) No existe ninguna diferencia real entre ambos  

---

## BLOQUE V: ALGORITMOS DE ORDENAMIENTO (Preguntas 81–100)

### Enunciado L — Trace de Insertion Sort (Preguntas 81 a 85)

```python
def ordenar(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = clave
    return arr

datos = [12, 4, 9, 7, 2]
```

**81. ¿Qué algoritmo de ordenamiento representa la función `ordenar`?**

* [ ] a) Selection Sort  
* [ ] b) Bubble Sort  
* [ ] c) Insertion Sort  
* [ ] d) Quicksort  

**82. *(Análisis de resultado en x iteración)* ¿Cuál es el contenido de `datos` inmediatamente después de terminar la iteración `i = 2` (es decir, tras insertar correctamente el tercer elemento, valor 9)?**

* [ ] a) `[4, 9, 12, 7, 2]`  
* [ ] b) `[4, 12, 9, 7, 2]`  
* [ ] c) `[4, 9, 7, 12, 2]`  
* [ ] d) `[9, 4, 12, 7, 2]`  

**83. ¿Cuál es el arreglo final completamente ordenado tras finalizar la función?**

* [ ] a) `[2, 4, 7, 9, 12]`  
* [ ] b) `[2, 4, 9, 7, 12]`  
* [ ] c) `[4, 2, 7, 9, 12]`  
* [ ] d) `[2, 4, 7, 12, 9]`  

**84. *(Análisis de complejidad)* Si el arreglo de entrada ya estuviera completamente ordenado en forma ascendente, ¿cuál sería la complejidad de esta implementación?**

* [ ] a) O(n)  
* [ ] b) O(n log n)  
* [ ] c) O(n²)  
* [ ] d) O(1)  

**85. *(Análisis de causa de error)* Si en la condición del `while` se cambiara `arr[j] > clave` por `arr[j] >= clave`, ¿qué propiedad importante del algoritmo se perdería?**

* [ ] a) La complejidad temporal en el peor caso  
* [ ] b) La estabilidad del algoritmo, ya que elementos iguales podrían intercambiar su orden relativo original  
* [ ] c) La capacidad de ordenar números negativos  
* [ ] d) La propiedad in-place del algoritmo  

---

### Enunciado M — Partición de Quicksort con pivote = primer elemento (Preguntas 86 a 90)

```python
def particion(arr, bajo, alto):
    pivote = arr[bajo]
    i = bajo + 1
    for j in range(bajo + 1, alto + 1):
        if arr[j] < pivote:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[bajo], arr[i - 1] = arr[i - 1], arr[bajo]
    return i - 1

datos = [40, 10, 55, 20, 35]
```

**86. ¿Qué elemento se selecciona como pivote en este esquema de partición?**

* [ ] a) El último elemento (`alto`)  
* [ ] b) El primer elemento (`bajo`)  
* [ ] c) El elemento medio  
* [ ] d) Un elemento aleatorio  

**87. *(Análisis de resultado en x iteración)* ¿Cuál es el arreglo `datos` inmediatamente después de procesar `j = 3` dentro del ciclo `for` (antes de procesar `j = 4`)?**

* [ ] a) `[40, 10, 20, 55, 35]`  
* [ ] b) `[40, 10, 55, 20, 35]`  
* [ ] c) `[40, 20, 10, 55, 35]`  
* [ ] d) `[10, 40, 20, 55, 35]`  

**88. ¿Cuál es el arreglo `datos` resultante inmediatamente después de finalizar la ejecución completa de `particion(datos, 0, 4)`?**

* [ ] a) `[35, 10, 20, 40, 55]`  
* [ ] b) `[10, 20, 35, 40, 55]`  
* [ ] c) `[35, 20, 10, 40, 55]`  
* [ ] d) `[40, 10, 20, 35, 55]`  

**89. ¿Qué índice retorna la función `particion` para el arreglo analizado?**

* [ ] a) 0  
* [ ] b) 2  
* [ ] c) 3  
* [ ] d) 4  

**90. *(Explique corta)* Explique qué ocurriría con el rendimiento de este esquema de partición (pivote = primer elemento) si se aplicara repetidamente sobre un arreglo ya ordenado de forma ascendente, y por qué esto representa el peor caso de Quicksort.**

---

### Enunciado N — Escenarios de selección de algoritmo de ordenamiento (Preguntas 91 a 94)

**91. Un sistema de e-commerce necesita ordenar millones de registros de pedidos por fecha de compra, y es indispensable que los pedidos con la misma fecha conserven el orden en que fueron recibidos originalmente. Se cuenta con suficiente memoria disponible en el servidor. ¿Qué algoritmo de ordenamiento es el más adecuado?**

* [ ] a) Quicksort  
* [ ] b) Heapsort  
* [ ] c) Selection Sort  
* [ ] d) Mergesort  

**92. Un sistema embebido con memoria extremadamente limitada necesita garantizar que el ordenamiento nunca exceda O(n log n), sin importar el orden inicial de los datos, y no puede usar memoria adicional significativa. La estabilidad no es un requisito. ¿Qué algoritmo conviene más?**

* [ ] a) Mergesort  
* [ ] b) Heapsort  
* [ ] c) Bubble Sort  
* [ ] d) Counting Sort  

**93. Se debe ordenar una lista pequeña (menos de 15 elementos) que llega casi siempre casi ordenada, priorizando la simplicidad de implementación por parte de un equipo junior. ¿Qué algoritmo conviene más?**

* [ ] a) Heapsort  
* [ ] b) Mergesort  
* [ ] c) Insertion Sort  
* [ ] d) Radix Sort  

**94. Se necesita ordenar 5 millones de edades de personas, sabiendo que el rango de valores posibles va de 0 a 120. ¿Qué algoritmo ofrece el mejor rendimiento absoluto para este caso específico?**

* [ ] a) Quicksort  
* [ ] b) Counting Sort  
* [ ] c) Insertion Sort  
* [ ] d) Bubble Sort  

---

**95. *(Selección múltiple — Seleccione 2)* ¿Cuáles de los siguientes algoritmos de ordenamiento son estables?**

* [ ] a) Selection Sort  
* [ ] b) Mergesort  
* [ ] c) Quicksort  
* [ ] d) Insertion Sort  
* [ ] e) Heapsort  

**96. ¿Por qué Radix Sort requiere que la subrutina de Counting Sort utilizada en cada pasada sea estrictamente estable?**

* [ ] a) Porque sin estabilidad el algoritmo no podría manejar números negativos  
* [ ] b) Porque el orden logrado en las pasadas de dígitos menos significativos debe preservarse al ordenar por los dígitos más significativos en pasadas posteriores  
* [ ] c) Porque la estabilidad reduce el uso de memoria del algoritmo  
* [ ] d) Porque, de lo contrario, el algoritmo tendría complejidad O(n²)  

**97. ¿Cuál es la razón principal por la que Quicksort suele superar en velocidad práctica a Mergesort, a pesar de que ambos comparten complejidad promedio O(n log n)?**

* [ ] a) Quicksort no realiza comparaciones entre elementos  
* [ ] b) Quicksort tiene mejor localidad de referencia (opera in-place) y menor overhead de asignación de memoria que Mergesort  
* [ ] c) Mergesort no puede implementarse de forma recursiva  
* [ ] d) Quicksort siempre tiene mejor complejidad en el peor caso  

**98. *(Respuesta corta)* Dado el arreglo `[3, 1, 4, 1, 5, 9, 2, 6]`, indique cuántas comparaciones exactas realizaría Selection Sort para ordenarlo completamente (Selection Sort siempre realiza la misma cantidad de comparaciones para un arreglo de tamaño n, sin importar el orden de los datos).**

Proporcione la respuesta como un único número entero. Ejemplo de formato esperado:
```
15
```

**99. Se tiene un sistema con limitaciones fuertes en la cantidad de escrituras que se pueden realizar en memoria (por ejemplo, una memoria Flash donde cada escritura desgasta el hardware). Comparando Selection Sort e Insertion Sort, ¿cuál conviene más y por qué?**

* [ ] a) Insertion Sort, porque siempre realiza menos comparaciones que Selection Sort  
* [ ] b) Selection Sort, porque en el peor caso realiza como máximo n-1 intercambios, mientras que Insertion Sort puede llegar a (n²-n)/2 desplazamientos en su peor caso  
* [ ] c) Ambos son equivalentes en cantidad de escrituras en cualquier caso  
* [ ] d) Ninguno de los dos; se debe usar siempre Bubble Sort  

**100. *(Explique corta)* Un desarrollador afirma que "Heapsort es estrictamente mejor que Quicksort en todos los escenarios, ya que garantiza O(n log n) en el peor caso". Explique por qué esta afirmación es imprecisa, considerando el rendimiento práctico de ambos algoritmos.**

---

## Bloque de Respuestas — Preguntas de Selección (marque con X)

| # | R | # | R | # | R | # | R | # | R |
|---|---|---|---|---|---|---|---|---|---|
| 1 | c | 21 | b | 41 | b | 61 | b | 81 | c |
| 2 | b | 22 | c | 42 | — | 62 | — | 82 | a |
| 3 | c | 23 | b | 43 | b | 63 | b | 83 | a |
| 4 | b | 24 | b | 44 | b | 64 | b | 84 | a |
| 5 | b | 25 | — | 45 | b, d | 65 | b | 85 | b |
| 6 | b | 26 | a | 46 | — | 66 | c | 86 | b |
| 7 | a | 27 | b | 47 | b | 67 | c | 87 | a |
| 8 | a, c | 28 | b | 48 | b | 68 | a | 88 | a |
| 9 | b | 29 | — | 49 | c | 69 | c | 89 | c |
| 10 | — | 30 | b | 50 | — | 70 | b | 90 | — |
| 11 | b | 31 | b | 51 | c | 71 | a | 91 | d |
| 12 | b | 32 | c | 52 | b | 72 | a | 92 | b |
| 13 | — | 33 | b, d | 53 | b | 73 | b | 93 | c |
| 14 | b | 34 | — | 54 | a | 74 | — | 94 | b |
| 15 | c | 35 | a | 55 | — | 75 | b | 95 | b, d |
| 16 | b | 36 | b | 56 | d | 76 | b | 96 | b |
| 17 | — | 37 | b | 57 | d | 77 | b | 97 | b |
| 18 | c | 38 | — | 58 | a | 78 | — | 98 | 28 |
| 19 | — | 39 | a | 59 | b | 79 | b | 99 | b |
| 20 | b | 40 | b | 60 | c | 80 | b | 100 | — |

> Las celdas marcadas con "—" corresponden a preguntas de respuesta corta o de "Explique", cuyas respuestas modelo se detallan a continuación.

---

## Respuestas de preguntas de Respuesta Corta y Explique

**10.** `text, data, bss, heap, stack`

**13.** Porque Java no compila a lenguaje máquina nativo, sino a *bytecode* intermedio (`.class`), el cual es interpretado/ejecutado por la JVM instalada en cada arquitectura. Es la JVM (específica de cada plataforma) la que traduce el bytecode a instrucciones nativas, no el programador ni el compilador original.

**17.** Porque la API expone únicamente una interfaz pública (contrato de entrada/salida) independiente del lenguaje interno de implementación del servicio. Mientras el servicio respete el formato acordado (por ejemplo, JSON sobre HTTP), otros módulos pueden consumirlo sin importar en qué lenguaje fue construido internamente.

**19.**
```
nombre: Marta
edad: 29
```

**25.** Porque al analizar la tendencia de crecimiento del algoritmo conforme n crece, el término dominante es el que crece más rápido (n² sobre n y sobre una constante); los términos de menor orden y las constantes multiplicativas se descartan porque no cambian la forma de la curva de crecimiento asintótico para valores grandes de n.

**29.** Porque el símbolo de apertura que debe cerrarse primero es siempre el más reciente que aún no ha sido cerrado (el más "interno" o anidado), lo cual corresponde exactamente al comportamiento LIFO de una pila. Una cola procesaría los símbolos en orden de llegada (FIFO), lo cual no refleja la estructura de anidamiento de las expresiones.

**34.** `[doc2, doc3, doc4]`

**38.** Porque, para llegar hasta la posición deseada, es necesario recorrer secuencialmente la lista desde el head (o desde el tail, si se optimiza) hasta alcanzar el nodo anterior a la posición de inserción; ese recorrido tiene complejidad O(n) en el peor caso, mientras que enlazar los punteros del nuevo nodo, una vez ubicado el lugar correcto, es efectivamente O(1).

**42.** Porque, al estar ambas listas ya ordenadas ascendentemente, el menor elemento disponible de cada lista siempre se encuentra en su nodo actual (el más cercano al frente que aún no ha sido procesado); por lo tanto, comparar solo esos dos nodos basta para garantizar que el elemento elegido sea el menor de todos los elementos restantes en ambas listas.

**46.** `[2, 9]`

**50.** Es más adecuada la Lista Enlazada Simple, porque insertar al inicio (en el head) tiene complejidad O(1), al no requerir desplazar ningún otro elemento. En un Vector, insertar al inicio obliga a desplazar todos los elementos existentes una posición (O(n)). Como el acceso aleatorio por posición —la principal ventaja del Vector— no es un requisito relevante en este caso, no se pierde ninguna ventaja significativa al optar por la lista enlazada.

**55.** Es recursión de cola porque la llamada recursiva `espejo(n // 10, profundidad + 1)` es la última instrucción ejecutada, sin ninguna operación pendiente después de que dicha llamada retorne. Sin embargo, Python no implementa la optimización de llamadas de cola (TCO) de forma nativa, por lo que cada llamada recursiva genera y mantiene su propio stack frame, sin reutilizar el frame anterior; esto significa que, para entradas muy grandes, la función igualmente podría causar un `RecursionError`.

**62.** Porque cada llamada `fib(n)` genera dos llamadas recursivas nuevas, `fib(n-1)` y `fib(n-2)`, y muchos de estos subproblemas se recalculan repetidamente sin guardar resultados previos. Esto genera un árbol de llamadas que crece exponencialmente con respecto a n, ya que el número total de llamadas se duplica aproximadamente en cada nivel de profundidad del árbol de recursión.

**74.** Porque, para aplicar correctamente el "bubble down" (sift-down) en un nodo, es necesario que los subárboles de sus hijos ya cumplan la propiedad de heap. Al procesar primero los nodos más cercanos a las hojas y avanzar hacia la raíz, se garantiza que, cuando se procese un nodo, sus subárboles ya sean heaps válidos, permitiendo que el sift-down funcione correctamente en un solo recorrido.

**78.** Porque una Cola FIFO atendería a los pacientes estrictamente en el orden de llegada, sin considerar la gravedad de su condición, lo cual sería inadecuado en un contexto médico donde un paciente más grave debe ser atendido antes que uno menos grave aunque haya llegado después. La Cola de Prioridad basada en Heap garantiza que siempre se atienda primero al paciente de mayor prioridad, con operaciones eficientes de O(log n) tanto para insertar como para extraer al más grave.

**90.** Si el pivote es siempre el primer elemento y el arreglo ya está ordenado ascendentemente, el pivote resultará ser siempre el menor elemento de la partición actual, generando particiones totalmente desbalanceadas (una partición vacía y otra con n-1 elementos). Esto provoca que la recursión tenga una profundidad de n niveles en lugar de log n, degradando la complejidad a O(n²), que es precisamente el peor caso de Quicksort.

**98.** `28` — Selection Sort realiza siempre (n²-n)/2 comparaciones; con n=8: (64-8)/2 = 28.

**100.** Aunque Heapsort garantiza O(n log n) en el peor caso mientras que Quicksort puede degradarse a O(n²), en la práctica Quicksort suele ser más rápido debido a su mejor localidad de referencia en memoria caché y menor overhead por comparación/intercambio; además, el peor caso de Quicksort puede mitigarse casi por completo con una estrategia de pivote aleatorio. La elección depende del contexto: si se necesita una garantía estricta de rendimiento (por ejemplo, sistemas de tiempo real), Heapsort es preferible; si se prioriza el rendimiento promedio en la mayoría de los casos, Quicksort suele ser la mejor opción.
