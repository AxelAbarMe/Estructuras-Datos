# 3. Área de un rectángulo. Recibe la base y la altura, e imprime el área y el perímetro.
import sys
if __name__ == "__main__": 
    base = int(sys.argv[1])
    altura = int(sys.argv[2])
    area = base * altura
    perimetro = 2 * (base + altura)
    print("El área del rectángulo es:", area, " | El perímetro del rectángulo es:", perimetro)
# Datos de prueba: python ej03.py 4 6