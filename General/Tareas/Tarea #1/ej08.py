# 8. Cuenta regresiva. Recibe un número N e imprime desde N hasta 1.
import sys
if __name__ == "__main__":
    for i in range(int(sys.argv[1]), 0, -1):
        print(i)
# Datos de prueba: python ej08.py 10