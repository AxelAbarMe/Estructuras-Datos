# 18. ¿Palíndromo? Recibe una palabra e indica si se lee igual al derecho y al revés (ignorando mayúsculas).
import sys
if __name__ == "__main__":
    palabra = sys.argv[1].lower()
    palindromo = palabra == palabra[::-1]
    print("La palabra", sys.argv[1], "es un palíndromo." if palindromo else "no es un palíndromo.")
# Datos de prueba: python ej18.py Reconocer