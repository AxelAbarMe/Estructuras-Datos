# Recursión

> Una función que se llama a si misma

## Partes de la recursión

* Caso Base
* Repetición

Hay problemas donde la recursividad es más natural para resolver algunos problemas específicos, donde en otros no sea tan buena.

### Ejemplo

Para resolver el caso de un laberinto, al moverse por este al encontrarse con una intersección, debe decidir el siguiente camino posible no visto. Las estructuras básicas cíclicas requieren mayor esfuerzo para poder resolver este problema, incluyendo hasta el uso de una pila.

El algoritmo recursivo permite para este caso, lograr devolverse en caso de un `dead point` o punto muerto, esto es llamado `backtracking` y permite tomar nuevas decisiones una vez el bloque de código encuentra un `dead point`

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

Caso Base debe definirse para evitar que la recursión sea infinita y si tenga fin.

CPU:
* RIP -> The program counter in x86, called RIP (EIP if 32-bit), points to the next instruction. For example, if the current instruction being executed is the one at 0x20B2, RIP would contain the value 0x20B4.
> The RIP register is a 64-bit instruction pointer in x86-64 processors. It stores the memory address of the next instruction the CPU will run.
* RSP -> Stack Pointer.
> En arquitectura de CPU x86-64, RSP (Register Stack Pointer) es el registro de 64 bits que funciona como el puntero de la pila. Su función principal es almacenar la dirección de memoria que apunta al elemento superior actual de la pila del sistema

En cada llamada de función se hace un push al stack. En la pila se guarda la dirección de retorno al hacer el push, es la dirección a la que el CPU debe dirigirse después de finalizar la llamada principal

Stack frame: En cada llamada de la función, se crea el stack frame y contiene la información necesaria para realizar las llamadas.

| Stack Frames | Stack
|:---:|:--:|
| Stack Frame | cuenta() - RET->0x400C - n=0 |
| Stack Frame | cuenta() - RET->0x400C - n=1 |
| Stack Frame | cuenta() - RET->0x400C - n=2 |
| Stack Frame | cuenta() - RET->0x400C - n=3 |
| Stack Frame | cuenta() - RET->0x400C - n=4 |
| Stack Frame | cuenta() - RET->0x4108 - n=5 |
| Stack Frame | main() - RET->0x4120 - X=5   |

> Nota: Aunque el valor en el stack frame donde se guarda cuenta(), si la variable local n se llamará x, está no afecta a la guardada en main() debido a que están en stack frames diferentes.

Cuando la pila, la función hace return, lo que pasa en la pila es que dicho stack frame ejecuta un pop(), devolviéndose a la dirección de memoria anterior. El top se encuentra en el RSP y se va actualizando en cada pop que se ejecuta en el stack.

Recursividad como un camino de ida y vuelta, se van ejecuntando los push y pop, lo que permite para el ejemplo del laberinto poder realizar push de una única dirección y pop cuando está no lleve a ningún lugar.

## Fallos de la recursividad

* Stack overflow: El Stack no es infinito, en caso de un absurdo llamadas push al stack, este puede llenarse y crear este fallo, además si la recursividad está mal planteada sin un caso base, está puede llamar absurdamente al stack hasta llenarlo.

# Recursión vs Iteración
Depende del problema, pero en términos generales se prefiere utilizar las versiones iterativas de un problema antes que los recursivos, debido a que tienen mejor rendimiento.
> Es preferible solo utilizar algoritmos recursivos cuando solucionar un problema cuando el código iterativo es difícil de plantear o resolver.

## Recursión de cola: 

Es una técnica aplicada por compiladores e intérpretes para manejar el código fuente recursivo y lo transforma en un código iterativo.
> La recursión de cola (tail recursion) ocurre cuando una función se llama a sí misma como su última instrucción, sin realizar ninguna operación posterior con ese resultado. Los compiladores aprovechan esto mediante la Optimización de Llamadas de Cola (TCO) para reutilizar el marco de pila actual, transformando la recursión en un ciclo eficiente

# Divide y vencerás Ejemplo

> Ejemplo de Sumatoria de 10

S10 -> 1+2+3+...+10 = 55

Si se observa, esto se puede traducir como 10 + S9, luego S9 como 9 + S8. Entonces se obtiene el patrón de Sn como n + Sn-1.

### Ejemplo codeado en python

```python
def sumatoria(n):
  if n==0
    return 0
  return n + sumatoria(n-1)
```

| Stack Frames | Stack
|:---:|:--:|
| Stack Frame | sum() - RET->0 - n=0   |
| Stack Frame | sum() - RET->1+( 0 ) - n=1   |
| Stack Frame | sum() - RET->2+( 1 ) - n=2   |
| Stack Frame | sum() - RET->3+( 2 ) - n=3   |
| Stack Frame | sum() - RET->4+( 3 ) - n=4   |
| Stack Frame | sum() - RET->5+( 4 ) - n=5   |

> Los resultados de RET son enviados una vez que el RSP llega al stack frame donde sum() tiene n=0, retornando entonces en bajada con cada pop, el valor faltante para el RET de cada stack frame para ir resolviendo el problema.

### Ejemplo factorial

```python
def factorial(n):
  if n<=1:
    return 1
  return n*factorial(n-1)
```

