from dataclasses import dataclass
from typing import List

@dataclass
class UserData:
    user_id: int
    username: str
    character_name: str
    roles: List[str]