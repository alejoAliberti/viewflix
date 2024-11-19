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
        
    def find_node(self, data: Any = None, node: Node = None) -> Node:
        """
        Busca un nodo por su dato o nombre
        Args:
            data: El dato a buscar (opcional)
            node: El nodo desde donde comenzar la búsqueda
        Returns:
            Node: El nodo encontrado o None si no existe
        """

        if node is None:
            node = self.root
            if node is None:
                return None
                
        if data is not None and node.data == data:
            return node
            
        for child in node.children:
            result = self.find_node(data, child)
            if result is not None:
                return result
            
        return None
        
    def find_nodes_by_name(self, name: str, node: Node = None, results: list = None) -> list:
        """
        Busca nodos cuyo atributo `name` coincida parcialmente con el valor proporcionado.
        Args:
            name: Subcadena para buscar dentro del nombre de los nodos.
            node: Nodo desde donde comenzar la búsqueda (opcional).
            results: Lista acumulativa de nodos coincidentes.
        Returns:
            list: Lista de nodos coincidentes.
        """
        # Inicialización de parámetros en la primera llamada
        if node is None:
            node = self.root
            results = []

        # Caso base: Si el nodo es None, retornamos los resultados acumulados
        if node is None:
            return results

        # Verificar si el atributo `name` contiene la subcadena buscada
        if name in str(getattr(node, 'name', "")):
            results.append(node)

        # Llamar recursivamente para todos los hijos del nodo actual
        for child in node.children:
            self.find_nodes_by_name(name, child, results)

        return results


    def clear(self) -> None:
        """Elimina todos los nodos del árbol"""
        self.root = None

    def dfs_traverse(self, node: Node = None):
        """
        Recorre el árbol en profundidad (Depth-First Search)
        Yields cada nodo en el recorrido
        """
        if node is None:
            node = self.root
            if node is None:
                return

        yield node  # Primero visitamos el nodo actual
        
        for child in node.children:
            yield from self.dfs_traverse(child)  # Recursivamente visitamos los hijos
            
    def bfs_traverse(self):
        """
        Recorre el árbol en anchura (Breadth-First Search)
        Yields cada nodo en el recorrido
        """
        if self.root is None:
            return
            
        cola = [self.root]
        while cola:
            node = cola.pop(0)
            yield node
            cola.extend(node.children)
    
    def bfs_traverse_with_depth(self, max_depth: int = 1):
        """
        Recorre el árbol en anchura hasta una profundidad máxima
        Args:
            max_depth: Profundidad máxima del recorrido (0 es solo la raíz, 1 incluye los hijos directos)
        Yields cada nodo en el recorrido
        """
        if self.root is None:
            return
            
        # Cola con tuplas de (nodo, nivel)
        cola = [(self.root, 0)]
        
        while cola:
            node, nivel = cola.pop(0)
            
            if nivel > max_depth:
                break
                
            yield node
            
            if nivel < max_depth:
                for child in node.children:
                    cola.append((child, nivel + 1))
