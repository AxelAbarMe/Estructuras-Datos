import sys

def ocurrencias(palabra, letra):
    if palabra=="":
        return 0
    coincidencia = 1 if palabra[0] == letra else 0
    return coincidencia + ocurrencias(palabra[1:], letra)

def main():
    if len(sys.argv) > 2:
        palabra, letra = sys.argv[1], sys.argv[2]
        print(ocurrencias(palabra,letra))
    else:
        print("Error. Requiere Argumento")


if __name__ == "__main__":
    main()