# 9. Tabla de multiplicar. Recibe un número e imprime su tabla del 1 al 10.
import sys
if __name__ == "__main__":
    num = int(sys.argv[1])
    for i in range(1,11):
        print(num, "x", i, "=", num * i)
# Datos de prueba: python ej09.py 7