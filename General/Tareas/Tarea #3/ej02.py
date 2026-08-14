import sys
import json
from queue import LifoQueue

def hhmm(hhmm):
    horas, mins = hhmm.split(":")
    return int(horas) * 60 + int(mins)

def comprimir_eventos(eventos):

    pila = LifoQueue()

    for evento in eventos:
        init = hhmm(evento["inicio"])
        duration = evento["duracion"]
        room = evento["sala"]

        if not pila.empty():
            last = pila.get()
            last_end = hhmm(last["inicio"]) + last["duracion"]

            if last["sala"] == room and init == last_end:
                last["duracion"] += duration
                pila.put(last)
                continue
            else:
                pila.put(last)
        pila.put({
            "inicio": evento["inicio"],
            "duracion": duration,
            "sala": room
        })
    tmp = []
    while not pila.empty():
        tmp.append(pila.get())
    tmp.reverse()

    return tmp

def format_json(eventos):
    lines = []
    for e in eventos:
        line = ' { "inicio": "%s", "duracion": %d, "sala": "%s" }' % (
            e["inicio"], e["duracion"], e["sala"]
        )
        lines.append(line)
    return "[\n" + ",\n".join(lines) + "\n]"

def main():
    if len(sys.argv) != 2:
        print("Uso: python ej02.py eventos.json")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, "r") as f:
            eventos = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{filename}'")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Archivo tiene formato JSON inválido")
        sys.exit(1)
    result = comprimir_eventos(eventos)
    print(format_json(result))

if __name__ == "__main__":
    main()