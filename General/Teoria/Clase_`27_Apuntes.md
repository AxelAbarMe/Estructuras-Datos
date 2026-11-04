# Backtracking

* Fuerza bruta para explorar toda una aplicación, funcionalidades, etc.

Complejidad algoritmica de este tipo de problemas es excesivamente costosos, hay una penalidad considerable.

Para el ejemplo de adivinar con fuerza bruta contraseñas de n digitos con todos los Key Space (a-z, A-Z, 0-9), llega a ser n^64 posibilidades.

* Gestor de contraseñas: (Roboform, NodePass, 1Password)

_  _  _ 

['a','b','c']

Explorar permutaciones posibles y encontrar la solución (push-pop), se crea un árbol para cada caso posible todo conectado a un [Empty] Nodo y de ahi en ese caso, difieren 3 hijos (A), (B), (C).

Decision-Tree  -  Greedy

```python

def backtracking(empty):
  if len(empty)==n:
    result.append("".join(empty))      //Agregar solucion
    return result
  for char in ["a","b","c"]:
    empty.append(char)                 //Buscar opciones
    backtracking(empty)
    pop()
```

* Busca las opciones
* Las guarda
* Pop para probar otra opción

## Problema N-Queen

NxN -> Board

N Queens sin que se ataque entre ellas (Ejemplo matriz 4x4) [01,13,20,32] Pos
