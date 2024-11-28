from typing import List
from datetime import datetime

class MediaContent:
    def __init__(self, name: str, category: str, id: int, publish_date: datetime, type: str, cast: List[str] = [],) -> None:
        self.name = name
        self.category = category
        self.id = id
        self.watched_date = datetime.now()
        self._ratings = []       
        self.rating = None
        self.views = 0
        self.cast = cast
        self.publish_date = publish_date
        self.type = type

    def __lt__(self, other) -> bool:
        """Sobrecarga del operador < usando views como criterio"""
        if not isinstance(other, MediaContent):
            return NotImplemented
        return self.views < other.views

    def __gt__(self, other) -> bool:
        """Sobrecarga del operador > usando views como criterio"""
        if not isinstance(other, MediaContent):
            return NotImplemented
        return self.views > other.views

    def __eq__(self, other) -> bool:
        """Sobrecarga del operador == usando name o id como criterio"""
        if not isinstance(other, MediaContent):
            return NotImplemented
        return self.name == other.name or self.id == other.id
    
    def add_view(self) -> None:
        """Añade una vista al contenido"""
        self.views += 1
    
    def get_views(self) -> int:
        """Retorna el número de vistas del contenido"""
        return self.views
    
    def add_rating(self, score: float) -> None:
        """Añade una nueva puntuación y actualiza el rating promedio"""
        if 0 <= score <= 5: 
            self.ratings.append(score)
            self.rating = sum(self.ratings) / len(self.ratings)

class Movie(MediaContent):
    def __init__(self, name: str, category: str, duration: int, id: int, cast: List[str], publish_date: datetime) -> None:
        super().__init__(name, category, id, publish_date, type="movie", cast=cast)
        self.duration = duration
        

class Episode:
    def __init__(self, name: str, duration: int, episode_number: int,  ) -> None:
        self.name = name
        self.duration = duration
        self.episode_number = episode_number
        self.watched_date = None

class Series(MediaContent):
    def __init__(self, name: str, category: str, id: int, cast: List[str], publish_date: datetime) -> None:
        super().__init__(name, category, id, publish_date, type="series", cast=cast)
        self.seasons = []  # Matriz donde el índice es (temporada - 1)
    
    def add_season(self, episodes: List[Episode]) -> None:
        """Añade una nueva temporada con sus episodios"""
        self.seasons.append(episodes)
    
    def get_season(self, season_number: int) -> List[Episode]:
        """Obtiene los episodios de una temporada específica"""
        if 0 <= season_number - 1 < len(self.seasons):
            return self.seasons[season_number - 1]
        return []
    
    def add_episode(self, season_number: int, episode: Episode) -> None:
        """Añade un episodio a una temporada específica"""
        while len(self.seasons) < season_number:
            self.seasons.append([])
        self.seasons[season_number - 1].append(episode)
