import sys
import json

def enter_list(entry_list):

    VIPresult = []
    NORMresult = []
    BULKresult = []

    for person in entry_list:
        tipo = person["tipo"]
        name = person["nombre"]

        if tipo == "VIP":
            VIPresult.append(name)
        elif tipo == "NORM":
            NORMresult.append(name)
        elif tipo == "BULK":
            BULKresult.append(name)
        else:
            print(f"Error: Tipo desconocido '{tipo}' para '{name}'")
            sys.exit(1)

    return VIPresult + NORMresult + BULKresult



def main():
    if len(sys.argv) != 2:
        print("Uso: python ej03.py comedor.json")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, "r") as f:
            entry_list = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{filename}'")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Archivo tiene formato JSON inválido")
        sys.exit(1)

    result = enter_list(entry_list)
    print(" ".join(result))

if __name__ == "__main__":
    main()