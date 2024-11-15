from typing import List, Dict, Any
from media import MediaContent

class User:
    def __init__(self, favorites: List[MediaContent], name: str, age: int, preferences: Dict[str, Any]):
        self.favorites = favorites
        self.name = name
        self.age = age
        self.preferences = preferences
        self.history: List[MediaContent] = []  # Inicializamos el historial vacío
    
    def add_to_history(self, content: MediaContent) -> None:
        """Añade una película o serie al historial del usuario"""
        self.history.append(content)
    
    def get_history(self) -> List[MediaContent]:
        """Retorna el historial completo ordenado por fecha de visualización"""
        return list(reversed(self.history))  # Lo más reciente primero
    
    def add_to_favorites(self, content: MediaContent) -> bool: 
        """Añade una película o serie a favoritos"""
        if content.type == "movie":
            if content not in self.favorites["movies"]:
                self.favorites["movies"].append(content)
                return True
        elif content.type == "series":
            if content not in self.favorites["series"]:
                self.favorites["series"].append(content)
                return True
        return False
    
    def remove_from_favorites(self, content: MediaContent) -> bool:
        """Elimina una película o serie de favoritos"""
        if content.type == "movie":
            if content in self.favorites["movies"]:
                self.favorites["movies"].remove(content)
                return True
        elif content.type == "series":
            if content in self.favorites["series"]:
                self.favorites["series"].remove(content)
                return True
        return False
    
    def get_favorites(self, content_type: str = None) -> Dict[str, List[MediaContent]]:
        """
        Retorna los favoritos. Si content_type es especificado ('movie' o 'series'),
        retorna solo ese tipo de contenido
        """
        if content_type:
            return {content_type: self.favorites[content_type]}
        return self.favorites
    
    def is_favorite(self, content: MediaContent) -> bool:
        """Verifica si un contenido está en favoritos"""
        return content in self.favorites[content.type + "s"]