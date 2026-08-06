# 17. Contar vocales. Recibe una frase (entre comillas) y cuenta cuántas vocales tiene.
import sys
if __name__ == "__main__":
    frase = sys.argv[1].lower()
    vocales = "aeiou"
    contador = sum(1 for letra in frase if letra in vocales)
    print("La frase tiene", contador, "vocales.")

# Data de prueba: python ej17.py "Estructuras de Datos"