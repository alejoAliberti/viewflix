from media import Movie
from media import Serie
from typing import List
from media import MediaContent
from tads.linkedList import LinkedList
from tads.generalTree import GeneralTree
from tads.binarySearch import BinarySearchTree
from utils.catalogHelpers import sortContentByPreference
from tads.generalTree import Node
from tads.recomendationsGraph import Graph

class Catalog:
    def __init__(self):
        self.movies = LinkedList()
        self.series = GeneralTree() #Punto 4 (arbol gral)
        self.most_popular = BinarySearchTree() #Arbol de busqueda
        self.most_popular_movie = BinarySearchTree() #Arbol de busqueda
        self.most_popular_series = BinarySearchTree() #Arbol de busqueda
        self.recommendations_graph = Graph()
        
    def add_most_popular(self) -> None: #Funciones que agregan contenido a la lista de más populares
        """Añade un contenido a la lista de más populares"""
        for movie in self.movies:
            self.most_popular_movie.insert(movie)
        for serie in self.series.bfs_traverse_with_depth(max_depth=1):
            self.most_popular_series.insert(serie)
        
    def add_most_popular_movies(self) -> None:
        """Añade una película a la lista de más populares"""
        for movie in self.movies:
            self.most_popular_movie.insert(movie)
        
    def add_most_popular_series(self) -> None:  
        """Añade una serie a la lista de más populares"""
        for serie in self.series.bfs_traverse_with_depth(max_depth=1):
            self.most_popular_series.insert(serie)

    def set_serie(self, serie: Serie) :  #Construimos el arbol general
        """Retorna una serie"""
        if self.series.is_empty():
            emptyNode = Node(serie)
            return self.series.add_root(emptyNode)
        else:
            self.series.add_child(self.series.root, serie)
            parent = self.series.find_node(serie)
            for season in serie.seasons:
                seasonNode = Node(season)
                self.series.add_child(parent, seasonNode)
                for episode in season.episodes:
                    episodeNode = Node(episode)
                    self.series.add_child(seasonNode, episodeNode)
    
    def set_movies(self, movie: Movie) :
        """Retorna una película"""
        self.movies.append(movie)

    def search_content(self, name: str, preferences: List[str] = None) -> MediaContent:
        """Busca un contenido por su título"""
        
        """Busca un nodo por su nombre en el arbol general"""
        result = []
        series = self.series.find_nodes_by_name(name=name)
        if series is not None:
            result.extend(series)
        
        """Busca nodo por nombre en la lista enlazada"""
        movies = self.movies.search_by_name(name=name)
        if movies is not None:
            result.extend(movies)
        
        if len(result) == 0:
            return None
        else:
            """Ordenamos el resultado por preferencias y rating"""
            return sortContentByPreference(result, preferences)
    
    def update_recommendations_graph(self):
        """Actualiza el grafo de recomendaciones basado en el contenido actual"""
        # Obtener todo el contenido
        all_content = []
        for movie in self.movies:
            all_content.append(movie)
        for serie in self.series.bfs_traverse():
            all_content.append(serie.data)
            
        # Crear conexiones entre contenido similar
        for i in range(len(all_content)):
            for j in range(i + 1, len(all_content)):
                similarity = self.recommendations_graph.calculate_similarity(
                    all_content[i], 
                    all_content[j]
                )
                if similarity > 0:
                    self.recommendations_graph.add_edge(
                        all_content[i],
                        all_content[j],
                        similarity
                    )    
    
    def get_recommendations(self, content, limit=5):
        """Obtiene recomendaciones para un contenido específico"""
        return self.recommendations_graph.get_recommendations(content, limit)       

