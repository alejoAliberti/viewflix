from movie import Movie
from serie import Serie
from typing import List
from media import MediaContent

class Catalog:
    def __init__(self, movies: List[Movie]):
        self.movies = movies
        self.series = None #punto 4 (arbol gral)
        self.most_popular = None
        self.add_most_popular_movie = None
        self.add_most_popular_series = None
        
    def add_most_popular(self, content: MediaContent) -> None: #funciones que agregan contenido a la lista de más populares
        """Añade un contenido a la lista de más populares"""
        self.most_popular.append(content)
        
    def add_most_popular_movies(self, movies: List[Movie]) -> None:
        """Añade una película a la lista de más populares"""
        self.most_popular.append(movies)
        
    def add_most_popular_series(self, series: List[Serie]) -> None:  
        """Añade una serie a la lista de más populares"""
        self.most_popular.append(series)
        
    def set_series(self, series: List[Serie]) :  #construimos el arbol general
        """Retorna una serie"""
        return self.series[series]
    
    def set_movies(self, movies: List[Movie]) :
        """Retorna una película"""
        return self.movies[movies]