from typing import List
from user import User

class Account:
    def __init__(self, username: str, password: str, profiles: List[User], id: int):
        self.username = username
        self.password = password
        self.profiles = profiles
        self.id = id
                              



