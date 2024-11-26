from interfaces.media import MediaContent

class Edge:
    def __init__(self, dest, weight=1.0):
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self):
        self.vertices = {}  # Diccionario de {contenido: [aristas]}
        self.dependencies = {}  # Diccionario para almacenar dependencias de contenido
        
    def add_vertex(self, content):
        """Añade un vértice (película o serie) al grafo"""
        if content not in self.vertices:
            self.vertices[content] = []
            
    def add_edge(self, content1, content2, similarity=1.0):
        """Añade una arista entre dos contenidos con un peso de similitud"""
        self.add_vertex(content1)
        self.add_vertex(content2)
        
        # Añade aristas en ambas direcciones (grafo no dirigido)
        self.vertices[content1].append(Edge(content2, similarity))
        self.vertices[content2].append(Edge(content1, similarity))
        
    def calculate_similarity(self, content1, content2):
        """Calcula la similitud entre dos contenidos"""
        similarity = 0.0
    
        # Similitud por género (0.4)
        if content1.category == content2.category:
            similarity += 0.4
        
        # Similitud por rating (0.3)
        if hasattr(content1, 'rating') and hasattr(content2, 'rating'):
            rating_diff = abs(content1.rating - content2.rating)
            if rating_diff <= 1:
                similarity += 0.3
    
        # Similitud por reparto (0.3)
        if hasattr(content1, 'cast') and hasattr(content2, 'cast'):
            # Convertimos las listas en conjuntos para usar intersección
            cast1 = set(content1.cast)
            cast2 = set(content2.cast)

            # Calculamos actores en común
            common_cast = cast1.intersection(cast2)
            
            # Si hay actores en común, añadimos peso proporcional
            if common_cast:
                # Máximo 0.3 si comparten 3 o más actores
                cast_similarity = min(len(common_cast) * 0.1, 0.3)
                similarity += cast_similarity
        
        return similarity
        
    def get_recommendations(self, content, limit=5):
        """Obtiene recomendaciones basadas en un contenido"""
        if content not in self.vertices:
            return []
            
        # Obtiene todos los vecinos y sus pesos
        recommendations = []
        for edge in self.vertices[content]:
            recommendations.append((edge.dest, edge.weight))
            
        # Ordena por peso de similitud y retorna los top N
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:limit]
    
    def get_recommendations_dfs(self, content, limit=5, min_similarity=0.3):
        """Obtiene recomendaciones usando DFS para explorar en profundidad contenidos similares"""
        if content not in self.vertices:
            return []
            
        visited = set()
        recommendations = []
        
        def dfs_helper(current_content, depth=0, max_depth=3):
            if depth >= max_depth or len(recommendations) >= limit:
                return
                
            visited.add(current_content)
            
            # Obtiene los vecinos ordenados por peso de similitud
            neighbors = [(edge.dest, edge.weight) for edge in self.vertices[current_content]]
            neighbors.sort(key=lambda x: x[1], reverse=True)
            
            for neighbor, similarity in neighbors:
                if neighbor not in visited and similarity >= min_similarity:
                    recommendations.append((neighbor, similarity))
                    dfs_helper(neighbor, depth + 1)
                    
        dfs_helper(content)
        return recommendations[:limit]
    
    def get_recommendations_bfs(self, content, limit=5, min_similarity=0.3):
        """Obtiene recomendaciones usando BFS para explorar contenidos similares por niveles"""
        if content not in self.vertices:
            return []
            
        visited = set([content])
        queue = [(content, 0)]  # (contenido, nivel)
        recommendations = []
        
        while queue and len(recommendations) < limit:
            current_content, level = queue.pop(0)
            
            # Obtiene los vecinos ordenados por peso de similitud
            neighbors = [(edge.dest, edge.weight) for edge in self.vertices[current_content]]
            neighbors.sort(key=lambda x: x[1], reverse=True)
            
            for neighbor, similarity in neighbors:
                if neighbor not in visited and similarity >= min_similarity:
                    visited.add(neighbor)
                    recommendations.append((neighbor, similarity))
                    queue.append((neighbor, level + 1))
                    
        return recommendations[:limit]
    
    def add_dependency(self, content_before, content_after):
        """Añade una dependencia entre dos contenidos (content_before debe estar disponible antes que content_after)"""
        if content_before not in self.dependencies:
            self.dependencies[content_before] = []
        self.dependencies[content_before].append(content_after)
        
    def get_content_order(self):
        """Realiza ordenamiento topológico para obtener el orden de visualización del contenido"""
        # Inicializar el grado de entrada para cada vértice
        in_degree = {content: 0 for content in self.vertices}
        for content in self.dependencies:
            for dependent in self.dependencies[content]:
                in_degree[dependent] = in_degree.get(dependent, 0) + 1
        
        # Cola para vértices con grado de entrada 0
        queue = [content for content in in_degree if in_degree[content] == 0]
        result = []
        
        while queue:
            current = queue.pop(0)
            result.append(current)
            
            # Reducir grado de entrada de los dependientes
            if current in self.dependencies:
                for dependent in self.dependencies[current]:
                    in_degree[dependent] -= 1
                    if in_degree[dependent] == 0:
                        queue.append(dependent)
        
        # Verificar si hay ciclos
        if len(result) != len(self.vertices):
            raise ValueError("El grafo contiene ciclos, no es posible establecer un orden válido")
            
        return result
    
    def find_optimal_viewing_sequence(self, user, available_time: int) -> List[MediaContent]:
        """
        Implementa el algoritmo de Dijkstra para encontrar la secuencia óptima de visualización
        que maximiza la satisfacción del usuario basado en sus preferencias y tiempo disponible.
        """
        # Inicializar distancias y caminos
        distances = {content: float('inf') for content in self.vertices}
        previous = {content: None for content in self.vertices}
        visited = set()
        
        # Crear cola de prioridad con todos los contenidos
        pq = []
        
        # Calcular satisfacción inicial para cada contenido basado en preferencias
        for content in self.vertices:
            satisfaction = sum(2 if content.category in pref else 0 
                            for pref in user.preferences)
            if satisfaction > 0:  # Solo considerar contenido que coincida con preferencias
                distances[content] = -satisfaction  # Negativo porque queremos maximizar
                pq.append((distances[content], content))
        
        # Ordenar cola de prioridad
        pq.sort()
        
        total_time = 0
        sequence = []
        
        while pq and total_time < available_time:
            current_dist, current_content = pq.pop(0)
            
            if current_content in visited:
                continue
                    
            # Verificar si añadir este contenido excede el tiempo disponible
            if total_time + current_content.duration > available_time:
                continue
                    
            visited.add(current_content)
            sequence.append(current_content)
            total_time += current_content.duration
            
            # Explorar vecinos
            for edge in self.vertices[current_content]:
                neighbor = edge.dest
                if neighbor in visited:
                    continue
                        
                # Calcular nueva satisfacción considerando similitud
                satisfaction = sum(2 if neighbor.category in pref  else 0 
                                for pref in user.preferences)
                new_satisfaction = -current_dist + (satisfaction * edge.weight)
                
                if -new_satisfaction < distances[neighbor]:
                    distances[neighbor] = -new_satisfaction
                    previous[neighbor] = current_content
                    pq.append((-new_satisfaction, neighbor))
                    pq.sort()
                    
        return sequence