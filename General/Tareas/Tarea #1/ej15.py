# 15. Generador de contraseñas. Recibe una longitud L y arma una contraseña aleatoria de esa longitud combinando letras y dígitos.
import string
import sys
import random
if __name__ == "__main__":
    longitud = int(sys.argv[1])
    caracteres = string.ascii_letters + string.digits
    contra = ''.join(random.choice(caracteres) for i in range(longitud))
    print("La contraseña generada es:", contra)
# Datos de prueba: python ej15.py 12