from typing import List
from datetime import datetime


class Movie:
    def __init__(self, publish_date: str, name: str, rating: float, category: str, cast: List[str], duration: int, id: int) -> None:
        self.publish_date = publish_date
        self.name = name
        self.rating = rating
        self.category = category
        self.cast = cast
        self.duration = duration
        self.id = id
        
        
class MediaContent:
    def __init__(self, name: str, category: str, id: int) -> None:
        self.name = name
        self.category = category
        self.id = id
        self.watched_date = datetime.now()  # Añadimos fecha de visualización

class Movie(MediaContent):
    def __init__(self, name: str, category: str, duration: int, id: int) -> None:
        super().__init__(name, category, id)
        self.duration = duration
        self.type = "movie"

class Series(MediaContent):
    def __init__(self, name: str, category: str, season: int, episode: int, id: int) -> None:
        super().__init__(name, category, id)
        self.season = season
        self.episode = episode
        self.type = "series"

