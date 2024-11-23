from typing import List, Dict, Any
from media import MediaContent
from tads.linkedList import LinkedList
from tads.stack import Stack
from tads.maxHeap import MaxHeap

class User:
    def __init__(self, name: str, age: int, preferences: List[str]):
        self.favorites = LinkedList()
        self.name = name
        self.age = age
        self.preferences = preferences #['drama', 'action', 'terror']
        self.history = Stack()  # Inicializamos el historial vacío
        self.watchlist = MaxHeap()

    def add_preference(self, preference: str) -> None:
        """Añade una preferencia al usuario"""
        self.preferences.append(preference)
    
    def add_to_history(self, content: MediaContent) -> None:
        """Añade una película o serie al historial del usuario"""
        self.history.push(content)
    def get_history(self) -> List[MediaContent]:
        """Retorna el historial completo ordenado por fecha de visualización"""
        return self.history.items  # Lo más reciente primero
    
    def clear_history(self) -> None:
        """Elimina todos los elementos del historial"""
        self.history.clear()

    def add_to_favorites(self, content: MediaContent) -> bool: 
        """Añade una película o serie a favoritos"""
        if self.favorites.search(content):
            raise ValueError(f"El contenido '{content}' ya está en la lista de favoritos.")
        
        self.favorites.append(content)
        return True

    def remove_from_favorites(self, content: MediaContent) -> bool:
        """Elimina una película o serie de favoritos"""
        return self.favorites.delete(content)

    def get_favorites(self, content_type: str = None) -> Dict[str, List[MediaContent]]:
        """
        Retorna los favoritos. Si content_type es especificado ('movie' o 'serie'),
        retorna solo ese tipo de contenido
        """
        all_favorites = self.favorites.get_all()
        
        if content_type:
            filtered_content = [content for content in all_favorites if content.type == content_type]
            return {content_type: filtered_content}
        
        return {
            "movie": [content for content in all_favorites if content.type == "movie"],
            "serie": [content for content in all_favorites if content.type == "serie"]
        }

    def is_favorite(self, content: MediaContent) -> bool:
        """Verifica si un contenido está en favoritos"""
        return self.favorites.search(content)
    
    def set_watchlist(self, content: MediaContent):
        """Agregamos un item a la watchlist"""""
        return self.watchlist.insert(content, content.views)
    

        

