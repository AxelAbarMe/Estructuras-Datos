# Archivos

## Tipos de archivos

- Texto
- Binarios

**Se diferencian en como se almacenan en el disco duro**

**Importante para espacio y rendimiento**

## Características

### Texto

- Representan una secuencia de caracteres.
- Cuando se abre el archivo el tipo de contenido que se observa es texto
- Almacenan cada representación del caracter.

### Binarios

- Representación en formato máquina, binaria (bits).
- Almacenan cada representación binaria del caracter.

## Codificación de caracteres

Se refiere a que hace la computadora para saber que tipo de caracter se quiere representar

- Se tiene diferentes idiomas con otros alfabetos.
- ASCII es de los primeros sistemas de codificación de caracteres, cada letra tiene una representación numérica, 7 bits primera versión (128 caracteres). Luego hubo mejoras de 8bit para 256 caracteres

1. 'A' -> 65 (01000001)
2. 'a' -> 97 (01100001)
3. '8' -> 56 (00111000)

- ASCII provoco que existieran evoluciones como Unicode.
- Unicode contiene hasta 240000 caracteres cada uno con su propio código
- Unicode reserva mayor cantidad de bits para almacenar un caracter

## Encoding

Al trabajar con una versión de unicode y el navegador trabaja con otra, va a haber caracteres diferentes.

- Unicode UTF-8
- Unicode UTF-16
- Unicode UTF-32

Mecanismos de codificación deben coincidir.

## Ejemplo

"Tengo 3 consolas". Cada carácter tiene una representación. Lo que se guarda es el texto codificado con el mecanismo usado.

UTF-8 guarda entonces la T con 8bit de espacio, e son otros 8bits.

En resumen, se guarda un Byte por cada carácter en el archivo.

Representación binaria no usa el mecanismo de codificación del carácter, sino usar la representación binaria de como está en la memoria RAM.

Si son enteros se guarda en espacio de bits. Al guardar el 12345678 con arquitectura de 32 bit, se guarda en 4 Bytes.

### Comparación:

- Texto: 10Bytes
- Binario: 8Bytes

Archivos binarios usan menos espacio para guardar elementos. Esto significa que los archivos binarios son preferidos por rendimiento.

Se seleccionan según el diseño que se requiera, textos extensos son útiles usando binarios, en cambio texto son útiles cuando se necesita saber que significa la información.

## Rendimiento (Performance)

En el disco se almacenan los archivos, se comunica en la RAM para llegar al programa.

RAM lee archivo, RAM comunica datos a CPU, debido a que CPU únicamente puede comunicarse con la RAM por temas de diseño de hardware por velocidad.

Cargar archivo a la memoria es una operación costosa, ya que dura más tiempo.

- CPU rápido/menos espacio
- RAM
- HDD menos rápido/más espacio

Eficiente es tener datos necesarios en RAM antes que tenerlo en el disco.

Como hacer que el CPU evite ir a memoria cada vez que necesita? El caché guarda cierta información para tenerlo lo más cercano.

Utilizar caché es necesario para High performance



