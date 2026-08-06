# 12. Pares en un rango. Recibe dos números a y b e imprime todos los pares entre ellos.
import sys
if __name__ == "__main__":
    print("Los números pares entre", sys.argv[1], "y", sys.argv[2], "son:")
    for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
        if i % 2 == 0:
            print(i)
# Datos de prueba: python ej12.py 3 14