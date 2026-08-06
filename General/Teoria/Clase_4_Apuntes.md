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

## Python with open()

| Mode | Description
|:---:|:-----:
|'r'|	Open text file for reading. Raises an I/O error if the file does not exist.
|'r+'|	Open the file for reading and writing. Raises an I/O error if the file does not exist.
|'w'|	Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist.
|'w+'|	Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist.
|'a'|	Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
|'a+'|	Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
|'rb'|	Open the file for reading in binary format. Raises an I/O error if the file does not exist.
|'rb+'|	Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist.
|'wb'|	Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
|'wb+'|	Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
|'ab'|	Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
|'ab+'|	Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.

### Serialización de los datos binarios:

Se toman los datos que se guardan directo de la memoria, pero para poder leer se necesita de formatear los datos al serializarlos para que este se guarde como OBJ en el disco, y cuando quiera volver a recuperarse dicha información, el formato permita obtener la misma información.

#### pickle

- pickle.dump() -> Serializa la información, dando un formato más adecuado para guardar en disco.
- piclke.load() -> Lee el archivo y los bytes almacenados.

Los archivos binarios para leerlos, el mismo formato de serialización indican cuantos bytes se deben leer, este lee bytes, no caracteres.

### Comparativa 1,000,000 records

Text file (.txt)
- File size: 23,219,754 bytes
- Write time: 0.688 s
- Read time: 0.369 s

Binary file (.bin)
- File size: 16,000,000 bytes
- Write time: 0.078 s
- Read time: 0.120 s

### Rendimiento Comparativa

Leer byte por byte implica operaciones de lectura y de escritura, entre mayor cantidad de lecturas en disco, peor rendimiento tendrá el programa. Es mejor pedir que se lea toda la información necesaria y se envíe directo a la RAM antes que ir poco a poco solo pidiendo lo que se ocupe en el momento.

# Formato Archivos

## XML Extensible Markup Language (Lenguaje de Marcado Extensible) 

Trabaja por etiquetas

```
<user>
  <id>1</id>
  <name>John Doe</name>
  <email>john.doe@example.com</email>
  <is_active>true</is_active>
  <roles>
    <role>admin</role>
    <role>editor</role>
  </roles>
</user>
```

## JSON (JavaScript Object Notation)

Trabaja por llaves

```
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "is_active": true,
  "roles": ["admin", "editor"]
}
```

## YAML (YAML Ain't Markup Language)

Trabaja por valor y llave

```
id: 1
name: John Doe
email: john.doe@example.com
is_active: true
roles:
  - admin
  - editor
```

