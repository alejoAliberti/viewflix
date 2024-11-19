def sortContentByPreference(content_list: List[MediaContent], preferences: List[str]) -> List[MediaContent]:
    """
    Ordena una lista de contenido basada en el rating y las preferencias del usuario.
    Los contenidos cuya categoría está en las preferencias tendrán prioridad.
    Para contenidos con la misma prioridad de preferencia, se ordena por rating.
    
    Args:
        content_list: Lista de contenido multimedia (películas o series)
        preferences: Lista de categorías preferidas por el usuario
        
    Returns:
        Lista ordenada de contenido
    """
    def get_content_priority(content: MediaContent) -> tuple:
        # Si la categoría está en preferencias, tendrá prioridad 1, sino 0
        preference_priority = 1 if content.category in preferences else 0
        # Usamos el rating como segundo criterio de ordenamiento
        # Si el rating es None, usamos -1 para que quede al final
        rating = content.rating if content.rating is not None else -1
        #Se compara el primer elemento de las tuplas.
        #Si el primer elemento es igual, se compara el segundo elemento.
        return (-preference_priority, -rating)  # Negativo para ordenar descendente
        
    return sorted(content_list, key=get_content_priority)
