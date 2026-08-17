# 1-2: Estructuras de Datos — Arquitecturas y Memoria

## Cómo se desarrolla software

### Arquitectura Monolítica

Se toma un lenguaje de programación (ejemplo Java), en este se codea todo el código necesario, o sea el código fuente, donde se segmentan en las diferentes funcionalidades o features implementadas. Este se compila y genera el archivo ejecutable (.exe), llamado **Artifact**. Normalmente se utiliza un servidor para ejecutar dicha aplicación.

* El servidor utiliza (en resumen) para ejecutar la aplicación el CPU y la RAM, llamado **Compute**.
* Aquellas aplicaciones que sean exitosas requerirán mayor cantidad de CPU y RAM, incluso llegando hasta un 100% de su uso.
* **Desventaja:** si la aplicación no se codeó para implementar un segundo servidor, no se puede escalar.
* **Otra desventaja:** si hay necesidad de actualizar un recurso, hay que bajar el servidor, probarlo y actualizar las nuevas funcionalidades que ya existían anteriormente.

A causa de esto, nació una nueva arquitectura de tecnologías retomadas.

### Arquitectura de Microservicios

Se agarra el código y se separa cada funcionalidad en módulos totalmente separados, como si fuesen aplicaciones individuales; esto se repite con cada funcionalidad diferente. No existe un solo código fuente, sino que se separa la lógica del programa en módulos totalmente independientes. Cada microservicio se ejecuta en un contenedor; es el principio de responsabilidad única aplicado más allá.

* **Ventaja:** cada aplicación puede desarrollarse en lenguajes diferentes, como Java, Python, Rust, C++.
* **¿Qué sucede si se quiere escalar?** Se agregan nuevos contenedores que permiten implementar más capacidad.
* **Actualización de contenedor:** para esto se quita la v1 y se ingresa la v2.

De esto nacen las **Apps Cloud Native**, basadas en microservicios, escalables y elásticas (quitar y poner según la cantidad de recursos que necesiten).

**¿Qué pasa si el módulo 2 ocupa información del módulo 5? ¿Cómo se conectan las partes?**

Esto se responde con las **API** (Application Programming Interface): son partes del código que se exponen para que agentes externos sean capaces de obtener información o funcionalidad. Esta interfaz básicamente se resume en objetos, en la interfaz pública de los objetos; entonces el M2 consume la API del M5, el M6 consume la API del M4.

#### Tipos de API

* REST API (más común)
* SOAP
* GraphQL

> **Nota adicional:** REST se apoya en el protocolo HTTP y en verbos estándar (GET, POST, PUT, DELETE); SOAP usa mensajes XML más estrictos y suele verse en sistemas empresariales/bancarios; GraphQL permite al cliente pedir exactamente los campos que necesita en una sola consulta, evitando sobrecarga de datos.

---

## Ejecución de un programa: RAM y CPU

El código fuente se encuentra en HDD o SSD; la carga de trabajo se realiza cuando se encuentra en la memoria RAM. El sistema operativo se encarga de definir instrucciones en el espacio de memoria; dichas instrucciones que lleguen a la RAM se encuentran listas para el CPU.

> **Pregunta importante:** ¿Cuáles son los componentes necesarios para la ejecución de un programa? RAM y CPU, llamado **Compute**.

Los archivos no son importantes para la ejecución de un programa, debido a que la RAM es volátil y el disco duro solamente sirve para guardar dicha información una vez el sistema se apague.

El CPU tiene memoria temporal donde guarda las instrucciones de memoria.

### Ciclo de instrucciones

* **Fetch:** Traer instrucciones de la memoria RAM para ejecutarlas.
* **Decode:** Tomar la instrucción y decodificarla.
* **Execute:** Al estar lista, se ejecuta.

La **ALU** ejecuta las instrucciones matemáticas y lógicas → Registros.

---

## Arquitectura de la CPU y PC

Se refiere a las x86, fabricantes Intel, AMD. Existe otra arquitectura, ARM, abierta para cualquier fabricante.

| Arquitectura | Potencia | Consumo de energía |
|:---:|:---:|:---:|
| x86-64 | Mayor | Mayor consumo |
| ARM | Menor | Menor consumo |

Esto afecta directamente el consumo de batería en el caso de los teléfonos móviles, debido a que ARM consume menos.

* Los chips de ARM alcanzan el mismo nivel de potencia que Intel a un costo energético menor.
* Cloud computing: importante porque a mayor consumo energético, aumenta el costo. ARM entonces genera menor costo.
* La migración de arquitecturas x86 a ARM genera ahorros de miles de dólares.

> Pensamiento cloud computing: enfocarse únicamente en RAM y CPU.

---

## Memoria

* 1 byte es el mínimo que se guarda en una celda de memoria; se guarda en una dirección hexadecimal: `0x0000, 0x0001, 0x0002 ... 0xffff`.
* El tamaño de `int` varía según la arquitectura: en x86 puede variar entre 4 bytes (64) a 2 bytes (32); en ARM usualmente el `int` tiene un tamaño de 8 bytes.
* Se asigna en memoria RAM, desde una dirección inicial, el tamaño de los bytes en las diferentes celdas hasta el tamaño total del tipo de variable utilizada.

### ¿Cómo se ejecuta la aplicación en memoria RAM?

El espacio de memoria se divide en varias secciones:

