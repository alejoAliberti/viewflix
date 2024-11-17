from media import Movie
from media import Serie
from typing import List
from media import MediaContent
from tads.linkedList import LinkedList
from tads.generalTree import GeneralTree
from tads.binarySearch import BinarySearchTree

class Catalog:
    def __init__(self):
        self.movies = LinkedList()
        self.series = GeneralTree() #Punto 4 (arbol gral)
        self.most_popular = BinarySearchTree()
        self.add_most_popular_movie = BinarySearchTree() #Arbol de busqueda
        self.add_most_popular_series = BinarySearchTree() #Arbol de busqueda
        
    def add_most_popular(self) -> None: #Funciones que agregan contenido a la lista de más populares
        """Añade un contenido a la lista de más populares"""
        pass
        
    def add_most_popular_movies(self) -> None:
        """Añade una película a la lista de más populares"""
        pass
        
    def add_most_popular_series(self) -> None:  
        """Añade una serie a la lista de más populares"""
        pass
        
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
        series = self.series.find_nodes_by_name(name=name)
        if series is not None:
            return series
        
        """Busca nodo por nombre en la lista enlazada"""
        movies = self.movies.search_by_name(name=name)
        if movies is not None:
            return movies
        return None 
    
    #TODO: Busqueda por preferencias, debemos mergear las listas series y movies, luego ordenar por rating y preferencias.
    

