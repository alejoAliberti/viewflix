from typing import List
from user import User

class Account:
    def __init__(self, username: str, password: str, profiles: List[User], id: int):
        self.username = username
        self.password = password
        self.profiles = profiles
        self.id = id
                              
    def add_profile(self, profile: User) -> None:
        """Añade un nuevo perfil al usuario"""
        if len(self.profiles) < 5:  
            self.profiles.append(profile)
        else:
            raise ValueError("El usuario ya tiene 5 perfiles")


