class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self) -> bool:
        """Verifica si la lista está vacía"""
        return self.head is None
    
    def append(self, data) -> None:
        """Añade un elemento al final de la lista"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data) -> None:
        """Añade un elemento al inicio de la lista"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, data) -> bool:
        """Elimina la primera ocurrencia del elemento dado"""
        if self.head is None:
            return False
            
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
            
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def get_size(self) -> int:
        """Retorna el tamaño de la lista"""
        return self.size
    
    def search(self, data=None, name=None, node=None) -> bool:
            """
            Busca un elemento en la lista de manera recursiva.
            - `data`: El dato a buscar.
            - `name`: Un atributo opcional que también puede usarse como criterio de búsqueda.
            """
            # Si es la primera llamada, comienza desde la cabeza
            if node is None:
                node = self.head

            # Caso base: Si el nodo es None, hemos llegado al final
            if node is None:
                return False

            # Verifica si el nodo actual cumple con la búsqueda. Ademas aplicamos una busqueda parcial por nombre.
            if data is not None and node.data == data:
                return True

            # Llama recursivamente con el siguiente nodo
            return self.search(data, name, node.next)
    
    def search_by_name(self, name: str, node=None, results=None) -> list:
        """
        Busca nodos cuyo atributo `name` coincida parcialmente con el valor proporcionado.
        Retorna una lista de nodos coincidentes.
        """
        # Inicialización de parámetros en la primera llamada
        if node is None:
            node = self.head
            results = []

        # Caso base: Si llegamos al final de la lista, retornamos los resultados
        if node is None:
            return results

        # Verificar si el atributo `name` contiene la subcadena buscada
        if name in str(getattr(node, 'name', "")):
            results.append(node)

        # Llamada recursiva al siguiente nodo
        return self.search_by_name(name, node.next, results)

        
    def clear(self) -> None:
        """Elimina todos los elementos de la lista"""
        self.head = None
        self.size = 0
    
    def get_all(self) -> list:
        """Retorna todos los elementos en una lista de Python"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
