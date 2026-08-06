# 5. Signo del número. Recibe un número e imprime si es positivo, negativo o cero.
import sys
if __name__ == "__main__":
    num = int(sys.argv[1])
    print ("El número", num, "es", "positivo." if num > 0 else "negativo." if num < 0 else "cero.")

# Datos de prueba: python ej05.py -3