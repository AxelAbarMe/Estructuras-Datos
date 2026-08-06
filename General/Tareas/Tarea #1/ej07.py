# 7. Clasificación de nota. Recibe un puntaje (0–100) y devuelve la letra correspondiente: A (90+), B (80–89), C (70–79), D (60–69), F (<60).
import sys
if __name__ == "__main__":
    nota = int(sys.argv[1])
    if nota < 0 or nota > 100:
        print("Nota inválida. Solo 0-100 son aceptables.")
    elif nota >= 90:
        print("La nota es A")
    elif nota >= 80:
        print("La nota es B")
    elif nota >= 70:
        print("La nota es C")
    elif nota >= 60:
        print("La nota es D")
    else:
        print("La nota es F")
# Datos de prueba: python ej07.py 84