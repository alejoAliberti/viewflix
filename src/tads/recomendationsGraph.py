class Edge:
    def __init__(self, dest, weight=1.0):
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self):
        self.vertices = {}  # Diccionario de {contenido: [aristas]}
        
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