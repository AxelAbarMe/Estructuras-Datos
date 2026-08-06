# 1. Saludo personalizado. Recibe un nombre y una edad, e imprime un saludo del tipo "Hola, Ana. El próximo año tendrás 21 años."
import sys
if __name__ == "__main__":
    nombre, edad = sys.argv[1], int(sys.argv[2])
    print(f"Hola, {nombre}. El próximo año tendrás {edad + 1} años.")
# Datos de prueba: python ej01.py Ana 20