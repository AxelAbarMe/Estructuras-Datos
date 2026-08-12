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

CPU
* RIP -> 
* RSP -> Stack Pointer

En cada llamada de función se hace un push al stack

En la pila se guarda la dirección de retorno al hacer el push, es la dirección a la que el CPU debe dirigirse después de finalizar la llamada principal

Stack frame: En cada llamada de la función, se crea el stack frame y contiene la información necesaria para realizar las llamadas.

| Stack Frames | Stack
|:---:|:--:|
| Stack Frame | cuenta() - RET->0x400C - n=1 |
| Stack Frame | cuenta() - RET->0x400C - n=2 |
| Stack Frame | cuenta() - RET->0x400C - n=3 |
| Stack Frame | cuenta() - RET->0x400C - n=4 |
| Stack Frame | cuenta() - RET->0x4108 - n=5 |
| Stack Frame | main() - RET->0x4120 - X=5 |

> Nota: Aunque el valor en el stack frame donde se guarda cuenta(), si la variable local n se llamará x, está no afecta a la guardada en main() debido a que están en stack frames diferentes.




