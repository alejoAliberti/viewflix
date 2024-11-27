class Node:
    def __init__(self, content, priority):
        self.content = content
        self.priority = priority

class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def is_empty(self) -> bool:
        return len(self.heap) == 0
        
    def insert(self, content, priority):
        """Añade contenido al heap con una prioridad específica"""
        node = Node(content, priority)
        self.heap.append(node)
        self._sift_up(len(self.heap) - 1)
        
    def extract_max(self):
        """Retorna y elimina el elemento con mayor prioridad"""
        if self.is_empty():
            raise IndexError("Heap vacío")
            
        if len(self.heap) == 1:
            return self.heap.pop().content
            
        result = self.heap[0].content
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return result
        
    def get_max(self):
        """Retorna el elemento con mayor prioridad sin eliminarlo"""
        if self.is_empty():
            raise IndexError("Heap vacío")
        return self.heap[0].content
        
    def _sift_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)
            
    def _sift_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if (left < len(self.heap) and 
            self.heap[left].priority > self.heap[largest].priority):
            largest = left
            
        if (right < len(self.heap) and 
            self.heap[right].priority > self.heap[largest].priority):
            largest = right
            
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)