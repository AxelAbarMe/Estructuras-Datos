# 6: Listas Doblemente Enlazadas, Colas y Pilas (Implementación)

## Listas Doblemente Enlazadas

Al igual que una lista enlazada simple, funciona por Nodos y referencias al siguiente Nodo.

Movimiento de nodo temporal a través de la lista en Python:

```python
while tmp is not none:
  tmp = tmp.next
```

Con dicha implementación de una lista simple, no se puede devolver hacia atrás; se debe empezar desde el inicio cada vez que se requiera.

Para esto, se debe modificar la estructura del Nodo para poder implementarlo:

| prev Apunta a | Nodo (Datos) | next Apunta a | prev Apunta a | Nodo (Datos) | next Apunta a | prev Apunta a | Nodo (Datos) | next Apunta a |
|:--:|:--:|:---:|:--:|:---:|:--:|:---:|:--:|:---:|
| ← Null | prev ! data ! next | → Next | ← prev | prev ! data ! next | → Next | ← prev | prev ! data ! next | → Null |

```python
class Nodo:
  self.value
  self.prev
  self.next
```

Estas listas otorgan la ventaja de poder recorrer la lista hacia atrás y hacia adelante.

> Un ejemplo es el carrusel en páginas web, donde se tiene un `< [ ] >`; para regresar o avanzar se utiliza esta lista doblemente enlazada. Si se utiliza una lista simple, el `tmp` debe recorrer toda la lista de nuevo para poder regresar en dicho carrusel.

### Overhead

`Overhead` es la memoria adicional que se debe consumir para realizar alguna implementación; la lista enlazada no funciona sin dichos punteros, pero estos punteros no son los datos en sí.

> Esto afecta debido a que, si se toma el valor del overhead como 4 bytes cada uno, al tener 2 overheads (prev y next) se transforma en 8 bytes por nodo; si se tiene una lista de 100.000 nodos, significa que se estaría consumiendo en memoria un tamaño de 800.000 bytes, o aproximadamente 800K.

Esto toma efecto cuando se debe implementar este tipo de estructuras en hardware más limitado, como una cámara con 2MB de RAM y 2GB de disco.

### Ejemplo de implementación en Python

```python
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None  # Points to next node
        self.prev = None  # Points to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = DoubleNode(value)
        if self.head is None:  # Empty list
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
```

---

## Colas

> La cola es un TDA de tipo **FIFO** (First in First Out).

Lo que diferencia a una cola de una lista enlazada son sus operaciones:

* Enqueue (Insertar)
* Dequeue (Remover al siguiente)

### Implementaciones

* Vector
* Listas

Se pueden implementar de varias formas; utilizar una lista doblemente enlazada para el caso de una cola es malgastar los recursos de memoria, ya que por naturaleza una cola nunca va a regresar de manera manual hacia sus elementos, solo se puede observar el primero (el *head*). Por esto, se puede concluir que la mejor opción es una lista simple, para no crear un overhead que gaste memoria adicional para algo que no tendrá funcionalidad en este caso.

### Ejemplo de implementación en Python

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to next node
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # Empty queue
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:  # Queue became empty
            self.rear = None
        return value
```

---

## Pila (Stack)

> La pila es un TDA de tipo **LIFO** (Last in First Out).

### Operaciones de la pila

* `push()` → Inserta
* `pop()` → Saca el valor de arriba y lo devuelve
* `peek()` → Retorna el último elemento (`Top()`)

### Implementaciones

* Vector
* Listas

Como se ha destacado en ambas, tanto colas como pilas se pueden implementar de diversas formas, pero los vectores y listas son una forma común de hacerlas.

> Un ejemplo es una pila de libros: a como se vayan acumulando, el puntero `top` va cambiando su valor al libro que esté en la posición más alta, según se vayan insertando utilizando `push()` o `pop()`.

### Ejemplo de implementación en Python

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to next node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        return None if self.top is None else self.top.value
```

---

## Conclusiones

Lo importante realmente es saber cuándo utilizar cuál, no cómo implementarlas, porque ya existen librerías como `queue`, que ya realiza la implementación de una cola estándar, o `LifoQueue` dentro de `queue`, que lo realiza para el caso de una pila en Python.

> **Nota adicional:** en Python, `collections.deque` es la implementación recomendada tanto para pilas como para colas eficientes, ya que internamente evita el costo de desplazar elementos que sí tiene una lista normal (`list`) al insertar o eliminar por el inicio.
