class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """Inicializa un árbol binario de búsqueda vacío"""
        self.root = None

    def insert(self, data):
        """Inserta un nuevo valor en el árbol"""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Función auxiliar recursiva para insertar"""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        """Busca un valor en el árbol"""
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        """Función auxiliar recursiva para buscar"""
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

    def delete(self, data):
        """Elimina un valor del árbol"""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        """Función auxiliar recursiva para eliminar"""
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Nodo con un solo hijo o sin hijos
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Nodo con dos hijos
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)

        return node

    def _min_value_node(self, node):
        """Encuentra el nodo con el valor mínimo en un subárbol"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def clear(self):
        """Elimina todos los nodos del árbol"""
        self.root = None
