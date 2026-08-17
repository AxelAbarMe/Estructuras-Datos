# 7: Recursión

> Una función que se llama a sí misma.

## Partes de la recursión

* Caso Base
* Repetición

Hay problemas donde la recursividad es más natural para resolver, mientras que en otros no es tan buena.

### Ejemplo: el laberinto

Para resolver el caso de un laberinto, al moverse por este y encontrarse con una intersección, se debe decidir el siguiente camino posible no visto. Las estructuras básicas cíclicas requieren mayor esfuerzo para poder resolver este problema, incluyendo hasta el uso de una pila.

El algoritmo recursivo permite, para este caso, lograr devolverse en caso de un *dead point* o punto muerto; esto se llama **backtracking** y permite tomar nuevas decisiones una vez que el bloque de código encuentra un *dead point*.

### Ejemplo de código

```python
def cuenta(n):       # 0x4000
  if n==0:           # 0x4004   }  Caso
    return           # 0x4008   }  Base
  cuenta(n-1)        # 0x400C   } -v
  print(n)           # 0x4010   }  Repetición

def main():          # 0x4100
  x=5                # 0x4104
  cuenta(x)          # 0x4108

main()               # 0x4120
```

El caso base debe definirse para evitar que la recursión sea infinita y sí tenga fin.

### Registros del CPU relevantes

* **RIP** → *The program counter* en x86, llamado RIP (EIP si es 32-bit), apunta a la siguiente instrucción. Por ejemplo, si la instrucción actual que se ejecuta es la de `0x20B2`, RIP contendría el valor `0x20B4`.
  > El registro RIP es un puntero de instrucción de 64 bits en procesadores x86-64. Almacena la dirección de memoria de la siguiente instrucción que el CPU ejecutará.
* **RSP** → *Stack Pointer*.
  > En arquitectura de CPU x86-64, RSP (Register Stack Pointer) es el registro de 64 bits que funciona como el puntero de la pila. Su función principal es almacenar la dirección de memoria que apunta al elemento superior actual de la pila del sistema.

En cada llamada de función se hace un `push` al stack. En la pila se guarda la dirección de retorno al hacer el `push`; es la dirección a la que el CPU debe dirigirse después de finalizar la llamada.

**Stack frame:** en cada llamada de la función, se crea el stack frame, que contiene la información necesaria para realizar las llamadas.

| Stack Frames | Stack |
|:---:|:--:|
| Stack Frame | `cuenta()` - RET->0x400C - n=0 |
| Stack Frame | `cuenta()` - RET->0x400C - n=1 |
| Stack Frame | `cuenta()` - RET->0x400C - n=2 |
| Stack Frame | `cuenta()` - RET->0x400C - n=3 |
| Stack Frame | `cuenta()` - RET->0x400C - n=4 |
| Stack Frame | `cuenta()` - RET->0x4108 - n=5 |
| Stack Frame | `main()` - RET->0x4120 - X=5 |

> **Nota:** aunque en el stack frame donde se guarda `cuenta()` la variable local se llamara `n` en vez de `x`, esto no afecta a la variable guardada en `main()`, debido a que están en stack frames diferentes.

Cuando la función hace `return`, lo que pasa en la pila es que dicho stack frame ejecuta un `pop()`, devolviéndose a la dirección de memoria anterior. El *top* se encuentra en el RSP y se va actualizando en cada `pop` que se ejecuta en el stack.

La recursividad puede pensarse como un camino de ida y vuelta: se van ejecutando los `push` y `pop`, lo que permite, para el ejemplo del laberinto, realizar `push` de una única dirección y `pop` cuando esta no lleve a ningún lugar.

## Fallos de la recursividad

* **Stack overflow:** el stack no es infinito; en caso de una cantidad absurda de llamadas `push` al stack, este puede llenarse y crear este fallo. Además, si la recursividad está mal planteada sin un caso base, esta puede llamar absurdamente al stack hasta llenarlo.

---

## Recursión vs. Iteración

Depende del problema, pero en términos generales se prefiere utilizar las versiones iterativas de un problema antes que las recursivas, debido a que tienen mejor rendimiento.

> Es preferible utilizar algoritmos recursivos solo cuando resolver el problema de forma iterativa es difícil de plantear o resolver.

### Recursión de cola

Es una técnica aplicada por compiladores e intérpretes para manejar el código fuente recursivo y transformarlo en código iterativo.

> La recursión de cola (*tail recursion*) ocurre cuando una función se llama a sí misma como su última instrucción, sin realizar ninguna operación posterior con ese resultado. Los compiladores aprovechan esto mediante la Optimización de Llamadas de Cola (TCO) para reutilizar el marco de pila actual, transformando la recursión en un ciclo eficiente.

> **Nota adicional:** Python, a diferencia de lenguajes como Scheme o algunos compiladores de C, **no** implementa TCO de forma nativa; por lo tanto, una función recursiva de cola en Python sigue consumiendo un stack frame por cada llamada, y puede llegar a un `RecursionError` si la entrada es muy grande.

---

## Divide y Vencerás — Ejemplo

> Ejemplo de sumatoria de 10

`S10 -> 1+2+3+...+10 = 55`

Si se observa, esto se puede traducir como `10 + S9`, luego `S9` como `9 + S8`. Entonces se obtiene el patrón de `Sn` como `n + Sn-1`.

### Ejemplo codeado en Python

```python
def sumatoria(n):
  if n==0:
    return 0
  return n + sumatoria(n-1)
```

| Stack Frames | Stack |
|:---:|:--:|
| Stack Frame | `sum()` - RET->0 - n=0 |
| Stack Frame | `sum()` - RET->1+( 0 ) - n=1 |
| Stack Frame | `sum()` - RET->2+( 1 ) - n=2 |
| Stack Frame | `sum()` - RET->3+( 2 ) - n=3 |
| Stack Frame | `sum()` - RET->4+( 3 ) - n=4 |
| Stack Frame | `sum()` - RET->5+( 4 ) - n=5 |

> Los resultados de RET se envían una vez que el RSP llega al stack frame donde `sum()` tiene `n=0`, retornando entonces en bajada, con cada `pop`, el valor faltante para el RET de cada stack frame, hasta ir resolviendo el problema.

### Ejemplo: factorial

```python
def factorial(n):
  if n<=1:
    return 1
  return n*factorial(n-1)
```
