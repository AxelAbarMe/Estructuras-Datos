# Instrucciones
Codifique el programa en Python para cada uno de los siguientes enunciados.

---

## Ejercicio #1 - Borrar en una lista doblemente enlazada
Basándose en el ejemplo de la lista doblemente enlazada realizada en clase, agregue el método `eliminar`, que reciba por parámetro el valor que se quiere eliminar de la lista. Si el valor existe, se elimina el nodo de la lista. En caso contrario, se debe imprimir un mensaje de error.

---

## Ejercicio #2 - Compresión de agenda de eventos
Durante un festival, se registran pequeños eventos en distintas salas. Debe unificar eventos consecutivos de una misma sala cuando el segundo empieza exactamente cuando termina el primero. Se debe preservar el orden relativo del resto de eventos.

El programa recibirá por línea de comandos el nombre de un archivo `.json`. El archivo contiene un array de objetos con:
* `"inicio"`: string en formato `"HH:MM"`
* `"duracion"`: entero en minutos
* `"sala"`: string (ID de sala)

### Ejemplo `eventos.json`:
```json
[
  { "inicio": "09:00", "duracion": 60, "sala": "A" },
  { "inicio": "10:00", "duracion": 30, "sala": "A" },
  { "inicio": "10:30", "duracion": 45, "sala": "B" },
  { "inicio": "10:30", "duracion": 30, "sala": "A" },
  { "inicio": "11:00", "duracion": 30, "sala": "A" }
]
```

### Salida
Un array JSON con los eventos resultantes, preservando orden relativo.

**Salida esperada para el ejemplo:**
```json
[
  { "inicio": "09:00", "duracion": 90, "sala": "A" },
  { "inicio": "10:30", "duracion": 45, "sala": "B" },
  { "inicio": "10:30", "duracion": 60, "sala": "A" }
]
```

### Consideraciones
* Solo se fusionan eventos adyacentes dentro de la misma sala si `inicio_siguiente == fin_anterior`.
* No reordenen la lista.
* Utilicen la o las estructuras de datos lineales que deseen para resolver el problema.
* El nombre del archivo json se recibe como parámetro al programa.

---

## Ejercicio #3 - Línea de comedor con reglas especiales
En una cafetería futurista, llega una secuencia de personas con una etiqueta:
* **VIP:** se inserta delante del primer NO-VIP en la fila (por tanto, antes de NORM y BULK).
* **BULK:** siempre se coloca al final absoluto de la fila; los BULK forman un bloque final.
* **NORM:** se coloca al final de la zona NO-BULK, es decir, justo antes del primer BULK si ya hay alguno.

Escriba un programa que procese todas las llegadas y retorne el orden final de servicio.

### Consideraciones
* Utilicen la o las estructuras de datos lineales que deseen para resolver el problema.
* El nombre del archivo json se recibe como parámetro al programa.

### Ejemplo `comedor.json`:
```json
[
  { "tipo": "NORM", "nombre": "Alice" },
  { "tipo": "VIP",  "nombre": "Bob" },
  { "tipo": "NORM", "nombre": "Charlie" },
  { "tipo": "BULK", "nombre": "Dave" },
  { "tipo": "VIP",  "nombre": "Eve" }
]
```

### Salida del programa
La salida del programa de acuerdo con el `.json` de ejemplo sería:
`Bob Eve Alice Charlie Dave`

*(Porque cada VIP se inserta delante del primer no-VIP; BULK siempre termina al final.)*

---

## Ejercicio #4 - Dron de reparto con retorno exacto
Un dron repartidor ejecuta las instrucciones dadas desde un archivo. Cuando encuentra `RETURN`, debe desandar exactamente el camino recorrido, en orden inverso, hasta volver al punto de partida. Su tarea consiste en imprimir en pantalla la secuencia de acciones del retorno (las inversas de los movimientos y giros realizados antes del `RETURN`).

### Modelo de instrucciones al dron:
* `{"cmd": "MOVE", "x": <entero_metros>}`
* `{"cmd": "TURN_LEFT"}`
* `{"cmd": "TURN_RIGHT"}`
* `{"cmd": "DROP"}` *(no afecta a la posición; se ignora durante el retorno)*
* `{"cmd": "RETURN"}` *(al leerla, se deben generar/emitir las acciones inversas hasta regresar al inicio)*

### Consideraciones
* Utilicen la o las estructuras de datos lineales que deseen para resolver el problema.
* El nombre del archivo json se recibe como parámetro al programa.

### Reglas de inversión
* Inversa de `MOVE x` → `"MOVE_BACK"`
* Inversa de `TURN_LEFT` → `TURN_RIGHT`
* Inversa de `TURN_RIGHT` → `TURN_LEFT`
* `DROP` no genera acción inversa.
* `RETURN` no se imprime, solo desencadena el retorno.

### Ejemplo `dron.json`:
```json
[
  { "cmd": "MOVE", "x": 100 },
  { "cmd": "TURN_RIGHT" },
  { "cmd": "MOVE", "x": 50 },
  { "cmd": "DROP" },
  { "cmd": "MOVE", "x": 30 },
  { "cmd": "TURN_LEFT" },
  { "cmd": "MOVE", "x": 20 },
  { "cmd": "DROP" },
  { "cmd": "RETURN" }
]
```

### Salida del programa
La salida del programa basado en el ejemplo anterior sería:
```text
MOVE_BACK x 20
TURN_RIGHT
MOVE_BACK x 30
MOVE_BACK x 50
TURN_LEFT
MOVE_BACK x 100
```
