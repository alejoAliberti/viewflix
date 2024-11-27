from typing import List
from user import User

class Account:
    def __init__(self, username: str, password: str, profiles: List[User], id: int):
        self.username = username
        self.password = password
        self.profiles = profiles
        self.id = id
                              
    def add_profile(self, profile: User):
        """Añade un nuevo perfil al usuario."""
        if len(self.profiles) < 5:  
            self.profiles.append(profile)
        else:
            raise ValueError("El usuario ya tiene 5 perfiles.")

    def get_username(self) -> str:
        """Obtiene el nombre de usuario."""
        return self.username

    def get_password(self) -> str:
        """Obtiene la contraseña (Nota: en producción, esto podría no ser seguro)."""
        return self.password

    def get_profiles(self) -> List[User]:
        """Obtiene la lista de perfiles del usuario."""
        return self.profiles

    def get_id(self) -> int:
        """Obtiene el ID de la cuenta."""
        return self.id

    def set_username(self, username: str):
        """Actualiza el nombre de usuario."""
        if username.strip():
            self.username = username
        else:
            raise ValueError("El nombre de usuario no puede estar vacío.")

    def set_password(self, password: str):
        """Actualiza la contraseña."""
        if len(password) >= 8:  # Ejemplo de validación simple
            self.password = password
        else:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

