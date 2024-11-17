from typing import List
from user import User

class Account:
    def __init__(self, username: str, password: str, profiles: List[User], id: int):
        self.username = username
        self.password = password
        self.profiles = profiles
        self.id = id
        
    def validate_password(self, password: str) -> bool: #"validar contraseña"
        return self.password == password
        
    def add_profile(self, profile: User) -> None:
        if len(self.profiles) >= 5:  # Límite de perfiles
            raise ValueError("No se pueden agregar más perfiles")
        self.profiles.append(profile)
    
    def remove_profile(self, profile: User) -> None: #"eliminar perfil relacionado con el usuario"
        self.profiles.remove(profile)
        
    def change_password(self, old_password: str, new_password: str) -> bool:    #"cambiar contraseña"
        if self.password == old_password:
            self.password = new_password
            return True
        return False

    
    def get_profile_by_name(self, name: str) -> User: #"obtener perfil por nombre"
        for profile in self.profiles:
            if profile.name == name: 
                return profile
        raise ValueError("Perfil no encontrado")

    def get_profile_by_id(self, profile_id: int) -> User: #"obtener perfil por id"
        for profile in self.profiles:
            if profile.id == profile_id: 
                return profile
        raise ValueError("Perfil no encontrado")
