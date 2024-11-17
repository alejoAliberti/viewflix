from typing import TypeVar, Generic, List


class Stack:
    def __init__(self):
        """Inicializa una pila vacía"""
        self.items = []

    def push(self, item) -> None:
        """Añade un elemento al tope de la pila"""
        self.items.append(item)

    def pop(self):
        """
        Remueve y retorna el elemento del tope de la pila
        Lanza IndexError si la pila está vacía
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Retorna el elemento del tope sin removerlo
        Lanza IndexError si la pila está vacía
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self) -> bool:
        """Retorna True si la pila está vacía, False en caso contrario"""
        return len(self.items) == 0

    def size(self) -> int:
        """Retorna el número de elementos en la pila"""
        return len(self.items)

    def clear(self) -> None:
        """Elimina todos los elementos de la pila"""
        self.items.clear()
