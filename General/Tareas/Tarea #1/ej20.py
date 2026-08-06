# 20. Analizar archivo. Recibe la ruta de un archivo de texto, lo lee e imprime cuántas líneas, palabras y caracteres contiene.
import sys
if __name__ == "__main__":
    archivo = sys.argv[1]
    with open(archivo, 'r') as f:
        cont = f.read()
        lineas = cont.splitlines()
        palabras = cont.split()
        caracteres = len(cont)
        print("El archivo tiene", len(lineas), "líneas,", len(palabras), "palabras y", caracteres, "caracteres.")
# Datos de prueba: python ej20.py salida.txt