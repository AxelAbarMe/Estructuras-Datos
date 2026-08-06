# 11. Factorial. Recibe N y calcula su factorial usando un ciclo.
import sys
if __name__ == "__main__":
    num = int(sys.argv[1])
    res = 1
    for i in range(1, num + 1):
        res *= i
    print("El factorial del número", num, "es:", res)
# Datos de prueba: python ej11.py 5