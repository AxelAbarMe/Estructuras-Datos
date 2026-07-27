# Clase #1 Estructuras de Datos

## Cómo se desarrolla software

### Arquitectura Monolítica

-> Se toma en lenguaje de programación, ejemplo Java, en este se codean todo el código necesario, ósea el código fuente, donde se segmentan en las diferentes funcionalidades o features implementadas. Este se compila y genera el archivo ejecutable (.exe), llamado Artifact. Donde normalmente se utiliza el server para ejecutar dicha aplicación.

Servidor utiliza (En resumen) para ejecutar la aplicación es del CPU y RAM llamada Compute
Aquellas que sean exitosas requeriran mayor cantidad de CPU y RAM, incluso llegando hasta un 100% de su uso.
Pero si la applicación no se codeo para implementar un segundo servidor, esto es una desventaja.

Otra desventaja es que, si hay necesidad de actualizar un recurso, hay que bajar el servidor, probarlo y actualizar las nuevas funcionalidades que ya existen anteriormente.

A causa de esto, nacio una nueva arquitectura de tecnologias retomadas

### Arquitectura de microservicios

-> Vamos a agarrar el código y separar cada funcionalidad en módulos totalmente separados como si fuesen aplicaciones individuales, se repite con cada funcionalidad diferente. Lo que dice entonces es que no existe un solo código fuente, sino que se separa la lógica del programa en módulos totalmente independientes. Cada microservicio se logra ejecutar en un contenedor, es el principio de responsabilidad única aplicado más allá.
Una ventaja es que cada aplicación puede desarrollarse en lenguajes diferentes como Java, Python, Rust, C++.
Que sucede si se quiere escalar? Agregar nuevos contenedores que permiten implementar.

Actualización de contenedor, para esto se quita la v1 y se ingresa la v2.

De esto nace las Apps Cloud Native, basadas en microservicios, escalables y son elásticas (Quitar y poner según la cantidad de recursos que necesiten). Que pasa si el módulo 2 ocupa información del módulo 5, como se conectan las partes? Esto se responde con las API (Application Programming Interface) son partes del código que se exponen para que agentes externos sean capaces de obtener. Está interfaz básicamente se resume en objetos, en la interfaz pública de los objetos, entonces el M2 consume la API del M5, el M6 consume el API del M4.

#### Tipos de API

REST API (Más común).
SOAP
GraphQL

---

# Clase #2 Estructuras de Datos

Codigo fuente se encuentra en HDD o SSD, la carga de trabajo se realiza cuando se encuentra en la memoria RAM, sistema operativo se encarga de definir instrucciones en espacio de memoria, dichas instrucciones que lleguen a la RAM se encuentran listas para el CPU.

--->Pregunta Importante: Cuales son los componentes necesarios para la ejecución de un programa? RAM y CPU, llamado Compute

Archivos no son importantes para la ejecución de un programa debido a que la RAM es volátil y el disco duro es solamente para guardar dicha información una vez el sistema se apaguen.

CPU tiene memoria temporal donde guarda las instrucciones de memoria.

## Ciclo de instrucciones

Fetch: Traer instrucciones de memoria RAM para ejecutarlas
Decode: Tomar instrucción y la decodifica.
Execute: Al estar lista, la ejecuta.

ALU ejecuta las instrucciones matemáticas y lógicas
->Registros

## Arquitectura de la CPU y PC

Se refiere a las x86, fabricantes de Intel, AMD. Existe otra arquitectura ARM abierto para cualquier fabricante.

x86 - 64 | Potencia	  | Mayor consumo de energía
ARM 	 | Menor Potencia | Menor consumo de energía
Esto afecta directamente en el consumo de la batería en el caso de los teléfonos móviles, debido a que ARM consume menor.

Chips de ARM alcanzan el mismo nivel de potencia de Intel a un costo energético menor. Cloud computing importante porque a mayor consumo energético, aumenta el costo. ARM entonces genera menor costo. Migración de arquitecturas x86 a ARM genera ahorros de miles de dólares.

Pensamiento cloud computing, enfocarse únicamente en RAM y CPU

## Memoria

1 byte es el mínimo que se guarda en una celda de memoria, se guarda una dirección hexadecimal 0x0000, 0x0001, 0x0002 ... 0xffff.

Tamaño de int varia según arquitectura, en un x86 puede variar entre 4 bytes (64) a 2 bytes (32), en ARM usualmente el int tiene de tamaño 8 bytes.

Se asigna en memoria RAM desde una dirección inicial el tamaño de los bytes en las diferentes celdas hasta el tamaño total del tipo de var utilizada.

### Como se ejecuta entonces la aplicación en memoria RAM?

Espacio de memoria se divide en varias secciones-

