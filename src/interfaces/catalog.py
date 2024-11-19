from media import Movie
from media import Serie
from typing import List
from media import MediaContent
from tads.linkedList import LinkedList
from tads.generalTree import GeneralTree
from tads.binarySearch import BinarySearchTree
from utils.catalogHelpers import sortContentByPreference

class Catalog:
    def __init__(self):
        self.movies = LinkedList()
        self.series = GeneralTree() #Punto 4 (arbol gral)
        self.most_popular = BinarySearchTree() #Arbol de busqueda
        self.most_popular_movie = BinarySearchTree() #Arbol de busqueda
        self.most_popular_series = BinarySearchTree() #Arbol de busqueda
        
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

    def set_series(self, series: List[Serie]) :  #Construimos el arbol general
        """Retorna una serie"""
        pass
    
    def set_movies(self, movies: List[Movie]) :
        """Retorna una película"""
        for movie in movies:
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
