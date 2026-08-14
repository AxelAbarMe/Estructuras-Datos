# Ejercicio #1 - Borrar en una lista doblemente enlazada
# Basándose en el ejemplo de la lista doblemente enlazada realizada en 
# clase, agregue el método eliminar, que reciba por parámetro el valor 
# que se quiere eliminar de la lista. Si el valor existe, se elimina el nodo 
# de la lista. En caso contrario, se debe imprimir un mensaje de error

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

    def delete(self,value):
        current = self.head
        while current:
            if current.value == value:
                # Case 1: Primer nodo
                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev

                current.next = None
                current.prev = None
                return

            current = current.next
        print(f"Error: {value} no existe en la lista.")
                

    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            last = current
            current = current.next
        print("None")

    def display_backward(self):
        # Go to the last node
        current = self.head
        if current is None:
            print("None")
            return
        while current.next:
            current = current.next
        # Traverse backwards
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

# Example
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

dll.display_forward()
dll.delete(20)
dll.display_forward()   # 10 <-> 30 <-> None
dll.display_backward()  # 30 <-> 10 <-> None

dll.delete(10)
dll.display_forward()   # 30 <-> None

dll.delete(99)