```
Low address-> Text segment		 <- Static Memory Layout		  |	<-- Espacio de dirección
	      Initialised Data		 <- Static Memory Layout    	  |	<-- Espacio de dirección
	      UnInitialised Data (BSS)   <- Static Memory Layout  	  |	<-- Espacio de dirección
------------------------------------------------------------------|
	Heap								 <- Dynamic Memory Layout |	<-- Espacio de dirección
	->									 <- Dynamic Memory Layout |	<-- Espacio de dirección
	->									 <- Dynamic Memory Layout |	<-- Espacio de dirección
	Stack								 <- Dynamic Memory Layout |	<-- Espacio de dirección
------------------------------------------------------------------|
High Address ->	Command-line Arguments & Environment Variables    |	<-- Espacio de dirección


					Cada linea tiene asignada un espacio de memoria

#include <iostream>			0x0040
#include <string>			0x0044

int numero = 10;			0x0048
int suma(int a, int b){		0x0052 y así sucesivamente, no siempre va de 4 en 4
	int res;
	res a+b;
	return res;
}

int main(){					0x0068
	int x=10;				0x0072
	int y=20;

	std::cout << suma(x,y);
	std::cout << numero;

	return 10;
}
```

Variables locales/automáticas
variables globales
Asignaciones aritmeticas
Bibliotecas
funciones std::cout
Son partes del programa, cada una se almacena en diferentes partes en el espacio de direcciones

### Ordena entonces ese código en el espacio de direcciones

Empezando en low address:

El segmento código, o el .text: se almacena todo el código, las instrucciones. (Lo que contiene la función suma y función main). Esta parte de la memoria es solo lectura (Read Only).

Segmento de datos: Se almacenan las variables globales y estáticas, existe la posibilidad a acceder a estos datos desde cualquier lugar del programa, gracias a que pertenecen al segmento de datos.
.data  Variables ya inicializadas se guardan en el .data
.bss   Variables sin inicializar se guardan en el BSS (.bss)

.heap  Guarda toda la información de memoria dinámica, objetos creados durante la ejecución del programa se ubican aquí, no se sabe que llenará está zona hasta que no se este ejecutando el programa. Tiene la propiedad de que crece y decrece (al liberar memoria). En c++ al usar new y en C al usar malloc. Se hace manual y es responsabilidad del programador. Que pasa con Python y Java? El manejo de la memoria dinámica o el heap se realiza de manera automática. Sino se maneja la memoria dinámica correctamente, puede ocurrir que nos quedemos sin memoria, out of memory. Memory Leak.

.stack  Es el único espacio de memoria que crece al revez, al disminuirse (Más alta hacia abajo). En el stack se guarda a las variables locales y los retornos de funciones. Importante retorno de funciones para recursividad y estructuras de stack.

Para ejemplo int x=10;
Se guarda en el stack 4Bytes, de dirección de memoria 0x1234.
Compilador crea tabla con las variables, llamada tabla de símbolo, donde guarda nombre, tipo y alcance.

## QUIZ

En que dirección de memoria está almacenada la función main? En el segmento código, en la dirección de memoria 0x0068. Aquí entonces inicia una función.

Res no está en el segmento código, ya que .text es solamente Read Only, las variables deben ir en otro espacio de direcciones diferente.

En cual parte de la memoria está almacenada la variable global int numero = 10; En la memoria de .data (Global inicializada)

Las librerías se ubican donde? En .text

Que ocurre con int* x = new int[10]
Operador new asigna suficiente memoria para el tamaño del objeto [10], con dirección de memoria 0x4000, new devuelve entonces 0x4000, esa dirección de memoria se guarda en x, pero x se encuentra en el stack.

x guarda 0x4000 en el stack (Variable local, de tipo puntero, guarda dirección 0x4000, que apunta a un objeto del heap que es un entero). Ya que cout << x imprime 0x4000, pero cout << *x imprime 10, el valor al que apunte.

&x, x se encuentra en el stack, en la dirección 0x2100, x con el & aparece la dirección de memoria 0x2100

Puntero global o estatico se guarda en .data o .bss

x se encuentra en 0x0500, x almacena [0x4000], en 0x4000 se tiene 0x2000, y en 0x2000 se tiene el valor int 10.
En este caso:

- &x imprime 0x0500	Dirección donde está x
- x imprime 0x4000	Dirección que almacena x
- *x imprime 0x2000	Contenido que apunta x
- **x imprime 10		Contenido apuntado por el contenido que apunta x

## Compilación -> C/C++ / Java

Un código compilado es un proceso donde se tiene el código fuente, este se compila. Que se genera compilar? Se genera el .text, .data y .bss, además genera lenguaje máquina (x86 - 64 o ARM). No se puede ejecutar un código compilado en una arquitectura diferente.

Código fuente al ser compilado genera el .obj (Código objeto) que está en lenguaje máquina variado según su arquitectura.

Existe un proceso después de compilar llamado linker (o enlazado), el compilador obtiene las bibliotecas del lenguaje compilado, y estas bibliotecas no se compilan, ya que están pre compiladas. El proceso agarra el .obj compilado del programa y lo mezcla junto con las librerías pre compiladas y genera entonces el ejecutable .exe. Y hace Run.

Para el caso de Debug, genera el mismo proceso de compilación, pero la diferencia es que genera un flag donde le pide al CPU que ejecute cada línea de código una por una.
