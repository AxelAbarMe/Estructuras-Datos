# 19. Escribir en archivo. Recibe el nombre de un archivo seguido de varias palabras, y las guarda en el archivo, una por línea.
import sys
if __name__ == "__main__":
    archivo = sys.argv[1]
    palabras = sys.argv[2:]
    with open(archivo, 'w') as f:
        for palabra in palabras:
            f.write(palabra + '\n')
# Datos de prueba: python ej19.py salida.txt manzana pera uva