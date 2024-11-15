from typing import List
from datetime import datetime

class MediaContent:
    def __init__(self, name: str, category: str, id: int) -> None:
        self.name = name
        self.category = category
        self.id = id
        self.watched_date = datetime.now()  # Fecha de visualización

class Movie(MediaContent):
    def __init__(self, name: str, category: str, duration: int, id: int) -> None:
        super().__init__(name, category, id)
        self.duration = duration
        self.type = "movie"

class Episode:
    def __init__(self, name: str, duration: int, episode_number: int) -> None:
        self.name = name
        self.duration = duration
        self.episode_number = episode_number
        self.watched_date = None

class Series(MediaContent):
    def __init__(self, name: str, category: str, id: int) -> None:
        super().__init__(name, category, id)
        self.type = "series" 
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
