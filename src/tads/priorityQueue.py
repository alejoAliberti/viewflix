class Node:
    def _init_(self, content, priority):
        self.content = content
        self.priority = priority

class PriorityQueue:
    def _init_(self):
        self.queue = []
        
    def is_empty(self) -> bool:
        return len(self.queue) == 0
        
    def enqueue(self, content, priority) -> None:
        """Añade contenido a la cola con una prioridad específica"""
        node = Node(content, priority)
        self.queue.append(node)
        self._heapify_up(len(self.queue) - 1)
        
    def dequeue(self):
        """Retorna y elimina el elemento con mayor prioridad"""
        if self.is_empty():
            raise IndexError("Cola vacía")
            
        if len(self.queue) == 1:
            return self.queue.pop().content
            
        result = self.queue[0].content
        self.queue[0] = self.queue.pop()
        self._heapify_down(0)
        return result
        
    def peek(self):
        """Retorna el elemento con mayor prioridad sin eliminarlo"""
        if self.is_empty():
            raise IndexError("Cola vacía")
        return self.queue[0].content
        
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.queue[index].priority > self.queue[parent].priority:
            self.queue[index], self.queue[parent] = self.queue[parent], self.queue[index]
            self._heapify_up(parent)
            
    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if (left < len(self.queue) and 
            self.queue[left].priority > self.queue[largest].priority):
            largest = left
            
        if (right < len(self.queue) and 
            self.queue[right].priority > self.queue[largest].priority):
            largest = right
            
        if largest != index:
            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self._heapify_down(largest)