# En este ejercicio, analizarán el rendimiento de lectura de archivos para tres casos distintos. Su tarea consiste en crear tres funciones distintas que abran un archivo de texto (de aproximadamente 10MB de tamaño) y lo lea de la siguiente manera:
# Función #1: Leerá el archivo caracter por caracter
# Función #2: Leerá el archivo línea por línea
# Función #3: Leerá el archivo en bloques de 4096 bytes (4KB).
# Deberá imprimir en pantalla el tiempo que le tomó a cada función terminar su trabajo. ¿Les sorprenden los resultados? ¿Por qué ocurre la diferencia entre cada una de las funciones?

import os
import time

ARCHIVO = "large_text.txt"

def write_text(filename=ARCHIVO):
    if os.path.exists(filename):
        print(f"El archivo '{filename}' ya existe.")
        return
    with open(filename, "w") as f:
        for _ in range(230000):
            f.write("The quick brown fox jumps over the lazy dog.\n")

def read_char(filename=ARCHIVO):
    start = time.perf_counter()
    contador=0
    with open(filename, "r") as f:
        caracter = f.read(1)
        while caracter:
            contador+=1
            caracter = f.read(1)
    return contador, time.perf_counter() - start

def read_line(filename=ARCHIVO):
    start = time.perf_counter()
    contador=0
    with open(filename, "r") as f:
        for line in f:
            contador+=1
    return contador, time.perf_counter() - start

def read_block(filename=ARCHIVO, tam=4096):
    start = time.perf_counter()
    contador=0
    with open(filename, "rb") as f:
        bloque = f.read(tam)
        while bloque:
            contador+=len(bloque)
            bloque = f.read(tam)
    return contador, time.perf_counter() - start

def report(label, filename, read_time):
    size = os.path.getsize(filename)
    print(f"{label}")
    print(f"  File size:  {size:,} bytes")
    print(f"  Read time:  {read_time:.3f} s")

def main():
    write_text()

    _, text_read_time1 = read_char(ARCHIVO)
    report("Caracter por caracter", ARCHIVO, text_read_time1)
    _, text_read_time2 = read_line(ARCHIVO)
    report("Linea por linea", ARCHIVO, text_read_time2)
    _, text_read_time3 = read_block(ARCHIVO)
    report("Bloque de 4KB", ARCHIVO, text_read_time3)

    print("\nResumen de tiempos:")
    print(f"  Caracter por caracter : {text_read_time1:.4f} s")
    print(f"  Línea por línea       : {text_read_time2:.4f} s")
    print(f"  Bloques de 4KB        : {text_read_time3:.4f} s")

if __name__ == "__main__":
    main()