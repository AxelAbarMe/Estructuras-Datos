import sys
import json
from queue import LifoQueue

def dron_inst(dron):

    pila = LifoQueue()

    for inst in dron:
        new_inst = inst["cmd"]
        if new_inst == "RETURN":
            break
        elif new_inst == "MOVE":
            pila.put(f"MOVE_BACK x {inst['x']}")
        elif new_inst == "TURN_LEFT":
            pila.put("TURN_RIGHT")
        elif new_inst == "TURN_RIGHT":
            pila.put("TURN_LEFT")
        elif new_inst == "DROP":
            continue
    while not pila.empty():
        print(pila.get())

def main():
    if len(sys.argv) != 2:
        print("Uso: python ej04.py dron.json")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, "r") as f:
            dron = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{filename}'")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Archivo tiene formato JSON inválido")
        sys.exit(1)
    dron_inst(dron)

if __name__ == "__main__":
    main()
