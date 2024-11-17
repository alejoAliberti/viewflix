
from typing import List, Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.children: List[Node] = []

class GeneralTree:
    def __init__(self):
        """Inicializa un árbol general vacío"""
        self.root = None
    
    def is_empty(self) -> bool:
        """Verifica si el árbol está vacío"""
        return self.root is None
        
    def add_root(self, data: Any) -> None:
        """Añade la raíz al árbol si está vacío"""
        if self.root is None:
            self.root = Node(data)
        else:
            raise ValueError("El árbol ya tiene una raíz")
            
    def add_child(self, parent: Node, data: Any) -> None:
        """Añade un hijo al nodo padre especificado"""
        if parent is None:
            raise ValueError("El nodo padre no puede ser None")
        new_node = Node(data)
        parent.children.append(new_node)
        
    def find_node(self, data: Any, node: Node = None) -> Node:
        """
        Busca un nodo con el dato especificado
        Retorna None si no lo encuentra
        """
        if node is None:
            node = self.root
            if node is None:
                return None
                
        if node.data == data:
            return node
            
        for child in node.children:
            result = self.find_node(data, child)
            if result is not None:
                return result
                
        return None
        
    def clear(self) -> None:
        """Elimina todos los nodos del árbol"""
        self.root = None
