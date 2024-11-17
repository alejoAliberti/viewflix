from typing import List
from user import User

class Account:
    def __init__(self, username: str, password: str, profiles: List[User], id: int):
        self.username = username
        self.password = password
        self.profiles = profiles
        self.id = id
        
    def add_profile(self, profile: User) -> None:  #"agregar perfil relacionado con el usuario"
        self.profiles.append(profile) 
    
    def remove_profile(self, profile: User) -> None: #"eliminar perfil relacionado con el usuario"
        self.profiles.remove(profile)

