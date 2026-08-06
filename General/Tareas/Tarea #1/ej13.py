# 13. Lanzamiento de dado. Recibe cuántas veces lanzar un dado, simula los lanzamientos e imprime cada resultado. Utilice la librería "random".
import sys
import random
if __name__ == "__main__":
    lanzamientos = int(sys.argv[1])
    print("Resultados de los lanzamientos:")
    for i in range(lanzamientos):
        res = random.randint(1, 6)
        print("Lanzamiento", i+1, ":", res)

# Datos de prueba: python ej13.py 5