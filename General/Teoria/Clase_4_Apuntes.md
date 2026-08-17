# 4: Archivos

## Tipos de archivos

* Texto
* Binarios

**Se diferencian en cómo se almacenan en el disco duro.** Importante para espacio y rendimiento.

### Características — Texto

* Representan una secuencia de caracteres.
* Cuando se abre el archivo, el tipo de contenido que se observa es texto.
* Almacenan cada representación del carácter.

### Características — Binarios

* Representación en formato máquina, binaria (bits).
* Almacenan cada representación binaria del carácter.

---

## Codificación de caracteres

Se refiere a qué hace la computadora para saber qué tipo de carácter se quiere representar.

* Se tienen diferentes idiomas con otros alfabetos.
* **ASCII** es de los primeros sistemas de codificación de caracteres; cada letra tiene una representación numérica: 7 bits en su primera versión (128 caracteres). Luego hubo mejoras de 8 bits para 256 caracteres.

| Carácter | Decimal | Binario |
|:---:|:---:|:---:|
| 'A' | 65 | 01000001 |
| 'a' | 97 | 01100001 |
| '8' | 56 | 00111000 |

* ASCII provocó que existieran evoluciones como **Unicode**.
* Unicode contiene hasta 240.000 caracteres, cada uno con su propio código.
* Unicode reserva mayor cantidad de bits para almacenar un carácter.

> **Nota adicional:** el estándar más usado hoy en día para representar Unicode en archivos y en la web es UTF-8, ya que es compatible hacia atrás con ASCII (los primeros 128 caracteres ocupan exactamente 1 byte, igual que en ASCII).

---

## Encoding

Al trabajar con una versión de Unicode y el navegador trabaja con otra, va a haber caracteres diferentes.

* Unicode UTF-8
* Unicode UTF-16
* Unicode UTF-32

Los mecanismos de codificación deben coincidir.

### Ejemplo

`"Tengo 3 consolas"`. Cada carácter tiene una representación. Lo que se guarda es el texto codificado con el mecanismo usado.

UTF-8 guarda entonces la `T` con 8 bits de espacio, la `e` son otros 8 bits. En resumen, se guarda un byte por cada carácter en el archivo.

La representación binaria no usa el mecanismo de codificación del carácter, sino la representación binaria de cómo está en la memoria RAM.

* Si son enteros, se guarda en espacio de bits. Al guardar el `12345678` con arquitectura de 32 bits, se guarda en 4 bytes.

### Comparación

| Formato | Tamaño |
|:---:|:---:|
| Texto | 10 Bytes |
| Binario | 8 Bytes |

Los archivos binarios usan menos espacio para guardar elementos. Esto significa que los archivos binarios son preferidos por rendimiento. Se seleccionan según el diseño que se requiera: textos extensos son útiles usando binarios; en cambio, texto es útil cuando se necesita saber qué significa la información.

---

## Rendimiento (Performance)

En el disco se almacenan los archivos, se comunican con la RAM para llegar al programa.

* La RAM lee el archivo, la RAM comunica los datos al CPU, debido a que el CPU únicamente puede comunicarse con la RAM por temas de diseño de hardware (velocidad).
* Cargar un archivo a la memoria es una operación costosa, ya que dura más tiempo.

| Componente | Velocidad | Espacio |
|:---:|:---:|:---:|
| CPU | Rápido | Menos espacio |
| RAM | — | — |
| HDD | Menos rápido | Más espacio |

Es eficiente tener los datos necesarios en RAM antes que tenerlos en el disco. ¿Cómo hacer que el CPU evite ir a memoria cada vez que necesita? El **caché** guarda cierta información para tenerla lo más cercana posible. Utilizar caché es necesario para *High Performance*.

---

## Python `with open()`

| Mode | Description |
|:---:|:-----|
| `'r'` | Open text file for reading. Raises an I/O error if the file does not exist. |
| `'r+'` | Open the file for reading and writing. Raises an I/O error if the file does not exist. |
| `'w'` | Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist. |
| `'w+'` | Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist. |
| `'a'` | Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist. |
| `'a+'` | Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist. |
| `'rb'` | Open the file for reading in binary format. Raises an I/O error if the file does not exist. |
| `'rb+'` | Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist. |
| `'wb'` | Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist. |
| `'wb+'` | Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist. |
| `'ab'` | Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist. |
| `'ab+'` | Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist. |

---

## Serialización de los datos binarios

Se toman los datos que se guardan directo de la memoria, pero para poder leerlos se necesita formatear los datos al serializarlos para que se guarden como OBJ en el disco, y cuando se quiera volver a recuperar dicha información, el formato permita obtener la misma información.

### pickle

* `pickle.dump()` → Serializa la información, dando un formato más adecuado para guardar en disco.
* `pickle.load()` → Lee el archivo y los bytes almacenados.

Los archivos binarios, para leerlos, usan el mismo formato de serialización, el cual indica cuántos bytes se deben leer; este lee bytes, no caracteres.

### Comparativa (1,000,000 records)

**Text file (.txt)**
* File size: 23,219,754 bytes
* Write time: 0.688 s
* Read time: 0.369 s

**Binary file (.bin)**
* File size: 16,000,000 bytes
* Write time: 0.078 s
* Read time: 0.120 s

### Rendimiento Comparativa

Leer byte por byte implica múltiples operaciones de lectura y escritura; entre mayor cantidad de lecturas en disco, peor rendimiento tendrá el programa. Es mejor pedir que se lea toda la información necesaria y se envíe directo a la RAM, en lugar de ir poco a poco solo pidiendo lo que se ocupe en el momento.

---

## Formato de Archivos

### XML (Extensible Markup Language)

Trabaja por etiquetas.

```xml
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

### JSON (JavaScript Object Notation)

Trabaja por llaves.

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "is_active": true,
  "roles": ["admin", "editor"]
}
```

### YAML (YAML Ain't Markup Language)

Trabaja por valor y llave.

```yaml
id: 1
name: John Doe
email: john.doe@example.com
is_active: true
roles:
  - admin
  - editor
```

> **Nota adicional:** de los tres, JSON suele ser el más común en APIs REST modernas por su ligereza; XML se mantiene en sistemas empresariales/SOAP; YAML es muy usado en archivos de configuración (por ejemplo, Docker Compose o pipelines de CI/CD) por ser el más legible para humanos.
