# 10. Suma acumulada. Recibe N y calcula la suma de todos los enteros de 1 hasta N.
import sys
if __name__ == "__main__":
    num = int(sys.argv[1])
    suma = sum(range(1, num+1))
    print("La suma acumulada es:", suma)
# Datos de prueba: python ej10.py 100