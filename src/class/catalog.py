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

    def search_content(self, name: str) -> MediaContent:
        """Busca una contenido por su título"""
        
