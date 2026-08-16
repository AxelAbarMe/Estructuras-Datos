# Ejercicio 1: Puzzles con cadenas (strings)

Queremos resolver problemas simples con cadenas usando recursión. Implementaremos dos funciones:

1. Invertir una cadena (ejemplo: `"hola"` → `"aloh"`)
2. Verificar si una cadena es un palíndromo (ejemplo: `"oso"` → `True`, `"python"` → `False`)

## Instrucciones

1. Abre el archivo con el código inicial. Observa las funciones `reverse_string` e `is_palindrome`.
2. Ejecuta el código. No va a funcionar: implementen la lógica faltante.
3. Agrega mensajes de depuración (print) para ver qué ocurre en cada llamada recursiva, por ejemplo:

```python
print(f"reverse_string llamado con: {s}")
```

4. Modifica el caso base (hazlo mal a propósito) y observa qué pasa (¡recursión infinita!).
5. Prueba con varios casos: `""`, `"a"`, `"abba"`, `"abc"`.

## Pistas

* Caso base para invertir: cadena vacía (`""`).
* Caso base para palíndromo: cadena de longitud 0 o 1 → siempre es palíndromo.
* Paso recursivo: "quitar" un carácter y llamar a la función con el resto.

## Resultado esperado

Al terminar, deberías poder:

* Implementar ambas funciones correctamente.
* Explicar qué es un caso base y por qué detiene la recursión.
* Usar `print` para seguir la cadena de llamadas.
* Entender cómo el problema se va reduciendo paso a paso.

---

# Ejercicio 2: Explorador de laberintos (Maze Solver)

Tenemos un pequeño laberinto representado como una matriz. Comenzamos en `"S"` (start) y queremos llegar a `"E"` (exit). Usaremos recursión para explorar posibles caminos.

## Leyenda del laberinto

* `"S"` → inicio
* `"E"` → salida
* `" "` → espacio libre
* `"X"` → muro

## Instrucciones

1. Abre los archivos `maze.py` (definición del laberinto) y `solver.py` (función recursiva).
2. Ejecuta el programa. Debería imprimir una solución como:

```
Solución: [(0, 0), (1, 0), ..., (3, 3)]
```

3. Agrega `print(path)` dentro de la función recursiva para ver cómo explora el laberinto.
4. Modifica el laberinto:
   * Agrega muros extra.
   * Cambia la posición de la salida.
   * Observa cómo cambia el resultado.
5. Rompe el programa: elimina la verificación de "ya visitado" (la condición `if (x, y) in path`) y observa qué ocurre (¡recursión infinita!).
6. Desafío: en lugar de devolver solo la primera solución, modifica la función para devolver todas las posibles soluciones.

## Pistas

Piensen la recursión como:

> "Desde una celda, intento moverme en las 4 direcciones posibles. Si una de ellas llega a la salida, regreso el camino."

Casos base:

* Me salgo del laberinto o encuentro un muro → paro.
* Llego a la salida → éxito.
