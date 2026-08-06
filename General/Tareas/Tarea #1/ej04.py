# 4. Par o impar. Recibe un entero e indica si es par o impar.
import sys
if __name__ == "__main__":
    num = int(sys.argv[1])
    print ("El número", num, "es", "par." if num % 2 == 0 else "impar.")

# Datos de prueba: python ej04.py 9