```
Low address ->  Text segment                <- Static Memory Layout    | <-- Espacio de dirección
                Initialised Data            <- Static Memory Layout    | <-- Espacio de dirección
                UnInitialised Data (BSS)    <- Static Memory Layout    | <-- Espacio de dirección
------------------------------------------------------------------|
                Heap                        <- Dynamic Memory Layout   | <-- Espacio de dirección
                ->                          <- Dynamic Memory Layout   | <-- Espacio de dirección
                ->                          <- Dynamic Memory Layout   | <-- Espacio de dirección
                Stack                       <- Dynamic Memory Layout   | <-- Espacio de dirección
------------------------------------------------------------------|
High Address -> Command-line Arguments & Environment Variables         | <-- Espacio de dirección


                    Cada línea tiene asignada un espacio de memoria

#include <iostream>            0x0040
#include <string>              0x0044

int numero = 10;               0x0048
int suma(int a, int b){        0x0052 y así sucesivamente, no siempre va de 4 en 4
    int res;
    res a+b;
    return res;
}

int main(){                    0x0068
    int x=10;                  0x0072
    int y=20;

    std::cout << suma(x,y);
    std::cout << numero;

    return 10;
}
```

Componentes que forman parte del programa (cada una se almacena en diferentes partes del espacio de direcciones):

* Variables locales/automáticas
* Variables globales
* Asignaciones aritméticas
* Bibliotecas
* Funciones `std::cout`

### Orden del código en el espacio de direcciones

Empezando en *low address*:

* **Segmento código (.text):** se almacena todo el código, las instrucciones (lo que contiene la función `suma` y la función `main`). Esta parte de la memoria es solo lectura (Read Only).
* **Segmento de datos:** se almacenan las variables globales y estáticas; existe la posibilidad de acceder a estos datos desde cualquier lugar del programa gracias a que pertenecen al segmento de datos.
  * `.data` → Variables ya inicializadas se guardan en `.data`.
  * `.bss` → Variables sin inicializar se guardan en el BSS (`.bss`).
* **`.heap`:** Guarda toda la información de memoria dinámica; objetos creados durante la ejecución del programa se ubican aquí, no se sabe qué llenará esta zona hasta que no se esté ejecutando el programa. Tiene la propiedad de que crece y decrece (al liberar memoria). En C++ se usa `new` y en C, `malloc`; se hace manual y es responsabilidad del programador.
  * ¿Qué pasa con Python y Java? El manejo de la memoria dinámica (heap) se realiza de manera automática.
  * Si no se maneja la memoria dinámica correctamente, puede ocurrir que nos quedemos sin memoria: *out of memory* / **Memory Leak**.
* **`.stack`:** Es el único espacio de memoria que crece al revés, es decir, disminuye (más alta hacia abajo). En el stack se guardan las variables locales y los retornos de funciones. Es importante para la recursividad y las estructuras de stack.

#### Ejemplo aplicado

Para `int x=10;` → se guarda en el stack 4 bytes, en la dirección de memoria `0x1234`.

El compilador crea una tabla con las variables, llamada **tabla de símbolos**, donde guarda nombre, tipo y alcance.

* ¿En qué dirección de memoria está almacenada la función `main`? En el segmento código, en la dirección de memoria `0x0068`. Aquí inicia una función.
* `res` no está en el segmento código, ya que `.text` es solamente de lectura (Read Only); las variables deben ir en otro espacio de direcciones diferente.
* ¿En cuál parte de la memoria está almacenada la variable global `int numero = 10;`? En la memoria de `.data` (global inicializada).
* Las librerías se ubican en `.text`.

#### ¿Qué ocurre con `int* x = new int[10]`?

El operador `new` asigna suficiente memoria para el tamaño del objeto `[10]`, con dirección de memoria `0x4000`; `new` devuelve entonces `0x4000`, esa dirección de memoria se guarda en `x`, pero `x` en sí se encuentra en el stack.

* `x` guarda `0x4000` en el stack (variable local, de tipo puntero, guarda la dirección `0x4000`, que apunta a un objeto del heap que es un entero).
* `cout << x` imprime `0x4000`, pero `cout << *x` imprime `10`, el valor al que apunta.
* `&x`: como `x` se encuentra en el stack, en la dirección `0x2100`, `&x` retorna la dirección de memoria `0x2100`.
* Un puntero global o estático se guarda en `.data` o `.bss`.

**Ejemplo de doble puntero:** `x` se encuentra en `0x0500`, `x` almacena `[0x4000]`, en `0x4000` se tiene `0x2000`, y en `0x2000` se tiene el valor `int 10`.

| Expresión | Resultado | Significado |
|:---:|:---:|:---|
| `&x` | `0x0500` | Dirección donde está `x` |
| `x` | `0x4000` | Dirección que almacena `x` |
| `*x` | `0x2000` | Contenido al que apunta `x` |
| `**x` | `10` | Contenido apuntado por el contenido al que apunta `x` |

---

## Compilación (C/C++ / Java)

Un código compilado es un proceso donde se tiene el código fuente y este se compila. ¿Qué se genera al compilar? Se genera el `.text`, `.data` y `.bss`, además se genera lenguaje máquina (x86-64 o ARM). No se puede ejecutar un código compilado en una arquitectura diferente.

* El código fuente, al ser compilado, genera el `.obj` (código objeto), que está en lenguaje máquina según su arquitectura.
* Existe un proceso posterior a la compilación llamado **linker** (o enlazado): el compilador obtiene las bibliotecas del lenguaje compilado, y estas bibliotecas no se compilan, ya que están pre compiladas. El proceso agarra el `.obj` compilado del programa y lo mezcla junto con las librerías pre compiladas, generando entonces el ejecutable `.exe`, y hace *Run*.
* Para el caso de **Debug**, genera el mismo proceso de compilación, pero la diferencia es que genera un *flag* donde le pide al CPU que ejecute cada línea de código una por una.

> **Nota adicional:** el binario `.obj` de Java en realidad es *bytecode* (`.class`), que no es lenguaje máquina nativo; corre sobre la JVM, lo cual explica por qué Java sí es portable entre arquitecturas a diferencia de C/C++.
