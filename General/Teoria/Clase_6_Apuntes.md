# Listas Doblemente Enlazadas

Al igual que una lista enlazada simple, que funciona por Nodos y referencias al siguiente Nodo.

Movimiento de nodo temporal a través de la lista en Python:
```python
while tmp is not none:
  tmp = tmp.next
``` 
Con dicha implementación de una lista simple, no se puede devolver hacia atrás, se debe de empezar desde el inicio cada vez que se requiera.

Para esto entonces se debe de modificar la estructura del Nodo para poder implementar esto:

|prev Apunta a| Nodo (Datos) |next Apunta a|prev Apunta a|Nodo (Datos)|next Apunta a|prev Apunta a|Nodo (Datos)|next Apunta a|
|:--:|:--:|:---:|:--:|:---:|:--:|:---:|:--:|:---:|
|<-Null| prev ! data ! next |->Next|<-prev| prev ! data ! next |->Next|<-prev| prev ! data ! next |->Null|


```python
class Nodo:
  self.value
  self.prev
  self.next
```

Estas listas otorgan la ventaja de poder recorrer la lista hacia atrás y hacia adelante.

> Un ejemplo es el carrusel en páginas web donde se tenga un < [ ] > y para regresar o avanzar, se utiliza está lista doblemente enlazada, si se utiliza una simple el tmp debe recorrer toda la lista de nuevo para poder regresar en dicho carrusel.

`Overhead` es para cuando se debe de realizar alguna implementación, la lista enlazada no funciona sin dichos punteros, pero estos punteros no son los datos. Dichos overhead se transforman en memoria adicional que se debe de consumir.

> Esto afecta debido a que si se toma el valor de los overhead como 4 Bytes cada uno, al tener 2 overhead se transforma en 8 Bytes por nodo y si se tiene una lista de 100.000 nodos, significa que se estaría consumiendo en memoria un tamaño de 800.800 Bytes o aproximadamente 800k.

Esto toma efecto cuando se debe de implementar este tipo de estructuras en hardware más limitado como una cámara con 2MB de RAM y 2GB de disco.

## Ejemplo Implementación Python

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

# Colas

> La cola es un TDA de tipo `FIFO` (First in First Out).

Lo que diferencia a una cola de una lista enlazada son sus operaciones.

* Enqueue (Insertar)
* Dequeue (Remover al siguiente)

## Implementaciones

* Vector
* Listas

Se pueden implementar de varias formas, utilizar una lista doblemente enlazada para el caso de cola es malgastar los recursos de memoria ya que por naturaleza, una cola nunca va a regresar de manera manual hacia sus elementos, solo se puede observar al primero o el head. Por esto, se puede concluir que la mejor opción es una lista simple para no crear un Overhead que gasta memoria adicional para algo que no tendrá funcionalidad para este caso.

## Ejemplo Implementación Python

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

# Pila (Stack)

> La pila es un TDA de tipo `LIFO` (Last in First Out).

Operaciones de la pila:

* push() -> Inserta
* pop() -> Saca el valor de arriba y lo devuelve
* peek() Retorna el último elemeto (`Top()`)

## Implementaciones

* Vector
* Listas

Como se ha destacado en ambas, tantos colas como pilas, se pueden implementar de diversas formas, pero los vectores y listas son una forma de hacerlas.

> Un ejemplo es que una pila de libros, a como se vayan acumulando el puntero top va cambiando su valor al libro que este en la posición más alta, según se vayan insertando utilizando push() o pop().

## Ejemplo Implementación Python

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

# Conclusiones

Lo importante realmente es saber cuando utilizar cuál, no como implementarlas, porque ya existen librerías como `queue` que ya realizan la implementación de una cola estándar o `LifoQueue` dentro de `queue` que lo realiza para el caso de una pila en Python.
