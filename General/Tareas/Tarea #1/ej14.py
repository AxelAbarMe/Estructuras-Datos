# 14. Estadística aleatoria. Recibe una cantidad N, genera N números aleatorios entre 1 y 100, e imprime el mayor y el promedio.
import sys
import random
if __name__ == "__main__":
    N = int(sys.argv[1])
    numeros = []
    for i in range(N):
        numeros.append(random.randint(1, 100))
    print("Los números generados son:", numeros)
    print("El mayor número es:", max(numeros))
    print("El promedio es:", sum(numeros) / N)
# Datos de prueba: python ej14.py 20