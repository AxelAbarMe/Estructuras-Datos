# Tarea 2

## Instrucciones

### Ejercicio #1

En este ejercicio, analizarán el rendimiento de lectura de archivos para tres casos distintos. Su tarea consiste en crear tres funciones distintas que abran un archivo de texto (de aproximadamente 10MB de tamaño) y lo lea de la siguiente manera:

- Función #1: Leerá el archivo caracter por caracter
- Función #2: Leerá el archivo línea por línea
- Función #3: Leerá el archivo en bloques de 4096 bytes (4KB).

Deberá imprimir en pantalla el tiempo que le tomó a cada función terminar su trabajo. ¿Les sorprenden los resultados? ¿Por qué ocurre la diferencia entre cada una de las funciones?

**Nota:** Para crear archivos de texto de ese tamaño, pueden crear un archivo de la siguiente manera:

```python
with open("large_text.txt", "w") as f:
    for _ in range(1500000):  # ~10MB total
        f.write("The quick brown fox jumps over the lazy dog.\n")
```

Asegúrense de que el tamaño del archivo sea de 10MB aproximadamente.

### Ejercicio #2

Escriba un programa en Python que permita guardar y recuperar datos de archivos en los tres formatos: XML, JSON, YAML. Ustedes pueden utilizar los datos que deseen en estos archivos.
